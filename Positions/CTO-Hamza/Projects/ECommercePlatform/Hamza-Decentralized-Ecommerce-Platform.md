<!--
Source: split from Hamza-CTO.md master evidence-bank entry.
Purpose: modular resume source file, not a finished resume section.
Generated: 2026-07-01
-->

# Hamza / Decentralized E-Commerce Platform

## Basic Info

**Company:** Hamza  
**Dates:** Approx. January 2024 – January 2026  
**Role / Title:** CTO and Co-Founder / Marketplace Architecture Lead  
**Status:** Live in production  
**Primary Domain:** Decentralized e-commerce, marketplace infrastructure, seller tooling, wallet checkout, NFT seller identity  
**Production Metrics:** Hundreds of users per month, ~$5k–$10k USD monthly throughput, 20+ individual sellers, thousands of SKUs  
**Primary Stack:** MedusaJS, NestJS, Next.js, TypeScript, PostgreSQL, Redis, AWS EC2, AWS RDS, AWS DynamoDB, AWS S3, AWS Load Balancing, Kubernetes, EventBridge/SQS, Solidity integration

## Canonical Summary

Led development of Hamza’s live multitenant decentralized e-commerce storefront, a production marketplace demonstrating how canonical on-chain seller identities could support seller-owned commerce infrastructure. The platform combined MedusaJS, NestJS, Next.js, TypeScript, PostgreSQL, Redis, AWS, Kubernetes, wallet-based checkout, escrow-backed transactions, seller administration, and NFT-based seller identity integration. It supported standard e-commerce workflows including inventory, product sorting/filtering, cart, wishlist, user management, preferences, notifications, seller tooling, and crypto-native checkout.

## Short Resume Summary Version

Led architecture and development of a live multitenant Web3 e-commerce marketplace using MedusaJS, NestJS, Next.js, TypeScript, PostgreSQL, Redis, AWS, Kubernetes, wallet-based checkout, seller administration, NFT-based seller identity, and escrow-backed commerce, supporting hundreds of monthly users, 20+ sellers, thousands of SKUs, and ~$5k–$10k monthly throughput.

## Primary Tags

- Multitenant e-commerce
- Marketplace platform
- Seller tools
- Seller admin
- Seller backend
- Product catalog
- Inventory management
- Cart
- Checkout
- Wishlist
- Filtering
- Sorting
- User preferences
- Notifications
- Buyer/seller workflows
- Decentralized marketplace
- Storefront infrastructure
- Marketplace operations
- Seller identity
- NFT seller identity
- SKUs
- GMV
- Throughput
- MedusaJS
- NestJS
- Next.js
- React
- TypeScript
- Zustand
- Vite
- Zod
- PostgreSQL
- Redis
- AWS EC2
- AWS RDS
- AWS DynamoDB
- AWS S3
- AWS Load Balancing
- Kubernetes
- EventBridge/SQS
- Wallet-based checkout
- Escrow-backed commerce

## Context

Hamza was created to decentralize e-commerce for sellers by allowing them sovereignty over their data, brands, products, and identity as sellers through Ethereum, Optimism, and EVM L2 infrastructure.

The core idea was that sellers should not be locked into a single centralized e-commerce marketplace. Instead, seller identity and marketplace participation could be represented through canonical on-chain primitives, allowing seller data, brand presence, product listings, and commerce relationships to become more portable across storefronts.

Hamza’s own flagship storefront was built to demonstrate this model in production: a working multitenant e-commerce site where sellers could list products, buyers could shop through familiar commerce flows, and crypto-native payment and escrow infrastructure could operate underneath the marketplace.

## Product / Business Model

Hamza’s product model centered on decentralized commerce infrastructure for sellers.

The platform was intended to support:

- Seller sovereignty over data.
- Seller sovereignty over brand presence.
- Seller sovereignty over product listings.
- NFT-based seller identity.
- Marketplace interoperability.
- Crypto-native checkout.
- Escrow-backed transactions.
- Tokenomics-based seller incentives.
- Dispute-resolution incentive design.
- Ecosystem storefronts sharing canonical on-chain seller identities.

The long-term ecosystem vision was that other builders could create their own storefronts while sharing canonical seller identities and commerce infrastructure. Hamza’s flagship site existed to prove the model and serve as the reference implementation.

## Flagship E-Commerce Site

### Problem

The ecosystem was intended to encourage external developers to build their own e-commerce storefronts around canonical on-chain seller identities. However, Hamza needed to demonstrate how the model would work in practice.

The flagship storefront solved that problem by providing a live reference marketplace.

### Product

The flagship site was a multitenant e-commerce storefront with standard marketplace functionality, including:

- Inventory.
- Product sorting.
- Product filtering.
- Cart.
- Wishlist.
- User management.
- User preferences.
- Notifications.
- Seller administration.
- Wallet-based payment flow.
- Escrow-backed commerce.
- NFT-based seller identity integration.

The platform used standard MedusaJS e-commerce functionality where appropriate and customized MedusaJS to allow payment by wallet.

### Backend Stack

- MedusaJS.
- NestJS.
- TypeScript.
- PostgreSQL.
- Redis.
- AWS EC2.
- Kubernetes.

### Frontend Stack

- MedusaJS.
- Next.js.
- TypeScript.
- Zustand.

### Seller Admin Stack

- TypeScript.
- Vite.
- Zustand.
- Zod.

### Seller Backend Stack

- MedusaJS.
- NestJS.
- TypeScript.
- PostgreSQL.
- Redis.
- AWS EC2.
- Kubernetes.

Potential resume phrasing:

> Led development of a live multitenant e-commerce storefront using MedusaJS, NestJS, Next.js, TypeScript, PostgreSQL, Redis, AWS EC2, and Kubernetes, customizing MedusaJS to support wallet-based crypto payments and escrow-backed marketplace transactions.

## NFT-Based Seller Identity

Seller identity used NFTs as the on-chain identity primitive.

This allowed seller identity to be represented independently from a single centralized storefront and supported the broader goal of seller-owned commerce identity across the ecosystem.

Potential resume phrasing:

> Designed NFT-based seller identity infrastructure to represent canonical seller identity on-chain and support decentralized marketplace interoperability across storefronts.

## System Architecture

Hamza’s architecture spanned storefront, seller admin, seller backend, marketplace backend, payment infrastructure, smart contracts, monitoring, and cloud deployment.

### Confirmed / Existing Infrastructure Components

- AWS Kubernetes.
- AWS Load Balancing.
- AWS RDS PostgreSQL.
- AWS DynamoDB.
- AWS S3.
- Redis.
- EventBridge/SQS.
- CI/CD.
- Dev environment.
- Staging environment.
- Testing environment.
- Monitoring.
- Alerting.

### High-Level Production Architecture

```text
Buyer / Seller / Storefront UI
        ↓
Next.js / MedusaJS storefront
        ↓
Marketplace backend
MedusaJS + NestJS + TypeScript
        ↓
PostgreSQL / Redis
        ↓
Payment intent service
        ↓
EventBridge/SQS event pipeline
        ↓
Chain listeners / payment verification
        ↓
Optimism settlement service
        ↓
Solidity multi-tenant escrow
        ↓
Merchant webhook callback
        ↓
LiFi batch settlement / liquidity replenishment
```

Potential resume phrasing:

> Architected a production Web3 commerce system across Next.js, MedusaJS, NestJS, PostgreSQL, Redis, EventBridge/SQS, AWS Kubernetes, DynamoDB, S3, Solidity contracts, chain listeners, and LiFi-based cross-chain settlement.

## Engineering Scope

Engineering work included:

- NestJS backend development.
- TypeScript backend/frontend development.
- MedusaJS customization.
- PostgreSQL-backed marketplace data.
- Redis caching/session support.
- EventBridge/SQS event-driven payment processing.
- AWS Kubernetes deployment.
- AWS RDS PostgreSQL infrastructure.
- AWS DynamoDB for payment/key-related data.
- AWS S3 object storage.
- AWS load balancing.
- CI/CD.
- Monitoring and alerting.
- Dev/staging/testing environments.

Potential resume phrasing:

> Built and led engineering across NestJS, TypeScript, MedusaJS, PostgreSQL, Redis, EventBridge/SQS, AWS Kubernetes, DynamoDB, S3, and load-balanced production infrastructure.

## Results / Metrics

Known production metrics:

- Live production marketplace.
- Hundreds of users per month.
- ~$5k–$10k USD monthly throughput.
- 20+ individual sellers.
- Thousands of SKUs.
- Cross-chain payment system fully built and in use.
- Escrow contracts deployed to Optimism and Optimism testnet.
- Tokenomics-related contracts deployed to Optimism and Optimism testnet.
- Solana payment support built but not deployed.
- CI/CD, dev/staging/testing environments, monitoring, and alerting.

Metrics to refine later:

- Exact user count.
- Exact SKU count.
- Exact seller count.
- Total GMV.
- Total escrow volume.
- Number of orders processed.
- Uptime/reliability metrics.
- Funding or business milestones, if safe to disclose.

# Bullet Bank

## E-Commerce / Marketplace Bullets

- Led development of a live multitenant e-commerce storefront with inventory, sorting, filtering, cart, wishlist, user management, preferences, notifications, seller tooling, wallet-based checkout, and escrow-backed commerce.

- Customized MedusaJS to support wallet-based crypto payments in a production decentralized commerce platform.

- Built seller/admin infrastructure using TypeScript, Vite, Zustand, Zod, MedusaJS, NestJS, PostgreSQL, Redis, AWS EC2, and Kubernetes.

- Designed marketplace infrastructure intended to let external storefronts interoperate with canonical NFT-based seller identities.

- Built and led engineering for a flagship multitenant e-commerce storefront demonstrating how canonical on-chain seller identities could support decentralized marketplace interoperability.

## Backend / Infrastructure Bullets

- Built and led backend engineering across NestJS, TypeScript, MedusaJS, PostgreSQL, Redis, EventBridge/SQS, AWS RDS, AWS DynamoDB, AWS S3, AWS load balancing, and Kubernetes.

- Architected a production Web3 commerce system spanning Next.js storefronts, MedusaJS/NestJS backends, PostgreSQL, Redis, EventBridge/SQS, AWS Kubernetes, DynamoDB, S3, chain listeners, LiFi settlement, and Solidity escrow contracts.

- Established dev, staging, and testing environments with CI/CD, monitoring, alerting, backend tests, payment-system tests, and smart-contract tests.

## Product / Web3 Marketplace Bullets

- Architected a production decentralized marketplace combining NFT-based seller identity, wallet-based checkout, multi-tenant escrow, cross-chain payments, and seller-owned commerce infrastructure.

- Designed NFT-based seller identity infrastructure to represent canonical seller identity on-chain and support decentralized marketplace interoperability across storefronts.

- Led a production marketplace with hundreds of monthly users, 20+ individual sellers, thousands of SKUs, and ~$5k–$10k USD monthly throughput.

# Strongest Resume Angles

## Marketplace / E-Commerce Roles

Emphasize:

- MedusaJS.
- Multitenant e-commerce.
- Inventory/cart/wishlist/users/preferences/notifications.
- Seller admin.
- Seller backend.
- Next.js storefront.
- Wallet checkout.
- Seller identity.
- 20+ sellers.
- Thousands of SKUs.
- Live production marketplace.

## Full-Stack / Product Engineering Roles

Emphasize:

- Next.js.
- TypeScript.
- Zustand.
- Vite.
- Zod.
- MedusaJS.
- NestJS.
- PostgreSQL.
- Redis.
- Marketplace UI.
- Seller admin.
- Payment integration.
- Production platform.

## Backend / Platform Roles

Emphasize:

- MedusaJS / NestJS backend customization.
- PostgreSQL and Redis.
- EventBridge/SQS event integration.
- AWS Kubernetes.
- Seller backend.
- Marketplace backend.
- Infrastructure and environments.

## Web3 Product / Marketplace Roles

Emphasize:

- NFT-based seller identity.
- Wallet-based checkout.
- Escrow-backed commerce.
- Decentralized marketplace interoperability.
- Seller-owned data/brand/product-listing model.

# ATS / Keyword Bank

Multitenant e-commerce, marketplace platform, seller tools, seller admin, product catalog, inventory management, cart, checkout, buyer/seller workflows, decentralized marketplace, storefront infrastructure, marketplace operations, seller identity, SKUs, GMV, throughput, MedusaJS, NestJS, Next.js, React, TypeScript, Zustand, Vite, Zod, PostgreSQL, Redis, EventBridge/SQS, AWS EC2, AWS RDS, AWS DynamoDB, AWS S3, AWS Load Balancing, Kubernetes, CI/CD, monitoring, alerting, wallet-based checkout, NFT seller identity, escrow-backed commerce.

# Future YAML Shape

```yaml
id: hamza_decentralized_ecommerce_platform
type: startup_project
company: Hamza
role_title: CTO and Co-Founder / Marketplace Architecture Lead
dates:
  start: 2024-01
  end: 2026-01
status:
  production: true
  flagship_storefront_live: true
scale:
  sellers: "20+"
  skus: "thousands"
  users_per_month: "hundreds"
  monthly_throughput_usd: "$5k-$10k"
domains:
  - decentralized_ecommerce
  - marketplace_infrastructure
  - multitenant_ecommerce
  - nft_seller_identity
  - wallet_checkout
  - escrow_backed_commerce
technologies:
  frontend:
    - Next.js
    - React
    - TypeScript
    - Zustand
    - Vite
    - Zod
  backend:
    - MedusaJS
    - NestJS
    - TypeScript
  databases:
    - PostgreSQL
    - Redis
    - DynamoDB
  cloud:
    - AWS_EC2
    - AWS_RDS
    - AWS_DynamoDB
    - AWS_S3
    - AWS_Load_Balancing
    - Kubernetes
  messaging:
    - EventBridge/SQS
features:
  - inventory
  - product_sorting
  - product_filtering
  - cart
  - wishlist
  - user_management
  - user_preferences
  - notifications
  - seller_administration
  - wallet_based_payment_flow
  - escrow_backed_commerce
  - nft_seller_identity_integration
seller_identity:
  model: NFT_based
```

# Missing / Worth Clarifying Later

1. Exact production launch date.
2. Exact user count.
3. Exact SKU count.
4. Exact seller count.
5. Exact total GMV / order count.
6. Whether seller NFT identity was minted for all production sellers.
7. Exact production frontend stack version.
8. Exact admin-dashboard scope versus seller-admin scope.
9. Exact deployment topology: Kubernetes/EKS, EC2-managed Kubernetes, or another cluster arrangement.
10. Exact monitoring/alerting tooling.
