---
name: tailor-resume
description: Compile a job-specific resume draft for John R. Kosinski from the Positions/ evidence bank. Use when the user pastes a job posting or description, names a target company/role and asks for a resume, or asks to tailor/update/refresh a resume for a specific application. Not for editing the master format guide itself.
---

# Tailor Resume

Compiles a job-specific resume draft by selecting and adapting content from the
`Positions/` evidence bank, matching the structure of
`ResumeFormatGuides/John_R_Kosinski.pdf`. Read `CLAUDE.md` at the repo root first
if it's not already in context — it defines the evidence-bank format and the
non-negotiable safety rules this skill depends on.

## Input

The argument passed to this skill is the job posting or a description of the
target role (pasted text, a path to a saved posting, or just "Company, Role
Title" if that's all the user has). If no argument was given and the user hasn't
pasted a posting in the conversation, ask for it before proceeding — don't guess
at what a company wants.

## Steps

1. **Re-read the format guide fresh.** Read `ResumeFormatGuides/John_R_Kosinski.pdf`
   even if you've read it before in this conversation — confirm current section
   order and headers: SUMMARY, CORE CAPABILITIES, SYSTEMS OWNED / SELECTED
   EXPERIENCE, ADDITIONAL EXPERIENCE, OPERATING PRINCIPLES, TOOLS & TECHNOLOGIES
   (SELECTED), AVAILABILITY, CITIZENSHIP.

2. **Extract signal from the posting.** Identify: target company, role title, and
   which domain(s) it draws on — System Architecture, DevOps, AI, fintech,
   trading, blockchain, and/or general backend are the recurring buckets across
   this evidence bank. Most postings mix 2-3 of these (e.g. "banking + DevOps").
   Note the 5-10 concrete skills/technologies the posting emphasizes most.

3. **Survey every position.** For each `Positions/<RoleTitle>-<Company>/` folder
   (and each file under any `Projects/` subfolder), read at least the Basic Info,
   Canonical Summary, and Strongest Resume Angles / Resume Compiler Guidance
   sections. These are usually already broken out by domain (e.g. Hamza's guidance
   separately covers CTO/leadership, payments/fintech, blockchain, and
   e-commerce angles) — score relevance per domain, not just per position, since
   one position can contribute to a resume for more than one reason. Positions
   with only diagrams and no write-up (currently Budgie, Quantgenie) can only
   contribute what's visible in the diagrams — don't fabricate narrative for them.

4. **Pick the lineup.** Choose the 3-5 positions with the strongest combined
   relevance for full "Systems Owned / Selected Experience" treatment. Everything
   else goes into the compressed "Additional Experience" list, same as the format
   guide does with Morgan Stanley/Aquamonix/etc.

5. **Pull and adapt bullets.** A position earns its place by *any* matching
   domain, but the bullets you pull from it should be the ones matching the
   target domain mix specifically — not the whole Bullet Bank. Bullet Banks are
   usually pre-grouped by angle (e.g. "Backend / Cloud Bullets," "Security /
   Operations Bullets," "Trading / Risk-Control Bullets") — pull from the
   subsections that match, and skip the ones that don't just because they're in
   the same file. For a banking + DevOps posting, that means pulling
   fintech-flavored bullets from one position and infra/CI-CD/Kubernetes-flavored
   bullets from another (or the same) position, not the position's full bullet
   bank. Draw 2-5 bullets per selected position, reworded toward the target
   posting's language where honest to do so. Apply the External Claim Safety
   Notes:
   - "Safe to Claim" — usable as stated.
   - "Use With Care" — soften/qualify, don't state as a flat fact.
   - "Avoid Unless Confirmed" — do not use, period.

6. **Rewrite Summary and reorder lists.** Adjust the SUMMARY paragraph and reorder
   CORE CAPABILITIES / TOOLS & TECHNOLOGIES so what the posting cares about most
   appears first. Don't invent capabilities that aren't backed by some evidence
   file. OPERATING PRINCIPLES and CITIZENSHIP normally carry over unchanged unless
   the user says otherwise.

7. **Write the draft** to
   `TailoredResumes/<Company>-<RoleTitle>/Resume.md` (create the folder). Use the
   exact section headers from step 1. Below the resume, add a short "Sourcing
   notes" section listing which `Positions/` files were used and anything you had
   to soften or omit for lack of evidence — this is for the user's review, not
   for the final resume.

8. **Hand off.** Tell the user the draft is ready for review at that path, and
   that turning it into the final PDF/DOCX still requires pasting it into the
   `ResumeFormatGuides` template — this skill doesn't touch the styled DOCX/PDF
   directly.

## Hard rules

- Never invent accomplishments, employers, metrics, or technologies not present
  in an evidence-bank file.
- Never promote an "Avoid Unless Confirmed" item to a stated fact.
- Never copy an entire Bullet Bank verbatim — a lineup of unselected, unadapted
  bullets is not a tailored resume.
- If the evidence bank has genuinely thin coverage for the target role, say so
  explicitly in the sourcing notes rather than padding the draft.
