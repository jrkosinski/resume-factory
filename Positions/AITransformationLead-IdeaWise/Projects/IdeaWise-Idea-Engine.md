<!--
Source: compiled 2026-11-26 from John's own description of the Idea Engine (2026-11-26), `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/Projects/IdeaEngine/` (README, Project Summary, History), `Projects/CodeFactory/History.md`, `Projects/Svyatogor/`, and the Idea Engine meeting summaries of 16 to 25 November 2026 in `Meetings/2026-11/`.
Purpose: modular resume source file for the Idea Engine, the product-side half of the client's automated delivery loop.
-->

# IdeaWise / Idea Engine / Automating the Product Management Loop

## Basic Info

**Client:** IdeaWise (EU-based, ~140 employees)
**Project:** Idea Engine (repo `agentic_workflow` on the client's GitHub Enterprise; runs as an MCP server on the company AI Platform)
**Dates:** Architecture consulting before the work group formed (confirmed by John, 2026-11-26); member of the three-person Idea Engine work group from 16 November 2026 to engagement end
**Role:** Architecture consultant, then production-side owner in the work group. André Hammen (COO) is the architect and the original idea was his; Iren Melamud is the main builder. John owned the production side (the Code Factory that builds what the engine approves) and the context layer the engine and factory share
**Status:** MVP redefined on 16 November 2026 as the full closed loop on a real product (idea, AI-built change in production, tracking, result fed back), first milestone due 16 December 2026; v3.1.0 released 6 November 2026

## Canonical Summary

Once the code pipeline from ticket to production is automated, the bottleneck moves to product management: deciding what to build and learning whether it worked. The Idea Engine automates that role. On the front end it vets ideas: gathers evidence, shapes each idea into a measurable hypothesis, models its value, and prioritizes it before anything is built. On the back end it evaluates the launched change against its hypothesis and records what was learned. The learnings feed back into how the next ideas are shaped and checked, so the engine improves itself. An agent prepares and recommends, deterministic code owns the workflow state and the rules, and a person makes the decision at every gate.

John consulted on the engine's architecture before joining its work group and, from 16 November 2026, owned the production side of the loop in the three-person work group: the Code Factory that turns the engine's approved ideas into shipped software, and the context layer the engine and the factory share.

## Short Resume Summary Version

Consulted on the architecture of an AI engine that automates product management for a company whose code pipeline was becoming automated: it vets ideas before build (evidence, measurable hypothesis, value model, prioritization), evaluates impact after launch, and feeds the learning back so the engine improves itself, with a person deciding at every gate. Owned the production side of the closed loop in the three-person work group.

## Compact Resume Version

Architecture consultant and production-side owner for an AI engine that automates the product-management loop: vetting ideas before build, evaluating impact after launch, and learning from the results, with humans deciding at every gate.

## Primary Tags

- AI product management
- Product discovery automation
- Experimentation and hypothesis testing
- Closed-loop product development
- Self-improving systems
- Human-in-the-loop AI
- Human-gated agent workflows
- Deterministic guardrails around LLM agents
- MCP server architecture
- Decision rights and approval integrity
- Agentic company
- Context engineering

## Context, Role and Ownership

André's diagnosis on 16 November 2026: developers barely write code any more, yet productivity hasn't risen, because the product owners refining ideas are now the bottleneck. The engine is the answer to that, and the Code Factory is what lets the engine prove itself without depending on other teams to adopt it.

How the engine works:

- **Eighteen steps in four phases:** Ideate, Prioritize, Experiment, Launch and Learn. The engine enforces the order and refuses a step whose prerequisite is missing.
- **Governing principle:** "Claude decides how to navigate. Code decides what is true and what is allowed. Humans decide." The agent can't approve anything and can't invent a number; every figure comes from a record, a prior evaluation, a read-only provider, or a human estimate logged as an assumption.
- **Value before mockup,** so sunk cost stays out of the continue decision. No single score: value is modeled in low, base and high scenarios, with confidence, effort and cost beside it.
- **Closed learning loop:** a learnings library feeds prior results into shaping, the pre-check and experiment design; a disproven assumption blocks the pre-check until a person assesses it. The engine also proposes new ideas from feedback and learnings for an authorized person to accept.
- **Runs as an MCP server only,** with decisions reaching people as forms signed with their Microsoft identity.

John's concrete responsibilities:

- Consulted on the engine's architecture.
- Owned the production side of the loop: the Code Factory that builds the engine's Ready-to-Build ideas (see `IdeaWise-Code-Factory.md`), including turning a Ready-to-Build brief into factory tickets (IEDV-20) and wiring product analytics back into the factory (IEDV-18).
- Owned the context layer the engine and the factory share (IEDV-19); designed Desire Paths, an index of company data that learns from how agents use it, with agent, shared and master levels.
- Ran Svyatogor (20 to 23 November 2026), an exploratory run of the whole loop on a dummy app with simulated users: an idea in, a factory-built change deployed, simulated traffic measured, the verdict back out, with no person writing code.
- Planned the work group's weekly epics to the 16 December milestone (IEDV-16) and the testing of the engine on production (IEDV-15).

## Bullet Bank

### General AI transformation, resume summary

- Consulted on the architecture of an AI engine that automates product management once code delivery is automated: vetting ideas before build, evaluating their impact after launch, and feeding the learning back so the system improves itself.
- Owned the production side of the company's closed product loop (idea, AI-built change in production, tracking, result fed back) in a three-person work group with the COO.

### Head of AI / Chief AI Officer angle

- Helped design a human-gated AI decision system in which an agent prepares evidence and recommends, deterministic code enforces state and rules, and people decide at every gate; the agent can neither approve nor invent a number.
- Moved the company's AI focus from the developer bottleneck to the product bottleneck, pairing an automated code factory with an engine that automates idea vetting and impact evaluation.

### AI product / product operations angle

- Architected around a closed learning loop: each launched change is evaluated against its hypothesis, and validated or disproven assumptions shape how the next ideas are vetted.
- Designed the context layer shared by the product engine and the code factory, an index of company data that learns from how agents use it.

### Agentic engineering angle

- Ran an end-to-end exploratory loop on a dummy app with simulated users: idea into the engine, change built and deployed by the code factory, traffic measured, verdict back, with no human code.

## Best External Resume Versions

**Short block:**

> Consulted on the architecture of an AI engine that automates product management for a company automating its code delivery: it vets ideas before build, evaluates impact after launch, and feeds what it learns back into the next round, with a person deciding at every gate. Owned the production side of the closed loop, the code factory and shared context layer that turn approved ideas into shipped, measured changes.

**One-liner:**

> Architecture consultant and production-side owner for an AI engine that automates the product-management loop: idea vetting, impact evaluation and self-improvement.

## External Claim Safety Notes

### Safe to Claim Now

- Architecture consulting on the Idea Engine, before and during the work group (John's own account, 2026-11-26; the detail of that earlier consulting isn't in the ideawise-core record).
- Member of the three-person work group from 16 November 2026, owning the production side and the shared context layer.
- What the engine does: idea vetting, impact evaluation, closed learning loop, human-gated decisions, MCP server.
- Svyatogor as an exploratory end-to-end run John designed and ran.

### Use With Care / Qualify Internally

- Human-gated by design: "automates product management, with people making the final call at each gate" reads as responsible, auditable AI. Lead with it.
- "Self-improving": the learning loop is built into the engine; validated and disproven assumptions shape the next round of vetting.
- John demonstrated the full loop end to end in Svyatogor: idea in, factory-built change deployed, traffic measured, verdict out, with no human code.
- The shared context layer (Desire Paths) is John's design.

### Avoid Unless Confirmed

- Claiming to have written the engine's code. André Hammen architected it and Iren Melamud built it; John's part is architecture consulting and the production side of the loop.
- Naming the client, its ventures or its people in external output.
- Inventing adoption, throughput or conversion figures.

## Primary Stack

TypeScript MCP server (the engine; 81 MCP tools, workflow defined in a manifest that generates the decision-rights table), MCP elicitation forms, Microsoft Entra ID for signed decisions, the company AI Platform for hosting, Jira (IEDV board) for the work group, PostHog for product analytics into the factory, Claude Code as the agent harness.
