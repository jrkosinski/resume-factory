<!--
Source: split from Hamza-CTO.md master evidence-bank entry.
Purpose: modular resume source file, not a finished resume section.
Generated: 2026-07-01
-->
# Hamza / Overview Index

## Basic Info

**Company:** Hamza  
**Dates:** Approx. January 2024 – January 2026  
**Role / Title:** CTO and Co-Founder  
**Team Size:** 6 developers  
**Status:** Live in production  
**Primary Domain:** Decentralized e-commerce, crypto payments, Ethereum/EVM L2s, escrow, marketplace infrastructure, tokenomics, seller identity  
**Production Metrics:** Hundreds of users per month, ~$5k–$10k USD monthly throughput, 20+ individual sellers, thousands of SKUs

## Canonical Summary

Served as CTO and co-founder of Hamza, a live decentralized e-commerce platform designed to give sellers sovereignty over their data, brands, products, and seller identity through Ethereum, Optimism, and EVM L2 infrastructure. Led a six-developer engineering team across frontend, backend, seller admin, marketplace infrastructure, smart contracts, escrow, tokenomics design, and cross-chain crypto payments.

Architected and helped build a production multitenant e-commerce storefront, NFT-based seller identity model, Solidity multi-tenant escrow contracts deployed to Optimism and Optimism testnet, and a fully built multi-chain payment system supporting payments across Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, and other L2s while settling canonical escrow state on Optimism.

## Short Resume Summary Version

CTO and co-founder of Hamza, a live decentralized e-commerce platform with hundreds of monthly users, 20+ sellers, thousands of SKUs, and ~$5k–$10k monthly throughput. Led a six-developer team building MedusaJS/NestJS/Next.js marketplace infrastructure, NFT-based seller identity, Solidity escrow contracts on Optimism, tokenomics contract components, and a production cross-chain crypto payment system using payment intents, one-time holding wallets, chain listeners, idempotent verification, payment state machines, LiFi settlement, and wallet-based checkout.

## Modular Files

This Hamza entry has been split into the following project/evidence-bank files:

1. **Hamza-General-CTO-Leadership.md**  
   CTO/co-founder leadership, six-developer team, technical strategy, product/business strategy, repo/code review ownership, delivery process, CI/CD, environments, and cross-functional technical management.

2. **Hamza-Cross-Chain-Payment-System.md**  
   Payment intents, one-time deposit/holding wallets, chain listeners, RabbitMQ event processing, idempotent verification, Optimism canonical settlement, LiFi replenishment, HD wallet architecture, payment state machine, service architecture, and AWS reference architecture.

3. **Hamza-Decentralized-Ecommerce-Platform.md**  
   Multitenant e-commerce storefront, MedusaJS/NestJS/Next.js architecture, seller admin, seller backend, wallet checkout, marketplace features, NFT seller identity integration, PostgreSQL/Redis/AWS/Kubernetes stack, and production metrics.

4. **Hamza-Onchain-Escrow-Contracts.md**  
   Solidity `PaymentEscrow`, `PaymentEscrowAdmins`, `EscrowMulticall`, `SystemSettings`, `IPurchaseTracker`, Hats Protocol role model, consent-based release/refund state machine, protocol fees, seller-delegated permissions, and Hardhat/Foundry/Echidna testing.

5. **Hamza-Tokenomics-Utility-Token-Design.md**  
   Utility token design, seller escrow rent, initial seller mint, dispute-resolution incentives, tokenomics-related contracts, vaults, governance wrappers, and deployment/status caveats.

## Confirmed Production Facts

* CTO/co-founder role.
* Six-developer engineering team.
* Live decentralized e-commerce marketplace.
* Hundreds of users per month.
* ~$5k–$10k USD monthly throughput.
* 20+ individual sellers.
* Thousands of SKUs.
* Cross-chain payment system fully built and in use.
* Solidity escrow contracts deployed to Optimism and Optimism testnet.
* Tokenomics-related contracts deployed to Optimism and Optimism testnet.
* Solana payment support built but not deployed.
* LiFi integration implemented.
* CI/CD, dev/staging/testing environments, monitoring, and alerting.

## Primary Stack

**Languages:** TypeScript, Solidity  
**Frontend:** Next.js, React, Vite, Zustand, Zod, TanStack Router, TanStack Query, Radix UI, Tailwind CSS  
**Backend:** MedusaJS, NestJS, TypeORM, pnpm monorepo, shared common package  
**Data:** PostgreSQL, Redis, DynamoDB  
**Messaging:** RabbitMQ confirmed; EventBridge/SQS as target/reference architecture unless confirmed  
**Cloud:** AWS EC2, AWS RDS, AWS DynamoDB, AWS S3, AWS Load Balancing, Kubernetes  
**Blockchain:** Ethereum, Optimism, Arbitrum, Polygon, Mantle, Scroll, Bitcoin, Solana built but not deployed  
**Contracts/Testing:** Solidity, OpenZeppelin, Foundry, Hardhat, Echidna, Ethers v6, TypeChain, Mocha/Chai

## Resume Compiler Guidance

### CTO / Head of Engineering Roles

Use primarily:

* `Hamza-General-CTO-Leadership.md`
* selected production metrics from this overview
* one strong architecture bullet from either payments or e-commerce

Emphasize CTO/co-founder role, six-developer team, production platform, technical strategy, roadmap ownership, code review, repo management, dev/staging/testing environments, monitoring, alerting, and balancing strategy with hands-on implementation.

### Payments / Fintech Roles

Use primarily:

* `Hamza-Cross-Chain-Payment-System.md`
* selected context from `Hamza-Onchain-Escrow-Contracts.md`

Emphasize payment intents, payment-specific holding wallets, chain listeners, RabbitMQ event processing, idempotency, Optimism escrow settlement, merchant callbacks, LiFi replenishment, EVM/Bitcoin/Solana architecture, key storage, and state-machine processing.

### Blockchain / Solidity Roles

Use primarily:

* `Hamza-Onchain-Escrow-Contracts.md`
* selected tokenomics details from `Hamza-Tokenomics-Utility-Token-Design.md`

Emphasize Optimism, Solidity, `PaymentEscrow`, ETH/ERC-20 escrow, buyer/seller release flags, protocol fees, refunds, arbiter resolution, Hats Protocol, seller-delegated admin permissions, Foundry, Hardhat, Echidna, and multi-layer testing.

### E-Commerce / Marketplace Roles

Use primarily:

* `Hamza-Decentralized-Ecommerce-Platform.md`
* selected leadership context from `Hamza-General-CTO-Leadership.md`

Emphasize multitenant marketplace, MedusaJS, NestJS, Next.js, product catalog, inventory, cart, wishlist, seller tooling, wallet checkout, PostgreSQL, Redis, AWS, Kubernetes, 20+ sellers, thousands of SKUs, and live production use.

### Web3 Strategy / Tokenomics Roles

Use primarily:

* `Hamza-Tokenomics-Utility-Token-Design.md`
* selected leadership context from `Hamza-General-CTO-Leadership.md`
* selected escrow context from `Hamza-Onchain-Escrow-Contracts.md`

Emphasize utility token economics, seller escrow rent, dispute-resolution incentives, tokenomics contract components, vaults, governance wrappers, and ecosystem design caveats.

## External Claim Safety Notes

### Safe to Claim Now

* CTO and co-founder.
* Led six-developer team.
* Live decentralized e-commerce marketplace.
* Hundreds of monthly users, 20+ sellers, thousands of SKUs, and ~$5k–$10k monthly throughput.
* Cross-chain payment system fully built and in use.
* Payment intents, per-payment holding wallets, chain listeners, idempotent verification, immediate Optimism escrow settlement, merchant callbacks, and LiFi replenishment.
* Supported Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, and other EVM L2s.
* Solana payment support built but not deployed.
* Solidity escrow contracts deployed to Optimism and Optimism testnet.
* MedusaJS/NestJS/Next.js/TypeScript/PostgreSQL/Redis/RabbitMQ/AWS/Kubernetes stack.

### Use With Care / Qualify Internally

* HD wallet / BIP32/BIP39 production scope across all chains.
* React 19/TanStack/Radix/Tailwind dashboard production status.
* EventBridge/SQS/Step Functions/ECS Fargate/Aurora/Lambda architecture as implemented production infrastructure.
* Secrets Manager/KMS versus DynamoDB-encrypted key storage.
* DynamoDB versus PostgreSQL address metadata.
* Lambda polling versus persistent listener architecture.
* Sweeper contract production usage.
* Polygon Amoy and Sepolia `PaymentEscrow` deployment scope.
* Hats Protocol production usage versus protocol/test branch usage.

### Avoid Unless Confirmed

* Claiming the full EventBridge-centered AWS architecture was live production.
* Claiming all inter-service communication used EventBridge rather than RabbitMQ.
* Claiming Aurora Serverless v2, ECS Fargate, Step Functions, X-Ray, Cognito, or ElastiCache were deployed if they were only architectural recommendations.
* Claiming fully non-custodial payment handling.
* Claiming exact volume, uptime, failure rates, or number of processed payment intents.
* Claiming exact coverage percentage, exact audit status, or external audit completion from internal testing details alone.
