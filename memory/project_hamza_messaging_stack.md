---
name: Hamza messaging stack correction
description: Confirmed that Hamza used EventBridge + SQS in production, not RabbitMQ (which was an earlier architectural proposal)
type: project
---

The Hamza platform's production messaging stack used **AWS EventBridge and SQS**, not RabbitMQ. RabbitMQ was an earlier proposed design that did not make it to production.

**Why:** The evidence files originally listed RabbitMQ as confirmed and flagged EventBridge/SQS under "Use With Care" — this is now resolved. User confirmed EventBridge + SQS were the actual implementation and updated the docs accordingly.

**How to apply:** When describing Hamza's architecture — in resume bullets, interview prep, or technical descriptions — use EventBridge + SQS for messaging. Do not cite RabbitMQ as a Hamza technology. SQS consumers ran as Kubernetes Deployments doing long-poll; EventBridge handled routing as a fully managed AWS service with no in-cluster component.
