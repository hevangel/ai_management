# AI Agents Won't Kill Scrum. They'll Kill the Parts That Never Worked.

Imagine arriving at work on Monday morning and discovering that your engineering team produced 37 pull requests over the weekend.

The code compiles. Tests pass. Documentation has been updated. Several agents even found and fixed problems nobody had explicitly assigned.

Is this a productivity breakthrough?

Maybe.

Or perhaps your organization has just created 37 things that five humans now have to understand.

This is the management problem that AI agents are beginning to create.

For years, companies have treated developer capacity as one of software development's scarcest resources. They estimated stories, measured velocity, allocated engineers, planned Sprints, and worried about whether expensive technical talent was fully utilized.

AI is beginning to invert that constraint.

As agents become capable of implementing, testing, documenting, and iterating on software with decreasing human involvement, producing code becomes cheaper.

But deciding what code should exist does not.

Neither does determining whether it is safe, understanding its architectural consequences, resolving conflicting stakeholder goals, or deciding whether what was shipped actually worked.

The new bottleneck is not execution.

It is **judgment**.

### Scrum has been preparing us for this all along

There is an irony here.

Many organizations think AI threatens Scrum because Scrum is associated with story points, two-week development cycles, daily status meetings, and Jira tickets.

But those aren't Scrum's essential ideas.

The official Scrum framework centers on empirical management: make work transparent, inspect what happens, and adapt based on evidence. Product Goals establish direction. Sprint Goals establish near-term purpose. The Definition of Done creates a shared quality standard. An Increment may be released whenever it is usable; organizations do not need to wait until the Sprint ends.

Seen from that perspective, AI doesn't eliminate Scrum's core logic.

It exposes how much corporate "Scrum" had become a system for managing human labor.

And that system is becoming obsolete.

### Replace capacity planning with verification planning

Suppose five engineers previously had the capacity to implement five significant pieces of work during a Sprint.

Management's problem was straightforward: Which five should we choose?

Now give those engineers a fleet of capable agents.

Perhaps the organization can generate 50 plausible implementations.

But the five engineers still cannot deeply review 50 architectural decisions. Product managers cannot run 50 meaningful customer experiments. Security teams cannot investigate 50 novel attack surfaces. Operations teams cannot absorb unlimited change without increasing systemic risk.

The scarce resource has moved.

I call the new constraint **verification bandwidth**: the amount of machine-generated change that an organization can responsibly understand and validate.

This changes Sprint Planning.

Instead of asking, "How much can we build in the next two weeks?" leaders should increasingly ask:

**How much change can we afford to understand?**

That seemingly small change has large consequences.

### Let machines run continuously. Keep humans on a learning cadence.

AI agents don't need Sprints.

They don't go home Friday afternoon. They don't get tired. They can generate another implementation immediately after the first one fails.

That does not mean people should operate the same way.

The future organization is likely to have two clocks.

The machine clock runs continuously.

Agents code, test, simulate, investigate, deploy, monitor, and revise.

The human clock remains periodic.

People decide which problems matter. They evaluate evidence. They resolve trade-offs. They reconsider priorities. They decide whether an experiment means what the data appears to say.

The Sprint therefore changes meaning.

It stops being primarily a production box and becomes a **learning box**.

### Change what goes into the backlog

A backlog full of tiny implementation instructions makes less sense when implementation becomes cheap.

Instead, teams should increasingly give agents **intent packages**.

An intent package specifies the problem, the desired outcome, constraints, representative scenarios, unacceptable behaviors, and evidence required before the solution can be trusted.

The human contribution moves upward—from telling machines *what code to write* toward defining *what must be true*.

This is also why the Definition of Done becomes more important rather than less.

An agent may be able to produce working software very quickly. But "working" cannot simply mean that the code compiles and unit tests pass.

Depending on risk, done may include security evidence, observability, rollback capability, policy compliance, evaluation against holdout scenarios, and appropriate provenance.

The objective is not to surround every AI-generated change with bureaucracy.

It is to make the cost of verification proportional to the cost of being wrong.

### Don't confuse more output with more productivity

The danger is already visible.

DORA's 2025 research characterizes AI as an amplifier of the engineering system in which it operates. Subsequent analysis notes a tension: greater AI adoption is associated with higher delivery throughput, but also with higher instability, while engineers often reinvest time saved generating code into auditing and verification.

That should change how executives interpret AI productivity.

If a team produces twice as much software but also doubles rework, incident response, and unwanted complexity, the company has not necessarily become twice as productive.

It may simply have become faster at creating work for itself.

This is why engineering leaders should pay more attention to measures such as deployment rework and change failure, alongside throughput and lead time. DORA's current framework explicitly includes deployment rework rate among its five software-delivery measures.

### The manager's job moves upstream

The management implication is larger than changing a few Scrum ceremonies.

When execution is expensive, managers create leverage by organizing execution.

When execution becomes abundant, managers create leverage by improving the quality of the decisions that feed execution.

That means better problem selection.

Better specifications.

Better constraints.

Better evaluation systems.

Better architecture.

Better risk classification.

And faster organizational learning.

AI therefore doesn't remove the need for management. It changes what good management looks like.

The companies that win the agentic-software transition won't necessarily be those that generate the most code, run the most agents, or spend the most tokens.

They will be the organizations capable of answering four questions faster than competitors:

**What are we trying to accomplish?**

**How will we know whether the machine did it correctly?**

**How much risk are we willing to accept?**

**What did we learn?**

Scrum can still provide the management rhythm for answering those questions.

But only if organizations stop using it to manage human typing speed.
