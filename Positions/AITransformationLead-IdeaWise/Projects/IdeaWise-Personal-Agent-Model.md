<!--
Source: compiled 2026-11-21 from `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/Projects/PersonalAgents/` and the Personal 2nd Brain Agent experiment folder under `KnowledgeReturn/Personal 2nd Brain Agent/`.
Purpose: modular resume source file for the Personal Agents pillar of the IdeaWise engagement.
-->

# IdeaWise / Personal Agent Model / Project Bogatyr

## Basic Info

**Client:** IdeaWise (EU-based, ~140 employees)
**Project:** Personal Agents (private codename Project Bogatyr; the name stays out of company-facing text)
**Dates:** Conceived early November 2026 from John's brainstorm of 5-6 November; first experiment in flight as of engagement end
**Role:** Sole conceiver, designer and author; running the first Learning Grant experiment (his own 2nd-brain repo as the hosted agent)
**Status:** Design published 2026-11-06; first experiment as a Learning Grant request in the Knowledge Return pipeline; rollout plan drafted (AI Ops first, then selected team leaders and the AI Circle and Lifehacks regulars, then everyone, through the module and onboarding)

## Canonical Summary

Conceived and designed IdeaWise's Personal Agent Model: every employee gets a personal AI agent grounded in that person's own data (their OKRs, their meetings and summaries, their projects, their writing voice) and a shared organizational layer (company OKRs, organization structure, public projects), with a team layer sitting naturally between the two. The agent reads private data through the person's own identity (the token broker, extended to M365), so no secondary copy of anyone's data is made. It is the personal half of the agentic-company picture, Code Factory being the other. The design directly addresses 11 distinct organizational problems from onboarding to standardization-by-use to the Golden Path idea (standards baked into the common skills every agent uses, spreading through use rather than enforcement).

John conceived the model, wrote the design and the rollout, drafted the Learning Grant request for the first experiment (his own local 2nd brain as a hosted agent tested against the local project on a fixed set of real weekly tasks), and raised the open privacy and monitoring questions with Legal and P&C ahead of rollout.

## Short Resume Summary Version

Conceived and designed the Personal Agent Model for every employee at an EU-based ~140-person company: each person's agent grounded in their own OKRs, meetings, projects and writing voice, with a shared organizational layer. Private data read through the user's own identity (M365 token broker), no secondary copy. Published the design, drafted the rollout (AI Ops first, then team leaders and power users, then everyone), and ran the first Learning Grant experiment with his own local 2nd brain promoted to a hosted agent.

## Compact Resume Version

Conceived and designed a personal-agent-for-every-employee model for an EU-based ~140-person company, grounded in each person's own OKRs, meetings, projects and writing voice plus a shared organizational layer, with no secondary copy of anyone's data; ran the first Learning Grant experiment with his own 2nd-brain repo as the hosted agent.

## Primary Tags

- Personal AI agents
- Agent for every employee
- Second brain
- Context-grounded agents
- OKR-aware agents
- Meeting-aware agents
- Writing-voice modeling
- Shared organizational context layer
- Team context layer
- Hosted agent runtime
- Local agent to hosted agent promotion
- Microsoft 365 token broker
- Identity-passthrough data access
- No-copy data pattern
- GDPR-first agent design
- German works council and monitoring considerations
- Onboarding automation
- Standardization through use
- AI Platform integration
- Golden Path (standards through skills)
- Agent co-learning with user
- Buy-before-build evaluation

## Context, Role and Ownership

Day-to-day AI use at the client is lumpy, even within AI Ops: a few people work with full context and most do not. A local project needs a terminal and the habit of keeping it current; a hosted agent removes the terminal. New hires gain most, since they start with no context at all. Miguel asked John for onboarding material (skills, IDs and so on), and this answers it. Inside the company nothing is per person: Ask Handycorn serves the company, the DF Agent a team, Phil's Obsidian graph a venture.

John's concrete responsibilities:

- Conceived the model from his own brainstorm of 5-6 November 2026.
- Wrote the design: the three data layers (personal, team, common), what gets read, how private data is read through the person's identity rather than copied, and how the agent compounds over time.
- Wrote the 11-point case for building it, strongest reasons first, smallest problem solved last (from "it gives the Council an example" through to "it solves standardization by itself: standards are baked into the common skills every agent uses, so they spread by use, not enforcement. The Golden Path idea, and possibly the strongest reason").
- Scoped the three artifacts built along the way: the local 2nd brain module (a learning module on using AI efficiently in your own job, built from John's own setup, compatible with Claude Code and Cowork, promoted one-on-one and through onboarding); the common layer on the AI Platform (shared data with no privacy problem, serving both local and hosted versions); and the hosted personal agent itself.
- Wrote the five-step route: evaluate an existing product first (André's buy-beats-build rule), then design, then experiment proposal (Learning Grant request), then Prototype-to-Production, then rollout.
- Ran the first experiment: his own local 2nd brain repo (the active working directory, containing this evidence file's source material) as a hosted agent on the AI Platform, tested against the local project on a fixed set of real weekly tasks.
- Raised the open questions with the right parties: privacy (admins see agent logs and traces, which cannot hold personal content), monitoring (in Germany, a system holding everything an employee says and does can count as a monitoring tool, which brings in the works council), colleagues' words (meeting transcripts hold other people's speech, which Data Review must clear), and Cowork compatibility.

## The Three Data Layers

- **Personal** (most important): the person's OKRs, meetings and summaries, projects, writing voice.
- **Team**: a squad's OKRs and shared projects.
- **Common**: the organization, company OKRs, public projects, glossary, structure.

## The 11-Point Case

Written in the design, smallest problem solved first, the biggest last, with "its own product" as an afterthought:

1. Gives the Council an example.
2. Promotes cheaper patterns of use, with smart tools that cut down on AI usage.
3. Helps with onboarding (agent as onboarding agent).
4. Stretches the AI Platform's capabilities.
5. Massively boosts productivity.
6. Promotes the AI-native agentic company OKRs.
7. Does many of the best things a Company 2nd Brain would, much more cheaply.
8. Smooths uneven AI efficiency: each agent keeps learning how its person works.
9. Smooths over the per-team look of "ANT": each team defines automation on its own terms.
10. Solves standardization by itself: standards baked into the common skills every agent uses, so they spread by use, not enforcement. The Golden Path idea, and possibly the strongest reason.
11. Could become its own product.

## Precedent John Cites

- Every (pulse.bot interview): gave every employee an AI agent, with a shared channel where the agents collaborate and share skills.
- Gemini Enterprise personalization: builds a personal memory per user from connected apps (collaborators, projects, recent decisions).

## First Experiment

John's own Learning Grant request: his local 2nd brain running as a hosted agent on the AI Platform, tested against the local project on a fixed set of his real weekly tasks. Draft lives at `KnowledgeReturn/Personal 2nd Brain Agent/grant-request-draft.md`. Goes to André first, together with the idea of Pierre and John running their own experiments.

## Bullet Bank

### General AI transformation, resume summary

- Conceived and designed a personal-AI-agent model for every employee at an EU-based ~140-person company, grounding each agent in the person's own OKRs, meetings, projects and writing voice, with a shared organizational layer.
- Routed private data through the person's own identity (M365 token broker) rather than copying it into an agent runtime, addressing the German works council and GDPR considerations at the design stage.
- Framed the model as the personal half of the agentic company, with the ticket-to-production Code Factory as the other half, and made standardization-through-use its strongest organizational argument (common skills every agent uses).

### Head of AI / Chief AI Officer angle

- Designed a personal-agent model that doubles as an onboarding system, a cost-reducing pattern of AI use, a standardization mechanism, and an input into the agent platform's roadmap, framed against 11 distinct organizational problems from newest hire through to Council-level direction.
- Scoped the three artifacts the rollout produces (a local 2nd-brain learning module, a shared common layer on the AI Platform, and the hosted personal agent), each with an independent value and a shared rollout surface.

### AI Platform / Platform Engineering angle

- Designed the Personal Agent model as a first-class consumer of the company's AI Platform (identity passthrough via Entra ID and M365 token broker, no secondary copy of personal data, agent runtime on the platform's hosted path), making the agent and the platform co-evolutionary.

### Enablement / Head of L and D angle

- Framed the personal-agent rollout as an onboarding system first, in response to a direct request from the team member responsible for new-hire setup, and designed the learning module that promotes the local-first version through one-on-ones and onboarding.

## Best External Resume Versions

**Short block:**

> Conceived and designed a personal-AI-agent-for-every-employee model for an EU-based ~140-person company. Each agent grounds in its person's own OKRs, meetings, projects and writing voice, with a shared organizational layer and a team layer in between; private data is read through the user's own identity (M365 token broker) rather than copied. Published the rollout (AI Ops first, then team leaders and power users, then everyone) and ran the first Learning Grant experiment with his own 2nd-brain repo promoted to a hosted agent.

**One-liner for a transformation lead summary:**

> Conceived and designed a personal-agent model for every employee at an EU-based ~140-person company, grounded in each person's own OKRs, meetings, projects and writing voice, with no secondary copy of personal data.

## External Claim Safety Notes

### Safe to Claim Now

- Conceived and designed the Personal Agent model solo.
- Published the 11-point case, the three-layer data model, the five-step route from existing-product evaluation through rollout, and the first Learning Grant experiment.
- First experiment (his own repo as hosted agent) in flight through the Knowledge Return Learning Grants mechanism.
- Raised the privacy, monitoring, colleagues' words and Cowork compatibility questions with Legal and P&C ahead of rollout.

### Use With Care / Qualify Internally

- "A personal agent for every employee": present the model John designed, the first agent experiment he ran, and the company-wide rollout plan he wrote.
- "Standardization through common skills": the design's strongest argument; present it as the mechanism.
- Codename Project Bogatyr stays internal; do not use it externally.
- The precedents (Every, Gemini Enterprise) are inspiration; John's design is not a copy of either.

### Avoid Unless Confirmed

- Naming the client (IdeaWise) in external output.
- Inventing adoption or productivity figures.
- Presenting the M365 token broker as a shipped agent-side integration; it is the identity design John chose.

## Primary Stack

Claude Code as the local harness; Cowork as the target hosted runtime; Microsoft Entra ID (OIDC) for identity; Microsoft 365 token broker (extended for agent-side use) for identity passthrough to private data; the AI Platform (LiteLLM gateway, Arize Phoenix, Northflank) for hosting and observability; the common layer on the AI Platform shared with local agents; Jira and Confluence for OKRs and projects; Meeting summaries in the second-brain repo; Oboard for OKR data.

## Open Questions Carried Forward

- Privacy: the AI Platform shows agent logs and traces to admins, which cannot hold personal content.
- Monitoring: in Germany, a system holding everything an employee says and does can count as a monitoring tool, which brings in the works council. For Legal and P&C, early.
- Colleagues' words: meeting transcripts hold other people's speech, which the data review has to clear.
- Cowork: how much of the second-brain repo's skills and conventions work there.
