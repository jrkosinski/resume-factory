# JOHN R. KOSINSKI
Senior Systems Architect • Principal Engineer • Operator
john.kosinski@toptal.com

---

## SUMMARY

Senior blockchain and financial systems engineer with a decade-long track record of building production crypto infrastructure where customer funds and real-money consequences are non-negotiable. Designed and built multi-chain crypto payment and on-chain escrow systems at Hamza spanning Ethereum, Optimism, Arbitrum, Bitcoin, and other EVM L2s, stablecoin and DeFi protocol infrastructure at Stream Finance (serving as the technical foundation for XUSD), and live real-money automated trading systems from 2017 through the present. Primary engineering stack spans TypeScript, Node.js, Solidity, and Rust.

Core strengths: stablecoin architecture and issuance mechanics, wallet orchestration and key management infrastructure, deposit/redemption/settlement flows, on-chain/off-chain reconciliation, smart contract security and invariant testing, correctness-critical financial system design, and production operational infrastructure that keeps balances accurate across chain boundaries.

---

## CORE CAPABILITIES

- Production stablecoin and DeFi protocol architecture (EVM, Solidity, OpenZeppelin)
- On-chain/off-chain reconciliation and correctness-critical financial system design
- Wallet orchestration: HD wallets, embedded wallet infrastructure, key management
- Smart contract security: Echidna invariant testing, RBAC, access control, Hardhat, Foundry
- TypeScript and Node.js backend engineering for high-throughput financial systems
- EVM-based chains: Ethereum, Optimism, Arbitrum, Polygon, BNB, Scroll, Mantle, and EVM L2s
- Idempotent payment and settlement flows, double-entry ledger thinking, threat modeling
- Event-driven operational infrastructure (AWS EventBridge, SQS, Step Functions, Lambda)
- Staff-level technical direction and cross-functional execution across Product, Compliance, and Legal
- Distributed systems, monitoring, alerting, and reconciliation for live financial infrastructure

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

### Hamza, CTO and Co-Founder

- Turned an ambiguous multi-chain crypto commerce concept into a production platform handling checkout, on-chain escrow settlement, and order flow across Ethereum, Optimism, Arbitrum, Bitcoin, Polygon, Mantle, Scroll, and other EVM L2s, with hundreds of monthly users and real-money throughput
- Architected wallet orchestration infrastructure: per-payment one-time holding wallets derived from an HD wallet (BIP32/BIP39) with chain-specific address generation for EVM, Bitcoin, and Solana (built, not deployed); private key material secured in AWS Secrets Manager/KMS with strict service-level boundaries between address provisioning and payment processing
- Built the cross-chain settlement model so verified source-chain payments triggered immediate Optimism escrow settlement from a canonical master wallet, with holding-wallet funds batch-settled later through LiFi; this avoided deploying escrow contracts to every chain and allowed non-EVM assets like Bitcoin without fragmenting escrow state
- Designed and deployed on-chain marketplace escrow in Solidity on Optimism: PaymentEscrow supporting ETH/ERC-20 payments, unique payment IDs, buyer/seller consent-based release, configurable protocol fees, partial/full refunds, arbiter dispute resolution, seller-delegated admin permissions through bit-flag mappings, and Hats Protocol role integration
- Modeled payment processing as an idempotent state machine covering WAITING, PARTIAL, RECEIVED, IN_ESCROW, and terminal settled/expired/failed states; event-driven processing through EventBridge and SQS with merchant webhook callbacks after settlement
- Multi-layer smart contract testing: Hardhat/TypeScript test suite, parallel Foundry Solidity suite (~165 tests across 7 files), and Echidna property-based fuzzing campaigns running 80,000 transactions per run covering fund-sufficiency invariants, authorization boundaries, and transfer-failure edge cases

### Stream Finance, Principal Architect / Founding Engineer

- Designed and implemented mission-critical on-chain financial primitives supporting bond rollover and compounding yield; systems secured hundreds of millions USD in TVL at peak during initial phase
- Foundation later enabled a lucrative stablecoin product (XUSD) locking hundreds of thousands USD in TVL, with the bond-vault architecture providing the deposit/redemption/exchange-rate accounting model the stablecoin layer was built on
- Architected deposit finalization, lifecycle approval, exchange-rate oracle, position rollover, and reconciliation services around the on-chain contracts, keeping customer balances accurate across deposit, locked, and withdrawal phases and alerting on basis-point drift from theoretical compounding curves
- Designed AWS-backed operational backend: ECS Fargate chain listeners for persistent WebSocket event subscriptions, SQS-queued deposit finalization with idempotency guards and confirmation-depth handling, Step Functions lifecycle transitions gated by human approval before any rate or phase transition was broadcast, and Kinesis/S3 Object Lock immutable audit logs
- Built production invariant monitoring that indexed contract events into RDS and alerted on supply/balance anomalies, exchange-rate plausibility violations, admin-role changes, and proxy upgrade events; operated with only one junior developer and security and correctness were non-negotiable
- Implemented multi-layer smart contract security: Hardhat/Chai unit and integration tests, randomized multi-user round simulations that verified realized profit and Vault accounting against an off-chain expected-profit ledger within 50 wei drift, and Echidna invariant campaigns covering value conservation, admin-role survivability, whitelist enforcement, and proxy upgrade authorization

### PFP Capital / Semi-Private Client, Solana Trading Systems Engineer

- Sole architect and developer of a live, real-money Solana copy-trading system using Rust/Tokio, Helius LaserStream WebSocket detection, Jito tip routing, Jupiter and Pump.fun execution paths, supply-aware position sizing, trailing stop-loss with peak P&L tracking, and configurable risk controls; system is live in production and currently profitable
- Built Python/FastAPI research and backtesting platform that reconstructs Solana wallet trade histories from Helius enhanced transaction data, parses swaps across 11 DEXs, applies FIFO P&L matching, and computes Sharpe ratio, drawdown, win rate, and copy-latency measurements to validate target wallets before committing real capital
- Designed GCP deployment with Secret Manager for private key handling, PostgreSQL-backed execution telemetry and trade records, structured WebSocket broadcast layer for real-time operator state, and React/TypeScript command dashboard with Google OAuth/JWT-gated access

### Skunk Capital, System Owner

- Automated previously manual cash-and-carry arbitrage strategies with real capital across BitMEX, Bitfinex, Kraken, and Binance
- Designed trading infrastructure for durability and longevity, including partial-fill handling, failed-leg recovery, funding-rate and borrow-cost modeling, and exchange-plugin architecture
- System operated with hundreds of thousands USD in deployed capital

---

## ADDITIONAL EXPERIENCE

- QuantGenie, Principal Architect / Technical Consultant
- Axiomsys, Blockchain Consultant (Ethereum, Solana, smart contract security scoping)
- Garbles Labs, Blockchain Developer (Orca Whirlpools Solana DeFi SDK, Rust smart contract work)
- Morgan Stanley
- Alteryx
- Leeds Rising
- Aquamonix
- Manao Software
- HotelTravel

(Details intentionally compressed; full history available on request)

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

---

## TOOLS & TECHNOLOGIES (SELECTED)

- TypeScript, Node.js, NestJS
- Solidity, EVM (Ethereum, Optimism, Arbitrum, Polygon, BNB, Mantle, Scroll)
- Echidna, Hardhat, Foundry
- Smart Contract Security, RBAC, OpenZeppelin
- Rust
- AWS (EventBridge, SQS, Step Functions, Lambda, ECS Fargate, Secrets Manager, KMS, RDS/PostgreSQL)
- Python, FastAPI
- GCP, Cloud Infrastructure
- Kafka, Kubernetes
- DeFi Protocol Design
- React, TypeScript (frontend)
- C++

---

## AWARDS & CERTIFICATIONS

EthGlobal Hackathon Award (2023) | AWS Certified Solutions Architect, Associate (2023) | Microsoft Certified Trainer (2002)

---

## AVAILABILITY

Staff-level and Principal-level blockchain engineering roles requiring production ownership of correctness-critical crypto financial systems, stablecoin infrastructure, on-chain/off-chain settlement, and operational reliability.

---

## CITIZENSHIP

US Citizen

---

---

## Sourcing Notes

### Positions used

- **Hamza (primary):** Hamza-Cross-Chain-Payment-System.md, Hamza-Onchain-Escrow-Contracts.md
- **Stream Finance:** Stream-Finance-Founding-Engineer.md
- **PFP Capital:** Solana-Low-Latency-Trading.md
- **Skunk Capital:** Skunk-Capital.txt (published resume bullets used verbatim as pre-vetted)
- **Additional Experience:** Axiomsys-BlockchainConsultant.md, GarblesLabs-OrcaWhirlpoolsSDK.md, Quantgenie-FoundingArchitect.md

### Items softened or qualified

- Stream Finance AWS backend: described as "designed/architected" throughout to cover both fully-deployed and architected-but-not-confirmed-production components (per "Use With Care" guidance in the evidence file).
- Hamza AWS architecture: EventBridge and SQS cited from the confirmed production source; the broader Step Functions/Aurora/Lambda reference architecture is not claimed as confirmed production deployment.
- Stream Finance deployed networks: stated as EVM mainnet (Ethereum confirmed); additional EVM network mentions framed as "EVM-compatible architecture" rather than specific confirmed deployments.
- XUSD TVL: used the pre-vetted phrasing "hundreds of thousands USD in TVL" from the published resume bullets.
- PFP Capital profitability: kept qualitative ("currently profitable") without exact metrics per guidance.
- GarblesLabs open-source SDK: not linked or given a download count (unconfirmed).
- EthGlobal award: listed as "Award" without specifying prize tier or sponsor category (missing details per Certifications.md).

### Coverage gaps for this role

- **Morpho/Aave DeFi lending protocols:** No direct evidence. Stream Finance's fixed-income DeFi and yield mechanics are the closest analog; the posting lists this as a "bonus" rather than required.
- **Stablecoin issuance platform integration (Bridge-equivalent):** No direct evidence of working with a third-party stablecoin issuance API. Stream Finance's XUSD infrastructure is the design analog for the minting/redemption/reserve layer.
- **Peg stability mechanics:** Not explicitly present. Stream Finance's exchange-rate drift monitoring and basis-point alerting are the closest coverage.
- **Emerging markets financial products:** Thin coverage. Hamza's multi-chain global commerce platform is the closest mapping.
- **Privy embedded wallets / wallet-as-a-service SDK integration:** No evidence of Privy-specific integration; Hamza's HD wallet and holding-wallet orchestration covers the embedded wallet infrastructure concept.
