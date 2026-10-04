# When Code Becomes Abundant, How Should We Measure Engineers?

Generative AI is changing software engineering faster than most corporate performance-management systems can adapt.

The obvious change is productivity. Controlled studies of AI coding tools have shown substantial improvements in task completion speed and increases in observable activity such as commits, builds, and completed tasks. But the more important management consequence is less obvious: AI is changing the information content of the signals managers have historically used to infer performance.

Lines of code, commits, pull requests, and tickets closed were always imperfect measures of engineering productivity. In an AI-assisted environment, they become considerably less useful because the activities they measure are becoming cheap to produce.

This creates a fundamental measurement problem.

When implementation capacity was scarce, visible production had at least some correlation with effort. An engineer who produced substantially more working software was usually doing something different from one who produced very little. AI weakens that relationship. A developer can now generate thousands of lines of code, multiple design alternatives, extensive documentation, and dozens of tests with relatively little incremental effort.

The implication is not simply that organizations need better metrics.

They need to reconsider **what engineering performance actually means when execution is abundant**.

### AI changes the production function of engineering

Traditional performance systems implicitly assume a chain that looks something like this:

Human effort → engineering activity → software output → business outcome

Managers cannot directly observe effort or judgment, so they often use activity as a proxy.

AI inserts another production factor:

Human judgment → AI execution → engineering activity → software outcome

The amount of visible activity that can be generated from a unit of human effort increases dramatically.

As a result, the correlation between activity and contribution deteriorates.

This is a classic measurement problem. Once an intermediate output becomes inexpensive, counting it provides little information about the scarce capability that produced the final result.

The scarce resource is moving upstream.

Increasingly, the important questions are not:

How much code did the engineer write?

How many pull requests did the engineer merge?

How many tickets did the engineer close?

They are:

Did the engineer identify the right problem?

Did the engineer reduce uncertainty?

Did the engineer make sound technical tradeoffs?

Did the engineer detect when the AI was wrong?

Did the engineer ship something reliable and maintainable?

Did the engineer increase the effectiveness of the surrounding team?

### From difficulty adjustment to difficulty retired

One response is to evaluate outcomes relative to task difficulty.

That is directionally correct. Delivering a routine feature should not be evaluated the same way as debugging an intermittent distributed-system failure involving multiple teams.

Organizations can characterize assignments along dimensions such as ambiguity, dependencies, blast radius, and novelty.

But difficulty alone creates another problem.

Strong engineers frequently make difficult problems look easy.

An engineer who receives an ambiguous project might spend two days clarifying requirements, eliminating unnecessary dependencies, and finding a simpler architecture. What initially appeared to be an "extreme" project can become straightforward.

A performance system that only rewards difficulty may perversely reward people for preserving complexity.

A more useful concept is **difficulty retired**.

How much uncertainty, complexity, dependency, and operational risk did the engineer remove?

Consider an engineer investigating an intermittent production failure. For several weeks, the engineer may write almost no production code. Yet during that time the engineer might reproduce the failure, eliminate several plausible causes, identify an undocumented dependency, coordinate multiple specialist teams, and eventually isolate the root cause.

The primary output is not code.

It is knowledge.

The engineer has converted uncertainty into organizational understanding.

That contribution becomes more important as AI handles a larger share of implementation.

### Five dimensions of AI-era engineering performance

A practical performance model can therefore focus on five dimensions.

**Problem framing** asks whether the engineer understands what problem should actually be solved. Strong engineers clarify goals, constraints, non-goals, and assumptions before generating large amounts of implementation.

**Uncertainty reduction** measures whether the engineer converts unknowns into knowns. Experiments, prototypes, investigation, instrumentation, and elimination of failed hypotheses can constitute meaningful progress even when no product feature ships that week.

**Judgment** concerns technical and business tradeoffs. AI can generate alternatives quickly, but deciding among them remains consequential. Engineers should be able to explain why an approach was accepted, modified, or rejected.

**Responsible delivery** evaluates whether the resulting system works reliably and can be maintained. Tests, rollout plans, observability, security, documentation, and operational readiness matter more than the quantity of implementation.

**Leverage** asks whether the engineer makes the surrounding organization more capable. This can include mentoring, high-quality reviews, reusable automation, better documentation, improved tooling, and effective orchestration of AI agents.

Importantly, these dimensions should not simply be converted into another composite productivity score.

Performance remains multidimensional.

### Telemetry is evidence, not judgment

Engineering organizations have access to increasingly detailed telemetry: pull-request size, cycle time, CI failures, review latency, reverts, incidents, code-scanning results, and now AI usage data.

These signals can be useful.

But organizations should resist turning them into automatic employee ratings.

A high revert rate might indicate poor engineering. It might also indicate that someone is working on the most unstable subsystem in the company.

A large pull request might indicate poor review discipline. It might also reflect an unavoidable generated migration.

An engineer associated with several incidents might be careless — or might be the person consistently trusted with the highest-risk infrastructure.

Telemetry should therefore **trigger questions rather than produce ratings**.

The same principle should apply to AI usage.

Prompt counts, token consumption, acceptance rates, and agent executions reveal workflow patterns but say little about value in isolation.

The relevant question is not whether an engineer uses more AI.

It is whether the engineer converts AI capability into better outcomes without transferring disproportionate verification cost to colleagues.

### When producing less becomes more valuable

There is a final consequence that performance systems may find particularly difficult to absorb.

When code becomes abundant, producing less code can become a mark of superior engineering.

An engineer who uses AI to generate five new services may appear highly productive.

A more experienced engineer might recognize that none of those services are necessary, simplify an interface, reuse an existing component, and delete thousands of lines of code.

Most activity metrics reward the first engineer.

The organization should probably value the second contribution more.

AI therefore increases the relative value of architectural restraint.

Implementation is becoming abundant. Complexity is not becoming free.

Every additional component still creates testing, security, operational, documentation, and maintenance costs.

As the cost of producing software falls, organizations will need engineers who know what **not** to produce.

### Performance management moves upstream

The deeper transformation is therefore not about finding a replacement for lines of code.

It is about recognizing where scarcity has moved.

Software organizations were historically constrained by human execution capacity. Performance systems naturally evolved around visible evidence of that execution.

AI weakens that constraint.

The scarce organizational resources increasingly become judgment, context, problem selection, coordination, risk ownership, and the ability to reduce uncertainty.

Performance management must follow.

The organizations that adapt successfully will stop asking primarily, "How much did this engineer produce?"

They will increasingly ask:

**What became clearer, safer, simpler, or more valuable because this engineer was here?**

That may prove to be a much better definition of engineering performance — even beyond the AI era.
