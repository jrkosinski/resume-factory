# JOHN R. KOSINSKI

Rust Systems Engineer • Low-Latency Trading Infrastructure • Solana
john.kosinski@gmail.com

---

## SUMMARY

Rust engineer specializing in low-latency trading systems and Solana-native execution infrastructure. Builds and operates production trading systems where detection speed, execution reliability, and risk discipline determine real financial outcomes. Has designed automated trading infrastructure continuously since 2017, across crypto arbitrage, prediction-market execution, and Solana copy-trading - progressing from multi-exchange bot architecture to high-performance Rust/Tokio backends with sub-second on-chain detection and MEV-aware execution.

Primary strengths include system ownership under risk, constraint-driven architecture, and end-to-end execution from concept to production.

---

## CORE CAPABILITIES

- Low-latency Rust/Tokio trading engine design and production operation
- Solana ecosystem: Helius LaserStream, Jito tip routing, Jupiter DEX aggregator, Pump.fun bonding-curve routing, multi-DEX execution
- High-performance async concurrent systems (Tokio, Arc-wrapped shared state, event-driven architecture)
- Exchange and DEX protocol integration (execution routing, position management, risk controls)
- Distributed systems & data pipelines (Kafka, Kubernetes, cloud infra)
- Blockchain & DeFi system design (Solana, EVM, cross-chain, tokenomics)
- Smart contract architecture & testing (Solidity, Rust, Echidna)
- Financial & risk modeling
- Automated trading system design and ownership
- Clear technical decision-making under uncertainty

---

## SYSTEMS OWNED / SELECTED EXPERIENCE

### PFP Capital / Semi-Private Client - Rust Low-Latency Trading Systems Engineer

_December 2025 – Present_

- Built and operate a live, real-money Solana copy-trading system centered on a Rust/Tokio execution engine that subscribes to Helius LaserStream WebSocket log streams, detects monitored-wallet swaps with sub-second latency, and autonomously routes copy trades through Pump.fun bonding-curve or Jupiter DEX aggregator execution paths depending on token liquidity venue
- Implemented Jito tip routing and Helius priority transaction broadcasting for MEV-aware execution, materially affecting trade inclusion speed in a latency-sensitive scalping environment
- Designed event-driven concurrent backend using Tokio async runtime, shared `Arc`-wrapped application state, and concurrent position-monitoring tasks across multiple simultaneous open trades
- Built risk and execution controls including supply-aware position sizing, trailing stop-loss with peak P&L tracking, configurable risk tiers, max slippage, liquidity-based price-impact limits, wallet/token filters, and max holding-time guards
- Built a Python/FastAPI research and backtesting platform that reconstructs Solana wallet trade histories from Helius enhanced transaction data, parses swaps across 11 DEXs, applies FIFO P&L matching, computes Sharpe/drawdown/win-rate metrics, and measures copy latency using slot/time deltas
- Sole architect and technical owner across client relationship, system architecture, data design, Rust implementation, analytics platform, GCP deployment, and React operator dashboard

### Hamza - CTO and Co-Founder

_January 2024 – January 2026_

- Conceived, architected, specified, and implemented (with small teams) a multi-chain crypto payments platform spanning Ethereum, BNB, Arbitrum, Optimism, Polygon, Bitcoin, Solana, Scroll, and Mantle
- Built a full-stack e-commerce platform on AWS (MedusaJS-based), including payments, order flow, and operational tooling
- Led a six-developer engineering team across marketplace backend, frontend, seller admin, payment infrastructure, Solidity escrow contracts on Optimism, tokenomics components, AWS/Kubernetes infrastructure, CI/CD, and production operations
- Owned architecture, execution, and iteration across on-chain systems, web infrastructure, and economic design while simultaneously discovering customer requirements
- Platform handled hundreds of users per month and ~$5–10k USD monthly throughput

### Skunk Capital - System Owner

_2017 – 2019_

- Automated previously manual cash-and-carry arbitrage strategies with real capital, exploiting pricing discrepancies between cryptocurrency futures and spot markets across BitMEX, Bitfinex, Kraken, and Binance
- Built exchange-specific plugins abstracting market data, authentication, order placement, balance retrieval, rate limits, retries, and venue-specific API behavior behind a shared arbitrage execution framework
- Implemented automated two-leg execution with cost modeling (funding rates, borrow costs, trading fees, slippage), partial-fill handling, failed-leg recovery, position tracking, and unwind workflows
- Designed trading infrastructure for durability and longevity; system operated with hundreds of thousands USD in deployed capital

### Private Client - Principal Architect / Data-Driven Trading Systems

_January 2026 – Present_

- Sole architect and developer of a live, real-money prediction-markets trading platform supporting Kalshi and Polymarket, combining TypeScript strategy execution, PostgreSQL/Google Bigtable market-data pipelines, Python/Optuna Bayesian parameter optimization, and embedded LLM agents for strategy analysis and parameter tuning
- Built a modular trading strategy framework where strategies are implemented as classes behind a shared interface, enabling consistent backtesting, optimization, comparison, and live deployment across strategy families including Avellaneda-Stoikov market making, OFI market making, and spread-capture
- Built a configurable backtesting engine modeling fees, slippage, and latency, with metrics including Calmar ratio, Sharpe ratio, max drawdown, P&L, inventory risk, win rate, and ROI

### QuantGenie - Founder / Principal Architect

- Conceived, validated, and built a natural-language → DSL → compiled trading system targeting retail traders
- Sole technical owner responsible for feasibility analysis, system architecture, and proof-of-concept execution
- Designed a constrained LLM generation pipeline integrated with deterministic compilation and execution
- Architected the backtesting data ingestion and processing pipeline, including data normalization, storage, and execution flow
- Established technical foundations, process flow, and early team structure

### Stream Finance - Principal Architect

_2022 – 2023_

- Designed and implemented mission-critical on-chain financial primitives supporting bond rollover and compounding yield
- Implemented system and security architecture for the back-office settlement system driving bond vault operations
- Systems secured hundreds of millions USD in TVL at peak during initial phase
- Foundation later enabled a lucrative stablecoin product locking hundreds of thousands USD in TVL
- Operated with only one junior developer; security and correctness were non-negotiable
- Made irreversible architectural decisions under capital-at-risk constraints

---

## ADDITIONAL EXPERIENCE

- Soundbeats (Blockchain Engineer - Sui Move smart contracts, GameFi token and NFT infrastructure)
- Alteryx (Senior Engineer - C++ analytics platform; diagnosed and resolved defects across multiple subsystems under production constraints)
- Morgan Stanley
- Aquamonix
- Leeds Rising
- Manao Software
- HotelTravel

_(Details intentionally compressed; full history available on request)_

---

## OPERATING PRINCIPLES

- Own the outcome, not just the implementation
- Design for failure modes before success cases
- Prefer irreversible correctness over reversible speed when capital is at risk
- Direct and clear communication

---

## TOOLS & TECHNOLOGIES (SELECTED)

- Rust
- Tokio
- Solana / Jito / Helius LaserStream / Jupiter / Pump.fun
- PostgreSQL
- Python
- TypeScript
- C++
- Solidity / Echidna
- WebSockets / REST APIs
- AWS, GCP
- Kubernetes / Kafka
- Grafana
- Trading Infrastructure
- DeFi Protocol Design
- Smart Contract Security
- LLM Integration

---

## AVAILABILITY

Senior / Principal-level roles requiring end-to-end ownership of high-stakes technical systems, correctness under real operational and financial risk, and high autonomy.

---

## CITIZENSHIP

US Citizen

---

---

## Sourcing Notes _(for review only - not part of the final resume)_

**Positions used:**

| Source file                                                                       | Role in this draft                                                   |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `LowLatencyTradingEngineer-PFPCapital/Solana-Low-Latency-Trading.md`              | Star entry - all Rust/Tokio/Solana bullets                           |
| `CTO-Hamza/Hamza-Overview.md` + `Hamza-General-CTO-Leadership.md`                 | Promoted to featured entry; multi-chain/Solana/CTO angle             |
| `TradingEngineer-SkunkCapital/Skunk-Capital.txt` + OldResumes                     | Blended detail bullets with old resume's capital metric and phrasing |
| `TradingEngineer-PrivateClient/Prediction-Markets-…Engine.txt`                    | Quant platform, strategy framework, backtesting                      |
| `FoundingEngineer-StreamFinance/Stream-Finance-Founding-Engineer.md` + OldResumes | Old resume bullets used (TVL numbers, sharper phrasing)              |
| `DiscoveryArchitect-Budgie/` (QuantGenie via diagrams + old resume bullets)       | Trading systems lineage                                              |

**Items softened or qualified:**

- "Sub-second latency" stated as detection characteristic, not exact percentile metric
- "MEV-aware execution" used instead of "MEV protection"
- Pump.fun wording uses "bonding-curve execution" without committing to PumpPortal vs. native SDK

**Coverage gaps:**

1. **"4+ years Rust"**: PFP Capital (Dec 2025–present) is the only explicitly named Rust project in the bank. Flag before submitting.
2. **ClickHouse, OTel, Prometheus**: Not evidenced; omitted.
3. **CEX margin/liquidation systems**: PFP Capital's risk controls are the closest analog; not padded.
