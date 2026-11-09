# Beyond Lines of Code: Rethinking Developer Performance in the AI Era

*When code is cheap to produce, volume stops measuring performance. Here is how engineering managers can review engineers on difficulty-adjusted judgment, ownership, and quality instead.*

Every engineering manager eventually faces the same uncomfortable question about someone on their team: *is this person lazy, or are they unlucky?*

One engineer has had a quiet quarter. Few merged pull requests, long gaps between updates, a ticket that keeps slipping. Is that someone coasting, or someone wrestling with an ambiguous, high-risk problem that nobody else wanted? For years, managers answered this question with imperfect proxies: lines of code, commit counts, pull-request counts. These were always crude. In the age of AI-assisted development, they are worse than crude. They are actively misleading.

AI coding tools have changed the production function of software. Visible activity—diffs, commits, builds—has become cheap to generate. An engineer can now appear remarkably productive by pushing large volumes of machine-generated code, whether or not the underlying problem is being solved, and whether or not the cost of that code is being quietly handed to reviewers, security teams, and future maintainers.

This article argues that performance reviews need to be reinvented around observable, *difficulty-adjusted* contributions: how an engineer frames ambiguous problems, makes technical tradeoffs, reduces risk, unblocks others, and ships maintainable outcomes. The goal is emphatically not to audit people's prompts. It is to build a review system that rewards the things AI has not made cheap—judgment, ownership, and verification—and that handles the underperformance conversation fairly and with far less manager effort than it demands today.

## Why Volume Proxies Break Under AI-Assisted Development

### AI changes how much code a unit of effort produces

The evidence that AI accelerates visible output is substantial. In a controlled experiment, developers with access to GitHub Copilot completed a programming task about 55.8 percent faster. In real-world randomized trials across Microsoft, Accenture, and an anonymous Fortune 100 company, developers using the tool completed an estimated 26 percent more tasks, alongside increases in commits and builds.

The implication is simple but far-reaching. When the "output tokens" of engineering—code, diffs, commits—are cheaper to produce, they stop differentiating effort, judgment, or impact. Throughput goes up for everyone, and the signal that once separated the diligent from the disengaged is diluted.

### Activity metrics were always fragile

Developer-productivity research has long warned against the idea that productivity is simply about activity. Higher activity can signal effectiveness, but it can just as easily signal brute-forcing through poor systems or poor planning. Writing in the same vein, the chapter *No Single Metric Captures Productivity* describes lines-of-code measurement as "clearly fraught": it encourages gaming and fails to capture quality, maintainability, or the wide variety of valuable work developers do beyond writing code.

This is Goodhart's Law in its classic form: when a measure becomes a target, it ceases to be a good measure. Reward lines of code, and you will receive more lines of code. With AI, you will receive them in unprecedented quantities.

### Verification costs rise, and they are often invisible

AI also moves effort rather than eliminating it. Early field and usage research on Copilot found that developers can spend more time reviewing suggestions than writing code; their role shifts from doing the task to assessing proposals. And the assessment matters. Security research has found that a substantial fraction of AI-generated suggestions can be vulnerable in certain scenarios—roughly 40 percent in one Copilot security analysis—and user studies have found that developers using AI assistance may write less secure code while believing it is more secure.

The NIST generative-AI risk profile names the underlying pattern: automation bias and over-reliance. People tend to over-trust AI output and perceive it as higher quality than it is, which compounds risks such as confabulation and bias.

The managerial consequence is uncomfortable. If you continue to reward volume, you may be inadvertently rewarding the engineers who externalize their costs—to reviewers, to site-reliability engineers, to the security team, and to whoever maintains the code in two years.

## A Difficulty-Adjusted Performance Model

The practical replacement for volume metrics is not a single better number. It is a scorecard that makes the *difficulty* of the work explicit and then evaluates performance against observable dimensions. This follows established measurement practice: define the goals first, then the questions, then the metrics—the Goal–Question–Metric approach—rather than starting from whatever the tooling happens to count.

### Step one: normalize for difficulty

For each meaningful deliverable—a ticket, epic, incident, or project—assign a **difficulty band** using four observable factors.

**Ambiguity** captures unclear requirements, shifting scope, and discovery work. A clearly specified task sits low; one requiring major discovery sits high; an ill-defined research-and-development problem sits at the extreme.

**Dependencies** captures cross-team reliance, external approvals, and vendor or tool constraints. No dependencies is low; one or two known ones is medium; multiple or contested ones is high; and dependencies that are unowned or blocking sit at the extreme.

**Blast radius** captures the risk if the work is wrong—customer impact, security, compliance, reliability. A local change is low; a service-level change is medium; a multi-service change is high; and a platform-wide or production-wide change is extreme.

**Novelty** captures whether the work is routine or breaks new ground: a new domain, a new stack, a new architecture. Routine work is low; some new elements is medium; a new subsystem is high; and a first-of-its-kind effort is extreme.

None of this requires perfection. What it requires is consistency and transparency, so that an unlucky hard problem is not evaluated as though it were routine work with AI autocomplete. The band exists to answer the manager's original question fairly: before asking whether someone delivered less, ask how hard the thing was.

### Step two: evaluate five dimensions that remain meaningful when code is cheap

Within a difficulty band, performance can be assessed on a small number of dimensions that do not collapse when code becomes abundant.

*Technical judgment* concerns the quality of tradeoffs and decisions: whether the engineer chooses appropriate solutions, anticipates failure modes, and adapts when new information arrives.

*Ownership and delivery reliability* concerns whether work reaches "done" responsibly: clarifying requirements, managing dependencies, communicating status, and closing loops.

*Quality and maintainability* concerns whether changes are testable, readable, reviewable, and stable, rather than merely voluminous.

*Risk mitigation*—security, privacy, reliability—concerns whether the engineer reduces the probability and impact of failure through testing, threat modeling, safe rollout, and monitoring.

*Collaboration and leverage* concerns whether the engineer unblocks others, reviews well, mentors, and makes the team faster, not only themselves.

These map naturally onto the SPACE framework, which warns against over-focusing on "activity" and insists that productivity is multidimensional.

### Step three: connect the model to outcomes without weaponizing metrics

Delivery and reliability metrics belong in the picture, but as context rather than as the grade. DORA's current guidance defines software-delivery performance metrics, which have evolved beyond the original "four keys," and frames them as indicators of delivery outcomes. Used as team-level context, they help a manager see whether an individual's difficulties reflect a personal pattern or a systemic one.

DORA's 2025 research on AI carries a related message that managers should take to heart: AI is an *amplifier*. It magnifies an organization's strengths and its weaknesses alike, and the largest gains come from the underlying system—culture, platform, and data ecosystem—rather than from the tool alone. A review process that blames individuals for what the system produces will therefore misfire in both directions.

## Reading the Traces: Lazy or Unlucky?

The manager's real problem is separating the engineer who is working hard on something difficult from the one whose low effort is concealed by fluent AI output. The best way to tell them apart is to look at process evidence: the traces that appear when someone is doing the hard thinking and responsible delivery work, even when much of the code was AI-assisted.

### Traces of a hard-working engineer on a hard problem

The first sign is **clear problem framing before heavy coding**. A short written artifact—a ticket comment, a design note, a pull-request description—that states a hypothesis, constraints, non-goals, and a plan to de-risk.

The second is **early de-risking**: small spike pull requests, feature-flag scaffolding, incremental rollout plans, added monitoring, or a test harness. An engineer who is stuck but serious tends to leave this scaffolding behind.

The third is **high-signal collaboration**: precise questions to partner teams, summarized decisions, proposed interfaces, and reviews that unblock others.

The fourth is **reviewability discipline**: small or logically segmented pull requests, descriptions that help reviewers, and prompt responses to feedback.

The fifth is **quality behavior that does not show up in line counts**: meaningful tests, refactors that reduce complexity, documentation, runbooks, and operational readiness.

### Traces of low effort hidden by AI output

The opposite pattern is just as recognizable. **Lots of code, little convergence**: reverts, thrash, high churn without explanation, or "big bang" pull requests that repeatedly fail continuous integration.

**A weak verification posture**: minimal tests, missing edge cases, ignored static-analysis or security alerts.

**Passive dependency management**: long blocked periods with no escalation, no alternative plan, and no proactive communication.

**Rubber-stamp collaboration**: shallow reviews, slow responses, and failure to follow through on commitments.

**Unowned operational consequences**: repeated incidents or regressions tied to the engineer's changes, with no participation in the postmortem and no improvement to monitoring.

### A fast heuristic: narrative plus artifacts

When the traces are ambiguous, one test cuts through quickly. Ask whether the engineer can produce a coherent *narrative* of what happened, what they tried, what they learned, and what they will do next—and whether they can back it with *artifacts*: pull requests, tickets, CI runs, incident timelines.

This borrows from the explainability principles NIST applies to AI systems, now applied to humans. The best engineers can explain what the AI did, what they accepted or rejected, and why. An engineer who cannot explain the code they submitted has delegated more than the typing.

## A Low-Effort, Defensible Improvement Workflow

When the evidence does point to underperformance, managers face the part of the job they like least: the improvement plan. The following workflow is a pragmatic design, not legal advice. It aims to reduce manager effort while staying aligned with widely recognized HR practice: clear expectations, regular check-ins, documented support, and a fair opportunity to improve. Performance-management guidance, such as that from the CIPD, consistently emphasizes exactly these elements.

### Three design principles

First, **use systems of record, not prompt surveillance**. Evidence should come from tickets, pull requests, CI, and incident records—artifacts the engineer already produces in the course of work—rather than from logging what they type into an AI assistant. Prompts may contain sensitive content, and monitoring them corrodes trust.

Second, **keep a human in the loop for every evaluative step**. AI can collect and summarize; it must not judge. This guards against the pitfall that researchers, including the International Labour Organization, describe in algorithmic management, where workers are primarily evaluated by the system itself and tracked data effectively becomes the manager.

Third, **build in bias and privacy safeguards by default**: minimize data collection, remove personal information where possible, and keep AI summaries auditable and correctable by a human.

### How the workflow runs

The process begins by defining expectations and the difficulty band of the work. Each week, an evidence pack is collected automatically. An AI assistant drafts a summary of the week and the change against goals; the manager reviews and corrects it. A weekly checkpoint follows, in which the manager gives feedback, removes blockers, and resets goals as needed.

At each decision point the question is simple: is the engineer on track? If so, the plan continues, or closes early if progress is sustained. If not, the manager escalates support and tightens the scope. At the end, either the pass criteria have been met—the plan closes and the manager continues to monitor—or they have not, in which case the manager consults HR to decide on a role change or exit.

### The evidence pack

The evidence pack is automated but verified by the manager. It contains the work list (tickets or epics owned, with difficulty band, status, and next step); the pull-request list (opened and merged, size, review comments, time to first review, and indicators of rework); CI results for the engineer's changes (pass rate, flaky tests, reruns); post-merge signals (rollbacks, hotfixes, incidents); and collaboration signals (reviews given, turnaround time, and instances of unblocking others).

### Pass and fail criteria that account for difficulty

Because the criteria are adjusted for difficulty, they look different for different work.

For **delivery**, low- and medium-difficulty work should reach its planned milestones reliably with minimal reopening or rework. For high- and extreme-difficulty work, the expectation is weekly de-risking progress—even if the final ship date is later. This is the clause that protects the unlucky engineer.

For **quality**, there should be no recurring defects of the same class, required tests should be added or updated, CI should be green on merge, and there should be no avoidable rollbacks.

For **collaboration**, the engineer should meet review and response expectations, escalate blockers within a defined time, and communicate status weekly.

For **judgment**, the engineer should keep a short decision log for significant tradeoffs and be able to explain why AI suggestions were accepted or rejected.

### A lean 30/60/90-day plan

A sensible plan stays narrow. It focuses on one role's core outcomes, not on personality traits.

In the **first thirty days**, the goal is to stabilize execution on one or two medium-scope deliverables. The engineer keeps a weekly plan and risk list, submits small pull requests with tests, and responds promptly to reviews. The evidence is the tickets, pull requests, CI results, and review threads. A reasonable pass standard is that at least 80 percent of weekly commitments are met or accompanied by documented de-risking, CI passes on merges, and there are no repeatable, avoidable regressions.

In **days thirty-one to sixty**, the goal is to deliver one end-to-end feature or subsystem change with a safe rollout. The engineer writes a design note, uses a feature flag or rollout checklist, adds monitoring, and prepares for incidents. The evidence is the design document, pull requests, release notes, and dashboards. The pass standard is that the feature ships, or is staged according to plan, with acceptable stability after merge.

In **days sixty-one to ninety**, the goal is to demonstrate sustained ownership and team leverage. The engineer mentors and reviews others, proactively unblocks colleagues, and maintains the quality bar. The evidence comes from review logs, teammate feedback, and metrics, and the pass standard is sustained role-level performance with consistent signals from manager and peers.

## Tooling That Supports the Workflow

Much of this can be supported with tools that engineering organizations already use, provided they are used for support rather than judgment.

**Repository workflow enforcement** turns quality expectations into gates rather than lectures: CODEOWNERS files, protected branches with required status checks, code scanning with CodeQL, and secret scanning with push protection.

**AI assistants for review and summarization** can reduce the clerical load: Copilot pull-request summaries (edited by the author for accuracy), Copilot code review as an assistant rather than an authority, and Copilot Autofix for CodeQL alerts.

**Telemetry and metrics aggregation** provides team-level context. Copilot's usage-metrics dashboard or API is useful for understanding adoption and workflow patterns, and DORA tooling—such as OpenDORA or Apache DevLake and its DORA dashboards—can aggregate delivery metrics. These are for analysis of the system, not for ranking individuals.

**Privacy and bias controls** complete the picture. Prefer artifact-based evidence over prompt logging; treat prompts as potentially sensitive; keep AI summaries auditable and correctable; and remove personal information and avoid over-collection wherever possible.

## The Manager's Playbook

### Calibrate before you evaluate

Four habits make the system fairer. Pre-calibrate difficulty bands at the start of the quarter, so that they are not assigned after the fact to justify a conclusion. Define "table stakes" separately from "impact," so that meeting the baseline is not mistaken for excelling. Use a second reader for any adverse action. And apply the same rubric consistently to everyone.

### Words that help

The conversation matters as much as the framework, and a few scripts can make it easier.

When resetting expectations: *"With AI tools, code volume is no longer a reliable signal. Going forward, I'll evaluate performance based on delivery outcomes adjusted for difficulty, quality gates, and collaboration signals."*

When you suspect low effort: *"I'm seeing repeated patterns: large changes without sufficient tests, slow response to review feedback, and no clear de-risking narrative."*

When starting an improvement plan: *"This plan isn't about code output. It's about meeting the role's expectations: predictable delivery, quality, and ownership."*

### Keep documentation light

Write down expectations and weekly goals. Use AI to draft the weekly summaries, with the manager editing for accuracy. Maintain a single decision log. The point is that a fair process does not have to be a heavy one.

### Charts worth watching

The most useful weekly charts compare each person to team medians *within the same difficulty band*: delivery predictability (planned versus done), pull-request reviewability (median size and review cycle time), rework (fix pull requests, reverts, and hotfixes), quality gates (CI pass rate, test-coverage changes, and code-scanning trends), collaboration (review turnaround and substantive comments), and operational impact (incidents tied to changes, and involvement in mitigation).

## Conclusion

Lines of code were never a good measure of engineering performance. They were merely convenient. AI has removed the convenience by making the thing being counted nearly free, and has added a hazard by shifting costs onto reviewers, security teams, and future maintainers.

What replaces them is not a cleverer metric but a different question. Instead of asking *how much did this person produce?*, ask: *how hard was the problem, how well did they frame it, how responsibly did they de-risk and deliver it, and how much did they help others while doing so?* Those questions can be answered from the artifacts engineers already leave behind—without surveilling prompts, without handing judgment to an algorithm, and without turning the manager into a data-entry clerk.

Handled this way, the performance review becomes what it was always supposed to be: not an audit of activity, but a structured conversation about judgment, ownership, and growth. And the engineer who is simply stuck on a hard problem finally has a fair way to show that they were not lazy, only unlucky.
