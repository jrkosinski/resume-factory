# Leeds Rising / Algorithmic Trading Engineer

## Basic Info

**Client / Employer:** Leeds Rising
**Domain:** Algorithmic trading, equities, short-selling, stock market automation, Python trading infrastructure
**Role / Title:** Algorithmic Trading Engineer / Python Developer (exact title to be confirmed)
**Dates:** 2023 (approx. 6 months)
**Ownership:** Primary developer — built PyDAS API and algo trading system from scratch
**Status:** Completed; strategies deployed and tested on live market
**Primary Stack:** Python
**Domain:** US equities, Nasdaq, NYSE, short-selling, borrowing, DAS Trader platform

---

## Canonical Summary

Built algorithmic trading infrastructure for Leeds Rising in 2023, focused on short-selling strategies for US equities. Developed PyDAS — a robust, complete, and rigorously tested Python API wrapping the DAS trading platform — covering buying, selling, borrowing, and short-selling of US stocks. On top of PyDAS, built a full algorithmic trading system with a composable architecture: configurable Triggers and plug-and-playable Trade logic modules that allow dynamic trading strategy specification. Implemented borrowing and short-selling strategies targeting illiquid stocks on the Nasdaq and NYSE, and deployed and tested those strategies against the live market. Stack: Python, algorithmic trading, low-latency systems.

---

## Short Resume Summary Version

Developed PyDAS (Python DAS Trader API) and a composable algorithmic trading system for Leeds Rising (2023) — implementing configurable trigger/trade logic architecture for dynamic strategy specification, then deploying and live-testing short-selling and borrowing strategies for illiquid Nasdaq and NYSE stocks.

---

## Primary Tags

* Python
* Algorithmic trading
* Short-selling
* Stock borrowing
* Illiquid stocks
* Nasdaq
* NYSE
* US equities
* DAS Trader
* PyDAS
* API development
* SDK development
* Trading system architecture
* Configurable trading strategy
* Trigger/signal design
* Low-latency trading
* Live market deployment
* Automated testing
* Stock market automation

---

## Context

Leeds Rising is a stock market trading firm focused on short-selling strategies for US equities. Short-selling illiquid stocks is a technically and operationally demanding niche: illiquid names are harder to borrow, spreads are wider, and execution timing is more critical. Automating these strategies requires a reliable programmatic interface to the trading platform as well as a flexible system that can express and adjust strategies dynamically.

DAS Trader is a widely-used direct-access trading platform used by active traders and proprietary trading firms. It exposes an API for programmatic order management and account interaction. PyDAS was built to be a complete, production-quality Python wrapper around this API — enabling algorithmic strategy development in Python rather than against DAS's native interface.

---

## Role and Ownership

Primary developer for Leeds Rising's Python trading infrastructure.

Owned:

* Full development of PyDAS — Python API wrapper for the DAS trading platform
* API coverage: buying, selling, borrowing, and short-selling of US stocks
* Rigorous automated testing of PyDAS
* Full algorithmic trading system built on PyDAS
* Composable strategy architecture: configurable Trigger + plug-and-playable Trade logic
* Short-selling and borrowing strategy implementation for illiquid Nasdaq/NYSE stocks
* Live market deployment and testing of strategies

---

## Technical Work

### PyDAS — Python DAS Trader API

Built PyDAS from scratch: a robust, complete Python API wrapper for the DAS trading platform. PyDAS covered the full range of trading operations needed by Leeds Rising:

* Buying and selling US equities
* Borrowing shares for short-selling
* Short-selling execution

"Complete" and "well-tested" are deliberate — PyDAS was designed to be production-grade developer infrastructure, not a quick script. The API was rigorously tested to ensure correctness and reliability before being used as the foundation for live trading strategies.

### Algorithmic Trading System

Built a full algorithmic trading system on top of PyDAS with a composable, extensible architecture:

* **Configurable Trigger** — the signal/condition layer that determines when to act. The trigger is configurable, allowing different market conditions or signals to be specified without rewriting core logic.
* **Plug-and-playable Trade logic** — the execution layer is modular and swappable, meaning different trading behaviors (entry, exit, sizing, order type) can be composed and substituted independently.

This architecture allows dynamic strategy specification — new strategies can be assembled from Trigger and Trade components without rebuilding the system, which is a significant operational advantage for a trading firm iterating on strategy ideas.

### Short-Selling and Borrowing Strategies

Implemented specific trading strategies for:

* **Borrowing illiquid stocks** — locating and borrowing hard-to-borrow shares on Nasdaq and NYSE, which is operationally complex compared to liquid names
* **Short-selling illiquid stocks** — executing short positions on low-liquidity equities, where execution quality and timing are critical

Deployed and tested these strategies against the live market with real capital — proven profitable in live trading.

### Live Market Deployment

Strategies were not just backtested — they were deployed and tested on the live Nasdaq and NYSE markets. This is a meaningful distinction: live deployment validates that the system handles real-world conditions (partial fills, order rejections, borrow unavailability, latency) that simulation cannot fully replicate.

---

# Bullet Bank

## Strong General Bullets

* Developed PyDAS, a robust and rigorously tested Python API to the DAS Trader platform, covering buying, selling, borrowing, and short-selling of US equities — serving as the foundation for Leeds Rising's algorithmic trading infrastructure.

* Built an algorithmic trading system on PyDAS with a composable architecture: configurable Triggers for signal specification and plug-and-playable Trade logic modules for strategy assembly without system rewrites.

* Implemented short-selling and borrowing strategies for illiquid Nasdaq and NYSE stocks and deployed and tested those strategies on the live market — proven profitable in real trading with real money.

---

## API / SDK Bullets

* Built PyDAS from scratch as a complete, production-grade Python API wrapper for the DAS trading platform, with rigorous automated tests covering all trading operations.

* Designed PyDAS to be a reliable developer foundation — fully tested and covering buying, selling, borrowing, and short-selling — rather than a minimal prototype.

---

## Architecture / System Design Bullets

* Architected an algorithmic trading system with a composable strategy model: a configurable Trigger layer for market signals and interchangeable Trade logic modules — enabling rapid strategy iteration without system-level changes.

* Designed plug-and-playable Trade logic components that allow trading strategies to be assembled, modified, and swapped independently of the core execution engine.

---

## Short-Selling / Finance Bullets

* Implemented algorithmic strategies for borrowing and short-selling illiquid US equities on Nasdaq and NYSE, handling the operational complexity of hard-to-borrow names and low-liquidity execution.

* Deployed short-selling strategies to the live market and validated them against real execution conditions — fills, rejections, borrow availability, and latency — on Nasdaq and NYSE.

---

## Low-Latency / Trading Bullets

* Built low-latency Python trading infrastructure for direct-access equity trading, with live deployment on US stock exchanges.

* Developed and deployed algorithmic short-selling strategies for a proprietary trading firm operating on Nasdaq and NYSE.

---

# Strongest Resume Angles

## Algorithmic / Quantitative Trading Roles

Emphasize:

* PyDAS — production Python trading API
* Composable Trigger/Trade logic architecture
* Short-selling and borrowing strategies
* Live Nasdaq/NYSE deployment
* Low-latency Python trading

Strong standalone quant/algo trading story — a complete system from API layer to live strategy execution.

---

## Python / API Development Roles

Emphasize:

* PyDAS API design and implementation
* Rigorous automated testing
* Complete coverage of trading operations
* Clean, reusable developer infrastructure

Demonstrates Python API/SDK development discipline in a demanding, correctness-critical domain.

---

## Financial Services / Fintech Roles

Emphasize:

* US equities domain (Nasdaq, NYSE)
* Short-selling and stock borrowing
* DAS Trader platform
* Live market experience
* Direct-access trading

---

## Systems Architecture Roles

Emphasize:

* Composable strategy architecture
* Configurable Trigger and plug-and-playable Trade logic
* Extensibility by design
* Clean separation of signal and execution

---

# ATS / Keyword Bank

## Trading / Finance Keywords

Algorithmic trading, quantitative trading, short-selling, stock borrowing, hard-to-borrow, illiquid stocks, US equities, Nasdaq, NYSE, DAS Trader, direct-access trading, equity trading, automated trading, trading strategy, low-latency trading, live market trading, proprietary trading.

## Technical Keywords

Python, API development, SDK development, trading API, automated testing, composable architecture, configurable strategy, signal processing, execution logic, trading system, low-latency, financial infrastructure.

---

# External Claim Safety Notes

## Safe to Claim

* Algorithmic trading engineer at Leeds Rising, 2023 (approx. 6 months)
* Developed PyDAS — a complete, rigorously tested Python API to the DAS Trader platform
* PyDAS covered buying, selling, borrowing, and short-selling of US stocks
* Built an algorithmic trading system with configurable Trigger and plug-and-playable Trade logic
* Implemented short-selling and borrowing strategies for illiquid Nasdaq and NYSE stocks
* Deployed and tested strategies on the live market

## Use With Care

* "Low-latency" framing — stated as a domain/skill; ensure the Python implementation genuinely prioritized latency if pressed in interview (Python has latency limitations vs. C++/Rust for HFT)
* Strategy performance — do not claim profitability or specific returns without confirmation

## Avoid Unless Confirmed

* Specific P&L, returns, or trading performance metrics
* Specific stocks or sectors targeted
* Whether PyDAS is publicly available or open-source
* Capital under management or position sizes

---

# Missing / Worth Clarifying

1. Was this a full-time employment, freelance, or consulting engagement?
2. Is PyDAS open-source or publicly available (GitHub)?
3. What was the latency profile of the system — how latency-sensitive was the Python implementation in practice?
4. What testing framework was used for PyDAS automated tests (pytest, unittest, etc.)?
5. What types of Triggers were implemented — price-based, volume-based, time-based, order book signals?
6. What was the broader strategy thesis for short-selling illiquid stocks — momentum, mean reversion, dilution plays, halt trading, etc.?
7. Were the strategies profitable in live testing?
8. How many strategies were built and deployed?
9. Did anyone else work on this system alongside you, or was it a solo build?
10. What, if anything, was Leeds Rising's existing infrastructure before PyDAS?

---

# Relative Positioning Against Other Trading Projects

* **PFP Capital / Solana Low-Latency** — stronger for Solana/DeFi/HFT/Rust low-latency; that is a harder-core performance story
* **Skunk Capital** — stronger for on-chain DEX/MEV trading automation in the crypto space
* **Leeds Rising** — strongest as a **stock-market automated short-trading** story; Python API development, strategy composability, and live US equity deployment are the differentiators here
* **Event Driven Investor (Pairtrade Finder)** — closer in domain (equities, statistical trading) but that was remediation/consulting; Leeds Rising is a full build-and-deploy story
