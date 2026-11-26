<!--
Source: compiled 2026-11-21 from `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/` project summaries, OKRs, meeting notes, and Confluence/Jira references captured in that repo. Revised 2026-11-26 after John's review: Idea Engine and Agentic Workflow files added, Code Factory gains John's assembled factory, L and D rewritten around the Learning Grant Program as it ran.
Purpose: modular resume source file, not a finished resume section. Evidence bank for the consulting engagement John is finishing as of late 2026.
-->

# IdeaWise / AI Transformation Consulting / Overview Index

## Basic Info

**Company / Client:** IdeaWise (EU-based, ~140 employees, active in Europe and China; two main ventures KaufMich and Dating Framework, plus service squads)
**Role / Title:** Principal Consultant / AI Transformation Lead (within AI Ops)
**Dates:** Approx. late 2025 to late 2026 (engagement winding down as of November 2026)
**Reporting:** Works directly with André (AI Ops), Pierre Clisson (AI Platform), Katya (L&D co-lead), with regular exposure to Julius (CEO) on strategy; Idea Engine work group with André and Iren
**Primary Domain:** Enterprise AI transformation, agentic company architecture, AI governance, learning and development, agentic software delivery, personal AI agents
**Status:** Engagement finishing; four signature initiatives in flight across design, pilot and rollout

## Canonical Summary

Served as the principal consultant driving an EU-based company's transformation into a fully agentic organization over approximately one year. The engagement covers the four pillars of what the client calls its agentic-company mandate: (1) an end-to-end lights-off coding factory that turns a Jira ticket into merged, deployed, production-watched software with agents doing the specification, build, review, test and fix work; (2) personal AI agents for every employee, each grounded in that person's own OKRs, meetings, projects and writing voice, with a shared organizational layer; (3) a company-wide AI agent platform with a self-service golden path from idea to governed production in under a day; and (4) a human-centric Learning and Development program in which any employee can get protected time and money to learn, repaid by teaching what they learned, governed by a council John built and chaired. John conceived, designed, architected or co-architected all four, with sole ownership of the L&D and Personal Agents designs, production-side ownership of the Code Factory, and co-architecture of the governance layer and production gate on the AI Platform.

Around the Code Factory sit two more pieces of the automated delivery loop. The Idea Engine automates the product-management work that becomes the bottleneck once code delivery is automated: vetting ideas before build, evaluating impact after launch, and improving itself from the results; John consulted on its architecture and owned the production side of its loop. The agentic Jira workflow, which John designed and built, lets agents carry a ticket from intake through a readiness check, a code-factory run and an acceptance-criteria review, bringing a person in only when one is needed.

## Short Resume Summary Version

Principal consultant driving an EU-based company (~140 employees) into a fully agentic organization over approximately one year. Owns or co-architects the four pillars of the transformation: an end-to-end lights-off coding factory (Jira ticket to production with agent-driven spec, build, review, test and fix), personal AI agents for every employee grounded in their own OKRs, meetings, projects and writing voice, a company-wide AI agent platform with a self-service golden path from idea to governed production in under a day, and a human-centric Learning and Development program of learning grants repaid by teaching, governed by a council he built and chaired. Also consulted on the architecture of an AI engine that automates product management (idea vetting, impact evaluation, self-improvement) and built the agentic Jira workflow that feeds the code factory.

## Compact Resume Version

Driving an EU-based ~140-person company's transformation into a fully agentic organization over approximately one year. Conceived, designed and architected: an end-to-end ticket-to-production coding factory with agent-driven spec, build, review, test and fix, assembled from parts across departments; personal AI agents for every employee; a company-wide AI agent platform with self-service golden path and production gate; and a human-centric Learning and Development program of learning grants governed by a council he chaired. Consulted on the architecture of an AI product-management engine and built the agentic Jira workflow feeding the factory.

## Modular Files

Six project/evidence-bank files: one per pillar (1 to 4), plus the two further pieces of the delivery loop (5 and 6):

1. **`Projects/IdeaWise-Code-Factory.md`**
   The ticket-to-production agent factory. Multi-agent debate on specification, plan and architecture; agent-driven development with PR review; staging with generated test personas; production release with automatic rollback and fix loop. 13-stage pipeline map, two factory options (André's proof of concept and IdeaWise's own KM-Platform-grown version), team-by-team state matrix, John's production-side ownership in the Idea Engine work group, and the working factory John assembled from other departments' parts plus his own launcher, CI fix loop, AI review and auto-merge gate.

2. **`Projects/IdeaWise-Personal-Agent-Model.md`**
   Codename Project Bogatyr. Every employee gets a personal agent reading their OKRs, meetings and summaries, projects and writing voice, grounded on a shared organizational layer (company OKRs, structure, public projects). Ties into the AI Platform. John conceived, designed and is running the first Learning Grant experiment (his own local 2nd brain repo as a hosted agent).

3. **`Projects/IdeaWise-Agent-Platform-Architecture.md`**
   Company-wide AI agent platform: LiteLLM gateway, Arize Phoenix observability, Northflank deployment, LightRAG default RAG engine, markdown-defined no-code assistants, MCP/A2A agent registry, EU-only data residency, Entra ID identity. Pierre Clisson owns the platform itself; John co-architected the Governance layer (initiative lifecycle, AI Central Council and Coordination Function, AHP prioritization, Drone Swarm alternative) and the Production Gate and Risk Tiers (ANT-746).

4. **`Projects/IdeaWise-LD-Program.md`**
   Human-centric Learning and Development program: the Learning Grant Program (protected time and money for any employee, repaid by teaching what they learned), the Knowledge Return Library, and the Light Council (then Formal Council) John built and chaired. Mostly organizational work: governance design, stakeholder alignment, legal and HR clearance in three countries, squad leader briefings, the pool negotiated with the COO and Finance. A little automation code.

5. **`Projects/IdeaWise-Idea-Engine.md`**
   The product side of the loop. Once code delivery is automated, product management becomes the bottleneck; the engine automates it by vetting ideas before build, evaluating impact after launch, and improving itself from the results, with a person deciding at every gate. André architected it and Iren built it; John consulted on its architecture before and during the work group, and owned the production side of its loop and the shared context layer.

6. **`Projects/IdeaWise-Agentic-Workflow.md`**
   The agentic Jira workflow John designed and built in two days: readiness check, cold-start doable check against 24 rules, hand-off to his code factory, agent review against acceptance criteria, Mattermost notifications only when a person is needed. First live ticket taken through the whole loop.

## Confirmed Facts

- Principal consultant engagement with an EU-based company, approximately one year in duration, winding down as of November 2026.
- Four signature initiatives, conceived or co-conceived by John, covering the client's agentic-company mandate (IDW-105: 100% of code AI-drafted; IDW-106: 3x spec-to-production throughput).
- Code Factory: John is production-side owner in the Idea Engine work group (with André and Iren); pipeline map published; André's factory chosen as the proof-of-concept vehicle on 16 November 2026.
- Personal Agents: design published 6 November 2026; John's own local 2nd brain running as a Learning Grant experiment, first through the hosted-agent route.
- AI Platform: John co-authored the Production Gate and Risk Tiers under ANT-746; Governance model proposal (Central Council, Coordination Function, Federated Reps, AHP prioritization, Drone Swarm alternative) authored by John.
- Learning and Development: designed by John and run as Knowledge Return; Learning Grant Program cleared by Legal, People and Culture and Finance and open to requests; Light Council chaired by John; Formal Council plan drafted; Confluence doc set published in space `ANT`; L&D OKRs set from S4 2026.
- Code Factory: John assembled and ran a working factory from 17 November 2026 out of KM Platform's parts plus his own launcher, CI fix loop, AI pull-request review and auto-merge gate.
- Idea Engine: John consulted on its architecture (confirmed by John, 2026-11-26) and owned the production side of its loop in the work group from 16 November 2026.
- Agentic Jira workflow: designed 24 November and built 25 November 2026 by John; repo `ops/jira-agentic-workflow`; ANT-1277 taken through the whole loop and accepted.

## Primary Stack

**Platform:** LiteLLM (AI gateway), Arize Phoenix (self-hosted observability and evals), Arize AX (SaaS escalation), Northflank (Git-driven CI/CD, preview environments, managed Postgres and Redis), LightRAG (graph-based RAG on pgvector plus Apache AGE), NVIDIA NAT or thin custom layer (no-code runtime, TBD), MCP/A2A agent registry on ARD draft spec, Microsoft Entra ID OIDC with Rippling for lifecycle, Presidio for PII guardrails, Opentelemetry/OpenInference throughout
**Code Factory:** Plane (preferred over Jira for MCP), Cursor Cloud agents, Claude Code, GitHub Enterprise, GitHub Actions CI, Playwright e2e suite, Sentry (releases, Auto-Fix), SonarQube, Podman and systemd timers for lab autofixers, Kubernetes for lab environments, Northflank for staging, shadow-mode backend auto-release, MedusaJS/NestJS context in sister teams
**Personal Agents:** Claude Code as local harness, Cowork as hosted runtime target, Microsoft 365 token broker, OKR and meeting data grounded through user identity (no secondary copy)
**L and D / Knowledge Return:** Confluence (space `ANT`) as library and documentation surface, Jira for the Light Council and Learning Grants work, GitHub Actions stats job with Mattermost notifications, Oboard for OKRs
**Idea Engine:** TypeScript MCP server (81 tools, manifest-defined workflow), MCP elicitation forms signed through Entra ID, hosted on the AI Platform, PostHog into the factory
**Agentic Jira Workflow:** Python, Claude Code headless agents, YAML config, Jira REST API, Mattermost bot, cron
**Governance and Measurement:** Analytic Hierarchy Process (Saaty), 16-element proposal template, two-tier risk model, manifest-based risk scoring, AI Central Council plus Coordination Function plus Federated Reps, Drone Swarm alternative model, initiative lifecycle Propose through Adapt

## Resume Compiler Guidance

### Head of / Director / VP / SVP of AI Transformation Roles

Use all four project files. This is the signature-work engagement and should be the resume's lead block. Emphasize ownership across the four pillars, the client's agentic-company mandate (100% of code AI-drafted, 3x spec-to-production throughput), the ~140-employee scope spanning Europe and China, and the combination of hands-on architecture (platform, factory, agents) with governance and enablement (Council, Learning Grants, L&D).

### CTO / Head of Engineering Roles

Use primarily `IdeaWise-Code-Factory.md` and `IdeaWise-Agent-Platform-Architecture.md`. Pull governance and enablement context lightly from the other two. Emphasize end-to-end ticket-to-production automation, multi-agent debate on specification, PR-centric agent development, staging with generated test personas, production watch with Sentry Auto-Fix, and the production gate with risk tiers.

### Head of AI / Chief AI Officer Roles

Use all four. Emphasize the whole-company view: platform plus factory plus agents plus enablement. Call out the governance layer (Central Council, Coordination Function, AHP prioritization, Drone Swarm alternative) as the AI operating model, and the Personal Agents design as the mechanism that makes AI-native concrete for non-developers.

### Head of L and D / Head of Enablement Roles

Use primarily `IdeaWise-LD-Program.md`. Pull Personal Agents and governance context lightly from the other files. Emphasize the human-centric trade (protected time and money for any employee, repaid by teaching), the council John built and chaired, the change-management and clearance work (squad leader briefings, COO and Finance pool, Legal, People and Culture and local HR in three countries), and the lessons from the prior failed program. Do not lead with the superseded LMS and course-catalogue design.

### Head of Platform / AI Platform Engineering Roles

Use primarily `IdeaWise-Agent-Platform-Architecture.md`. Pull Code Factory context lightly. Emphasize the three-brick architecture (LiteLLM gateway, Arize Phoenix, Northflank), the self-service golden path from idea to governed production in under a day, EU-only data residency with Shanghai VPN relay, no vendor lock-in through OpenTelemetry/MCP/A2A standards, and the production gate plus risk tiers.

### Agentic Engineering / AI DevOps Roles

Use primarily `IdeaWise-Code-Factory.md` and `IdeaWise-Agentic-Workflow.md`. Lead with the hands-on work: the factory John assembled from other departments' parts (unattended launcher, CI fix loop with revert, independent AI review, auto-merge gate, safe self-modification) and the agentic Jira workflow that feeds it. Then the 13-stage pipeline map, multi-agent debate on specification, lab environments with generated test personas, Sentry Auto-Fix in an unattended fix loop, and the lights-off ambition (qualified).

### Technical Program Manager / AI Product Roles

Use all four pillars at moderate depth, plus `IdeaWise-Idea-Engine.md`. Emphasize the Idea Engine (automating product management once code delivery is automated) and its work group, Jira-driven initiative lifecycle, the Golden Path as a self-service product, and the OKR-grounded delivery plan (IDW-105, IDW-106, team OKRs for S4 2026 and S1 2027).

## External Claim Safety Notes

### Safe to Claim Now

- Principal consultant engagement with an EU-based company, approximately one year.
- Four signature initiatives covering an agentic-company mandate (code factory, personal agents, agent platform, L and D).
- Conceived and designed the Personal Agent model and the L and D / Knowledge Return program solo.
- Co-architected the governance layer and production gate on the AI Platform (with Pierre Clisson on the platform itself).
- Production-side ownership of the Code Factory within a three-person work group.
- Scope: ~140 employees, active in Europe and China, multiple consumer-facing ventures plus service squads.
- Pipeline map covers 13 stages from ready-ticket gate to the fix loop.
- Confluence doc sets, Jira epics, OKRs and Light Council are live artifacts under John's name.
- Assembled and ran a working code factory from parts built across departments.
- Designed and built the agentic Jira workflow; one live ticket through the whole loop.
- Consulted on the Idea Engine's architecture; owned the production side of its loop.

### Use With Care / Qualify Internally

- "Fully agentic company": the client's mandate, which John was brought in to drive. Present each initiative by what John designed, built, launched or architected.
- "Lights-off factory": present the factory John assembled and ran end to end (readiness gate, unattended build, CI fix loop, independent AI review, auto-merge) and the consolidation toward one canonical company factory that he drove.
- "A personal agent for every employee": present the model John designed, the first agent experiment he ran, and the company-wide rollout plan he wrote.
- "Self-service in under a day": present as the golden-path standard the platform was built to meet.
- Learning program: lead with the design, the council John built and chaired, and the change-management, legal and HR work; it launched company-wide in October 2026, open to every employee.
- Agentic Jira workflow: a working system John designed and built in two days; the first live ticket ran end to end.
- Idea Engine: automates product management, with people making the final call at each gate, which reads as responsible, auditable AI.
- KM Platform's OKR percentages (e.g. first-pass CI) are that team's context, not John's metrics.
- Role title: "Principal Consultant" and "AI Transformation Lead" capture the function.

### Avoid Unless Confirmed

- Naming the client company (IdeaWise, KaufMich, Dating Framework, Julius) in any external output, including recruiter outreach, LinkedIn posts, and resume text. Use the memory's pitch verbatim: "an EU-based company" and "transforming into a fully agentic company."
- Presenting Pierre Clisson's platform bricks (LiteLLM, Arize Phoenix, Northflank, LightRAG) as John's choices. John's layer is governance and the production gate.
- Presenting KM Platform's components or the Idea Engine's code as John's builds. He assembled the former into his factory and architected around the latter.
- Inventing headcount, revenue, uptime, cost, throughput or adoption figures.
- Stating the pitch phrasing ("two-thirds mine from conception to implementation") as an exact split.

## Relative Positioning Against Other Positions

Unique on the resume:

- Only engagement at this organizational scale (~140 employees) and with whole-company AI transformation scope.
- Only engagement combining engineering architecture (factory, platform), organizational design (Council, governance model), and enablement (L and D, Learning Grants, Personal Agents).
- Only engagement where John designed the operating model, not just the technical system.
- Only engagement where AI agents are both the product and the delivery mechanism.

Complements:

- `CTO-Hamza`: six-developer production engineering leadership; IdeaWise is at a larger organizational scale and higher in the stack (operating model, governance, enablement). Hamza remains the strongest live production CTO story; IdeaWise is the strongest transformation and agentic-architecture story.
- `FoundingEngineer-StreamFinance`: individual-contributor-plus-one deep architecture under capital-at-risk. IdeaWise is the opposite shape: breadth across many teams, governance and enablement, with architectural depth concentrated in the Code Factory and Personal Agents.
- `FoundingArchitect-Quantgenie`: LLM-to-DSL design and founder scope. IdeaWise is the enterprise deployment of comparable LLM-and-deterministic patterns at company scale.

Use IdeaWise as the lead block for any AI transformation, Head of AI, VP/SVP AI, Chief AI, agentic engineering or platform engineering target. For deeper blockchain, DeFi or fintech roles, lead with Stream Finance or Hamza and keep IdeaWise as the current engagement bullet.
