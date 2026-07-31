# QuantGenie - Principal Architect / Technical Consultant

## Basic Info

**Client / Employer:** QuantGenie (client engagement)
**Domain:** AI-assisted algorithmic trading, LLM pipelines, DSL design, code generation, fintech
**Role / Title:** Principal Architect / Technical Consultant
**Dates:** Nov 2025 – Feb 2026 (approx.)
**Ownership:** Consulting role - requirements, roadmap, architecture, and working proof of concept; handed off to a development team
**Status:** POC delivered and handed off; team continuing build-out
**Primary Stack:** TypeScript, Node.js, NestJS, Fastify, PostgreSQL, Anthropic Claude API, pnpm monorepo
**Focus Areas:** LLM pipeline design, DSL/schema architecture, AST and code generation, backtesting architecture

---

## Source Notes

Bullets from old resume versions (listed as "Founder / Principal Architect" - inaccurate title; was a consulting engagement, not founder). Technical detail derived from the proof-of-concept codebase at `~/Desktop/development/quantgenie/quantgenie-server`. Codebase reflects both POC work and subsequent team build-out; only the POC and architectural foundation are attributable to this engagement.

Note on old resume title: old resumes say "Founder / Principal Architect." This is misleading - the role was a consulting engagement. Prefer "Principal Architect" or "Lead Architect (Consultant)" in future resume output.

---

## Canonical Summary

QuantGenie is a natural-language-to-trading-strategy compiler platform targeting retail traders who lack programming experience. Engaged as principal architect and technical consultant, the work spanned four areas: (1) requirements discovery - discussing the client's vision, documenting requirements, and clarifying scope; (2) roadmap and architecture proposal - defining the system's technical direction, component boundaries, and phased delivery plan; (3) proof-of-concept implementation - building a working POC that validated the core technical thesis: an LLM agent (Anthropic Claude API) that elicits clarifications and generates QSDL (a proprietary typed JSON DSL), a schema validation layer that enforces correctness with auto-retry, and code generator layers that compile QSDL through a platform-agnostic AST into executable MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#) code; (4) team handoff - establishing foundations and getting the development team started on the full build-out. Backtesting engine was designed and included in the roadmap; implementation was scoped for a later stage. Stack: TypeScript, NestJS, Fastify, PostgreSQL, Anthropic Claude API, AJV JSON schema validation, Handlebars code generation templates.

---

## Short Resume Summary Version

Principal architect and technical consultant for QuantGenie (Nov 2025–Feb 2026) - an AI-assisted algorithmic trading platform. Gathered requirements, proposed the initial roadmap and system architecture, and delivered a working proof of concept: an LLM pipeline (Anthropic Claude API) that converts natural-language strategy descriptions into validated QSDL (a proprietary JSON DSL), compiled through an AST to executable MetaTrader 5 (MQL5) and NinjaTrader (C#) code. Designed the backtesting engine architecture for later-stage implementation. Handed off to a development team with technical foundations and early team structure established.

---

## Compact Version

QuantGenie - Principal Architect / Consultant (Nov 2025–Feb 2026). Gathered requirements, proposed roadmap and architecture, and built a working POC for an AI-assisted algorithmic trading platform. POC demonstrated: LLM pipeline (Claude API) → validated QSDL JSON DSL → AST → MQL5 and NinjaScript code generation. Designed backtesting architecture for later implementation. Handed off to development team.

---

## Primary Tags

- AI/LLM pipeline
- Anthropic Claude API
- Prompt caching
- DSL design
- JSON schema
- AST (abstract syntax tree)
- Code generation
- Visitor pattern
- MetaTrader 5 / MQL5
- NinjaTrader / NinjaScript
- Backtesting architecture
- Algorithmic trading
- Fintech
- TypeScript
- Node.js
- NestJS
- Fastify
- PostgreSQL
- AJV / JSON schema validation
- Requirements gathering
- Technical roadmap
- System architecture
- Consulting / engagement
- POC delivery
- Team handoff

---

## Context

QuantGenie's premise: retail traders have valid strategy intuitions but can't implement them in platform-specific trading languages (MQL5 for MetaTrader 5, NinjaScript/C# for NinjaTrader, Pine Script for TradingView). The platform removes that barrier by converting a conversational strategy description into a validated, platform-agnostic JSON specification (QSDL), then compiling that spec into runnable code for the trader's platform of choice. No custody of funds; no live execution - the user owns the generated file.

Engagement scope: consulting to establish requirements, architecture, and a working POC - then hand off to a development team to build the full system.

---

## Role and Ownership

**Requirements and Documentation**

- Discussed the client's product vision and trading platform requirements
- Documented requirements and clarified scope of the initial system

**Roadmap and Architecture Proposal**

- Proposed the initial technical roadmap and phased delivery plan
- Designed the overall system architecture: component boundaries, data flow from user conversation to compiled executable, key design decisions
- Key architectural choices: QSDL as single source of truth, platform-agnostic AST decoupled from schema version, zero-custody deployment model, LLM vs. deterministic boundary
- Designed the backtesting engine architecture (data ingestion pipeline, OHLCV streaming, deterministic QSDL interpretation) scoped for a later implementation stage

**Proof-of-Concept Implementation**

- Built a working POC validating the core technical thesis:
  - LLM conversation engine using Anthropic Claude API with ephemeral prompt caching; multi-turn state machine that elicits clarifying questions and generates QSDL
  - In-loop AJV schema validation with LLM self-correction (error details and JSON path fed back to Claude; up to 5 retries)
  - QSDL (QuantGenie Strategy Description Language) - a typed, versioned JSON DSL for trading strategies; 50+ indicator type definitions
  - Platform-agnostic AST compiled from validated QSDL, with each node supporting both code generation (Visitor pattern) and backtesting evaluation
  - Code generators producing executable MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#) output from the AST

**Team Handoff**

- Established technical foundations and process flow
- Got the development team started on full system build-out
- Handed off codebase, architecture documentation, and roadmap

---

## Technical Architecture Detail

### Core POC Pipeline (what the POC demonstrated)

```
User natural language
  → Multi-turn Claude conversation
    → QSDL JSON generated, validated (AJV), auto-corrected (up to 5 retries)
      → QSDL confirmed
        → AST compiled from QSDL
          ├─ Backtesting: AST.evaluate(context) [architecture designed; impl. later stage]
          └─ Code generation: AST.accept(visitor) → MQL5 / NinjaScript
```

### LLM Pipeline

- Anthropic Claude API with ephemeral prompt caching: full QSDL JSON schema (~60KB) + indicator reference (~4KB) cached per conversation, reducing inference cost materially
- Conversation state machine: `STARTED → WAITING_CONFIRM → COMPLETED` (or back to `STARTED` on rejection)
- Claude elicits clarifying questions before generating QSDL
- Generated JSON parsed, schema-version-stamped, and validated with AJV
- On validation failure: error details + JSON path sent back to Claude for self-correction; up to 5 retries
- On confirmation: QSDL immutable; downstream AST compilation proceeds

### QSDL DSL

QSDL (QuantGenie Strategy Description Language): a declarative, versioned JSON specification for trading strategies.

- Platform-agnostic single source of truth - AST, backtesting, and code generation are all interpreters/compilers of QSDL
- 50+ indicator types (RSI, ATR, MACD, Bollinger Bands, etc.) with typed inputs/outputs
- Boolean signals as numeric 0/1 for type consistency
- Supports variable references, nested rules, binary ops, ternary conditionals
- Schema versioned independently of AST

### AST and Code Generation

- Parser transforms validated QSDL into an immutable hierarchical node tree
- Each AST node implements:
  - `validate(context)` - referential integrity and cross-checks
  - `accept(visitor)` - Visitor pattern for platform-specific code generation
  - `evaluate(context)` - deterministic backtesting interpretation (interface designed; interpreter scoped for later stage)
- Code generators (Visitor pattern):
  - **MT5 (MQL5)** - indicator handle management, `OnInit()` + `OnTick()` structure, buffer management, order execution helpers
  - **NinjaScript (C#)** - NinjaTrader platform code generation
- Generated code is human-readable and deployable without modification

### Backtesting Architecture (designed; not implemented in POC)

- Deterministic QSDL interpretation: stream historical OHLCV candles per timeframe against AST `evaluate()` methods
- Multi-timeframe and multi-instrument support
- Data ingestion pipeline: historical US stocks, futures, forex; normalization, storage, execution flow
- Job queuing and concurrent isolation
- Scoped for a later implementation stage; not part of the POC deliverable

---

# Bullet Bank

## Strong General Bullets

- Engaged as principal architect and technical consultant for QuantGenie - gathered requirements, proposed the initial system architecture and roadmap, and delivered a working proof of concept for an AI-assisted algorithmic trading platform.

- Built a working POC demonstrating the core technical thesis: an LLM pipeline (Anthropic Claude API) converts natural-language trading strategy descriptions to validated QSDL (a proprietary JSON DSL), which is compiled through a platform-agnostic AST to executable MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#) code.

- Designed a constrained LLM generation pipeline integrated with deterministic compilation and execution - from user conversation to deployable trading algorithm code.

- Designed the backtesting data ingestion and processing pipeline, including data normalization, storage, and execution flow; scoped for a later implementation stage.

- Established technical foundations, architecture documentation, and early team structure; handed off to a development team to continue full system build-out.

---

## LLM / AI Pipeline Bullets

- Designed and implemented a multi-turn AI conversation engine using Anthropic Claude API with ephemeral prompt caching; in-loop AJV schema validation and LLM self-correction converge to a valid QSDL spec within 5 retries.

- Architected a constrained LLM generation pipeline: Claude elicits clarifications, generates QSDL JSON, receives structured validation errors, and self-corrects - all within the conversation loop before any output is accepted.

- Designed prompt caching strategy embedding the full QSDL schema and indicator reference into the system context per conversation, reducing inference cost materially without sacrificing schema fidelity.

---

## DSL / Schema Design Bullets

- Designed QSDL (QuantGenie Strategy Description Language) - a typed, versioned JSON DSL for algorithmic trading strategies with 50+ indicator type definitions, variable references, nested rules, and binary/ternary expressions.

- Established QSDL as the platform-agnostic single source of truth for strategy specification, enabling compilation to MT5 (MQL5), NinjaTrader (NinjaScript/C#), and future platforms from one validated JSON artifact.

---

## AST / Code Generation Bullets

- Designed a platform-agnostic AST in which each node implements code generation (Visitor pattern), backtesting evaluation, and referential integrity validation - decoupled from the QSDL schema version.

- Implemented Visitor pattern-based code generators for MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#), producing human-readable, deployable trading algorithms from validated strategy ASTs.

---

## Backtesting / Architecture Bullets

- Designed the backtesting engine architecture: deterministic QSDL interpretation streaming historical OHLCV candles per timeframe through AST `evaluate()` methods, with multi-timeframe/multi-instrument support and job queuing for concurrent isolation.

- Proposed the phased delivery roadmap for QuantGenie, scoping the backtesting implementation as a follow-on stage after the core LLM → QSDL → code generation pipeline was proven.

---

## Consulting / Handoff Bullets

- Led requirements discovery and documentation for a novel AI-assisted trading platform - translating the client's product vision into a concrete system architecture, component boundaries, and phased roadmap.

- Handed off working POC, architecture documentation, and technical foundations to a development team; established early team structure to enable continued build-out.

---

# Best External Resume Versions

## Paragraph Version (Long)

QuantGenie - Principal Architect / Technical Consultant (Nov 2025–Feb 2026). Engaged to establish requirements, propose the initial architecture and roadmap, and deliver a working proof of concept for an AI-assisted algorithmic trading platform targeting retail traders. The POC demonstrated the full core pipeline: a multi-turn Anthropic Claude conversation engine (with ephemeral prompt caching) elicits clarifying questions, generates QSDL - a proprietary typed JSON DSL for trading strategies - validates it against a rich AJV schema with LLM self-correction on failure, then compiles the validated spec through a platform-agnostic AST to executable MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#) code. Also designed the backtesting engine architecture (data ingestion, OHLCV streaming, deterministic AST evaluation) scoped for a later implementation stage. Established technical foundations and got the development team started on full system build-out.

## Paragraph Version (Short)

Principal architect and technical consultant for QuantGenie (Nov 2025–Feb 2026). Gathered requirements, proposed system architecture and roadmap, and built a working POC: Anthropic Claude LLM pipeline converts natural-language strategy descriptions to validated QSDL (a proprietary JSON DSL), compiled through an AST to executable MetaTrader 5 and NinjaTrader code. Designed backtesting architecture for later-stage implementation; handed off to a development team.

---

# Strongest Resume Angles

## AI/LLM Engineering Roles

Emphasize:

- Constrained LLM generation pipeline - Claude generates within a typed JSON schema, not free-form
- In-loop schema validation + LLM auto-correction (structured error feedback → self-correction → retry)
- Prompt caching strategy for cost optimization
- Multi-turn conversation state machine

This demonstrates sophisticated LLM integration - not a prompt wrapper, but a validation-gated generation pipeline with real engineering constraints.

---

## Platform / DSL / Compiler Roles

Emphasize:

- QSDL DSL design - typed, versioned, 50+ indicator types
- Platform-agnostic AST with dual-mode nodes (code generation + backtesting)
- Visitor pattern code generation to multiple target platforms
- Single source of truth enabling multi-platform compilation

---

## Fintech / Trading Technology Roles

Emphasize:

- Domain: algorithmic trading, retail strategy automation, multi-platform code generation
- Zero-custody model - users own the generated code; no funds or live execution
- MT5 (MQL5) and NinjaTrader (NinjaScript/C#) code generation
- Backtesting architecture: OHLCV streaming, multi-timeframe, multi-instrument

---

## Consulting / Principal Engineer / Architect Roles

Emphasize:

- Requirements discovery and documentation
- Architecture proposal and technical roadmap
- POC delivery that validated the product's technical feasibility
- Clean handoff to a development team with established foundations

---

# ATS / Keyword Bank

## AI / LLM Keywords

Anthropic Claude, Claude API, LLM pipeline, prompt caching, multi-turn conversation, constrained generation, AI-assisted, natural language processing, LLM self-correction, schema-constrained generation, generative AI.

## DSL / Schema Keywords

DSL design, domain-specific language, JSON schema, AJV, schema validation, versioned schema, declarative specification, trading strategy specification.

## Code Generation / Compiler Keywords

Abstract syntax tree, AST, code generation, Visitor pattern, compiler, MetaTrader 5, MQL5, NinjaTrader, NinjaScript, Handlebars, template-based code generation.

## Trading / Fintech Keywords

Algorithmic trading, retail trading, backtesting, trading strategy, OHLCV, historical data, indicators, RSI, ATR, MACD, Bollinger Bands, multi-timeframe, multi-instrument, fintech.

## Backend / Engineering Keywords

TypeScript, Node.js, NestJS, Fastify, PostgreSQL, REST API, WebSocket, state machine, dependency injection, repository pattern.

## Consulting / Architecture Keywords

Requirements gathering, technical roadmap, system architecture, proof of concept, POC, technical consulting, team handoff, architecture documentation.

---

# External Claim Safety Notes

## Safe to Claim

- Principal architect and technical consultant for QuantGenie, Nov 2025–Feb 2026
- Requirements gathering, documentation, and roadmap proposal
- System architecture design: full pipeline from user conversation to compiled executable
- Working POC: LLM pipeline (Claude API) → QSDL JSON DSL → AST → MT5 (MQL5) and NinjaTrader (NinjaScript/C#) code generators
- Prompt caching strategy for inference cost reduction
- In-loop AJV schema validation with LLM self-correction (up to 5 retries)
- QSDL: typed, versioned JSON DSL with 50+ indicator type definitions
- Backtesting engine architecture designed; scoped for later-stage implementation
- Handed off to a development team; established technical foundations and early team structure

## Use With Care

- "QuantGenie" as client name - confirmed safe to name publicly
- Prompt caching cost reduction - frame as material/significant, not as a specific percentage (exact number requires measurement)
- "Proof of concept" scope - be precise about what was and wasn't part of the POC deliverable (LLM pipeline + QSDL + code generators yes; backtesting interpreter no; full production API no)

## Avoid Unless Confirmed

- "Founder" or any language implying ownership of the company - this was a client engagement
- Attributing the full codebase (LOC, commit count) to this engagement - the team continued building after handoff; only the POC and architectural foundation are attributable
- Any claim the backtesting engine was implemented - it was designed and roadmapped, not built in the POC
- Any live trading, user metrics, or revenue figures

---

# Missing / Worth Clarifying

1. What specifically was in the POC vs. the team's subsequent build? (Helps sharpen what to attribute)
2. Was the role billed as independent consulting, or through an agency/platform like Toptal?
3. Is the project still active / did the team complete the build?

---

# Relative Positioning Against Other Positions

**Vs. other AI/LLM work in the portfolio:** QuantGenie is the deepest LLM integration in the portfolio - constrained generation, schema validation loop, prompt caching. Use it as the primary evidence for serious LLM engineering capability.

**Vs. Hamza (Founder/System Owner):** Hamza is a true founder engagement; QuantGenie is a consulting engagement. Both show principal/architect-level ownership but at different scales and relationship types.

**Vs. Skunk Capital (trading infrastructure):** Skunk Capital shows live trading systems with real capital. QuantGenie shows AI-native trading tooling architecture. Together they demonstrate breadth across algo trading infrastructure.

**Vs. Budgie (Discovery Architect):** Both are consulting engagements with a roadmap/architecture focus. QuantGenie adds a concrete POC implementation deliverable; Budgie is more purely strategic.
