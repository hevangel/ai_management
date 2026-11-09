# AI Junior-Engineer Agents and the Rewiring of Software Organizations

*Give every engineer an AI agent as capable as a junior engineer, and the org chart does not simply speed up. The firm shifts from scarce human execution capacity to human judgment, boundary management, review, and coordination.*

## Bottom Line

If every engineer in a large software company gets an AI agent that is roughly as capable as a junior engineer, the organization does not simply become "the same org chart, but faster." The deeper change is that the firm shifts from a hierarchy built around scarce human execution capacity to a system built around human judgment, boundary management, review, and coordination, with AI handling much of the local execution, search, drafting, and synthesis work.

Current evidence already suggests that AI in software work is near-universal, perceived as productivity-enhancing by most practitioners, and best understood as a multiplier of the underlying team system rather than a standalone fix for weak collaboration. At the same time, the evidence is heterogeneous: less-experienced workers often benefit more, while very experienced developers on familiar, high-context tasks can be slowed down by current AI tools.

My synthesis is that the most likely post-AI equilibrium inside a large software company is a smaller human core per unit of output, more explicit interfaces, more persistent machine-readable artifacts, fewer routine handoffs, and more importance placed on the humans who own architecture, integration, trust, and cross-boundary decisions. The organization becomes less dependent on informal human memory and unwritten conventions, and more dependent on auditable artifacts, shared context, and governance over who is allowed to delegate what to which agent. This is because AI improves throughput, but also sharpens the costs of ambiguity, weak ownership, and misaligned incentives.

## What Current Research Already Shows

The strongest current evidence says AI adoption in software development is already widespread and is changing work patterns, but not in a uniform way. Google's 2025 DORA research, based on nearly 5,000 technology professionals, reports that AI adoption among software-development professionals reached 90 percent, that more than 80 percent said AI enhanced their productivity, and that AI functions as a "mirror and a multiplier": cohesive organizations benefit more, while fragmented ones see their weaknesses exposed more clearly. The same research finds a "trust paradox": many developers find AI useful without fully trusting it.

### Individual productivity: heterogeneous, not monotonic

A 2025 set of randomized field experiments at Microsoft, Accenture, and a Fortune 100 company found a 26.08 percent increase in completed tasks among 4,867 developers using an AI coding assistant, with larger gains and higher adoption among less-experienced developers. In customer support, Brynjolfsson, Li, and Raymond found a 14 percent average productivity increase from a generative AI assistant, including a 34 percent improvement for novice and low-skilled workers, with minimal gains for experienced and highly skilled workers.

But a randomized controlled trial of experienced open-source developers working in mature codebases found the opposite: allowing early-2025 AI tools *increased* completion time by 19 percent.

That combination matters organizationally. AI tends to compress some skill gaps, but it does not eliminate the value of expertise, especially where deep context and rigorous validation dominate.

### Team performance: it depends on how context is distributed

At the team level, the evidence points in two directions at once. On one hand, AI can behave like a genuine teammate in some settings. In Harvard Business School's Procter & Gamble field experiment, AI-assisted individuals matched the output quality of a traditional two-person human team on innovation tasks, while teams using AI performed best: they were more likely to generate top-decile ideas, mixed technical and commercial thinking more effectively, and reported more enthusiasm and less frustration.

On the other hand, team-AI performance depends heavily on how context is distributed. Experimental work on team decision-making found that teams with centralized AI knowledge outperformed human-only teams, whereas teams in which AI knowledge was fragmented or asymmetric failed to clearly outperform human teams, because new AI-specific asymmetries emerged, including mistrust and ineffective use of AI-provided information.

### Why "one agent per person" is not a strategy

The organizational-behavior literature also suggests why giving every person an agent does not automatically produce a high-performing collective. Teams and multiteam systems work by coordinating interdependent specialized roles around shared goals, and they depend on *transactive memory*—shared awareness of who knows what. Recent work on human-AI teams shows that trust emerges differently in human-AI teams than in human-only teams, and that third-party human teammates influence how trust in AI teammates forms.

A recent longitudinal study in a project-based software development organization found that by 2025 AI was mostly accelerating individual tasks such as coding, writing, and documentation, while longstanding collaboration problems around accountability and fragile communication largely persisted. What changed most was not teamwork mechanics but collaborative culture, including stronger norms around efficiency and "responsible" AI use.

## How Team Structure Will Change

### From a coordination tax to human nuclei with agent capacity

The pre-AI large software company was already a multiteam system: many interdependent teams, each with local objectives but also a superordinate product or platform goal. In that world, firms paid a high tax for coordination, onboarding, search, documentation, context transfer, and routine implementation. With junior-like agents attached to each engineer, much of that tax falls on the local side of the equation. Engineers can draft code, tests, documentation, migration plans, and design alternatives with far less waiting. That reduces the need for some traditional junior-human bandwidth and probably lowers the number of purely execution-focused human roles per unit of output.

But this should not be confused with flat replacement of people by agents. The more plausible structural shift is toward *human nuclei with attached agent capacity*. A senior or mid-level engineer stops being "one worker" and starts looking more like a small production cell: planner, reviewer, integrator, and coach of local agents. This makes some units more productive with fewer humans, but it also makes a subset of roles more valuable: architects, tech leads, incident commanders, product integrators, and boundary owners.

A recent NBER team-production model is consistent with this intuition. In a sequential workflow, optimal AI replacement preserved the role that maintained the flow of information and disproportionately replaced edge positions rather than the central coordination role; the model also found that firms may rationally leave some AI capacity unused rather than automate indiscriminately. That is a theoretical result, not a field result, but it maps well to what software organizations know from practice: execution is easier to delegate than integration.

### Apprenticeship changes shape

A second structural shift concerns how engineers learn. If AI takes over many classic junior tasks—first drafts, CRUD scaffolding, boilerplate tests, issue triage, documentation stubs—then large companies lose some of the natural ladder by which younger engineers learned system constraints. That risk is not just economic; it is psychological and organizational. Experimental and survey evidence shows that passive reliance on AI-generated content reduces self-efficacy and psychological ownership, while active collaboration with AI mitigates those harms.

So the winning firm does not simply assign every engineer an agent. It redesigns learning so that humans still own review, debugging, integration, failure analysis, and architectural reasoning, rather than becoming passive acceptors of machine output.

### Shared AI infrastructure beats purely private agents

A third structural shift is toward shared AI infrastructure. The evidence on team decision-making suggests that centralized AI knowledge works better than fragmented AI knowledge. That implies that platform, developer-experience, knowledge-management, and architecture teams become more important, not less: they define the shared corpora, interface contracts, evaluation loops, guardrails, and agent access patterns that keep local agents from becoming isolated private assistants.

In practice, large firms will probably evolve toward a model with both personal agents and shared organizational agents, with the latter carrying canonical context for codebase conventions, security policies, build systems, architecture decisions, and service ownership.

## How Communication Will Change

### From conversation to artifact

The biggest communication change is a move from conversation-centric coordination toward artifact-centric coordination. Research on technology and teams shows that when task interdependence is high, access to a team's communication history can improve coordination. Research on global software engineering similarly finds that tools like Slack can increase team awareness and informal communication, but coordination still breaks down when key people are unavailable or when participation is uneven. In other words, software organizations already depend on persistent digital traces; AI increases the value of those traces because agents can consume, summarize, compare, and act on them at scale.

That means the important communication unit increasingly becomes the **boundary artifact**: the requirement, user story, architecture decision record, design spec, interface contract, test policy, runbook, and incident timeline. Recent software-engineering research describes user stories and specifications as boundary artifacts that help different groups interpret the same artifact according to their own needs, and shows that artifacts support knowledge retention and transfer across organizational boundaries. It also shows that artifact reliability degrades when ownership is unclear, trust is low, or maintenance is inconsistent.

In an AI-heavy company, those findings matter more, because the agent is only as good as the artifact it can read. Unwritten social norms that a skilled human could infer from hallway context will not be a reliable communication channel for delegated agent work.

### Inside teams: from generation to adjudication

Inside teams, communication also becomes more asynchronous, review-heavy, and traceable. Microsoft's research on AI pair programming found that developers were already spending more time reviewing code than writing it, and argued that AI will shift roles further toward assessing suggestions instead of manually performing every step. DORA's trust-paradox result points the same way: AI is useful enough to be embedded in workflows, but not trusted enough to eliminate human review.

So within a team, fewer conversations will be about "please draft this," and more will be about "which version do we accept, under what assumptions, and who signs off?" The center of gravity moves from generation to adjudication.

### Across teams: ambiguity becomes expensive

Across teams, communication becomes more formalized because AI makes ambiguity expensive. Relational-contract research in organizational economics emphasizes a "clarity problem": parties need a shared understanding of the promises they are making to one another, especially when change is unavoidable and contracts are incomplete. That is exactly the old large-company problem of unwritten scope, blame, and credit rules. AI does not remove that problem. It makes it more visible, because agents need explicit instructions and because AI-generated output makes overlap cheaper.

The likely result is more explicit pre-commitments around scope, review, ownership, and acceptance criteria—but not necessarily more legalistic rigidity. Research on rules versus principles in relational contracts suggests that principle-based agreements often adapt better than narrow rules when conditions change unexpectedly. The design implication is subtle: firms need more explicit boundaries, but those boundaries should often be framed as durable principles plus concrete artifacts, not as brittle microrules.

## A Game-Theoretic Look at Three Scenarios

Organizational change is ultimately a story about incentives, and incentives are the domain of game theory. Three scenarios show how junior-like agents change the game, depending on who is playing against whom.

### Same-team collaboration: an assurance game

The cleanest model for two engineers on the same team is a repeated assurance game with complementarities. If both engineers share state, expose intermediate artifacts, and review each other's AI-augmented output, both do better. If one collaborates and the other free-rides, the collaborator bears more coordination cost and may be exploited.

AI changes this game in two ways. First, it lowers the private cost of producing useful artifacts: drafts, tests, documentation, synthetic examples, alternative designs. Second, it raises the value of review and integration, because total output volume goes up and the marginal cost of bad acceptance can rise with it. The cooperative equilibrium therefore becomes easier to reach if there is observability, shared context, and common review norms.

This produces a genuinely win-win outcome when the pair uses AI as a joint amplifier rather than as two private replacement engines. Harvard Business School's "cybernetic teammate" results imply that AI can compensate for some missing expertise and help individuals perform at team-like levels, but that the best results still come from human teams with AI, not just isolated individuals using AI. The experiment on centralized versus asymmetric AI knowledge points in the same direction: shared AI context and balanced collaboration outperform fragmented AI usage. So inside a team, the superior equilibrium is not "everyone disappears into their own agent window." It is "everyone brings AI-accelerated artifacts into a shared human review loop."

The main risk is that AI makes each engineer more self-sufficient in the short run, and therefore less dependent on the other engineer for day-to-day tactics. That sounds good, but it can reduce the ordinary human interactions through which teams build shared understanding and expertise. Evidence on self-efficacy and psychological ownership suggests that passive reliance on AI can erode a worker's connection to the task, while the longitudinal software-organization study suggests AI improved individual throughput without solving accountability or communication problems. So the same-team equilibrium improves only if the team explicitly rewards review, explanation, and integration—not just raw local throughput.

### Cross-team "frenemies" inside one company

For two engineers in different departments and cost centers, the right model is not a pure cooperation game. It is a repeated game with incomplete contracts, local payoffs, and shared project value—the classic terrain of multiteam systems and relational contracts. Before AI, many large firms ran this game on unwritten norms: who "owns" the story, whose headcount gets charged, who gets blamed if the integration fails, who gets credit if the launch succeeds. Organizational-economics research treats such arrangements as relational contracts sustained by repeated interaction rather than complete formal contracts, and stresses that collaboration requires clarity about commitments even when environments change.

AI changes the payoff matrix sharply. It lowers the cost of doing overlapping work, and it also lowers the cost of doing political work: drafting memos, generating status narratives, summarizing evidence, and constructing retrospective accounts of who contributed what. At the same time, AI can improve traceability, because commits, tickets, prompts, summaries, and artifact histories can be logged more systematically. So AI pushes in two directions at once. It can make cross-team relations more governable through stronger evidence, or more adversarial through faster claim-staking and blame-shifting. Whether the equilibrium becomes cooperative or political is determined mostly by incentives, not model quality. DORA's "mirror and multiplier" framing is exactly relevant here.

If the two departments keep separate scorecards and separate budget incentives, the likely Nash equilibrium becomes more defensive than in the pre-AI era. Each side can use AI to expand its apparent scope, protect itself with documentation, and push ambiguous work onto the other team. Recent evidence also suggests that organizational AI adoption can provoke knowledge hiding under some conditions, especially when workers appraise AI as a hindrance rather than a challenge. That matters because in a multi-cost-center project, the temptation to hoard context, or to reveal it selectively, grows stronger when local incentives dominate shared outcomes.

The cooperative equilibrium is still attainable, but it requires stronger mechanism design than before. The firm should define a shared superordinate payoff, explicit acceptance criteria, named decision rights, common incident and postmortem procedures, and boundary artifacts with clear owners. Software-engineering work on boundary artifacts is especially relevant here: artifacts are effective only when stakeholders trust them, ownership is clear, and the artifact is actively maintained across boundaries. My best inference is that AI will reduce some interpersonal bargaining over "who said what," but will increase the need for ex ante rules on who owns decisions, who owns integration, and how credit is allocated across idea generation, implementation, operational support, and risk absorption.

### Cross-company negotiation with a vendor or supplier

The last scenario is closest to a bargaining game under incomplete information. Strictly speaking, buyer-supplier interaction is not fully zero-sum over time, because better forecasting, faster cycles, and resilient relationships can increase total surplus. But many procurement moments are locally distributive: every extra dollar, concession, or extra token spent by one side reduces its own margin.

In that environment, AI changes the game mostly by changing the information structure. Procurement-oriented analyses already describe agentic AI as able to synthesize bids, build market intelligence, prepare negotiation playbooks, track benchmarks, generate counteroffers, and support end-to-end workflows from sourcing through post-award performance monitoring. McKinsey's 2026 procurement analysis also emphasizes that procurement return on investment should be measured against the full cost of people, technology, data, and change—so token spend becomes one more managed input against the value created.

That change does not automatically produce clean, efficient equilibrium behavior, because current AI negotiators are not perfectly rational. Research on large language models in strategic and negotiation settings finds that they often deviate from rational strategies as games become more complex. A large-scale autonomous negotiation competition found that classic human negotiation principles remain powerful in AI-to-AI settings: "warmth" improved deal frequency and value creation, while dominance improved value claiming. Separate work on agentic interactions suggests that delegating to agents does not necessarily homogenize outcomes; instead, outcomes may become more dispersed, and the identity of the human who designed the agent matters as much as, or more than, shared information or code. Autonomous bargaining, in other words, does not wash out human style. It scales it.

The likely equilibrium is therefore *cyborg bargaining*, not fully autonomous bargaining. For routine, low-stakes, high-volume transactions—tail spend, standard renewals, standardized clauses—agents can do a meaningful fraction of the work. For strategic vendors or suppliers, humans will stay on the critical path for reservation-price choices, relationship repair, contingent obligations, off-price terms, and decisions where short-run price extraction conflicts with long-run resilience. The game-theoretic reason is simple: repeated games with relational value reward credible cooperation and learning, while one-shot hard bargaining only optimizes the immediate slice of surplus. The empirical negotiation evidence reinforces the point by showing that relationship-oriented traits still matter even among AI negotiators.

For the concern that token costs will hit the bottom line, the organizational implication is that firms will increasingly separate negotiation workflows into cheap deterministic stages and expensive agentic stages. Screening, data extraction, benchmark lookup, clause comparison, and counterfactual modeling will be budgeted and automated aggressively; open-ended strategic reasoning will be reserved for high-value exceptions. AI makes negotiation more analytical and more scalable, but it also makes compute governance part of commercial governance. The win is not simply "use more AI." It is "use enough AI to improve estimates of your best alternative to a negotiated agreement, and to speed the process, without creating an uncontrolled compute race or making unreviewed concessions."

## What Large Software Companies Should Formalize Now

The main organizational task is to redesign incentives and interfaces before AI volume overwhelms the old social operating system. In practice, the most important moves are not exotic. They are governance moves that make a human-agent organization legible.

**First, make boundary ownership explicit.** Every important artifact—architecture decision, API contract, product requirement, operating procedure, exception policy—needs a named human owner, an update cadence, and identified downstream consumers. Software-engineering research shows that artifact trust and usefulness collapse when ownership is unclear or maintenance becomes inconsistent.

**Second, replace vague cross-team understandings with principles plus artifacts.** The relational-contract literature does not say to write everything down as rigid rules. It says the real challenge is shared understanding under change, and that principle-based agreements often adapt better than narrow rules. For AI-era software organizations, that means explicit service boundaries, credit rules, escalation norms, and acceptance criteria, expressed in a way that can survive unforeseen change rather than hard-coding every edge case.

**Third, explicitly reward review, integration, and exception handling.** AI-assisted development shifts work toward evaluating and accepting machine-generated suggestions. If the organization still rewards only raw ticket throughput or code volume, it will underinvest in the human bottlenecks that actually matter. The evidence already shows that AI can increase throughput without fully resolving trust, validation, and coordination challenges.

**Fourth, keep apprenticeship alive by design.** The risk of passive AI use is not only technical debt but human-capability debt. Workers who only paste and accept AI output can lose self-efficacy and psychological ownership. That makes deliberate rotation through architecture review, incident handling, debugging, and human explanation even more important.

**Fifth, create a shared AI context layer**—the "data spine" or knowledge layer that prevents every engineer's agent from becoming a private, inconsistent source of truth. Procurement research makes this point explicitly for commercial data; the same logic applies inside software engineering to policies, code conventions, platform dependencies, service catalogs, and reliability standards.

## Open Questions and Limitations

The evidence base for fully agentic software organizations is still developing. Some of the most relevant studies are preprints, working papers, or single-organization case studies rather than long-run, multi-firm panel data, so the strongest claims today should be about the direction of change, not precise magnitudes.

The results are also highly context-sensitive. AI appears especially helpful for novices, for tasks with lower context requirements, and for ideation- or drafting-intensive work, but the gains are smaller or even negative for experienced practitioners operating in dense, familiar, high-quality codebases. That means there will not be one universal post-AI team design across every software domain. Platform engineering, safety-critical systems, product ideation, enterprise integrations, and procurement negotiations will not converge to the same equilibrium at the same speed.

## Conclusion

The highest-confidence conclusion is narrower than the headline, but still important: AI makes local execution cheaper, increases output volume, magnifies coordination quality, and forces large organizations to replace tacit social rules with more explicit, human-governed interfaces.

In same-team settings, that can be strongly win-win. In cross-team settings, it can either civilize or intensify turf games, depending on incentives. In cross-company bargaining, it speeds analysis and scales style, but it does not eliminate the need for human judgment over trust, strategy, and long-run relationship value.

The organizations that thrive will not be those that hand every engineer an agent and wait. They will be the ones that redesign the system around the agents: who owns what, who reviews what, who learns how, and who is rewarded for making the whole thing work together.
