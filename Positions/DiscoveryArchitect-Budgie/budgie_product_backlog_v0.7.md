# Budgie AI — Product Backlog

**Version:** 0.7 (Draft)

**Date:** 1 May 2026

**Author:** Eddie George, Senior Product Manager, Toptal

---

## Table of Contents

- [Purpose](#purpose)
- [How to Read This Backlog](#how-to-read-this-backlog)
- [Priority & Sizing Key](#priority--sizing-key)
- [Epic 1: Onboarding & Activation](#epic-1-onboarding--activation)
- [Epic 2: Account Aggregation — Banking](#epic-2-account-aggregation--banking)
- [Epic 3: Account Aggregation — Crypto](#epic-3-account-aggregation--crypto)
- [Epic 4: AI Coaching & Personality](#epic-4-ai-coaching--personality)
- [Epic 5: Budget & Expense Management](#epic-5-budget--expense-management)
- [Epic 6: Goal Planning](#epic-6-goal-planning)
- [Epic 7: Financial Health Score](#epic-7-financial-health-score)
- [Epic 8: Ask Anything — Natural Language Queries](#epic-8-ask-anything--natural-language-queries)
- [Epic 9: Notifications & Proactive Engagement](#epic-9-notifications--proactive-engagement)
- [Epic 10: Social Features](#epic-10-social-features)
- [Epic 11: Pricing & Subscription](#epic-11-pricing--subscription)
- [Epic 12: Data & Privacy Infrastructure](#epic-12-data--privacy-infrastructure)
- [Epic 13: Compliance & Regulatory](#epic-13-compliance--regulatory)
- [Epic 14: Analytics & Instrumentation](#epic-14-analytics--instrumentation)
- [Epic 15: Internal Admin & Back Office](#epic-15-internal-admin--back-office)
- [Epic 16: Localisation & Internationalisation](#epic-16-localisation--internationalisation)
- [Appendix](#appendix)

---

## Purpose

This document defines the product backlog for Budgie AI at feature level, organised by epic. It translates the vision and scope captured in the Market Discovery document into buildable work items, each with a priority bucket, rough size estimate, dependencies, and notes on assumptions or open questions.

The backlog is intended to support:
- MVP scope negotiation with the founder
- Technical sizing and architecture planning
- Design prioritisation of user flows
- Delivery planning (timeline, resourcing, risk identification)

This is a feature-level backlog, not a user-story backlog. Each item is sized at a level appropriate for discovery-phase prioritisation, not sprint planning. User stories, acceptance criteria, and detailed specifications are produced during build phase from the agreed MVP items.

---

## How to Read This Backlog

Each epic contains a set of features. For each feature:

- **Priority** — Private Beta / MVP / v1.1 / v2+ (see key below)
- **Size** — rough effort estimate (S / M / L / XL)
- **Dependencies** — other features or external systems required
- **Notes** — assumptions, open questions, or references to the Market Discovery document

Features marked **Private Beta** are required for a controlled, limited-user soft launch ahead of full MVP — the minimum needed to safely put real Singapore users in front of the product and learn from their behaviour. Features marked **MVP** are required for full public day-one launch (the additional scope on top of Private Beta). Features marked **v1.1** are close-in post-launch iterations. Features marked **v2+** are deferred for later consideration and are included here for architectural awareness, not commitment.

**Important caveat on Private Beta scope:** Private Beta is not a "first wave of MVP" in feature terms — it is a structurally complete but feature-narrowed product. Foundational items like data infrastructure, privacy controls, regulatory positioning, basic compliance, geo-restriction, analytics, and the AI guardrail layer ship in Private Beta because no real user can safely use the product without them. The cost saving over MVP comes from cutting *visible feature breadth*, not from cutting *invisible foundations*.

**Open Questions and Assumptions:** Each epic has an "Assumptions & Open Questions" block, and a doc-wide backlog-specific Open Questions list sits in Appendix B. Items struck through have been resolved; the resolution is noted inline with a reference to the relevant epic or feature.

---

## Priority & Sizing

**Priority buckets** (in delivery order):
- **Private Beta** — required for controlled limited-user soft launch ahead of full MVP. Includes both founder-prioritised visible features (per the Founder's note of 1 May: Epics 1, 2, 3, 5, 7 plus simple version of 4) and the structurally required foundations (privacy, compliance, analytics, AI guardrails, admin) without which the product cannot safely run for any user.
- **MVP** — additional scope required for full public day-one launch beyond Private Beta
- **v1.1** — desirable within first 3 months post-launch
- **v2+** — future scope, included for visibility and architectural planning

| Priority | Count | % of total |
|---|---|---|
| Private Beta | 179 | 43% |
| MVP (additional) | 148 | 35% |
| v1.1 | 71 | 17% |
| v2+ | 23 | 5% |
| **Total** | **421** | **100%** |

**Size estimates (rough, discovery-phase):**
- **S** — days of work
- **M** — 1–2 weeks
- **L** — 2–4 weeks
- **XL** — 1+ months or spans multiple disciplines

| Size | Count | % of total |
|---|---|---|
| S | 61 | 14% |
| M | 272 | 65% |
| L | 83 | 20% |
| XL | 5 | 1% |
| **Total** | **421** | **100%** |

*Note: 16.3.6 (SEA language translations) is sized "L per language" and counted as L for this summary.*

All sizes are provisional and subject to refinement by the technical team.

---

## Epic 1: Onboarding & Activation

_First-time user experience from app install through to activated, value-receiving user._

The founder has described a sophisticated onboarding vision: progressive disclosure, AI-led introduction, minimal upfront friction, and feature unlocking as users provide more data. This epic captures the work to deliver that — balancing the founder's vision with realistic v1 scope.

**Key strategic considerations:**
- Onboarding is where most users will drop off if done poorly — every step must earn its place
- The Budgie AI personality should lead the experience, not appear as a feature within it
- Bank connection is a likely friction point and should be introduced only after initial value is demonstrated
- Progressive disclosure means features unlock as data is provided — this must be designed, not just described

### 1.1 First-Launch Experience

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **1.1.1** App install flow and first-launch detection | Private Beta | S | — | Standard; included for completeness |
| **1.1.2** Welcome screen — Budgie introduces itself in character | Private Beta | S | Epic 4 (AI personality defined) | Sets the tone immediately; first-person voice, not a generic splash screen |
| **1.1.3** Enforced introductory tour (skippable or not TBD) | Private Beta | M | 1.1.2 | Founder specified "enforced" — UX tension with friction needs resolving. *Beta: stripped 2-3 screen basic intro; full polished tour is the MVP scope.* |
| **1.1.4** Account creation (email/phone/social login) | Private Beta | M | Epic 12 (identity infrastructure) | Social login (Google/Apple) reduces friction significantly |

### 1.2 AI-Led Initial Engagement

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **1.2.1** Budgie asks critical onboarding questions only (minimise drop-off) | Private Beta | M | 1.1.2, Epic 4 | Founder explicit on this — only critical info upfront |
| **1.2.2** Budgie sets its own tone, check-in cadence, and personality primers with user | MVP | M | Epic 4 | Part of making the AI feel personal from the start. *Beta: hardcoded sensible defaults; user-negotiated tone/cadence stays MVP.* |
| **1.2.3** Progressive information gathering — further questions unlock features over time | v1.1 | L | 1.2.1, feature unlock logic | Important but not strictly required for MVP — can launch with a fixed question set |

### 1.3 Early Value Delivery (Pre-Bank Connection)

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **1.3.1** Generate initial Financial Health Score from onboarding inputs | Private Beta | M | Epic 7 | Hooks user before asking for bank connection — critical value demonstration |
| **1.3.2** Personalised initial Budgie commentary on user's situation | Private Beta | M | Epic 4, 1.3.1 | First "aha" moment — AI speaks to their actual answers |
| **1.3.3** Preview of what Budgie can do once fully connected | MVP | S | 1.3.1 | Manages expectations and motivates connection. *Beta: marketing/expectation-setting; beta users have direct support contact and don't need this.* |

### 1.4 Bank Account Connection

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **1.4.1** Explain bank connection benefit and security before triggering Finverse flow | Private Beta | S | Epic 2 | Trust-building moment; reduces drop-off at the highest-friction step |
| **1.4.2** Invoke Finverse account linking flow | Private Beta | M | Epic 2 | Largely controlled by Finverse's SDK/flow |
| **1.4.3** Handle connection failure, retry, partial connection, and skip paths | Private Beta | M | 1.4.2 | Failure modes are inevitable; product must degrade gracefully |
| **1.4.4** Post-connection celebration / Budgie reacts to seeing the user's data | MVP | S | 1.4.2, Epic 4 | Converts a technical moment into a relationship moment. *Beta: polish moment; beta users don't need a celebration.* |

### 1.5 Feature Unlocking & Progressive Disclosure

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **1.5.1** Feature unlock logic — gate features on completion of prerequisites | v1.1 | L | Requires defined unlock model | Core to founder's vision but implementable post-MVP; v1 can use fixed feature availability |
| **1.5.2** In-app prompts encouraging completion of unlocks | v1.1 | M | 1.5.1 | Secondary to the unlock logic itself |
| **1.5.3** Greyed-out UI elements for features on the roadmap but not yet shipped (e.g. joint accounts, HK-specific options) | MVP | S | — | Workshop 21 April: helps transparency and reinforces the product's direction of travel. Prevents "is this app finished?" perception. Must link to a short explanation when tapped ("coming soon"). *Beta: users have implicit expectation of incompleteness; greyed-out hints are about managing public-user expectations.* |

### 1.6 Onboarding Analytics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **1.6.1** Funnel instrumentation at every onboarding step | Private Beta | M | Epic 14 | Non-negotiable — onboarding is where the most optimisation opportunity lives. *Beta: critical — without analytics, the beta teaches nothing.* |
| **1.6.2** Drop-off alerting and dashboards | v1.1 | S | 1.6.1 | Data is MVP; dashboards can follow |

### Epic 1 — Assumptions & Open Questions

**Assumptions:**
- The founder's stated "enforced tour" is the design intent but may soften to "strongly suggested" in user testing
- Social login (Google/Apple) will be acceptable to the founder as the default authentication method
- Finverse provides a hosted or SDK-based flow that handles the bank authorisation UX rather than requiring Budgie to build it from scratch

**Open Questions:**
- How strict is "enforced" for the introductory tour? Does this extend to not allowing skip at all?
- What happens if a user completes onboarding but never connects a bank account — is there a useful "demo mode" or do they churn?
- What's the minimum set of onboarding questions to generate a meaningful Financial Health Score?
- Does the founder want a waitlist / referral onboarding mechanic for early launch, or is it open access from day one?

---

## Epic 2: Account Aggregation — Banking

_Connecting, refreshing, and managing bank account data via Finverse._

Bank aggregation is the single biggest technical dependency in the MVP. Finverse's capabilities in Singapore — bank coverage, account scope, transaction history, pricing, and re-authentication model — were substantially clarified at the 20 April workshop (Market Discovery 8.1). What remains to be verified is data quality, real-world reliability, and whether any of the 2FA-per-refresh friction can be mitigated. A pending Finverse call and a running alternative-aggregator evaluation both feed into the final banking-integration decision.

**Key strategic considerations:**
- MVP is read-only — no payment initiation, no account actions. This deliberately constrains scope, reduces regulatory exposure, and lowers trust barriers (Market Discovery 8.1, 13.1).
- Data quality from Finverse is unverified — assume some banks return incomplete or inconsistent data and design for it.
- Re-authentication is confirmed as the core friction: Finverse requires 2FA per connected account on every refresh (20 April workshop). This directly undermines the engagement model and is the driver of the running alternative-aggregator evaluation (Market Discovery 8.1).
- Account connection is also a key drop-off point in onboarding (Epic 1) and a major contributor to churn if it breaks mid-flow.

### 2.1 Finverse Integration — Core

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **2.1.1** Technical spike: verify Finverse data quality, real-world reliability, and whether 2FA-per-refresh friction can be mitigated (coverage, history, and pricing are already confirmed — Market Discovery 8.1) | Private Beta | M | Finverse account | **Must happen early** — outputs of this spike, combined with the alternative-aggregator evaluation, will resize this epic and determine the final banking-integration approach |
| **2.1.2** Finverse SDK/API integration into mobile app | Private Beta | L | 2.1.1 | Core plumbing |
| **2.1.3** Bank account linking flow (invoked from onboarding and settings) | Private Beta | M | 2.1.2 | Shared UX entry point from multiple surfaces |
| **2.1.4** Secure storage and refresh of Finverse access tokens | Private Beta | M | 2.1.2, Epic 12 | Sensitive — must follow data architecture decisions |
| **2.1.5** Handle Finverse connection failures, timeouts, and error states gracefully | Private Beta | M | 2.1.2 | Real-world APIs fail; product must not |

### 2.2 Data Retrieval & Refresh

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **2.2.1** Retrieve account balance and metadata on connection | Private Beta | S | 2.1.2 | Initial data load |
| **2.2.2** Retrieve transaction history (as far back as Finverse provides) | Private Beta | M | 2.1.2, 2.1.1 | History depth depends on Finverse and bank — user expectations must be managed |
| **2.2.3** Scheduled refresh of balances and transactions | Private Beta | M | 2.1.2 | Frequency TBD. In the current Finverse model, scheduled refreshes require 2FA per account — effectively limiting to user-triggered (2.2.4). True scheduled/background refresh depends on the alternative-aggregator evaluation outcome. *Beta: framework built but configured manual-only; active scheduling depends on alternative-aggregator outcome — sized as build-now to avoid retrofit later.* |
| **2.2.4** On-demand user-triggered refresh | Private Beta | S | 2.2.3 | User trust mechanism — "I just got paid, why doesn't Budgie see it?" |
| **2.2.5** Background sync with notification on significant changes | v1.1 | M | 2.2.3, Epic 9 | Powers proactive alerts |

### 2.3 Account Management

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **2.3.1** View list of connected accounts | Private Beta | S | 2.1.2 | Basic account dashboard |
| **2.3.2** Disconnect / remove a connected account | Private Beta | S | 2.1.2, Epic 12 | Must also clean up associated data per privacy requirements |
| **2.3.3** Reconnect / re-authenticate an account after credential expiry | Private Beta | M | 2.1.2 | Will happen frequently; UX matters |
| **2.3.4** Display connection status and last-refresh timestamp per account | Private Beta | S | 2.2.3 | Transparency about data freshness |
| **2.3.5** Support multiple accounts across multiple banks per user | Private Beta | S | 2.1.2 | Core to the "fragmented accounts" value proposition |

### 2.4 Data Quality & Normalisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **2.4.1** Normalise transaction data across banks into a consistent internal model | Private Beta | L | 2.2.2 | Different banks return different formats — this is non-trivial |
| **2.4.2** Deduplicate transactions across refresh cycles | Private Beta | M | 2.2.3 | Finverse may return overlapping data across syncs |
| **2.4.3** Handle pending vs cleared transactions | Private Beta | M | 2.4.1 | Affects balance accuracy and user trust |
| **2.4.4** Multi-currency support for accounts in different currencies | v1.1 | L | 2.4.1 | Singapore users often hold USD/GBP accounts; v2 expansion requires this |

### 2.5 Supported Institutions

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **2.5.1** Define and document which Singapore banks are supported at launch | Private Beta | S | 2.1.1 | Finverse confirmed top 3 SG retail banks covered (20 April workshop). Final list — and coverage depth per bank — pending the spike and any expansion via alternative providers. Shapes marketing and expectations. |
| **2.5.2** Graceful handling for banks not supported by Finverse (manual-entry fallback TBD) | v1.1 | M | 2.5.1 | Users will expect all their accounts; unsupported banks are a churn risk |

### 2.6 Manual Entry (Fallback)

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **2.6.1** Manual CPF entry — user enters their CPF balance (Ordinary, Special, Medisave as applicable) | Private Beta | M | 2.4.1 | Fallback for CPF, which sits behind SingPass and is not covered by Finverse. CPF balances change infrequently (monthly contributions + stable interest) so manual entry is a viable substitute. Included because CPF is a material part of most Singaporeans' net worth — excluding it would leave a significant gap in the visibility-first proposition. *Beta: low engineering effort but high impact on beta net-worth credibility — CPF is the largest asset for most SG users; excluding it would understate net worth materially.* |
| **2.6.2** Periodic prompt to refresh manually-entered values | Private Beta | S | 2.6.1 | Without refresh prompts, manual values go stale and degrade the net-worth view. Suggested cadence: monthly. |
| **2.6.3** Visual distinction between connected and manually-entered accounts | Private Beta | S | 2.6.1, Epic 1 | Users need to know which numbers are live vs last-entered — trust depends on this being obvious. |

### Epic 2 — Assumptions & Open Questions

**Assumptions:**
- Finverse covers the top 3 Singapore retail banks (workshop-confirmed — likely DBS, OCBC, UOB) and the top 5 in Hong Kong. Coverage of other banks (Standard Chartered, HSBC, Citi) is unverified — an alternative-aggregator evaluation is in progress for broader coverage
- Finverse provides up to 2 years of historical transaction data per connected account, with a typical minimum of around 6 months (20 April workshop)
- Finverse hosts the account authorisation UX (user is redirected to bank login and back), so Budgie does not need to build this from scratch
- Read-only access only in MVP — no payment initiation
- CPF will not be available via automated integration in MVP (Finverse doesn't cover it; SGFinDex integration not in MVP scope), and manual entry is an acceptable substitute for visibility-first functionality

**Open Questions:**
- ~~What is Finverse's pricing model, and does it scale with our cost assumptions?~~ — **Partially resolved (20 April workshop):** pricing is per connected bank account per month. **Still open:** specific rates and whether they align with unit economics assumptions (Market Discovery 9.4)
- ~~What banks does Finverse actually cover in Singapore, and to what depth?~~ — **Partially resolved (20 April workshop):** top 3 SG retail banks + top 5 HK, personal accounts only, with variable support for account types. **Still open:** which specific banks, coverage depth per bank, and account-type specifics (deliverable from the spike, 2.1.1)
- ~~What is the re-authentication frequency? Daily, weekly, every 90 days?~~ — **Resolved (20 April workshop):** 2FA is required on every refresh for every connected bank account. This is the driver of the alternative-aggregator evaluation (Market Discovery 8.1)
- Does Finverse provide credit card transaction data, or only bank account data?
- ~~Is there a manual-entry fallback for accounts Finverse can't connect to, and is that in MVP or deferred?~~ — **Resolved:** manual entry is MVP for CPF specifically (Section 2.6); other non-connected assets deferred pending the generalisation decision below
- Should the manual-entry pattern be extended to other non-aggregated assets (overseas accounts, pensions, private investments) in v1.1+, or kept CPF-specific? Risk of drift toward "spreadsheet replacement" if generalised without care.
- What's the expected sync frequency — every few hours, daily, on-demand only?

---

## Epic 3: Account Aggregation — Crypto

_Connecting and tracking crypto holdings via exchange APIs and on-chain addresses._

Crypto aggregation is a meaningful differentiator for Budgie but carries significant scope uncertainty. The range from "show balances from one exchange" to "track DeFi positions across multiple chains and protocols" represents orders of magnitude of effort. This epic deliberately separates the easy wins from the genuine engineering journey.

**Key strategic considerations:**
- MVP crypto scope was confirmed at the 20 April workshop: exchange holdings plus on-chain wallet balances, no DeFi, no NFTs, no transaction-level on-chain data (Market Discovery Section 8.3)
- Exchange balance tracking is relatively cheap; DeFi position tracking is not (Market Discovery 8.3)
- Crypto adds regulatory complexity in Hong Kong and potentially Singapore (Market Discovery 13.1.2)
- The "unified TradFi + DeFi view" is positioned as a core differentiator but is a multi-year engineering journey if done fully (Market Discovery 12.2)
- A credible minimum-viable crypto offering (e.g. one or two major exchanges + one wallet address type) is enough to validate the positioning without committing to the full vision

### 3.1 Crypto Exchange Integration

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **3.1.1** Select and document the 1–2 crypto exchanges to support at launch | Private Beta | S | Founder decision | MVP limited to native balances of major coins (BTC, ETH, SOL) on major exchanges — no obscure tokens, no NFTs |
| **3.1.2** Exchange API integration (read-only, per selected exchange) | Private Beta | L | 3.1.1 | Each exchange is effectively a separate integration |
| **3.1.3** Exchange account connection flow (API key or OAuth) | Private Beta | M | 3.1.2 | API key entry has security UX implications |
| **3.1.4** Retrieve balances, holdings, and transaction history from exchange | Private Beta | M | 3.1.2 | Analogous to Epic 2 for banks |
| **3.1.5** Handle exchange API rate limits, errors, and outages | Private Beta | M | 3.1.2 | Crypto exchange APIs are less mature than bank APIs — expect issues |

### 3.2 On-Chain Wallet Tracking

**Scope clarification:** MVP on-chain coverage is **balance-only** — the system reads token balances by public address but does not index on-chain transactions. Transaction-level on-chain data is out of MVP scope due to uneven availability across chains and the additional engineering load; it can be revisited for v1.1+. This is the key difference from Epic 3.1 (exchanges), where transaction history is also retrieved.

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **3.2.1** User-entered wallet address tracking (read-only by address) | Private Beta | M | Blockchain data provider (3.2.2) | Balance-only reads — no transaction-level data in MVP. Users paste a public address; system fetches token balances on supported chains. |
| **3.2.2** Select and integrate a blockchain data provider (e.g. Alchemy, Moralis, Covalent) | Private Beta | L | — | A balance-focused provider is sufficient for MVP — full transaction indexing not required. Provider must support the chains in 3.2.3 and 3.2.4. |
| **3.2.3** Support Ethereum / EVM chains | Private Beta | M | 3.2.2 | Native ETH + ERC-20 token balance reads on Ethereum mainnet. Other EVM chains (Polygon, Arbitrum, Base, etc.) may come "free" with the chosen provider or require per-chain enablement — decide at provider-selection time. |
| **3.2.4** Support Bitcoin addresses | Private Beta | M | 3.2.2 | Bitcoin balance reads by address. Separate data model from EVM — additional integration work. *Beta: BTC is the most-held crypto by SG retail; excluding leaves a similar gap to excluding CPF — sized as required for beta despite the separate-from-EVM engineering load.* |
| **3.2.5** Support Solana / other L1 chains | v1.1 | L | 3.2.2 | Workshop specified BTC/ETH/SOL on **exchanges** as MVP, but on-chain coverage committed only to EVM + Bitcoin for MVP. SOL on-chain and other L1s deferred to v1.1 — there is product pull since SOL is MVP on the exchange side. |

### 3.3 DeFi Position Tracking

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **3.3.1** Detect user's DeFi protocol positions (yield farms, lending, staking) | v2+ | XL | 3.2.2 | Each protocol has its own data structure; significant ongoing engineering |
| **3.3.2** Track DeFi position value over time | v2+ | L | 3.3.1 | Position valuation is non-trivial given changing token prices and rewards |
| **3.3.3** Alert on DeFi-specific events (liquidation risk, reward claims, protocol changes) | v2+ | L | 3.3.1, Epic 9 | High-value features but unsuitable for MVP |

### 3.4 Crypto Data Normalisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **3.4.1** Normalise crypto holdings into a consistent internal model (shared with bank accounts where sensible) | Private Beta | L | 3.1.4 | Foundational — affects how unified views render. MVP scope covers both exchange data and on-chain wallet balances; normalisation model must handle both. |
| **3.4.2** Fiat valuation of crypto holdings using live price feeds | Private Beta | M | 3.4.1 | Required for any unified net worth view |
| **3.4.3** Handle tokens without reliable price data | MVP | S | 3.4.2 | Common edge case; users hold obscure tokens. *Beta: obscure tokens shown as "valuation unavailable" placeholder is enough; full handling (alt price sources, manual override) stays MVP.* |

### 3.5 Account Management

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **3.5.1** View list of connected crypto accounts and wallets | Private Beta | S | 3.1.2 | Parallels Epic 2.3.1 for banks. MVP scope covers exchange accounts and on-chain wallet addresses — list view must accommodate both. |
| **3.5.2** Disconnect / remove a crypto account or wallet | Private Beta | S | Epic 12 | Must clean up data per privacy requirements |
| **3.5.3** Refresh on-demand and scheduled | Private Beta | M | 3.1.4 | Crypto markets move fast — users expect up-to-date data |

### Epic 3 — Assumptions & Open Questions

**Assumptions:**
- MVP crypto scope is: exchange holdings (balances and transaction history via exchange APIs), plus on-chain wallet **balances** by public address — no transaction-level on-chain data, no DeFi positions, no NFTs
- Users who want to track crypto are willing to either generate a read-only API key on an exchange or enter a public wallet address
- A third-party blockchain data provider (rather than self-hosted node infrastructure) is acceptable from cost, latency, and data sovereignty perspectives
- One or two EVM chains are enough for v1; additional chains are v1.1 / v2+

**Open Questions:**
- ~~Is crypto aggregation in MVP scope at all, or deferred to v1.1 in favour of a sharper bank-only launch? (Market Discovery Open Question #7)~~ — **Resolved (20 April workshop):** in MVP; scope confirmed as exchange holdings + on-chain wallet balances (Section 3.2 scope clarification; MD Section 8.3)
- Which specific exchanges do target users in Singapore use most — is there research to guide the v1 selection?
- ~~Does the founder want to support NFT visibility in the wallet view, or is it token-only for v1?~~ — **Resolved (20 April workshop):** no NFTs in MVP
- How are stablecoins represented in the net worth view — as crypto, as cash-equivalent, or user-configurable?
- What's the policy on wallets associated with mixers, sanctioned addresses, or other flagged activity? (This is a compliance question that will need to be answered before launch.)

---

## Epic 4: AI Coaching & Personality

_The Budgie AI character, its conversational behaviour, and the coaching logic that powers proactive engagement. The core differentiator._

This epic captures what makes Budgie different from every other budgeting app. Most competitors bolt on a chatbox; Budgie positions the AI personality *as the product*, with financial data as the fuel (Market Discovery 10.2). Everything here needs to serve that positioning.

**Key strategic considerations:**
- The AI personality is the core product, not a feature — investment in tone, voice, and contextual quality matters more than building sophisticated data visualisations (Market Discovery 10.2)
- Budgie is also the brand face across social media and external surfaces — the personality must be consistent across app, social, email, and notifications (Market Discovery 10.2)
- Explainability is essential — users must understand *why* Budgie is saying what it says, not just *what* (Market Discovery 8.2)
- Hallucination risk is particularly dangerous in financial contexts — mitigated by tool-augmented calculations (LLM does not compute) and RAG-constrained external knowledge (Market Discovery 8.2, 20 April workshop)
- The AI's boundaries matter for regulatory reasons — it must not stray into personalised investment advice (Market Discovery 13.1)
- Proactive daily engagement that remains useful over weeks and months is one of the hardest product design challenges in the concept (Market Discovery 12.2)

### 4.1 Budgie Personality Definition

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.1.1** Define Budgie's character, voice, tone, and personality traits (document) | Private Beta | M | Founder input, design partner | Foundational — every other AI feature depends on this |
| **4.1.2** Define conversational style guide (phrasing, humour level, warmth, formality) | Private Beta | M | 4.1.1 | How Budgie speaks is as important as what Budgie says |
| **4.1.3** Define Budgie's boundaries — what it will and won't say | Private Beta | M | 4.1.1, Epic 13 | Regulatory guardrails, sensitive topics, areas of avoidance |
| **4.1.4** Visual representation of Budgie (avatar, mascot, or stylistic cue) | Private Beta | M | Design partner | The character needs a face, even if minimal |
| **4.1.5** Enforce Budgie's public voice as consistent across all external surfaces (social, email, support, website) — one character, no per-surface variation | MVP | S | 4.1.1, 4.1.2 | Workshop confirmed 21 April: the public voice is fixed. Implementation note not a feature in its own right, but needs an owner — usually the content approval process (Epic 13.5). *Beta: cross-surface (social, email, website) enforcement is for public launch; beta is in-app only.* |
| **4.1.6** In-app user tone preference — user can adjust in-chat tone (more formal/casual) within a session; preference does not persist across sessions | MVP | M | 4.1.1, 4.2.2 | Workshop 21 April: single-voice MVP with lightweight per-session dial. Selectable personality *types* deferred to later release — this is the minimal form. *Beta: polish feature; beta runs on fixed default voice.* |

### 4.2 Core AI Infrastructure

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.2.1** Finalise LLM provider commercial terms and data policies | Private Beta | M | Epic 12 (data policies) | Claude selected at 20 April workshop as the preferred LLM — commercial terms pending; data retention / usage policies require formal review against PDPA/PDPO (Market Discovery 13.2) |
| **4.2.2** Prompt engineering foundation — system prompts embedding Budgie's personality | Private Beta | L | 4.1.1, 4.2.1 | Significant investment; ongoing refinement |
| **4.2.3** Context assembly — injecting relevant user data into prompts at the right moments | Private Beta | L | 4.2.1, Epic 2, Epic 5 | Critical for explainability and quality |
| **4.2.4** Response filtering and guardrails — preventing off-topic, unsafe, or out-of-scope outputs | Private Beta | L | 4.2.1, 4.1.3 | Essential for regulatory and brand safety |
| **4.2.5** LLM cost and usage monitoring per user and in aggregate | Private Beta | M | 4.2.1, Epic 14 | LLM costs are a unit economics factor that must be tracked from day one |
| **4.2.6** Retrieval Augmented Generation (RAG) with curated source library — limit external knowledge to credible sources (e.g. Investopedia, regulatory sites) with source citations shown in responses | MVP | L | 4.2.1, 4.2.4 | Design team decision — prevents misinformation by restricting what the AI can reference beyond user data. Citations increase transparency and trust. *Beta: data-grounded chat only — when asked broader questions, AI says "I can only discuss your data right now"; full RAG with citations is MVP.* |
| **4.2.7** Deterministic calculation tool library — the LLM calls dedicated tools for all arithmetic (totals, rates, averages, projections) rather than computing inline | Private Beta | L | 4.2.1, Epic 2, Epic 5 | Tool-augmented architecture confirmed at 20 April workshop (Market Discovery 8.2). Materially reduces hallucination risk and keeps financial outputs auditable. Works in tandem with 4.5.3 (enforcement) and 4.5.4 (audit log). |

### 4.3 Contextual AI Engagement

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.3.1** Identify key "moments" where contextual AI engages (post-transaction, goal milestone, threshold breach, etc.) | MVP | M | 4.2.2 | Design decision — not every screen needs AI. *Beta: push pattern — beta keeps AI in chat surface only, not embedded across screens.* |
| **4.3.2** In-context AI comments/insights embedded at those moments (not in a separate chatbox) | MVP | L | 4.3.1, 4.2.3 | Core differentiator — AI *embedded*, not bolted on (Market Discovery 10.2). *Beta: push pattern deferred — depends on 4.3.1.* |
| **4.3.3** User-initiated AI interaction from any screen (tap Budgie to ask) | v1.1 | M | 4.2.1, Epic 8 | Complements Epic 8; can be deferred if Epic 8 covers the ask-anywhere need |

### 4.4 Proactive Coaching

The engagement model has two tiers confirmed at the 20 April workshop: brief daily check-ins (notification-style touchpoints), and more comprehensive weekly coaching sessions (system-scheduled, advisor-session format). Neither is user-initiated — users cannot launch a coaching session at will. "Ask Anything" (Epic 8) is the user-initiated channel. The same proactive-insight mechanism also fires event-driven alerts outside the scheduled cadences.

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.4.1** Daily check-in framework — Budgie initiates a short, notification-style touchpoint (brief by design, not a full session) | MVP | L | 4.2.3, Epic 9 | Habit loop — must be useful, varied, and non-annoying. *Beta: push pattern — daily proactive engagement deferred; beta tests reactive chat only.* |
| **4.4.2** Content variation engine — avoid repetition in daily check-ins | MVP | L | 4.4.1 | One of the hardest problems — users churn when AI feels repetitive. *Beta: depends on 4.4.1.* |
| **4.4.3** User control over check-in frequency and style | MVP | M | 4.4.1 | Prevents the "annoying notification" failure mode. *Beta: depends on 4.4.1.* |
| **4.4.4** Proactive insights triggered by specific data events (unusual spending, goal at risk, etc.) | MVP | L | 4.2.3, Epic 5, Epic 6 | The predictive/warning capability — a key differentiator. *Beta: push pattern deferred.* |
| **4.4.5** Longer-horizon predictive coaching (spending pattern extrapolation, cash-flow forecasting) | v1.1 | XL | 4.4.4 | Requires sufficient data history; genuinely predictive AI is hard |
| **4.4.6** Weekly coaching session framework — system-scheduled, comprehensive coaching engagement modelled on an in-person financial advisor session | MVP | L | 4.2.3, Epic 9 | 20 April workshop — the weekly cadence and advisor-session format are the defining product choice here. Users cannot self-initiate; scheduled weekly with user notification. Entry flow takes the user from a notification into the session UI. *Beta: push pattern — system-scheduled coaching deferred.* |
| **4.4.7** Weekly session content orchestration — for each user's weekly session, curate what's covered (progress review, themes from the week, flagged changes, trade-offs) | MVP | L | 4.4.6, 4.2.3, Epic 5, Epic 6, Epic 7 | Distinct layer from the framework — this decides *what* a given user's session contains, drawing on their data, goals, and FHS movement. Content quality is the felt-value of the session. *Beta: depends on 4.4.6.* |
| **4.4.8** Monthly review card on dashboard — month-over-month trends, monthly financial highlights, recalibration | v1.1 | L | 4.4.6, 4.4.7, Epic 5, Epic 7 | Workshop 21 April: requested as a dashboard card alongside daily/weekly. Defaults to v1.1 because a month of real user data is needed before the review is meaningful. |
| **4.4.9** Yearly review card on dashboard — year-over-year retrospective, annual narrative, next-year goal setting | v2+ | L | 4.4.8 | Workshop 21 April: requested for eventual inclusion. A year of real data needed, so v2+ is the honest priority. |

### 4.5 Explainability

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.5.1** All AI insights are traceable to underlying data (show the "why") | Private Beta | L | 4.2.3 | Market Discovery 8.2 — essential for trust and compliance |
| **4.5.2** "Show me why" / "show me the numbers" interaction on AI messages | Private Beta | M | 4.5.1 | User-initiated deeper explanation |
| **4.5.3** Enforce that all quantitative claims come from actual user data via the calculation tool library (4.2.7), not LLM generation | Private Beta | L | 4.2.3, 4.2.4, 4.2.7 | Tool-augmented architecture (Market Discovery 8.2) — the LLM orchestrates but does not compute. Hallucination prevention — critical for financial trust. |
| **4.5.4** Audit log of AI interactions for dispute and review purposes | Private Beta | M | Epic 12, Epic 13 | Regulatory and liability requirement (Market Discovery 13.3.3) |

### 4.6 Memory & Personalisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.6.1** Short-term conversation memory within a session | Private Beta | M | 4.2.1 | Standard for conversational AI |
| **4.6.2** Long-term memory — Budgie remembers key user facts, preferences, goals over time | Private Beta | L | 4.2.3, Epic 12 | Key to making Budgie feel personal rather than generic. Retention scope is bounded by token-cost economics — long-term persistence of all interaction history is neither necessary nor affordable. MVP design needs to define what's retained verbatim, what's summarised, and what's dropped. *Beta: simpler retention logic — keep last N exchanges plus key user facts; full token-economics-tuned retention model lands in MVP.* |
| **4.6.3** User can view, edit, and delete what Budgie remembers about them | Private Beta | M | 4.6.2, Epic 12 | Privacy and trust requirement |
| **4.6.4** Personalisation deepens over time as more data is gathered | v1.1 | L | 4.6.2 | Natural evolution of 4.6.2; not strictly MVP |

### 4.7 Budgie as Brand Voice (Cross-Surface)

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **4.7.1** Shared personality guidelines for Budgie across app, email, push notifications, and social media | MVP | M | 4.1.1, 4.1.2 | Budgie is the public face of the brand (Market Discovery 10.2). *Beta: in-app only; cross-surface guidelines for public launch.* |
| **4.7.2** Content approval / voice consistency process for Budgie's social media posts | MVP | M | 4.7.1, Epic 13 | Social media is regulated like any other financial advertising (Market Discovery 13.1.4). *Beta: no active social posting required.* |
| **4.7.3** Transactional email and notification copy written in Budgie's voice | MVP | M | 4.7.1, Epic 9 | Consistency is the differentiator — even receipts should sound like Budgie. *Beta: generic system emails are fine; beta users have direct team contact.* |

### Epic 4 — Assumptions & Open Questions

**Assumptions:**
- Claude (selected as the preferred LLM at the 20 April workshop) will be acceptable from both a cost and a data-handling perspective — commercial terms and formal data-policy review still pending
- Budgie's personality will be defined by the founder with design support, not discovered through user research (though it should be tested with users post-launch)
- Hallucination prevention via prompt architecture, data grounding, tool-augmented calculations (4.2.7) and RAG-constrained external knowledge (4.2.6) is sufficient without bespoke model fine-tuning at MVP stage
- Proactive coaching at MVP is a mix of rule-based triggers (from data events) and LLM-generated content, rather than fully AI-driven decisioning

**Open Questions:**
- Is the founder's vision for Budgie's personality documented anywhere, or does it need to be created from scratch in this engagement?
- How much content variation is required to sustain daily check-ins for a 90-day user — this drives the size of 4.4.2 significantly
- What LLM provider is preferred, and has any commercial conversation happened? — **Partially resolved (20 April workshop):** Claude is the preferred LLM. **Still open:** commercial conversation status.
- ~~Is there a human review loop in the AI flow for edge cases, or is the AI fully autonomous at MVP?~~ — **Resolved (20 April workshop):** fully autonomous, no human escalation team at MVP (Market Discovery 13.3.1)
- What's the policy on Budgie's tone when discussing sensitive topics — job loss, divorce, debt distress? These will come up.
- Should Budgie have visible "limits" the user can see (e.g. "I don't talk about specific investments") or should that be invisible?

---

## Epic 5: Budget & Expense Management

_Transaction categorisation, budget tracking, spending analysis, and in-app visibility of where money is going._

This epic covers the "traditional" budgeting functionality — the table-stakes features users expect from any finance app. While these are not the differentiators (that's Epic 4), they are the foundation on which the AI coaching stands. Budgie can't give good advice about spending without first understanding where the money is going.

**Key strategic considerations:**
- The founder's website claims "97%+ accuracy" on transaction categorisation — the basis for this claim is unverified (Market Discovery 8.2). The MVP needs to deliver credible accuracy without overclaiming.
- Transaction data quality varies by bank and by Finverse's data depth — categorisation logic must be robust to messy inputs (Market Discovery 8.1).
- Proactive budget warnings (before overspending happens) are a stated founder differentiator vs reactive dashboards (Market Discovery 4.1).
- Categorisation and budgeting data powers Epic 4 (AI coaching) and Epic 7 (Financial Health Score) — it's a foundational capability, not an isolated feature.
- Localisation matters — Asian merchants, currencies, and transaction patterns differ from Western defaults used by most categorisation ML models.

### 5.1 Transaction Categorisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **5.1.1** Build or integrate a transaction categorisation engine | Private Beta | L | Epic 2 | Build-vs-buy decision; third-party options exist but need Asian market validation. **24 April workshop flagged specific risk:** transaction descriptions from SG/HK banks may contain non-English text (Mandarin, Cantonese character strings, mixed scripts) which Western categorisation engines handle poorly. Proprietary in-house engine is on the table — Tech Lead to assess. |
| **5.1.2** Define the category taxonomy (e.g. Food, Transport, Housing, Entertainment, etc.) | Private Beta | M | 5.1.1 | Foundational — affects everything downstream |
| **5.1.3** Auto-categorise incoming transactions | Private Beta | M | 5.1.1, 5.1.2 | Core feature users expect |
| **5.1.4** User can recategorise transactions manually | Private Beta | M | 5.1.3 | Essential — auto-categorisation is never 100% accurate |
| **5.1.5** Learn from user corrections to improve future categorisation | v1.1 | L | 5.1.4 | Per-user improvement; meaningful but not MVP-blocking |
| **5.1.6** Support custom user-defined categories | v1.1 | M | 5.1.2 | Power-user feature |
| **5.1.7** Handle split transactions (one charge across multiple categories) | v1.1 | M | 5.1.3 | Common edge case but complex UX |

### 5.2 Spending Analysis

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **5.2.1** Monthly spending summary by category | Private Beta | M | 5.1.3 | Core dashboard element |
| **5.2.2** Spending trends over time (weekly/monthly/quarterly views) | Private Beta | M | 5.2.1 | Shows patterns the user may not have noticed. Finverse provides 6 months historic — trends are meaningful from day 1. |
| **5.2.3** Spending vs income comparison | Private Beta | S | 5.2.1, Epic 2 | Simple but high-value view |
| **5.2.4** Identify unusual or anomalous transactions | MVP | M | 5.1.3, Epic 4 | Feeds into proactive AI insights. *Beta: detection logic feeds proactive AI insights (Epic 4.4.4) — without that channel in beta, user-facing value is limited.* |
| **5.2.5** Cross-account spending view (unified across all connected accounts) | Private Beta | M | Epic 2 | Critical for the "fragmented finances" value prop |
| **5.2.6** Merchant-level spending view ("how much have I spent at X?") | v1.1 | M | 5.1.3 | Useful but not MVP-critical |

### 5.3 Budget Creation & Tracking

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **5.3.1** User creates monthly budgets per category | Private Beta | M | 5.1.2 | Core budgeting feature |
| **5.3.2** Real-time tracking of spending against budget | Private Beta | M | 5.3.1, 5.1.3 | Updates as transactions come in |
| **5.3.3** Proactive warning when approaching budget limit | MVP | M | 5.3.2, Epic 9 | Founder differentiator — warn before, not after (Market Discovery 4.1). *Beta: push pattern — beta users see budget status visually in-app (5.3.2); proactive alerts deferred with the rest of the push layer.* |
| **5.3.4** Budget overspend alerts | MVP | S | 5.3.2, Epic 9 | Backup to 5.3.3. *Beta: push pattern deferred.* |
| **5.3.5** Budgie-suggested budgets based on the user's actual spending history | Private Beta | M | 5.1.3, Epic 4 | Removes the blank-page problem for new users |
| **5.3.6** Budget rollover (unspent money carries to next month) | v1.1 | M | 5.3.1 | Popular feature in budgeting apps (YNAB-style) |
| **5.3.7** Shared budgets (household, couples, roommates) | v2+ | L | Epic 10 | Significantly more complex — deferred |

### 5.4 Subscription & Recurring Transaction Tracking

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **5.4.1** Detect recurring payments and subscriptions automatically | MVP | M | 5.1.3 | Rocket Money's core value prop; table stakes for a modern budgeting app. *Beta: feature breadth deferred — beta users see subscriptions as regular transactions in the categorised view; dedicated detection + dashboard adds value but isn't foundational.* |
| **5.4.2** Subscription dashboard — list all detected subscriptions with totals | MVP | M | 5.4.1 | High-value view for users. *Beta: depends on 5.4.1.* |
| **5.4.3** Alert on subscription price changes | v1.1 | M | 5.4.1, Epic 9 | Nice-to-have; demonstrates active monitoring |
| **5.4.4** Alert on unused subscriptions (no engagement after N months) | v1.1 | L | 5.4.1 | Genuinely useful but harder to detect reliably |

### 5.5 Income Tracking

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **5.5.1** Detect and categorise income transactions | Private Beta | M | 5.1.1 | Often just salary but may include multiple sources |
| **5.5.2** Income trend view | Private Beta | S | 5.5.1 | Simple but important, especially for variable income earners |
| **5.5.3** Expected vs actual income comparison | v1.1 | M | 5.5.1 | Useful for freelancers, commission earners |

### Epic 5 — Assumptions & Open Questions

**Assumptions:**
- Transaction categorisation can achieve acceptable accuracy in Asian markets without significant pre-launch training data (Market Discovery Assumption A12)
- A category taxonomy of around 15–25 top-level categories (with optional sub-categories) is sufficient for v1
- Users will accept that categorisation is imperfect and will be willing to correct mistakes
- Budget-setting is a sufficiently strong habit to build an MVP around — some users will set a budget and engage with it; others won't

**Open Questions:**
- What's the basis for the website's "97%+ accuracy" claim, and is it something to validate or quietly retire? (Market Discovery Open Question #9)
- Is the category taxonomy localised for Singapore/HK (e.g. hawker food, MRT, red packets, property tax) or generic Western categories?
- Should budgets be "zero-based" (every dollar assigned, YNAB-style) or "envelope" (allocate to categories and spend)? The UX implications are significantly different.
- How does the product handle users who never set budgets — is there a "passive mode" that still provides value?
- For subscription detection, is there a third-party service (e.g. similar to Rocket Money's backend) that could be licensed rather than built?
- Should we build a proprietary transaction categorisation engine tuned for Asian markets (handles non-English descriptions, local merchant taxonomy) versus integrate a third-party engine and wrap it? 24 April workshop flagged this as a real build-vs-buy decision for the Tech Lead to assess.

---

## Epic 6: Goal Planning

_User-defined financial goals (savings, debt, targets), roadmaps to reach them, and ongoing tracking._

Goals are what transform Budgie from a financial observer into an active participant in the user's life. A user with a goal has a reason to keep opening the app. Goals also directly address two of the secondary personas identified in discovery — the goal-driven saver (house, car, wedding) and the debt manager (Market Discovery 3.2).

**Key strategic considerations:**
- Goal-oriented users have natural retention mechanics — ongoing progress tracking and accountability (Market Discovery 3.2, 11.3).
- The founder's market research acknowledges that "unify + decision layer" is the gap — goals are a key part of the "decision" side of that equation.
- Dynamic goals (adjusting based on actual behaviour) are a founder differentiator vs static target setting (Market Discovery 4.1).
- Debt payoff goals are treated as savings-style goals for MVP (user sets target, system tracks progress) — deliberately avoiding prioritisation strategies, consolidation, or relief advice, which sit in regulated debt-advisory territory (Market Discovery 13.1.3, 20 April workshop).
- Goals tie heavily into Epic 4 (AI coaching) — the AI should reference goals when discussing spending, budgets, and decisions.
- **Beta scope:** Epic 6 defers entirely to MVP per the Founder's 1 May guidance ("replace Epic 6 with Epic 3"). Nothing in this epic is structurally required for the integrity of Private Beta — goals are a feature layer that adds engagement and depth, not a foundation. The entire epic ships at MVP. Other epics that reference goals (FHS, Ask Anything, Notifications, Social) handle the absence gracefully in beta.

### 6.1 Goal Definition & Setup

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **6.1.1** User creates a savings goal with target amount and target date | MVP | M | Epic 2 | Core goal creation flow |
| **6.1.2** User creates a debt payoff goal with current balance and target payoff date | MVP | M | Epic 2 | Treated as a savings-style goal for MVP — user sets the payoff target and date, system tracks progress. The AI does not advise on debt prioritisation, negotiation, or consolidation (20 April workshop; MD 13.1.3). |
| **6.1.3** Pre-defined goal templates (house deposit, car, wedding, emergency fund, credit card payoff) | MVP | M | 6.1.1, 6.1.2 | Reduces blank-page friction; reflects identified personas |
| **6.1.4** Budgie-guided goal setup — AI helps the user define realistic targets | MVP | L | 6.1.1, Epic 4 | Differentiator — the AI provides coaching during setup, not just tracking |
| **6.1.5** Link a goal to a specific account or set of accounts | MVP | M | 6.1.1, Epic 2 | Users need to know which account the goal relates to |
| **6.1.6** Multiple concurrent goals per user | MVP | S | 6.1.1 | Realistic — most users have several goals at once |

### 6.2 Goal Roadmap & Projections

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **6.2.1** Calculate required monthly contribution to hit target | MVP | M | 6.1.1 | Basic maths but needs to handle compound considerations for debt goals |
| **6.2.2** Project goal completion date based on current behaviour | MVP | M | 6.2.1 | "At your current pace, you'll hit this in X months" |
| **6.2.3** Dynamic adjustment — if user has more money, suggest putting more toward goal | MVP | L | 6.2.1, Epic 5 | Founder differentiator (Market Discovery 4.1) — requires spending pattern analysis |
| **6.2.4** Dynamic adjustment — if user has less, show revised timeline and trade-offs | MVP | L | 6.2.3 | The other side of flexibility — honesty rather than false hope |
| **6.2.5** "What if" scenarios — show impact of changing contribution amounts | v1.1 | M | 6.2.1 | Nice-to-have; complements Epic 8 scenario planning |
| **6.2.6** Debt payoff strategy suggestions (avalanche vs snowball) | v2+ | M | 6.1.2 | Deferred from v1.1 per 20 April workshop — debt prioritisation strategies sit in regulated advisory territory (MD 13.1.3). Requires legal/regulatory clearance before inclusion. |

### 6.3 Goal Tracking & Progress

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **6.3.1** Visual progress indicator per goal | MVP | S | 6.1.1 | Standard; motivating |
| **6.3.2** Contribution tracking — automatic or manual | MVP | M | 6.1.5, Epic 2 | Track what's actually going toward the goal |
| **6.3.3** Goal history — see progress over time | MVP | S | 6.3.1 | Shows momentum |
| **6.3.4** Milestone celebrations when user hits 25%, 50%, 75%, 100% | MVP | M | 6.3.1, Epic 9 | Engagement driver; Budgie in-character reaction |
| **6.3.5** Warn when goal is at risk (behind schedule, insufficient contribution) | MVP | M | 6.2.2, Epic 9 | Proactive coaching tied directly to user intent |

### 6.4 Goal Management

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **6.4.1** Edit or update an existing goal | MVP | S | 6.1.1 | Life changes; goals should too |
| **6.4.2** Pause or abandon a goal | MVP | S | 6.1.1 | Users shouldn't feel trapped by goals they've outgrown |
| **6.4.3** Mark a goal as completed and archive | MVP | S | 6.1.1 | Celebrate, then move on |
| **6.4.4** Goal history / past goals view | v1.1 | S | 6.4.3 | Shows lifetime progress |

### 6.5 Goal-Aware Coaching Integration

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **6.5.1** Budgie references active goals in daily check-ins and insights | MVP | M | 6.1.1, Epic 4 | "You saved X toward your house goal this week" — connects budgeting to meaning |
| **6.5.2** Budgie suggests trade-offs across goals when user has constrained cash flow | v1.1 | L | 6.2.3, Epic 4 | "You could hit both goals but later, or prioritise one and hit it sooner" |

### Epic 6 — Assumptions & Open Questions

**Assumptions:**
- Most users will engage with 1–3 concurrent goals, not 10+
- Savings goals and debt *payoff* goals are the two primary goal types for MVP. Other types (investment goals, retirement planning) and debt *advisory* features (prioritisation strategies, consolidation, relief) are deferred as they cross into regulated advisory territory.
- Users are willing to link specific accounts to specific goals (rather than goals being entirely abstract)
- Goal progress doesn't require complex automation (e.g. auto-transfer to savings) — the MVP tracks, it doesn't act

**Open Questions:**
- Does debt goal support include credit cards, loans, mortgages, or all of the above? Each has different data availability from banks.
- How does the system handle shared goals across couples or households? (MVP is probably single-user; shared is v2+ with Epic 10.)
- When a user marks a goal complete, does the app celebrate meaningfully or just tick it off? The character-driven positioning argues for the former.
- Are goals a Premium-tier feature or part of the free experience? (Market Discovery 9.1 — tier boundaries are undefined.)
- ~~For debt goals, do we suggest specific payoff strategies (avalanche, snowball) or stay neutral? The regulatory line here is subtle.~~ — **Resolved (20 April workshop):** stay neutral for MVP — prioritisation strategy advice deferred to v2+ pending regulatory clearance (6.2.6)

---

## Epic 7: Financial Health Score

_A single composite metric representing the user's overall financial wellbeing, used as an onboarding hook and ongoing engagement driver._

The Financial Health Score is one of the founder's strongest product ideas. A single number that captures "how I'm doing financially" is simple, shareable, and emotionally resonant — much more so than a dashboard of disconnected metrics. It plays multiple roles: onboarding hook (value before bank connection, per Epic 1), retention driver (a score to maintain or improve), and potential viral mechanic (shareable milestone).

**Key strategic considerations:**
- The score is a Budgie-defined metric, not an industry standard — this gives freedom to design it well but also means it must be defensible and explainable
- Built from onboarding inputs so it can be calculated before bank connection, then refined as more data arrives (Market Discovery 4.1)
- Components typically include savings rate, spending habits, budgeting discipline, debt management — these are stated in the founder's onboarding vision
- Must be interpretable and actionable — a score with no context becomes a vanity metric; a score with clear drivers becomes a coaching tool
- Sits at the intersection of several epics — draws on Epic 2 (bank data), Epic 5 (budgets), Epic 6 (goals), Epic 4 (AI narration of the score)
- Could become a brand asset in itself — "check your Budgie Score" has marketing potential

### 7.1 Score Definition

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **7.1.1** Define the Financial Health Score methodology (components, weights, formula) | Private Beta | L | Founder input | Foundational decision — influences credibility and defensibility. Founder acknowledged at 20 April workshop that the current methodology is simplistic and needs refinement to be credible and research-based. Direction: weighted aggregation of multiple factors (savings rate, spending, budgeting, debt), benchmarked against local averages, positioned to complement rather than replace credit scores. Phase 1 (questionnaire) and Phase 2 (connected-data) methodology documents delivered by founder 17 April — parked for build phase. |
| **7.1.2** Define score range and bands (e.g. 0–1000 with named bands like "Building", "Healthy", "Thriving") | Private Beta | M | 7.1.1 | Bands give meaning to the number |
| **7.1.3** Document methodology transparently for users who want to understand how it's calculated | MVP | M | 7.1.1, 4.5.1 | Explainability principle — users must be able to see what goes into the score. *Beta: in-app methodology page is polish; beta users see the component breakdown (7.3.2) which gives basic transparency, full methodology doc lands in MVP.* |

### 7.2 Score Calculation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **7.2.1** Calculate initial score from onboarding answers (pre-bank connection) | Private Beta | M | Epic 1, 7.1.1 | Early value moment (Market Discovery 4.1) |
| **7.2.2** Recalculate score using actual bank data once connected | Private Beta | M | Epic 2, 7.1.1 | Refined accuracy once real data is available |
| **7.2.3** Recalculate on a scheduled basis (weekly or monthly) | Private Beta | M | 7.2.2 | Ongoing tracking |
| **7.2.4** Real-time recalculation on significant events (large transaction, budget breach, goal milestone) | v1.1 | M | 7.2.2, Epic 9 | Nice-to-have; scheduled recalculation is MVP-sufficient |

### 7.3 Score Display & Components

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **7.3.1** Prominent display of current score on home screen | Private Beta | S | 7.2.1 | The score should be impossible to miss |
| **7.3.2** Breakdown view — show the components contributing to the score | Private Beta | M | 7.1.1 | Savings rate, spending habits, debt, budget discipline as separate dimensions |
| **7.3.3** Score history view over time (trend graph) | MVP | M | 7.2.3 | Shows progress or decline — motivating either way. *Beta: 4-8 weeks of beta = limited score history; users see current score in beta, history view ships with MVP when there's meaningful trend data.* |
| **7.3.4** Comparison to a benchmark (e.g. "your score vs typical users like you") | v1.1 | L | 7.2.2 | Powerful but needs meaningful benchmark data — may require user base scale |
| **7.3.5** Score-related insights explaining recent changes | MVP | M | 7.2.3, Epic 4 | "Your score went up 15 points because you hit your savings goal". *Beta: push pattern — depends on Epic 4 coaching layer cut from beta.* |

### 7.4 Score-Driven Engagement

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **7.4.1** Budgie provides specific, actionable suggestions to improve the score | MVP | L | 7.3.2, Epic 4 | Turns the score into a coaching tool. *Beta: depends on Epic 4 coaching layer cut from beta.* |
| **7.4.2** Alert on significant score changes (up or down) | MVP | M | 7.2.3, Epic 9 | Attention-grabbing; motivates engagement. *Beta: push pattern deferred.* |
| **7.4.3** Celebrate crossing into a new band ("You're now Thriving!") | MVP | M | 7.1.2, Epic 9 | Emotional engagement moment. *Beta: push pattern deferred.* |
| **7.4.4** Annual or periodic score summary ("Your Budgie Year in Review") | v1.1 | M | 7.2.3 | Spotify Wrapped-style retrospective — highly shareable |

### 7.5 Score Sharing

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **7.5.1** User can share their score or band (not the underlying data) externally | MVP | M | Epic 10 | Moved to MVP per 20 April workshop — score sharing is a planned motivation/engagement mechanic. Viral if privacy is handled correctly — band-only is safer than number. *Beta: viral mechanic doesn't apply to a closed 50-user beta; sharing infrastructure (Epic 10) is also deferring.* |
| **7.5.2** Privacy controls on sharing | MVP | M | 7.5.1, Epic 12 | Moved to MVP alongside 7.5.1 — privacy controls cannot lag the feature. Ensure users never accidentally share sensitive financial details. *Beta: depends on 7.5.1.* |

### Epic 7 — Assumptions & Open Questions

**Assumptions:**
- The Financial Health Score is a single composite number, not a suite of separate scores
- Components are weighted (not all dimensions equal) and the weighting is justifiable
- The score can be calculated without requiring every possible data input — partial calculation with clear communication is acceptable
- The score is a proprietary Budgie metric, not aligned to any existing industry standard (e.g. not a credit score)

**Open Questions:**
- ~~What are the exact components and weights the founder envisages — is this documented or to be defined during this engagement?~~ — **Partially resolved:** Phase 1 (questionnaire) and Phase 2 (connected-data) methodology documents received from founder 17 April. **Still open:** methodology refinement work (founder acknowledged current approach as simplistic at 20 April workshop) — components, weights, and benchmarking approach need definition for build phase.
- Is the score numeric (e.g. 0–1000, 0–100) or band-only (Building / Healthy / Thriving)? Numeric gives precision, bands give meaning.
- Does the score ever decrease meaningfully, or is it designed to only go up? The former is more credible; the latter is more emotionally safe.
- Is the methodology defensible against scrutiny — can we explain to a user (or regulator) why a particular score was produced?
- Is the score in the free tier or a Premium feature? It's likely the single strongest hook, so locking it behind paywall would hurt onboarding.

---

## Epic 8: Ask Anything — Natural Language Queries

_The user-initiated natural language interface for querying their own financial data in plain English._

"Ask anything" is the user-initiated counterpart to Epic 4's proactive engagement. Where Epic 4 is about Budgie coming to the user, this epic is about the user coming to Budgie with a question. It's the feature most directly comparable to ChatGPT-style interaction, but with a critical difference — the answers must be grounded in the user's actual data, not generic advice.

**Key strategic considerations:**
- The quality bar is very high — bad answers about someone's money erode trust fast, and there is no second chance once trust is broken (Market Discovery 4.2)
- Scenario planning ("what if I took a pay cut?") is conceptually part of this epic but requires significantly more capability than simple data queries
- Explainability is essential — every answer must show its working (Market Discovery 8.2)
- The feature needs clear boundaries — Budgie must refuse or redirect questions outside its scope (investment recommendations, specific product advice)
- Ask Anything could become a Premium tier feature or a rate-limited free feature (Market Discovery 9.1)
- The natural language interaction is LLM-powered and therefore LLM-cost-sensitive — usage patterns directly affect unit economics

### 8.1 Query Interface

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **8.1.1** Text input for natural language questions | Private Beta | M | Epic 4 | Core UX element |
| **8.1.2** Voice input option | v1.1 | M | 8.1.1 | Nice-to-have; hands-free coaching use case |
| **8.1.3** Suggested question prompts to guide new users | MVP | M | 8.1.1 | Prevents blank-page problem; teaches users what Budgie can do. *Beta: hardcoded welcome message with 3-4 example questions baked into the chat UI is enough; dynamic suggestion engine is MVP.* |
| **8.1.4** Chat history management — multiple concurrent conversations, each independently accessible and continuable | MVP | M | 8.1.1 | Workshop 21 April: explicitly called out as a usability advantage over typical chatbots. Users can maintain separate threads (e.g. "housing budget" conversation vs "daily spending" conversation) without them bleeding into each other. Size upgraded from S to M to reflect thread-management scope. *Beta: single thread for beta tests core chat; multi-conversation thread management lands in MVP.* |
| **8.1.5** Seed new chats with a daily or weekly summary to avoid the blank-start problem | MVP | M | 8.1.1, 4.4.1, 4.4.6 | Workshop 21 April: when a user opens a new chat, Budgie starts with a contextual summary (today's brief or this week's review) rather than an empty page. Increases engagement and surfaces relevant coaching moments. *Beta: depends on Epic 4 daily/weekly check-in framework cut from beta.* |
| **8.1.6** Chat branching and categorisation — organise and split chat threads by topic | v1.1 | L | 8.1.4 | Workshop 21 April: flagged as a future feature beyond MVP multi-thread basics. |

### 8.2 Data-Grounded Question Answering

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **8.2.1** Classify user question type (spending query, balance query, trend query, affordability, etc.) | Private Beta | L | 4.2.1 | Routing decision — different question types need different handling |
| **8.2.2** Retrieve and assemble the relevant data from user's accounts for the query | Private Beta | L | 4.2.3, Epic 2, Epic 5 | Retrieval layer — this is the hardest part |
| **8.2.3** Generate natural language answer grounded in actual data | Private Beta | L | 8.2.2, 4.2.2 | LLM-powered but constrained to retrieved facts |
| **8.2.4** Show supporting data alongside the answer (receipts, charts, account references) | Private Beta | M | 8.2.3, 4.5.1 | Explainability in practice — user sees the evidence |
| **8.2.5** Handle ambiguous questions with clarifying follow-ups | Private Beta | M | 8.2.1 | "Do you mean last month or this month?" |
| **8.2.6** Out-of-scope question detection and graceful refusal | Private Beta | M | 4.2.4, Epic 13 | Must refuse investment advice, market predictions, etc. |

### 8.3 Common Question Categories

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **8.3.1** Spending queries ("how much did I spend on food last month?") | Private Beta | M | Epic 5 | High-frequency question type |
| **8.3.2** Balance and net worth queries ("what's my total across all accounts?") | Private Beta | M | Epic 2 | Core aggregation question |
| **8.3.3** Trend queries ("is my spending going up?") | Private Beta | M | Epic 5 | Requires comparison logic. Beta users have 6 months historic from Finverse — trends are answerable. |
| **8.3.4** Affordability queries ("can I afford a $500 dinner this weekend?") | MVP | L | Epic 5, Epic 6 | Requires understanding current balance, upcoming bills, budgets, goals. *Beta: depends on Epic 5 (partly in beta) + Epic 6 (deferred entirely) — affordability would only partially work in beta.* |
| **8.3.5** Goal-related queries ("how am I doing on my house goal?") | MVP | M | Epic 6 | Reinforces goal engagement. *Beta: depends on Epic 6 which defers entirely.* |
| **8.3.6** Subscription queries ("what am I paying for monthly?") | MVP | M | 5.4 | Uses subscription detection. *Beta: depends on Epic 5.4 (subscription detection) which defers.* |

### 8.4 Scenario Planning

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **8.4.1** Simple scenario queries ("what if I saved $200 more a month?") | v1.1 | L | 8.2.3, Epic 6 | Requires projection logic beyond retrieval |
| **8.4.2** Complex scenario queries ("what if I took a pay cut of 20%?") | v1.1 | XL | 8.4.1, Epic 5 | Requires holistic financial modelling — v2+ territory for real depth |
| **8.4.3** Scenario comparison (side-by-side "what if" outcomes) | v2+ | L | 8.4.1 | Power user feature |
| **8.4.4** Scenario persistence (save and revisit scenarios) | v2+ | M | 8.4.1 | Transforms scenario planning from one-off to iterative |

### 8.5 Quality & Safety Controls

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **8.5.1** Uncertainty flagging — Budgie states when it doesn't have enough data | Private Beta | M | 8.2.3 | Honesty over false confidence |
| **8.5.2** "I don't know" handling — graceful response when an answer isn't available | Private Beta | S | 8.5.1 | Better than a hallucinated answer |
| **8.5.3** User feedback on answer quality (thumbs up/down) | Private Beta | S | 8.2.3 | Quality monitoring and improvement loop. *Beta: critical instrument — without it the team can't learn from beta feedback systematically.* |
| **8.5.4** Escalation or redirection for questions requiring human judgement (e.g. financial advisor) | v1.1 | M | 8.2.6 | "This sounds like you'd benefit from speaking to a licensed advisor" |

### 8.6 Usage & Cost Controls

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **8.6.1** Rate limiting per user (free vs paid tiers) | Private Beta | M | 4.2.5, Epic 11 | Commercial necessity given LLM costs. *Beta: simple per-user daily message cap; sophisticated tier-based limits land in MVP with the pricing tiers.* |
| **8.6.2** Monitoring of per-user and aggregate LLM spend | Private Beta | M | 4.2.5, Epic 14 | Tracks unit economics |
| **8.6.3** Caching of common queries to reduce cost | v1.1 | L | 8.2.3 | Optimisation; may not be MVP-critical depending on usage patterns |

### Epic 8 — Assumptions & Open Questions

**Assumptions:**
- Users will ask natural language questions primarily about their own data, not general financial questions (though some will, and these need handling)
- LLM providers can be configured to refuse out-of-scope questions reliably enough for MVP — edge cases will exist but shouldn't dominate
- The quality of retrieved data (from Epic 2, 5, 6) is high enough to support accurate answers — this is an upstream dependency
- Users understand that Budgie is not a financial advisor and will not be upset by scoped refusals

**Open Questions:**
- Is Ask Anything a Premium-only feature, rate-limited for free users, or fully available to all?
- What's the acceptable latency for an answer? Users expect chat interactions to feel responsive.
- How does Ask Anything relate to Epic 4.3.3 (user-initiated AI from any screen)? Are they the same feature or distinct?
- For scenario planning, how deep does v1 go — simple arithmetic projections, or genuinely modelled scenarios with assumptions the user can see?
- What happens when Budgie genuinely doesn't know or gets something wrong — is there a human escalation path or feedback loop?

---

## Epic 9: Notifications & Proactive Engagement

_System- and AI-initiated outbound engagement: daily check-ins, alerts, reminders, insights. The operational mechanism that makes Budgie proactive rather than reactive._

This epic is the plumbing that makes the "proactive AI" positioning real. It's not glamorous, but without it Budgie is just another dashboard that waits for the user to visit. Every other epic's proactive features (budget warnings, goal milestones, score alerts, daily check-ins) land here.

**Key strategic considerations:**
- The line between "proactive coaching" and "annoying notification spam" is thin — getting this wrong causes uninstalls (Market Discovery 4.2)
- Different notification types serve different purposes — a budget warning is urgent, a weekly summary is informational, a daily check-in is habitual. They need different tone, timing, and delivery channels.
- All notifications must be written in Budgie's voice (Epic 4.7.3) — even system messages
- User control over notifications is essential — not just a binary on/off but granular preferences by type
- Delivery infrastructure (push, email, in-app) is a backend decision with commercial implications — some push services cost money at scale
- Notifications are a compliance surface — they represent communications to users and must meet the same standards as in-app content (Market Discovery 13.1.4)
- **Beta scope:** Epic 9 defers almost entirely to MVP — the notification infrastructure exists to power the proactive coaching layer (Epic 4.4, 5.3, 6.3, 7.4), all of which is cut from beta. Beta uses transactional email only (9.1.4) for three operational notification types (welcome, re-authentication required, connection success/failure). Team has direct contact with beta users for everything else.

### 9.1 Notification Infrastructure

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **9.1.1** Select and integrate a push notification service (e.g. Firebase Cloud Messaging, OneSignal, Expo) | MVP | M | — | Foundational infrastructure. *Beta: push notification infrastructure deferred — beta uses transactional email only for operational comms; team has direct contact with beta users for time-sensitive matters.* |
| **9.1.2** Push notification delivery on iOS and Android | MVP | M | 9.1.1 | Platform-specific configuration |
| **9.1.3** In-app notification centre / inbox | MVP | M | 9.1.1 | Users miss push notifications; inbox provides a catch-up surface. *Beta: with no proactive notifications firing in beta, no inbox needed.* |
| **9.1.4** Email notification delivery (transactional) | Private Beta | M | 9.1.1, Epic 12 | Backup channel and for users who disable push. The operational comms channel for beta — required for welcome, bank reconnect, connection events. |
| **9.1.5** Notification preference centre (granular on/off by type and channel) | MVP | L | 9.1.1, 9.1.2, 9.1.3, 9.1.4 | Essential — users will leave otherwise. *Beta: only one notification channel (email) and minimal types — no preferences to manage beyond opt-out.* |

### 9.2 Notification Types

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **9.2.1** Daily check-in push from Budgie | MVP | M | Epic 4.4.1 | The habit-forming notification |
| **9.2.2** Budget warning (approaching or exceeding budget) | MVP | M | Epic 5.3.3 | Founder differentiator — warn before, not after |
| **9.2.3** Goal milestone reached | MVP | M | Epic 6.3.4 | Celebration moment |
| **9.2.4** Goal at risk (behind schedule) | MVP | M | Epic 6.3.5 | Proactive coaching |
| **9.2.5** Significant score change | MVP | M | Epic 7.4.2 | Score as engagement anchor |
| **9.2.6** Unusual or anomalous transaction | MVP | M | Epic 5.2.4 | Trust-building — Budgie is watching out for them |
| **9.2.7** Upcoming bill or subscription reminder | MVP | M | Epic 5.4 | Reduces "I forgot to budget for that" moments |
| **9.2.8** Weekly summary digest | MVP | M | Epic 5.2 | Slower-paced overview for passive users |
| **9.2.9** Re-authentication required (bank connection expired) | Private Beta | M | Epic 2.3.3 | Critical operational notification — unfixed means data stops flowing. Beta-essential given 2FA-per-refresh on Finverse — without an email prompt, users could go days with stale data thinking the app is broken. |
| **9.2.10** Account connection success/failure | Private Beta | S | Epic 2.1.5 | Transparency during onboarding and reconnection. Operational — required for onboarding (Epic 1) which is in beta. |

### 9.3 Timing & Cadence

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **9.3.1** User-configurable time-of-day for daily check-in | MVP | S | 9.2.1 | Respect time zones and user preference — a morning person is different from an evening person |
| **9.3.2** Notification throttling — cap the number of notifications per day (target: 2–3 push per day) | MVP | M | 9.1.1 | Prevents cascade of alerts on a busy day. Workshop 21 April: target confirmed at 2–3 push/day to calibrate engagement against uninstall risk. |
| **9.3.3** Intelligent batching — combine related low-priority notifications | v1.1 | L | 9.3.2 | Reduces spam feel while preserving information |
| **9.3.4** Quiet hours — no notifications during user-defined windows | MVP | S | 9.1.1 | Basic respect for sleep |

### 9.4 Content & Voice

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **9.4.1** All notifications authored in Budgie's voice | MVP | M | Epic 4.7.3 | Part of cross-surface personality consistency. *Beta: small set of templated emails written with basic character during build; full notification-voice enforcement system lands in MVP.* |
| **9.4.2** Dynamic notification content — avoid repetition across similar notifications | MVP | L | Epic 4.4.2 | Daily check-ins and weekly digests can become stale fast |
| **9.4.3** Personalised notification content based on user data | MVP | L | Epic 4.2.3 | "You spent $X on coffee this week" feels different from "Weekly summary" |
| **9.4.4** Rich notification content (with images, charts, or CTAs) | v1.1 | L | 9.1.2 | Platform-specific; increases engagement but adds complexity |

### 9.5 Delivery Reliability & Analytics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **9.5.1** Delivery tracking — did the notification reach the user? | MVP | M | 9.1.1, Epic 14 | Standard push service capability |
| **9.5.2** Engagement tracking — did the user tap, dismiss, or ignore? | MVP | M | 9.5.1, Epic 14 | Feedback loop for content optimisation |
| **9.5.3** Unsubscribe / preference-change signals | MVP | M | 9.1.5, Epic 14 | Early warning of notification fatigue |

### Epic 9 — Assumptions & Open Questions

**Assumptions:**
- Push notifications are the primary proactive channel, with email and in-app inbox as supplements
- Users will grant push notification permissions at a reasonable rate (30–60% typical for finance apps)
- A granular preference centre is preferable to a blunt on/off switch — more users will opt in if they can tune
- SMS is not in scope for MVP — expensive, regulated, and unnecessary given push reach

**Open Questions:**
- What's the default notification posture for a new user — opt-in to all, opt-in to essentials only, or opt-in to none?
- How does the product handle users who deny push permissions entirely — is email a realistic substitute or is this a significantly degraded experience?
- ~~Is there a hard daily cap on notifications, and if so, what is it?~~ — **Resolved (21 April workshop):** target is 2–3 push notifications per day, with user preference controls to reduce further (Section 9.3.2).
- For the daily check-in, what time of day is recommended by default? Evidence suggests morning is better for engagement, but this varies by region.
- Does the compliance review process for social media posts (Epic 4.7.2) extend to push notification copy, or are notifications considered distinct?

---

## Epic 10: Social Features

_User-to-user interaction including milestone sharing. Largely deferred from MVP but included for architectural visibility._

The founder described social sharing as part of the product vision — users sharing milestones, successes, and financial moments with each other. This is a legitimate retention and viral mechanic, but it introduces significant complexity (user accounts with public identity, content moderation, privacy), and most of it is unlikely to be MVP.

The founder has confirmed that outward sharing (Section 10.1) is in MVP scope as a marketing/traction mechanic. The full in-app social graph (friends, feeds, reactions) remains v2+.

**Key strategic considerations:**
- Social features are mentioned in the founder's vision (Market Discovery 4.1) but are not required for the core value proposition
- Deferring social is a clear MVP scope-reduction opportunity — it removes a large category of complexity without killing the product
- Architectural foundations (user identity beyond email, privacy controls, content storage) still need consideration in MVP so v1.1 doesn't require a rewrite
- Financial social networks have well-documented failure modes — oversharing, social comparison, financial voyeurism. Design choices here matter.
- Share mechanics aimed outward (WhatsApp, Instagram stories) are lower-risk than in-app social graphs — they generate organic acquisition without building a community product
- Compliance implications — user-generated content in a financial app creates moderation and regulatory responsibilities
- **Beta scope:** External sharing (10.1) defers to MVP — beta is closed-user by design, viral mechanics are not relevant. The two architectural foundations (10.5) come forward into beta because the identity and privacy data models are better future-proofed from the start than retrofitted later. v2+ items unchanged.

### 10.1 Outward Sharing (External)

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **10.1.1** Shareable milestone card — user shares a goal hit or score improvement to external platforms (WhatsApp, Instagram, X) | MVP | M | Epic 6.3.4, Epic 7.4.3 | Founder confirmed as MVP — intended as a marketing/traction mechanic. *Beta: external sharing not relevant for closed 50-user beta.* |
| **10.1.2** Pre-designed share card templates featuring Budgie's character | MVP | M | 10.1.1, Epic 4.1.4 | Branded sharing drives brand recognition |
| **10.1.3** Privacy controls on shared content — nothing sensitive by default | MVP | M | 10.1.1, Epic 12 | User shares a band or a % milestone, never raw financial numbers |
| **10.1.4** Referral tracking on shared content | MVP | M | 10.1.1, Epic 14 | If sharing drives installs, measure it |

### 10.2 Internal Social (In-App Community)

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **10.2.1** User profile — display name, avatar, optional bio | v2+ | M | Epic 12 | Needed before any in-app social |
| **10.2.2** Friend/connection system — users can connect with other users | v2+ | L | 10.2.1 | Classic social graph — significant complexity |
| **10.2.3** In-app milestone feed — see friends' achievements | v2+ | L | 10.2.2 | Core community feature if pursued |
| **10.2.4** Reactions and comments on shared milestones | v2+ | L | 10.2.3 | Content moderation requirements start here |
| **10.2.5** Privacy controls on in-app social (public, friends only, off) | v2+ | M | 10.2.1 | Essential if any in-app social is built |

### 10.3 Group Features

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **10.3.1** Challenge groups (e.g. "30-day no-spend challenge") | v2+ | XL | 10.2.2 | Potentially powerful retention mechanic |
| **10.3.2** Shared goals across multiple users (e.g. couples, households) | v2+ | XL | Epic 6, 10.2.2 | Referenced as deferred in Epic 6.3.7 |
| **10.3.3** Leaderboards (optional, opt-in) | v2+ | L | 10.2.2 | Gamification that some users love and others hate |

### 10.4 Content Moderation & Safety

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **10.4.1** Reporting mechanism for inappropriate user content | v2+ | M | 10.2.4 | Required the moment user-generated content exists |
| **10.4.2** Automated content moderation for user-posted text | v2+ | L | 10.2.4 | Manual moderation doesn't scale |
| **10.4.3** Block / mute other users | v2+ | M | 10.2.2 | Standard social safety feature |

### 10.5 Architectural Foundations (MVP)

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **10.5.1** User identity model designed to support future display name and avatar | Private Beta | S | Epic 12 | Avoid having to rebuild identity when social arrives. *Beta: architectural one-time decision — embedding future-social fields (display name, avatar) in the identity model now has minimal additional cost vs retrofitting later.* |
| **10.5.2** Privacy model flexible enough to accommodate "share-able" vs "personal-only" data classification | Private Beta | M | Epic 12 | Data architecture decision with long-lived implications. *Beta: architectural one-time decision — data classification model is better designed once than retrofitted.* |

### Epic 10 — Assumptions & Open Questions

**Assumptions:**
- Social features are not in MVP scope — the core value proposition does not require them
- External sharing (v1.1) is preferable to in-app social (v2+) from a complexity and risk perspective
- Users will not expect a social layer in v1 — competitors in the budgeting space (Monarch, YNAB) also lack meaningful in-app social
- Any user-generated content introduces moderation and legal obligations that are not worth the complexity at MVP stage

**Open Questions:**
- Does the founder see social as a v1.1 priority (within 3 months post-launch) or a genuinely longer-term feature?
- Is external sharing acceptable without in-app social, or does the founder see them as a package?
- What's the founder's view on financial comparison — some users find it motivating, others find it damaging. This is a design philosophy decision.
- Are any share mechanics specifically valuable for the Budgie brand (e.g. character-driven share cards that spread the personality)?
- If in-app community is pursued eventually, how is user identity verified — are users real people or can they be pseudonymous?

---

## Epic 11: Pricing & Subscription

_Paid tier management, payment integration, tier enforcement, free trial handling._

This epic is the commercial machinery that turns users into revenue. It's often underestimated because it feels like "just payments", but getting it right affects conversion, unit economics, and user trust. The founder has sketched a three-tier freemium model but the boundaries between tiers, trial mechanics, and payment flows are undefined.

**Key strategic considerations:**
- The tier boundaries (what's free, what's basic, what's premium) are a critical product decision that affects both conversion and user perception (Market Discovery 9.1)
- App store commissions (15–30% to Apple/Google) are unavoidable for subscription billing — this directly impacts unit economics (Market Discovery 13.4.3)
- Free trial mechanics shape conversion patterns — length, what's available during trial, whether it requires payment details upfront
- Subscription management complexity (cancellation, refunds, plan changes, dunning) is easy to underestimate
- Regional pricing may matter — what's $15/month in Singapore may need different positioning in Hong Kong, EU, US
- In-app purchase compliance with Apple's and Google's rules is strict for digital goods and services — no workarounds
- **Beta scope:** Epic 11 defers entirely to MVP — beta users get free access to the beta scope without any commercial machinery (no tiers, no payments, no trials, no upgrade prompts, no entitlement checks). Tier definition (11.1.1) is founder-led design work that should ideally be settled before MVP build begins, but doesn't require beta-phase engineering. The full commercial layer ships at MVP.

### 11.1 Tier Definition & Entitlements

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **11.1.1** Define features and usage limits per tier (Free / Premium / Pro) | MVP | L | Founder input | Tier names confirmed at 21 April workshop: **Free / Premium / Pro** (previously Free / Basic / Premium). First tier decision: **Free tier includes unlimited account connections** — aspirational and may be constrained by aggregator per-account costs (MD 9.4). Paid tier feature allocation and Premium vs Pro differentiation still TBC. |
| **11.1.2** Document tier boundaries in a single source of truth | MVP | S | 11.1.1 | Must be referenced by every feature that has tier-dependent behaviour |
| **11.1.3** Entitlement system — runtime check of what the current user is allowed to do | MVP | L | 11.1.1 | Foundational; every feature checks this |
| **11.1.4** Graceful degradation when a user hits a tier limit (upgrade prompt, not a dead end) | MVP | M | 11.1.3 | Conversion moment — must feel helpful, not punitive |

### 11.2 Payment & Subscription Integration

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **11.2.1** Integrate Apple In-App Purchase for iOS | MVP | L | — | Required by Apple for subscriptions; no alternative |
| **11.2.2** Integrate Google Play Billing for Android | MVP | L | — | Required by Google for subscriptions |
| **11.2.3** Use a subscription management platform (e.g. RevenueCat) to unify iOS and Android subscription state | MVP | M | 11.2.1, 11.2.2 | Strongly recommended — building subscription management in-house is a tax with no reward |
| **11.2.4** Server-side subscription validation | MVP | M | 11.2.3 | Prevents client-side spoofing; standard practice |

### 11.3 Free Trial

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **11.3.1** Time-bounded free trial (e.g. 7 or 14 days of Premium features) | MVP | M | 11.1.3, 11.2.3 | Founder described a trial model (Market Discovery 9.1) |
| **11.3.2** Trial expiry handling — auto-downgrade to Free tier with notification | MVP | M | 11.3.1, Epic 9 | Workshop 21 April: Free is the continuing tier for non-converters (not time-bound). Communication is critical — surprise cancellations cause churn. |
| **11.3.3** Trial recovery flow — user can upgrade before trial ends | MVP | M | 11.3.1 | Conversion optimisation |

### 11.4 Subscription Lifecycle Management

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **11.4.1** Upgrade flow — user moves from Free to Premium, or Premium to Pro | MVP | M | 11.2.3 | Must be friction-free at the moment of intent |
| **11.4.2** Downgrade flow — user steps down a tier | MVP | M | 11.2.3 | Less common but must work; handle data/feature access gracefully |
| **11.4.3** Cancellation flow — standard cancellation with retention offer | MVP | M | 11.2.3 | Both platforms require easy cancellation; retention offers allowed |
| **11.4.4** Payment failure handling (dunning) | MVP | M | 11.2.3 | Subscriptions fail — cards expire, payments decline. Needs thoughtful user comms. |
| **11.4.5** Subscription status visible to user in-app | MVP | S | 11.2.3 | Trust and transparency |

### 11.5 Pricing Strategy & Display

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **11.5.1** Pricing page / paywall screen | MVP | M | 11.1.1 | Where the upgrade conversion happens — high design investment |
| **11.5.2** Support for regional pricing | v1.1 | M | 11.2.3 | Useful when expanding to HK / EU / US; not strictly MVP |
| **11.5.3** Support for annual plans with discount | MVP | M | 11.2.3 | Improves LTV and reduces churn — common pattern |
| **11.5.4** Promotional pricing / coupon codes | v1.1 | L | 11.2.3 | Useful for marketing campaigns post-launch |

### 11.6 Revenue Tracking & Analytics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **11.6.1** Revenue dashboards — MRR, ARR, conversion, churn | MVP | M | 11.2.3, Epic 14 | Essential for founder and investors |
| **11.6.2** Cohort analysis — retention and revenue by cohort | MVP | M | 11.6.1, Epic 14 | Required for meaningful unit economics discussion |
| **11.6.3** Integration with RevenueCat dashboards or equivalent | MVP | S | 11.2.3 | Near-free if using RevenueCat |

### Epic 11 — Assumptions & Open Questions

**Assumptions:**
- Apple In-App Purchase and Google Play Billing are the primary payment mechanisms for MVP — no external payment processor for subscriptions (Apple and Google don't generally allow this for digital services)
- A third-party subscription management platform (RevenueCat or similar) will be used — not a build
- Free trial is part of the MVP model — founder's stated approach
- Single currency (SGD or USD) at MVP — multi-currency is v1.1

**Open Questions:**
- ~~What are the specific features and limits per tier?~~ — **Partially resolved (21 April workshop):** tier names confirmed Free / Premium / Pro (11.1.1); free trial model confirmed (7 or 14 days Premium, downgrade to Free). **Still open:** feature-by-feature allocation across tiers, Premium vs Pro differentiation. (Market Discovery Open Question #10 — partially resolved there as well)
- What's the trial length — 7 days, 14 days, 30 days? Shorter = more pressure; longer = deeper conversion
- Does the trial require payment details upfront (higher conversion, lower trial starts) or not (lower conversion, higher trial starts)?
- What's the annual plan discount if offered — 20%, 30%, two months free?
- Are there any features intentionally *outside* the paid tiers — e.g. the Financial Health Score might be always free to drive the hook, even if other features require payment (see Epic 7 open question)
- Does the founder have revenue targets per month/quarter post-launch that the tier structure needs to support?

---

## Epic 12: Data & Privacy Infrastructure

_The underlying data architecture, storage, consent management, and user data controls (access, export, deletion) that support both product functionality and regulatory compliance._

This epic is the invisible foundation that the rest of the product stands on. It's the bridge between "we have features" and "we can legally launch and operate those features". Most of this work is unglamorous but non-negotiable — a financial app handling sensitive user data across jurisdictions needs a defensible data architecture from day one, not bolted on later.

**Key strategic considerations:**
- Decisions made here have long-lived implications — migrating data architecture post-launch is painful and risky
- Data residency, storage location, and cross-border transfer are all live regulatory questions (Market Discovery 13.2.3)
- LLM providers handling user financial data raise specific questions about data retention, training use, and cross-border transfer (Market Discovery 13.2.4)
- User rights under PDPA (Singapore) and PDPO (Hong Kong) — access, correction, deletion, consent — must be supported in-product, not just in a privacy policy (Market Discovery 13.2.1, 13.2.2)
- Data monetisation (ad targeting, affiliate) requires separate consent flows and cannot be bundled into core product consent (Market Discovery 9.3, 13.2.6)
- Security posture (encryption, access controls, incident response) is a trust prerequisite for a financial app — users and regulators both expect it
- This epic enables commercial flexibility in Epic 9 (Business Model) — data monetisation only works if the consent and architecture support it

### 12.1 Identity & Account Infrastructure

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **12.1.1** User account creation and authentication | Private Beta | M | — | Google and Apple social login only for MVP — no username/password or phone number. Reduces complexity, ties to verified identities for potential KYC, eliminates password management |
| **12.1.2** Secure token/session storage for social login credentials | Private Beta | M | 12.1.1 | Standard but non-negotiable |
| **12.1.3** Multi-factor authentication (MFA) | MVP | M | 12.1.1 | Table stakes for financial apps — users expect it and regulators favour it. *Beta: relies on Google/Apple IDP-level MFA at social login (already enforced by user's IDP); app-level MFA enforcement layer lands in MVP.* |
| **12.1.4** Session management and token refresh | Private Beta | M | 12.1.1 | Balance security (short sessions) and UX (not constantly re-authenticating) |
| **12.1.5** Account recovery flows (social login re-authentication) | Private Beta | S | 12.1.1 | Simplified by social login — no password reset needed |
| **12.1.6** Device management — user can see and revoke active devices | v1.1 | M | 12.1.4 | Good security hygiene feature; not MVP-blocking |

### 12.2 Data Storage Architecture

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **12.2.1** Decide data residency strategy — where user data is stored physically | Private Beta | M | Legal review | Market Discovery 13.2.3 — must be decided before any build |
| **12.2.2** Encryption at rest for all user data | Private Beta | M | 12.2.1 | Industry standard; regulatory expectation |
| **12.2.3** Encryption in transit (TLS everywhere) | Private Beta | S | — | Standard for any modern app |
| **12.2.4** Separation of sensitive data (financial details, PII) from less-sensitive operational data | Private Beta | L | 12.2.1 | Architectural decision; enables finer-grained access control and audit |
| **12.2.5** Backup and disaster recovery | Private Beta | M | 12.2.1 | Financial data loss is catastrophic |
| **12.2.6** Key management for encryption keys | Private Beta | M | 12.2.2 | Where keys live matters — typically a managed service (AWS KMS, GCP KMS) |

### 12.3 Consent Management

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **12.3.1** Granular consent flows — separate consents for core product, AI processing, and marketing. Data monetisation consent deferred to v1.1 but the consent architecture should be designed to support it without rework | Private Beta | L | Legal review | Market Discovery 13.2.1 — data monetisation confirmed not MVP (Market Discovery 9.3) |
| **12.3.2** Consent state storage and history | Private Beta | M | 12.3.1 | Auditable record of what the user agreed to and when |
| **12.3.3** Consent withdrawal mechanism — user can revoke any specific consent | Private Beta | M | 12.3.1 | Required by PDPA/PDPO; not just an "unsubscribe" button |
| **12.3.4** Downstream enforcement — systems respect current consent state in real time | Private Beta | L | 12.3.3 | A user who revokes ad-targeting consent must immediately stop being targeted |
| **12.3.5** Consent prompts at relevant moments (in-app context, not just onboarding) | Private Beta | M | 12.3.1 | Contextual consent for AI processing, account connections, etc. |

### 12.4 User Data Rights

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **12.4.1** User can view all personal data Budgie holds | Private Beta | M | 12.2.4 | PDPA/PDPO access right |
| **12.4.2** User can export their data in a portable format (JSON/CSV) | MVP | M | 12.4.1 | Data portability; good practice even where not mandated. *Beta: self-service export is polish; beta users can request data via support team; full self-service feature lands in MVP.* |
| **12.4.3** User can correct their personal data | Private Beta | M | 12.4.1 | Required by PDPA/PDPO |
| **12.4.4** User can delete their account and all associated data | Private Beta | L | 12.2.4, 12.5 | Market Discovery 13.2.5 — "all data" must really mean all data |
| **12.4.5** Verifiable deletion including third-party data (LLM providers, data processors) | Private Beta | L | 12.4.4 | Harder than it sounds — must chase deletion downstream |

### 12.5 Third-Party Data Handling

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **12.5.1** Document all data processors (Finverse, LLM providers, payment processors, analytics) | Private Beta | M | — | Required for transparency and privacy policy |
| **12.5.2** Data processing agreements (DPAs) with all third-party processors | Private Beta | M | 12.5.1, Legal review | Contractual compliance |
| **12.5.3** Verify LLM provider data retention and training policies meet our consent model | Private Beta | M | 12.5.1, Epic 4.2.1 | Market Discovery 13.2.4 — a key unresolved question |
| **12.5.4** PII scrubbing of data sent to AI processing — remove names, identifiers, and PII metadata before the LLM call | Private Beta | L | 12.5.3, Epic 4.2.3 | Workshop 21 April: confirmed as an MVP requirement (MD 13.2.4). Reduces exposure even if provider policies change. |
| **12.5.5** Optional further obfuscation of specific financial figures before AI processing (convert amounts to ratios or bands) | v1.1 | M | 12.5.4 | Workshop 21 April flagged as under consideration — reduces leak risk further but at cost of AI response precision. Not MVP; re-evaluate in v1.1 with real user data. |

### 12.6 Security Operations

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **12.6.1** Audit logging of sensitive operations (logins, data access, data changes, deletions) | Private Beta | M | — | Required for incident investigation and regulatory audit |
| **12.6.2** Access control model for internal team (least privilege, role-based) | Private Beta | M | — | Day-one discipline; much harder to retrofit |
| **12.6.3** Incident response plan and runbooks | Private Beta | M | — | Required by PDPA/PDPO for breach notification. *Beta: basic plan only (one-pager: what to do, who to call); full runbooks land in MVP.* |
| **12.6.4** Security monitoring and alerting | MVP | M | 12.6.1 | Detect unusual access or anomalies. *Beta: basic logging with manual team review is feasible for 50 known users; sophisticated security monitoring infrastructure lands in MVP.* |
| **12.6.5** Penetration testing pre-launch | MVP | M | Build complete | Not cheap; outsourced to security firm. *Beta: launches with security best practices applied during build but no formal pentest; pentest before public MVP launch.* |
| **12.6.6** Ongoing security review cadence | v1.1 | S | 12.6.5 | Annual or per-release |

### Epic 12 — Assumptions & Open Questions

**Assumptions:**
- Data will be stored in Singapore or a jurisdiction acceptable to MAS and PDPA
- LLM processing will use a provider with a business tier that excludes training on customer data (e.g. Anthropic, OpenAI business tiers)
- User data deletion within 30 days of request is acceptable (gives time for downstream propagation)
- A managed cloud provider (AWS, GCP, Azure) provides the underlying infrastructure — not self-hosted

**Open Questions:**
- Where will data be physically stored? (Market Discovery Open Question #17 — currently unresolved)
- Which LLM provider will be used and what are their data retention policies? (Market Discovery Open Question #18)
- How will data be anonymised or pseudonymised before AI processing? (Market Discovery Open Question #19)
- What's the breach notification timeline the team commits to internally — beyond the regulatory minimum?
- Is the data architecture designed to support future EU expansion (GDPR) without major rework? This is a forward-looking decision but has MVP implications.
- Is there a named Data Protection Officer (or equivalent responsibility) — PDPA requires this for most entities

---

## Epic 13: Compliance & Regulatory

_Product-level features and processes required for regulatory compliance, including disclaimers, terms of service integration, content approval workflows, and audit logging._

Where Epic 12 is the data and privacy infrastructure, this epic is the behavioural and operational compliance layer — the things that keep Budgie on the right side of financial regulators, advertising rules, and liability expectations. Most of these items are small individually but collectively define whether the product can launch and operate in its target markets.

**Key strategic considerations:**
- The "Financial Coach" positioning only holds if the product behaves like a coach, not an advisor — this requires active design choices, not just labelling (Market Discovery 13.1.3)
- Regulatory engagement with MAS (Singapore) is strongly recommended and may unlock the MAS Sandbox pathway (Market Discovery 13.1.1)
- A corporate entity is a prerequisite for every compliance activity — if not yet established, this blocks a lot of downstream work (Market Discovery 13.5)
- Social media compliance applies the same rules as in-app content — Budgie posting on X is subject to MAS advertising rules (Market Discovery 13.1.4)
- Explainability and audit trails overlap with Epic 4.5.4 and Epic 12.6.1 — compliance is often about being able to reconstruct what happened and why
- The content approval process for Budgie's voice across surfaces (Epic 4.7.2) lives here operationally
- Liability mitigation through disclaimers and guardrails is necessary but not sufficient — the underlying product behaviour matters more than the fine print (Market Discovery 13.3)
- The AI is fully autonomous at MVP with no human-in-the-loop review (20 April workshop) — compliance mitigation therefore depends entirely on pre-built guardrails, disclaimers, audit logs, and insurance. This concentrates risk in those layers and raises the bar on each (Market Discovery 13.3.1)

### 13.1 Corporate Entity & Foundational Setup

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.1.1** Confirm or establish legal entity for Budgie | Private Beta | M | Founder / Legal | Blocking prerequisite (Market Discovery 13.5) |
| **13.1.2** Register entity for applicable business activities in chosen jurisdiction | Private Beta | M | 13.1.1 | Depends on jurisdiction choice |
| **13.1.3** Obtain professional indemnity / product liability insurance | Private Beta | M | 13.1.1 | Protects against AI guidance disputes (Market Discovery 13.3) |
| **13.1.4** Appoint a Data Protection Officer or equivalent | Private Beta | S | 13.1.1 | PDPA requirement for most entities |

### 13.2 Regulatory Engagement

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.2.1** Legal review of MVP feature set against MAS Financial Advisers Act | Private Beta | M | Legal counsel | Critical — determines what features are safe to launch |
| **13.2.2** Informal or formal engagement with MAS | MVP | M | 13.2.1 | Market Discovery 13.1.1 recommends this. *Beta: depends on outcome of 13.2.1 — legal opinion will indicate whether direct MAS engagement is required pre-beta or can wait for public launch.* |
| **13.2.3** Evaluate MAS Sandbox as a launch vehicle | v1.1 | M | 13.2.1 | Provides controlled environment for novel fintech products |
| **13.2.4** Pre-launch legal review of Hong Kong entry requirements | v1.1 | M | 13.2.1 | Hong Kong launch is post-MVP but warrants early assessment |

### 13.3 Terms of Service & Disclaimers

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.3.1** Draft terms of service with clear non-advisory disclaimers | Private Beta | M | Legal counsel | Market Discovery 13.3.2 — accessible, not buried |
| **13.3.2** Draft privacy policy aligned with PDPA and PDPO | Private Beta | M | Epic 12, Legal counsel | Mandatory for app store submission |
| **13.3.3** In-app presentation of terms and privacy at signup (clear, not buried) | Private Beta | M | 13.3.1, 13.3.2 | Record of acceptance with timestamp |
| **13.3.4** Re-consent flow when terms materially change | MVP | M | 13.3.1, Epic 9 | Standard practice. *Beta: in 4-8 week beta, terms unlikely to materially change; team handles re-consent manually via email if needed.* |
| **13.3.5** In-context disclaimers at high-risk moments (e.g. scenario planning, AI suggestions) | Private Beta | M | Epic 4, Epic 8 | Disclaimers should appear where they matter, not only on signup |

### 13.4 AI Behaviour & Advisory Boundary

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.4.1** Document AI behavioural boundaries — what Budgie will and won't say | Private Beta | M | Epic 4.1.3, Legal counsel | Maps to regulatory grey/red zones (Market Discovery 13.1.3). Specific exclusions confirmed at 20 April workshop: debt prioritisation strategies, debt consolidation and relief advice, negotiation guidance. Debt *payoff* as a savings-style goal is permitted (Epic 6). |
| **13.4.2** Guardrails enforcement in AI responses | Private Beta | L | Epic 4.2.4 | Technical enforcement of 13.4.1 |
| **13.4.3** Graceful refusal and redirect for out-of-scope queries | Private Beta | M | 13.4.2, Epic 8.2.6 | When user asks for advice Budgie can't give. Workshop (20 April) confirmed this as a specific behaviour pattern: Budgie transparently indicates unsupported requests rather than attempting partial or oblique answers. |
| **13.4.4** AI interaction audit log for regulatory review and dispute resolution | Private Beta | M | Epic 4.5.4, Epic 12.6.1 | Cross-epic capability |

### 13.5 Marketing & Communications Compliance

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.5.1** Review website and marketing materials for advisory claims | MVP | M | Legal counsel | Website currently has "personal CFO" and DeFi advice language that must be reconciled with MVP scope (Market Discovery 10.2). *Beta: no public marketing during closed beta — beta users get accurate expectations via personal onboarding emails; website realignment part of public launch prep.* |
| **13.5.2** Content approval process for Budgie's social media posts | MVP | M | Epic 4.7.2 | Market Discovery 13.1.4 — social media under same rules as other advertising. *Beta: no active social posting during closed beta.* |
| **13.5.3** Content approval process for app store listings, screenshots, descriptions | MVP | M | — | Claims in listings must match product capability (Market Discovery 13.4.3). *Beta: distributed via TestFlight (iOS) / Internal Testing (Android) — no public app store listings required.* |
| **13.5.4** Retention of marketing communications for audit | MVP | M | — | Standard in regulated financial marketing. *Beta: no marketing communications generated during closed beta.* |
| **13.5.5** Pre-approved canned templates for all external marketing communications, with audit logging per post | MVP | L | 13.5.1, 13.5.2, 13.5.4 | Workshop 21 April: marketing comms (social, email, ad copy) use pre-approved templates rather than freely-generated content. Content approval happens once at template level, not per-post; each deployed post is logged against the template it came from. Provides compliance defensibility at scale (MD 13.1.4). *Beta: depends on marketing not happening during closed beta.* |

### 13.6 User Dispute & Support Infrastructure

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.6.1** User support channel (email minimum; in-app preferred) | Private Beta | M | — | Also required by app stores. Email satisfies the floor for beta. |
| **13.6.2** Complaint logging and tracking | MVP | M | 13.6.1 | Regulatory expectation in financial services. *Beta: manual tracking via shared spreadsheet or Slack channel for 50 users; formal system at MVP.* |
| **13.6.3** Process for escalation of complaints involving AI guidance | Private Beta | M | 13.6.2, 13.4.4 | Needed to review what the AI actually said and why. This is a post-hoc dispute resolution process, not real-time human-in-the-loop review — the MVP AI is fully autonomous (Market Discovery 13.3.1, 20 April workshop). Review happens after a user raises a concern, drawing on the audit log. *Beta: one-pager process drawing on the audit log; formal workflow at MVP.* |

### 13.7 Ongoing Compliance Operations

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **13.7.1** Regulatory change monitoring — track MAS, HKMA, and app store policy changes | v1.1 | S | — | Lightweight but necessary; could be a founder/operations task rather than product |
| **13.7.2** Annual compliance review process | v1.1 | M | 13.1.1 | Organisational discipline |
| **13.7.3** Incident disclosure process for breaches or regulatory events | Private Beta | M | Epic 12.6.3 | Bridges data privacy and financial regulatory reporting. PDPA requires breach notification capability — even a basic written process is required for beta. |

### Epic 13 — Assumptions & Open Questions

**Assumptions:**
- The "Financial Coach" positioning holds under legal review — pending formal advice
- Budgie's AI can be reliably constrained from giving investment advice through the combination of guardrails, prompt engineering, tool-augmented calculations, RAG-constrained external knowledge, and transparent refusal — no human-in-the-loop review is planned
- Legal counsel will be engaged for at least MVP review, MAS engagement, terms of service drafting, and data privacy policy review
- The founder will drive corporate entity and insurance matters with legal support — this is not Toptal scope

**Open Questions:**
- Has a legal entity been established? If so, where? (Market Discovery Open Question #20)
- Who is the legal counsel engaged for MAS and regulatory advice?
- Is MAS Sandbox being actively considered, and if so who is managing that engagement?
- What's the compliance policy on Budgie discussing topics adjacent to investment advice — tax, insurance, property, pensions? Each is a separate regulatory surface.
- Is the content approval process for Budgie's social voice (Epic 4.7.2) run by the founder's marketing partner or by Toptal during the engagement?

---

## Epic 14: Analytics & Instrumentation

_Product analytics, funnel tracking, engagement metrics, and the telemetry required to measure MVP success and demonstrate traction to investors._

Analytics is the unglamorous capability that makes every other capability measurable. Without it, Budgie is flying blind — there's no way to know what's working, what isn't, or which assumptions (from the Market Discovery doc) are holding up in the real world. For a pre-seed/seed-stage startup, this is also the machinery that produces the traction story for investors (Market Discovery 9.5).

**Key strategic considerations:**
- The primary commercial objective at this stage is traction for fundraising, not cashflow positivity (Market Discovery 9.5). Analytics is what *demonstrates* traction credibly.
- Analytics must be built from day one — retrofitting instrumentation after launch creates data gaps that undermine the ability to show meaningful trends
- Funnel instrumentation (Epic 1.6) is the single highest-value area — onboarding is where most users are lost
- Unit economics (LTV, CAC, churn) require data that can only be collected if the right events are tracked from the start
- Privacy considerations apply here too — analytics that identifies users must be included in consent flows (Epic 12.3)
- Third-party analytics tools process user data and therefore fall under Epic 12.5 third-party data handling
- Investor-grade metrics (MRR growth, cohort retention, conversion funnels) need specific tracking, not just "how many users do we have"

### 14.1 Analytics Infrastructure

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.1.1** Select analytics platform(s) — product analytics (Amplitude / Mixpanel / PostHog) + marketing attribution (Branch / AppsFlyer) | Private Beta | M | Epic 12.5 | Build-vs-buy is firmly buy; DPAs required |
| **14.1.2** Implement event tracking SDK in mobile app | Private Beta | M | 14.1.1 | Standard integration |
| **14.1.3** Define event taxonomy — naming conventions, event schema, properties | Private Beta | M | 14.1.2 | Critical for data quality; messy taxonomies become unusable fast |
| **14.1.4** Server-side event tracking for authoritative events (subscriptions, account deletions) | Private Beta | M | 14.1.2 | Client events can be lost or blocked; server-side is the source of truth for business-critical metrics |
| **14.1.5** Data warehouse for long-term analytics (e.g. BigQuery, Snowflake) | v1.1 | L | 14.1.1 | Nice-to-have at MVP; essential once the team has data analysts |

### 14.2 Onboarding & Activation Funnel

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.2.1** Track every step of the onboarding funnel | Private Beta | M | Epic 1.6.1, 14.1.2 | Highest-value analytics area |
| **14.2.2** Drop-off analysis at each step | Private Beta | S | 14.2.1 | Identifies friction points |
| **14.2.3** Time-to-activation metric (first meaningful value moment — connecting an account, setting a goal, etc.) | Private Beta | M | 14.2.1 | Activation is a better leading indicator than signups |
| **14.2.4** Cohort analysis of activation by acquisition source | v1.1 | M | 14.2.3, 14.5.1 | Different channels produce different quality users |

### 14.3 Engagement Metrics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.3.1** Daily / weekly / monthly active users (DAU / WAU / MAU) | Private Beta | S | 14.1.2 | Core engagement trio |
| **14.3.2** Session length and frequency | Private Beta | S | 14.1.2 | Depth of engagement |
| **14.3.3** Feature adoption rates — what percentage of users use each feature | Private Beta | M | 14.1.2 | Shows which features earn their place |
| **14.3.4** Retention curves (N-day retention, cohort retention) | Private Beta | M | 14.1.2 | Critical investor metric |
| **14.3.5** Notification engagement (delivered, opened, acted upon) | MVP | M | Epic 9.5 | Directly measures the proactive AI value. *Beta: depends on Epic 9.5 deferred.* |
| **14.3.6** AI interaction metrics (messages exchanged, feature usage, user feedback) | Private Beta | M | Epic 4, Epic 8 | Measures the core differentiator |

### 14.4 Financial & Subscription Metrics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.4.1** MRR (Monthly Recurring Revenue) tracking | MVP | M | Epic 11.6.1 | Primary SaaS metric. *Beta: no revenue in beta — Epic 11 deferred entirely.* |
| **14.4.2** Conversion rate — free to paid | MVP | M | 14.4.1, Epic 11 | Core funnel metric. *Beta: no conversion in beta.* |
| **14.4.3** Churn rate — monthly subscription cancellations | MVP | M | 14.4.1 | Leading indicator of product-market fit. *Beta: no subscriptions in beta.* |
| **14.4.4** ARPU (Average Revenue Per User) | MVP | S | 14.4.1 | Unit economics input. *Beta: no revenue in beta.* |
| **14.4.5** LTV:CAC ratio (requires CAC data from 14.5) | v1.1 | M | 14.4.4, 14.5 | Fundamental SaaS health metric |

### 14.5 Acquisition & Attribution

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.5.1** Attribution tracking — where did users come from (app store, social, content, referral) | MVP | M | 14.1.1 | Required to measure CAC per channel. *Beta: no acquisition channels in closed beta — invitations are direct.* |
| **14.5.2** Install attribution via third-party SDK (Branch / AppsFlyer) | MVP | M | 14.5.1 | Mobile attribution is a specialist category. *Beta: TestFlight/Internal Testing — no public install attribution needed.* |
| **14.5.3** Referral code tracking for shared content | MVP | M | Epic 10.1.4 | Sharing confirmed as MVP; referral tracking should match. *Beta: no referrals in closed beta.* |
| **14.5.4** Marketing spend tracking and CAC calculation | MVP | M | 14.5.1 | Founder / operations may do this in a spreadsheet initially. *Beta: no marketing spend during closed beta.* |

### 14.6 AI-Specific Analytics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.6.1** LLM cost tracking per user and aggregate | Private Beta | M | Epic 4.2.5 | Critical unit economics input — LLM costs scale with usage |
| **14.6.2** AI response quality metrics (user thumbs up/down, follow-up questions, session abandonment) | Private Beta | M | Epic 8.5.3 | Quality signal loop |
| **14.6.3** AI guardrail trigger tracking (refusals, redirects, fallback responses) | Private Beta | M | Epic 13.4.2 | Helps identify edge cases and regulatory boundary misses |
| **14.6.4** Content variation effectiveness — are daily check-ins staying fresh? | v1.1 | M | Epic 4.4.2 | Harder to measure but critical for long-term engagement |

### 14.7 Operational & Quality Metrics

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.7.1** App crash reporting (e.g. Sentry, Firebase Crashlytics) | Private Beta | S | — | Mobile app stability is essential |
| **14.7.2** API error rate monitoring (Finverse, LLM, internal APIs) | Private Beta | M | — | Early warning of systemic issues |
| **14.7.3** Performance monitoring (API latency, app launch time) | MVP | M | — | Finance app users expect snappiness. *Beta: basic crash + error monitoring (14.7.1, 14.7.2) covers beta needs; detailed performance monitoring at MVP.* |
| **14.7.4** Data pipeline health monitoring (transactions flowing, categorisation accuracy) | Private Beta | M | Epic 2, Epic 5 | Silent data failures erode trust |

### 14.8 Reporting & Dashboards

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **14.8.1** Founder-level KPI dashboard (DAU, MRR, conversion, churn, Financial Health Score distribution) | MVP | M | 14.3, 14.4 | Real-time view of traction. *Beta: team queries raw data via analytics platform UI during beta; formal dashboard at MVP.* |
| **14.8.2** Investor-update dashboard / report template | MVP | M | 14.8.1 | Makes monthly investor updates straightforward. *Beta: too small for investor reporting purposes.* |
| **14.8.3** Team-level operational dashboards (error rates, user support load, AI quality) | v1.1 | M | 14.7 | Tactical rather than strategic |

### Epic 14 — Assumptions & Open Questions

**Assumptions:**
- A third-party analytics platform (Amplitude, Mixpanel, or PostHog) is used rather than building in-house
- A third-party attribution platform (Branch or AppsFlyer) is used for install attribution
- The team has analytics skills to configure, query, and interpret the data — or will develop them
- GDPR-style consent mechanisms (already built in Epic 12.3) will cover analytics consent for launch markets; cookie-style consent banners are not required for a mobile app

**Open Questions:**
- What specific metrics will the founder commit to reporting to investors in monthly updates? This shapes dashboard priorities.
- Is there a target for each of the key metrics (DAU, conversion rate, LTV, etc.) at 3, 6, 12 months post-launch?
- How much analytics data is retained and for how long — this has privacy and cost implications
- Will the founder or a growth specialist own the analytics function post-launch? This affects the sophistication level required from day one.
- Are there specific event types that should be server-side only for business-critical accuracy (e.g. subscription events) vs client-side for tactical insight?

---

## Epic 15: Internal Admin & Back Office

_The web-based internal dashboard used by the founder, customer support, marketing, and operations teams. Not user-facing, but essential for running the business._

The mobile app is what users see; the back office is what makes running the business possible. This epic covers the internal tooling the team needs to support users, configure the app, harvest marketing data, and operate day-to-day. It's often under-scoped in early-stage products because it doesn't feel like "real product work" — until customer support requests start arriving and there's no way to look anything up.

**Key strategic considerations:**
- The back office is a multi-user system with role-based access — different team members need different levels of access
- Configuration capabilities (feature flags, tier limits, AI parameters) in the back office allow the team to change behaviour without a new app release — critical for responsive iteration post-launch
- All back-office access touches sensitive user data and falls under Epic 12 (Data & Privacy) — audit logging and least-privilege access are non-negotiable
- The marketing list (harvested emails, signups, etc.) is a commercial asset that must be managed with explicit consent under PDPA/PDPO (Epic 12.3)
- Some of this capability could be served initially by third-party tools (Zendesk for support, Customer.io for marketing, etc.) — build-vs-buy decisions should be explicit
- Back office usually lags the main app in polish — that's acceptable as long as it's functional and secure
- **Beta scope:** Admin tooling for beta is intentionally minimal — the team operates 50 beta users using direct tools (analytics platform UI, monitoring services, email service dashboards, Slack for tracking, direct DB access for support actions) rather than custom admin screens. Foundational items ship in beta (admin accounts, MFA, audit log, user lookup, AI conversation review for dispute resolution); the rest of the back-office tooling lands at MVP when team scale and user volume justify the investment.

### 15.1 Admin Authentication & Access Control

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.1.1** Admin user accounts separate from consumer user accounts | Private Beta | M | Epic 12.1 | Different security model; different database |
| **15.1.2** Role-based access control (admin, support, marketing, read-only) | MVP | M | 15.1.1 | Least-privilege principle. *Beta: small team (4-5 people) operates on single admin role with audit logging (15.1.4); formal RBAC at MVP.* |
| **15.1.3** MFA required for all admin accounts | Private Beta | S | 15.1.1 | Non-negotiable for internal access to user data |
| **15.1.4** Audit log of all admin actions | Private Beta | M | Epic 12.6.1 | Who viewed what, when, and why |
| **15.1.5** Session management and forced timeout for admin sessions | Private Beta | S | 15.1.1 | Stricter than consumer app |

### 15.2 Customer Support Tooling

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.2.1** User search and lookup by email, name, or user ID | Private Beta | M | Epic 12 | Foundational for any support interaction |
| **15.2.2** User profile view — account status, subscription tier, connected accounts (metadata only, not balances) | Private Beta | M | 15.2.1 | Support needs context without seeing sensitive financial detail |
| **15.2.3** View user's recent AI interactions (for dispute resolution) | Private Beta | M | Epic 4.5.4, Epic 13.4.4 | Tied to AI audit log |
| **15.2.4** View user's notification history | MVP | S | Epic 9 | "Did I really get a notification about this?" *Beta: team queries email service provider dashboards directly for 50 users.* |
| **15.2.5** Trigger common support actions — resend verification email, reset password, refund subscription | MVP | M | Epic 11, Epic 12 | Saves back-and-forth. *Beta: no subscriptions/refunds, no password resets (social login). Team handles edge cases via direct DB / email service for 50 users.* |
| **15.2.6** Integrate with a CRM for support and marketing management (specific platform TBC — Zoho is a candidate but not decided) | MVP | M | — | Integrates with an existing tool rather than building custom. **24 April workshop** reopened the Zoho-specific decision — alternative CRMs are on the table. *Beta: no CRM needed for closed beta — team uses Slack for tracking.* |
| **15.2.7** Internal notes on user accounts | MVP | S | 15.2.2 | Support teams need to leave context for each other. *Beta: team uses Slack/shared doc for 50 users.* |

### 15.3 Marketing & Communications

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.3.1** Marketing email list management — signups, waitlist, active users | MVP | M | Epic 12.3 | Respect consent state; cannot email users who haven't opted in. *Beta: no marketing during closed beta — team manages a small manual list (spreadsheet or Slack) for the 50 users.* |
| **15.3.2** Segmented lists (by tier, by activation state, by geography) | MVP | M | 15.3.1, Epic 14 | Targeted marketing is more effective |
| **15.3.3** Integration with email service provider (e.g. Customer.io, SendGrid, Mailchimp) | MVP | M | 15.3.1 | Build-vs-buy firmly buy. *Beta: transactional email infrastructure (9.1.4) covers beta needs; marketing campaign infrastructure at MVP.* |
| **15.3.4** Export of marketing list for external campaigns | MVP | S | 15.3.1, Epic 12.3 | With consent enforcement |
| **15.3.5** Campaign performance tracking (open rates, click rates, conversions) | v1.1 | M | 15.3.3, Epic 14 | Usually provided by the ESP |

### 15.4 App Configuration & Feature Flags

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.4.1** Feature flag system — enable/disable features per user, cohort, or globally without app release | MVP | L | Epic 11.1.3 | Essential for safe rollouts and A/B testing. *Beta: TestFlight rapid iteration covers beta; full feature flag system at MVP for safe production rollouts.* |
| **15.4.2** Tier limit configuration — adjust what's included in Free/Basic/Premium without code changes | MVP | M | Epic 11.1.1 | Commercial flexibility |
| **15.4.3** AI parameter configuration — adjust prompts, guardrail strictness, check-in frequency defaults | MVP | L | Epic 4 | Lets the team iterate on AI behaviour without engineering time. *Beta: AI behaviour iterated via config files + redeploy (Tech Lead handles); admin UI for AI parameters at MVP.* |
| **15.4.4** Notification template management | MVP | M | Epic 9 | Edit notification copy, test variants |
| **15.4.5** Category taxonomy management | v1.1 | M | Epic 5.1.2 | Add/edit transaction categories without app release |

### 15.5 Business Analytics & Reporting

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.5.1** Integrate analytics dashboards (from Epic 14.8) into the admin portal | MVP | M | Epic 14.8 | Single place for the team to check metrics. *Beta: dashboards deferred (Epic 14.8).* |
| **15.5.2** Ad-hoc querying capability for product managers | v1.1 | M | Epic 14.1.5 | Usually via the analytics platform directly, not custom UI |
| **15.5.3** Financial reports (revenue, churn, cohort LTV) | MVP | M | Epic 11.6, Epic 14.4 | Useful for founder and investor updates |

### 15.6 Content & Review Management

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.6.1** Review queue for AI responses flagged for quality issues | MVP | M | Epic 8.5.3 | Human-in-the-loop quality control. *Beta: thumbs-down feedback (Epic 8.5.3) reviewed via analytics platform query rather than dedicated queue UI.* |
| **15.6.2** Social media post approval workflow | MVP | M | Epic 4.7.2, Epic 13.5.2 | Compliance requirement |
| **15.6.3** User-reported content review queue | v2+ | M | Epic 10.4.1 | Only relevant once user-generated content exists |

### 15.7 Operational Monitoring

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **15.7.1** System health dashboard (API status, error rates, sync health) | MVP | M | Epic 14.7 | "Is Budgie working right now?" *Beta: team checks individual monitoring tools directly (Sentry, analytics platform, etc.).* |
| **15.7.2** Alerting rules and on-call configuration | MVP | M | 15.7.1 | 24/7 finance app needs someone watching. *Beta: native alerting from monitoring tools (Sentry → Slack) covers beta needs.* |
| **15.7.3** Incident management integration | v1.1 | M | 15.7.2 | Formal process for significant outages |

### Epic 15 — Assumptions & Open Questions

**Assumptions:**
- The back office is a web application separate from the mobile app, accessed by internal team members only
- Several components can be served by third-party SaaS tools (helpdesk, email marketing, analytics) rather than custom-built
- The founder and small initial team are the primary users at launch; the system must scale to a larger support team later
- Admin access is restricted to a whitelist of email domains / specific accounts

**Open Questions:**
- Who will be the first admin users — just the founder, or is there a support or marketing hire already planned?
- What's the preferred helpdesk tool — Zendesk, Intercom, Freshdesk, or other?
- What's the preferred email marketing tool — Customer.io, Mailchimp, SendGrid, or other?
- Will the back office need to support external contractors (e.g. Toptal team members during the engagement) or strictly full-time employees?
- Is there a dedicated customer support hire planned for post-launch, or will the founder handle support initially?

---

## Epic 16: Localisation & Internationalisation

_Locale restriction to control which markets the app serves, connection restrictions per jurisdiction, and internationalisation (i18n) to support multiple languages, currencies, date formats, and regional conventions._

Singapore is a multi-lingual market (English, Mandarin, Malay, Tamil). The founder's market research explicitly states "Multi-language (EN, CN, SEA expansion)" as a target. Even for an English-first MVP, the i18n architecture must be in place from day one — retrofitting it later means touching every screen, every notification, and every AI prompt. Separately, locale restriction is a regulatory necessity — the app must not serve users in jurisdictions where it's not licensed to operate, and must restrict all data connections (bank, crypto, DeFi) to the user's registered locale.

**Key strategic considerations:**
- Singapore's English-first market simplifies MVP but Mandarin support would significantly widen the addressable user base. **Language priority confirmed (24 April workshop):** SG = English MVP, Mandarin later (simplified); HK = English and Cantonese launched jointly.
- **i18n architecture timing resolved (1 May):** retrofit in v1.1, not built in MVP. English-only MVP launches with hardcoded strings; i18n framework, string externalisation, and locale-specific formatting added in v1.1.
- Locale restriction is a regulatory requirement, not a nice-to-have — serving users in unlicensed jurisdictions creates legal exposure (Market Discovery 13.1)
- Locale restriction extends beyond app access to all data connections — a Singapore-registered user must only be able to connect Singapore bank accounts, Singapore-available exchanges, and Singapore-relevant DeFi protocols. Allowing a Singapore user to add a Hong Kong bank account would create regulatory, data privacy, and tax reporting complications in a jurisdiction the product is not licensed to operate in.
- The AI layer (Epic 4) adds a unique i18n challenge — Budgie's personality, tone, and coaching must work in every supported language, not just be translated
- Currency formatting, date formats, and number formats vary by locale and affect trust — $1,000.00 vs $1.000,00 matters
- Transaction data from banks arrives in local formats and languages — categorisation (Epic 5) must handle this
- App store listings need localisation per market for discoverability

### 16.1 Locale Restriction & Jurisdiction Control

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **16.1.1** Restrict app availability to approved markets via app store settings (Singapore only for MVP) | Private Beta | S | — | Apple and Google both support geographic availability restrictions. Beta uses TestFlight country restrictions. |
| **16.1.2** Server-side locale check — verify user's jurisdiction on registration and enforce strict geo-restriction to Singapore users only for MVP | Private Beta | M | Epic 12.1 | Belt-and-braces alongside app store restriction. **24 April workshop confirmed** strict enforcement — unauthorised access from HK or elsewhere must be blocked to avoid regulatory exposure. |
| **16.1.3** Restrict Finverse bank connections to Singapore-registered institutions only | Private Beta | M | Epic 2, 16.1.2 | User cannot add a HK or US bank account from a Singapore locale |
| **16.1.4** Restrict crypto exchange connections to exchanges available/licensed in the user's locale | Private Beta | M | Epic 3, 16.1.2 | Exchange availability varies by jurisdiction; must match the user's registered locale |
| **16.1.5** Restrict DeFi wallet tracking to protocols and chains approved for the user's locale | Private Beta | M | Epic 3, 16.1.2 | DeFi regulatory status varies by jurisdiction — some protocols may be restricted in certain markets |
| **16.1.6** Locale-aware connection options — only show the user banks, exchanges, and DeFi options relevant to their registered jurisdiction | Private Beta | M | 16.1.3, 16.1.4, 16.1.5 | UX implication — users shouldn't even see options they can't use |
| **16.1.7** Graceful handling for users outside supported locales (waitlist capture, not a dead end) | MVP | M | 16.1.2 | Turn a restriction into a marketing opportunity — "we're not in your market yet, but sign up to be first". *Beta: simple "not available in your region" message is enough; full waitlist capture at MVP.* |
| **16.1.8** Add Hong Kong as a supported locale (with HK-specific bank, exchange, and DeFi restrictions) | v1.1 | M | 16.1.2, Epic 13 (HK regulatory review) | Gated by regulatory readiness; each new locale requires its own connection whitelist |
| **16.1.9** Locale expansion framework — add new markets and their connection restrictions without code changes | v1.1 | L | 16.1.2 | Configuration-driven rather than hardcoded; each locale is a bundle of: allowed banks, allowed exchanges, allowed chains, regulatory rules |

### 16.2 Internationalisation Architecture

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **16.2.1** i18n framework selection and integration into mobile app | v1.1 | L | — | **Resolved (1 May):** retrofit in v1.1 — English-only MVP launches with hardcoded strings; i18n framework added in v1.1. Trade-off: faster MVP scope at cost of more painful v1.1 work touching every screen. |
| **16.2.2** Externalise all user-facing strings (screens, buttons, labels, error messages) | v1.1 | L | 16.2.1 | All strings live in code through MVP; externalised in v1.1 alongside i18n framework. |
| **16.2.3** Currency formatting per locale (symbol, decimal separator, thousands separator) | v1.1 | M | 16.2.1 | Hardcoded SGD format for MVP; per-locale formatting in v1.1. Financial app — getting this wrong destroys trust. |
| **16.2.4** Date and time formatting per locale | v1.1 | S | 16.2.1 | Hardcoded SG format for MVP. DD/MM/YYYY vs MM/DD/YYYY etc. |
| **16.2.5** Number formatting per locale | v1.1 | S | 16.2.1 | Hardcoded for MVP. Decimal and thousands separators vary. |
| **16.2.6** Right-to-left (RTL) layout support | v2+ | L | 16.2.1 | Only relevant if Arabic or Hebrew markets are in scope |

### 16.3 Language Support

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **16.3.1** English as default and fully supported language | Private Beta | S | 16.2.2 | Baseline |
| **16.3.2** Simplified Chinese (Mandarin) translation of all UI strings for Singapore market | v1.1 | L | 16.2.2 | Widens SG addressable market. Note: HK Mandarin is traditional, not simplified — this is a different localisation exercise (16.3.5) |
| **16.3.3** Language selection in user settings | v1.1 | M | 16.2.1 | Depends on 16.2.1 i18n framework now deferred to v1.1 — no point in language selection without the framework to switch into. |
| **16.3.4** Auto-detect preferred language from device settings | v1.1 | S | 16.3.3 | Depends on 16.3.3 now v1.1. |
| **16.3.5** Traditional Chinese translation for Taiwan and other traditional-Chinese markets | v2+ | L | 16.3.7 | Hong Kong handled separately at v1.1 via 16.3.7. |
| **16.3.6** Additional SEA language translations (Malay, Thai, etc.) | v2+ | L per language | 16.2.2 | Per founder's expansion roadmap |
| **16.3.7** Cantonese (traditional Chinese) translation of all UI strings for Hong Kong market | v1.1 | L | 16.2.2 | Hong Kong launch requires English and Cantonese jointly (24 April workshop). Traditional Chinese character set. Separate from SG Mandarin simplified translation (16.3.2). |

### 16.4 AI & Notification Localisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **16.4.1** Budgie's AI personality defined and tested in English | Private Beta | M | Epic 4.1.1 | Character, tone, and humour are language-specific |
| **16.4.2** Budgie's AI personality adapted for Mandarin (not just translated — culturally appropriate tone and idiom) | v1.1 | L | 16.4.1, 16.3.2 | Translation is not localisation — financial humour and coaching style differ culturally |
| **16.4.3** LLM prompt templates per supported language | v1.1 | L | Epic 4.2.2, 16.4.2 | Each language needs its own prompt engineering |
| **16.4.4** Notification and email templates per supported language | v1.1 | M | Epic 9, 16.3.2 | All outbound comms need localisation |
| **16.4.5** AI can respond in the user's preferred language | v1.1 | M | 16.4.3, Epic 4.2.1 | LLMs handle multi-language well but quality varies — needs testing |

### 16.5 Transaction & Data Localisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **16.5.1** Handle transaction descriptions in local languages (Mandarin merchant names, etc.) | Private Beta | M | Epic 5.1.1 | Singapore bank data may contain non-English text |
| **16.5.2** Category taxonomy localised per language | v1.1 | M | Epic 5.1.2, 16.3.2 | Categories must make sense in each language |
| **16.5.3** Financial Health Score explanation localised per language | v1.1 | M | Epic 7.1.3, 16.3.2 | Score methodology must be understandable in each supported language |

### 16.6 App Store Localisation

| Feature | Priority | Size | Dependencies | Notes |
|---|---|---|---|---|
| **16.6.1** English app store listing (title, description, screenshots, keywords) | MVP | M | — | Baseline for Singapore launch. *Beta: distributed via TestFlight which doesn't require public store listing.* |
| **16.6.2** Mandarin app store listing | v1.1 | M | 16.3.2 | Improves discoverability for Mandarin-searching users |
| **16.6.3** Localised screenshots per language | v1.1 | M | 16.6.2 | App store conversion optimisation |

### Epic 16 — Assumptions & Open Questions

**Assumptions:**
- MVP launches in English only (24 April workshop). Language priority: SG = English MVP + Mandarin later (simplified); HK = English and Cantonese launched jointly.
- ~~The i18n architecture is implemented from day one even though only English is populated — this avoids a painful retrofit~~ — **Resolved (1 May):** i18n framework retrofitted in v1.1; English-only MVP launches with hardcoded strings (16.2.1).
- Locale restriction via app store geographic settings plus server-side check is sufficient for MVP
- All data connections (banks, exchanges, DeFi) are restricted to the user's registered locale — no cross-jurisdiction connections
- Each new locale added to the system comes as a configuration bundle: allowed banks, allowed exchanges, allowed chains, regulatory rules, supported languages
- AI localisation requires cultural adaptation, not just translation — a separate prompt engineering effort per language

**Open Questions:**
- ~~Is Mandarin support a priority for Singapore launch (v1.1) or deferred to HK expansion?~~ — **Resolved (24 April workshop):** SG Mandarin (simplified) is v1.1 as previously assumed; HK is English + Cantonese jointly at v1.1, not dependent on Mandarin.
- ~~Should the i18n architecture be built in MVP (clean but adds scope) or retrofitted in v1.1 (adds v1.1 effort but a faster English-only MVP)?~~ — **Resolved (1 May):** retrofit in v1.1 (16.2.1).
- Who handles translations — in-house, agency, or crowdsourced? Quality matters enormously for a financial product.
- Does the founder have Mandarin-speaking team members who can validate AI personality and tone in Chinese?
- For locale restriction, what's the policy on expats — a UK citizen living in Singapore with a UK phone number should be allowed; how is this handled?
- Should the AI be able to code-switch (mix languages in a single response, as is common in Singapore) or stay strictly in the user's selected language?
- How is locale determined at registration — app store country, device settings, self-declared, address verification, or a combination?
- For crypto restrictions per locale, who maintains the approved list of exchanges and protocols — is this a product/compliance function or outsourced to a data provider?

---

## Appendix

### A. Cross-Epic Dependencies

_Dependencies that span multiple epics, illustrating where coordination is required and which epics are most foundational._

**Epic 4 (AI Coaching & Personality) is central.** It's referenced by Epics 1 (onboarding), 5 (budget insights), 6 (goal coaching), 7 (score narration), 8 (ask anything), 9 (notification content), and 13 (advisory boundary enforcement). The AI infrastructure and personality must be defined early because so much else depends on it.

**Epic 12 (Data & Privacy Infrastructure) is foundational.** Every other epic that touches user data depends on the identity model, storage architecture, and consent framework defined here. Late changes to data architecture cascade painfully through the rest of the product.

**Epic 9 (Notifications) is the delivery mechanism** for proactive features across Epics 2 (re-authentication), 5 (budget warnings), 6 (goal milestones), 7 (score alerts), 11 (trial expiry), and 13 (terms updates). Without the notification infrastructure, "proactive" is a claim the product can't back up.

**Epic 11 (Pricing & Subscription) gates features across the product.** The tier boundaries defined in 11.1.1 are referenced by every feature that might be Premium-only. This means 11.1.1 is a blocking decision — until it's made, many feature designs have an open question.

**Epic 14 (Analytics & Instrumentation) cuts across everything.** Funnel tracking in Epic 1, engagement metrics in Epics 4 and 9, subscription metrics in Epic 11, AI quality metrics in Epics 4 and 8 — all require Epic 14 instrumentation to be built alongside the features they measure.

**Epic 13 (Compliance & Regulatory) constrains multiple epics.** The advisory boundary (13.4) affects what Epic 4 and Epic 8 can say. Terms of service and disclaimers (13.3) thread through Epic 1 onboarding. Social media approval (13.5.2) governs Epic 4.7. Corporate entity (13.1.1) is a prerequisite for entire categories of work.

**Epic 2 (Banking Aggregation) has a critical upstream spike.** Feature 2.1.1 (Finverse capability verification) is the single most important early technical task — its outcomes resize substantial parts of Epics 2, 5, 7, and 8.

**Epic 16 (Localisation & Internationalisation) constrains Epics 2 and 3.** Locale restriction is not just about who can use the app — it determines which banks, exchanges, and DeFi protocols a user can connect to. The jurisdiction control layer (16.1) must be in place before any data connection features in Epics 2 and 3 go live, otherwise a Singapore user could connect a Hong Kong bank account or an exchange not licensed in their market. The i18n architecture (16.2) must be implemented from day one to avoid a painful retrofit of every screen, notification, and AI prompt later.

**Foundational epic sequencing for MVP:**

The natural build order is:
1. Epic 12 (Data & Privacy) and Epic 15 (Admin) scaffolding
2. Epic 16 (Localisation) i18n architecture and locale restriction framework in parallel
3. Epic 2 technical spike (2.1.1) in parallel
4. Epic 4 AI personality and infrastructure definition
5. Epic 1, 2, 5 core data capture and display (with locale-restricted connections enforced via Epic 16)
6. Epic 3 crypto connections (if in MVP scope, with locale restrictions enforced via Epic 16)
7. Epic 6, 7, 8 value-layer features
8. Epic 9, 11 proactive and commercial layer
9. Epic 13, 14 compliance and instrumentation woven throughout
10. Epic 10 largely deferred

---

### B. Open Questions

_Backlog-specific questions that emerged during feature definition, distinct from the open questions already logged in the Market Discovery document._

**Scope & Prioritisation**

1. ~~Is crypto aggregation (Epic 3) in or out of MVP? A clean bank-only MVP would ship meaningfully faster.~~ — **Resolved (20 April workshop):** in MVP; scope confirmed as exchange holdings + on-chain wallet balances (Epic 3).
2. ~~Are social sharing features (Epic 10.1) needed for MVP, or is v1.1 acceptable?~~ — **Resolved:** outward sharing confirmed as MVP (founder 17 April; v0.3 change log; workshop reinforced for score sharing specifically — Epic 7.5).
3. What's the minimum viable set for Epic 4 (AI) — which of the MVP features can be deferred without killing the differentiation?

**Technical Approach**

4. ~~Which LLM provider will be used, and is the commercial conversation underway?~~ — **Partially resolved (20 April workshop):** Claude is the selected LLM. **Still open:** commercial conversation status (Epic 4.2.1).
5. Build vs buy decisions for transaction categorisation, subscription detection, and blockchain data — are these to be made by the technical lead during this engagement or post-engagement?
6. Will the back office (Epic 15) be built as a custom web app or assembled from SaaS tools (helpdesk, email platform, etc.) with custom glue?

**Timeline**

7. What's the target launch date, and does it align with the scope defined here?
8. Is there a soft launch / beta phase planned, and if so, what are the entry criteria and success measures?
9. Is fundraising tied to specific product milestones (e.g. "launch by Q3, 1,000 paying users by Q4")?

**Product Decisions Pending**

10. ~~Tier boundaries for Free / Basic / Premium (Epic 11.1.1)~~ — **Further resolved (21 April workshop):** tier names now Free / Premium / Pro; free trial model confirmed (7 or 14 days Premium, downgrade to Free). Previous decision — free tier = unlimited connections — remains but flagged aspirational per aggregator costs (Epic 11.1.1). **Still open:** feature-by-feature allocation across tiers, Premium vs Pro differentiation, trial length.
11. ~~Financial Health Score methodology (Epic 7.1.1)~~ — **Partially resolved:** Phase 1 (questionnaire) and Phase 2 (connected-data) methodology documents received from founder 17 April. **Still open:** methodology refinement work — founder acknowledged current approach as simplistic at 20 April workshop.
12. ~~Crypto MVP scope (Epic 3)~~ — **Resolved (20 April workshop):** exchange holdings + on-chain wallet balances (no transactions, no DeFi, no NFTs).
13. Onboarding tour enforcement level (Epic 1.1.3)
14. Budgeting methodology — zero-based vs envelope (Epic 5.3)

---

### C. Change Log

| Version | Date | Changes |
|---|---|---|
| 0.1 | 16 April 2026 | Initial draft backlog structured by 16 epics covering consumer app, AI, data, compliance, analytics, back office, and localisation. Feature-level breakdown with priority (MVP / v1.1 / v2+) and rough sizing. Cross-referenced to the Budgie Market Discovery document. |
| 0.2 | 17 April 2026 | Founder's Financial Health Score methodology documents (Phase 1 questionnaire, Phase 2 connected scoring) received and parked for build phase — referenced by Epic 7. |
| 0.3 | 20 April 2026 | Incorporated founder responses to Market Discovery open questions. Epic 10.1 (Outward Sharing) moved from v1.1 to MVP per founder confirmation. Epic 14.5.3 (Referral tracking) moved to MVP to match. Epic 12.3.1 updated to defer data monetisation consent to v1.1 per founder confirmation that data monetisation is not MVP scope. Epic 3.2 (On-chain wallet tracking) deferred from MVP to v1.1 per backlog refinement — MVP crypto scope narrowed to exchange balances for major coins only. Epic 12.1 updated to Google/Apple social login only for MVP. Epic 11.1.1 updated with first tier boundary decision (free tier = unlimited connections). Epic 15.2.6 updated to Zoho CRM. RAG feature (4.2.6) added per design discovery. Removed Team & Resourcing from open questions. Cleaned up open questions list. |
| 0.4 | 21 April 2026 | Incorporated the 20 April MVP workshop outcomes (first engagement session after v0.3) — in parallel with Market Discovery v0.4 updates. **Epic 2:** 2.1.1 spike narrowed to data quality / 2FA mitigation (coverage, history, pricing now known); assumptions and three open questions updated with workshop-confirmed Finverse specifics. **Epic 3:** 3.2 on-chain wallet tracking moved from v1.1 to MVP — scope is balance-only, no transaction-level data; 3.2.5 Solana/other L1s moved v2+ → v1.1; 3.4.1 and 3.5.1 updated to include on-chain scope. **Epic 4:** 4.2.1 updated — Claude selected as preferred LLM; new 4.2.7 deterministic calculation tool library; new 4.4.6 and 4.4.7 for weekly coaching sessions (system-scheduled, advisor-format, not user-initiated); 4.5.3 tightened; 4.6.2 token-cost framing added. **Epic 6:** Debt handling bifurcated — payoff treated as savings-style goal, prioritisation/consolidation/relief advice deferred v2+; 6.2.6 demoted v1.1 → v2+. **Epic 7:** 7.1.1 notes expanded on methodology refinement and Phase 1/Phase 2 founder docs; 7.5.1 and 7.5.2 score sharing moved v1.1 → MVP per workshop. **Epic 13:** Debt exclusions documented in 13.4.1; full-autonomy / no-human-escalation confirmed as strategic consideration and in 13.6.3; assumption A2 tightened with layered controls. **Appendix B:** Crypto-MVP questions (Q1, Q12) and social-sharing question (Q2) closed; LLM provider (Q4), tier boundaries (Q10), and FHS methodology (Q11) partially closed. Added strikethrough convention note to "How to Read This Backlog". |
| 0.5 | 22 April 2026 | Incorporated 21 April MVP workshop outcomes. **Epic 1:** added 1.5.3 (greyed-out upcoming features). **Epic 4:** added 4.1.5 and 4.1.6 (public voice enforcement; in-app user tone preference); added 4.4.8 monthly review (v1.1) and 4.4.9 yearly review (v2+). **Epic 8:** restructured 8.1.4 from query history to multi-conversation chat history management; added 8.1.5 (seeded summaries) and 8.1.6 (branching, v1.1). **Epic 9:** 9.3.2 notification throttling target confirmed at 2–3/day; daily-cap Open Question closed. **Epic 11:** tier names renamed Free/Premium/Pro across 11.1.1, 11.3.2, 11.4.1; tier-specifics Open Question partial-close. **Epic 12:** 12.5.4 reshaped to PII scrubbing specifically; added 12.5.5 financial figure obfuscation as v1.1. **Epic 13:** added 13.5.5 (pre-approved canned templates with per-post audit logging). **Appendix B:** Q10 further updated with tier rename and trial model. |
| 0.6 | 24 April 2026 | Incorporated 24 April internal workshop outcomes. **Epic 5:** 5.1.1 categorisation engine Notes flag non-English transaction description risk; added Open Question on proprietary vs third-party categorisation engine. **Epic 15:** 15.2.6 generalised — CRM platform TBC (Zoho is a candidate but no longer the decision). **Epic 16:** i18n architecture timing reopened — 16.2.1 through 16.2.5 priorities now "MVP *or* v1.1 — TBC" pending Tech Lead's technical assessment; 16.1.2 server-side locale check tightened to reflect workshop-confirmed strict geo-restriction; 16.3.2 Mandarin scoped specifically to SG-simplified; added 16.3.7 Cantonese for HK (v1.1); 16.3.5 refocused to Taiwan; strategic considerations and assumptions updated with SG = English MVP + Mandarin later / HK = English + Cantonese jointly language priority (24 April workshop); added Open Question on i18n build-now vs retrofit; closed Mandarin-priority Open Question. |
| 0.7 | 1 May 2026 | Major restructure introducing **Private Beta** as a new priority bucket sitting before MVP, in response to the Founder's 1 May guidance on a controlled limited-user soft launch. **Framing:** added Private Beta to the priority list with explicit caveat that beta is structurally complete but feature-narrowed — foundations ship in beta, breadth is deferred. **All 16 epics reclassified** with per-row Beta annotations explaining bucket choices: 179 features now in Private Beta, 148 MVP-additional, 71 v1.1, 23 v2+ (total 421). **Epic-level Beta scope notes added** to Epics 6 (defers entirely per Founder), 9 (notifications layer mostly defers), 10 (external sharing defers), 11 (commercial machinery defers entirely), 15 (admin tooling minimal for beta). **Epic 16 TBC resolved (1 May):** i18n architecture retrofitted in v1.1 — 16.2.1 through 16.2.5 moved from "MVP *or* v1.1 — TBC" to v1.1; 16.3.3 and 16.3.4 moved from MVP to v1.1 as dependents; strategic considerations bullet, assumption, and Open Question closed accordingly. **Anonymisation pass:** all references to individual team members and the founder removed throughout the document — replaced with "Tech Lead" and "Founder" for consistency and durability. **Structural updates:** "Priority & Sizing Key" renamed to "Priority & Sizing"; summary tables added showing distribution by priority bucket and by size estimate. |
