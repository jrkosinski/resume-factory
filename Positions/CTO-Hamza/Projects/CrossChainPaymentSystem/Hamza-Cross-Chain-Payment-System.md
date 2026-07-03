<!--
Source: split from Hamza-CTO.md master evidence-bank entry.
Purpose: modular resume source file, not a finished resume section.
Generated: 2026-07-01
-->
# Hamza / Cross-Chain Crypto Payment System

## Basic Info

**Company:** Hamza  
**Dates:** Approx. January 2024 – January 2026  
**Role / Title:** CTO and Co-Founder / Payment System Architect  
**Status:** Fully built and in use in production  
**Primary Domain:** Crypto payments, cross-chain settlement, fintech infrastructure, wallet-based checkout, event-driven payment processing  
**Supported Networks:** Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, other EVM L2s  
**Built but Not Deployed:** Solana  
**Primary Stack:** NestJS, TypeScript, PostgreSQL, TypeORM, DynamoDB, EventBridge and SQS, AWS, Kubernetes, Ethers.js v6, `@solana/web3.js`, `bitcoinjs-lib`, LiFi, Solidity, Foundry

## Canonical Summary

Architected and helped deliver Hamza’s production cross-chain crypto payment system, allowing buyers to pay from multiple networks while settling canonical marketplace escrow state on Optimism. The system used payment intents, payment-specific holding wallets / one-time deposit addresses, chain listeners, EventBridge and SQS event processing, idempotent verification, payment state-machine processing, immediate Optimism escrow settlement, merchant webhooks, and LiFi-based batch settlement to replenish settlement liquidity.

Newer architecture details describe a payment platform built around NestJS microservices, a shared pnpm monorepo/common package, HD wallet address derivation using BIP32/BIP39, EVM/Solana/Bitcoin chain support via Ethers.js v6, `@solana/web3.js`, and `bitcoinjs-lib`, PostgreSQL/TypeORM payment records, DynamoDB address metadata, Secrets Manager/KMS key storage, and a payment lifecycle state machine progressing through WAITING, PARTIAL, RECEIVED, IN_ESCROW, and terminal settled/expired/failed states.

## Short Resume Summary Version

Architected and delivered a production cross-chain crypto payment system for Hamza using payment intents, one-time payment holding wallets, chain listeners, EventBridge and SQS event processing, idempotent verification, Optimism escrow settlement, merchant webhooks, LiFi replenishment, NestJS services, EVM/Bitcoin/Solana chain tooling, and payment state-machine processing.

## Primary Tags

* Crypto checkout
* Cross-chain payments
* Multi-chain payments
* Payment processing
* Payment intents
* Payment state machine
* Payment verification
* Idempotency
* Escrow settlement
* Merchant webhooks
* Settlement architecture
* LiFi
* Liquidity management
* Master wallet
* Holding wallets
* One-time deposit addresses
* HD wallets
* BIP32
* BIP39
* Deferred settlement
* Bitcoin payments
* EVM L2 payments
* Solana payments built but not deployed
* Transaction monitoring
* Chain listeners
* Chain polling
* Partial payments
* Expired payments
* Failed payments
* EventBridge
* SQS
* NestJS
* TypeScript
* PostgreSQL
* TypeORM
* DynamoDB
* Secrets Manager
* KMS
* Ethers.js v6
* @solana/web3.js
* bitcoinjs-lib
* pnpm monorepo
* Shared common package
* Sweeper contract
* EventBridge reference architecture
* SQS reference architecture
* Step Functions reference architecture

## Problem

Hamza originally required users to pay on Optimism. This simplified early settlement because the payment network and escrow network were the same, but it created adoption friction.

Limitations of the Optimism-only model:

* Buyers had to move funds to Optimism.
* Users wanted Arbitrum, Bitcoin, and other chains.
* Deploying escrow contracts to every EVM L2 would fragment settlement state.
* Non-EVM support such as Bitcoin or Solana would not fit cleanly into a pure contract-per-chain model.

The implemented solution was to support payments on many networks while settling canonical marketplace escrow state on Optimism. This avoided the need to deploy escrow contracts to every L2 and allowed support for non-EVM chains such as Bitcoin. Solana support was also built, though never deployed.

## Production Status

The cross-chain payment system was fully built and in use.

Supported payment networks included:

* Optimism.
* Arbitrum.
* Bitcoin.
* Ethereum mainnet.
* Polygon.
* Mantle.
* Scroll.
* Other EVM L2s.

Built but not deployed:

* Solana.

LiFi integration was implemented.

## Payment Intent Model

Hamza Payments used a payment-intent model.

A client or storefront submitted a payment intent specifying:

* Receiver.
* Token.
* Payment amount.
* Payment chain/network.
* Order details.
* Seller details.
* Buyer/payment context.
* Target escrow contract or settlement target.
* Unique holding wallet / destination address.

Each unique payment intent received a dedicated one-time deposit address or holding wallet on the selected chain. That address contained only that payment, making payment matching simpler and reducing ambiguity.

Newer architecture details describe these addresses as being derived from an HD wallet using BIP32/BIP39, with chain-specific address generation for EVM, Solana, and Bitcoin.

Potential resume phrasing:

> Designed a multi-chain payment-intent system that generated a unique one-time deposit address per checkout, simplifying transaction matching, idempotent verification, and downstream escrow settlement.

## Payment Lifecycle / State Machine

The payment processor advanced each payment through a defined lifecycle.

Known or described states included:

* `WAITING` — intent created and deposit address provisioned, but no payment detected yet.
* `PARTIAL` — some funds detected, but less than the expected amount.
* `RECEIVED` — full expected payment detected and verified.
* `IN_ESCROW` — payment accepted and escrow deposit transaction in progress or completed against the target escrow contract.
* Settled / terminal completed state.
* Expired path for payments not completed within the expected time window.
* Failed path for settlement, verification, or transaction failures.

Potential resume phrasing:

> Modeled crypto checkout as a payment state machine covering waiting, partial payment, received, escrow-settlement, settled, expired, and failed paths.

## Service Architecture

The backend was structured as independent NestJS microservices coordinated through a shared `common` package.

### `address-store`

Responsibilities:

* Generated and persisted wallet/address material.
* Derived one-time deposit addresses using HD wallet patterns.
* Used AWS Secrets Manager in production for key material.
* Used PostgreSQL/TypeORM for address metadata in one architecture description.
* Used DynamoDB for address metadata in the AWS reference architecture.
* Exposed an internal API used by other services to provision deposit addresses.
TODO: what encryption? 

### `payment-processor`

Responsibilities:

* Central payment engine.
* Created and persisted payment intents and payment records.
* Called address-store to provision deposit addresses.
* Polled or monitored multiple chains for incoming transactions.
* Used Ethers.js v6 for EVM chains.
* Used `@solana/web3.js` for Solana support.
* Used `bitcoinjs-lib` for Bitcoin support.
* Managed payment state in PostgreSQL.
* Verified amount sufficiency, chain correctness, and idempotency.
* Executed on-chain escrow deposit / sweep transactions after settlement conditions were met.

TODO: if these services had to call each other, but were spun up dynamically, how did they know about each other?

### `payment-admin-api`

Responsibilities:

* Provided management and reporting endpoints for the admin dashboard.
* Was backed by DynamoDB in the new architecture notes for scale-oriented reporting/address lookups.
* Exposed payment status, lifecycle, and operational views to administrators.

The on-chain escrow and settlement logic lived in Solidity contracts managed with Foundry, including a Sweeper contract for fund movement.

Potential resume phrasing:

> Architected Hamza Payments as a set of NestJS microservices, including address-store, payment-processor, and payment-admin-api services, coordinated through a shared pnpm monorepo package for payment models, chain helpers, contract ABIs, repositories, and structured event logging.

## Monorepo / Shared Common Package

The codebase was structured as a pnpm monorepo.

The shared `common` package provided:

* `PaymentIntent` model.
* `PaymentRecord` model.
* `PaymentStatus` enums.
* Chain helper utilities.
* Contract ABIs.
* Repository abstractions.
* Structured event logging.
* Shared cross-service types and utilities.

This reduced duplication and kept services consistent around payment lifecycle, chain handling, contract calls, and domain events.

Potential resume phrasing:

> Structured a pnpm monorepo around a shared common package containing payment models, status enums, chain helpers, contract ABIs, repository abstractions, and structured event logging for consistency across payment microservices.

## Event-Driven Payment Flow

The production Hamza payment system was event-driven.

Listeners on supported chains watched for incoming payments and triggered downstream processing through an event-driven backend architecture using EventBridge and SQS in the confirmed production source.

```text
Buyer submits payment intent
        ↓
System creates dedicated payment holding wallet / one-time deposit address
        ↓
Buyer sends payment on selected chain
        ↓
Chain listener detects incoming payment
        ↓
Event enters payment-processing pipeline
        ↓
Payment is verified against registered intent
        ↓
System checks amount sufficiency, chain correctness, and validity
        ↓
Record is marked for idempotency
        ↓
Settlement / sweep transaction moves value into escrow path
        ↓
Optimism master wallet settles payment into canonical escrow where applicable
        ↓
Merchant/storefront callback fires via webhook
        ↓
Holding-wallet funds are later batch-settled through LiFi where applicable
        ↓
Optimism master wallet is replenished
```
TODO: describe inbox/outbox pattern

Potential resume phrasing:

> Designed event-driven payment infrastructure where chain listeners detected source-chain payments, backend services verified payment-intent state idempotently, escrow settlement proceeded automatically, and merchant callbacks completed the checkout flow.

## Chain Monitoring

The newer architecture describes chain monitoring using per-chain polling workers or scheduled AWS Lambda functions:

* EVM monitoring through Ethers.js v6.
* Solana monitoring through `@solana/web3.js`.
* Bitcoin monitoring through `bitcoinjs-lib` and Bitcoin transaction/address logic.

Detected funds emitted domain events such as:

* `payment.funds_detected`.
* `payment.received`.
* `payment.failed`.
* `payment.settled`.

TODO: describe DLQ

Production-specific implementation details should be clarified before claiming all monitoring was Lambda-based; the confirmed source says chain listeners and EventBridge were used.

## Immediate Escrow Settlement / Deferred Replenishment

When payment was verified on the source chain, the system settled immediately into the Optimism escrow contract by moving funds from a master wallet on Optimism into escrow on behalf of the user, product, and seller.

Later, in batches, funds from the source chain’s holding wallets were bridged/swapped back into the Optimism master wallet using LiFi. This completed the settlement loop and refilled Optimism liquidity.

This separated buyer payment acceptance from final liquidity replenishment, allowing marketplace workflows to proceed without waiting for every cross-chain settlement step to complete synchronously.

The newer architecture also describes a Sweeper contract and an autonomous sweep/deposit process for moving funds into designated escrow contracts after the expected amount is received.

Potential resume phrasing:

> Designed deferred cross-chain settlement where verified source-chain payments triggered immediate canonical Optimism escrow settlement, while holding-wallet funds were later batch-bridged through LiFi to replenish settlement liquidity.

## Idempotency

Idempotency was a key design concern.

The system verified:

* Whether the payment belonged to a valid payment intent.
* Whether the payment amount was sufficient.
* Whether the payment had already been processed.
* Whether the payment was on the expected chain/network.
* Whether downstream settlement should proceed.
* Whether webhook callbacks or escrow settlement had already been completed.

Records were marked to prevent duplicate processing before escrow settlement and merchant callback workflows completed.

Potential resume phrasing:

> Built idempotent payment verification and settlement workflows to prevent duplicate processing across chain detection, escrow settlement, and merchant callback delivery.

## Custody Wording Note

The system was not a user-balance custody system. Holding wallets were used as payment-specific settlement infrastructure, and private keys were securely stored and encrypted in DynamoDB or Secrets Manager/KMS depending on the architecture/version.

Safer external phrasing:

> Designed the system so each completed checkout used a dedicated payment holding wallet for payment isolation and settlement, with funds treated as completed payment funds after verification rather than as ongoing user balances.

Avoid overstating:

> “Fully non-custodial.”

Better resume phrasing:

> Built a payment-specific holding-wallet settlement model with secure key storage, event-driven verification, idempotent processing, and automated escrow settlement.

## Admin Dashboard / Frontend Architecture

The newer payment-admin frontend was described as a React 19 application using:

* Vite.
* TanStack Router.
* TanStack Query.
* Radix UI.
* Tailwind CSS.

The dashboard gave operators visibility into:

* Payment status.
* Payment lifecycle events.
* Management/reporting data.
* Deposit address activity.
* Settlement progress.
* Failed or expired payments.
* Operational status for payment processing.

Potential resume phrasing:

> Built or led a React/Vite/TanStack/Radix/Tailwind admin dashboard providing operators with real-time visibility into payment status, lifecycle events, reporting, and settlement progress.

## Target / Reference AWS Event-Driven Architecture

The new architecture notes describe a natural AWS implementation using EventBridge-centered event routing, SQS queue buffering, EKS, scheduled chain-polling Lambdas, and Step Functions settlement orchestration.

Treat this as a target/reference architecture unless confirmed as the exact production deployment.

```text
Client
  └─► API Gateway
        └─► ECS: payment-processor ──────────► Aurora Serverless v2 / PostgreSQL
                    │
                    └─► EventBridge custom bus
                              │
              ┌───────────────┼──────────────────────┐
              ▼               ▼                      ▼
        SQS → ECS:      EventBridge              SQS → Step Functions
        address-store   Scheduled Rules          Settlement Orchestrator
              │         Chain polling                  │
              ▼               │                         ▼
        Secrets Manager       └─► Lambda          On-chain Escrow
        KMS-encrypted             EVM/Solana/BTC  Smart Contract
        DynamoDB metadata              │
                                       └─► EventBridge bus
                                                        │
                                              payment-processor
                                              updates payment state

Frontend: S3 + CloudFront
  └─► Cognito admin auth
  └─► API Gateway → ECS: payment-admin-api
                              ├─► Aurora / PostgreSQL
                              ├─► DynamoDB
                              └─► ElastiCache Redis ◄── DynamoDB Streams → Lambda
```

### Target / Reference AWS Service Roles

| Service | Role |
|---|---|
| API Gateway | Public ingress for payment intent creation and admin API |
| EKS | Containerized NestJS services: payment-processor, address-store, payment-admin-api |
| EventBridge | Central domain-event bus for payment lifecycle events |
| SQS | Queue buffering between EventBridge and consumers; DLQs for failed events |
| Lambda | Chain polling, DynamoDB stream projections, DLQ alerting |
| Step Functions | Multi-step escrow settlement orchestration with retry and audit trail |
| Aurora Serverless v2 | PostgreSQL for payment records and payment intents |
| DynamoDB | Address metadata and high-throughput key-value lookups |
| ElastiCache Redis | Read cache for dashboard real-time payment status |
| Secrets Manager + KMS | Encrypted HD wallet key storage and key access control |
| S3 + CloudFront | Static hosting for admin dashboard |
| Cognito | Admin authentication |
| CloudWatch + X-Ray | Logs, metrics, distributed tracing, and correlation-based lifecycle reconstruction |
| SNS | Operator alerting for DLQs and settlement failures |
| VPC private subnets | Network isolation for ECS services and data stores |
| ALB | Internal service load balancing |

### Architectural Properties

**Decoupling:** Address provisioning, chain monitoring, payment verification, and escrow settlement can scale and fail independently.

**Observability:** Domain events carry a correlation ID, ideally the payment intent ID, across services, queues, Lambdas, and settlement executions.

**Extensibility:** Adding a new chain mainly requires a new address generator, chain listener/polling worker, chain-specific verification logic, and settlement integration.

**Resilience:** SQS DLQs capture failed processing. Step Functions can retry settlement actions with exponential backoff. Idempotency prevents duplicate settlement or callback effects.

**Security:** Key material is isolated in Secrets Manager/KMS or encrypted storage. Non-address-store services should interact with addresses and payment records rather than raw private keys.

Potential resume phrasing:

> Designed an AWS event-driven payment architecture using EventBridge, SQS, EKS, Lambda chain pollers, Step Functions settlement orchestration, Aurora PostgreSQL, DynamoDB, Secrets Manager/KMS, CloudWatch/X-Ray tracing, and CloudFront/Cognito dashboard delivery.

# Bullet Bank

## Cross-Chain / Crypto Payments Bullets

* Designed and delivered a production cross-chain crypto payment system supporting Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, and other L2s.

* Built payment flows using uniquely identifiable payment intents, dedicated per-payment holding wallets, chain listeners, EventBridge and SQS event processing, idempotent verification, immediate Optimism escrow settlement, merchant webhooks, and LiFi-based batch settlement.

* Designed a payment architecture that allowed Hamza to accept payments across multiple networks without deploying escrow contracts to every supported chain.

* Built Solana payment support for the cross-chain payment system, though it was not deployed in production.

* Implemented LiFi-based settlement to batch-settle source-chain holding-wallet funds back into the Optimism master wallet and replenish escrow settlement liquidity.

* Designed payment-intent workflows that generated a unique one-time deposit address per checkout using HD-wallet architecture, improving transaction matching and reducing ambiguity across multi-chain payments.

* Modeled the payment lifecycle as a state machine covering waiting, partial payment, received, in-escrow, settled, expired, and failed paths.

* Built or designed chain monitoring across EVM, Solana, and Bitcoin flows using Ethers.js v6, `@solana/web3.js`, and `bitcoinjs-lib`.

* Designed automated escrow-sweep workflows using Solidity contracts and payment-processor settlement logic to move verified funds into designated escrow flows.

## Backend / Infrastructure Bullets

* Designed event-driven backend workflows for cross-chain payment detection, verification, idempotency, escrow settlement, webhook delivery, and liquidity replenishment.

* Structured the payment backend as NestJS microservices, including address-store, payment-processor, and payment-admin-api services coordinated through a shared pnpm monorepo common package.

* Designed shared backend primitives for payment intents, payment records, payment status enums, chain helpers, contract ABIs, repository abstractions, and structured event logging.

* Designed a target AWS event-driven architecture using EventBridge, SQS, EKS, Lambda chain pollers, Step Functions settlement orchestration, Aurora PostgreSQL, DynamoDB, Secrets Manager/KMS, CloudWatch/X-Ray, and SNS alerting.

* Designed secure key/address infrastructure using HD-wallet-derived deposit addresses, encrypted key storage, strict IAM boundaries, and service-level separation between address provisioning and payment processing.

## Fintech / Payment Bullets

* Designed an idempotent crypto payment and settlement system supporting payment intents, payment-specific holding wallets, source-chain monitoring, amount verification, escrow settlement, and merchant callbacks.

* Architected deferred cross-chain settlement where verified payments on external chains immediately triggered Optimism escrow settlement, while source-chain funds were batch-settled later through LiFi.

* Built payment infrastructure processing ~$5k–$10k USD monthly throughput across a live marketplace with hundreds of monthly users and 20+ sellers.

* Built a payment state-machine model covering waiting, partial payment, full receipt, escrow settlement, terminal settlement, expiration, and failure cases.

* Designed one-time deposit address workflows using HD-wallet architecture for EVM, Bitcoin, and built-but-not-deployed Solana payment support.

* Designed observability around payment lifecycle events using structured event logging and correlation IDs to reconstruct a payment from intent creation through escrow settlement.

# Strongest Resume Angles

## Fintech / Payments Roles

Emphasize:

* Cross-chain payments.
* Multi-chain crypto checkout.
* Bitcoin + EVM L2 payments.
* Solana payment support built but not deployed.
* Payment intents.
* One-time deposit addresses.
* HD wallets / BIP32 / BIP39.
* Holding wallets.
* Chain listeners.
* EventBridge and SQS.
* Event-driven processing.
* Payment state machines.
* Idempotency.
* LiFi settlement.
* Optimism master-wallet settlement.
* Escrow.
* Sweeper contract / automated fund movement.
* Webhooks.
* Ethers.js v6 / `@solana/web3.js` / `bitcoinjs-lib`.
* Secrets Manager / KMS key-storage architecture.
* EventBridge / SQS / Step Functions, if presenting AWS reference architecture.
* $5k–$10k monthly throughput.

## Backend / Distributed Systems Roles

Emphasize:

* Event-driven processing.
* Payment state transitions.
* Idempotency.
* Queue-based processing.
* Chain listeners.
* Microservice boundaries.
* Shared common package.
* Observability and correlation IDs.
* Secure key/address boundaries.
* Retry/failure states.

## Architecture Roles

Emphasize:

* Optimism canonical settlement.
* Avoiding escrow deployment on every chain.
* Separating payment acceptance from settlement liquidity replenishment.
* Service decomposition.
* Extensibility to new chains.
* Target/reference AWS architecture, qualified appropriately.

# ATS / Keyword Bank

Crypto checkout, cross-chain payments, multi-chain payments, payment processing, payment intents, payment state machine, payment verification, idempotency, escrow settlement, merchant webhooks, settlement architecture, LiFi, liquidity management, master wallet, holding wallets, one-time deposit addresses, HD wallets, BIP32, BIP39, deferred settlement, Bitcoin payments, EVM L2 payments, Solana payments, transaction monitoring, chain listeners, chain polling, partial payments, expired payments, failed payments, Step Functions settlement orchestration, EventBridge domain events, SQS queues, DLQs, correlation IDs, EventBridge, SQS, NestJS, TypeScript, TypeORM, PostgreSQL, DynamoDB, Secrets Manager, KMS, Ethers.js v6, `@solana/web3.js`, `bitcoinjs-lib`, AWS, Kubernetes.

# Future YAML Shape

```yaml
id: hamza_cross_chain_payment_system
type: startup_project
company: Hamza
role_title: CTO and Co-Founder / Payment System Architect
dates:
  start: 2024-01
  end: 2026-01
status:
  production: true
  cross_chain_payment_system_live: true
  lifi_integration_implemented: true
payment_system:
  original_chain: Optimism
  original_limitation: buyers_forced_onto_optimism
  solution: multi_chain_payment_acceptance_with_optimism_settlement
  payment_intents: true
  dedicated_holding_wallet_per_payment: true
  one_time_deposit_addresses: true
  hd_wallet_derivation: true
  bip32_bip39: true
  payment_state_machine:
    - WAITING
    - PARTIAL
    - RECEIVED
    - IN_ESCROW
    - settled
    - expired
    - failed
  chain_listeners: true
  event_bridge: true
  sqs: true
  idempotency: true
  merchant_webhooks: true
  immediate_escrow_settlement_from_optimism_master_wallet: true
  batch_replenishment_via_lifi: true
  sweeper_contract_or_fund_movement_contract: true
  services:
    address_store:
      responsibilities:
        - address_generation
        - key_material_storage
        - address_metadata
        - internal_address_provisioning_api
    payment_processor:
      responsibilities:
        - create_payment_intents
        - manage_payment_records
        - monitor_or_poll_chains
        - verify_payments
        - update_state_machine
        - execute_escrow_settlement
    payment_admin_api:
      responsibilities:
        - management_endpoints
        - reporting_endpoints
        - admin_dashboard_support
  live_or_supported_chains:
    - Optimism
    - Arbitrum
    - Bitcoin
    - Ethereum_mainnet
    - Polygon
    - Mantle
    - Scroll
    - other_EVM_L2s
  built_not_deployed:
    - Solana
aws_reference_architecture:
  status: target_or_reference_architecture_until_confirmed
  event_bus: EventBridge_custom_bus
  queues:
    - SQS
    - DLQ
  compute:
    - EKS
    - Lambda_chain_pollers
    - Step_Functions_settlement_orchestrator
  data:
    - Aurora_Serverless_v2_PostgreSQL
    - DynamoDB_address_metadata
    - ElastiCache_Redis_dashboard_projection
  security:
    - Secrets_Manager
    - KMS
    - IAM_task_roles
    - VPC_private_subnets
    - Cognito_admin_auth
  observability:
    - CloudWatch
    - X_Ray
    - SNS_alerting
    - correlation_id_payment_intent_id
```

# Missing / Worth Clarifying Later

2. Whether address metadata lived in PostgreSQL/TypeORM, DynamoDB, or both in different service versions.
3. Whether Aurora Serverless v2 was deployed or is only a proposed AWS target architecture.
5. Whether chain monitoring was implemented as long-running listeners, scheduled Lambda pollers, or both.
6. Whether Step Functions settlement orchestration was implemented or belongs to the AWS architecture design.
7. Whether the React 19/TanStack/Radix/Tailwind admin dashboard was live, prototype, or target rebuild.
8. Whether the Sweeper contract was deployed and used in production, and how it related to the Optimism escrow/master-wallet settlement path.
9. Whether HD wallet derivation generated all one-time deposit addresses in production across EVM/Bitcoin/Solana, or only for some chains.
10. Exact key-storage approach: AWS Secrets Manager, DynamoDB encrypted private keys, KMS envelope encryption, or staged migration between them.
11. Whether payment states were exactly `WAITING`, `PARTIAL`, `RECEIVED`, `IN_ESCROW`, and `settled`, or whether these are normalized names from later architecture.
12. Payment expiration behavior: timeout duration, refund/cancel handling, partial-payment policy, and manual override paths.

# External Claim Safety Notes

## Safe to Claim Now

* Cross-chain payment system fully built and in use.
* Payment intents, per-payment holding wallets, chain listeners, idempotent verification, immediate Optimism escrow settlement, merchant callbacks, and LiFi replenishment.
* Supported Optimism, Arbitrum, Bitcoin, Ethereum mainnet, Polygon, Mantle, Scroll, and other EVM L2s.
* Solana payment support built but not deployed.

## Use With Care / Qualify Internally

* HD wallet / BIP32/BIP39 production scope across all chains.
* EventBridge/SQS/Step Functions/Aurora/Lambda architecture as implemented production infrastructure.
* Secrets Manager/KMS versus DynamoDB-encrypted key storage.
* DynamoDB versus PostgreSQL address metadata.
* Lambda polling versus persistent listener architecture.
* Sweeper contract production usage.

## Avoid Unless Confirmed

* Claiming the full EventBridge-centered AWS architecture was live production.
* Claiming Aurora Serverless v2, Step Functions, X-Ray, Cognito, or ElastiCache were deployed if they were only architectural recommendations.
* Claiming fully non-custodial payment handling.
* Claiming exact volume, uptime, failure rates, or number of processed payment intents.
