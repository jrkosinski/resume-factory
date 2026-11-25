# scripts

The repo's only code: a renderer that turns a tailored draft's Markdown into DOCX and PDF, and an MCP
server that lets an agent in any other repo use the whole factory.

| Folder | What lives there | Run or import? |
| --- | --- | --- |
| `tools/` | `render_resume.py`, Markdown to DOCX and PDF | Run by hand, or imported by the server |
| `mcp/` | The repo as an MCP server for local agents | Started by the agent |

Run everything from the repo root, so that relative paths resolve.

## Setup

The server needs the MCP Python SDK 2.x, which the system Python here doesn't have (it has 1.x, which
other things may rely on), so the repo carries its own virtualenv. `.venv/` is gitignored; to rebuild it:

```
python3 -m venv .venv
.venv/bin/pip install "mcp>=2,<3" python-docx
```

PDFs need LibreOffice (`libreoffice` or `soffice` on the PATH), and `read` on a PDF needs `pdftotext`
(poppler-utils). `tailor`, `revise` and `ask` need the `claude` CLI: the server looks on the PATH, then
`$CLAUDE_BIN`, then the newest copy the VS Code extension installed.

## tools/

- `render_resume.py`: renders a folder's `Resume*.md` and `CoverLetter*.md` into `.docx` and `.pdf`
  beside them, with `ResumeFormatGuides/John.R.Kosinski.docx` as the style source and the style mapping
  the `tailor-resume` skill describes. The `## Sourcing notes` section and everything after it stays
  out of the DOCX. It refuses a file holding an em-dash, since CLAUDE.md forbids them, and names the
  lines. The Markdown shape it reads is in its docstring; every draft in `TailoredResumes/` already
  follows it. `python3 scripts/tools/render_resume.py TailoredResumes/<Folder>` (`--no-pdf` to skip
  LibreOffice). It replaces the per-job `build_resume.py` scripts the skill used to have Claude write.

## mcp/

- `resume_server.py`: the repo as an MCP server, `resume-factory`, over stdio, so it is never on the
  network. Eight tools:

  | Tool | What it does | Writes? |
  | --- | --- | --- |
  | `positions` | Lists past positions; one position's Basic Info, Canonical Summary and outline; or one section (`Bullet Bank`, `External Claim Safety Notes`, ...) across positions | No |
  | `resumes` | Lists `TailoredResumes/`; one folder's absolute file paths and Markdown drafts | No |
  | `search` | Phrase search over the repo's text, file:line hits | No |
  | `read` | One file with line numbers; PDFs and DOCX come as text | No |
  | `tailor` | Posting in; resume, cover letter or both out (Markdown, DOCX, PDF), via the `tailor-resume` workflow | `TailoredResumes/` only |
  | `revise` | Changes an existing draft as asked and re-renders | `TailoredResumes/` only |
  | `render` | Rebuilds DOCX and PDF after a hand edit to the Markdown | `TailoredResumes/` only |
  | `ask` | A question that needs judgment, answered by an agent reading the evidence bank | No |

  `tailor`, `revise` and `ask` run Claude Code headless in this repo (`claude -p`), with CLAUDE.md, the
  skills and the evidence bank. What that agent can touch is set on its command line, not by its
  prompt: Read, Glob and Grep only inside this repo, Write and Edit only under `TailoredResumes/` (and
  only for `tailor` and `revise`), and no shell, no web and no MCP servers. Job postings are
  third-party text, so a posting that carries instructions can't make it read your other files or run
  anything. The agent writes Markdown only; the server renders it and saves the posting as
  `Posting.md` in the folder, so `revise` can see what the draft was for.
  `tailor` and `revise` run on Opus (set `RESUME_FACTORY_MODEL` in the server's env to change it);
  `ask` uses the account default. A `tailor` run takes several minutes.

  The server never serves `.env` files, `.git`, `.venv` or anything outside the repo. Binary files are
  refused except PDF and DOCX, whose text `read` extracts.

- `test_resume_server.py`: checks the tools against a fixture repo, the exclusions, a real render, the
  `claude` lookup and the stdio listing. `--agent` adds a real `ask` and a real `tailor` on Haiku into a
  throwaway folder (well under a dollar). `.venv/bin/python scripts/mcp/test_resume_server.py` prints
  PASS or FAIL per check.

- `resume.mcp.json`: the same server as an MCP config file, for a client that takes one
  (`claude --mcp-config scripts/mcp/resume.mcp.json`).

### Registered at user scope

It is registered in `~/.claude.json` at user scope, so every Claude Code session on this machine, in
any repo, has the `resume-factory` tools without per-repo config:

```
claude mcp add --scope user resume-factory -- \
  /home/blanta/NOWY/projects/resume-factory/.venv/bin/python \
  /home/blanta/NOWY/projects/resume-factory/scripts/mcp/resume_server.py
```

`claude mcp get resume-factory` shows it; `claude mcp remove --scope user resume-factory` undoes it.
If the repo moves, remove and add it again with the new paths. Sessions started before registration
need a restart to see it.
