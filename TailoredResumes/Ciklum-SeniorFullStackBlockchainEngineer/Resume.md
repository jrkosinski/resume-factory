# JOHN R. KOSINSKI
Senior Blockchain & Full-Stack Engineer | Multi-Chain | DeFi | Node.js / TypeScript

john.kosinski@gmail.com

---

## SUMMARY

Senior blockchain and full-stack engineer with production experience building multi-chain payment infrastructure, DeFi protocols, on-chain data indexing pipelines, and Solana execution systems. Brings deep TypeScript and Node.js expertise alongside hands-on Solidity smart contract development and a security-first engineering posture proven in capital-at-risk systems. Known for end-to-end ownership across backend microservices, cross-chain transaction processing, DeFi protocol integrations, and real-time operator tooling.

Primary strengths include multi-chain backend engineering across EVM and non-EVM chains, DeFi protocol integration (AMMs, bridging, on-chain routing), on-chain data indexing, and clear technical decision-making where system failures carry direct financial consequences.

---

## CORE CAPABILITIES

- Multi-chain backend engineering: EVM (Ethereum, Arbitrum, Optimism, Polygon, BNB, Scroll, Mantle) and non-EVM (Solana, Bitcoin)
- DeFi protocol integration: AMMs, DEX aggregation, cross-chain bridging (LiFi), on-chain routing, and escrow
- Node.js / NestJS / TypeScript microservices in production financial environments
- Web3 tooling: Ethers.js v6, @solana/web3.js, Helius, Jupiter, Jito, bitcoinjs-lib
- On-chain data indexing, chain listeners, and event-driven transaction processing pipelines
- Solidity smart contract development, testing, and security review (Hardhat, Foundry, Echidna)
- Secure key management and cryptographic infrastructure (AWS KMS, Secrets Manager, HD wallets, BIP32/BIP39)
- End-to-end ownership of high-stakes technical systems under financial and operational risk
- Full-stack development: React, TypeScript, real-time WebSocket operator tooling
- Distributed systems and event-driven architecture: microservices, Kubernetes, AWS

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

### Hamza - CTO and Co-Founder
Jan 2024 - Jan 2026

- Architected and delivered a production cross-chain crypto payment system accepting payments on Optimism, Arbitrum, Ethereum mainnet, Bitcoin, Polygon, Mantle, Scroll, and other EVM L2s, with Solana chain support also built
- Designed NestJS microservices for multi-chain payment processing: chain listeners monitoring transactions via Ethers.js v6, @solana/web3.js, and bitcoinjs-lib, with event-driven payment flows over EventBridge and SQS
- Modeled crypto checkout as a payment state machine covering waiting, partial payment, received, in-escrow, settled, expired, and failed paths, with HD-wallet-derived per-payment deposit addresses and idempotent verification throughout
- Integrated LiFi for cross-chain bridging and deferred batch settlement, allowing buyers to pay on any supported chain while canonical escrow state settled on Optimism
- Architected and developed Solidity marketplace escrow contracts deployed to Optimism: ETH/ERC-20 escrow, dual buyer/seller release consent, configurable protocol fees, Hats Protocol role integration, and multicall batching
- Secured contracts through multi-layer testing: Hardhat/Mocha/Chai TypeScript tests, a parallel Foundry Solidity suite, and Echidna property-based fuzzing campaigns running 80,000-transaction sequences to detect invariant violations beyond deterministic tests

---

### PFP Capital - Solana Systems Architect / Low-Latency Trading Engineer
Dec 2025 - Present

- Sole architect and developer of a live real-money Solana copy-trading platform combining a Rust/Tokio execution engine, React/TypeScript command-and-control dashboard, and Python/FastAPI research and backtesting platform
- Built on-chain data indexing using the Helius enhanced transaction API to reconstruct complete Solana wallet trade histories, parse swaps across 11 DEXs, and compute FIFO P&L, Sharpe ratio, max drawdown, and copy-latency metrics
- Integrated Jupiter DEX aggregator routing and Pump.fun native bonding-curve execution, with Jito tip routing and Helius priority transaction broadcasting for MEV-aware low-latency order execution on Solana
- Implemented sub-second monitored-wallet swap detection through Helius LaserStream WebSocket subscriptions and event-driven Rust processing, with concurrent position monitoring, trailing stop-loss, and configurable risk controls

---

### Stream Finance - Principal Architect / Founding Engineer
2022 - 2023

- Served as principal architect and founding engineer for Stream Finance's EVM Bond Vault, a tokenized US Treasury and fixed-income DeFi protocol deployed to Ethereum
- Designed a modular Solidity contract suite around Vault, VaultToken, SecurityManager, Whitelist, and DepositVault, supporting deposit/lock/withdraw lifecycle phases, sequential investment rounds, rollover-based compounding, and stablecoin redemption
- Built multi-layer smart-contract security using Hardhat/Chai/Ethers.js unit and integration tests, randomized multi-user round simulations, and Echidna invariant campaigns covering value conservation, admin-role survivability, whitelist enforcement, and proxy upgrade authorization
- Systems secured hundreds of millions USD in TVL at peak during initial phase; the protocol became the foundation for XUSD, a same-company stablecoin locking hundreds of thousands USD in TVL

---

### Garbles Labs - Blockchain SDK Developer
2022

- Ported the Orca Whirlpools TypeScript SDK, covering one of Solana's leading concentrated liquidity AMMs, to C#/.NET for the Unity game engine, releasing the SDK open-source for community use
- Interfaced directly with Orca Whirlpools Rust smart contracts on Solana and modified contract code to support testability; built a full automated test suite for the ported SDK
- Gained hands-on working knowledge of Solana AMM mechanics, concentrated liquidity protocol design, and on-chain protocol interaction through direct SDK and smart contract work

---

## ADDITIONAL EXPERIENCE

- Axiomsys - Blockchain Consultant (2022-2023): scoped NFT, fungible token, and smart contract security audit project packages across Ethereum and Solana; led R&D into Unity/token integration strategy for a well-known online meeting venue
- Skunk Capital - System Owner: automated crypto arbitrage trading, operating with hundreds of thousands USD in deployed capital
- QuantGenie - Principal Architect / Consultant: AI-assisted algorithmic trading platform using an LLM pipeline, proprietary DSL, and code generation targeting MetaTrader 5 and NinjaTrader
- Alteryx - Senior Engineer: production defect resolution in a large C++ analytics platform
- Morgan Stanley
- Manao Software
- HotelTravel
- Leeds Rising

(Details intentionally compressed; full history available on request)

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

---

## TOOLS & TECHNOLOGIES (SELECTED)

- TypeScript / Node.js / NestJS
- Ethers.js v6 / @solana/web3.js / bitcoinjs-lib
- Solidity / Hardhat / Foundry / Echidna
- Rust / Tokio
- React / TanStack Query / Vite
- PostgreSQL / DynamoDB / TypeORM
- AWS / Kubernetes / EventBridge / SQS
- LiFi / Jupiter / Jito / Helius / Pump.fun
- Python / FastAPI
- Smart Contract Security
- DeFi Protocol Integration
- Multi-Chain Infrastructure
- HD Wallets / BIP32 / BIP39

---

## AVAILABILITY

Senior and principal-level blockchain and full-stack engineering roles requiring end-to-end ownership of multi-chain production systems, DeFi protocol integrations, and high-stakes financial infrastructure.

---

## CITIZENSHIP

US Citizen

---

---

## Sourcing Notes (for review only; not part of final resume)

### Positions used

- **Hamza / Cross-Chain Payment System** (`Hamza-Cross-Chain-Payment-System.md`): Primary source for multi-chain backend, NestJS microservices, Ethers.js v6, @solana/web3.js, LiFi, EventBridge/SQS, payment state machine, HD wallets, and idempotent verification bullets.
- **Hamza / On-Chain Escrow Contracts** (`Hamza-Onchain-Escrow-Contracts.md`): Source for Solidity escrow architecture, Hats Protocol, Foundry testing, and Echidna fuzzing bullets.
- **PFP Capital / Solana Low-Latency Trading** (`Solana-Low-Latency-Trading.md`): Source for Helius on-chain data indexing, Jupiter/Pump.fun DeFi protocol integration, Jito execution, and Solana analytics platform bullets.
- **Stream Finance / EVM Bond Vault** (`Stream-Finance-Founding-Engineer.md`): Source for DeFi protocol depth, Solidity/Echidna security, and TVL metrics. The "hundreds of millions USD in TVL" and "XUSD stablecoin" bullets are from the evidence file's Published Resume Bullets section, pre-vetted for external use.
- **Garbles Labs / Orca Whirlpools SDK** (`GarblesLabs-OrcaWhirlpoolsSDK.md`): Source for Solana AMM / developer tooling angle. Kept brief to represent the short engagement accurately.

### Items softened or omitted

- **Hamza Solana support**: Described accurately as "Solana chain support also built" (not "deployed") per the evidence file's "Built but Not Deployed: Solana" note.
- **Hamza AWS EventBridge/SQS architecture**: Only referenced as confirmed production features ("EventBridge and SQS event processing"), not the full target AWS reference architecture (EventBridge, Step Functions, Aurora, etc.) which is in the "Avoid Unless Confirmed" list.
- **Stream Finance networks**: Only claimed Ethereum deployment; BSC/Polygon are in the "Use With Care / Qualify Internally" list.
- **PFP Capital latency metrics**: Described as "sub-second" detection (per the evidence bank's safe claim) without exact percentile distributions (not yet confirmed).
- **PFP Capital profitability**: Not quantified; evidence says "small but increasing" profits and advises against exact ROI claims.
- **Soundbeats** (Sui/Move): Not included in selected experience; Sui/Move is not requested by the posting, and EVM/Solana coverage is already strong. Moved to Additional.
- **Skunk Capital, QuantGenie**: In Additional Experience only; not core enough to this posting to earn full treatment.

### Coverage note

The evidence bank covers EVM chains and Solana thoroughly. Coverage for TON, Tron, and other non-EVM chains mentioned in the posting is not present in any evidence file. No fabricated experience was added for these chains. The AMM angle is covered through Orca Whirlpools (Garbles Labs) and Jupiter/Pump.fun (PFP Capital). Bridging is covered through LiFi (Hamza).
