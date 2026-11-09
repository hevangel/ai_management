# Office Politics in the Age of AI

*When an organization's knowledge must be written down for AI to work, influence moves from the people who hold tribal knowledge to the people who control the knowledge supply chain.*

Every organization has people who are "the only one who knows." The engineer who remembers why the legacy module was built that way. The operations lead who knows which customer escalations really matter. The senior specialist whose opinion quietly decides which project survives the review. Their influence rarely appears on an org chart, yet it shapes who is consulted, who is trusted, and who is indispensable.

Enterprise AI is about to disturb that arrangement.

The assistants now being deployed in companies—enterprise search, retrieval-augmented LLM assistants, knowledge graphs, agent toolchains—work only when an organization's knowledge is written down, indexed, permissioned, and retrievable. In doing so, they convert informal, person-held expertise into something legible, queryable, and auditable. That is not merely a productivity story. It is a redistribution of informational power and a redrawing of turf boundaries.

This article makes a simple argument. Office politics will not disappear in the age of AI; it will move. Influence will drift away from those who guard tribal knowledge and toward those who control what I will call the **knowledge supply chain**: who authors the source-of-truth documents, who curates the taxonomy, who decides what gets ingested, who tunes what gets retrieved, who sets access rules, and who interprets the audit trail. Understanding that shift—and choosing a defensible way to play in it—may become one of the more important career skills of the next decade.

## Why AI That Depends on Written Knowledge Changes the Game

Most enterprise assistants are variations of one architectural idea: retrieval-augmented generation, or RAG. The approach was formalized as a model class that pairs the parametric memory of a language model with a non-parametric memory—a retrievable corpus of documents—motivated explicitly by the limits of language models in precision, updating, and provenance. In the enterprise, the corpus is your company's documents, tickets, chats, and wikis; the retriever decides which fragments the model sees; the model then writes an answer.

Vendors describe the same pattern in their own words. Microsoft 365 Copilot, for example, coordinates large language models with the content in Microsoft Graph that the user has permission to access. Microsoft's own readiness guidance ties the quality and safety of answers to data being "well governed, current, and appropriately shared."

That sentence is a technical statement with political consequences. Whoever determines what counts as governed, current, and appropriately shared effectively influences what the AI will claim is true inside the company.

The incentives follow directly. Because the assistant is only as useful as what is written and retrievable, organizations are pushed to document more, to standardize and index what they document, and to govern who can see and retain it. Knowledge that once lived in people's heads and in hallway conversations is pulled into artifacts. And artifacts, unlike memories, can be owned, ranked, permissioned, and audited.

## The Knowledge Supply Chain and Its Control Points

The deeper change is that decisions are increasingly mediated by systems that select what is relevant. Scholars of algorithms have long argued that search and ranking systems are not neutral: they adjudicate relevance and visibility, and so shape what people encounter and act on. Research on algorithmic technologies at work describes them as a "contested terrain of control," where each new control mechanism invites adaptation and resistance from the people subject to it.

Large language models intensify this. When an assistant summarizes across sources, the winner is not merely the author whose document is found. It is the author whose framing becomes the AI's synthesized narrative.

It helps to see the enterprise knowledge pipeline as a chain with six control points, each of which is a lever of power:

- **Authoring.** Who can create and bless canonical artifacts—design documents, runbooks, policies? The author of the page the assistant treats as authoritative shapes the answer.
- **Curation.** Who controls the taxonomy, metadata, templates, and the definition of "done"? Whoever defines the categories defines what can be found.
- **Ingestion.** Who runs the connectors, decides what is indexed, and sets how often it is refreshed? What is not ingested effectively does not exist for the AI.
- **Retrieval and ranking.** Who can tune ranking signals, embeddings, freshness, and "featured sources"? This is the quiet power to decide which voices are heard first.
- **Access control.** Who writes the role- and attribute-based rules, and who remediates oversharing? Permission-aware assistants only surface what a user is allowed to see, so the permission model becomes a map of who gets to know.
- **Audit and analytics.** Who can see usage, prompts, administrative actions, and compliance logs—and how do they interpret them? They shape what leaders believe is happening.

These map neatly onto the classical bases of social power described by French and Raven: expert, informational, legitimate, and reward power. The difference is that they are now partly mediated by tools and policies rather than by purely interpersonal networks. A person with no formal authority but control of a connector or a canonical template can hold more practical influence than a manager who has never looked at the index.

## How Performance Heterogeneity Erodes Status Hierarchies

Traditional status hierarchies rest on a plausible assumption: senior people know more, and therefore they are indispensable. Generative AI puts pressure on that assumption, because it appears to help the least experienced people the most.

Two field studies are instructive. In a deployment study covering 5,179 customer-support agents, access to a generative AI assistant raised the number of issues resolved per hour by 14 percent on average. For novice and low-skilled workers the gain was 34 percent, while the impact on experienced and high-skilled workers was minimal.

A controlled field experiment with high-skill professionals found something similar, with an important caveat. For tasks inside what the researchers called the AI's "jagged frontier," AI use increased speed by 25 percent, quality by more than 40 percent, and task completion by 12 percent. Below-average performers gained 43 percent; above-average performers gained 17 percent. But for tasks outside the frontier, overreliance on the tool degraded correctness.

The political implications are significant:

- Experts lose the monopoly rents on routine know-how once that know-how is encoded and retrievable. If the answer to a standard question is one prompt away, being the person who knows it is worth less.
- Newcomers gain leverage. Higher baseline competence and faster drafting let them contribute earlier and challenge established views with better-prepared arguments.
- Gatekeeping moves upstream. Experts who adapt preserve their influence by owning the documents and governance that feed the AI, by reviewing its outputs, and by owning the judgment-heavy tasks that sit beyond the frontier.

The shift is not from experts to novices. It is from experts as *holders* of knowledge to experts as *stewards, reviewers, and judges* of it.

## From People-Centric to Artifact-Centric Knowledge

It is useful to compare two regimes.

In the **pre-AI regime**, knowledge is people-centric. Tribal knowledge resides in experts' heads. It flows through social networks and meetings. Experts gatekeep decisions through informal control: they are consulted because they are the only ones who know.

In the **AI-mediated regime**, knowledge is artifact-centric. Runbooks, design documents, tickets, and chats are the raw material. Connectors ingest them; indexes organize them through keyword search, vector search, and knowledge graphs; ranking decides what surfaces; an assistant synthesizes an answer; and decisions and execution increasingly follow those AI-mediated summaries.

Notice what has happened to the levers. Power that was once exercised through personal reputation and proximity is now exercised through document ownership and templates, connector scope and cadence, ranking signals and featured sources, access controls, and audit logs. These are less visible than a reporting line, but in an AI-mediated organization they may be far more consequential.

## What Determines Who Wins the Turf Wars

Not every organization will experience this shift in the same way. Several attributes determine who wins which battles.

### Structure and knowledge topology

The most important structural variable is whether knowledge is treated as centralized or federated. In a centralized model, a central team controls the templates, ingestion, ranking, and the definition of truth. In a federated model—similar in spirit to data-mesh approaches—domain teams own their knowledge as products, under shared governance rules.

Either way, this is fundamentally a question of decision rights. Which artifacts are authoritative? Who can publish or approve them? What gets indexed, and by whom? What ranking and grounding rules apply? What retention and deletion rules apply? Who audits, and against what thresholds?

Ambiguity on these questions invites politics. Knowledge-management research has long warned that power dynamics are embedded in knowledge flows; AI makes the embedding more explicit by forcing organizations to answer, in configuration, questions they once left vague.

### The type of AI system

Each type of system creates its own political attack surface.

**Knowledge bases and wikis** produce distinct roles—creators and integrators—and a kind of political real estate forms around canonical pages and templates.

**Enterprise search and ranking** determine visibility, and visibility determines action. Internal "SEO" behavior—writing documents to be found rather than to be read—becomes a political tactic.

**LLM assistants, whether RAG-based or agentic,** inherit the framing of their sources. Which documents are cited becomes a quasi-managerial form of influence, because a citation is an endorsement the reader rarely questions.

**Permission-aware retrieval** surfaces only what each user can access, which is exactly what organizations want. But it relocates politics to the permission model and to the clean-up of oversharing that the first deployments inevitably expose.

**Audit logs and compliance tooling** record prompts, responses, and administrative actions. That enables accountability, but it also creates a surveillance dynamic in which the people who read the logs hold a particular kind of power.

### Data governance as a source of power

Governance choices carry political weight even when they look purely technical.

*Control and edit rights.* The right to edit a canonical source is a political resource. In centralized models it produces queue-based power: whoever manages the review queue decides what gets through and how fast. Federated models, by contrast, depend on rules rather than manual policing, which distributes power but demands maturity.

*Provenance.* Citations and traceability make verification possible, and they make blame assignment possible too. They increase accountability, but they also fuel turf wars over who is credited when an answer is right and who is blamed when it is wrong.

*Retention and deletion.* Retention policies shape institutional memory—what the organization can remember and what it is allowed to forget. They can protect people, or they can be weaponized to bury inconvenient history.

### Visibility, metrics, and audit culture

AI-mediated systems increase visibility across four dimensions: discovery (what people look for), attribution (whose work answers the question), behavior (how people use the tools), and administration (who changed what). But that visibility is asymmetric. People who understand the pipeline gain interpretive power: they can explain to leadership what the data means, and they can decide which metrics to put in front of them.

Metrics, as always, invite gaming. People will optimize for ranking rather than for truth. They will over-document in order to appear in more answers. And outside the AI's frontier, they may engage in what might be called "answer theater": producing confident, fluent responses that look authoritative precisely where the tool is least reliable.

## Tactical Playbooks: What Works, and What Is Dangerous

Individuals and teams will inevitably respond to these incentives. The tactics available range from the constructive to the corrosive, and they differ sharply in both effectiveness and risk.

The most effective and least risky approaches are the ones that create genuine organizational value.

**Becoming a source-of-truth owner** is the clearest example. If you maintain the canonical, accurate, well-structured documents on which others depend, you hold durable influence, and it is influence that survives an audit because it rests on usefulness.

**Participating in governance** is similar: sitting on the bodies that set taxonomy, review policy, and decision rights places you where the rules are made, at low personal risk.

**Internal SEO for retrieval**—structuring documents with clear titles, summaries, and metadata so that the right content is found—is a medium-to-high-effectiveness, low-risk tactic, provided the goal is findability of accurate material rather than visibility of self-serving material.

**Building domain RAG assistants with evaluation** is high in effectiveness and medium in risk. A team that delivers a trusted assistant for its domain, with measured accuracy, becomes the default interface to that domain's knowledge. The risk lies in an assistant that is poorly evaluated and then trusted anyway.

**Pre-emptive documentation**—writing down decisions, rationales, and runbooks before others do—and **analytics-driven documentation**—using search and usage data to find gaps and fill them—are medium-to-high and medium in effectiveness respectively, each with moderate risk, because they can slide into over-documentation or the manufacture of a record that favors the author.

**Connector control** is a medium-to-high effectiveness tactic with medium risk. Owning what gets ingested confers real influence, but it draws scrutiny, and an owner who quietly excludes inconvenient sources is exposed when the exclusion is discovered.

Then there are the tactics that I would regard as ethically and practically perilous.

**Permission sculpting**—adjusting access rules to advantage one's own team or to starve rivals of information—may produce short-term gains, but the risk is high. Permission changes are logged, and they are among the first things an investigation reviews.

**Narrative seeding in authoritative documents**—embedding a favored framing in a canonical page so that the AI repeats it—has medium effectiveness and high risk. It is manipulation dressed as documentation, and provenance tools exist precisely to expose it.

**Data poisoning**—deliberately inserting misleading content to corrupt what the assistant says—is not recommended under any circumstances. The risk is extreme, ethically and legally, and the audit trail makes detection likely.

The pattern is clear. The tactics that work best are the ones that make the organization's knowledge more trustworthy. The tactics that depend on concealment are the ones the new visibility is built to catch.

## The Ethical and Legal Risks

The central risk of this regime can be stated in one sentence: AI turns politics into evidence.

Prompts and responses are stored. Administrative actions are logged. Systems are auditable and, increasingly, regulated. Vendor documentation makes this explicit, describing interaction histories that administrators can retain and administer for compliance. A maneuver that once left no trace beyond a hallway conversation now leaves a timestamped record.

Several categories of risk follow.

**Privacy and surveillance.** The same logs that enable accountability can be used to monitor employees in ways they did not anticipate or consent to.

**Access control and oversharing.** Permission-aware retrieval is only as good as the permissions beneath it. Years of loosely shared folders suddenly become searchable by a tireless assistant that can find what no human would have bothered to look for.

**Security and prompt injection.** When assistants read documents, documents become an attack vector. Content can be written to manipulate the assistant, which is another reason that narrative seeding is not merely unethical but dangerous.

**Misrepresentation.** If an assistant presents a confident synthesis built on stale or biased sources, the organization is misrepresenting itself to its own people, and perhaps to customers or regulators.

**Retention and eDiscovery.** Conversations with an AI assistant may be discoverable in litigation. Retention settings are therefore legal decisions as much as technical ones.

**Regulatory exposure.** Regimes such as the EU AI Act add obligations around transparency, oversight, and risk management that apply to some workplace uses of AI.

## What This Means for Careers

Over the long run, the people who thrive will be those who combine domain expertise with what might be called artifact leverage—the ability to turn what they know into trustworthy, retrievable artifacts—and with governance literacy: an understanding of permissions, provenance, retention, and evaluation.

Those who lose ground will be the ones who rely on tacit knowledge as a moat. Hoarding what you know was always a risky strategy; in an organization that is systematically encoding and retrieving knowledge, it becomes a visible and avoidable liability. This does not mean that tacit expertise has no value. Judgment, taste, and the ability to handle cases outside the frontier remain scarce. But a moat built on the mere possession of routine answers is a moat that retrieval will drain.

The highest-risk group is covert manipulators. In an environment where actions leave audit trails, those who try to win through permission sculpting, seeded narratives, or quiet exclusion are betting that no one will look. Increasingly, someone will.

## A Roadmap for Organizations

Leaders who want to channel this politics toward healthy ends, rather than leaving it to emerge by accident, can adopt a phased approach.

**Foundation (0–60 days).** Inventory the knowledge sources, their owners, and their access control lists. Fix the oversharing that the inventory reveals. Establish governance and decision rights—who may publish, approve, ingest, and audit—before the tools make those decisions by default.

**Pilot (1–4 months).** Launch permission-aware RAG pilots in bounded domains. Add provenance, so that every answer can be traced to its sources, and evaluation, so that quality is measured rather than assumed. Define the retention and audit workflows that will apply.

**Scale (3–9 months).** Move toward federated ownership under shared standards, so that domain teams own their knowledge as products without fragmenting the whole. Expand connectors under least-privilege principles. Invest in AI literacy so that employees can recognize both the value and the limits of what the assistant tells them.

**Optimize (6–18 months).** Improve ranking through feedback loops that are guarded against gaming. Automate compliance reporting. And rebalance incentives so that the work of maintaining knowledge—curating, reviewing, correcting—is recognized and rewarded rather than treated as a chore. If it is not, the best people will rationally avoid it, and the quality of everything the AI says will decay.

## Closing Synthesis

In AI-mediated enterprises, durable advantage accrues to those who provide three things: trustworthy, retrievable, permission-safe artifacts; strong stories of provenance and evaluation that explain why those artifacts deserve trust; and governance mechanisms that prevent the whole system from descending into chaos.

That path is ethically defensible. It is resilient to audits, because it depends on being useful rather than on being hidden. And it is aligned with both the technical realities of the technology—RAG's dependence on written sources—and the organizational realities it meets: power embedded in knowledge flows, and contested algorithmic control.

Office politics is not going away. But for the first time, the game is played in the open, on the record, and in a medium that rewards the people who make everyone else's knowledge easier to trust.
