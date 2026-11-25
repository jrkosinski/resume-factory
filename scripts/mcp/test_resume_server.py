#!/usr/bin/env python3
"""Checks on the resume-factory MCP server. Run: .venv/bin/python scripts/mcp/test_resume_server.py

The tool checks run against a small fixture repo in a temporary folder, so they pass whatever the real
repo holds; the render check uses the real format-guide template. The stdio check starts the real
server. --agent adds a real `ask` and a real `tailor` (on Haiku, about $0.50 together, in a temporary
TailoredResumes/ folder that is deleted afterwards).
"""

import asyncio
import os
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resume_server as rs  # noqa: E402
from mcp.server.mcpserver.exceptions import ToolError  # noqa: E402

TEMPLATE = rs.ROOT / "ResumeFormatGuides" / "John.R.Kosinski.docx"
EVIDENCE = """# Example Co / Platform Engineer

## Basic Info

**Company:** Example Co
**Dates:** 2020 – 2022
**Role / Title:** Platform Engineer

## Canonical Summary

Built the example platform on Kubernetes.

# Bullet Bank

## Backend Bullets

- Ran Kubernetes clusters in production.

## External Claim Safety Notes

### Avoid Unless Confirmed

- Exact uptime figures.
"""
RESUME = """# JOHN R. KOSINSKI

Platform Engineer • Architect
someone@example.com

---

## SUMMARY

Platform engineer with **production Kubernetes** experience.

## SYSTEMS OWNED / SELECTED EXPERIENCE

### Example Co - Platform Engineer

2020 – 2022

- Ran Kubernetes clusters in production
  - a sub-bullet

## Sourcing notes

- Review-only text that must stay out of the DOCX.
"""
FIXTURE = {
    "Positions/PlatformEngineer-ExampleCo/ExampleCo-Platform.md": EVIDENCE,
    "Positions/PlatformEngineer-ExampleCo/notes-without-headings.md": "just a scrap\n",
    "TailoredResumes/ExampleCo-PlatformEngineer/Resume.md": RESUME,
    "TailoredResumes/Dashed-Role/Resume.md": "# JOHN R. KOSINSKI\n\nA line — with an em-dash\n",
    ".env": "SECRET=not-a-real-secret\n",
    ".venv/lib/thing.py": "venv text\n",
    "Diagrams/arch.png": "binary stand-in\n",
}


def refused(call) -> bool:
    try:
        call()
    except ToolError:
        return True
    return False


def with_fixture(test):
    def run():
        real = rs.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            for rel, text in FIXTURE.items():
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_text(text)
            (root / "ResumeFormatGuides").mkdir()
            shutil.copy(TEMPLATE, root / "ResumeFormatGuides" / TEMPLATE.name)
            rs.ROOT = root
            try:
                test()
            finally:
                rs.ROOT = real
    run.__name__ = test.__name__
    return run


@with_fixture
def test_positions():
    listing = rs.positions()
    assert "PlatformEngineer-ExampleCo  [2020 – 2022; Platform Engineer]" in listing, listing
    assert "notes-without-headings" not in listing
    one = rs.positions("example co")
    assert "Built the example platform" in one and "Outline:" in one and "(line " in one
    assert "Exact uptime figures" in rs.positions("ExampleCo", "External Claim Safety Notes")
    assert "Ran Kubernetes clusters" in rs.positions(section="Bullet Bank")
    assert refused(lambda: rs.positions("Nobody Inc"))
    assert refused(lambda: rs.positions(section="No Such Section"))


@with_fixture
def test_resumes():
    assert "ExampleCo-PlatformEngineer: Resume.md" in rs.resumes()
    shown = rs.resumes("exampleco")
    assert "production Kubernetes" in shown and str(rs.ROOT / "TailoredResumes") in shown
    assert refused(lambda: rs.resumes("../Positions"))


@with_fixture
def test_search_and_read():
    assert "ExampleCo-Platform.md:" in rs.search("kubernetes clusters", "Positions")
    assert refused(lambda: rs.search("ab"))
    page = rs.read("Positions/PlatformEngineer-ExampleCo/ExampleCo-Platform.md", 1, 2)
    assert page.startswith("# Positions/PlatformEngineer-ExampleCo/ExampleCo-Platform.md")
    assert "pass start=3" in page


@with_fixture
def test_never_served():
    for path in [".env", "../passwords.txt", "/etc/passwd", ".venv/lib/thing.py", "Diagrams/arch.png", ".git/config"]:
        assert refused(lambda: rs.read(path)), path
    hits = rs.search("text")
    assert "venv text" not in hits and rs.search("SECRET").startswith("no hits")


@with_fixture
def test_render():
    out = rs.render("ExampleCo-PlatformEngineer")
    folder = rs.ROOT / "TailoredResumes" / "ExampleCo-PlatformEngineer"
    assert str(folder / "Resume.docx") in out
    from docx import Document
    from docx.oxml.ns import qn
    doc = Document(str(folder / "Resume.docx"))
    styles = [(p.style.name, p.text) for p in doc.paragraphs]
    assert ("Heading 1", "JOHN R. KOSINSKI") in styles
    assert ("Heading 3", "Example Co - Platform Engineer") in styles
    assert not any("Review-only" in t for _, t in styles), "sourcing notes leaked into the DOCX"
    bullets = [p for p in doc.paragraphs if p._p.pPr is not None and p._p.pPr.find(qn("w:numPr")) is not None]
    assert len(bullets) == 2
    bold = [r.text for p in doc.paragraphs for r in p.runs if r.bold]
    assert "production Kubernetes" in bold
    if shutil.which("libreoffice") or shutil.which("soffice"):
        assert (folder / "Resume.pdf").exists() and str(folder / "Resume.pdf") in out
    else:
        print("  (no LibreOffice, so no PDF check)")
    assert refused(lambda: rs.render("Dashed-Role"))
    assert not (rs.ROOT / "TailoredResumes" / "Dashed-Role" / "Resume.docx").exists()


def test_claude_bin():
    assert Path(rs.claude_bin()).exists(), rs.claude_bin()


def test_over_stdio():
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    async def tools():
        params = StdioServerParameters(command=sys.executable, args=[str(Path(rs.__file__))])
        async with stdio_client(params) as (r, w):
            async with ClientSession(r, w) as session:
                await session.initialize()
                listed = (await session.list_tools()).tools
                result = await session.call_tool("positions", {"name": "Hamza", "section": "Basic Info"})
                return sorted(t.name for t in listed), result

    names, result = asyncio.run(tools())
    assert names == ["ask", "positions", "read", "render", "resumes", "revise", "search", "tailor"], names
    assert not result.is_error and "Hamza" in result.content[0].text


def test_agent():
    """Slow and costs money, so it runs only with --agent."""
    if "--agent" not in sys.argv:
        print("skip test_agent (run with --agent)")
        return
    answer = rs.ask("Which position folders mention Kubernetes? Name them in one sentence.")
    assert "Hamza" in answer, answer
    folder = rs.out_dir() / "_McpTest-PlatformEngineer"
    rs.MODEL = "haiku"
    try:
        result = rs.tailor("Example Corp is hiring a Senior Platform Engineer: Kubernetes, AWS, TypeScript, "
                           "CI/CD, on-call ownership of payment services.", "resume",
                           "Keep it short: three positions in full.", folder.name)
        print(result[:1500])
        assert (folder / "Resume.md").exists() and (folder / "Posting.md").exists(), result
        assert (folder / "Resume.docx").exists() or "NOT RENDERED" in result, result
    finally:
        shutil.rmtree(folder, ignore_errors=True)


if __name__ == "__main__":
    failed = 0
    for name, test in [(n, f) for n, f in globals().items() if n.startswith("test_")]:
        try:
            test()
            print(f"PASS {name}")
        except AssertionError as error:
            failed += 1
            print(f"FAIL {name}: {error}")
    sys.exit(1 if failed else 0)
