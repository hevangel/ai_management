# Your Best Engineer May Soon Write the Least Code

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

### The metrics were already bad. AI makes them worse.

Engineering leaders have long known that lines of code are a poor measure of productivity. Commit counts, pull requests, tickets closed, and other activity indicators are only marginally better.

Yet these measures survive because managers need observable signals.

Before generative AI, activity at least had some relationship with human effort. Producing a large amount of functioning software required time.

That relationship is breaking.

AI can now produce code, tests, documentation, design alternatives, and implementation plans almost instantly.

The problem isn't that AI makes engineers more productive.

The problem is that **AI makes productivity theater dramatically cheaper**.

An employee can produce enormous amounts of visible activity without necessarily producing more organizational value.

Managers need a different question.

Instead of asking, "What did this person produce?" ask:

**"What changed because of this person's judgment?"**

### Measure the work that remains scarce

When implementation becomes cheap, several capabilities become relatively more valuable.

The first is **problem framing**.

AI will happily solve the wrong problem at extraordinary speed.

Strong engineers clarify what the organization is actually trying to accomplish, identify constraints, surface assumptions, and prevent teams from optimizing an implementation that should never have existed.

The second is **uncertainty reduction**.

Some of the hardest engineering work produces surprisingly little code.

An engineer debugging an intermittent system failure may spend days designing experiments, collecting traces, eliminating hypotheses, and negotiating access to another team's infrastructure.

Nothing "ships."

But the organization knows something on Friday that it didn't know on Monday.

That is progress.

The third is **judgment**.

AI can generate five architectures. It cannot assume organizational accountability for choosing one.

Someone still needs to consider reliability, security, operating cost, migration risk, organizational expertise, and future maintenance.

The fourth is **responsible delivery**.

AI-generated code that transfers debugging cost to reviewers, operations teams, security engineers, or future maintainers is not productivity.

It is cost displacement.

And the fifth is **leverage**.

The most valuable engineer may increasingly be the person who makes everyone else — human and AI — work better.

### Don't measure AI usage

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

### Use evidence without creating surveillance

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

### Stop rewarding complexity

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

The engineer who says, "We don't need to build this," may create more value than the engineer who builds it in two hours with AI.

The engineer who deletes 10,000 lines may outperform the engineer who generates 20,000.

Managers need performance systems capable of recognizing that.

### A better performance conversation

Rather than arriving at a review armed with commit charts, managers can structure the conversation around five questions:

What important problems did you frame correctly?

What uncertainty did you eliminate?

What consequential decisions did you make, and why?

What did you deliver responsibly?

How did you increase the effectiveness of the people and systems around you?

Evidence can then support the answers.

The same framework works when performance is below expectations.

A manager does not need to decide whether someone is "lazy." Motivation is difficult to observe and often irrelevant.

The more useful question is whether the employee is making reasonable progress given the difficulty of the work and the expectations of the role.

When the answer is no, managers can point to observable gaps in judgment, delivery, quality, ownership, or collaboration.

That is more defensible than counting output — and more useful to the employee.

### What performance reviews are really measuring

Performance systems were designed in an era when human production capacity was scarce.

That assumption is changing.

As AI makes execution abundant, management must move upstream.

The scarce capabilities are increasingly understanding what should be done, deciding how it should be done, recognizing when the machine is wrong, reducing uncertainty, managing risk, and taking responsibility for the result.

That leads to a counterintuitive conclusion.

The best engineer in an AI-enabled organization may not be the person producing the most code.

It may be the person who prevents the most unnecessary code from being written.
