<!--
Source: compiled 2026-11-21, revised 2026-11-26 (John's assembled factory, from `Projects/CodeFactory/History.md` and `Projects/AgenticWorkflow/History.md`), from `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/Projects/CodeFactory/`, meeting summaries in `/Meetings/2026-11/` referenced by that folder, OKR documents, and the KM Platform / DF Platform / AI Core Services dossiers in `CodeFactory/TeamDossier/`.
Purpose: modular resume source file for the Code Factory pillar of the IdeaWise engagement.
-->

# IdeaWise / Code Factory / Ticket-to-Production Agent Pipeline

## Basic Info

**Client:** IdeaWise (EU-based, ~140 employees)
**Project:** Code Factory (previously "Code Pipeline"; renamed on 16 November 2026, John proposed, André agreed)
**Dates:** Active ownership from approximately mid-2026 through engagement end
**Role:** Production-side owner in the three-person Idea Engine work group (André: strategy and ideation side; Iren: research side; John: production side). Assembled and ran his own working factory from parts built by different departments, then combined it with André's
**Status:** John's assembled factory running end to end from 17 November 2026 (ticket to merged pull request, with AI review and auto-merge). André's private factory chosen 16 November as the proof-of-concept vehicle; on 18 November John began combining the two; on 25 November André moved to one company factory with two pipelines (Idea Engine and KaufMich). Minimum version of research, factory and self-improvement targeted for Q1 2027

## Canonical Summary

Owned the production side of IdeaWise's end-to-end "lights-off" Code Factory: an agent-driven pipeline that turns a Jira ticket into merged, deployed, production-watched software without human keyboard time between the specification and the production gate. The factory is one half of the client's agentic-company mandate (IDW-105: 100% of code AI-drafted; IDW-106: 3x spec-to-production throughput); Personal Agents are the other half. Scope covers 13 stages from a ready-ticket gate through staging, production release, progressive rollout, production watch and the Sentry-based fix loop. Dispatched agents debate each ticket over several rounds (data, architecture, security, growth, Scrum methodology, software craftsmanship among them) until the specification and plan are sound; development goes through PR review into a lab environment where generated test personas exercise features; only bug-free work reaches production.

John's ownership covers the production path from ticket to release, the 13-stage pipeline map that scored the client's existing capability against the target, the team-by-team state matrix (KM Platform, Sys Admin, DF Platform, AI Core Services, KM Acquisition, KM Monetization and Meta Search), the company-wide adoption plan, and the review and selection work between André's proof-of-concept factory and the IdeaWise-grown factory that would succeed it.

He also built one. Starting 17 November 2026, John assembled a working factory from parts different departments had built separately (KM Platform's readiness scorer, `/develop` workflow and `ai-standards` skills) and added the parts nobody had: a launcher that runs the agent unattended in its own worktree and branch, a run report checked against an independent test rerun, CI with up to two agent fix rounds and automatic revert on red, an independent AI review on every pull request, and auto-merge only on an approving review with green checks. The factory can work on its own code, with its own guards protected from automatic merge. On 18 November he began combining it with André's factory, aiming at one canonical factory for company-wide use.

## Short Resume Summary Version

Production-side owner of IdeaWise's end-to-end agent-driven coding factory: Jira ticket to production with multi-agent debate on specification and architecture, agent-driven development through PR review, lab environments with generated test personas, progressive release with automatic rollback, production watch per release, and a Sentry-based fix loop. Delivered the 13-stage pipeline map, the team-by-team state matrix, the adoption plan, and the review that chose the proof-of-concept vehicle. Assembled a working factory from parts built across departments, adding the unattended launcher, CI fix loop, AI pull-request review and auto-merge gate that joined them into one ticket-to-merge line.

## Compact Resume Version

Owned the production side of an end-to-end agent-driven ticket-to-production coding factory for an EU-based company (IDW-105: 100% of code AI-drafted; IDW-106: 3x spec-to-production throughput). Mapped 13 stages from ready-ticket gate to the fix loop across five platform teams, assembled a working factory from parts built by different departments, delivered the adoption plan, and ran the review that selected the proof-of-concept vehicle.

## Primary Tags

- Agentic engineering
- AI agents
- AI-assisted software development
- Autonomous software delivery
- Ticket-to-production pipeline
- Multi-agent systems
- Agent debate and specification
- Agent-driven PR review
- Generated test personas
- CI/CD with AI gates
- Shadow-mode release
- Sentry Auto-Fix
- SonarQube AI fixes
- Progressive release
- Automatic rollback
- Jira and Plane MCP
- Cursor Cloud agents
- Claude Code
- GitHub Enterprise
- Playwright end-to-end
- Lab environments
- Production watch
- OKR-grounded delivery

## Context, Role and Ownership

Idea Engine work group: André and Iren on ideation and research, John on production. The group's mandate on 11 November 2026, from André: one factory that works, not five. On 16 November, the group confirmed André's private factory as the proof-of-concept vehicle for closing the Idea Engine's loop, with the IdeaWise-grown factory (KM Platform's work under Baohua Cai) as the later target.

John's concrete responsibilities:

- Reviewed André's factory documentation and worked out the most minimal production engine that could prove the loop end to end.
- Delivered the 13-stage AI Code Pipeline Map and the team-by-team state matrix against it (owners, certainty scores, OKR coverage).
- Produced the company-wide adoption plan: Baohua's S1 2027 OKRs automate KM Platform ticket-to-merged-PR in one season, other code-producing teams adopt Sentry Auto-Fix in S1 and the rest of Baohua's work from S2; Sentry Auto-Fix adoption offered under ANT-1187.
- Produced the Golden Test Cases plan: a small set of cases that demonstrate the system working end to end.
- Owned the review of Baohua's factory as a later option.
- Published the pipeline map, the team dossiers and the Follow-Up Outline from the 11 November alignment meeting.
- Participated in the open-question work on timelines, success criteria, ownership of André's factory within IdeaWise, hosting (AI Platform versus sandbox), the data warehouse versus PostHog decision for feedback loops, and the human-gate question (one approval versus lights-out).

## The 13-Stage Pipeline, Target State

1. Ready-ticket gate: automated readiness scoring; a ticket cannot start until it passes.
2. Automatic start in a sandbox: ticket to Cursor Cloud launch with no human approval per start.
3. Specification and plan: Jira-to-spec skill drives the specification; multi-agent debate (data, architecture, security, growth, Scrum, software craftsmanship) hardens it.
4. Code and tests: `/develop` workflow writes the code and tests end to end.
5. CI checks, all blocking: GitHub Actions CI covers quality, security and mutation testing; floor at 95% first-pass.
6. Preview and end-to-end tests: lab environments spin up; generated test personas exercise the feature against the Playwright suite.
7. AI review with risk tiers: PR review agent runs; risk tier determines what gates are required.
8. Auto-merge for low-risk changes: no human merge for green low-risk PRs.
9. Auto-deploy to staging: backend auto-release in shadow mode, then live.
10. One human approval: environment approval on tag deploys for production.
11. Progressive release with automatic rollback: zero-impact rollbacks against measurable signals.
12. Production watch per release: Sentry releases, FactWatch, Smart APM converged on one view.
13. Fix loop: Sentry Auto-Fix opens a PR back into the pipeline when production breaks.

## Current-State Picture (as of 17 November 2026)

Stage-by-stage state as mapped by John, scored by how certain the group was each part existed and worked:

| Step | State | Best part today |
|---|---|---|
| 01 Ready-ticket gate | Have | KM Jira Readiness Assistant (90%), advisory |
| 02 Automatic start | Partial | Jira to Cursor Cloud launch (85%), person approves |
| 03 Spec and plan | Have | Jira-to-spec skill and `/develop` (85-95%) |
| 04 Code and tests | Have | `/develop` workflow (95%) |
| 05 CI blocking | Have | GitHub Actions CI (95%); first-pass CI 88% against 95% floor |
| 06 Preview and E2E | Partial | Lab environments and Playwright suite (85%), advisory |
| 07 AI review with tiers | Partial | Review skill (85%); CI review advises only (40-50%); no tiers |
| 08 Auto-merge low-risk | Missing | Person merges every change |
| 09 Auto-deploy staging | Partial | Backend shadow-mode auto-release (70%) |
| 10 One human approval | Have | Environment approval on tag deploys (95%) |
| 11 Progressive release | Missing | Sys Admin S2 zero-impact rollbacks KR (35% on Oboard) |
| 12 Production watch | Partial | Sentry releases, FactWatch (65%), Smart APM (55%); no single view |
| 13 Fix loop | Have | Sentry Auto-Fix (95%), unattended to the PR |

Two foundational workstreams underneath: agent-ready repositories with shared skills (`ai-standards` covers KaufMich; DF reads 25%), and the evidence trail from ticket to production (KM AI Factory, Aura and the AI gateway's PII guardrails exist; no end-to-end trail).

## Team-by-Team Ownership Map

- **KM Platform** (Baohua Cai): nearly every stage on KaufMich repos. `ai-standards`, `/develop`, Jira Readiness Assistant, Cursor Cloud launch, Playwright suite (Salah Ezzaari), GitHub Actions CI, review skill, tag-started deploys, shadow-mode backend auto-release, Sentry Auto-Fix (Archer Wu and Tianwen Dong), AI SonarQube fixes, KM AI Factory.
- **Sys Admin** (Benjamin Smekens): GitHub Enterprise org-wide, GitLab-to-GitHub migration, FactWatch, auto-remediation of trivial incidents.
- **DF Platform** (Joanna Chen): DF repos on GitHub Enterprise, DF Agent and Settings MCP, Kevin Pan's AI code review in CI, Guangqi Wu's Smart APM.
- **AI Core Services** (Blaise Iranyumviye): Foreman (Oscar Eriksson), Jira-ticket-to-PR through Cursor Cloud, AI Delivery Workflow (Marvin Ma), Aura, the AI gateway's PII guardrails.
- **KM Acquisition**: Skills Library (Tomek Duda), frontend release command (Andres Cagua).
- **KM Monetization and Meta Search** (Arame Simonian): agent-driven browser tests.

No team's OKR asks for one unified factory. S2 and S3 OKRs for KM Platform explicitly reject auto-merge and auto-deploy; S4 OKRs feed IDW-106 only from KM Platform and are behind (88% against a 95% floor).

## André's Factory, the Proof of Concept

Chosen 16 November 2026. Private project, roughly 3,000 in tokens last month (currency unclear, probably euros). Runs on a harness André wrote about six months prior. Uses Plane for its better MCP setup, Jira would work. Several agents debate each ticket over several rounds; PR review drives staging; generated test personas exercise features; only bug-free work reaches production. A cloud setup dispatches agents around the clock. Ownership, hosting (whether inside the IdeaWise AI Platform or in a sandbox elsewhere), and token cost are unsettled.

## The Factory John Assembled

The client had the parts of a factory scattered across teams, and no team's OKRs asked for a unified one. John put one together and ran it, starting 17 November 2026:

- **Step 01, gate:** KM Platform's readiness scorer, run locally (chosen over the Idea Engine's own Ready-to-Build gate). The factory's MCP server exposes it as `score_ticket`.
- **Steps 02 to 04, start, spec and build:** a local launcher running KM's `/develop` workflow with Claude Code headless, each run in its own worktree and branch, ending in a report checked against an independent test rerun (`/factory-run`). Porting KM's KaufMich-specific setup to other repos meant a new `node-ts` stack, kept as a patch against `ai-standards`; the porting findings are recorded.
- **Step 05, CI:** up to two agent fix rounds, CI again after merge, revert on red.
- **Steps 06 to 08, pull request:** push, pull request, an independent Opus review posted as a comment, GitHub's checks, and merge through GitHub only on an approving review with green checks.
- **Self-hosting:** the factory is one of its own target repositories; a run that changes the launcher, gate, CI or merge code is never merged automatically.
- **Targets:** a push-disabled clone of the Idea Engine, a Personal Agents repo (PA-1 and PA-2 ran end to end), the factory itself, and the Svyatogor demo app, the first target with a deploy step.
- **Hooked to the agentic Jira workflow** (see `IdeaWise-Agentic-Workflow.md`): ANT-1277 went from ticket to merged and accepted through both.

On 18 November John walked André through it (every step automatic, with auto-merge) and André showed his (multi-perspective ticket review, tests written first, isolated worktrees, post-deploy smoke tests, persona testing, production checks against the hypothesis). John took on combining the two, time-boxed to a couple of days. On 25 November André announced one company factory with two pipelines, the Idea Engine's and KaufMich's, with KaufMich keeping the last steps of Baohua's pipeline.

## Bullet Bank

### General AI transformation, resume summary

- Owned the production side of an EU-based company's end-to-end agent-driven coding factory, the automation half of its agentic-company mandate.
- Mapped a 13-stage ticket-to-production pipeline (ready gate, sandbox start, multi-agent specification, agent-driven development, CI gates, lab environments with generated test personas, AI review with risk tiers, auto-merge, shadow-mode release, progressive rollout, production watch, Sentry-based fix loop) against the client's current capability across five platform teams.
- Reviewed and selected the proof-of-concept factory out of two candidate implementations; produced the company-wide adoption plan that routes the rest of the engineering organization onto it in stages.

### Agentic engineering, technical lead

- Owned the production path of an end-to-end agent-driven software delivery pipeline: multi-agent debate (data, architecture, security, growth, Scrum, software craftsmanship) on each specification, agent-driven PR-centric development, lab environments with generated test personas, progressive release with automatic rollback, Sentry Auto-Fix in an unattended fix loop back into the pipeline.
- Drove the readiness and risk-tier gate design: automated readiness scoring before a ticket starts, risk-tier-based PR review that determines auto-merge eligibility, and shadow-mode release ahead of live deployment.
- Produced the Golden Test Cases plan: a minimal set of end-to-end cases the factory must pass to prove the loop.
- Assembled a working ticket-to-merge code factory from components built separately by different departments (readiness scorer, spec-and-build workflow, shared agent skills), adding the unattended launcher, CI fix loop with automatic revert, independent AI pull-request review and auto-merge gate that joined them into one line.
- Made the factory able to work on its own code, with its guard code (launcher, gate, CI, merge) protected from automatic merge.

### Head of engineering, delivery process

- Mapped a 13-stage ticket-to-production pipeline across KM Platform, Sys Admin, DF Platform, AI Core Services, KM Acquisition, and KM Monetization and Meta Search, scoring each stage's state and owner.
- Delivered the company-wide adoption plan that routes code-producing teams onto Sentry Auto-Fix in S1 and the rest of the KM Platform factory from S2 (Jira epic ANT-1187).
- Negotiated the OKR impact: KM Platform's auto-merge and auto-deploy explicitly deferred in S2 and S3, picked up in S1 2027 under Baohua.

### OKR / product delivery angle

- Grounded the pipeline work in IDW-105 (100% of code AI-drafted) and IDW-106 (3x spec-to-production throughput), with S4 2026 KM Platform first-pass CI at 88% against a 95% floor and the adoption plan to bring other code-producing teams onto the pipeline in S1 2027.

## Best External Resume Versions

**Short block for an AI transformation resume lead:**

> Production-side owner of an EU-based company's end-to-end agent-driven coding factory: Jira ticket to production with multi-agent debate on specification, agent-driven PR-centric development, lab environments with generated test personas, progressive release with automatic rollback, and a Sentry-based fix loop. Mapped the 13-stage pipeline against current capability across five platform teams, assembled a working factory from parts built across departments, and worked toward one canonical factory for company-wide use.

**Compressed single bullet for a head-of-engineering CV:**

> Owned the production side of an end-to-end agent-driven ticket-to-production coding factory for an EU-based ~140-person company; mapped 13 stages across five platform teams, assembled a working factory from parts built by different departments, and delivered the company-wide adoption plan.

**Hands-on bullet for an agentic engineering CV:**

> Assembled a working agent code factory from components built separately across departments, adding an unattended launcher, a CI fix loop with automatic revert, independent AI pull-request review and an auto-merge gate; the factory can safely work on its own code.

## External Claim Safety Notes

### Safe to Claim Now

- Production-side ownership in a three-person work group on the Code Factory.
- 13-stage pipeline map from ready-ticket gate to fix loop.
- Review and selection of the proof-of-concept factory.
- Company-wide adoption plan including Jira epic ANT-1187 and OKR grounding in IDW-105 and IDW-106.
- Team-by-team state matrix across KM Platform, Sys Admin, DF Platform, AI Core Services, KM Acquisition, KM Monetization and Meta Search.
- Assembling and running a working factory from other departments' parts plus his own launcher, CI fix loop, AI pull-request review and auto-merge gate.

### Use With Care / Qualify Internally

- "Lights-off": present as the target John built toward, with the stages he automated end to end in his own factory (readiness gate, unattended build, CI fix loop, independent AI review, auto-merge, safe self-modification).
- "Canonical factory for company-wide use": John drove the consolidation of the company's separate factory efforts into one; the one-factory, two-pipeline model was adopted on 25 November 2026.
- Sentry Auto-Fix is KM Platform's build; John's part is the plan that took it company-wide (ANT-1187).
- 88% first-pass CI is KM Platform's OKR number, context only.

### Avoid Unless Confirmed

- Naming the client (IdeaWise, KaufMich, Dating Framework) in external output.
- Claiming ownership of KM Platform code (`ai-standards`, `/develop`, the readiness scorer, Sentry Auto-Fix, KM AI Factory) which Baohua Cai's team built. John assembled these into his factory and wrote the parts joining them; say "assembled from" or "integrated", never "built" for these components.
- Specific token-cost figures for André's factory in any external context.
- Claiming unattended production deploys on the company's live products.

## Primary Stack

John's assembled factory: Claude Code headless, git worktrees, KM's `/develop` and `ai-standards` with a `node-ts` stack patch, an MCP server exposing the readiness scorer, GitHub Actions, `gh` on GitHub Enterprise, Opus as the independent reviewer. Company-wide: Plane (preferred for MCP), Jira (current), Cursor Cloud agents, Claude Code, GitHub Enterprise (`ideawise.ghe.com`), GitHub Actions CI, Playwright e2e, Sentry (releases and Auto-Fix), SonarQube, Podman and systemd timers for the lab autofixers, Kubernetes for lab environments, Northflank for deployment target, shadow-mode backend auto-release, Forge for the Jira Readiness Assistant, MedusaJS/NestJS sister stack in KM Platform, OpenTelemetry/OpenInference for the evidence trail.
