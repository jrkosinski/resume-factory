# JOHN R. KOSINSKI

Senior Systems Architect • Principal Engineer • Operator

---

## SUMMARY

Senior technologist and system owner specializing in high-risk, high-constraint environments across blockchain, financial markets, distributed systems, and AI-integrated trading infrastructure. Known for owning systems end-to-end where failure carries real financial, operational, or reputational consequences; from on-chain escrow holding investor capital to live algorithmic trading bots executing with real money. Brings ideas from concept to production under uncertainty, minimal resources, and tight constraints, spanning solo founding-engineer engagements, CTO-level team leadership, and precise technical consulting. Combines deep Solidity and Rust engineering with LLM pipeline design, quant trading system architecture, and the judgment to know when to automate and when to gate on human approval.

---

## CORE CAPABILITIES

- System ownership under financial and operational risk
- Constraint-driven architecture (security, capital, latency, irreversibility)
- Blockchain and DeFi system design (EVM, Solana, cross-chain, tokenomics)
- Smart contract architecture and multi-layer security testing (Solidity, Rust, Echidna, Foundry, Hardhat)
- Low-latency trading systems (Rust/Tokio, Solana execution, exchange integrations)
- LLM pipeline design and constrained AI generation integrated with deterministic code
- Distributed systems, event-driven architecture, and cloud operations (AWS, GCP, Kubernetes)
- Quantitative trading system design: execution, backtesting, optimization, and live deployment
- Financial product modeling (tokenized RWA, escrow mechanics, payment state machines)
- Engineering leadership and team management (6–30 developers) with hands-on delivery

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

---

### Budgie: Technical Software Architect / Discovery (via Toptal)

_April – May 2026_

- Served as technical architecture lead on a formal 3-week discovery engagement for a Singapore AI personal finance startup; technical member of a 3-person team (architect, product manager, UI/UX designer).
- Designed complete C4-level system architecture across six diagrams; system context, container structure, financial core components, AI service layers, and notifications pipeline; for a platform integrating Finverse bank aggregation, Goldrush blockchain data (Bitcoin, Ethereum, Solana, EVM L2s), crypto exchange APIs, CoinGecko pricing, and Anthropic Claude as LLM.
- Designed a layered LLM orchestration architecture (Personality, Policy/Guardrails, Tools, Context & History, Explainability, PII Detection, LLM Abstraction, Token Usage Tracking) with a deterministic calculation Tools layer to prevent hallucination in financial AI outputs.
- Designed the Financial Data Aggregation Hub; Canonical Model Mapper, Account Consolidator, Derived Metrics Builder, Query API; feeding a Financial Health Score service, transaction categorization engine, goals/budgeting engine, and proactive insights engine.
- Identified Finverse's 2FA-per-refresh constraint as the primary engagement-model risk, triggering an alternative aggregator evaluation; flagged Asian-market transaction categorization as a build-vs-buy decision.
- Contributed technical scoping to a 421-feature product backlog across 16 epics and recommended RAG grounding with curated sources and MAS/PDPA regulatory compliance constraints for LLM deployment.

---

### QuantGenie: Principal Architect / Technical Consultant

_November 2025 – February 2026_

- Engaged as principal architect and technical consultant to gather requirements, propose system architecture and roadmap, and deliver a working proof of concept for an AI-assisted algorithmic trading platform targeting retail traders.
- Built the core POC pipeline: a multi-turn Anthropic Claude conversation engine (with ephemeral prompt caching) elicits clarifying questions, generates QSDL; a proprietary typed JSON DSL for trading strategies with 50+ indicator type definitions; validates the output against an AJV schema with LLM self-correction on failure (up to 5 retries), then compiles the validated spec through a platform-agnostic AST to executable MetaTrader 5 (MQL5) and NinjaTrader (NinjaScript/C#) code.
- Designed a constrained LLM generation pipeline where Claude generates within a typed JSON schema rather than free-form; in-loop schema validation and self-correction converge to a valid spec before any output is accepted downstream.
- Designed the backtesting engine architecture; deterministic QSDL interpretation streaming historical OHLCV candles through AST evaluate() methods with multi-timeframe and multi-instrument support; scoped for a later implementation stage.
- Established technical foundations, architecture documentation, and early team structure; handed off to a development team to continue full build-out.

---

### PFP Capital / Semi-Private Client: Rust Low-Latency Trading Systems Engineer

_December 2025 – Present_

- Sole architect and developer of a live, real-money Solana copy-trading system: Rust/Tokio execution engine, React/TypeScript operator dashboard, and Python/FastAPI research and backtesting platform.
- Production backend subscribes to real-time Solana log streams through Helius LaserStream WebSockets, detects monitored-wallet swaps with sub-second latency, and autonomously routes copy trades through Pump.fun bonding-curve execution (pre-graduation tokens) or the Jupiter DEX aggregator (broader liquidity).
- Execution uses Jito tip routing, Helius priority transaction broadcasting, supply-aware position sizing, and trailing stop-loss with peak P&L tracking; concurrent position monitoring tracks multiple open trades through shared Arc-wrapped Tokio async state.
- Built a Python/FastAPI research and backtesting platform that reconstructs wallet trade histories from Helius enhanced transaction data, parses swaps across 11 DEXs, applies FIFO P&L matching, computes Sharpe ratio, max drawdown, win rate, P&L distributions, and cumulative returns, and measures copy-latency slot/time deltas before committing real capital.
- System is live in production with real money and currently profitable at small but increasing scale as execution parameters, risk controls, and target-wallet selection are tuned.

---

### Private Client: AI/Trading Systems Engineer (Prediction Markets)

_January 2026 – Present_

- Sole architect and developer of a live, real-money prediction-markets trading execution and backtesting platform for a private trader client, supporting Kalshi and Polymarket.
- Built a modular TypeScript strategy framework where strategies are implemented as classes behind a shared interface, enabling consistent backtesting, optimization, comparison, and live execution across multiple strategy families including Avellaneda-Stoikov market making, OFI market making, and a modified Dutch Arbitrage spread-capture strategy.
- Designed a full-stack research platform: Kalshi/Polymarket/ESPN data ingestion, Google Bigtable historical storage, PostgreSQL-backed backtesting engine with train/test split, side-by-side strategy comparison, Bayesian parameter optimization through Optuna, and metrics including Calmar ratio, Profit Factor, P&L, drawdown, Sharpe ratio, ROI, and expectancy.
- Embedded lightweight LLM-wrapper agents for strategy-code generation, diagnostic parsing, backtest interpretation, parameter-tuning suggestions, and trading analysis; designed tool-use, structured-output, and workflow-based agent patterns without unnecessary orchestration complexity.
- Moved the client from high-risk, unreliable P&L behavior toward more deterministic, better-tested strategies generating small but increasing real-money profits.

---

### Hamza: CTO and Co-Founder

_January 2024 – January 2026_

- Served as CTO and co-founder, leading a six-developer engineering team across frontend, backend, seller admin, payment infrastructure, smart contracts, tokenomics, infrastructure, and production operations for a live decentralized e-commerce platform with hundreds of monthly users, 20+ sellers, thousands of SKUs, and ~$5k–$10k USD monthly throughput.
- Architected and delivered a production cross-chain crypto payment system supporting Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, and other EVM L2s: payment intents, dedicated per-payment holding wallets, chain listeners, EventBridge and SQS event processing, idempotent verification, immediate Optimism escrow settlement, merchant webhooks, and LiFi-based batch settlement.
- Architected Hamza's Solidity multi-tenant escrow on Optimism; PaymentEscrow with ETH/ERC-20 payments, unique payment IDs, dual buyer/seller consent release, configurable protocol fees, partial/full refunds, arbiter resolution, Hats Protocol role integration, seller-delegated release/refund admins via PaymentEscrowAdmins, EscrowMulticall batching, and precision-safe fee arithmetic; tested through Hardhat/Mocha/Chai TypeScript tests, ~165 Foundry Solidity tests, and Echidna property-based fuzzing campaigns running 80,000-transaction runs.
- Built a live multitenant e-commerce storefront using MedusaJS, NestJS, Next.js, TypeScript, PostgreSQL, Redis, AWS Kubernetes, and EventBridge/SQS, customized for wallet-based crypto checkout and NFT-based seller identity.
- Advised on utility-token tokenomics (seller escrow rent, initial seller mint, token-incentivized dispute resolution) and co-developed tokenomics-related Solidity contracts including vault and governance-wrapper components deployed to Optimism and Optimism testnet.
- Established production engineering practices: CI/CD, backend tests, payment-system tests, smart-contract tests, dev/staging/testing environments, monitoring, alerting, code review, and repository management.

---

### Stream Finance: Principal Architect and Founding Engineer

_2022 – 2023_

- Designed and implemented mission-critical on-chain financial primitives supporting bond rollover and compounding yield for an EVM investment protocol backed by short-term US Treasury bonds and fixed-income instruments.
- Architected a modular Solidity contract suite; upgradeable Vault/VaultToken contracts, SecurityManager RBAC layer, optional Whitelist, DepositVault sweep-in flow, and precision-safe exchange-rate arithmetic; supporting deposit/lock/withdraw phases, sequential investment rounds, rollover-based compounding, stablecoin deposits, and admin-set exchange rates.
- Implemented system and security architecture for the back-office settlement system driving bond vault operations; systems secured hundreds of millions USD in TVL at peak during the initial phase.
- Built a multi-layer smart-contract testing strategy: Hardhat unit tests, randomized multi-user round simulations (5 epochs, 10 concurrent users, 12 rounds per epoch, verified against an off-chain profit ledger within 50 wei), and Echidna invariant campaigns covering value conservation, admin-role survivability, whitelist enforcement, and proxy upgrade authorization.
- Architected AWS-backed operational infrastructure: deposit finalization pipeline, lifecycle management with human approval gates, exchange-rate oracle and drift monitoring, audit and invariant monitoring, rollover and position reconciliation, and secure key management; system later became the foundation for XUSD, a stablecoin product with hundreds of thousands USD in TVL.
- Operated with only one junior developer; security and correctness were non-negotiable; made irreversible architectural decisions under capital-at-risk constraints.

---

### Leeds Rising: Algorithmic Trading Engineer

_2023 (approx. 6 months)_

- Built PyDAS; a robust, complete, and rigorously tested Python API to the DAS Trader platform; covering buying, selling, borrowing, and short-selling of US equities; served as the foundation for Leeds Rising's algorithmic trading infrastructure.
- Built an algorithmic trading system on PyDAS with a composable architecture: configurable Trigger layer for signal specification and plug-and-playable Trade logic modules enabling dynamic strategy assembly without system rewrites.
- Implemented short-selling and borrowing strategies for illiquid Nasdaq and NYSE stocks and deployed those strategies against the live market with real capital; proven profitable in live trading.

---

### Skunk Capital: System Owner / Crypto Arbitrage Trading Engineer

_2017 – 2019_

- Sole architect and developer of a profitable crypto cash-and-carry arbitrage system, exploiting pricing discrepancies between cryptocurrency futures and spot markets on BitMEX, Bitfinex, Kraken, and Binance.
- Built exchange-specific plugins abstracting market data, authentication, order placement, balance retrieval, rate limits, retries, and venue-specific API behavior behind a shared arbitrage execution framework.
- Automated previously manual cash-and-carry arbitrage strategies with real capital; designed trading infrastructure for durability and longevity; system operated with hundreds of thousands USD in deployed capital.
- Implemented automated two-leg execution with partial-fill handling, failed-leg recovery, retry logic, rate-limit handling, position tracking, and unwind workflows; modeled funding rates, borrow costs, trading fees, and slippage to validate trade viability.

---

### Axiomsys: Blockchain Consultant

_2022 – 2023_

- Served as blockchain consultant at Axiomsys, scoping and estimating NFT, fungible token, front-end minting website, and smart contract security audit project packages across Ethereum (Solidity) and Solana (Rust) ecosystems.
- Researched, planned, and delivered a stakeholder presentation on integrating fungible and non-fungible tokens into the Unity game engine back end of a well-known online meeting venue.
- Built the foundation for Axiomsys's international blockchain engineering team; contacting, vetting, and interviewing developers across the global Web3 talent pool.

---

### Alteryx: Senior C++ Engineer

_2019 – 2022_

- Developed and maintained the core C++ back-end engine of Alteryx's enterprise data analytics platform, resolving customer and internal defects and delivering new features in C++ 11 on Windows and Linux.
- Took ownership of some of the most long-standing and difficult defects in the Alteryx engine; performing deep root cause analysis, documenting findings thoroughly, and implementing regression tests to prevent recurrence.
- Managed the full defect lifecycle within a 6–8 person engine team, coordinating cross-team to gather information and drive resolution of complex issues.

---

### Morgan Stanley: Senior .NET Developer

_2006 – 2009_

- Developed back-end logic for a new fixed-income product interface within Morgan Stanley's Global Wealth Management Platform.
- Designed and integrated .NET modules bridging modern application code with legacy COBOL mainframe systems.
- Pioneered test-driven development (TDD) policies across the department, implementing automated testing standards across multiple projects and establishing a culture of test-first engineering.

---

## ADDITIONAL EXPERIENCE

- **HotelTravel.com: Software Development Manager** (Phuket, Thailand, 2009–2012): Managed a department of 20–30 developers; architected a full overhaul of the back-end booking engine integrating hotel rate data from multiple provider categories; established TDD and QA policies; mentored developers on design patterns, mobile, and engineering best practices.

- **Manao Software: Senior Team Leader** (Chiang Mai, Thailand, 2012–2014): Led 10–20 developers to deliver a REST/JSON API front-end layer over EveryAngle's SAP-querying interface; designed architecture using .NET Web API with MVVM and NHibernate; directed QA and served as primary liaison to the client's executive team.

- **Garbles Labs: Blockchain/SDK Developer** (2022): Ported the Orca Whirlpools TypeScript SDK to C#/.NET for the Unity game engine; released open-source for community use; built automated test coverage and modified Orca's Rust smart contracts for testability.

- **Soundbeats: Sole Blockchain Engineer** (GameFi prototype): Built Sui Move smart contracts for fungible in-game points and NFT avatars, a secure NestJS REST API for game-to-blockchain minting flows, and Unity proof-of-concepts for authentication and smart wallet onboarding via Google OAuth.

- **Event Driven Investor: Quant Developer / Consultant** (2016): Corrected Pearson's correlation calculations in Pairtrade Finder, improved correlation algorithms for financial asset price series analysis, refactored the C# codebase, and added automated tests to surface and fix latent bugs; integrated with the Interactive Brokers API.

- **Aquamonix: Mobile Developer / iOS Architect** (2015–2017): Built from scratch a Xamarin iOS application controlling large-scale SCADA irrigation systems via a Java middle tier; designed the MVP architecture, cross-platform portability plan, and a long-running task synchronization system across multiple WebSocket connections and app sessions.

- **FreshDirect: Mobile Developer** (via Door3, 2014–2016): Contributed backend and frontend development for FreshDirect's Android and iOS mobile app on a ~10-person team using Java, Objective-C, and Xamarin; the app won a Webby Award.

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

---

## TOOLS & TECHNOLOGIES (SELECTED)

- **Languages:** Solidity, Rust, TypeScript, Python, C++, C#, JavaScript/Node.js
- **Blockchain:** Ethereum, Optimism, EVM L2s, Solana, Sui Move, Bitcoin; Foundry, Hardhat, Echidna, OpenZeppelin, Hats Protocol, Ethers.js, Jito, Helius, Jupiter, Pump.fun
- **AI/LLM:** Anthropic Claude API, LLM pipeline design, constrained generation, prompt caching, RAG, MCP, tool-augmented orchestration
- **Trading/Quant:** Algorithmic trading systems, backtesting engines, Optuna/Bayesian optimization, FIFO P&L, DAS Trader, Kalshi, Polymarket, Helius LaserStream
- **Cloud/Infra:** AWS (Lambda, ECS Fargate, EventBridge, SQS, Step Functions, RDS, DynamoDB, Secrets Manager, KMS, S3, CloudWatch), GCP, Kubernetes
- **Backend:** NestJS, FastAPI, MedusaJS, PostgreSQL, Redis, Google Bigtable, Tokio
- **Frontend:** React, Next.js, Vite, TypeScript, TanStack Query, Tailwind CSS
- **Smart Contract Security:** Echidna, Foundry, Hardhat, randomized fuzzing, invariant testing, manual penetration testing

---

## AVAILABILITY

Senior / Principal-level roles where early ownership, architecture under risk, and decision authority are required; including blockchain systems, trading infrastructure, AI-integrated systems, and high-constraint distributed systems.

---

## CITIZENSHIP

US Citizen
