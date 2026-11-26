<!--
Source: compiled 2026-11-21 from `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/Projects/GoldenPath/` (Pierre Clisson's AI Platform v1.1 design) and `Projects/old-versions/Governance/` (John's Governance Model Proposal and Drone Swarm alternative), plus Jira ANT-746 (Production Gate and Risk Tiers, John owned).
Purpose: modular resume source file for the Company AI Agent Platform pillar of the IdeaWise engagement. John co-architected the governance and production-gate layers on top of Pierre's platform design; this file captures that split.
-->

# IdeaWise / Company AI Agent Platform / Golden Path + Governance

## Basic Info

**Client:** IdeaWise (EU-based, ~140 employees, active in Europe and China)
**Project:** Company AI Agent Platform ("the AI Platform") plus the Golden Path to production; the governance layer that sits above it
**Dates:** Design work from mid-2026 through engagement end
**Role:** Co-architect. Pierre Clisson (external contractor, developer/architect) owns the platform itself (the three bricks and the no-code runtime); John owns the governance layer and the production gate and risk tiers (Jira ANT-746), plus the Drone Swarm alternative governance model
**Status:** Phase 0 decisions and initial configuration under way; Phase 1 (Foundations: self-service virtual keys, Presidio PII guardrails, Phoenix deployed with Entra ID OAuth, budget and cost dashboards) targeted next; Production Gate and Risk Tiers co-designed under ANT-746

## Canonical Summary

Helped architect IdeaWise's company-wide AI agent platform: the end-to-end system that lets any employee take an AI agent from idea to governed production in under a day. The platform is a three-brick stack (LiteLLM for the AI gateway, Arize Phoenix for observability and evaluations, Northflank for deployment) plus a markdown-defined no-code runtime for non-developer assistants, an MCP/A2A agent registry, EU-only data residency with a Shanghai VPN relay, and Microsoft Entra ID identity with Rippling for lifecycle. Pierre Clisson owns the platform's three-brick design; John co-architected the governance layer above it (initiative lifecycle, AI Central Council and Coordination Function, Federated Reps and Initiative Execution Groups, AHP prioritization, Drone Swarm alternative) and the production gate (named owner, budget, tracing enabled, baseline eval suite, guardrails on, review passed) with two risk tiers (internal tools pass with owner sign-off; customer-facing agents additionally require human sign-off, human-read eval results, and an incident plan).

## Short Resume Summary Version

Co-architected the company-wide AI agent platform at an EU-based ~140-person company: three-brick stack (LiteLLM gateway, Arize Phoenix observability, Northflank deployment), markdown-defined no-code runtime for non-developer assistants, MCP/A2A agent registry, EU-only data residency with Shanghai VPN relay, Entra ID identity. Owned the governance layer (Central Council, Coordination Function, Federated Reps, AHP prioritization, Drone Swarm alternative) and the production gate with two risk tiers that sits above the platform.

## Compact Resume Version

Co-architected the company-wide AI agent platform (LiteLLM, Arize Phoenix, Northflank, markdown-defined no-code runtime, MCP/A2A registry, EU-only data residency, Entra ID identity) and owned the governance layer and production gate with two risk tiers for an EU-based ~140-person company.

## Primary Tags

- Company-wide AI agent platform
- AI gateway
- LLM observability and evaluations
- Deployment platform for AI services
- Golden Path to production
- Self-service agent deployment
- Virtual keys and budget controls
- PII guardrails
- OpenTelemetry / OpenInference
- MCP / A2A agent registry
- Markdown-defined no-code assistants
- Graph-based RAG
- EU data residency
- GDPR and PIPL
- Entra ID OIDC identity
- Shadow AI mitigation
- AI governance
- Initiative lifecycle
- AI Central Council
- AI Coordination Function
- Federated Reps / IEG
- AHP prioritization (Saaty)
- Drone Swarm governance alternative
- Production gate
- Two-tier risk model
- Manifest-based risk scoring

## Context, Role and Ownership

The client already had good AI practices in pockets (an AI gateway, observability, robust CI/CD on Coolify) but no sanctioned route from prototype to production. The clearest symptom was shadow AI: useful tools running informally on one person's laptop or on company Claude/Cursor subscriptions, without traces, evaluations, budget attribution or owner. The Golden Path exists to give those prototypes somewhere to go.

**Pierre Clisson's ownership** (not John's):

- The three bricks: LiteLLM proxy on Northflank for the AI gateway (virtual keys, budgets, Presidio PII guardrails, EU-only model list, OTel callback to Phoenix). Arize Phoenix (OSS, self-hosted) for observability and evaluations with Arize AX (SaaS) as escalation. Northflank (managed EU or BYOC) for Git-driven CI/CD, preview environments, auto TLS, managed Postgres and Redis addons.
- The markdown-defined no-code runtime (NVIDIA NAT or a thin custom layer; Phase 2 decision).
- The MCP/A2A agent registry, thin catalog on the ARD draft spec (Phase 3).
- The default RAG engine: LightRAG (HKU, MIT-licensed), graph-based with incremental indexing, dual-level retrieval, Postgres (pgvector plus Apache AGE) storage so no new database to operate.
- The four-phase roadmap: Phase 0 decisions, Phase 1 Foundations, Phase 2 Production Backbone, Phase 3 Compounding, plus Standing Operations and the Push-Button Ventures north star.

**John's ownership:**

- The governance layer that sits above the platform: initiative lifecycle (Propose through Adapt), the 16-element proposal template, AI Central Council, AI Coordination Function, Federated Team Representatives, Initiative Execution Groups, AHP prioritization (six axes: Area of Impact, Magnitude of Impact, Cost/Effort, Risk, Strategic Leverage, Urgency).
- The Drone Swarm alternative governance model: carrier-fleet versus drone-swarm, an Idea Agent that handles intake, structuring, routing and orchestration, with leaders interacting the way developers interact with Claude Code (natural-language intent, AI proposes and executes, human approves or redirects at gates). Presented as a four-position spectrum (Fully Manual, AI-Assisted, Human-in-the-Loop, Full Cyborg), not a linear roadmap.
- The production gate and risk tiers on the platform (ANT-746): the five-element gate (named owner, budget, tracing enabled, baseline eval suite, guardrails on, review passed), where the template already satisfies the first five so the gate is normally already green when the review runs; the automated security and best-practices review agent (prompt-injection exposure, secret/PII leakage, tool permissions, GDPR/PIPL); two risk tiers (internal tools pass with owner sign-off; customer-facing agents additionally require human sign-off, human-read eval results, and an incident plan).
- The manifest-based risk scoring proposal that threads the risk tier into the gate.
- The L and D linkage: the AI Power Users program (one champion per team, brought through the Golden Path with a real use case) is the applied-learning arm of the L and D program John owns.

## Three Guiding Principles the Governance Layer Enforces

- **Data residency and compliance by design** (EU-hosted, GDPR plus PIPL).
- **No vendor lock-in.** Everything swappable, data exportable, OpenTelemetry and MCP/A2A as the standards.
- **No mandated framework.** Teams pick their own (CrewAI, LangGraph, plain SDK); consistency comes from templates.

## Three Adoption Commitments the Governance Layer Carries

- **Adoption is voluntary.** No team is forced onto the platform; the Golden Path wins by being easier with better guarantees.
- **Monitoring covers production, not people.** Gateway tracing applies to production services and platform-issued dev keys; subscription use (Claude, Cursor) stays private. Developers see their own traces, managers see aggregated cost, not individual activity.
- **AI changes jobs, and the platform makes that concrete.** Enablement continues via the AI Power Users program that John's L and D program carries.

## Bullet Bank

### General AI transformation, resume summary

- Co-architected an EU-based ~140-person company's company-wide AI agent platform (LiteLLM gateway, Arize Phoenix observability, Northflank deployment, markdown-defined no-code runtime for non-developer assistants, MCP/A2A agent registry, EU-only data residency with Shanghai VPN relay, Entra ID identity).
- Owned the governance layer above the platform: initiative lifecycle, AI Central Council plus Coordination Function plus Federated Representatives, AHP prioritization across six axes, and a Drone Swarm alternative model presented as a four-position spectrum rather than a linear roadmap.
- Owned the Production Gate and Risk Tiers (ANT-746): five-element gate (owner, budget, tracing, baseline evaluations, guardrails, review), automated security and best-practices review agent, two risk tiers with human sign-off and incident plan required for customer-facing agents.

### Head of AI / Chief AI Officer angle

- Designed the operating model for AI initiatives at an EU-based ~140-person company: AI Central Council as the primary decision body with CEO veto, AI Coordination Function as the technical and organizational arm, Federated Reps and Initiative Execution Groups lazy-loaded per initiative, with AHP prioritization and a 16-element proposal template.
- Published a Drone Swarm alternative to traditional governance: an Idea Agent handling intake, structuring, routing and orchestration, with leaders interacting via natural-language intent and humans approving or redirecting at gates; the governance proposal presents both as a spectrum the client picks and moves along.

### Head of Platform / AI Platform Engineering angle

- Co-architected the Golden Path from idea to governed production in under a day: for developers (virtual key, scaffold from a template with tracing, evaluations, CI/CD and deployment wired from the first commit, merge triggers an automated review agent and evaluation gate, Northflank deploys with subdomain and TLS, registry publishes as MCP/A2A tool), for non-developers (markdown-defined assistants in a shared runtime with model access, tracing and guardrails invisible, sandbox first, review only on the step into production).
- Owned the production gate (owner, budget, tracing, baseline evaluations, guardrails, review), with two risk tiers and an automated review agent that itself runs on the platform.

### Governance / compliance angle

- Owned the governance proposal for an EU-based ~140-person company: initiative lifecycle, AHP prioritization, Central Council and Coordination Function, Federated Reps and Initiative Execution Groups, metrics defined before implementation with costs and negative effects measured alongside benefits, and a Drone Swarm alternative mapped as a four-position spectrum.
- Owned the two-tier risk model (internal tools pass with owner sign-off; customer-facing agents additionally require human sign-off, human-read eval results, and an incident plan) under Jira epic ANT-746.

## Best External Resume Versions

**Short block:**

> Co-architected an EU-based ~140-person company's company-wide AI agent platform: three-brick stack (LiteLLM gateway, Arize Phoenix observability, Northflank deployment), markdown-defined no-code runtime for non-developer assistants, MCP/A2A agent registry, EU-only data residency with Shanghai VPN relay, Microsoft Entra ID identity. Owned the governance layer above it (Central Council, Coordination Function, Federated Reps, AHP prioritization, Drone Swarm alternative) and the production gate with two risk tiers.

**One-liner:**

> Co-architected the company-wide AI agent platform and owned the governance layer and production gate with two risk tiers for an EU-based ~140-person company.

## External Claim Safety Notes

### Safe to Claim Now

- Co-architect of the AI Platform with specific ownership of the governance layer and the production gate and risk tiers.
- Published the Governance Model proposal (traditional model plus Drone Swarm alternative) and the L and D linkage.
- Ownership of Jira epic ANT-746 (Production Gate and Risk Tiers).
- Participation in Phase 0 decisions (gateway latency, Northflank vs Coolify, managed vs BYOC, LiteLLM SSO path, pace and help commitments).

### Use With Care / Qualify Internally

- John's scope is the governance layer and the production gate and risk tiers; "co-architected the company AI agent platform" is accurate and strong. The platform bricks (LiteLLM, Arize Phoenix, Northflank, LightRAG) are Pierre Clisson's choices.
- "Self-service in under a day": present as the golden-path standard the platform was built to meet.
- AHP prioritization: John's recommended method, with a staged rollout from manual to AI-assisted.
- The Drone Swarm model: John's alternative governance design, offered as a spectrum of options.

### Avoid Unless Confirmed

- Naming the client (IdeaWise) or the platform owner (Pierre Clisson) in external output.
- Presenting Pierre's platform choices as John's own.
- Inventing latency, cost or token-throughput figures.

## Primary Stack

LiteLLM proxy on Northflank; Arize Phoenix (self-hosted) plus Arize AX (SaaS escalation); Northflank (managed EU or BYOC) with managed Postgres and Redis; LightRAG on pgvector plus Apache AGE; NVIDIA NAT or thin custom layer for the no-code runtime; MCP and A2A over an ARD-based registry; Microsoft Entra ID (OIDC) plus Rippling for lifecycle; Presidio for PII guardrails; OpenTelemetry/OpenInference throughout; EU-hosted model providers only (Azure OpenAI EU, Anthropic via Bedrock or Vertex EU, Mistral); Shanghai VPN link for China-based staff with guardrails at the gateway enforcing GDPR-first and PIPL-compatibility for China-related data.

## Open Questions Carried Forward

- Northflank plan-level SSO: which plan includes Entra ID login (verified in Phase 0).
- Phoenix RBAC depth: whether per-project access control suffices or Arize AX is warranted (decided by the pilot).
- Shanghai VPN latency: measured during Foundations; relay or read path if it hurts interactive use.
- Runtime for non-developer agents: NAT, an alternative, or a thin custom layer (decided during Production Backbone, informed by the pilot).
- Registry: build vs adopt (decided in Phase 3 as ARD implementations mature).
- Budget defaults: initial per-team envelopes and per-agent caps (co-designed during Foundations).
- Timeline: indicative durations to be confirmed with teams once the roadmap is validated.
