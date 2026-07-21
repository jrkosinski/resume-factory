# Garbles Labs / Orca Whirlpools .NET SDK Port

## Basic Info

**Client / Employer:** Garbles Labs
**Product:** Orca Whirlpools .NET SDK (community open-source)
**Domain:** Blockchain, Solana, DeFi, AMM, SDK development, Unity game engine, open-source
**Role / Title:** Blockchain / SDK Developer (exact title to be confirmed)
**Dates:** 2022 (short engagement)
**Ownership:** Primary developer — full SDK port, testing, and Rust contract modification
**Status:** Completed; released as open-source for community use
**Primary Stack:** C#, .NET, Unity, Solana, Rust
**Ecosystem:** Orca Whirlpools (Solana AMM / market maker)

---

## Canonical Summary

Short engagement in 2022 for Garbles Labs, porting the TypeScript SDK for Orca Whirlpools — a well-known automated market maker (AMM) and market maker on the Solana blockchain — to C#/.NET for use in the Unity game engine. The SDK was released open-source for community use. Work included developing and refactoring the SDK for .NET, building a suite of automated tests to ensure quality, and interfacing with the Orca Whirlpools Rust smart contracts — modifying the Rust code as needed to support testability.

---

## Short Resume Summary Version

Ported the Orca Whirlpools TypeScript SDK to C#/.NET for the Unity game engine (Garbles Labs, 2022), releasing the SDK open-source; built automated test coverage and modified Orca's Rust smart contracts as needed for testability.

---

## Primary Tags

* Solana
* Orca Whirlpools
* AMM
* DeFi
* SDK development
* SDK port
* TypeScript to C# port
* C#
* .NET
* Unity
* GameFi
* Blockchain gaming
* Rust
* Smart contracts
* Open-source
* Community SDK
* Automated testing
* Cross-language port

---

## Context

Orca is one of the most widely used decentralized exchanges (DEX) and automated market makers on the Solana blockchain. Its Whirlpools product is a concentrated liquidity AMM — the same model popularized by Uniswap v3 on Ethereum — and is a significant piece of Solana DeFi infrastructure. Orca provides an official TypeScript SDK for interacting with Whirlpools programmatically.

Garbles Labs needed a C#/.NET version of this SDK to enable Unity game developers to integrate Orca Whirlpools liquidity and trading functionality into games — bridging DeFi infrastructure and the gaming ecosystem. The resulting SDK was made open-source and available to the broader community, not just internal use.

The Whirlpools protocol is implemented as Rust smart contracts on Solana. Interfacing with and modifying these contracts for testability was part of the engagement, requiring working knowledge of Rust and Solana's smart contract model.

---

## Role and Ownership

Primary developer for the Orca Whirlpools .NET SDK port.

Owned:

* Full port of the Orca Whirlpools TypeScript SDK to C#/.NET
* Refactoring of SDK code as needed for the .NET environment
* Automated test suite for the .NET SDK
* Rust smart contract interfacing and modification for testability
* Open-source release for community use

---

## Technical Work

### TypeScript → C#/.NET SDK Port

Ported the official Orca Whirlpools TypeScript SDK to C#/.NET. This required translating TypeScript idioms, async patterns, and Solana client interaction patterns into idiomatic C# .NET equivalents, while preserving the SDK's functional surface area. Refactored code as necessary to fit .NET conventions and the Unity game engine runtime environment.

### Unity Integration Target

The primary consumer of the SDK was the Unity game engine — meaning the .NET implementation needed to be compatible with Unity's version of the .NET runtime (which has specific constraints compared to standard .NET). This shaped architectural and compatibility decisions throughout the SDK development.

### Automated Testing

Built a suite of automated tests to ensure SDK quality — validating that the ported C# SDK behavior was correct relative to the TypeScript original and against the live Solana/Orca Whirlpools contracts.

### Rust Smart Contract Work

Interfaced directly with the Orca Whirlpools Rust smart contracts on Solana. Modified the Rust contract code as needed to support testability — likely involving test harness setup, program modifications for local validator testing, or instrumentation that enabled the .NET SDK tests to run reliably against the contract logic.

### Open-Source Community Release

The completed SDK was made open-source and published for community use — available to any Unity developer wanting to integrate Orca Whirlpools into a game or GameFi product.

---

# Bullet Bank

## Strong General Bullets

* Ported the Orca Whirlpools TypeScript SDK to C#/.NET for the Unity game engine (Garbles Labs, 2022), releasing the SDK open-source for community use.

* Developed and refactored the Orca Whirlpools .NET SDK from a TypeScript original, built a full automated test suite, and modified the underlying Rust smart contracts as needed for testability.

* Bridged Solana DeFi infrastructure (Orca Whirlpools AMM) and the Unity game engine ecosystem by delivering a community-available C#/.NET SDK.

---

## Blockchain / Solana Bullets

* Ported the Orca Whirlpools SDK from TypeScript to C#/.NET, enabling Unity game developers to integrate one of Solana's leading concentrated liquidity AMMs into games.

* Interfaced with Orca Whirlpools' Rust smart contracts on Solana and modified Rust code as needed to support SDK testability.

* Delivered a Solana DeFi SDK in C#/.NET targeting the Unity runtime — bridging blockchain and gaming ecosystems for community use.

---

## SDK / Developer Tools Bullets

* Built a production-quality C#/.NET SDK port of the Orca Whirlpools TypeScript SDK, including refactoring for .NET idioms and a full automated test suite.

* Released an open-source Solana AMM SDK for Unity developers, expanding DeFi developer tooling to the game development community.

---

## Rust Bullets

* Modified Orca Whirlpools Rust smart contract code to support testability as part of the .NET SDK port, working across both C# and Rust within the same engagement.

---

## GameFi / Unity Bullets

* Targeted the Unity game engine runtime as the primary consumer of the .NET SDK, shaping architecture and compatibility decisions to fit Unity's .NET constraints.

* Enabled Unity game developers to interact with Orca Whirlpools — Solana's leading AMM — through an open-source C# SDK built for the gaming ecosystem.

---

# Strongest Resume Angles

## Blockchain / Web3 / Solana Roles

Emphasize:

* Solana ecosystem
* Orca Whirlpools (recognizable Solana DeFi brand)
* AMM / concentrated liquidity domain
* Rust smart contract work
* SDK development for DeFi protocols
* Open-source contribution

Strong signal for Solana-native roles — direct protocol-level work, not just consumer dApp development.

---

## SDK / Developer Tooling Roles

Emphasize:

* Cross-language SDK port (TypeScript → C#)
* Developer-facing open-source release
* Test coverage for SDK quality
* Community adoption goal
* .NET runtime compatibility (Unity constraints)

---

## GameFi / Blockchain Gaming Roles

Emphasize:

* Unity game engine target
* DeFi-to-gaming bridge
* Solana AMM integrated with game ecosystem
* Open-source for game developer community
* C#/.NET in a Unity context

Pairs well with Soundbeats (Sui GameFi) to demonstrate breadth across gaming + blockchain.

---

## Open-Source / Community Roles

Emphasize:

* Open-source SDK release
* Community availability
* Developer tooling for an underserved niche (Unity + Solana DeFi)

---

# ATS / Keyword Bank

## Blockchain / DeFi Keywords

Solana, Orca, Orca Whirlpools, AMM, automated market maker, concentrated liquidity, DeFi, decentralized exchange, DEX, Rust, Solana smart contracts, Anchor, Web3, blockchain gaming, GameFi.

## SDK / Engineering Keywords

SDK development, SDK port, TypeScript to C#, cross-language port, .NET SDK, open-source SDK, developer tooling, automated testing, test suite, SDK quality, refactoring.

## Gaming / Unity Keywords

Unity, Unity game engine, C#, .NET, GameFi, blockchain gaming, game developer SDK, Unity runtime, Solana Unity SDK.

---

# External Claim Safety Notes

## Safe to Claim

* Ported Orca Whirlpools TypeScript SDK to C#/.NET for Garbles Labs, 2022
* Target platform: Unity game engine
* Released open-source for community use
* Developed and refactored the .NET SDK
* Added automated test suite
* Interfaced with and modified Orca Whirlpools Rust smart contracts for testability
* Technologies: C#, .NET, Solana, Orca Whirlpools, Unity, Rust

## Use With Care

* "Orca Whirlpools" is a real, well-known protocol — confirm the open-source SDK is publicly findable if asked to point to it
* Rust smart contract modification claims — accurate but narrow; frame as "modified for testability" rather than implying broader contract authorship

## Avoid Unless Confirmed

* Number of community users or SDK downloads
* Whether the SDK is still maintained or actively used
* Any Orca team involvement or official endorsement of the port
* Specific concentrated liquidity math or AMM mechanics authored (vs. ported)

---

# Missing / Worth Clarifying

1. Is the open-source SDK publicly available (GitHub link)?
2. Was this freelance, consulting, or employment with Garbles Labs?
3. What testing framework was used for the .NET automated tests?
4. What specific Rust modifications were made — test validator setup, program instrumentation, test accounts, or other?
5. Did the SDK support the full Whirlpools API surface or a targeted subset?
6. Was the Unity runtime target Unity's .NET Standard 2.1 / IL2CPP, or a specific Unity version?
7. Has the SDK been used in any known games or GameFi projects?
8. Were there other developers involved, or was this a solo effort?
9. Any community traction — GitHub stars, forks, Discord mentions, etc.?
