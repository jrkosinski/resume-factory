<!--
Source: architecture diagrams (BudgieSystemContext.png, BudgieContainerHighLevel.png, BudgieContainerDetailed.png, BudgieFinancialCore.png, BudgieAIServices.png, BudgieNotifications.png), product backlog v0.7 (May 2026), estimation spreadsheet.
Purpose: evidence-bank file for resume compilation.
Generated: 2026-07-03
-->

# Budgie / Discovery Architect

## Basic Info

**Company:** Budgie (Singapore-based AI personal finance startup)  
**Dates:** Approx. April – May 2026 (3-week formal discovery engagement)  
**Role / Title:** Technical Software Architect — Discovery Team (Toptal engagement)  
**Team:** 3-person discovery team: Technical Software Architect (John), Product Manager (Eddie George, Toptal), UI/UX Designer  
**Status:** Discovery phase complete; product not yet built  
**Engagement Type:** Formal 3-week technical discovery, architecture design, product scoping  
**Primary Domain:** AI-powered personal finance, bank aggregation (Finverse), crypto aggregation, LLM orchestration, financial data platform  
**Market:** Singapore (primary), Hong Kong (secondary)

## Canonical Summary

Served as Technical Software Architect on a formal 3-week discovery engagement for Budgie, a Singapore-focused AI-powered personal finance startup, through Toptal. Operated as the technical member of a 3-person discovery team (technical architect, product manager, UI/UX designer) to define system architecture, assess third-party integrations, scope 421 product features across 16 epics, and produce a technical estimation model for the full build phase.

Designed the complete system architecture for the Budgie platform: a multi-service backend spanning bank aggregation via Finverse, crypto aggregation via exchange APIs and Goldrush blockchain data, a layered AI orchestration system using Anthropic Claude as the LLM, a Financial Data Aggregation Hub with canonical data modelling, a transaction categorization engine (rule-based plus AI-assisted), a Financial Health Score service, a proactive insights engine, a notifications pipeline, user and auth services, and an admin console. Produced six C4-level architecture diagrams covering system context, container structure, financial core components, AI service layers, and the cross-cutting notifications flow.

## Short Resume Summary Version

Technical Software Architect on a formal 3-week Toptal discovery engagement for Budgie, designing full-stack architecture for an AI personal finance platform targeting Singapore users. Produced system context, container, and component-level C4 diagrams; led technical scoping workshops; assessed Finverse, Goldrush API, and Anthropic/Claude integrations; defined a tool-augmented AI orchestration architecture (personality, guardrails, PII detection, deterministic calculation tools, explainability) to prevent hallucination in financial contexts; and scoped a 421-feature product backlog across 16 epics for the build phase.

## Primary Tags

* Discovery Architecture
* Technical Discovery
* System Architecture
* C4 Architecture Diagrams
* AI Orchestration
* LLM Integration (Claude / Anthropic)
* Tool-Augmented LLM
* Hallucination Prevention
* Personal Finance Platform
* Bank Aggregation (Finverse)
* Crypto Aggregation
* Blockchain Data (Goldrush API)
* Financial Health Score
* Transaction Categorization
* Proactive AI Coaching
* Natural Language Queries
* Notifications Pipeline
* Product Backlog
* Technical Estimation
* Singapore Fintech
* Regulatory Awareness (PDPA / MAS)
* Multi-Service Architecture
* BFF Pattern
* Toptal

## Context

Budgie is a founder-led Singapore startup building an AI-powered personal finance app. The core product concept: aggregate a user's bank accounts and crypto holdings, present a Financial Health Score, and deliver proactive AI coaching through a named character (Budgie) that acts as a personal financial advisor rather than a chatbot feature bolted onto a dashboard. Target market is retail consumers in Singapore with future expansion to Hong Kong.

The engagement was a formal 3-week paid discovery. The discovery team was three people: myself as Technical Software Architect, Eddie George (Toptal Senior PM) as Product lead, and a UI/UX Designer. My role was the technical counterpart to the product and design tracks — running architecture design, leading technical scoping discussions in workshops, assessing integration vendors, flagging engineering risk, and producing the technical deliverables needed to support an accurate build-phase estimate and a credible build-team handoff.

## Role and Ownership

Served as the technical architecture lead for the discovery engagement.

Owned or contributed to:

* System context design (C4 Level 1) — identifying all external systems, actors, and integration points
* Container architecture design (C4 Level 2 high-level and detailed) — defining the service decomposition for the full platform
* Financial Core component design — Financial Data Aggregation Hub, Transaction Categorization Engine, Goals/Budgeting Engine, Budgie Score Service (Financial Health Score), Insights Engine
* AI Services architecture — layered orchestration design (Personality, Policy/Guardrails, Tools, Context & History, Explainability, PII Detection, LLM Abstraction, Token Usage Tracking)
* Notifications pipeline architecture — Notification Intake API, preference/consent, deduplication and throttling, content building, multi-channel routing (push, email)
* Technical workshop facilitation — contributed technical guidance across 20, 21, and 24 April workshops
* Third-party integration assessment — Finverse (bank aggregation), Goldrush API (blockchain wallet data), CoinGecko (crypto pricing), Anthropic/Claude (LLM), Expo/OneSignal (push notifications)
* Technical contributions to the 421-feature product backlog (Epic 2 banking, Epic 3 crypto, Epic 4 AI, Epic 5 budgeting, Epic 7 FHS, Epic 8 Ask Anything, Epic 12 data/privacy, Epic 13 compliance)
* Technical estimation spreadsheet
* Build-vs-buy scoping for transaction categorization (Asian market validation concern)

## Architecture Designed

### System Context

The Budgie Platform integrates with:

* **Bank Aggregation APIs** (Finverse) — aggregates Singapore and Hong Kong retail bank accounts; read-only at MVP; top 3 SG retail banks confirmed at launch
* **Blockchains** (Solana, Bitcoin, Ethereum, EVM L2s) — via Goldrush API for wallet balance reads
* **Crypto Exchange APIs** (Coinbase, Binance and others) — exchange account balances and transaction history
* **CoinGecko API** — crypto pricing / fiat valuation for holdings not handled by Goldrush
* **LLM Provider API** (Anthropic/Claude) — AI orchestration for coaching, Ask Anything, proactive insights
* **External Billing Providers** (Google Play Store, Apple App Store) — in-app subscription billing

### Container Architecture (Service Decomposition)

| Service | Role |
|---|---|
| Mobile UI | iOS / Android app (React Native / Expo) |
| Mobile App Backend API / BFF | Backend-for-Frontend aggregating Mobile UI calls |
| Bank Data Ingestion Adapter | Pulls, normalizes, and stores bank data from Finverse |
| Crypto Data Ingestion Adapter | Pulls exchange data and on-chain wallet balances; normalizes to canonical model |
| Financial Core Services | Aggregation hub, categorization, budgeting, FHS scoring, insights |
| Budgie AI Orchestration | Layered LLM orchestration (see AI Services below) |
| User Services | User profiles, preferences, goals, subscription/billing data |
| Auth Service | Authentication, identity, session management |
| Admin Console Backend API / BFF | Admin-facing BFF |
| Admin UI | Internal back-office and reporting console |
| Admin Reporting Services | Reporting aggregates for admin console |
| Application Database | PostgreSQL — primary application data store |
| Secure PK Token Store | Secure storage for sensitive keys/tokens |
| External Identity Providers | Social login (Google, Apple) |

### Financial Core Services (Component Detail)

**Financial Data Aggregation Hub:**
- Canonical Model Mapper — converts provider-specific bank and crypto data into Budgie's internal canonical schema
- Account & Balance Consolidator — builds a unified view of a user's accounts, holdings, and balances across all sources
- Derived Metrics Builder — computes movable financial metrics from canonical data
- Query API — internal API surface for other services to query aggregated financial data

**Transaction Categorization Engine:**
- Rule-based categorization pass (speed/cost)
- AI-assisted categorization (handles ambiguous/non-English transactions; SG/HK merchants, Mandarin/Cantonese descriptions)
- User correction feedback loop
- *Note: build-vs-buy decision flagged during discovery — Western categorization engines perform poorly on Asian merchant data*

**Goals/Budgeting Engine:** Manages user-defined savings and debt-payoff goals; calculates required monthly contributions, projected timelines, and dynamic adjustments based on actual spending.

**Budgie Score Service:** Calculates the Financial Health Score — a proprietary composite metric covering savings rate, spending habits, budget discipline, and debt management. Supports Phase 1 (questionnaire-based, pre-bank-connection) and Phase 2 (connected-data-driven) calculation modes.

**Insights Engine:**
- Insight Rules Engine — maps specific financial conditions to coaching insights
- Anomaly & Trend Detection Engine — identifies unusual spending, spending pattern trends, and statistically notable deviations

### AI Services Architecture (Layered Orchestration)

Designed to prevent hallucination in a financial context by separating concerns into distinct layers:

| Layer | Purpose |
|---|---|
| Personality Layer | Embeds Budgie's character, tone, voice, and conversational style into the LLM system prompt |
| Policy & Guardrails Layer | Enforces scope limits — prevents investment advice, off-topic, unsafe, or regulatory-risk outputs |
| Tools Layer | Deterministic calculation tools for all arithmetic — the LLM calls tools rather than computing inline, keeping financial outputs auditable and hallucination-free |
| Context & History Layer | Assembles relevant user data (accounts, spending, goals, session history) for injection into the prompt |
| Explainability & Auditing Layer | Audit log of AI interactions; ensures every quantitative claim traces back to source data |
| PII Detection / Tokenization Layer | Scans prompts for PII before sending to LLM; replaces with anonymized tokens; restores in response |
| LLM Model Abstraction Layer | Abstraction over the LLM provider (Claude selected at April workshops) for swap-ability |
| Token Usage Tracking Layer | Per-user and aggregate LLM cost monitoring tied to subscription/billing tier enforcement |
| AI API Chat Endpoint | Synchronous chat API serving the Ask Anything and in-context AI surfaces |
| Async Task Endpoint | Asynchronous endpoint for scheduled proactive coaching tasks (daily check-ins, weekly sessions) |

### Notifications Flow

Event-driven pipeline with consent-first design:

1. **Notification sources:** Events/Analytics Service (TypeScript REST API), direct app/admin trigger, scheduled job
2. **Notification Intake API** (TypeScript) — single canonical ingest point
3. **Preference/consent check** — validates user has consented to receive this notification type
4. **Deduplication & throttling** — prevents repeat or flood notifications
5. **Content build** — generates notification body in Budgie's voice
6. **Route to channel:** push notification (via Expo/OneSignal) or email (Event Dispatcher with subscriber mapping)

## Product Backlog Scope

Technical input contributed to a 421-feature backlog across 16 epics:

| Epic | Feature Count | Priority Split |
|---|---|---|
| 1: Onboarding & Activation | — | Private Beta / MVP / v1.1 / v2+ |
| 2: Account Aggregation — Banking | — | Primarily Private Beta |
| 3: Account Aggregation — Crypto | — | Primarily Private Beta |
| 4: AI Coaching & Personality | — | Private Beta / MVP / v1.1 |
| 5: Budget & Expense Management | — | Private Beta / MVP / v1.1 |
| 6: Goal Planning | — | MVP (deferred from Private Beta) |
| 7: Financial Health Score | — | Private Beta / MVP / v1.1 |
| 8: Ask Anything — Natural Language Queries | — | Private Beta / MVP / v1.1 |
| 9: Notifications & Proactive Engagement | — | MVP / v1.1 |
| 10: Social Features | — | MVP / v2+ |
| 11: Pricing & Subscription | — | Private Beta / MVP |
| 12: Data & Privacy Infrastructure | — | Private Beta |
| 13: Compliance & Regulatory | — | Private Beta |
| 14: Analytics & Instrumentation | — | Private Beta |
| 15: Internal Admin & Back Office | — | Private Beta |
| 16: Localisation & Internationalisation | — | MVP / v1.1 |

**Overall:** 179 Private Beta features (43%), 148 MVP features (35%), 71 v1.1 features (17%), 23 v2+ features (5%).

## Technical Advisory / Workshop Contributions

Key technical recommendations and assessments made during the April workshop series:

* **LLM selection:** Recommended Claude (Anthropic) based on data-handling suitability and capability; commercial terms flagged as still pending at close of discovery
* **Tool-augmented AI architecture:** Proposed separating deterministic arithmetic into dedicated calculation tools (LLM orchestrates, tools compute) to prevent hallucination in quantitative financial outputs
* **Finverse integration assessment:** Confirmed Singapore top-3 retail bank coverage and transaction history depth; identified 2FA-per-refresh as the core Finverse friction — every balance sync requires user re-authentication, undermining the engagement model — and flagged the need for an alternative aggregator evaluation
* **Blockchain data provider:** Recommended Goldrush API for unified multi-chain wallet balance reads (Solana, Bitcoin, Ethereum, EVM L2s)
* **Transaction categorization risk:** Flagged that Western ML categorization engines handle Asian merchant data (Mandarin/Cantonese descriptions, local SG/HK taxonomy) poorly; raised as a build-vs-buy decision for the Tech Lead
* **RAG grounding:** Recommended RAG with curated source library (e.g. Investopedia, MAS, regulatory sites) for any AI responses to general financial knowledge queries — with source citations shown
* **Regulatory surface:** Flagged MAS (Singapore) and PDPA constraints on AI outputs; advised AI guardrail architecture must prevent scope drift into personalized investment advice; flagged LLM data retention policies against PDPA/PDPO compliance requirements

## Bullet Bank

### Discovery / Architecture Angle

* Served as Technical Software Architect on a formal 3-week Toptal discovery engagement for Budgie, a Singapore AI personal finance startup — technical member of a 3-person team (architect, product, design) — producing C4 system-context, container, and component-level architecture diagrams spanning bank aggregation, crypto aggregation, AI orchestration, financial data services, and a cross-cutting notifications pipeline.

* Designed a layered AI orchestration architecture — Personality, Guardrails, Tools, Context & History, Explainability, PII Detection, LLM Abstraction, Token Usage — with deterministic calculation tools preventing LLM hallucination in financial output.

* Produced the technical architecture and integration assessment for a platform connecting Finverse bank aggregation (SG/HK), Goldrush on-chain blockchain data (Bitcoin, ETH, Solana, EVM L2s), exchange APIs (Coinbase, Binance), CoinGecko pricing, and Anthropic Claude as LLM.

* Designed a Financial Data Aggregation Hub with canonical model mapping, cross-source account consolidation, and a derived metrics layer serving a Financial Health Score service, transaction categorization engine, goals/budgeting engine, and AI-powered insights engine.

* Contributed technical scoping to a 421-feature product backlog across 16 epics (Private Beta through v2+), covering onboarding, bank aggregation, crypto aggregation, AI coaching, budget management, goal planning, Financial Health Score, natural-language queries, notifications, compliance, and analytics.

* Identified Finverse's 2FA-per-refresh constraint as the primary engagement-model risk during technical discovery, triggering an alternative aggregator evaluation before build commitment.

* Scoped a tool-augmented natural-language "Ask Anything" feature architecture — data-grounded query answering, question type classification, deterministic retrieval, explainability receipts, and graceful out-of-scope refusal — for a personal finance AI context where hallucination in financial answers directly erodes user trust.

### Platform / Architecture Angle

* Architected a multi-service personal finance platform across a mobile BFF, bank and crypto ingestion adapters, financial core services (aggregation, categorization, FHS scoring, insights), AI orchestration, user/auth services, and an admin console — designed as a discovery-phase deliverable for a build team handoff.

* Designed a consent-first notifications pipeline with intake API, preference/consent check, deduplication, throttling, content building, and multi-channel routing (push via Expo/OneSignal, email), feeding proactive AI coaching cadences (daily check-ins, weekly advisor sessions).

### AI / LLM Angle

* Designed a layered LLM orchestration architecture for a financial coaching AI: Personality, Policy/Guardrails, and PII Detection layers wrap all prompts before LLM dispatch; a Tools Layer replaces inline LLM arithmetic with deterministic calculation tools; an Explainability/Auditing Layer ensures every quantitative claim traces to source data.

* Recommended and scoped a RAG architecture constraining AI knowledge to curated sources (Investopedia, MAS, regulatory sites) with visible citations, preventing financial misinformation while enabling general-knowledge coaching.

* Flagged regulatory constraints (MAS, PDPA/PDPO) shaping AI guardrail design — guardrails must prevent scope drift into personalized investment advice; LLM data retention policies require formal PDPA review before commercial deployment.

## Best External Resume Versions

### Discovery / Architecture (general)

> Technical Software Architect on a formal 3-week Toptal discovery engagement for Budgie, a Singapore AI personal finance startup. Served as the technical member of a 3-person discovery team (architect, product manager, UI/UX designer). Led technical architecture design across a six-diagram C4 deliverable set — system context, container structure, financial core components, AI service layers, and notifications pipeline — and contributed technical scoping to a 421-feature build-phase backlog. Designed a tool-augmented LLM orchestration architecture (Personality, Guardrails, PII Detection, deterministic calculation Tools, Explainability, LLM Abstraction layers) to prevent hallucination in financial AI outputs. Assessed Finverse bank aggregation, Goldrush blockchain data, and Anthropic Claude for the build stack; identified Finverse's 2FA-per-refresh constraint as a core engagement-model risk.

### AI / LLM Specialization

> Designed the AI orchestration architecture for an AI-first personal finance platform (Budgie, Toptal): layered LLM orchestration with a dedicated Personality layer, Policy/Guardrails enforcement, PII Detection/Tokenization, a deterministic calculation Tools layer (LLM never computes arithmetic inline), a Context & History assembly layer, and a full Explainability/Auditing layer. Recommended Claude (Anthropic) as the LLM; scoped RAG grounding with curated sources and source citations to prevent financial misinformation. Advised on PDPA/MAS compliance implications for LLM data retention.

### Fintech / Banking Platform

> Discovery Architect for a Singapore personal finance platform integrating Finverse bank aggregation (SG/HK retail banks), Goldrush API for on-chain blockchain wallet reads (Bitcoin, Ethereum, Solana, EVM L2s), crypto exchange APIs, and CoinGecko pricing into a unified canonical data model. Designed the Financial Data Aggregation Hub — Canonical Model Mapper, Account Consolidator, Derived Metrics Builder, Query API — feeding a Financial Health Score service, transaction categorization engine (rule-based + AI-assisted, with Asian-market localisation flag), goals/budgeting engine, and proactive insights engine.

## Strongest Resume Angles

### AI / LLM Architecture Roles

Emphasize:
* Layered LLM orchestration design (Personality / Guardrails / Tools / Context / Explainability / PII / Abstraction)
* Tool-augmented architecture for hallucination prevention in financial contexts
* RAG grounding with citation model
* Claude/Anthropic selection and commercial/compliance advisory
* PDPA and MAS regulatory surface flagging

### Staff / Principal / Architecture Roles

Emphasize:
* Six-diagram C4 architecture suite delivered as a discovery artifact
* Multi-service decomposition across ingestion adapters, financial core, AI orchestration, BFF, auth, admin
* Canonical data model design spanning heterogeneous bank and crypto sources
* Vendor risk identification (Finverse 2FA-per-refresh)
* Build-vs-buy scoping (transaction categorization)

### Fintech / Banking Roles

Emphasize:
* Finverse integration design (bank aggregation, Singapore/HK market)
* Canonical financial data modelling
* Financial Health Score (multi-factor proprietary composite metric)
* Transaction categorization architecture for Asian merchant data
* MAS and PDPA regulatory advisory

### Discovery / Pre-Build Consulting Roles

Emphasize:
* Full technical discovery engagement: workshops, architecture, vendor assessment, estimation
* 421-feature product backlog contribution across 16 epics
* Private Beta vs MVP vs v1.1 scoping and prioritisation input
* Identifying build-blocking technical risks before build commitment

## ATS / Keyword Bank

Discovery Architecture, Technical Discovery, System Architecture, C4 Diagrams, AI Orchestration, LLM Integration, Claude, Anthropic, Tool-Augmented LLM, Hallucination Prevention, Personal Finance Platform, Bank Aggregation, Finverse, Crypto Aggregation, Blockchain Data, Goldrush API, Financial Health Score, Transaction Categorization, Proactive AI Coaching, Natural Language Queries, RAG, Retrieval Augmented Generation, Notifications Pipeline, Technical Estimation, Singapore Fintech, PDPA, MAS Compliance, Multi-Service Architecture, BFF Pattern, Backend-for-Frontend, PostgreSQL, Expo, OneSignal, CoinGecko, Toptal, Product Backlog, Technical Scoping, Canonical Data Model, Financial Data Aggregation.

## External Claim Safety Notes

### Safe to Claim

* Technical Software Architect on a formal 3-week Toptal discovery engagement; technical member of a 3-person discovery team (architect, product manager, UI/UX designer).
* Produced C4-level architecture diagrams: system context, container high-level, container detailed, financial core components, AI services layers, notifications flow.
* Led technical architecture design for a Singapore AI personal finance platform.
* Designed layered LLM orchestration architecture with Personality, Guardrails, Tools, Context & History, Explainability, PII Detection, LLM Abstraction, and Token Usage Tracking layers.
* Recommended tool-augmented architecture (deterministic calculation tools instead of inline LLM arithmetic) for hallucination prevention.
* Assessed Finverse (bank aggregation), Goldrush API (blockchain data), Anthropic Claude (LLM), CoinGecko (pricing), Expo/OneSignal (push notifications).
* Identified Finverse 2FA-per-refresh constraint as core engagement-model risk.
* Contributed technical scoping to a 421-feature product backlog across 16 epics.
* Participated in April 2026 workshops (20, 21, 24 April) providing technical guidance.
* Recommended RAG grounding and flagged PDPA/MAS regulatory constraints on LLM deployment.
* Flagged Asian-market transaction categorization as a build-vs-buy risk (non-English merchant descriptions).

### Use With Care / Qualify

* Position as "technical co-author of the backlog" rather than sole author — the product backlog was primarily authored by Toptal PM Eddie George; technical input contributed specific epics and shaped the build-phase framing.
* Claude as "selected LLM" — workshop confirmed Claude as the preferred provider but commercial terms were still pending at close of discovery; phrase as "recommended and selected in discovery" rather than "commercially contracted."
* Singapore top-3 bank coverage via Finverse — workshop-confirmed but final list pending the Finverse technical spike (2.1.1). Phrase as "workshop-confirmed coverage of top SG retail banks."

### Avoid Unless Confirmed

* Claiming any part of the platform was built or deployed — this is a discovery-only engagement; the product was not built.
* Claiming specific estimation figures from the spreadsheet without verifying exact numbers.
* Claiming the Finverse alternative aggregator evaluation reached a conclusion during the engagement — it was in progress at close of discovery.
* Claiming Goldrush was the confirmed final blockchain data provider — it was the evaluated/recommended option, pending final confirmation.

## Relative Positioning Against Other Positions

* **vs Hamza (CTO/Co-Founder):** Hamza is the stronger CTO/leadership entry with six-developer team management and a live production platform. Budgie-Discovery is the stronger entry for: discovery consulting, AI/LLM architecture, fintech/bank-aggregation architecture, pre-build architecture depth.
* **vs FoundingEngineer-StreamFinance:** StreamFinance would be the stronger payments-execution entry; Budgie-Discovery is the stronger AI orchestration and discovery-phase architecture entry.
* **For AI/LLM Architecture roles:** Budgie-Discovery is the primary entry — the layered LLM orchestration design is the most detailed AI architecture artifact in the evidence bank.
* **For Fintech/Singapore Fintech roles:** Budgie-Discovery provides strong Singapore-specific fintech context (MAS, PDPA, Finverse, CPF, SGFinDex awareness).
