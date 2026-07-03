# resume-factory

Personal archive and compiler system for tailoring John R. Kosinski's resume to
specific job applications. Not a code project — no source, no build, no tests.

## Structure

- `ResumeFormatGuides/` — the canonical resume template (`John_R_Kosinski.pdf` +
  `.docx`). Defines the target structure, section order, and tone for any generated
  resume: SUMMARY, CORE CAPABILITIES, SYSTEMS OWNED / SELECTED EXPERIENCE (per
  company, 3-6 bullets each), ADDITIONAL EXPERIENCE (compressed list), OPERATING
  PRINCIPLES, TOOLS & TECHNOLOGIES (SELECTED), AVAILABILITY, CITIZENSHIP.
- `OldResumes/` — prior resume versions, kept for historical reference only. Do not
  edit; do not treat as current.
- `Positions/<RoleTitle>-<Company>/` — one folder per **past** position or client
  engagement (these are jobs already held, not postings being applied to). Each
  holds one or more evidence-bank files plus supporting architecture diagrams
  (PNG).
  - Some positions split into a `Projects/<ProjectName>/` subfolder when the
    engagement covers multiple distinct systems (see `CTO-Hamza/Projects/`,
    `FoundingEngineer-StreamFinance/Projects/`), each with its own evidence-bank
    file and diagrams.
  - Some position folders currently contain only diagrams with no evidence-bank
    write-up yet (`FoundingArchitect-Budgie`, `FoundingArchitect-Quantgenie`) —
    treat these as incomplete, not as "nothing to report."
- `TailoredResumes/<Company>-<RoleTitle>/` — job-specific resume drafts generated
  by the `tailor-resume` skill. Doesn't exist until first use; created on demand.

## Evidence-bank file format

Every `.md`/`.txt` file under `Positions/` is **raw material, not a finished resume
section**. They consistently follow this shape (not every file has every section):

- Source Notes — what prior material this entry merges/replaces
- Basic Info — client, dates, role, stack, status
- Canonical Summary / Short Resume Summary Version / Compact version
- Primary Tags
- Context, Role and Ownership, technical architecture detail
- Bullet Bank — many pre-written bullet variants grouped by angle (general,
  backend, frontend, security, etc.)
- Best External Resume Versions — ready-to-use paragraph variants
- Strongest Resume Angles / Resume Compiler Guidance — which parts to emphasize
  per target-role archetype (e.g., "CTO roles," "Payments/Fintech roles,"
  "Blockchain roles")
- ATS / Keyword Bank
- External Claim Safety Notes — **Safe to Claim / Use With Care / Avoid Unless
  Confirmed** — governs what can be stated as fact externally
- Relative Positioning Against Other Projects — how this entry compares to other
  Positions entries for the same kind of role

## Rules when working in this repo

- Never copy a whole Bullet Bank into an output resume verbatim — select and adapt
  bullets to the target job.
- Never state anything from an entry's "Avoid Unless Confirmed" list as fact in
  resume output. Treat "Use With Care" items as needing qualified/softened
  phrasing.
- Never invent accomplishments, metrics, or technologies that aren't present in
  some evidence-bank file. If coverage for a target role is thin, say so rather
  than padding.
- Match new resume drafts to the structure and tone of
  `ResumeFormatGuides/John_R_Kosinski.pdf`.
- When adding a new position/evidence entry, follow the section template above so
  future compilation stays consistent.
- Some client names are intentionally anonymized in evidence files ("semi-private
  client," "Private Client"). Preserve that anonymization in output unless the
  source file itself uses the real name.
