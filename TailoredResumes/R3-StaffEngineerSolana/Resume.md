# JOHN R. KOSINSKI
Senior Systems Architect • Principal Engineer • DeFi Protocol Specialist
john.kosinski@toptal.com

---

## SUMMARY

Principal architect and founding engineer with direct experience building production RWA yield vault infrastructure: stablecoin deposits, vault token issuance, exchange-rate-based yield accrual, phase-based investment rounds, and curator-controlled settlement, across EVM and Solana ecosystems. Built and currently operate a live Rust/Solana trading system using Helius, Jito, Jupiter, and Pump.fun. Delivered smart-contract suites, on-chain escrow protocols, off-chain keepers and indexers, TypeScript/React frontends, and cloud operations infrastructure for production financial systems where security and correctness carry direct capital consequences.

Primary strengths include DeFi protocol design, RWA vault architecture, Rust/Solana execution systems, smart-contract security and invariant testing, and full-stack delivery from on-chain programs through APIs and React frontends.

---

## CORE CAPABILITIES

- DeFi protocol design: RWA vaults, stablecoin deposits, vault token issuance, oracle-priced redemption, phase-based investment rounds
- Rust/Solana ecosystem: Tokio async runtime, Helius LaserStream, Jito, Jupiter, Pump.fun, GCP Secret Manager
- Smart contract architecture and security: Solidity, OpenZeppelin, UUPS upgradeability, fine-grained RBAC
- Invariant testing, Echidna campaigns, threat modeling, and audit-grade testing
- Full-stack DeFi: on-chain contracts, off-chain keepers and indexers, APIs, React/TypeScript frontends
- Production financial systems under capital-at-risk constraints
- Cloud operations around financial protocols: AWS, GCP, Kubernetes, event-driven pipelines
- LLM-assisted systems combined with deterministic code

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

**Stream Finance — Principal Architect / Founding Engineer**

- Served as principal architect and founding engineer for Stream Finance's RWA yield vault protocol: KYC'd stablecoin deposits into Treasury-backed vaults, proprietary vault token issuance representing investor positions, admin-controlled oracle-priced exchange-rate updates, and stablecoin redemption with phase-based investment rounds and rollover-based compounding across sequential rounds
- Designed the full smart-contract suite: core `Vault`, paired restricted-transfer `VaultToken`, `SecurityManager` RBAC contract over OpenZeppelin AccessControl, optional `Whitelist` for regulated/KYC-gated participation, `DepositVault` sweep-in flow, and precision-safe `CarefulMath` exchange-rate arithmetic
- Built a multi-layer testing strategy: Hardhat/Chai/Ethers.js unit and integration tests, randomized multi-user round simulations verifying realized profit and Vault accounting against an off-chain expected-profit ledger, Echidna invariant campaigns covering value conservation, admin-role survivability, whitelist enforcement, proxy upgrade authorization, and storage-slot immutability, and manual penetration testing
- Architected off-chain operations around the contracts: ECS Fargate event indexers, SQS-backed deposit finalization with idempotency and DLQs, Step Functions lifecycle approval workflows requiring human review before high-risk phase/rate transactions, EventBridge rate processing, production invariant monitors, immutable S3 audit logs, and CloudWatch/SNS/SES alerting
- Systems secured hundreds of millions USD in TVL at peak; the architecture became the foundation for XUSD, a same-company stablecoin with hundreds of thousands USD in financial exposure

**PFP Capital — Solana Low-Latency Trading Systems Engineer**

- Sole architect and developer of a live Rust/Tokio Solana copy-trading system: Helius LaserStream WebSocket detection of monitored-wallet swaps, Jito tip routing, Helius priority transaction broadcasting, Pump.fun bonding-curve and Jupiter DEX aggregator execution routing, concurrent position monitoring with shared Arc-wrapped application state, trailing stop-loss with peak P&L tracking, and GCP Secret Manager key management
- Built a Python/FastAPI research and backtesting platform that reconstructs Solana wallet trade histories from Helius enhanced transaction data, parses swaps across 11 DEXs (Jupiter, Raydium, Orca, Meteora, Pump.fun, OpenBook, and others), applies FIFO P&L matching, and backtests copy-trading strategies with configurable latency assumptions before live capital deployment
- Built a React 18/TypeScript operator dashboard with Vite, Tailwind, TanStack Query, persistent WebSocket telemetry, exponential-backoff reconnect, live positions, P&L multipliers, real-time logs, background task heartbeats, and Google OAuth/JWT-gated authenticated operator controls

**Hamza — CTO / Co-Founder**

- Architected on-chain Solidity escrow contracts for a production multi-chain crypto payment marketplace: buyer/seller release flags, arbiter resolution, protocol fees, payment-intent state machines, idempotent on-chain verification, and delegated seller admin permissions through a role-based access model
- Designed and delivered a production multi-chain crypto payment system spanning Optimism, Arbitrum, Bitcoin, Ethereum, Polygon, Mantle, Scroll, and other EVM L2s: per-payment isolated holding wallets, cross-chain event listener verification, idempotent finalization, and canonical settlement; designed key storage architecture for a multi-chain payment processor with isolated per-payment key material and operational separation between key management and execution layers
- Led a six-developer engineering team as CTO and co-founder across frontend, backend, smart contracts, and AWS/Kubernetes infrastructure; established CI/CD, monitoring, alerting, smart-contract tests, payment-system tests, and code review

**Private Client — Principal Architect / Data-Driven Trading Systems**

- Sole architect and developer of a live, real-money prediction-markets trading platform: TypeScript strategy framework, Kalshi and Polymarket execution, Google Bigtable market data ingestion, PostgreSQL-backed backtesting, Python/Optuna Bayesian parameter optimization, and embedded LLM agents for strategy analysis and diagnostic interpretation
- Designed a shared execution model where live trading and historical backtesting use the same strategy logic, parameters, diagnostics, and evaluation flow, reducing implementation surface area and improving correctness under real-money constraints

---

## ADDITIONAL EXPERIENCE

- Morgan Stanley — Senior .NET Developer (Global Wealth Management platform, fixed income and currency trading systems, .NET/C# and COBOL mainframe integration, TDD leadership)
- Alteryx — Senior Engineer (C++ back-end engine for enterprise data analytics platform, complex defect resolution, cross-platform Windows/Linux)
- Leeds Rising — Algorithmic Trading Engineer (Python short-selling strategies, composable trigger/trade architecture, live US equities deployment)
- Skunk Capital — System Owner (automated crypto cash-and-carry arbitrage, NodeJS/AWS, BitMEX/Bitfinex/Kraken/Binance, six-figure deployed capital)
- Budgie — Discovery Architect (layered AI orchestration architecture with PII detection, policy/guardrails, and security-aware LLM design for a Singapore fintech platform; formal Toptal discovery engagement)
- Manao Software, HotelTravel, Aquamonix (additional history available on request)

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

---

## TOOLS & TECHNOLOGIES (SELECTED)

- Rust
- Solidity
- TypeScript
- Python
- Solana (Helius, Jito, Jupiter, Pump.fun)
- React
- Echidna
- Hardhat
- AWS, GCP
- Kubernetes
- PostgreSQL
- Smart Contract Security
- DeFi Protocol Design
- RWA / Vault Infrastructure
- LLM Integration

---

## AVAILABILITY

Senior / Staff / Principal-level roles in DeFi protocol engineering, RWA vault infrastructure, and Solana/Rust systems requiring full-stack ownership from on-chain programs through off-chain services and production operations.

---

## CITIZENSHIP

US Citizen

---

## Sourcing notes

**Positions used:** FoundingEngineer-StreamFinance, LowLatencyTradingEngineer-PFPCapital, CTO-Hamza (OnChain/CrossChain), TradingEngineer-PrivateClient

**Lineup rationale:**
R3 is building an institutional RWA yield vault marketplace on Solana: KYC'd stablecoin deposits, vault tokens, oracle-priced redemption, curator-managed real-world assets. Stream Finance is the strongest match because the product model is architecturally identical (stablecoin deposits, vault token issuance, oracle exchange-rate-based yield, phase-based rounds, curator-equivalent admin control) even though it was EVM/Solidity rather than Solana/Anchor. PFP Capital provides Rust/Solana production credibility. Hamza provides on-chain smart contract design, multi-chain payment systems, and CTO/team leadership. Private Client demonstrates current full-stack TypeScript production ownership.

**Gaps relative to posting:**
- R3 explicitly requires "3 years of experience in Rust with meaningful production time on Solana" and "proven experience shipping and deploying Solana programs in Rust (Anchor or native)." John's Rust/Solana work at PFP Capital is off-chain execution infrastructure (a Rust application that interacts with Solana programs via Helius/Jito/Jupiter APIs), not on-chain Anchor or native Solana program authorship. This is a real and material gap that should be acknowledged honestly in any interview conversation.
- The posting prefers "experience at a lending protocol, yield marketplace, vaults infra or any similar marketplace that connected onchain allocators to the curated vaults." Stream Finance fills this exactly as a product concept but on EVM; the gap is Solana-native program authorship within that context.
- Order book, AMM, and lending market on-chain Solana program experience is not in the evidence bank.

**Softened/omitted:**
- HD wallet / BIP32/BIP39 production scope for Hamza: described as "per-payment isolated holding wallets" consistent with the evidence bank Use With Care caveat.
- Stream Finance AWS reference architecture: described as "architected" for cloud components, consistent with the evidence bank caveat that exact production vs. designed/prototyped scope should be confirmed.
- No exact TVL/AUM figures for XUSD beyond what is stated as Safe to Claim.
- Anchor framework not explicitly claimed in the tools section because John has not authored Anchor on-chain programs; "Solana (Helius, Jito, Jupiter, Pump.fun)" reflects off-chain Solana ecosystem usage.
