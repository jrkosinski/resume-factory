#!/usr/bin/env python3
"""Render a tailored resume or cover letter from its Markdown into DOCX and PDF.

Usage: python3 scripts/tools/render_resume.py TailoredResumes/<Folder> [more folders or .md files] [--no-pdf]

A folder renders every Resume*.md and CoverLetter*.md in it; Resume.md becomes Resume.docx and
Resume.pdf beside it. The DOCX takes its styles from ResumeFormatGuides/John.R.Kosinski.docx (the
same mapping the tailor-resume skill describes), and LibreOffice makes the PDF. A file holding an
em-dash is refused, since CLAUDE.md forbids them in all output.

The Markdown shape it reads, which every draft in TailoredResumes/ already follows:

    # JOHN R. KOSINSKI              -> Heading 1
    ## SUMMARY                      -> Heading 2 (section)
    ### Hamza - CTO and Co-Founder  -> Heading 3 (company / role); so is a line that is all **bold**
    - a bullet                      -> bullet (indent two spaces for a sub-bullet)
    any other line                  -> its own paragraph; **bold** and *italic* carry over
    ---                             -> dropped (a visual separator in the Markdown only)
    ## Sourcing notes               -> it and everything after it stay out of the DOCX

In a cover letter, a blank line becomes an empty paragraph, the first line becomes Heading 1 when it
isn't a heading already, and a leading "# Cover Letter: ..." title is dropped.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "ResumeFormatGuides" / "John.R.Kosinski.docx"
BULLET_NUM_ID = "5"  # the template's bullet list, as the tailor-resume skill uses
FORBIDDEN = {"—": "em-dash", "―": "horizontal bar"}
STOP = re.compile(r"^sourcing", re.I)  # the review-only appendix
INLINE = re.compile(r"(\*\*[^*]+\*\*|__[^_]+__|\*[^*\s][^*]*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")
ESCAPE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|])")


class RenderError(Exception):
    pass


def dashes(text: str) -> list[str]:
    """Every line holding a forbidden dash, as 'line N: text'."""
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        for char, name in FORBIDDEN.items():
            if char in line:
                found.append(f"line {number} ({name}): {line.strip()[:120]}")
                break
    return found


def plain(text: str) -> str:
    """Inline Markdown stripped to its text, for headings."""
    text = re.sub(r"\*\*([^*]+)\*\*|__([^_]+)__", lambda m: m.group(1) or m.group(2), text)
    text = re.sub(r"\*([^*\s][^*]*)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return ESCAPE.sub(r"\1", text).strip()


def add_runs(paragraph, text: str) -> None:
    position = 0
    for match in INLINE.finditer(text):
        if match.start() > position:
            paragraph.add_run(ESCAPE.sub(r"\1", text[position:match.start()]))
        token = match.group(0)
        if token[:2] in ("**", "__"):
            paragraph.add_run(token[2:-2]).bold = True
        elif token[0] == "*":
            paragraph.add_run(token[1:-1]).italic = True
        elif token[0] == "`":
            paragraph.add_run(token[1:-1])
        else:
            paragraph.add_run(re.match(r"\[([^\]]+)\]", token).group(1))
        position = match.end()
    if position < len(text):
        paragraph.add_run(ESCAPE.sub(r"\1", text[position:]))


def bullet(doc, text: str, level: int = 0) -> None:
    paragraph = doc.add_paragraph(style="normal")
    add_runs(paragraph, text)
    num_pr = OxmlElement("w:numPr")
    ilvl = OxmlElement("w:ilvl")
    ilvl.set(qn("w:val"), str(level))
    num_id = OxmlElement("w:numId")
    num_id.set(qn("w:val"), BULLET_NUM_ID)
    num_pr.append(ilvl)
    num_pr.append(num_id)
    paragraph._p.get_or_add_pPr().append(num_pr)


def build_docx(markdown: str, letter: bool, template: Path) -> Document:
    doc = Document(str(template))
    body = doc.element.body
    for element in list(body):
        if element.tag != qn("w:sectPr"):
            body.remove(element)

    started = False
    blank = False
    for raw in markdown.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading and STOP.match(plain(heading.group(2))):
            break
        if not stripped or re.fullmatch(r"[-*_]{3,}", stripped):
            blank = blank or (letter and started and not stripped)
            continue
        if letter and blank:
            doc.add_paragraph(style="normal")
        blank = False

        if heading:
            text = plain(heading.group(2))
            if letter and not started and text.lower().startswith("cover letter"):
                continue
            level = min(len(heading.group(1)), 4)
            doc.add_paragraph(text, style=f"Heading {level}")
        elif not letter and re.fullmatch(r"\*\*[^*]+\*\*", stripped):
            # Older drafts write "**Company - Role**" on its own line for a company header.
            doc.add_paragraph(plain(stripped), style="Heading 3")
        elif re.match(r"^\s*[-*•]\s+", line):
            indent = len(line) - len(line.lstrip())
            bullet(doc, re.sub(r"^\s*[-*•]\s+", "", line), 1 if indent >= 2 else 0)
        elif letter and not started:
            doc.add_paragraph(plain(stripped), style="Heading 1")
        else:
            paragraph = doc.add_paragraph(style="normal")
            add_runs(paragraph, stripped)
        started = True

    if not started:
        raise RenderError("nothing to render before the Sourcing notes")
    return doc


def to_pdf(docx: Path) -> Path:
    office = shutil.which("libreoffice") or shutil.which("soffice")
    if not office:
        raise RenderError("LibreOffice isn't installed, so no PDF; the DOCX is written")
    pdf = docx.with_suffix(".pdf")
    pdf.unlink(missing_ok=True)
    # A throwaway profile, so an open LibreOffice window can't swallow the conversion.
    with tempfile.TemporaryDirectory() as profile:
        done = subprocess.run(
            [office, f"-env:UserInstallation={Path(profile).as_uri()}", "--headless",
             "--convert-to", "pdf", "--outdir", str(docx.parent), str(docx)],
            capture_output=True, text=True, timeout=180)
    if not pdf.exists():
        raise RenderError(f"LibreOffice made no PDF: {(done.stderr or done.stdout).strip()[:300]}")
    return pdf


def render(md: Path, pdf: bool = True, template: Path = TEMPLATE) -> list[Path]:
    """Render one Markdown file; returns the files written."""
    text = md.read_text()
    found = dashes(text)
    if found:
        raise RenderError(f"{md.name} has em-dashes, which CLAUDE.md forbids:\n" + "\n".join(found))
    docx = md.with_suffix(".docx")
    build_docx(text, "cover" in md.stem.lower(), template).save(str(docx))
    return [docx] + ([to_pdf(docx)] if pdf else [])


def drafts(folder: Path) -> list[Path]:
    return sorted(folder.glob("Resume*.md")) + sorted(folder.glob("CoverLetter*.md"))


def render_folder(folder: Path, pdf: bool = True, template: Path = TEMPLATE) -> list[Path]:
    """Render every draft in a folder. Checks them all before writing any."""
    found = drafts(folder)
    if not found:
        raise RenderError(f"no Resume*.md or CoverLetter*.md in {folder}")
    problems = [f"{md.name}: {line}" for md in found for line in dashes(md.read_text())]
    if problems:
        raise RenderError("em-dashes, which CLAUDE.md forbids; replace them and render again:\n"
                          + "\n".join(problems))
    written = []
    for md in found:
        written += render(md, pdf, template)
    return written


def main(argv: list[str]) -> int:
    pdf = "--no-pdf" not in argv
    targets = [Path(a) for a in argv if not a.startswith("--")]
    if not targets:
        print(__doc__.split("\n\n")[1])
        return 2
    failed = 0
    for target in targets:
        try:
            written = render_folder(target, pdf) if target.is_dir() else render(target, pdf)
            for path in written:
                print(f"wrote {path}")
        except (RenderError, OSError) as error:
            failed += 1
            print(f"FAILED {target}: {error}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
