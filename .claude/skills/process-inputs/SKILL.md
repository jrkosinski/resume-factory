---
name: process-inputs
description: Batch-process all job applications in the inputs/ folder. For each subfolder, reads the description (job posting) and instructions file, then generates a tailored resume, cover letter, or both as directed. Use when the user says "process inputs", "run inputs", or "handle the inputs folder".
---

# Process Inputs

Iterates every direct subfolder of `inputs/` and fulfills the deliverables called
for in each job's `instructions` file. Read `CLAUDE.md` at the repo root first if
it's not already in context.

## Steps

### 1. Discover subfolders

List `inputs/` non-recursively. Each subdirectory (e.g. `inputs/capital-one`,
`inputs/oracle-crypto`) is one job application. Collect the list; skip any
loose files at the top level of `inputs/`.

### 2. For each job folder, read inputs

- `inputs/<folder>/description` - the raw job posting text.
- `inputs/<folder>/instructions` - freeform directives from the user. Typical
  values:
  - `"just a resume, pdf format"` - resume only, all three formats.
  - `"resume and cover letter"` / `"both"` - resume + cover letter.
  - `"cover letter only"` - cover letter only.
  - Any qualifier like `"translate cover letter to polish"` - apply as a
    post-processing step on the relevant deliverable.
  Parse this loosely; the intent is always clear from a few keywords.

### 3. Extract company and role from the description

Read the first 10-20 lines of the description to identify:
- Company name (e.g. "Capital One")
- Role title (e.g. "Senior Distinguished Engineer")

Slugify both for the output folder: `TailoredResumes/<Company>-<RoleTitle>/`
where each word is Title-cased and joined with no spaces
(e.g. `TailoredResumes/CapitalOne-SeniorDistinguishedEngineer/`). Use the
`inputs/` subfolder name as a fallback slug if the description is ambiguous.

### 4. Resume (if instructed)

Follow the full `tailor-resume` workflow, steps 1-11, using the description
text as the job posting. Output to `TailoredResumes/<Company>-<RoleTitle>/`:
- `Resume.md` (draft + sourcing notes)
- `Resume.docx` (styled)
- `Resume.pdf` (final)

The tailor-resume steps are reproduced here for reference:

1. Re-read `ResumeFormatGuides/John_R_Kosinski.pdf` to confirm section order.
2. Extract domains and top 5-10 skills from the posting.
3. Survey every `Positions/` folder (Basic Info, Canonical Summary, Strongest
   Resume Angles).
4. Pick 3-5 positions for full "Systems Owned / Selected Experience" treatment;
   remainder go to "Additional Experience".
5. Pull and adapt 2-5 bullets per selected position from the matching angle
   subsections only. Apply External Claim Safety Notes strictly.
6. Rewrite SUMMARY; reorder CORE CAPABILITIES and TOOLS & TECHNOLOGIES by
   relevance.
7. Write `Resume.md` with a "Sourcing notes" appendix.
8. Check `OldResumes/` for sharper phrasing or concrete metrics for positions
   already in the lineup.
9. Generate `Resume.docx` via `python-docx` using
   `ResumeFormatGuides/John.R.Kosinski.docx` as the style source. Style map:
   Name → `Heading 1`, section headers → `Heading 2`, company/role →
   `Heading 3`, everything else → `normal`. Apply list numPr (numId=5, ilvl=0)
   to all bullet-point paragraphs using:
   ```python
   def bullet(doc, t):
       p = doc.add_paragraph(t, style='normal')
       pPr = p._p.get_or_add_pPr()
       numPr = OxmlElement('w:numPr')
       ilvl = OxmlElement('w:ilvl'); ilvl.set(qn('w:val'), '0')
       numId = OxmlElement('w:numId'); numId.set(qn('w:val'), '5')
       numPr.append(ilvl); numPr.append(numId)
       pPr.append(numPr)
       return p
   ```
10. Convert to PDF:
    ```
    libreoffice --headless --convert-to pdf "TailoredResumes/.../Resume.docx" --outdir "TailoredResumes/.../"
    ```
11. Confirm all three files exist before moving on.

### 5. Cover letter (if instructed)

Write a cover letter in `TailoredResumes/<Company>-<RoleTitle>/CoverLetter.md`
then generate `.docx` and `.pdf` alongside it.

**Content structure (4 paragraphs, ~300-400 words total):**

1. **Opening** - name the specific role and company; one confident sentence on
   why this is a natural fit. No generic opener ("I am writing to apply...").
2. **Why this company/role** - 2-3 sentences grounded in the posting's stated
   mission, domain, or technical problem. Connect it to something real in
   John's background (not fabricated).
3. **What I bring** - 2-3 sentences pulling the 2-3 strongest, most relevant
   accomplishments from the evidence bank (same safety rules as resume: no
   "Avoid Unless Confirmed" items, "Use With Care" items qualified).
4. **Closing** - express interest in a conversation; keep it short and direct.

**Header block** (before the paragraphs):
```
John R. Kosinski
john.kosinski@toptal.com

<Today's date>

Hiring Manager
<Company Name>
```

**DOCX generation** - use `python-docx`. Load
`ResumeFormatGuides/John.R.Kosinski.docx` as the style source, clear its body,
then write:
- Name line → `Heading 1`
- Email, date, salutation, company → `normal`
- Each paragraph → `normal`
- Closing ("Sincerely," / name) → `normal`

No bullets in a cover letter. Run `pip install python-docx --break-system-packages`
if needed.

**PDF conversion:**
```
libreoffice --headless --convert-to pdf "TailoredResumes/.../CoverLetter.docx" --outdir "TailoredResumes/.../"
```

### 6. Special post-processing

If `instructions` contains a translation directive (e.g. "translate cover
letter to polish"), after the cover letter is finalized:
- Translate the full cover letter text into the target language.
- Write it to `CoverLetter_<Language>.md` / `.docx` / `.pdf` in the same folder.
- Use native script and spelling conventions for the target language.

### 7. Progress reporting

After finishing each job folder, print a one-line status:
```
✓ <folder>  →  <files produced>
```
e.g. `✓ capital-one  →  Resume.md, Resume.docx, Resume.pdf`

After all folders are processed, print a summary table of every output file
produced so the user knows exactly what to review.

## Hard rules (apply to all output)

- **Em-dashes are forbidden** everywhere: summaries, bullets, cover letter
  paragraphs, DOCX strings. Use a comma, colon, semicolon, or rewrite.
- Never invent accomplishments, employers, metrics, or technologies not in an
  evidence-bank file.
- Never promote an "Avoid Unless Confirmed" item to a stated fact.
- Never copy an entire Bullet Bank verbatim.
- If the evidence bank is thin for a target role, say so in the sourcing notes
  rather than padding.
- If a job folder is missing `description` or `instructions`, skip it and warn
  the user rather than guessing.
