# When Code Becomes Abundant: Rethinking Engineering Performance in the Age of AI

## The business problem

For most of software engineering's history, execution capacity was scarce. Turning an idea into working software required large amounts of human labor, and the performance systems built around engineers — lines of code, commit counts, pull requests, tickets closed, velocity — all rested on the same implicit assumption: visible activity was evidence of human effort, because producing it was expensive.

AI coding tools are breaking that assumption. Controlled studies of AI coding assistants have shown substantial improvements in task completion speed, and engineers can now generate code, tests, documentation, design alternatives, and implementation plans with relatively little incremental effort. The activities managers have historically counted are becoming cheap to produce — and when an intermediate output becomes inexpensive, counting it provides little information about the scarce capability behind it.

This creates an uncomfortable measurement problem. Organizations have unprecedented visibility into engineering activity at exactly the moment activity is becoming least informative. A performance system that keeps rewarding visible production will rationally reward productivity theater: more services, more complexity, more review burden, more downstream cost — while the engineers who prevent unnecessary work, retire uncertainty, and exercise judgment look, on paper, like the least productive people in the organization.

The question for engineering leaders is no longer "How much did this engineer produce?" It is: **What became clearer, safer, simpler, or more valuable because this engineer was here — and what management system can recognize it?**

## What we found

Across five analytical lenses — management theory, managerial practice, enterprise operating models, competitive strategy, and economic decision-making — a consistent picture emerges:

1. **The scarcity has moved upstream, from execution to judgment.** The traditional production chain ran from human effort to engineering activity to software output to business outcome, with activity serving as the observable proxy for effort. AI inserts machine execution into that chain: a unit of human judgment can now generate dramatically more visible activity. As the correlation between activity and contribution deteriorates, performance management must follow the scarcity — toward problem framing, uncertainty reduction, and decision quality.

2. **Measuring difficulty assigned perversely rewards preserving complexity.** Strong engineers make hard problems look easy: two days of clarifying requirements, eliminating dependencies, and simplifying an architecture can turn an "extreme" project into a straightforward one. The more useful measure is **difficulty retired** — how much uncertainty, complexity, dependency, and operational risk the engineer removed. Much of the most valuable engineering work produces knowledge rather than code.

3. **Five dimensions distinguish performance that activity metrics cannot see:** problem framing (solving the right problem), uncertainty reduction (converting unknowns into knowledge), judgment (choosing among AI-generated alternatives), responsible delivery (reliability, security, and maintainability — not cost displacement onto reviewers and operators), and leverage (making the surrounding organization more capable).

4. **Measuring AI usage repeats the old mistake with better instrumentation.** Prompt counts, token consumption, acceptance rates, and the percentage of AI-generated code are utilization metrics, not performance. The relevant question is AI leverage: whether an engineer converts AI capability into better outcomes without transferring disproportionate verification cost to colleagues.

5. **Telemetry is evidence, not judgment.** A high revert rate, a large pull request, or a cluster of incidents each has an innocent explanation as often as a guilty one. Engineering data should trigger questions, not produce ratings — and organizations should draw a hard architectural boundary: AI may collect and summarize evidence; humans remain accountable for evaluation. Prompt surveillance tells managers little and costs trust.

6. **When code is abundant, restraint becomes a top contribution.** The engineer who recognizes that none of five AI-generated services are needed, reuses an existing component, and deletes thousands of lines creates more value than the engineer who ships all of them. Every artifact creates future obligations — testing, security, operations, maintenance — so implementation is becoming abundant while complexity is not becoming free. Organizations that keep counting the exhaust of engineering work will increasingly misidentify their best people.
