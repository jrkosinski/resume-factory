<!--
Source: compiled 2026-11-26 from `/home/blanta/NOWY/projects/IdeaWise/ideawise-core/Projects/AgenticWorkflow/` (Project Summary, Workflow Design, Action Plan, History, TODO), `Projects/IdeaEngine/IEDV/Pre-sprint/IEDV-17: Sprint 1 Tickets Cold-Start Test/`, and the Idea Engine standup summaries of 23 to 25 November 2026.
Purpose: modular resume source file for the agentic Jira workflow John designed and built for the Idea Engine work group.
-->

# IdeaWise / Agentic Jira Workflow / Ticket to Vetted Result

## Basic Info

**Client:** IdeaWise (EU-based, ~140 employees)
**Project:** Agentic Workflow: how a team works when agents do most of the work, from a drafted Jira ticket to a vetted result, and where people step in. Code in `ops/jira-agentic-workflow` on the client's GitHub Enterprise. Not the Idea Engine's own repository, which is also called `agentic_workflow`
**Dates:** Designed 24 November 2026; built and run end to end 25 November 2026
**Role:** Sole designer and owner; built with Claude Code under John's direction
**Status:** Working system, built in two days; first live ticket taken through the whole loop and accepted; demonstrated to the work group on 25 November 2026

## Canonical Summary

Designed and built an agentic Jira workflow for the Idea Engine work group: agents pick tickets up, check them, hand codable work to a code factory, review the result against the acceptance criteria, and bring a person in only when one is needed. Every ticket passes a ready check (blockers done, prerequisites ready). Codable tickets are graded by an agent against 24 cold-start rules (could a fresh agent that sees only the ticket do the work without asking anyone?); a ticket that passes starts an unattended code-factory run, and one that fails goes back to its assignee with the agent's questions. A second agent reviews every finished ticket against its acceptance criteria; a ticket its writer marked for human review waits for a person, the rest move on automatically. People hear from it as direct messages on Mattermost, and every notification, stop, question and answer is logged.

The first live ticket (ANT-1277) went through the whole loop: the doable check, a factory run that committed the change with green CI, merge, and an agent review that passed it 3 of 3 and moved it to Accepted.

## Short Resume Summary Version

Designed and built an agentic Jira workflow in which agents check each ticket's readiness against 24 cold-start rules, hand codable work to an unattended code factory, review results against acceptance criteria, and notify a person on Mattermost only when one is needed. Took the first live ticket through the whole loop, from intake to merged, reviewed and accepted.

## Compact Resume Version

Designed and built an agentic Jira workflow: agent readiness check, hand-off to an unattended code factory, agent review against acceptance criteria, and Mattermost notifications only when a person is needed; first live ticket taken end to end.

## Primary Tags

- Agentic workflow
- AI agents in Jira
- Ticket readiness and cold-start testing
- Agent-doable ticket criteria
- Human-in-the-loop design
- Acceptance-criteria review agent
- Code factory integration
- Claude Code headless agents
- Mattermost bot integration
- Agentic team operating model

## Context, Role and Ownership

At the 24 November 2026 standup André said a team of this size already moved slower than one person driving alone, and asked for two days to set up how the group would work when agents do most of the work. John proposed a design that day, vetted it the same day (eight gaps, seven settled), and built it the next.

The doable check came first. On 23 November John had six Sprint 1 tickets tested by hand (IEDV-17): fresh agents got only the ticket text and the 24 readiness rules from André's Critical Path, and listed what they would have to ask; the questions were sorted into gaps in the ticket, open blockers and background, and each ticket was graded and the result posted to Jira. Most tickets took three or four rounds. That method became the workflow's first agent.

John's concrete responsibilities:

- Designed the workflow: two kinds of ticket (codable to a factory, non-codable to a person working with Claude), the assignee always a person, done meaning the pull request is merged, mixed tickets split, a stop policy (failed review returns to the factory for up to two rounds, then to the assignee; no answer gets one reminder after four working hours, then the ticket shows as blocked), and everything logged.
- Ran the hand-tested cold-start trial that defined the doable check.
- Directed the build: a small Python script, one config file, one prompt file per agent, each agent a Claude Code headless run; hourly on a schedule with a manual run and an off switch; Jira under his account with every comment marked as the workflow's, Mattermost through a bot; staged testing (dry run, his own tickets, then the open sprint) on labeled tickets only.
- Wired it to his code factory: a codable ticket that passes the doable check starts an unattended factory run behind the factory's own gate; a merge moves the ticket to review, a stop tells the assignee and returns the ticket to To Do.
- Took ANT-1277 through the loop and fixed what the run turned up: the factory's merge check, a ticket sent to the factory twice, intake trusting a lagging search, and the merge comment missing the diff the review agent needed.

## Bullet Bank

### General AI transformation, resume summary

- Designed and built an agentic Jira workflow that lets agents carry a ticket from intake to a reviewed, merged result, bringing people in only where they add value.
- Turned "is this ticket ready for an agent?" into a test: fresh agents see only the ticket and 24 cold-start rules and list what they would have to ask, and only gaps in the ticket count against it.

### Agentic engineering, technical lead

- Built an agent pipeline in Jira: readiness check, cold-start doable check, hand-off to an unattended code factory, and an agent review of each result against its acceptance criteria, with Mattermost notifications for the assignee.
- Took the first live ticket through the whole loop (doable check, factory run with green CI, merge, agent review passing 3 of 3, Accepted) and fixed the four integration faults the run exposed.

### Head of engineering / delivery process angle

- Designed how a team works when agents do most of the work: which tickets go to agents, when a person is notified, how a stopped ticket restarts, and where human review sits.

## Best External Resume Versions

**Short block:**

> Designed and built an agentic Jira workflow for an AI product team: agents check each ticket against 24 cold-start rules, hand codable work to an unattended code factory, review the result against its acceptance criteria, and notify a person on Mattermost only when one is needed. Took the first live ticket end to end, from intake to merged, reviewed and accepted.

**One-liner:**

> Built an agentic Jira workflow: agent readiness check, unattended code-factory hand-off, agent review against acceptance criteria.

## External Claim Safety Notes

### Safe to Claim Now

- Sole design of the workflow, and its build under John's direction.
- The cold-start doable check and the hand-tested trial behind it.
- One live ticket through the whole loop, merged and accepted.
- Integration with John's own code factory and with Mattermost.

### Use With Care / Qualify Internally

- "Designed and built" is accurate: John designed it and directed the build with Claude Code.
- Present as a working system proven end to end on a live ticket, a new capability for the team.

### Avoid Unless Confirmed

- Naming the client or its people in external output.
- Inventing throughput, cycle-time or adoption figures.

## Primary Stack

Python, Claude Code headless (`claude -p`) agents with one prompt file each, YAML config, Jira REST API, Mattermost bot and webhooks, cron scheduling, GitHub Enterprise, John's local code factory (see `IdeaWise-Code-Factory.md`).
