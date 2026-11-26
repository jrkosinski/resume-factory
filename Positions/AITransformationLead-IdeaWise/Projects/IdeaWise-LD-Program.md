<!--
Source: compiled 2026-11-21, rewritten 2026-11-26 around the program as it ran. Sources: `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/Projects/KnowledgeReturn/` (README, History.md: the dated record from 28 September to 11 November 2026), `OKRs/S4-2026/L&D/`, and `Projects/old-versions/L&D/` (the original proposal, now under Earlier Design). John's own framing, 2026-11-26: a human-centric program and its governance, mostly organizational work (persuasion, planning, organizing), with a little coding.
Purpose: modular resume source file for the L and D program pillar of the IdeaWise engagement.
-->

# IdeaWise / Learning and Development / The Learning Grant Program and Knowledge Return

## Basic Info

**Client:** IdeaWise (EU-based, ~140 employees, active in Europe and China)
**Project:** The company's Learning and Development program, run as Knowledge Return: the Learning Grant Program (any employee can ask for protected work time and money to learn or experiment, and pays it back by teaching what they learned), the Knowledge Return Library where those lessons live, and the councils that govern it (the Light Council, then a Formal Council)
**Dates:** Proposal from mid-2026; Knowledge Return Library published September 2026; Light Council running from October 2026; Formal Council planned for late 2026
**Role:** Sole owner and designer; chair of the Light Council and of the planned Formal Council. Worked with Katya Dozhdikova on lessons from a prior failed attempt
**Status:** Library published; Learning Grant Program cleared by Legal, People and Culture, and Finance and open to requests; Light Council running; Formal Council designed.

## Canonical Summary

Designed and ran a human-centric Learning and Development program for a ~140-person company across Europe and China. Its core is a trade between the company and its people: any employee can ask for protected work time and money to learn something or run an experiment, and repays it by teaching the company what they learned, negative results included. Those lessons ("returns") go into the Knowledge Return Library. A small council decides the larger grants, with the applicant's squad leader brought in when hours come from their squad and Finance when money is involved; smaller grants are the squad leader's call. The program is a pull system: nothing is pushed on people, and the company sponsors the learning people choose to do.

Most of the work was organizational rather than technical. John designed the scheme and the governance, built the Light Council and chaired it, briefed squad leaders one by one, negotiated the time and money pool with the COO and Finance, took the scheme through data protection, People and Culture, local HR in Spain and China and German labor-law review, wrote the rules, FAQ and privacy notice, and presented it to the company. The little code in it is automation: a scheduled job that keeps the library's returns list current and announces new returns and grant requests to the team chat.

## Short Resume Summary Version

Designed and ran a human-centric Learning and Development program for an EU-based ~140-person company: any employee can ask for protected time and money to learn or experiment, and repays it by teaching what they learned. Built and chaired the council that grants it, negotiated the pool with the COO and Finance, cleared it through Legal, People and Culture and local HR in three countries, briefed squad leaders, and wrote the rules, FAQ and privacy notice.

## Compact Resume Version

Designed and ran a human-centric L and D program for an EU-based ~140-person company: learning grants of protected time and money for any employee, repaid by teaching what they learned, governed by a council John built and chaired, and cleared through Legal, People and Culture and Finance.

## Primary Tags

- Learning and Development
- Human-centric enablement
- Change management
- Organizational design
- Governance design
- Council and decision-rights design
- Stakeholder alignment
- Learning grants
- Peer teaching
- Knowledge sharing
- Pull-based learning culture
- Protected learning time
- Legal, privacy and labor-law clearance
- GDPR-aware program design
- Program documentation
- Confluence as documentation surface
- Light automation (GitHub Actions, team-chat notifications)

## Context, Role and Ownership

The client had already tried an AI L and D program, run by a consultancy. It did not catch on. Katya's diagnosis: disconnected from what people were actually doing, not tailored to skill levels, no process defined, a custom platform with mostly AI-generated material that was role-specific in name only. Tine's: the contractor was largely ignored, time was granted but not tied to real work, unused time was not tracked, and underlying disorganization compounded it. The lessons John drew: tie learning to real work, couple it closely to team leadership, account for the time, and don't hand the program's legitimacy to an outside contractor.

John's concrete responsibilities:

- **Designed the scheme.** Learning Grants for every employee; repayment by a teaching return, with a negative-result return when work stops early; a council threshold (a request goes to the council if it needs any money, more than 4 hours, or hours from more than one squad; below that the squad leader grants it); a turnaround ceiling of 10 calendar days; due dates that pause for absences; no overtime.
- **Built and chaired the Light Council.** Members John (chair), Katya, Pierre and Iren on every request, with the applicant's squad leader and Finance called in as needed and the COO above it with a veto. Its four-week record was designed to set the fixed criteria for the Formal Council that follows.
- **Planned the Formal Council.** At most five members on every request, John chairing without a vote, Legal and Finance as sign-offs who don't vote, stand-ins for single requests, a conflict-of-interest rule, a voting rule, and written decision criteria; a shortlist of twelve candidates.
- **Negotiated the pool.** 300 hours and 3,000 euros for the season, up to 500 euros per grant, agreed by the COO and Finance; Finance cleared grant money without a budget line.
- **Cleared it.** Data protection, People and Culture and local management reviewed the scheme; under German and EU law it needed no works council co-determination; local HR answered for Spain and China; John drafted the Learning Grants privacy notice, which data protection approved. Their conditions (rules in writing before the first request, private decisions on delivery, "Delivered" and "Not Delivered" in place of "paid back", no effect of a Not Delivered grant on reviews or pay) were written into the rules.
- **Brought people in.** One-on-one briefings for squad leaders; the KM Platform lead signed on as the flagship creator, his Sentry Auto-Fix pipeline becoming the first real return and a three-part technical video series; the program opened the company-wide presentation of 20 October 2026.
- **Wrote it down.** The Confluence doc set in space ANT: Rollout Plan and phase pages, Knowledge Return Library and Light Council user docs, Learning Grants for Everyone, How to Ask, the L and D FAQ, the privacy notice, the operating docs, and a glossary; Jira epics and the S4 2026 L and D OKRs.
- **The little coding.** The library itself is Confluence templates and labels: adding a return is a template pick, three tags and publish. John's View Stats job runs on GitHub Actions every 4 hours, regenerates the returns list, and posts each new return and grant request to the L and D channel on Mattermost, replacing a Confluence Automation rule that missed template-made labels.

## How It Works, Short Version

- **Phase 1, Knowledge Return Library:** where returns are published, as pages, videos or modules, with a page template, labels and a returns list kept current by the stats job.
- **Phase 2, the Light Council:** decides Learning Grant requests above the threshold for about four weeks and records every decision.
- **Phase 3, the Formal Council:** fixed membership, criteria and voting rules drawn from the Light Council's record.

## Bullet Bank

### General AI transformation, resume summary

- Designed and ran a human-centric learning program for an EU-based ~140-person company: protected time and money for any employee who wants to learn or experiment, repaid by teaching the company what they learned.
- Built the program's governance from scratch: a council with clear decision rights, a threshold below which squad leaders decide alone, a 10-day turnaround ceiling, and a plan for a permanent council drawn from the first council's record.
- Drew the design from a close read of a prior consultancy-run program that failed, tying learning to real work and team leadership instead.

### Head of L and D / Head of Enablement angle

- Replaced a failed top-down training program with a pull system: employees choose what to learn, the company sponsors it with protected time and a grant pool, and each grant is repaid with a teaching return to a shared library.
- Chaired the Light Council deciding Learning Grants, and planned the Formal Council that succeeds it (membership, voting, conflict-of-interest and decision criteria).
- Briefed squad leaders one on one and recruited the first flagship creator, whose production-automation work became the first return and a technical video series.

### People, legal and change management angle

- Took a learning-grant scheme through data protection, People and Culture, Finance and local HR in Germany, Spain and China, writing their conditions (privacy, absence, no effect on reviews or pay) into the rules and drafting the privacy notice data protection approved.
- Negotiated the season's grant pool of hours and money with the COO and Finance.

### Governance / operating model angle

- Designed decision rights for a company-wide grant scheme: who decides at which size, who is consulted, where the COO's veto sits, and how decisions are recorded so the first council's record becomes the next council's criteria.

### Light automation angle

- Automated the library's upkeep with a scheduled GitHub Actions job that regenerates the returns list and announces new returns and grant requests to the team chat.

## Best External Resume Versions

**Short block:**

> Designed and ran a human-centric learning program for an EU-based ~140-person company: any employee can ask for protected time and money to learn or experiment, and repays it by teaching what they learned. Built and chaired the council that decides the grants, negotiated the pool with the COO and Finance, cleared the scheme through Legal, People and Culture and local HR in three countries, and wrote the full documentation set.

**One-liner:**

> Designed and ran a learning-grant program and its governing council: protected time and money for any employee, repaid by teaching the company what they learned.

## External Claim Safety Notes

### Safe to Claim Now

- Sole owner and designer of the program as run through Knowledge Return and the Learning Grant Program.
- Chair of the Light Council; author of the Formal Council plan.
- Pool negotiated with the COO and Finance; scheme cleared by data protection, People and Culture, Finance and local HR; privacy notice approved.
- Squad leader briefings; flagship creator recruited; company presentation.
- Published Confluence doc set, Jira epics, S4 2026 OKRs.
- The View Stats job and its chat notifications.

### Use With Care / Qualify Internally

- Lead with the design, the council John built and chaired, and the change-management, legal and HR work. The program launched company-wide in October 2026 and is open to every employee.
- The Formal Council: John designed it; present as "designed the permanent council that succeeds it."
- Pool figures are internal; describe as "a season's pool of protected hours and grant money, negotiated with the COO and Finance."
- Case-study attribution (S and P Global, Moderna, PwC) is lesson-drawing, not replication.

### Avoid Unless Confirmed

- Naming the client (IdeaWise) or its people in external output.
- Inventing adoption, hours-saved or ROI figures.
- Presenting the superseded LMS, course catalogue or points scheme as built.

## Primary Stack

Confluence space `ANT` (templates, labels, page properties reports) as the library and documentation surface; Jira for epics and the council's work; GitHub Actions for the View Stats job; Mattermost webhooks for notifications; Oboard for OKRs.

## Earlier Design (Superseded)

John's original proposal (mid-2026) took a different route: a three-phase rollout from hand-picked external courses (Coursera, Udemy) with agent-validated certificate submission, to an internal LMS with internal content creation (Moodle, 360Learning and TalentLMS shortlisted), to an eventual fusion with a company knowledge base in the GitLab handbook style. Incentives were recognition, small rewards, points visible in reviews and protected time, weighted toward verified usage in real work. The principles carried over (make it easy, rewarding, paid as part of work and visibly backed by management; tie it to real work); the course catalogue, LMS and points scheme did not. Use this only as background on how the design evolved.

## Related Case Studies John Drew On

- **S and P Global (Spark AI Academy)**: foundational fluency for all plus role-specific journeys; C-suite completed training. Lesson: mandatory foundations work only when combined with role-specific, immediately applicable material and visible leadership participation.
- **Moderna**: universal proficiency, prompt competitions, Generative AI Champions, office hours, exec sponsorship. Lesson: training embedded inside broader change management.
- **Microsoft Copilot Expo**: three-week online expo, repeated across time zones, role-specific breakouts, badges and leaderboards, on-demand material. Lesson: peer leadership, role-specific content, gamification, and measuring depth of use.
- **Microsoft Copilot Champs**: peer champions given train-the-trainer sessions, reusable assets, community support, recognition. Lesson: super-users are not automatically good trainers; decentralize teaching but not completely.
- **PwC Singapore Digital Academy**: universal Digital Academy plus volunteer Digital Accelerators with protected time to build automation. Lesson: strongest precedent for the current plan.
- **GitLab Handbook-first**: handbook as source of truth, training built from it. 8,000-page handbook was too much. Lesson: documentation is not automatically good training.
- **Amazon Machine Learning University**: central experts build canonical courses. Lesson: central expert content for foundations and hard topics, peer content for applied internal experience.
