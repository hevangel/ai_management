# Beyond Developer Productivity: Rewiring Performance Management for AI-Enabled Engineering

Generative AI is rapidly lowering the cost of software production. What has received less attention is what this means for the management systems surrounding software development.

Many engineering organizations still rely — formally or informally — on activity signals such as commits, pull requests, tickets completed, code produced, and delivery velocity to understand individual performance.

As AI increases the amount of engineering output that individuals can generate, these signals become less informative.

The result is an emerging management paradox:

**Organizations are gaining unprecedented visibility into engineering activity at exactly the moment when activity is becoming less useful as a proxy for value.**

Addressing this challenge requires more than changing a scorecard.

It requires redesigning engineering performance management around the capabilities that remain scarce when execution becomes abundant.

We see three shifts as particularly important.

### Shift 1: From output volume to value-creating judgment

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

**Management implication.** Organizations should treat activity metrics as operational telemetry rather than individual-performance measures. Telemetry can identify where managers should investigate. It should not automatically determine employee ratings.

### Shift 2: From task difficulty to difficulty retired

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

### Shift 3: From individual production to human-AI leverage

Organizations will also need to rethink what "using AI well" means.

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

### A five-dimension performance architecture

Organizations can operationalize these shifts around five dimensions.

**1. Problem framing.** Does the engineer establish goals, constraints, assumptions, and non-goals before scaling execution?

**2. Uncertainty reduction.** Does the engineer use experiments, prototypes, investigation, instrumentation, or stakeholder interaction to convert unknowns into actionable knowledge?

**3. Judgment.** Does the engineer make effective technical and business tradeoffs and adapt decisions when new evidence appears?

**4. Responsible delivery.** Does the engineer deliver reliable, secure, testable, observable, and maintainable outcomes?

**5. Leverage.** Does the engineer increase the effectiveness of colleagues, platforms, processes, and AI systems?

These dimensions should be supported by evidence but not collapsed into a mechanically generated performance score.

### Build the evidence layer before automating the evaluation layer

AI can make performance management significantly less expensive administratively.

Engineering systems already contain much of the relevant evidence:

- ticketing systems;
- source repositories;
- continuous integration;
- code review;
- security scanning;
- deployment systems;
- incident systems;
- design documentation.

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

### Four guardrails matter

Organizations moving in this direction should establish four safeguards.

**First, avoid prompt surveillance.** Prompts are often sensitive and reveal little about whether engineering outcomes were valuable.

**Second, do not turn telemetry into targets.** Once individuals are rewarded for small PRs, fast reviews, or low revert counts, they will rationally optimize those signals.

**Third, calibrate against role and context rather than raw team medians.** Engineers working on infrastructure, verification, research, maintenance, and customer-facing features face fundamentally different production functions.

**Fourth, reward simplification explicitly.** When AI makes code inexpensive, unnecessary code becomes easier to create. Removing complexity should therefore carry greater organizational value.

### The road ahead

The first wave of enterprise AI adoption has focused on how much faster engineers can produce software.

The next management challenge will be determining what productivity means once production itself is no longer scarce.

The answer is unlikely to be a better activity dashboard.

Instead, organizations will need performance systems that recognize a different set of scarce capabilities: judgment, context, uncertainty reduction, coordination, accountability, and disciplined use of abundant machine execution.

For engineering leaders, the transition can be summarized simply:

**Measure less of what AI can cheaply produce and more of what humans must still decide.**
