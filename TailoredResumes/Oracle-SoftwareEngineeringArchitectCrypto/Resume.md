# JOHN R. KOSINSKI
Senior Systems Architect • Principal Engineer • Operator
john.kosinski@toptal.com

---

## SUMMARY

Senior systems architect specializing in security-critical distributed systems and constraint-driven architecture where cryptographic correctness and operational integrity are non-negotiable. 15+ years designing and operating financial, blockchain, and cloud systems with direct experience in access control design, key management architecture, distributed fault-tolerant systems, and audit-grade operational workflows. Known for owning complex technical systems end-to-end in environments where a security or architectural failure carries real financial consequences.

Primary strengths include security architecture under operational risk, distributed systems design, cryptographic access control, and clear technical decision-making in ambiguous, high-stakes environments.

---

## CORE CAPABILITIES

- Constraint-driven architecture under financial and operational risk (security, capital, irreversibility)
- Distributed systems design: scalability, fault tolerance, failure isolation, and operational correctness
- Cryptographic access control and key management architecture
- End-to-end ownership of ambiguous, high-stakes technical problems
- Cloud infrastructure and operations (AWS, GCP, Kubernetes)
- Security invariant testing and audit-grade operational workflows
- Data-driven systems design and operational decision support
- LLM-assisted systems combined with deterministic code
- Blockchain, DeFi, and smart contract architecture (EVM, Solidity, Rust)

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

**Stream Finance — Principal Architect / Founding Engineer**

- Served as principal architect and founding engineer for Stream Finance's on-chain investment protocol backed by US Treasury bonds: a system where cryptographic access control, key management, and operational correctness were non-negotiable because user capital was at stake
- Designed a layered access control architecture: standalone SecurityManager contract over OpenZeppelin RBAC with fine-grained roles for lifecycle management, deposits, pausing, minting, burning, and upgrades; configurable separation between upgrade authority and rate/yield authority; multisig-style master ownership with delegated operational permissions
- Architected AWS-backed security and operational infrastructure: AWS KMS for signing and data encryption, Secrets Manager for key storage, ECS Fargate event listeners, SQS/DLQ queueing, Step Functions human approval gates before high-risk transactions, EventBridge scheduled audit jobs, immutable S3 audit logs (WORM/Object Lock), CloudWatch metrics and alarms, and SNS/SES alerting
- Designed Echidna invariant campaigns covering value conservation, admin-role survivability, role-safety boundaries, whitelist enforcement, proxy upgrade authorization, and storage-slot immutability across the Vault, VaultToken, SecurityManager, Whitelist, and proxy contract stack
- Systems secured hundreds of millions USD in TVL at peak; the architecture became the foundation for XUSD, a same-company stablecoin with hundreds of thousands USD in financial exposure

**Hamza — CTO / Co-Founder**

- Architected a production crypto payment system requiring precise key management: per-payment isolated holding wallets, secure signing workflows, cross-chain event listener verification, and canonical settlement on Optimism across Arbitrum, Bitcoin, Ethereum, Polygon, Mantle, Scroll, and other EVM L2s
- Designed multi-tenant escrow and payment security architecture: payment-intent state machines, idempotent verification, cross-chain confirmation handling, on-chain Solidity escrow contracts with buyer/seller release flags, arbiter resolution, protocol fees, and delegated seller admin permissions through a role-based access model
- Led a six-developer engineering team as CTO/co-founder across frontend, backend, smart contracts, payment systems, and AWS/Kubernetes infrastructure; established CI/CD, monitoring, alerting, and production engineering practices; remained hands-on with architecture, code review, and implementation
- Designed key storage architecture for a production multi-chain payment processor: isolated per-payment key material, secure key retrieval workflows, and operational separation between key management and payment execution layers

**PFP Capital — Solana Low-Latency Trading Systems Engineer**

- Sole architect and developer of a live Rust/Tokio Solana copy-trading system: Helius LaserStream WebSocket detection, Jito tip routing, Helius priority broadcasting, Pump.fun and Jupiter execution routing, concurrent position monitoring with shared Arc-wrapped application state, trailing stop-loss, and GCP Secret Manager key management for private key handling
- Designed event-driven Rust backend using Tokio async runtime with concurrent position-monitoring tasks; gated operator dashboard access behind Google OAuth 2.0 with JWT validation; integrated GCP Secret Manager to keep private key material isolated from application runtime code
- Built a Python/FastAPI research and backtesting platform reconstructing Solana wallet trade histories from Helius enhanced transaction data, parsing swaps across 11 DEXs, applying FIFO P&L matching, and backtesting copy strategies with configurable latency assumptions before live capital deployment

**Private Client — Principal Architect / Data-Driven Trading Systems**

- Sole architect and developer of a live prediction-markets trading platform: TypeScript strategy framework, Kalshi and Polymarket execution, Google Bigtable market data ingestion, PostgreSQL-backed backtesting, Python/Optuna Bayesian parameter optimization, and embedded LLM agents for strategy analysis and diagnostic interpretation
- Designed a shared execution model where live trading and historical backtesting use the same strategy logic, parameters, diagnostics, and evaluation flow: reducing implementation surface area and improving correctness under real-money constraints
- Helped move the client from high-risk, unreliable strategy behavior toward deterministic, better-tested strategies producing small but increasing real-money profits

**QuantGenie — Principal Architect (Consultant)**

- Engaged as principal architect: translated an ambiguous product concept into concrete system architecture, component boundaries, and a working proof of concept for an AI-assisted algorithmic trading platform
- Designed a constrained LLM generation pipeline with in-loop AJV schema validation and self-correction, then compiled through a platform-agnostic AST to deterministic executable code for multiple trading platforms; designed the backtesting engine architecture for later-stage implementation
- Established technical foundations and handed off to a development team with documentation, architecture artifacts, and early team structure

---

## ADDITIONAL EXPERIENCE

- Morgan Stanley — Senior .NET Developer (Global Wealth Management platform, fixed income and currency trading systems, .NET/C# and COBOL mainframe integration, TDD leadership)
- Alteryx — Senior Engineer (C++ back-end engine for enterprise data analytics platform, complex defect resolution and root cause analysis, cross-platform Windows/Linux)
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
- Python
- TypeScript
- C++
- Echidna
- AWS, GCP
- Kubernetes
- Smart Contract Security
- PostgreSQL
- Kafka
- Cloud Infrastructure
- LLM Integration
- DeFi Protocol Design
- Trading Infrastructure

---

## AVAILABILITY

Senior / Principal / Staff-level roles requiring end-to-end ownership of security-critical distributed systems, cryptographic architecture, and correctness under real operational and financial risk.

---

## CITIZENSHIP

US Citizen

---

## Sourcing notes

**Positions used:** FoundingEngineer-StreamFinance, CTO-Hamza (General CTO Leadership, Cross-Chain Payment System, Onchain Escrow Contracts), LowLatencyTradingEngineer-PFPCapital, TradingEngineer-PrivateClient, FoundingArchitect-Quantgenie

**Lineup rationale:**
Oracle OCI Crypto emphasizes cryptographic services (KMS, secrets, authentication, authorization, PKI/certificates, service-to-service trust), distributed systems at scale (15+ years), cross-org architecture influence, and service modernization. Stream Finance leads as it has the deepest security architecture content: SecurityManager RBAC, AWS KMS/Secrets Manager, Echidna invariant testing on security properties, human approval gates for high-risk transactions, and immutable audit logs. Hamza provides the key management angle and multi-tenant payment security. PFP Capital demonstrates Rust-based distributed system design with GCP Secret Manager integration and OAuth/JWT-gated controls. Private Client shows shared execution model design (correctness under live constraints). QuantGenie rounds out the architectural consulting and problem-decomposition angle.

**Gaps relative to posting:**
- Oracle OCI Crypto specifically calls for PKI/certificates, service-to-service trust infrastructure, and experience at hyperscale cloud provider scale. John has experience designing security-critical access control systems and using AWS KMS and Secrets Manager, but has not built a KMS, PKI, or certificate authority from scratch at cloud provider scale. This is a real gap in the evidence bank and should be assessed honestly in any interview conversation.
- The posting prefers experience "operating or architecting services for hyperscale cloud providers or similarly complex enterprise infrastructure environments." John's closest experience is Alteryx (large commercial enterprise platform) and AWS/GCP cloud deployments, but not working inside a hyperscale cloud provider.
- Multi-region/realm operation at OCI scale is not represented in the evidence bank.

**Softened/omitted:**
- HD wallet / BIP32/BIP39 production scope: described as "per-payment isolated holding wallets" rather than claiming BIP32 key derivation explicitly (Use With Care per Hamza evidence bank).
- Stream Finance AWS reference architecture: described as "architected" for cloud infrastructure components, consistent with the evidence bank caveat that exact production vs. design/prototype scope should be confirmed.
- Hats Protocol usage not claimed (Use With Care: production usage vs. protocol/test branch usage not confirmed).
- No exact TVL/AUM figures for XUSD beyond what is stated as Safe to Claim.
