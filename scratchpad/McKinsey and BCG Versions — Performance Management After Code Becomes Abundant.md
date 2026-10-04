
# 3. McKinsey-Style Version

## Beyond Developer Productivity: Rewiring Performance Management for AI-Enabled Engineering

Generative AI is rapidly lowering the cost of software production. What has received less attention is what this means for the management systems surrounding software development.

Many engineering organizations still rely—formally or informally—on activity signals such as commits, pull requests, tickets completed, code produced, and delivery velocity to understand individual performance.

As AI increases the amount of engineering output that individuals can generate, these signals become less informative.

The result is an emerging management paradox:

**Organizations are gaining unprecedented visibility into engineering activity at exactly the moment when activity is becoming less useful as a proxy for value.**

Addressing this challenge requires more than changing a scorecard.

It requires redesigning engineering performance management around the capabilities that remain scarce when execution becomes abundant.

We see three shifts as particularly important.

## Shift 1: From Output Volume to Value-Creating Judgment

AI dramatically increases an engineer's capacity to generate code, documentation, tests, design alternatives, and analysis.

This is valuable.

But it also means that the amount of production generated is increasingly determined by tool capacity rather than individual contribution.

Engineering organizations should therefore distinguish between **production** and **performance**.

Production includes observable activities:

- code generated;
- pull requests created;
- tickets completed;
- builds executed;
- reviews performed.

Performance includes the decisions that determine whether those activities create value:

- framing the correct problem;
- selecting appropriate technical approaches;
- eliminating unnecessary complexity;
- identifying and mitigating risk;
- validating outputs;
- achieving maintainable business outcomes.

This distinction becomes particularly important with agentic AI.

An engineer managing several agents may generate substantially more implementation activity than an engineer working manually. But the relevant management question is not how busy the agents were.

It is whether the human directed them toward valuable outcomes.

### Management implication

Organizations should treat activity metrics as operational telemetry rather than individual-performance measures.

Telemetry can identify where managers should investigate.

It should not automatically determine employee ratings.

## Shift 2: From Task Difficulty to Difficulty Retired

Engineering leaders have long struggled to compare employees working on fundamentally different assignments.

AI makes this harder.

Routine implementation can now be completed extremely quickly, while highly ambiguous work may continue to require extensive human investigation and coordination.

Organizations can begin by characterizing assignments across four dimensions:

**Ambiguity:** How clearly is the desired outcome understood?

**Dependencies:** How many external teams, systems, or decisions constrain progress?

**Blast radius:** What are the consequences of failure?

**Novelty:** How much prior organizational knowledge exists?

But assignment difficulty should not itself become a score.

The stronger measure is how much difficulty the engineer removes.

Consider two engineers assigned similarly ambiguous projects.

One immediately begins implementation and continues to encounter unexpected problems.

The other spends two days clarifying requirements, eliminates two dependencies, reuses an existing platform capability, and reduces the project scope by half.

The second project now appears easier.

That is not evidence that the employee received easier work.

It is evidence of effective engineering.

Organizations should therefore look at **difficulty retired**:

- uncertainty converted into knowledge;
- dependencies removed;
- risks identified and mitigated;
- complexity eliminated;
- decisions clarified.

This is often where senior engineers create disproportionate value.

## Shift 3: From Individual Production to Human-AI Leverage

Organizations will also need to rethink what “using AI well” means.

AI adoption metrics are unlikely to provide the answer.

Prompt counts, token usage, generated-code percentages, and suggestion-acceptance rates can measure utilization, but utilization is not performance.

A more useful concept is **AI leverage**.

High AI leverage occurs when an engineer uses AI to:

- explore alternatives faster;
- identify assumptions;
- increase verification coverage;
- investigate unfamiliar systems;
- automate repeatable work;
- improve documentation;
- accelerate other employees;
- reduce time from uncertainty to decision.

Low-quality AI usage may produce exactly the opposite effect: large volumes of code that increase review burden, create security vulnerabilities, introduce regressions, and increase future maintenance.

The distinction is therefore not AI versus no AI.

It is productive versus unproductive leverage.

# A Five-Dimension Performance Architecture

Organizations can operationalize these shifts around five dimensions.

### 1. Problem framing

Does the engineer establish goals, constraints, assumptions, and non-goals before scaling execution?

### 2. Uncertainty reduction

Does the engineer use experiments, prototypes, investigation, instrumentation, or stakeholder interaction to convert unknowns into actionable knowledge?

### 3. Judgment

Does the engineer make effective technical and business tradeoffs and adapt decisions when new evidence appears?

### 4. Responsible delivery

Does the engineer deliver reliable, secure, testable, observable, and maintainable outcomes?

### 5. Leverage

Does the engineer increase the effectiveness of colleagues, platforms, processes, and AI systems?

These dimensions should be supported by evidence but not collapsed into a mechanically generated performance score.

# Build the Evidence Layer Before Automating the Evaluation Layer

AI can make performance management significantly less expensive administratively.

Engineering systems already contain much of the relevant evidence:

ticketing systems,
source repositories,
continuous integration,
code review,
security scanning,
deployment systems,
incident systems,
design documentation.

AI can assemble these artifacts into an evidence pack and summarize changes over time.

This can reduce the burden on managers.

But the organization should draw a clear architectural boundary:

**AI may collect and summarize evidence. Humans should remain accountable for evaluation.**

A practical workflow might include:

1. Define role expectations and the context of assigned work.
2. Automatically assemble relevant evidence.
3. Use AI to draft a factual summary.
4. Allow the employee and manager to correct the summary.
5. Discuss gaps and contextual factors.
6. Make performance judgments through human calibration.

This architecture captures the efficiency of AI without turning performance management into algorithmic management.

# Four Guardrails Matter

Organizations moving in this direction should establish four safeguards.

**First, avoid prompt surveillance.** Prompts are often sensitive and reveal little about whether engineering outcomes were valuable.

**Second, do not turn telemetry into targets.** Once individuals are rewarded for small PRs, fast reviews, or low revert counts, they will rationally optimize those signals.

**Third, calibrate against role and context rather than raw team medians.** Engineers working on infrastructure, verification, research, maintenance, and customer-facing features face fundamentally different production functions.

**Fourth, reward simplification explicitly.** When AI makes code inexpensive, unnecessary code becomes easier to create. Removing complexity should therefore carry greater organizational value.

# The Road Ahead

The first wave of enterprise AI adoption has focused on how much faster engineers can produce software.

The next management challenge will be determining what productivity means once production itself is no longer scarce.

The answer is unlikely to be a better activity dashboard.

Instead, organizations will need performance systems that recognize a different set of scarce capabilities: judgment, context, uncertainty reduction, coordination, accountability, and disciplined use of abundant machine execution.

For engineering leaders, the transition can be summarized simply:

**Measure less of what AI can cheaply produce and more of what humans must still decide.**


---

# 4. BCG-Style Version

## The Post-Productivity Engineer: Redesigning Performance When AI Makes Execution Abundant

For decades, engineering organizations operated under one fundamental constraint: skilled execution was scarce.

Software required humans to write code, search documentation, produce tests, debug systems, draft designs, and translate specifications into implementation.

That scarcity shaped not only engineering organizations but also how companies measured engineers.

Then generative AI changed the constraint.

As AI agents become capable of performing larger portions of execution, organizations face an inversion:

**Code is becoming abundant. Judgment is becoming scarce.**

Yet most performance-management systems still measure the organization as though execution were the bottleneck.

This mismatch creates what we call the **post-productivity problem**.

Companies can produce more engineering activity than ever while becoming less certain about which humans are actually creating value.

## From the Coding Organization to the Judgment Organization

The traditional engineering organization converts human labor into software.

The emerging AI-enabled organization converts human intent and judgment into software through machines.

That sounds like a small distinction.

It is not.

In the traditional model, an engineer's visible output contained information about the engineer's capability because producing that output required substantial human effort.

In the emerging model, visible output increasingly reflects the capacity of the AI system.

The human contribution moves upstream.

The engineer determines:

What problem are we solving?

What context does the AI need?

Which constraints matter?

What alternatives deserve exploration?

How do we know the output is correct?

What risks have we overlooked?

Should this software exist at all?

The organizational bottleneck migrates from **execution capacity** to **decision quality**.

Companies that continue evaluating people primarily through execution metrics will increasingly reward the wrong behaviors.

## The Abundance Trap

AI creates an abundance trap.

Because software artifacts become easy to produce, employees can create more:

code,
microservices,
abstractions,
tests,
documentation,
dashboards,
configuration,
experiments,
design alternatives.

Some of this abundance produces enormous value.

Some creates enormous complexity.

And traditional productivity metrics often struggle to distinguish between the two.

Imagine two teams.

Team A uses AI to increase code output threefold. The number of services, pull requests, and deployments rises rapidly.

Team B also uses AI but focuses on simplifying interfaces, retiring obsolete systems, eliminating manual operations, and reducing the number of components engineers must understand.

Traditional activity dashboards may celebrate Team A.

Yet Team B may have created the more scalable organization.

The management challenge is therefore not maximizing AI-enabled production.

It is **converting abundance into advantage without converting it into complexity**.

## A New Performance Currency: Difficulty Retired

How should companies recognize individual contribution in this environment?

The answer begins with moving beyond “tasks completed.”

Complex engineering work creates value by reducing several forms of difficulty:

**Cognitive difficulty:** What don't we understand?

**Technical difficulty:** What cannot yet be made to work?

**Organizational difficulty:** Which dependencies prevent action?

**Risk difficulty:** What could fail and with what consequences?

**Structural difficulty:** What complexity can be removed altogether?

Strong engineers continuously retire these forms of difficulty.

Sometimes the result is a major new product.

Sometimes it is a small architecture change.

Sometimes it is deciding not to build anything.

This concept changes the meaning of progress.

Suppose an engineer spends a week on a critical reliability problem.

No production code is shipped.

But the engineer creates a reproduction, instruments the failure, disproves three hypotheses, isolates the defect to a specific interaction, and produces a safe workaround.

The visible production is small.

The amount of difficulty retired is enormous.

In an AI-enabled organization, that difference matters more than ever.

## The Human Performance Stack

Companies can redesign evaluation around a five-layer Human Performance Stack.

### Frame

Can the employee convert poorly formed requests into well-defined problems?

### Learn

Can the employee reduce uncertainty quickly and update beliefs as evidence changes?

### Decide

Can the employee make sound tradeoffs across technical, customer, financial, and operational constraints?

### Deliver

Can the employee translate decisions into reliable outcomes with appropriate verification and risk control?

### Amplify

Can the employee make the broader system—people plus AI—more capable?

The final layer is particularly important.

Historically, individual leverage came from mentoring, tools, platforms, and organizational influence.

AI adds another multiplier.

The strongest engineers can increasingly manage fleets of machine capability, delegating execution while retaining responsibility for framing, validation, and integration.

Performance systems should recognize this leverage without rewarding AI usage for its own sake.

## From Digital Exhaust to Evidence

Modern software organizations produce an extraordinary volume of digital exhaust.

Every pull request, review comment, ticket change, build, deployment, test failure, incident, and security warning produces data.

AI makes it possible to summarize that evidence cheaply.

This creates an opportunity—and a danger.

The opportunity is to dramatically reduce the administrative burden of performance management.

The danger is algorithmic management.

Organizations may be tempted to allow the system to infer performance directly from the exhaust.

That would simply industrialize the weaknesses of today's metrics.

A better architecture separates three layers:

**Evidence layer:** Systems automatically collect relevant artifacts.

**Interpretation layer:** AI organizes evidence, identifies patterns, and drafts summaries.

**Judgment layer:** Humans evaluate performance using role expectations and context.

This division preserves the efficiency benefits of AI while maintaining accountability where it belongs.

## The Counterintuitive Winners

The most successful AI-enabled engineering organizations may exhibit several counterintuitive patterns.

Their strongest engineers may write less code.

Their most important projects may generate fewer services.

Their senior people may spend more time defining questions than producing answers.

Their highest-leverage employees may operate multiple AI agents simultaneously but personally author very little implementation.

Their best architecture decisions may appear in repositories as deleted code.

This is not a decline in productivity.

It reflects a change in what productive human work looks like.

## The Leadership Agenda

Leaders should act in three areas.

First, **remove activity metrics from the center of individual performance evaluation**.

Second, **teach managers to evaluate ambiguity reduction, judgment, and responsible delivery**.

Third, **redesign roles around human-machine leverage**, explicitly recognizing employees who improve how the broader system uses AI.

The broader implication reaches beyond engineering.

Whenever AI makes production abundant, performance shifts toward deciding what should be produced, validating whether it is correct, and accepting accountability for the consequences.

Engineering is simply reaching that future first.

The companies that recognize this shift early will not merely have more productive developers.

They will build a fundamentally different kind of organization:

one optimized not for scarce execution, but for **abundant intelligence governed by scarce human judgment**.