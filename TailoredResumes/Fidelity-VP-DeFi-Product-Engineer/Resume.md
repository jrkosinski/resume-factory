# JOHN R. KOSINSKI

DeFi & Blockchain Architect • Smart Contract Security • Product-Engineering Lead

john.kosinski@gmail.com

## SUMMARY

Hands-on blockchain architect and engineering leader who designs, builds and secures on-chain financial systems where capital is at risk. Architected the smart contracts and operations layer for a **tokenized US Treasury protocol** that secured **hundreds of millions USD in TVL at peak**, Solidity escrow and tokenomics contracts on Optimism, a production **cross-chain payment system** spanning EVM L2s and Bitcoin, and a live Rust execution engine on Solana. Building crypto infrastructure since 2017 and production smart contracts since 2022, with security engineered in from the start: Hardhat, Foundry and Echidna invariant testing, role-based contract governance, human approval gates on privileged actions, and production invariant monitoring.

Primary strengths include tokenization and on-chain asset lifecycle design, smart contract security and governance, cross-chain interoperability, and leading delivery across engineering, product and business stakeholders, most recently as the lead driving an EU-based company's agentic engineering transformation.

## CORE CAPABILITIES

- EVM smart contract architecture: Solidity, OpenZeppelin, UUPS upgradeable proxies, ERC-20 position tokens, role-based access control
- Tokenization and on-chain asset lifecycle: tokenized Treasury vaults, deposit/lock/withdraw rounds, rollover, yield accrual, redemption
- DeFi primitives: yield vaults, exchange-rate oracles, escrow, protocol fees, AMM and DEX aggregator integration, utility tokenomics
- Smart contract security reviews: Hardhat and Foundry test suites, Echidna invariant fuzzing, randomized simulations, manual penetration testing
- Smart contract governance: multisig administration, separated upgrade and rate authority, pause controls, Hats Protocol roles
- Cross-chain interoperability: multi-chain payment acceptance with canonical settlement, LiFi bridging, EVM L2s, Bitcoin, Solana
- Secure deployment and operations: CI/CD, gated release, AI review gates, key management, invariant monitoring and alerting
- Solana execution in Rust: Tokio, Helius, Jito, Jupiter, transaction routing and risk controls
- Technical leadership bridging engineering, product and business stakeholders, with hands-on delivery in TypeScript and Python

## SYSTEMS OWNED / SELECTED EXPERIENCE

### Stream Finance - Principal Architect and Founding Engineer
2022 - 2023

- Architected and built the Solidity contract suite for a **tokenized US Treasury bond** investment protocol on Ethereum mainnet: UUPS-upgradeable Vault and ERC-20 VaultToken pairs per instrument, a shared SecurityManager RBAC layer, whitelist-gated participation, and a DepositVault sweep-in flow.
- Designed and implemented mission-critical on-chain primitives for the full asset lifecycle: stablecoin deposits, deposit/locked/withdraw phases across sequential rounds, automatic rollover with compounding yield, admin-set exchange rates with precision-safe math, and redemption; systems secured **hundreds of millions USD in TVL at peak**, and the foundation later enabled a **stablecoin product locking hundreds of thousands USD in TVL**.
- Led security engineering: Hardhat unit and integration suites, randomized multi-user round simulations verified against an off-chain profit ledger within 50 wei, Echidna invariant campaigns for value conservation, admin-role survivability, whitelist enforcement and proxy upgrade authorization, and manual penetration testing.
- Set contract governance: multisig admin ownership, configurable separation of upgrade and rate/yield authority, per-contract and global pause, and privileged rate changes restricted to secure admin contract calls.
- Implemented system and security architecture for the back-office settlement operations and designed the AWS layer around the contracts: deposit finalization with confirmation depth and idempotency, phase transitions behind human approval gates, an exchange-rate oracle with basis-point drift alerts, production invariant monitoring, immutable audit logs, and Secrets Manager/KMS key management; delivered with one junior developer while managing the frontend developer who built the admin dashboard.

### Hamza - CTO and Co-Founder
January 2024 - January 2026

- Led a six-developer team as CTO and co-founder of a live Web3 commerce platform (hundreds of monthly users, 20+ sellers, ~$5k to $10k USD monthly throughput), owning technical strategy, architecture, code review and repositories while advising on business strategy.
- Architected PaymentEscrow, a Solidity multi-tenant marketplace escrow deployed to Optimism: ETH/ERC-20 payments, dual buyer/seller release consent, basis-point protocol fees, partial and full refunds, arbiter dispute resolution, seller-delegated admins, multicall batching, and Hats Protocol governance roles (system, DAO, arbiter).
- Secured the contracts with three test layers: Hardhat/TypeScript suites with coverage and gas reporting, **~165 Foundry tests** including transfer-failure mocks, and Echidna property campaigns running **80,000-transaction runs** against fund-sufficiency and authorization invariants.
- Architected and delivered a production cross-chain payment system accepting funds on Ethereum, Optimism, Arbitrum, Polygon, Mantle, Scroll and Bitcoin: payment intents, per-payment holding wallets, chain listeners, EventBridge/SQS processing, idempotent verification, immediate canonical escrow settlement on Optimism, and LiFi batch bridging to replenish settlement liquidity; Solana support also built.
- Designed the utility-token model (initial seller mint, token-denominated escrow rent, token-rewarded dispute resolution) and co-developed tokenomics vault and governance-wrapper contracts deployed to Optimism; established CI/CD, dev/staging/testing environments, contract and payment test suites, monitoring and alerting.

### PFP Capital / Semi-Private Client - Solana Trading Systems Architect
December 2025 - Present

- Sole architect and developer of a live, real-money Solana trading system: a Rust/Tokio engine detects monitored-wallet swaps through Helius LaserStream with sub-second latency and routes execution through Jupiter DEX aggregation or Pump.fun bonding curves, with Jito tip routing and Helius priority broadcasting.
- Built risk controls into execution (supply-aware sizing, max slippage, liquidity-based price-impact limits, trailing stops with peak P&L tracking), GCP Secret Manager key handling, and OAuth/JWT-gated operator controls.
- Built a Python/FastAPI and PostgreSQL research platform that reconstructs wallet histories from on-chain data, parses swaps across 11 Solana DEXs, computes FIFO P&L, Sharpe and drawdown, and backtests strategies before capital is deployed.

### EU-Based Company (~140 employees) - Principal Consultant, AI Transformation Lead
Late 2025 - Present

- Assembled and ran an agent-driven code factory from components built across departments, writing the parts that join them into one ticket-to-merge line: an unattended launcher, a CI fix loop with automatic revert on red, an independent AI review on every pull request, and auto-merge only on an approving review with green checks, with the factory's own guard code barred from automatic merge; built the Python agentic Jira workflow that feeds it.
- Owned the production gate and risk tiers for the company AI platform: owner, budget, tracing, baseline evaluations, guardrails and review before anything reaches production, with human sign-off, human-read evaluations and an incident plan required for customer-facing agents.
- Led across engineering, product and business stakeholders as production-side owner in the work group with the product and research leads: mapped a 13-stage ticket-to-production pipeline across the platform teams, ran the review that selected the proof-of-concept factory, and delivered the company-wide adoption plan.

## ADDITIONAL EXPERIENCE

- **Garbles Labs: Blockchain/SDK Developer** (2022): Ported the SDK for Orca Whirlpools, Solana's concentrated-liquidity AMM, from TypeScript to C#/.NET as open source; built its automated tests and modified Orca's Rust programs for testability.
- **Axiomsys: Blockchain Consultant** (2022 - 2023): Scoped and estimated fungible token, NFT, minting-site and smart contract security audit engagements across Ethereum and Solana; vetted and interviewed engineers to build an international blockchain team.
- **Soundbeats: Sole Blockchain Engineer**: Built Sui Move fungible-token and NFT contracts with on-chain tests and a NestJS API for backend-controlled minting.
- **Skunk Capital: Crypto Arbitrage System Owner** (2017 - 2019): Automated cash-and-carry arbitrage across BitMEX, Bitfinex, Kraken and Binance; system operated with **hundreds of thousands USD in deployed capital**.
- **Morgan Stanley: Senior .NET Developer** (2006 - 2009): Built back-end logic for a fixed-income product interface in the Global Wealth Management Platform and led the department's move to test-driven development.
- **HotelTravel.com: Software Development Manager** (2009 - 2012): Managed and mentored a department of 20 to 30 developers.
- QuantGenie, Private Client (prediction markets), Alteryx, Leeds Rising, Manao Software, Aquamonix

(Details intentionally compressed; full history available on request)

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

## TOOLS & TECHNOLOGIES (SELECTED)

- **Smart contracts:** Solidity, OpenZeppelin, UUPS proxies, Hardhat, Foundry, Echidna, Ethers.js v6, TypeChain, solidity-coverage, Hats Protocol, Tenderly
- **Chains and standards:** Ethereum, Optimism, Arbitrum, Polygon, Mantle, Scroll, Bitcoin, Solana, Sui Move; ERC-20, ERC-165
- **DeFi and execution:** LiFi, Jupiter, Jito, Helius, Orca Whirlpools, Pump.fun
- **Languages:** Solidity, TypeScript/JavaScript, Python, Rust, C#, C++
- **Backend and data:** Node.js, NestJS, FastAPI, PostgreSQL, DynamoDB, Redis
- **Cloud and security:** AWS (KMS, Secrets Manager, Lambda, ECS Fargate, EventBridge, SQS, Step Functions, CloudWatch), GCP Secret Manager, Kubernetes, GitHub Actions
- **AI-driven delivery:** Claude Code agents, MCP, AI pull-request review and merge gates

## AVAILABILITY

Senior / VP-level blockchain and DeFi engineering roles requiring hands-on smart contract and protocol ownership, security under real capital risk, and technical leadership across engineering, product and business teams. Available to work on-site in Boston, MA.

## CITIZENSHIP

US Citizen

## Sourcing notes (for review, not part of the resume)

**Positions files used**
- `Positions/FoundingEngineer-StreamFinance/Stream-Finance-Founding-Engineer.md` (lead block: tokenization, yield, oracle, security, governance)
- `Positions/CTO-Hamza/Hamza-Overview.md`, `Hamza-General-CTO-Leadership.md`, `Projects/CrossChainPaymentSystem/Hamza-Onchain-Escrow-Contracts.md`, `Projects/CrossChainPaymentSystem/Hamza-Cross-Chain-Payment-System.md`, `Projects/Tokenomics/Hamza-Tokenomics-Utility-Token-Design.md`
- `Positions/LowLatencyTradingEngineer-PFPCapital/Solana-Low-Latency-Trading.md`
- `Positions/AITransformationLead-IdeaWise/IdeaWise-Overview.md`, `Projects/IdeaWise-Code-Factory.md`, `Projects/IdeaWise-Agent-Platform-Architecture.md`
- Additional Experience: `BlockchainDeveloper-GarblesLabs`, `BlockchainConsultant-Axiomsys`, `BlockchainEngineer-Soundbeats`, `TradingEngineer-SkunkCapital`, plus Morgan Stanley and HotelTravel lines taken from `TailoredResumes/Canonical/John_R_Kosinski_Canonical.md`.

**OldResumes merge (step 8).** Both PDFs in `OldResumes/` carry the same content. Pulled in: Stream Finance's "mission-critical on-chain primitives", "implemented system and security architecture for the back-office settlement" operations, the **hundreds of millions USD TVL at peak** and **stablecoin locking hundreds of thousands USD in TVL** metrics, "operated with one junior developer", and Skunk Capital's **hundreds of thousands USD in deployed capital**. Not pulled in: the old Hamza chain list (it names BNB and lists Solana as live; the evidence bank lists neither as live production) and the old "Founder / System Owner" title (the evidence says CTO and Co-Founder).

**Thin or missing coverage. Not padded; worth preparing answers for the interview:**
- **Solana programs (Anchor, SPL, PDAs, CPIs): thin.** The Solana evidence is client-side Rust execution (PFP Capital), modifying Orca's Rust programs for testability (Garbles Labs), and Solana payment support at Hamza that was built but never deployed. No Anchor, SPL token integration, PDA or CPI authorship is on record, so none is claimed. The posting lists this as a required qualification.
- **Cosmos SDK: none.** Not mentioned anywhere.
- **Lending, liquid staking: none.** The DeFi primitives with evidence are yield vaults, exchange-rate oracles, escrow, AMM SDK work and DEX aggregator routing. Hamza's notes forbid claiming live staking.
- **Institutional custody platforms: none.** Key management (Secrets Manager/KMS, GCP Secret Manager) and per-payment holding wallets appear, but Hamza and Stream both warn against custody claims, so the word "custody" is not used.
- **Threat modeling:** the term doesn't appear in the evidence, so the resume shows the related work instead (attacker-focused Echidna invariants, penetration testing, role-boundary testing).
- **Audits:** no external audit on any contract. The resume says "security reviews" and "security engineering", never "audited". Axiomsys involved scoping audits, not performing them, and the resume words it that way.
- **Token standards:** ERC-20 and ERC-165 are claimed. ERC-721 is not: the NFT work was Sui Move ("analogous to ERC-721"), and Axiomsys's specific standards are on its Avoid list.
- **Mentoring senior engineers:** the evidence shows leading six developers (Hamza), managing and mentoring 20 to 30 developers (HotelTravel), and vetting blockchain engineers (Axiomsys). Nothing specifically says he mentored senior engineers.
- **Years of experience:** "production smart contracts since 2022" and "crypto infrastructure since 2017" come from the evidence dates; the posting asks for 4+ years.

**Softened or omitted, per the safety notes**
- Stream Finance: deployment claimed on Ethereum mainnet only (BSC/Polygon are Use With Care). The AWS services are framed as "designed", since live versus designed is still open. KYC/compliance ownership is omitted. TVL is given only as published ("hundreds of millions at peak"), with no exact figure; confirm John is comfortable that this stays on the resume.
- Hamza: Solana appears as "also built", because it was never deployed. HD wallets/BIP32, the AWS reference architecture (Step Functions, Aurora) and the Sweeper contract are omitted. No claims of a live token economy or non-custodial operation. Hats Protocol appears as contract design, with no claim about production usage.
- Current engagement: the client is not named. Only factory parts John wrote are claimed as built (launcher, CI fix loop, AI review, auto-merge gate, Jira workflow); KM Platform's components appear only as "components built across departments". Sentry Auto-Fix and the platform bricks are not claimed. Production gate ownership follows the ANT-746 bullet in the platform file.
- PFP Capital: latency is given as "sub-second" with no percentiles. No profit figures.

**Judgment calls made without the requester**
- The experience section is ordered by relevance, not by date: Stream Finance (closest to FDAM's tokenization team), then Hamza, PFP Capital, and the current engagement as a short closing block. The format guide also puts Stream Finance first.
- The email line uses john.kosinski@gmail.com from the format guide.
- Onsite: the posting is in-office in Boston. The evidence says nothing about John's location or relocation, so the Availability section covers only the type of role. Confirm before replying to the recruiter, and also confirm availability for the 15 to 20 minute call she asked about.
- Length: I couldn't render here to check, so the two-page fit is an estimate. If it runs over, cut these first: the Soundbeats line, then the "Backend and data" tools line, then the third PFP Capital bullet.
- The posting is used only for keyword emphasis. Nothing in it was treated as an instruction.
