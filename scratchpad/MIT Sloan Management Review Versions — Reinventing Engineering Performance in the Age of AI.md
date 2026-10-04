
# 1. MIT Sloan Management Review Version

## When Code Becomes Abundant, How Should We Measure Engineers?

Generative AI is changing software engineering faster than most corporate performance-management systems can adapt.

The obvious change is productivity. Controlled studies of AI coding tools have shown substantial improvements in task completion speed and increases in observable activity such as commits, builds, and completed tasks. But the more important management consequence is less obvious: AI is changing the information content of the signals managers have historically used to infer performance.

Lines of code, commits, pull requests, and tickets closed were always imperfect measures of engineering productivity. In an AI-assisted environment, they become considerably less useful because the activities they measure are becoming cheap to produce.

This creates a fundamental measurement problem.

When implementation capacity was scarce, visible production had at least some correlation with effort. An engineer who produced substantially more working software was usually doing something different from one who produced very little. AI weakens that relationship. A developer can now generate thousands of lines of code, multiple design alternatives, extensive documentation, and dozens of tests with relatively little incremental effort.

The implication is not simply that organizations need better metrics.

They need to reconsider **what engineering performance actually means when execution is abundant**.

### AI Changes the Production Function of Engineering

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

### From Difficulty Adjustment to Uncertainty Reduction

One response is to evaluate outcomes relative to task difficulty.

That is directionally correct. Delivering a routine feature should not be evaluated the same way as debugging an intermittent distributed-system failure involving multiple teams.

Organizations can characterize assignments along dimensions such as ambiguity, dependencies, blast radius, and novelty.

But difficulty alone creates another problem.

Strong engineers frequently make difficult problems look easy.

An engineer who receives an ambiguous project might spend two days clarifying requirements, eliminating unnecessary dependencies, and finding a simpler architecture. What initially appeared to be an “extreme” project can become straightforward.

A performance system that only rewards difficulty may perversely reward people for preserving complexity.

A more useful concept is **difficulty retired**.

How much uncertainty, complexity, dependency, and operational risk did the engineer remove?

Consider an engineer investigating an intermittent production failure. For several weeks, the engineer may write almost no production code. Yet during that time the engineer might reproduce the failure, eliminate several plausible causes, identify an undocumented dependency, coordinate multiple specialist teams, and eventually isolate the root cause.

The primary output is not code.

It is knowledge.

The engineer has converted uncertainty into organizational understanding.

That contribution becomes more important as AI handles a larger share of implementation.

### Five Dimensions of AI-Era Engineering Performance

A practical performance model can therefore focus on five dimensions.

**Problem framing** asks whether the engineer understands what problem should actually be solved. Strong engineers clarify goals, constraints, non-goals, and assumptions before generating large amounts of implementation.

**Uncertainty reduction** measures whether the engineer converts unknowns into knowns. Experiments, prototypes, investigation, instrumentation, and elimination of failed hypotheses can constitute meaningful progress even when no product feature ships that week.

**Judgment** concerns technical and business tradeoffs. AI can generate alternatives quickly, but deciding among them remains consequential. Engineers should be able to explain why an approach was accepted, modified, or rejected.

**Responsible delivery** evaluates whether the resulting system works reliably and can be maintained. Tests, rollout plans, observability, security, documentation, and operational readiness matter more than the quantity of implementation.

**Leverage** asks whether the engineer makes the surrounding organization more capable. This can include mentoring, high-quality reviews, reusable automation, better documentation, improved tooling, and effective orchestration of AI agents.

Importantly, these dimensions should not simply be converted into another composite productivity score.

Performance remains multidimensional.

### Telemetry Is Evidence, Not Judgment

Engineering organizations have access to increasingly detailed telemetry: pull-request size, cycle time, CI failures, review latency, reverts, incidents, code-scanning results, and now AI usage data.

These signals can be useful.

But organizations should resist turning them into automatic employee ratings.

A high revert rate might indicate poor engineering. It might also indicate that someone is working on the most unstable subsystem in the company.

A large pull request might indicate poor review discipline. It might also reflect an unavoidable generated migration.

An engineer associated with several incidents might be careless—or might be the person consistently trusted with the highest-risk infrastructure.

Telemetry should therefore **trigger questions rather than produce ratings**.

The same principle should apply to AI usage.

Prompt counts, token consumption, acceptance rates, and agent executions reveal workflow patterns but say little about value in isolation.

The relevant question is not whether an engineer uses more AI.

It is whether the engineer converts AI capability into better outcomes without transferring disproportionate verification cost to colleagues.

### When Producing Less Becomes More Valuable

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

### Performance Management Moves Upstream

The deeper transformation is therefore not about finding a replacement for lines of code.

It is about recognizing where scarcity has moved.

Software organizations were historically constrained by human execution capacity. Performance systems naturally evolved around visible evidence of that execution.

AI weakens that constraint.

The scarce organizational resources increasingly become judgment, context, problem selection, coordination, risk ownership, and the ability to reduce uncertainty.

Performance management must follow.

The organizations that adapt successfully will stop asking primarily, “How much did this engineer produce?”

They will increasingly ask:

**What became clearer, safer, simpler, or more valuable because this engineer was here?**

That may prove to be a much better definition of engineering performance—even beyond the AI era.


---

# 2. Harvard Business Review Version

## Your Best Engineer May Soon Write the Least Code

Imagine two engineers receiving the same assignment.

The first opens an AI coding agent and gets to work. By Friday, the engineer has created 12 pull requests, generated thousands of lines of code, added several services, and closed six tickets.

The second engineer spends much of Monday asking questions.

Why does the feature need to exist?

Could the requirement be satisfied by changing an existing interface?

What happens if the new service fails?

By Wednesday, that engineer has concluded that most of the proposed architecture is unnecessary. A small change to an existing component solves the customer problem. The implementation is a few hundred lines.

Who had the better week?

Most executives would instinctively choose the second engineer.

Many corporate performance systems would quietly reward the first.

Generative AI is about to make this contradiction impossible to ignore.

### The Metrics Were Already Bad. AI Makes Them Worse.

Engineering leaders have long known that lines of code are a poor measure of productivity. Commit counts, pull requests, tickets closed, and other activity indicators are only marginally better.

Yet these measures survive because managers need observable signals.

Before generative AI, activity at least had some relationship with human effort. Producing a large amount of functioning software required time.

That relationship is breaking.

AI can now produce code, tests, documentation, design alternatives, and implementation plans almost instantly.

The problem isn't that AI makes engineers more productive.

The problem is that **AI makes productivity theater dramatically cheaper**.

An employee can produce enormous amounts of visible activity without necessarily producing more organizational value.

Managers need a different question.

Instead of asking, “What did this person produce?” ask:

**“What changed because of this person's judgment?”**

### Measure the Work That Remains Scarce

When implementation becomes cheap, several capabilities become relatively more valuable.

The first is **problem framing**.

AI will happily solve the wrong problem at extraordinary speed.

Strong engineers clarify what the organization is actually trying to accomplish, identify constraints, surface assumptions, and prevent teams from optimizing an implementation that should never have existed.

The second is **uncertainty reduction**.

Some of the hardest engineering work produces surprisingly little code.

An engineer debugging an intermittent system failure may spend days designing experiments, collecting traces, eliminating hypotheses, and negotiating access to another team's infrastructure.

Nothing “ships.”

But the organization knows something on Friday that it didn't know on Monday.

That is progress.

The third is **judgment**.

AI can generate five architectures. It cannot assume organizational accountability for choosing one.

Someone still needs to consider reliability, security, operating cost, migration risk, organizational expertise, and future maintenance.

The fourth is **responsible delivery**.

AI-generated code that transfers debugging cost to reviewers, operations teams, security engineers, or future maintainers is not productivity.

It is cost displacement.

And the fifth is **leverage**.

The most valuable engineer may increasingly be the person who makes everyone else—human and AI—work better.

### Don't Measure AI Usage

Managers will be tempted to solve the measurement problem with a new set of metrics.

How many AI prompts did each employee send?

How many tokens did they consume?

What percentage of their code was AI-generated?

How often did they accept AI suggestions?

This would repeat the same mistake with better instrumentation.

AI usage is an input.

Performance is an outcome.

Imagine two employees.

One uses an agent 500 times to brute-force an implementation.

The other asks three agents to investigate alternatives in parallel, discovers that the proposed architecture creates an unnecessary dependency, and cancels the project.

The first employee wins the AI-usage contest.

The second may have saved the company six months of engineering work.

Organizations should evaluate **AI leverage**, not AI consumption.

The question is whether employees can use AI to explore faster, test assumptions earlier, increase quality, understand unfamiliar systems, automate repetitive work, and expand the capacity of the team.

### Use Evidence Without Creating Surveillance

Managers still need evidence.

Fortunately, modern engineering organizations already produce it.

Tickets show how requirements evolved.

Design documents show assumptions and tradeoffs.

Pull requests show implementation and review behavior.

Continuous-integration systems show verification.

Incident records show operational consequences.

Code-scanning systems show security posture.

The key is how managers use this evidence.

A metric should start a conversation, not end one.

A high number of reverts should cause a manager to ask why. It should not automatically reduce an employee's rating.

Slow delivery should prompt examination of dependencies and ambiguity. It should not automatically imply poor effort.

Large pull requests deserve scrutiny but may sometimes be unavoidable.

The principle is simple:

**Telemetry is evidence, not judgment.**

This also means resisting invasive prompt surveillance. Employee prompts may contain sensitive technical, organizational, and personal context. More important, reviewing them tells managers surprisingly little about whether the work was good.

Judge the decisions and outcomes, not the keystrokes that produced them.

### Stop Rewarding Complexity

AI creates another management challenge.

Organizations may soon find themselves drowning in technically correct software.

When the marginal cost of generating another implementation falls, engineers can create additional services, abstractions, frameworks, tests, documentation, and configuration with almost no friction.

But every artifact creates future obligations.

Someone must understand it.

Someone must review it.

Someone must secure it.

Someone must operate it.

Someone must eventually change it.

This makes restraint increasingly valuable.

The engineer who says, “We don't need to build this,” may create more value than the engineer who builds it in two hours with AI.

The engineer who deletes 10,000 lines may outperform the engineer who generates 20,000.

Managers need performance systems capable of recognizing that.

### A Better Performance Conversation

Rather than arriving at a review armed with commit charts, managers can structure the conversation around five questions:

What important problems did you frame correctly?

What uncertainty did you eliminate?

What consequential decisions did you make, and why?

What did you deliver responsibly?

How did you increase the effectiveness of the people and systems around you?

Evidence can then support the answers.

The same framework works when performance is below expectations.

A manager does not need to decide whether someone is “lazy.” Motivation is difficult to observe and often irrelevant.

The more useful question is whether the employee is making reasonable progress given the difficulty of the work and the expectations of the role.

When the answer is no, managers can point to observable gaps in judgment, delivery, quality, ownership, or collaboration.

That is more defensible than counting output—and more useful to the employee.

### What Performance Reviews Are Really Measuring

Performance systems were designed in an era when human production capacity was scarce.

That assumption is changing.

As AI makes execution abundant, management must move upstream.

The scarce capabilities are increasingly understanding what should be done, deciding how it should be done, recognizing when the machine is wrong, reducing uncertainty, managing risk, and taking responsibility for the result.

That leads to a counterintuitive conclusion.

The best engineer in an AI-enabled organization may not be the person producing the most code.

It may be the person who prevents the most unnecessary code from being written.