# JOHN R. KOSINSKI

Senior Systems Architect • Principal Engineer • Operator

---

## SUMMARY

Senior technologist and system owner with over fifteen years of experience building production systems across blockchain, decentralized finance, automated trading, fintech infrastructure, and enterprise software. Known for owning complex technical problems end-to-end - from concept through architecture, implementation, and production operations - in environments where failure carries real financial, operational, or reputational consequences. Currently active across live real-money trading systems, Web3 infrastructure, AI-assisted engineering, and technical discovery engagements via Toptal.

Primary strengths include system ownership under risk, constraint-driven architecture, technical decision authority in ambiguous environments, and the ability to translate complex domain requirements into production-grade systems with minimal support structure.

---

## CORE CAPABILITIES

- System ownership under financial and operational risk
- Constraint-driven architecture (security, capital, latency, irreversibility)
- Blockchain & DeFi system design (EVM, Solana, Sui, cross-chain, tokenomics)
- Smart contract architecture, security, and multi-layer testing (Solidity, Sui Move, Echidna, Foundry)
- Distributed systems, event-driven architecture, and data pipelines (Kafka, Kubernetes, cloud infrastructure)
- Financial & risk modeling
- Automated trading system design and ownership (crypto arbitrage, prediction markets, copy-trading)
- LLM orchestration and AI-assisted systems combined with deterministic code
- Technical discovery, C4 architecture, and pre-build scoping
- Team leadership, CTO-level technical strategy, and startup co-founding
- Clear technical decision-making under uncertainty

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

---

### Budgie - Technical Software Architect (Toptal Discovery Engagement)

_Apr–May 2026 · Singapore AI Personal Finance Startup · 3-week formal discovery_

- Served as the technical architecture lead on a formal 3-week Toptal discovery engagement for Budgie, a Singapore AI personal finance startup; sole technical member of a 3-person discovery team (architect, product manager, UI/UX designer), producing six C4-level architecture diagrams covering system context, container decomposition, financial core components, AI service layers, and a cross-cutting notifications pipeline.
- Designed a layered LLM orchestration architecture - Personality, Policy/Guardrails, Tools, Context & History, Explainability, PII Detection, LLM Abstraction, and Token Usage Tracking layers - where deterministic calculation tools replace inline LLM arithmetic to prevent hallucination in financial outputs; recommended Anthropic Claude as the LLM provider and scoped RAG grounding with curated source citations for financial knowledge queries.
- Designed the Financial Data Aggregation Hub with canonical model mapping, cross-source account consolidation, and a derived metrics layer feeding a Financial Health Score service, transaction categorization engine (rule-based plus AI-assisted, with Asian-market localization flag), goals/budgeting engine, and proactive insights engine; assessed Finverse (bank aggregation, SG/HK), Goldrush API (multi-chain blockchain wallet data), and CoinGecko (crypto pricing) for the integration stack.
- Contributed technical scoping to a 421-feature product backlog across 16 epics (Private Beta through v2+), identified Finverse's 2FA-per-refresh constraint as the primary engagement-model risk before build commitment, and flagged MAS and PDPA regulatory constraints shaping AI guardrail design and LLM data retention requirements.
- Designed a consent-first notifications pipeline with intake API, preference/consent check, deduplication, throttling, content building, and multi-channel routing (push via Expo/OneSignal, email) feeding proactive AI coaching cadences.

---

### Prediction Markets Trading Engine - AI/Trading Systems Engineer

_Jan 2026–Present · Private Trader Client · Kalshi, Polymarket_

- Sole architect and developer of a live, real-money prediction-markets trading platform for a private trader client supporting Kalshi and Polymarket execution, currently in production at small but increasing profitability; owns full client relationship, architecture, strategy framework, data engineering, AI integration, frontend, and production operations.
- Designed a modular TypeScript strategy framework where each strategy is implemented as a class behind a shared interface, enabling consistent backtesting, parameter optimization, side-by-side comparison, and live execution across strategy families including Avellaneda-Stoikov market making, OFI market making, and a modified Dutch Arbitrage spread-capture model for ranging markets.
- Built a configurable backtesting engine with train/test split support, Bayesian parameter optimization via Python/Optuna, and comprehensive metrics including Calmar ratio, Profit Factor, P&L, max drawdown, inventory risk, ROI, expectancy, Sharpe ratio, and win rate; modeled fees, slippage, and latency to improve strategy evaluation reliability before live deployment.
- Embedded lightweight LLM-wrapper agents (tool-use, structured-output, and workflow-based) for strategy-code generation, backtest interpretation, parameter-tuning suggestions, and diagnostic analysis; AI outputs optionally saved with backtest sessions for audit; agents prevented from accessing sensitive data.
- Built market-data ingestion workflows from Kalshi, Polymarket, and ESPN APIs into Google Bigtable for historical storage and PostgreSQL for backtesting; built a TypeScript/Vite/Tailwind frontend exposing backtests, optimization runs, live session data, strategy parameter sets, dashboards, AI-assisted strategy generation, and live trading controls.

---

### Hamza - CTO & Co-Founder

_Jan 2024–Jan 2026 · Decentralized E-Commerce · Six-developer team · Live production_

- Served as CTO and co-founder of Hamza, a live decentralized e-commerce platform with hundreds of monthly users, 20+ sellers, thousands of SKUs, and ~$5k–$10k USD monthly throughput; led a six-developer engineering team across frontend, backend, seller admin, cross-chain payment infrastructure, Solidity smart contracts, tokenomics, AWS/Kubernetes infrastructure, CI/CD, and production operations.
- Architected a production cross-chain crypto payment system using payment intents, per-payment one-time holding wallets (HD wallet / BIP32/BIP39 address derivation), chain listeners, EventBridge/SQS event processing, idempotent verification, immediate Optimism canonical escrow settlement, merchant webhooks, and LiFi-based batch settlement replenishment - supporting Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, and other EVM L2s; Solana payment support was built but not deployed.
- Architected Solidity escrow contracts (`PaymentEscrow`, `EscrowMulticall`, `SystemSettings`) deployed to Optimism, implementing consent-based buyer/seller release/refund state machines, Hats Protocol role models, protocol fees, seller-delegated admin permissions, and a multi-service NestJS payment backend (address-store, payment-processor, payment-admin-api) coordinated through a shared pnpm monorepo common package; tested with Foundry, Hardhat, and Echidna.
- Led development of the flagship multitenant decentralized marketplace using MedusaJS, NestJS, Next.js, TypeScript, PostgreSQL, Redis, EventBridge/SQS, AWS EC2, AWS RDS, AWS S3, and Kubernetes, supporting inventory, product sorting/filtering, cart, wishlist, user management, notifications, seller administration, wallet-based checkout, and NFT-based on-chain seller identity.
- Co-designed utility token tokenomics - seller escrow rent, initial seller mint, dispute-resolution incentives, vault contracts, and governance wrappers - and established production engineering practices including CI/CD, backend tests, payment-system tests, smart-contract tests, dev/staging/testing environments, monitoring, and alerting across the full stack.

---

### PFP Capital - Solana Copy-Trading Systems Architect

_Dec 2025–Present · Semi-Private Client · Live real-money trading_

- Sole architect and developer of a live, real-money Solana copy-trading system for PFP Capital; owns full client relationship, architecture, data design, implementation, testing, diagnostics, deployment, and production operations for a latency-sensitive trading system currently operating profitably at small but increasing scale.
- Built the production Rust/Tokio execution engine: subscribes to real-time Solana blockchain log streams via Helius LaserStream WebSockets, detects monitored-wallet swaps with sub-second latency using shared `Arc`-wrapped async application state, routes copy trades through Pump.fun bonding-curve execution for pre-graduation tokens or Jupiter DEX aggregator for broader liquidity, and monitors multiple open positions concurrently.
- Implemented Jito tip routing and Helius priority transaction broadcasting for MEV-aware execution; built risk controls including supply-aware position sizing, trailing stop-loss with peak P&L tracking, configurable risk tiers, max slippage, liquidity-based price-impact limits, wallet/token filters, and max holding-time guards; integrated GCP Secret Manager for private key management.
- Built a Python/FastAPI research and backtesting platform that reconstructs Solana wallet trade histories from Helius enhanced transaction data, parses swaps across 11 DEXs, computes FIFO P&L, Sharpe ratio, max drawdown, win rate, P&L distributions, and cumulative returns, and backtests copy strategies with pluggable `ITradingStrategy` hooks, configurable latency assumptions, and copy-latency measurement using slot/time deltas.
- Built a React 18/TypeScript operator command dashboard with Vite, Tailwind, TanStack Query, persistent WebSockets with exponential-backoff reconnect, Google OAuth 2.0/JWT-gated access, live positions, P&L multipliers, color-coded log stream, background task heartbeats, graceful shutdown, force-sell, and wallet-list management.

---

### Stream Finance - Principal Architect & Founding Engineer

_2022–2023 · EVM Bond Vault / Tokenized US Treasury Investment System_

- Served as principal architect and founding engineer for Stream Finance, designing and building the smart-contract and cloud operations infrastructure for an EVM-based investment protocol backed by short-term US Treasury bonds and other fixed-income instruments; the system later became the technical foundation for XUSD, a same-company stablecoin product.
- Architected a modular Solidity contract suite - `Vault`, `VaultToken`, `SecurityManager`, optional `Whitelist`, `DepositVault`, and precision-safe `CarefulMath` exchange-rate arithmetic - supporting stablecoin deposits, Vault Token issuance, Deposit/Locked/Withdraw phases, sequential investment rounds, rollover-based compounding, admin-controlled exchange-rate updates, and stablecoin redemption; deployed to Ethereum testnet and mainnet.
- Built a multi-layer smart-contract testing strategy using Hardhat/Chai/Ethers.js, randomized multi-user round simulations (5 epochs × 10 users × 12 rounds, accounting tolerance under 50 wei), and Echidna invariant campaigns covering value conservation (`vault_cannot_leak_money`), admin-role survivability, role-safety boundaries, whitelist enforcement, proxy upgrade authorization, and storage-slot immutability; performed manual penetration testing and internal security review.
- Architected AWS-backed operational infrastructure: deposit-finalization pipeline (ECS Fargate listener → SQS → Lambda, idempotent with RDS transaction check), lifecycle-management workflow (EventBridge → Step Functions → human approval gate → Lambda, phase/rate transitions require human sign-off), exchange-rate oracle and drift monitoring, and production invariant monitoring with immutable S3/Kinesis audit logs and CloudWatch/SNS alerting.
- Designed a shared SecurityManager access-control layer over OpenZeppelin RBAC with fine-grained roles for lifecycle management, deposits, pausing, minting, burning, and upgrades; kept privileged rate/yield authority restricted to secure administrative contract calls rather than ordinary dashboard controls; managed delivery of frontend/admin dashboard by a developer under my oversight.

---

### QuantGenie - Founder & Principal Architect

_~2023–2024 · Natural Language → Trading System_

- Conceived, validated, and built the technical foundation for QuantGenie, a natural-language → DSL → compiled trading system targeting retail traders; served as sole technical owner responsible for feasibility analysis, system architecture, and proof-of-concept execution from scratch.
- Designed a constrained LLM generation pipeline integrated with deterministic compilation and execution, separating AI-generated strategy descriptions from compiled, auditable trading logic to prevent hallucination in generated trading behavior.
- Architected the backtesting data ingestion and processing pipeline, including data normalization, storage strategy, and execution flow; established technical foundations, process architecture, and early team structure.

---

### Soundbeats - Blockchain Engineer

_~2023 · Sui GameFi / Music Gaming Prototype_

- Served as sole blockchain engineer for Soundbeats, a Sui-based GameFi prototype that used tokenized in-game points and NFT-based characters/avatars to gamify a Beat Saber-like music experience; worked cross-functionally with designers, game developers, and marketing stakeholders on an early-stage prototype that received outside attention and investment.
- Built Sui Move smart contracts for fungible in-game points and NFT-based game assets using Sui-native object ownership and minting patterns, including built-in on-chain tests and best-practice package structure.
- Developed a secure NestJS REST API as the integration layer between the Unity game client and Sui blockchain, implementing backend-controlled minting authorization; prototyped Google OAuth smart-wallet onboarding and learned sufficient Unity to create proof-of-concept REST API communication, authentication, and end-to-end minting validation before game developer handoff.

---

### Skunk Capital - Algorithmic Trading Systems Engineer

_2017–2019 · Crypto Cash-and-Carry Arbitrage · Remote / Perth, Australia_

- Served as sole architect and developer of a profitable crypto cash-and-carry arbitrage trading system for Skunk Capital, exploiting pricing discrepancies between cryptocurrency spot and futures markets; system operated with approximately $100K USD in deployed capital and ran continuously in production for sustained periods.
- Built exchange-specific plugins for BitMEX, Bitfinex, Kraken, and Binance, abstracting market data, authentication, order placement, balance retrieval, rate-limit handling, retry behavior, and venue-specific API differences behind a shared arbitrage execution framework.
- Implemented automated two-leg cash-and-carry execution including futures/spot basis detection, cost modeling (funding rates, borrow costs, trading fees, slippage), automatic execution of both legs, partial-fill handling, failed-leg recovery, retry logic, position tracking, and unwind workflows.
- Built NodeJS/AWS trading services on EC2 with MySQL-centered persistence, WebSocket exchange feeds, ReactJS operational dashboard, and homemade logging, monitoring, and alerting; hardened the system against real exchange edge cases for reliable continuous production operation.

---

### Alteryx - Senior Engineer

_Data and Analytics Platform · C++_

- Worked within a large, mature, and undocumented C++ framework supporting complex data and analytics workloads; rapidly oriented in a highly unfamiliar codebase and became independently productive.
- Diagnosed and resolved production defects appearing in new and non-obvious areas of the system; implemented and tested fixes across multiple subsystems under production constraints.

---

## ADDITIONAL EXPERIENCE

- **Leeds Rising** - Sole developer of an automated short-trading system targeting US equity markets
- **Aquamonix** - Backend engineering for an IoT-based water management platform
- **Morgan Stanley** - Software engineering in financial services infrastructure
- **HotelTravel** - Full-stack engineering for a hospitality / travel e-commerce platform
- **Manao Software** - Software engineering across agency and product work

_(Details available on request)_

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication
- Translate ambiguity into architecture, not assumptions

---

## TOOLS & TECHNOLOGIES (SELECTED)

**Languages:** Solidity, Rust, TypeScript, Python, JavaScript / Node.js, C++, Sui Move

**Blockchain & Web3:** Ethereum, Optimism, Arbitrum, Polygon, Solana, Bitcoin, Sui, EVM L2s · Foundry, Hardhat, Echidna, OpenZeppelin, Ethers.js v6, @solana/web3.js, bitcoinjs-lib · Helius (LaserStream, enhanced transaction API), Jito, Jupiter, Pump.fun, LiFi · Hats Protocol, UUPS proxy upgradeability, RBAC

**Backend:** NestJS, FastAPI, MedusaJS, Express / Node.js · EventBridge/SQS, Kafka, SQS, EventBridge · REST, WebSockets, event-driven architecture

**Frontend:** React 18 / Next.js, TypeScript, Vite, Tailwind CSS, TanStack Query, TanStack Router, Zustand, Zod, Radix UI, Recharts

**Data:** PostgreSQL, Redis, DynamoDB, Google Bigtable, Amazon Timestream, MySQL, MongoDB

**Cloud & Infrastructure:** AWS (EC2, RDS, S3, Lambda, ECS Fargate, EKS, SQS, SNS, EventBridge, Step Functions, Secrets Manager, KMS, CloudWatch, CDK, S3 Object Lock) · GCP (Secret Manager) · Kubernetes · CI/CD, monitoring, alerting

**AI / LLM:** Anthropic Claude, layered LLM orchestration, RAG, MCP, tool-augmented AI, PII detection, hallucination-prevention architecture, Optuna (Bayesian optimization)

**Trading Infrastructure:** Kalshi, Polymarket, Helius LaserStream, Jito, Jupiter, Pump.fun · market making (Avellaneda-Stoikov, OFI), copy-trading, backtesting, FIFO P&L, Sharpe/drawdown analysis, Bayesian strategy optimization

**Security & Testing:** Smart contract security, Echidna invariant testing, randomized/stochastic fuzzing, manual penetration testing, OpenZeppelin RBAC, Secrets Manager / KMS

---

## AVAILABILITY

Open to senior/principal-level, CTO, or founding-engineer roles where early ownership, architecture under risk, technical leadership, and decision authority are required. Active across multiple client engagements via Toptal.

---

## CITIZENSHIP

US Citizen
