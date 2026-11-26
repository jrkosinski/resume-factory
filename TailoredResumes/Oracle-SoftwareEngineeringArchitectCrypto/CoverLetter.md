John R. Kosinski
john.kosinski@toptal.com

July 31, 2026

Hiring Manager
Oracle

---

The Software Engineering Architect role in OCI Crypto is a strong fit for someone who has spent the past decade designing and operating security-critical systems where cryptographic access control, key management, and distributed system correctness are the first design constraints, not afterthoughts.

OCI Crypto sits beneath everything else: authentication, authorization, KMS, PKI, secrets, and service-to-service trust are the foundational layer that OCI services and enterprise customers depend on for their security posture. That is exactly the kind of system I find most technically interesting, because there is no room to defer hard problems about invariants, failure modes, or privilege separation. The posting's emphasis on Tier 0 services, cross-region/realm resilience, and modernizing foundational cryptographic services into operationally simpler architectures reflects the same class of constraints I have worked under in production financial systems, where an architectural failure in access control or key management has direct, irreversible capital consequences.

The most relevant work I can point to is Stream Finance, where I served as principal architect for a production on-chain investment protocol backed by US Treasury bonds. I designed a layered access control architecture using a standalone SecurityManager contract over OpenZeppelin RBAC, with fine-grained role separation between upgrade authority, rate/yield authority, minting, burning, pausing, and lifecycle management; AWS KMS for signing and data encryption; AWS Secrets Manager for key storage; Step Functions human-approval gates before high-risk transactions; and immutable S3 audit logs. I also designed Echidna invariant campaigns specifically targeting access control properties: value conservation, admin-role survivability, role-safety boundaries, whitelist enforcement, and proxy upgrade authorization. That system secured hundreds of millions USD in TVL at peak. At Hamza, I designed key storage architecture for a production multi-chain payment processor, including per-payment key isolation and operational separation between key management and payment execution layers. Across both, the guiding principle was the same as what the OCI Crypto role describes: design for correctness and security invariants first, then build for availability and scale.

I would welcome the chance to discuss the role and how my background maps to what you are building.

Sincerely,
John R. Kosinski
