# JOHN R. KOSINSKI
Senior Systems Architect • Principal Engineer • Technical Leader
john.kosinski@toptal.com

---

## SUMMARY

Senior systems architect and technical leader with 15+ years designing, building, and operating financial, cloud, and distributed systems across the full engineering lifecycle. Experienced at decomposing ambiguous business and technical requirements into shipped, production-grade architecture spanning cloud infrastructure, AI-assisted pipelines, payment systems, and real-time data platforms. Known for end-to-end ownership, leading engineering teams, and making clear architectural decisions in high-stakes environments where failure carries real financial or operational consequences.

Primary strengths include cloud-native architecture, technical leadership and mentoring, full-lifecycle execution from concept through production support, and cross-domain problem-solving under financial and operational constraints.

---

## CORE CAPABILITIES

- End-to-end ownership of complex, high-stakes technical problems across the full development lifecycle
- Cloud infrastructure architecture and operations (AWS, GCP, Kubernetes)
- Technical leadership, team mentoring, and cross-org engineering influence
- Distributed systems and data pipelines (Kafka, Kubernetes, event-driven architectures)
- Constraint-driven architecture under financial and operational risk
- LLM-assisted systems combined with deterministic code
- Financial and risk modeling
- Automated trading system design and ownership
- Blockchain, DeFi, and smart contract architecture (EVM, Solidity, Rust)

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

**Hamza — CTO / Co-Founder**

- Led a six-developer engineering team as CTO and co-founder, managing frontend, backend, seller admin, payment, and smart-contract workstreams while remaining hands-on with architecture, code review, repository management, and implementation
- Established production engineering practices across a Web3 marketplace stack: CI/CD, backend tests, payment-system tests, smart-contract tests, dev/staging/testing environments, monitoring, alerting, and code review
- Designed and delivered a production multi-chain crypto payment system spanning Optimism, Arbitrum, Bitcoin, Ethereum, Polygon, Mantle, Scroll, and other EVM L2s: payment intents, per-payment holding wallets, chain listeners, idempotent verification, canonical settlement, and LiFi replenishment
- Coordinated architecture and delivery across e-commerce, blockchain, payments, seller tooling, frontend, backend, and AWS/Kubernetes infrastructure while advising on technical business strategy and roadmap
- Platform reached hundreds of users per month, 20+ sellers, thousands of SKUs, and approximately $5–10k USD monthly throughput on AWS Kubernetes production infrastructure

**Stream Finance — Principal Architect / Founding Engineer**

- Served as principal architect and founding engineer for Stream Finance, designing and building smart-contract and cloud operations infrastructure for an on-chain investment product backed by US Treasury bonds and other fixed-income instruments
- Architected AWS-backed operational infrastructure around the smart contracts: secure key management (AWS KMS, Secrets Manager), ECS Fargate event listeners, SQS-backed deposit finalization with idempotency and DLQs, Step Functions lifecycle approval workflows requiring human review before high-risk transactions, EventBridge rate processing, invariant monitoring, reconciliation jobs, and CloudWatch/SNS/SES alerting
- Designed phase-based investment lifecycle on Ethereum mainnet: stablecoin deposits, Vault Token issuance, deposit/lock/withdraw phases, sequential rounds, rollover-based compounding, and admin-set exchange-rate/yield updates secured behind configurable role separation and multisig-style admin ownership
- Built a multi-layer smart-contract testing strategy using Hardhat, Chai/Ethers.js, randomized multi-user round simulations, Echidna invariant testing, and manual penetration testing for a production-grade financial protocol
- Systems secured hundreds of millions USD in TVL at peak; the architecture became the foundation for XUSD, a same-company stablecoin with hundreds of thousands USD in financial exposure

**QuantGenie — Principal Architect (Consultant)**

- Engaged as principal architect and technical consultant: gathered requirements, proposed the initial system architecture and phased roadmap, and delivered a working proof of concept for an AI-assisted algorithmic trading platform targeting retail traders
- Built a constrained LLM generation pipeline: multi-turn Anthropic Claude conversation engine elicits clarifications, generates QSDL (a proprietary typed JSON DSL), validates against a rich AJV schema with LLM self-correction on failure, then compiles through a platform-agnostic AST to executable MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#) code
- Translated an ambiguous product concept into concrete system architecture, component boundaries, and a phased delivery plan; established technical foundations and handed off to a development team with documentation and early team structure
- Designed the backtesting engine architecture for later-stage implementation: data ingestion pipeline, OHLCV streaming, deterministic AST evaluation, job queuing, and concurrent isolation

**Private Client — Principal Architect / Data-Driven Trading Systems**

- Sole architect and developer of a live, real-money prediction-markets trading platform for a private trader client, supporting Kalshi and Polymarket execution, historical backtesting, Bayesian/Optuna parameter optimization, and embedded LLM agents for strategy analysis and diagnostics
- Designed a modular TypeScript strategy framework where trading strategies are implemented as classes behind a shared interface, enabling consistent backtesting, optimization, comparison, and live execution across multiple strategy families including Avellaneda-Stoikov market making and OFI market making
- Built configurable backtesting with train/test split, side-by-side comparison, and metrics including Calmar ratio, Profit Factor, P&L, max drawdown, Sharpe ratio, and win rate; modeled fees, slippage, and latency for pre-deployment strategy validation
- Designed data flows spanning Kalshi, Polymarket, and ESPN API ingestion, Google Bigtable historical storage, and PostgreSQL-backed backtesting and analysis; embedded LLM agents for strategy-code generation, diagnostic parsing, and parameter-tuning assistance

**PFP Capital — Solana Low-Latency Trading Systems Engineer**

- Sole architect and developer of a live Rust/Tokio Solana copy-trading system: Helius LaserStream WebSocket detection of monitored-wallet swaps, Jito tip routing, Helius priority transaction broadcasting, Pump.fun and Jupiter execution routing, concurrent position monitoring, trailing stop-loss with peak P&L tracking, configurable risk controls, and GCP Secret Manager key management
- Designed event-driven Rust backend using Tokio async runtime, shared Arc-wrapped application state, concurrent position-monitoring tasks, and structured WebSocket telemetry broadcast to a React 18/TypeScript operator dashboard with Google OAuth/JWT-gated access
- Built a Python/FastAPI research and backtesting platform that reconstructs Solana wallet trade histories from Helius enhanced transaction data, parses swaps across 11 DEXs, applies FIFO P&L matching, and backtests copy-trading strategies with configurable latency assumptions before live capital deployment

---

## ADDITIONAL EXPERIENCE

- Morgan Stanley — Senior .NET Developer (Global Wealth Management platform, fixed income and currency trading systems, .NET/C# and COBOL mainframe integration, TDD leadership)
- Alteryx — Senior Engineer (C++ back-end engine for enterprise data analytics platform, complex defect resolution, cross-platform Windows/Linux)
- Leeds Rising — Algorithmic Trading Engineer (Python short-selling strategies, composable trigger/trade architecture, live US equities deployment)
- Skunk Capital — System Owner (automated crypto cash-and-carry arbitrage, NodeJS/AWS, BitMEX/Bitfinex/Kraken/Binance, six-figure deployed capital)
- Budgie — Discovery Architect (layered LLM orchestration architecture for Singapore AI personal finance platform, formal 3-week Toptal discovery engagement)
- Manao Software, HotelTravel, Aquamonix (additional history available on request)

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

---

## TOOLS & TECHNOLOGIES (SELECTED)

- Python
- TypeScript
- Rust
- C++
- AWS, GCP
- Kubernetes
- PostgreSQL
- Kafka
- LLM Integration
- Cloud Infrastructure
- Data Pipelines
- Full-Stack Systems
- Solidity
- Trading Infrastructure
- Smart Contract Security

---

## AVAILABILITY

Senior / Distinguished / Principal-level roles requiring technical leadership, full-lifecycle system ownership, and architectural decision authority across cloud and distributed systems.

---

## CITIZENSHIP

US Citizen

---

## Sourcing notes

**Positions used:** CTO-Hamza/Hamza-General-CTO-Leadership, FoundingEngineer-StreamFinance, FoundingArchitect-Quantgenie, TradingEngineer-PrivateClient, LowLatencyTradingEngineer-PFPCapital

**Lineup rationale:**
Capital One emphasizes cloud (AWS/GCP/K8s), technical leadership and mentoring, full lifecycle from conception through production support, non-functional characteristics (scalability, performance, operability), and cross-org technical influence. Hamza leads because it is the strongest leadership entry (CTO, six developers, AWS/K8s production) and most recent. Stream Finance provides the strongest cloud architecture and financial systems evidence. QuantGenie maps directly to "decompose complex problems into practical solutions." Private Client and PFP Capital demonstrate current production ownership across AI, distributed systems, and cloud.

**Gaps relative to posting:**
- Capital One's preferred qualifications include 10+ years networking experience (BGP, SD-WAN, Cloud Networking, Data Center Networking). This is not covered in the evidence bank and has not been claimed.
- Java and Go are preferred languages but are not in John's primary stack. TypeScript and Python are present and claimed.
- "Cloud" (3+ years) is met through AWS (Stream Finance, Hamza) and GCP (PFP Capital), but cloud is not positioned as John's primary brand in the canonical resume; it is framed here as a genuine capability rather than an invented one.

**Softened/omitted:**
- HD wallet / BIP32/BIP39 production scope across all chains: described as "per-payment holding wallets" and "canonical settlement" to reflect what is Safe to Claim per the Hamza evidence bank. BIP32/BIP39 production scope is Use With Care and has not been stated explicitly.
- Stream Finance AWS reference architecture: described as "architected" for cloud components, consistent with the evidence bank caveat that the exact split between fully implemented vs designed/prototyped should be confirmed before external claims.
- No exact TVL or AUM figures for XUSD beyond what is stated as Safe to Claim ("hundreds of thousands USD in financial exposure").
