# VERSION 1 — MIT SLOAN MANAGEMENT REVIEW STYLE

## When Execution Becomes Abundant: Rethinking Scrum for the Age of AI Agents

**Horace Chan**  
*Expert in applying AI in verification*

For most of software engineering’s history, execution capacity was scarce. Organizations employed developers because turning an idea into working software required large amounts of human labor. Agile methods, including Scrum, evolved in that environment.

AI agents are beginning to change the underlying economics.

An engineer who previously implemented one piece of work at a time can increasingly delegate coding, testing, documentation, investigation, and refactoring to multiple AI agents operating in parallel. As these capabilities improve, the constraint on software development moves away from producing changes and toward deciding what changes should be made, determining whether they are correct, and understanding what has been learned after they are deployed.

This transition does not make Scrum obsolete. Paradoxically, it may make the fundamental logic of Scrum more important while making many common Scrum practices less useful.

The distinction matters because Scrum itself was never formally defined as a system for allocating programmer labor. The Scrum Guide describes an empirical system built around transparency, inspection, adaptation, goals, and usable increments. Story points, velocity targets, status reporting, and utilization optimization are not fundamental elements of the framework.

AI therefore presents less of a challenge to Scrum than to the managerial system that organizations have built around it.

### The scarcity moves

Consider the implicit production model of a conventional software team.

A team has five engineers. Each engineer has a finite number of hours. Planning therefore revolves, implicitly or explicitly, around allocating those hours to work. Estimates help determine what can fit into a Sprint. Managers worry about whether enough work is ready for developers and whether developers are fully utilized.

Now imagine those same five engineers supervising 20 capable software agents.

The agents may be able to generate dozens of implementations, tests, designs, and experiments simultaneously. Yet the humans may still be capable of carefully assessing only a handful of architectural decisions, security implications, customer trade-offs, or production anomalies.

The relationship becomes:

**Agent execution capacity \> human verification capacity.**

This suggests that one of the central management concepts in AI-native software organizations will be **verification bandwidth**.

The relevant planning question changes from:

**How much work can the team produce?**

to:

**How much change can the organization safely understand, validate, absorb, and learn from?**

That is a different operating problem.

### From production cadence to learning cadence

A common assumption is that autonomous agents will eliminate Sprints because machines do not need two-week work cycles.

That conclusion confuses the production cycle with the management cycle.

Nothing prevents agents from working continuously. Code can be generated continuously. Tests can run continuously. Deployment can be continuous as well. Scrum already allows multiple increments to be produced and released during a Sprint; the Sprint Review is explicitly not supposed to function as a release gate.

What remains periodic is human sense-making.

Teams still need to ask whether an experiment changed customer behavior, whether an architectural direction remains appropriate, whether unexpected risks have appeared, and whether the next set of goals should change.

This creates a dual-cadence organization:

**Machines operate continuously; humans govern periodically.**

The Sprint may therefore survive, but with a different economic purpose. Instead of being a container for human production capacity, it becomes a clock for organizational learning and decision-making.

### The AI-era Scrum loop

The conventional mental model of software delivery is often approximately:

**Backlog → estimate → implement → test → review → release.**

Agentic development increasingly looks like:

**Intent → generate → verify → observe → learn → adapt.**

The critical artifact at the beginning of the process is no longer a small unit of estimated work. It is an **intent package**.

An intent package describes the problem to solve, relevant constraints, acceptance scenarios, nonfunctional requirements, policy boundaries, and desired outcomes.

AI agents can then explore the implementation space.

This also changes what “done” means.

A Definition of Done for an agent-generated change may need to incorporate automated evaluation, security checks, operational observability, rollback capability, and appropriate software-supply-chain evidence. These controls should be risk-based rather than universally imposed. Current supply-chain frameworks such as SLSA, whose current approved specification is version 1.2, provide one model for stronger provenance where it is warranted.

### AI is an amplifier, not an independent production system

The most important empirical warning comes from DORA's research on AI-assisted software development.

Its 2025 research describes AI as an **amplifier** of the organizational system around it. More recent DORA analysis reports that higher AI adoption can be associated simultaneously with increased software delivery throughput and increased delivery instability. In qualitative research, time saved during initial creation is often reallocated to auditing and verification.

This is exactly what we would expect if execution capacity were increasing faster than verification capacity.

A high-performing engineering organization can use agents to increase the speed of an already disciplined system.

A poorly controlled organization can use the same agents to manufacture technical debt, vulnerabilities, rework, and production incidents faster.

The differentiating capability therefore shifts upward in the stack.

### The changing meaning of engineering productivity

This change also weakens activity-based productivity measures.

When an agent can produce ten pull requests overnight, pull-request count says little about human contribution. Lines of code become even less meaningful. Even velocity becomes difficult to interpret when the relationship between implementation effort and business value becomes increasingly nonlinear.

More useful measures combine outcomes, flow, reliability, and rework.

DORA's current software-delivery framework uses five measures, including deployment rework rate alongside deployment frequency, change lead time, failed deployment recovery time, and change fail rate. Deployment rework may become particularly informative in agentic environments because nominal output can increase while the organization spends increasing effort correcting machine-generated change.

### What survives

The interesting conclusion is not that AI requires a new Scrum.

It is almost the opposite.

AI weakens many practices that became associated with Scrum without being fundamental to it: elaborate estimation, velocity optimization, ticket decomposition, utilization planning, and status-oriented ceremonies.

At the same time, AI strengthens the need for the mechanisms at Scrum's conceptual core: explicit goals, transparency, inspection, adaptation, quality standards, and frequent learning.

The future engineering organization may therefore look simultaneously less like conventional Scrum and more like the original theory behind Scrum.

When execution becomes abundant, managing execution becomes less important.

Managing **intent, verification, risk, and learning** becomes the work.

And the organizations that learn how to increase those scarce resources—not merely the number of tokens or agents they consume—may capture the largest productivity gains from AI.

---

# VERSION 2 — HARVARD BUSINESS REVIEW STYLE

## AI Agents Won't Kill Scrum. They'll Kill the Parts That Never Worked.

**Horace Chan**  
*Expert in applying AI in verification*

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

It exposes how much corporate “Scrum” had become a system for managing human labor.

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

Instead of asking, “How much can we build in the next two weeks?” leaders should increasingly ask:

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

An agent may be able to produce working software very quickly. But “working” cannot simply mean that the code compiles and unit tests pass.

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

---

# VERSION 3 — McKINSEY STYLE

## The Agentic Software Operating Model: Rewiring Agile Delivery Around Intent, Verification, and Learning

**Horace Chan**  
*Expert in applying AI in verification*

Generative AI is rapidly changing the economics of software delivery. The next stage—agentic development—will push that shift further as AI systems take responsibility for increasingly complete units of implementation, testing, documentation, investigation, and deployment.

For technology leaders, the implication goes beyond developer productivity.

The software-development operating model itself needs to change.

Most enterprise delivery systems were designed around a historical constraint: scarce human engineering capacity. Processes for estimation, prioritization, Sprint planning, staffing, and portfolio management implicitly assumed that implementation effort was expensive and had to be carefully allocated.

Agentic systems weaken that assumption.

As execution becomes cheaper, four other constraints become more important: **intent clarity, verification capacity, risk absorption, and organizational learning**.

The opportunity for technology leaders is therefore not merely to add AI tools to the existing software-development lifecycle. It is to redesign the lifecycle around the new bottlenecks.

### Exhibit 1: The bottleneck migrates

The traditional delivery equation can be simplified as:

**Demand \> engineering capacity → optimize execution**

The emerging agentic equation becomes:

**Machine execution \> human verification → optimize judgment**

This migration has significant implications for Agile operating models.

Organizations frequently use Scrum as a mechanism for allocating development capacity through backlog decomposition, estimates, velocity, and Sprint commitments.

Yet the underlying Scrum framework is already compatible with a different model. The Scrum Guide emphasizes goals, empiricism, transparency, inspection, adaptation, and usable increments; releases may occur during a Sprint rather than waiting for its completion.

This makes Scrum potentially useful in an agentic environment—but the management system surrounding it must evolve.

### Shift one: From work packages to intent packages

Traditional backlogs often decompose a desired outcome into implementation tasks.

Agentic development reduces the need for this decomposition.

Instead, organizations can move toward **intent packages** containing the business problem, desired outcome, functional scenarios, nonfunctional constraints, policy requirements, architectural boundaries, and evaluation criteria.

Agents can then explore implementation alternatives within those boundaries.

The human role moves from specifying execution to specifying the conditions of success.

This approach can also reduce a common failure mode in AI adoption: automating inefficient processes without changing the surrounding operating model.

### Shift two: From development capacity to verification capacity

As agents generate more output, organizations need to understand a new limiting resource: **verification bandwidth**.

Verification bandwidth includes the human and automated capacity required to assess whether machine-generated changes are functionally correct, strategically appropriate, secure, maintainable, compliant, and operationally safe.

This capacity is not unlimited.

A development organization capable of generating 100 changes per day but capable of safely validating only 20 has not created a 100-change production system. It has created an 80-change queue.

Leading organizations will therefore increasingly plan around verification capacity rather than raw execution capacity.

Sprint Planning in this environment becomes less focused on estimated implementation effort and more focused on the amount and type of evidence necessary to accept a change.

### Shift three: Separate machine flow from human governance cadence

Agentic delivery can operate continuously.

Human governance does not have to.

This distinction allows enterprises to combine continuous software production with periodic management cycles.

Agents may generate, test, deploy, and monitor changes continuously. Teams can still use weekly or biweekly cycles to inspect outcomes, revisit goals, allocate verification capacity, resolve strategic trade-offs, and adapt priorities.

The result is a two-speed system:

**continuous machine execution + timeboxed human learning.**

Rather than disappearing, the Sprint may evolve from an execution cadence into a management cadence.

### Shift four: Make risk-based verification part of the delivery architecture

Agentic systems can increase the volume of software change dramatically. Applying the same verification process to every change would quickly become uneconomic.

Organizations therefore need differentiated controls.

Low-risk changes may flow through highly automated evaluation.

Higher-risk changes may require deeper security analysis, human review, provenance, staged deployment, additional observability, or explicit approval.

Software-supply-chain standards can provide part of the control architecture. SLSA's current approved specification, version 1.2, for example, includes build and source tracks and mîechanisms for provenance and attestations.

The objective is not universal governance overhead. It is automated governance proportional to risk.

### Shift five: Change the productivity system

AI will make traditional activity measures increasingly unreliable.

Lines of code, pull-request counts, ticket completion, and similar measures become particularly weak when machines can generate those outputs at very low marginal cost.

Even velocity may provide less information when agent capability changes rapidly.

Leaders should instead combine product outcomes with delivery performance, reliability, rework, and verification effectiveness.

DORA's latest research offers an important warning. Its 2025 work describes AI as an organizational amplifier, and subsequent analysis reports that greater AI adoption can coincide with both higher delivery throughput and higher instability.

DORA's current delivery framework now includes five metrics, with deployment rework rate added alongside change lead time, deployment frequency, failed deployment recovery time, and change fail rate.

For agentic organizations, rework may prove especially valuable because it helps distinguish useful acceleration from accelerated churn.

### A staged transition

The transformation need not begin with a fully autonomous “dark factory.”

Organizations can move progressively from AI-assisted coding to human-gated agentic delivery and eventually toward human-on-the-loop software factories where appropriate.

At each stage, the relevant management question changes.

Early adoption asks how AI can make developers faster.

More mature adoption asks how teams can delegate complete work packages.

Advanced adoption asks how organizations can govern a software-production system whose execution capacity may exceed the human organization's ability to supervise it directly.

This final stage requires more than better models. It requires an operating model built for abundant execution.

### The CEO and CIO agenda

The strategic mistake would be to treat agentic software development primarily as a tooling rollout.

The technology is only one component.

The larger transformation is a reallocation of scarce organizational capacity.

Enterprises historically optimized scarce engineering execution.

They will increasingly need to optimize scarce **intent, judgment, verification, risk capacity, and learning**.

The organizations that make this transition successfully can capture more than a local productivity improvement.

They can create a software operating system capable of converting machine intelligence into reliable business change at scale.

---

# VERSION 4 — BCG STYLE

## Beyond Developer Productivity: How AI Agents Could Reshape the Economics of Software Delivery

**Horace Chan**  
*Expert in applying AI in verification*

The first wave of generative AI in software engineering focused on a simple question:

**How much faster can developers code?**

The next wave raises a more consequential question:

**What happens to the organization when coding is no longer the bottleneck?**

This distinction will increasingly separate companies that obtain incremental productivity gains from those that redesign software delivery around AI.

As autonomous agents assume more implementation, testing, documentation, investigation, and deployment work, software organizations face a fundamental shift in scarcity.

Execution becomes cheaper.

Judgment does not.

The competitive advantage moves from producing software efficiently toward directing, validating, and learning from machine-produced change.

### The old software cost curve is breaking

Traditional software-development organizations evolved around expensive human execution.

Companies recruited scarce technical talent, divided work among teams, estimated engineering effort, allocated capacity, and constructed planning systems designed to ensure that developers worked on the highest-value tasks.

Scrum frequently became part of that production machinery.

Stories represented units of work. Points approximated difficulty. Velocity approximated capacity. Sprints created production batches.

Yet these practices are not Scrum's conceptual core. Official Scrum remains centered on goals, empiricism, inspection, adaptation, usable increments, and a shared Definition of Done.

AI agents expose the distinction.

When implementation cost falls dramatically, optimizing the allocation of coding effort generates diminishing strategic value.

The scarce asset moves elsewhere.

### The new scarce asset: verification bandwidth

Imagine two competitors deploying identical AI coding systems.

Company A gives each engineer several agents and measures the resulting increase in code generation.

Company B does the same—but also redesigns architecture, automated evaluation, production observability, specifications, security controls, and decision rights so that a larger volume of machine-generated change can be safely accepted.

Both companies bought similar AI.

They did not build the same capability.

Company B has increased its **verification bandwidth**.

That difference may become one of the major sources of competitive advantage in AI-native engineering.

Verification bandwidth represents the amount of machine-generated change an organization can confidently evaluate and absorb.

It consists partly of automation—testing, simulation, security analysis, policy checks, production telemetry—and partly of human judgment.

The relevant competitive ratio may therefore become:

**agent execution capacity / verification capacity**

An organization that expands the numerator while leaving the denominator unchanged eventually creates congestion rather than productivity.

### Four organizational archetypes will emerge

Companies are likely to diverge in how they respond.

The **AI-assisted incumbent** will use copilots but preserve most existing processes. Productivity improves locally, but the organizational architecture changes little.

The **agent-accelerated factory** will deploy agents aggressively while retaining conventional approval processes. Output increases rapidly, but verification queues and rework may also grow.

The **controlled agentic enterprise** will redesign specifications, testing, risk classification, platform capabilities, and observability around machine execution. Human attention will concentrate on high-value exceptions.

Finally, the **autonomous learning enterprise** will connect agents not merely to implementation but to experiments, customer signals, operations, and portfolio decisions—with humans defining strategic boundaries and governance.

The progression is not simply technological.

It represents increasing organizational capacity to convert abundant machine execution into useful change.

### AI magnifies the organization that already exists

This distinction is consistent with DORA's recent findings.

DORA's 2025 research characterizes AI as an amplifier of existing organizational strengths and weaknesses. Its subsequent analysis reports that greater AI adoption can raise software-delivery throughput while simultaneously increasing instability.

This suggests a nonlinear return to AI investment.

An organization with strong platforms, small batches, automated testing, clear architecture, and fast feedback loops may receive substantial benefits from increased agent capacity.

An organization with unclear ownership, brittle systems, poor testing, weak observability, and large release batches may simply automate its dysfunction.

The same AI investment therefore produces different economic returns depending on the surrounding system.

### Scrum becomes a competitive sensing mechanism

This is where Scrum remains relevant.

The value of a Sprint in an AI-native company is unlikely to come from giving machines two weeks to finish their assigned work.

Machines can work continuously.

The Sprint instead provides a periodic point at which humans reconsider intent.

Did the product move toward its goal?

Did customer behavior change?

Did the agents produce unexpected risks?

Did assumptions prove wrong?

Should investment continue?

This creates a useful separation:

**continuous execution below; periodic strategic adaptation above.**

Scrum thus evolves from production coordination toward a competitive sensing mechanism.

### Change the unit of management

The unit managed by the organization must change as well.

Instead of decomposing outcomes into hundreds of human-executable tasks, companies can increasingly define **intent packages** containing problems, scenarios, constraints, risk classifications, and desired outcomes.

Agents determine more of the implementation.

Humans own the boundaries and evidence.

The Definition of Done consequently becomes a critical competitive interface between machine execution and enterprise trust.

For a low-risk internal change, the required evidence may be almost entirely automated.

For a high-risk customer-facing system, it may include deeper validation, security testing, provenance, controlled deployment, and production monitoring.

The objective is not more governance.

It is **cheaper governance per unit of trustworthy change**.

### The emerging performance gap

This leads to a different interpretation of AI productivity.

The winner is not necessarily the organization whose developers accept the most AI suggestions or generate the most code.

The winner is the organization that converts each unit of human judgment into the greatest amount of reliable business change.

That implies a new optimization target:

**maximize learning and business impact per unit of scarce human attention.**

Traditional activity measures become much less useful under this model.

Measures of flow, reliability, rework, and product outcomes become more valuable. DORA's current framework, for example, includes deployment rework rate as one of five core software-delivery measures—a particularly relevant signal when machines can cheaply generate both useful code and unnecessary change.

### A widening strategic divide

For the past decade, companies competed partly on their ability to attract and organize scarce software engineers.

AI agents will not make engineering capability irrelevant.

They will change what engineering capability means.

Execution capacity can increasingly be purchased through models, tokens, and compute.

The harder capabilities will be organizational: defining good intent, creating strong evaluation systems, designing AI-compatible platforms, allocating risk intelligently, and learning faster than competitors.

Companies that merely add agents to existing development systems may achieve respectable productivity gains.

Companies that redesign the system around abundant execution may move onto a different cost and learning curve entirely.

That is where the strategic opportunity lies.

---

# VERSION 5 — BAIN STYLE

## Stop Measuring How Much AI Can Produce. Measure How Much Value Your Organization Can Absorb.

**Horace Chan**  
*Expert in applying AI in verification*

Companies are spending rapidly on AI coding tools, agents, model subscriptions, and compute.

The obvious question is: **How much more software are we getting?**

It is increasingly the wrong question.

As AI agents become capable of producing more code, tests, documentation, and analysis, the marginal cost of software execution falls.

But companies do not earn returns by producing code.

They earn returns when software creates business value.

That makes the critical management question:

**How much additional machine-generated change can the organization convert into reliable economic value?**

For many companies, the answer will be much less than their agents are theoretically capable of producing.

### Find the real bottleneck before buying more capacity

Consider a team of five developers.

Before AI, the team's limiting factor may genuinely have been implementation capacity.

Give those engineers effective agents and the constraint can shift quickly.

The team may now be capable of initiating 50 pieces of work but only able to deeply validate 15.

Adding more agents at that point does not solve the bottleneck.

It makes the queue longer.

The economic equation becomes:

**Value from AI = useful machine output × organizational ability to verify and absorb it**

The second term is easy to underestimate.

We call this constraint **verification bandwidth**.

It includes automated testing, security controls, architecture, platform capability, observability, domain expertise, product judgment, and the human attention required to deal with exceptions.

Once verification becomes the bottleneck, another dollar spent on execution capacity may have a lower return than a dollar spent on automated evaluation, better internal platforms, clearer product specifications, or stronger production telemetry.

### Scrum should help expose the constraint

This is where Agile practices still matter.

Scrum was never formally intended to maximize developer utilization. Its underlying system is empirical: establish goals, produce usable increments, inspect results, and adapt.

That logic becomes increasingly valuable when agents can produce changes faster than humans can evaluate them.

But some common Agile practices lose usefulness.

Story points are less informative when implementation effort changes depending on model capability.

Velocity becomes difficult to compare when an agent upgrade can change output overnight.

Detailed task decomposition becomes wasteful if an agent can determine implementation itself.

The purpose of planning therefore shifts.

Instead of asking how much work fits into the Sprint, leaders should ask how much **risk-adjusted change** the organization can validate during the period.

### Manage AI like capital

Executives should treat AI capacity as an investment portfolio rather than an unlimited productivity subsidy.

Consider two potential investments.

The first buys enough model capacity to double agent output.

The second improves the verification platform so that 50% more machine-generated changes can be accepted automatically with the same or lower failure rate.

If verification is already the bottleneck, the second investment may generate the higher marginal return.

This is the key AI capital-allocation principle:

**Fund the constraint, not the excitement.**

At low levels of AI adoption, model capability may be the constraint.

Later it may be internal data.

Then automated testing.

Then architecture.

Then product decision-making.

Then customer demand itself.

Management's job is to identify where the bottleneck moved after the previous investment.

### Watch the hidden cost of rework

Raw production metrics can make poor AI investments look attractive.

Suppose AI increases software-delivery throughput by 30%.

If defects, rollbacks, operational incidents, security remediation, and unnecessary changes also increase, the economic gain may be much smaller.

Recent DORA research captures this tension. Its 2025 work describes AI as an amplifier of the surrounding engineering system, and later analysis finds higher AI adoption associated with greater delivery throughput but also greater instability.

This makes rework particularly important.

DORA's current software-delivery framework includes deployment rework rate among its five metrics. For executives evaluating AI investments, rework helps expose a cost that gross-output measures hide.

A team that produces twice as many changes but spends most of its new capacity correcting those changes has not doubled productivity.

It has increased gross production without proportionate net output.

### Change what “done” costs

The Definition of Done should therefore become an economic control.

Not every change deserves the same verification investment.

A low-risk internal UI improvement may warrant almost completely automated validation.

A change affecting payment processing, security, regulated decisions, or critical infrastructure should require substantially stronger evidence.

Companies should classify changes by risk and match verification spending accordingly.

This creates a scalable model:

**low risk → low-cost automated verification**

**high risk → high-confidence verification**

The objective is not zero risk.

Zero risk would make software delivery uneconomic.

The objective is the optimal amount of verification for the value and downside associated with the change.

### Separate machine utilization from human utilization

Leaders should also resist applying traditional utilization logic to AI.

Idle compute is a cost problem.

Idle human cognitive capacity is not the same thing.

If engineers are responsible for supervising agents, reviewing anomalies, making architectural decisions, and responding to unexpected failures, deliberately preserving human slack may increase total system performance.

A factory running machines at 100% utilization can be desirable.

A decision system running every expert at 100% cognitive utilization can become brittle.

Agentic organizations therefore need to optimize the combined system rather than maximize either human activity or machine activity independently.

### Follow the money

The AI transformation of software development can ultimately be evaluated through a straightforward sequence.

Did AI reduce the cost of producing a candidate change?

Did verification costs rise or fall?

Did rework increase or decrease?

Did cycle time improve?

Did reliability change?

And most importantly: did the additional software produce incremental business value?

Those questions are more useful than asking how many developers use AI or how many lines of AI-generated code were committed.

The first phase of enterprise AI has largely focused on adoption.

The next phase will be about economics.

As execution becomes abundant, competitive advantage will not come from maximizing how much software AI can produce.

It will come from identifying the next scarce resource—and investing the next dollar there.