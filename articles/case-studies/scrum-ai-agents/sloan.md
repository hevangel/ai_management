# When Execution Becomes Abundant: Rethinking Scrum for the Age of AI Agents

For most of software engineering's history, execution capacity was scarce. Organizations employed developers because turning an idea into working software required large amounts of human labor. Agile methods, including Scrum, evolved in that environment.

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

This also changes what "done" means.

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
