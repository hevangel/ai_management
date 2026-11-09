# Sell the Work, Not the Doorway: How SaaS Wins in the Age of Agents

*Why forcing customers onto a proprietary agent to mark up model usage is a weak long-term strategy—and why controlled openness, with governed execution as the product, is the stronger one.*

A SaaS executive's pitch might sound like this: *we will build an AI agent into our product, buy foundation-model inference at wholesale, charge customers a healthy multiple, and make sure they cannot point any competing agent at their own data.* The revenue case is easy to see. Customers are already locked into the software, AI is the hot budget line, and a markup on tokens looks like free money.

This essay argues that the strategy is directionally wrong for most competitive SaaS companies. It may well increase revenue over the next few years. But if AI capability keeps advancing and inference keeps getting cheaper, the markup on "intelligence" will become increasingly transparent and contestable, and a company whose strategy rests on controlling the doorway will find that the intelligence behind the doorway has become cheap and interchangeable.

The more durable model is **controlled openness**: open the product's data and action layer to authorized external agents, while selling a first-party managed agent that wins on convenience, reliability, governance, integration, and guaranteed outcomes. The qualification matters. The SaaS company does not need to give away API access, allow arbitrary agents to execute unrestricted actions, or sell its own agent at cost. It can charge substantial margins. But those margins should attach to governed execution, domain workflow expertise, validation, risk transfer, compliance, human exception handling, and measurable business outcomes—not to making alternative intelligence providers inaccessible.

## Two Ideas That Are Not Opposites

The pitch above bundles two separate ideas.

The first is to **charge according to completed work rather than raw tokens**. The second is to **prevent customers from using any competing agent or model**. The first idea can be excellent. The second is usually the dangerous part.

Customers generally do not want to buy forty thousand input tokens, six retrieval operations, three tool calls, and two retries. They want a support issue resolved, an invoice reconciled, a contract reviewed, a configuration changed, a customer onboarded, an engineering failure diagnosed. A SaaS provider can legitimately convert uncertain, complicated AI costs into a simple business price—much as a cloud provider charges for a managed database rather than itemizing every CPU instruction and disk operation.

The problem begins when the strategy becomes: *our agent does not need to be the best or the cheapest, because we will prevent every other agent from accessing the customer's own data and workflows.* That is not an AI moat. It is an access toll.

## Why Raw Intelligence Is a Poor Place to Build a Moat

The economics of inference are moving against simple token arbitrage. Stanford's 2025 AI Index found that the cost of querying a model at roughly GPT-3.5-level benchmark quality fell from $20 per million tokens in November 2022 to $0.07 by October 2024—a reduction of more than 280 times. Depending on the task, observed inference-price declines ranged from roughly 9-fold to 900-fold per year, and hardware price-performance was also improving rapidly.

That does not mean every frontier model will become continuously cheaper. The newest reasoning models may remain expensive, and agents can consume enormous quantities of inference through planning, retries, and tool use. But it does mean that a SaaS company cannot safely assume that today's model cost is a durable source of pricing power.

At the same time, agent capability is improving quickly. METR's software-task measurements found that the length of tasks frontier agents could complete with 50 percent reliability had historically doubled approximately every seven months, although METR emphasizes substantial methodological uncertainty and does not claim the trend must continue. Stanford's 2026 AI Index reported that computer-using agents reached 66.3 percent on OSWorld, yet still failed roughly one out of three attempts on structured agent benchmarks.

These findings point in two directions at once. Models are becoming capable enough to threaten thin SaaS wrappers. And they remain unreliable enough that orchestration, controls, and accountability still have value. That combination is exactly why a managed agent can be a valuable product while token resale alone is a weak moat.

## Where Value Moves as Models Improve

A useful way to think about the market is to divide the AI stack into layers. As intelligence becomes more interchangeable, value shifts toward assets that a model cannot independently manufacture: permission to take an action; access to authoritative data; knowledge of what a successful outcome looks like; business rules; approval chains; historical exceptions; liability when the result is wrong; and integration with the rest of the organization.

The winning SaaS company is therefore unlikely to be the one that merely owns the chatbot. It is more likely to be the one that owns the *trusted execution environment* behind the chatbot.

## Why Charging by Outcome Can Be a Very Good Model

A high markup over model cost is not inherently objectionable. Consider a hypothetical task that uses 15,000 input tokens and 3,000 output tokens, at hypothetical model rates of $3 per million input tokens and $15 per million output tokens. The first-pass model cost is about $0.09: $0.045 for input and $0.045 for output.

Now add the rest of the real cost of delivering the outcome: roughly $0.04 in expected retries, $0.03 for retrieval and tool services, $0.02 for monitoring and logging, $0.25 on an expected-value basis for human exception handling, and $0.10 for a support, security, and liability reserve. The all-in expected cost is about $0.53.

Selling the outcome for $2 would produce a gross margin near 74 percent. That can be entirely reasonable if the task previously cost the customer $10 or $20 and the vendor guarantees the result. The customer is not purchasing nine cents of tokens. The customer is purchasing a functioning workflow, predictable cost, fewer people doing repetitive work, integration with business records, exception handling, a service-level commitment, and someone to call when it fails.

HubSpot offers a useful real-world example. In April 2026, it moved its Customer Agent to $0.50 per resolved conversation and its Prospecting Agent to $1 per recommended lead, rather than charging merely for activation or conversation volume. HubSpot says its ability to do this comes from integration with its Smart CRM context. It reports that Customer Agent resolves 65 percent of conversations and reduces resolution time by 39 percent, although those figures are vendor-reported rather than independently audited.

That is much closer to a defensible business model. It says: *we understand the customer, the history, and the workflow well enough to accept performance risk.* It is very different from saying: *we passed your prompt to a model and charged you twenty times the API cost.*

## The Definition of "Completed Task" Is Everything

Outcome pricing becomes dangerous when the vendor controls both the agent performing the work and the definition of whether the work succeeded.

Take a "resolved support conversation." Does it mean the agent sent a final answer? That the customer did not immediately respond? That the ticket stayed closed for seven days? That no human had to intervene? That the customer confirmed the solution? That the account was not later refunded? Each definition produces a different price and a different incentive.

A robust outcome contract should specify the observable completion event, quality thresholds, a time window for reversal or reopening, human-escalation rules, refund or credit rules, the treatment of partial completion and duplicate tasks, and the audit evidence. For a financial reconciliation, "done" might mean that the transaction matched, passed all controls, posted to the ledger, and was not reversed within thirty days. For a support task, it might mean that the customer confirmed resolution, no human takeover occurred, and the case did not reopen within seven days.

Without such definitions, "pay per task completed" can become a disguised consumption meter with optimistic labeling.

## Why Banning External Agents Is Strategically Risky

### The enterprise is becoming multi-model

Large customers increasingly do not want every SaaS vendor to choose a separate model, security policy, and AI billing system on their behalf. They may already have an enterprise OpenAI agreement, Microsoft Copilot, Anthropic through AWS or Google Cloud, an internal model gateway, locally hosted open-weight models, central logging and data-loss-prevention controls, and approved models for different data classifications.

McKinsey's 2025 survey found that 88 percent of respondents reported AI use in at least one business function, but nearly two-thirds had not begun scaling it enterprise-wide. Sixty-two percent were at least experimenting with agents, while only 39 percent reported enterprise-level EBIT impact. The bottleneck, in other words, is not simply model access; it is scaling, workflow redesign, and operational control. Deloitte surveys have similarly identified regulatory compliance, risk management, and missing governance models as leading barriers to deployment.

A SaaS vendor that says "you must use our model procurement, our agent runtime, and our governance layer" may therefore collide with the customer's enterprise architecture.

### Model abstraction is becoming normal infrastructure

Several major enterprise platforms now deliberately abstract the model provider. Snowflake's Cortex REST API supports OpenAI-compatible and Anthropic-compatible interfaces and exposes models from OpenAI, Anthropic, Meta, Mistral, DeepSeek, and Snowflake within a common governance boundary. Amazon Bedrock supports more than a hundred models and provides model-agnostic Converse APIs as well as OpenAI-compatible and Anthropic-compatible interfaces. Oracle's OCI Responses API is OpenAI-compatible, supports multiple model families, provides model routing, and connects to external tools through MCP. Databricks supports external models from OpenAI, Anthropic, Amazon Bedrock, Google Vertex AI, and OpenAI-compatible custom providers behind a common managed interface.

The strategic signal is clear: enterprise customers increasingly expect the model to be a replaceable component, not permanently fused to every application. A SaaS company that tightly couples its product economics to one model provider risks becoming the inflexible part of the customer's stack.

### External agents are becoming the new system of engagement

Historically, the SaaS application owned both the system of record and the user interface. AI may separate the two. The customer's preferred agent could become the system of *engagement*, while individual SaaS products become systems of record, policy, action, computation, and verification.

Imagine a user asking one enterprise agent: *find the delayed shipment, check the customer's support history, determine whether a credit is permitted, issue it, update the CRM, and notify the account manager.* That workflow may span five SaaS systems. The user does not want five conversations with five different proprietary agents. A SaaS application that refuses to participate in the cross-application workflow becomes the obstruction—and if an open competitor can supply the same core functionality, the customer may replace the SaaS product rather than the enterprise agent.

### Closing the API does not eliminate automation

Commercial agent platforms already support browser and desktop automation. Microsoft's Copilot Studio, for example, supports computer-use workflows with both OpenAI and Anthropic models. Blocking API access may therefore not prevent external automation. It may push automation toward screen scraping, simulated clicks, browser control, file imports and exports, and email-based interactions—approaches that are usually more brittle and harder to govern than a well-designed API.

From a security standpoint, the better position is often to give authorized agents a narrow, auditable, permission-scoped interface rather than forcing them to impersonate humans through the graphical interface.

## Open Protocols Are Part of the Competitive Landscape

The Model Context Protocol is an open standard for connecting AI applications with tools, data sources, and workflows; its documentation describes a broad ecosystem of clients and servers, including ChatGPT, Claude, development tools, and other agent platforms. The Agent2Agent protocol addresses communication among agents rather than merely agent-to-tool access. Google transferred A2A to the Linux Foundation in 2025, with founding participation from AWS, Microsoft, Salesforce, SAP, ServiceNow, and Cisco, and reported more than a hundred supporting companies at the time.

These standards may change or be superseded. Their importance is not that MCP or A2A must win forever; it is the direction of the market. Customers and large technology suppliers are trying to make agents and tools interoperable, and a small or mid-sized SaaS vendor that adopts a deliberately incompatible architecture is betting against that direction.

## What Leading Vendors Are Actually Doing

The market is not converging on "everything is free and open." It is converging on **open connectivity plus proprietary, metered value.**

**ServiceNow opens the action system and meters the execution.** It may be the closest current example of the model argued for here. In May 2026, ServiceNow announced that its "system of action" would be available to any authorized agent—including Claude, Copilot, and customer-built agents—through its MCP server. Execution was not made free: headless actions consume the same commercial currency used by ServiceNow's own AI products. ServiceNow also applies identity checks, permissions, OAuth, audit trails, session controls, and role-based tool packages. Its AI Control Tower is designed to govern native and third-party agents and models across other systems, with observability, risk controls, and spend measurement. These are the company's own product claims, but the strategic architecture is notable: it seeks to become the governed execution layer regardless of which agent owns the user interface. External agents become distribution channels. Every time one needs to execute an enterprise action, ServiceNow can authenticate it, apply the workflow, enforce policy, record the transaction, and charge for the execution. That is considerably more defensible than demanding that every user start inside a ServiceNow chat window.

**Salesforce charges for actions while supporting external tools.** Agentforce offers several pricing methods: $500 per 100,000 Flex Credits, $2 per conversation, per-user licenses, and flat-fee access. Its pricing examples meter actions rather than exposing raw model-token costs; a "where is my order?" workflow using two actions is illustrated as 40 credits, or $0.20. Salesforce has also added native MCP client support and access to partner MCP servers. It is trying to preserve its own agent platform and commercial meter without isolating itself from the broader tool ecosystem.

**Microsoft meters common credits over heterogeneous work.** Copilot Studio charges different credit amounts for classic answers, generative answers, agent actions, graph grounding, flow execution, and premium reasoning, and its computer-use feature can employ different model providers behind the same agent product. The pattern is not free inference; it is a metered agent platform with flexibility in the underlying intelligence.

**HubSpot charges for a verified business event.** Its move toward resolved-conversation and recommended-lead pricing is a direct attempt to align billing with customer value rather than model consumption—particularly attractive for small and medium-sized customers who do not want to design model-routing or governance infrastructure.

**Atlassian uses credits for higher-compute agent functions.** Rovo agent requests consume credits, with different amounts for ordinary requests, Deep Research, and other higher-compute functions. This illustrates an intermediate stage: the customer is not buying tokens directly, but the price still tracks computational effort more closely than a guaranteed business outcome.

**Infrastructure vendors compete on model choice.** Snowflake, AWS, Databricks, Oracle, and Google Cloud increasingly advertise model choice and common interfaces as a feature rather than a problem. These companies influence enterprise architecture, so a SaaS vendor attempting hard model lock-in may be working against the procurement and governance patterns its customers are adopting elsewhere.

## The Best Arguments for the Closed Approach

The closed approach is not irrational. There are valid reasons to prefer a first-party agent.

*End-to-end quality control.* The vendor can test a known model with known prompts, tools, data formats, and retry policies. Supporting arbitrary external agents multiplies the failure combinations.

*Security and compliance.* A poorly governed external agent could retrieve excessive data, expose secrets, perform unauthorized writes, misunderstand approval requirements, or create unmanageable support incidents.

*Supportability.* When the vendor controls the whole stack, support can reproduce a problem. With an unknown customer model and orchestration framework, responsibility becomes ambiguous.

*A simpler product experience.* Most customers, especially smaller ones, do not want to select models, configure credentials, monitor token use, or maintain agent infrastructure.

*Better optimization.* The vendor can use smaller models for easy steps, larger models for hard decisions, deterministic code where possible, and human escalation when required. Its all-in cost may be lower than the customer's do-it-yourself implementation.

*A data and feedback flywheel.* A first-party agent can collect better information about failures, corrections, accepted recommendations, rejected actions, and exceptional cases, and improve the workflow over time.

These are good reasons for the vendor's agent to be the default and best-supported option. They are not, by themselves, good reasons for it to be the only technically permitted one.

## When the Closed Strategy Can Win

There are circumstances in which a closed strategy may stay profitable for a long time.

If the vendor has **monopoly-like market power**—a product that is extremely hard to replace and controls a unique system of record—customers may accept forced agent usage. But that rests on distribution and switching costs, not on a superior token-resale model.

If the task is **highly regulated or dangerous**—releasing payments, changing medical records, approving insurance claims, modifying safety-critical infrastructure—the vendor may need to certify the complete workflow, including the model and agent runtime. External models could still be allowed eventually, but through a compatibility and approval program.

If the vendor **accepts substantial liability**, a company that guarantees the correctness of an outcome may reasonably require control over the execution stack.

If **customers overwhelmingly prefer simplicity**, as in much SMB software, an integrated agent with one bill and no configuration may dominate even when bring-your-own-model is technically possible.

And if the restriction is **temporary**, it is a different thing altogether. During an early product phase, a vendor may support only its first-party agent while it develops permission models, auditing, rate limits, external-agent certification, and stable action APIs. A temporary restriction based on product maturity is not a permanent tollbooth.

## Why Controlled Openness Beats Both Extremes

The academic platform literature helps clarify the choice. Kevin Boudreau's research on handheld computing platforms distinguished *granting access* from *giving up control*. In the observed sample, greater access for independent complementors was associated with as much as a fivefold acceleration in new-device development, while relinquishing control over the platform produced much smaller additional effects.

The lesson is not that every SaaS company should become open source. It is that a company can open access to complementors without surrendering ownership, governance, or monetization of the core platform. The vendor can retain control over identity, authorization, business rules, transaction integrity, certification, API versions, rate limits, auditing, and commercial terms, while letting customers and partners innovate at the agent layer.

That is controlled openness.

## The Platform-Envelopment Risk

The platform-envelopment literature describes how a company in an adjacent platform market can bundle its existing relationship with users into another market and weaken an incumbent's control of the customer interface. Applied to AI, the potential envelopers are Microsoft Copilot, ChatGPT, Claude, Google's agent ecosystem, enterprise agent platforms, and customer-built internal assistants. They may become the place where users begin work, with individual SaaS products appearing as tools behind that interface.

A closed SaaS company may try to stop envelopment by denying access. That can work when it has strong market power. For a replaceable SaaS company, however, the customer may simply respond: *we have standardized on our enterprise agent; we will buy applications that work with it.*

The defensive strategy is therefore not necessarily to own the chat window. It is to make the underlying system indispensable. A system-of-action vendor can capture value even if another company owns the conversation.

## The Seat-Pricing Problem Behind the Conflict

Many SaaS companies fear external agents for a reason that has little to do with security: agents threaten per-seat pricing.

Suppose a company has a thousand employees using a SaaS product. A central agent might allow two hundred of them—or twenty automated identities—to perform much of the same workload. If revenue depends entirely on human seats, open agent access may reduce revenue even as it increases product usage. That creates an incentive to prohibit external agents and force each user through a licensed first-party interface.

But that strategy tries to preserve the previous unit of value after the customer's workflow has changed. The more sustainable transition is to charge for the system of record, governed actions, platform capacity, verified outcomes, high-value human seats, and premium first-party agent capabilities. The adoption of credits, actions, conversations, and outcomes at Salesforce, Microsoft, HubSpot, and Atlassian reflects exactly this transition. A vendor that changes its meter can welcome external agents rather than treating them as seat thieves.

## A Recommended Technical Architecture

### Build a business-capability API, not merely a database API

The API should expose meaningful operations—reconcile an invoice, generate a refund quote, approve an access request, schedule maintenance, validate a configuration, close a support case—rather than only create-read-update-delete. A good agent API supports typed inputs and outputs, idempotency keys, dry-run or preview modes, preconditions, explicit side-effect declarations, asynchronous job status, cancellation, rollback where possible, webhooks and events, stable versioning, and machine-readable error recovery.

The business logic should stay in the SaaS product. The external agent should *request* the action, not reimplement the company's entire process.

### Treat MCP as an adapter, not as the architecture

An MCP server can expose the product's tools and resources to compatible agents, but the company should maintain a stable internal capability API underneath it. That protects the product if standards evolve. Conceptually, the layers run from external agents, through MCP, A2A, and SDK adapters, to a stable business-capability API, then to a policy engine and workflow runtime, and finally to authoritative records and transaction systems.

### Support several model deployment modes

A mature product could offer vendor-managed AI (one bill, full support); a customer-provided cloud model (an approved OpenAI, Anthropic, Google, Azure, AWS, or other endpoint); a customer private model running in the customer's own environment; a customer agent that uses the SaaS action API, with the vendor governing every action; and vendor-managed routing that selects among models to optimize quality, latency, and cost. Not every option needs to be available at every pricing tier.

### Treat agents as non-human identities

Every agent should have its own identity, an owner, an approved purpose, delegated-user context where applicable, short-lived credentials, explicit scopes, transaction limits, an expiration date, and a complete action history. The system should distinguish between "the user performed this action," "the agent performed it on behalf of the user," and "the autonomous service performed it under a standing policy."

### Put policy around actions

Rather than labeling an agent as simply allowed or prohibited, attach policy to each action. Reading a customer record and drafting a refund can be autonomous. Issuing a refund below $100 can be autonomous; between $100 and $1,000 it might require manager approval; above $1,000 it might require finance approval plus step-up authentication. Changing a bank account should never be autonomous.

### Build evaluation into production

The vendor needs continuous measurement of task-completion rate, false completion, human escalation, reversal rate, policy violations, customer corrections, latency, model and tool cost, and performance by model and by workflow version. That evaluation system is likely to become a stronger moat than prompt engineering.

### Maintain an outcome ledger

For each billable outcome, record the task request, expected success conditions, actions taken, approvals, evidence of completion, cost, final status, any later reversal or reopening, and the billing event. This makes outcome pricing auditable and reduces disputes.

### Certify external agents rather than prohibiting them

Access can be tiered: uncertified agents get read-only access with low rate limits; registered agents get limited write actions and a test environment; certified agents get production actions within approved scopes; strategic partners get higher capacity and advanced workflows; and customer-managed internal agents operate under access governed by the enterprise contract. This provides security without turning interoperability into an all-or-nothing decision.

## A Recommended Commercial Architecture

A strong commercial design has four components.

The **core platform subscription** charges for authoritative data, workflow configuration, compliance, reporting, human seats, and platform administration.

**Agent and API execution** charges for governed use of actions, workflows, tool calls, transaction capacity, and high-cost computation. The charge should apply whether the caller is the vendor's agent, the customer's agent, ChatGPT, Claude, Copilot, or an internal automated service.

The **managed agent service** charges a premium for zero setup, model routing, prompt and workflow maintenance, evaluation, monitoring, support, predictable cost, and better service levels.

The **guaranteed-outcome service** charges on verified results where success is objectively measurable: per resolved case, per reconciled invoice, per completed onboarding, per qualified lead, per verified compliance check, or as a percentage of recovered revenue or measured savings.

The managed agent should be attractive because it is economically and operationally superior—not because alternatives are artificially disabled.

## How Much Margin Is Reasonable?

A SaaS company can price against the customer's *next-best way of completing the work*, not only against the customer's raw model cost. Suppose a task costs $30 when done manually, and $8 all-in when the customer builds its own agent. The vendor-managed agent might sell the outcome at $5, against an internal cost of $0.75. A $4.25 gross profit is justified if the vendor provides the best combination of reliability, integration, implementation effort, support, governance, and risk reduction. Even a large multiple over model cost can be sustainable.

What is unlikely to be sustainable is a $5 charge on $0.10 of inference, with no meaningful validation, no unique workflow, and no accountability, enforced by blocking every alternative.

The right question is therefore not "what percentage markup over tokens is fair?" It is: *what business risk and operational burden did the vendor remove?*

## How Markets Will Differ by Segment

**Small businesses** will likely favor the first-party managed agent: one invoice, no model procurement, no API keys, no infrastructure, simple outcome pricing. Bring-your-own-model may exist but see limited adoption.

**Mid-market companies** will find the hybrid model strongest. They will want a supported default agent but may also use Microsoft, ChatGPT, specialized industry agents, or internal automation, and a blanket prohibition becomes a competitive disadvantage.

**Large enterprises** will treat controlled openness as essential. They care about central model procurement, data residency, private networking, identity, model approval, cost allocation, audit, and cross-system integration, and may reject a vendor that insists on an isolated, opaque agent stack.

**Regulated industries** allow the vendor to be more restrictive, but the winning model is likely a certified compatibility matrix rather than permanent single-model lock-in.

**Consumer applications** may remain well served by closed, integrated agents, since distribution, convenience, and product design can matter more than interoperability.

## Five Scenarios for the Next Five to Ten Years

**Models improve rapidly and inference becomes much cheaper.** This is the most hostile scenario for the forced-agent tollbooth. Customers can reproduce simple agent behavior cheaply, generic orchestration becomes less differentiated, model selection changes frequently, external agents become better at learning new software, and token markup becomes easier to expose. Open systems of record, action APIs, workflow engines, outcome providers, and governance platforms win; thin agent wrappers, UI-only SaaS, and token resellers with no proprietary execution layer lose.

**Models improve, but reliability remains difficult.** This is very favorable to specialized managed agents. The model may understand the task yet still require validation, exception handling, deterministic checks, human review, and policy enforcement, and a vertical SaaS vendor can capture substantial margin. Interoperability still matters, because customers will use several agents. The moat is reliability, not exclusivity.

**One or two general enterprise agents become the primary interface.** Application-specific chatbots become secondary, and SaaS products compete to be the preferred action and data providers behind a Microsoft, OpenAI, Anthropic, Google, or internally built front end. The best strategy is to be callable by every important agent and charge for the governed work.

**Regulation and data sovereignty fragment model deployment.** Customers may require different models by geography, data classification, department, use case, or regulatory regime. A model-neutral architecture wins, and a product permanently fused to one external model provider loses eligible customers.

**Frontier intelligence remains concentrated and expensive.** A SaaS company with aggregate buying power may negotiate better model economics than individual customers and profitably sell a managed service. Even here, a model-abstraction layer is prudent, since the vendor otherwise becomes dependent on its upstream supplier.

## Winners and Losers

The likely winners are **systems of record that become systems of action**, because they hold authoritative information and the permission to execute; **vertical SaaS companies with deep workflow knowledge**, which understand exceptions, regulations, and definitions of success; **vendors that accept outcome risk**, because they can charge against customer value rather than model cost; **multi-model governance and routing platforms**; **agent-friendly platforms**, which gain external agents as another distribution channel; and **evaluation and observability providers**, because as agents take consequential actions, proving they behave correctly becomes essential.

The likely losers are **pure token resellers**, whose input cost is visible, falling, and available from many suppliers; **thin wrappers** with no proprietary data, workflow, transactions, or evaluation; **closed mid-sized SaaS products without market power**; **UI-only products**, whose interaction layer general agents may absorb; **vendors that cannot objectively prove completion**, since customers resist outcome billing when the seller defines success unilaterally; and **SaaS companies that preserve seats at the expense of platform relevance**, protecting near-term revenue while losing the future workflow.

Across the strategic options, the best expected-value position is the same one this essay has argued for: a controlled open platform, plus managed and outcome-priced services.

## What a SaaS Company Should Do

**Do not ban external agents categorically.** Publish clear supported channels instead: REST or GraphQL APIs, SDKs, an MCP server, webhooks and events, and certified partner integrations.

**Charge external agents for platform value.** An external agent call need not be free. Meter governed actions, workflow executions, high-cost searches, transaction volume, premium data retrieval, and audit and compliance features.

**Make the first-party agent the easiest option.** It should offer one-click setup, known reliability, lower implementation cost, automatic model routing, full support, clear service levels, and transparent outcome pricing.

**Allow bring-your-own-model selectively.** Start with enterprise tiers and approved providers, and provide compatibility tests, minimum model requirements, supported context windows, tool-calling requirements, security rules, and a clear division of support responsibility.

**Protect the product's real moat.** Invest in workflow semantics, domain ontology, action permissions, exception handling, outcome labels, evaluations, audit, integrations, and transaction reliability. Do not overinvest in proprietary chat presentation as though the chat interface were the platform.

**Rebuild pricing before agents reduce seat counts.** Move toward a mixture of platform subscription, human seats, action capacity, managed-agent usage, and outcomes. That reduces the incentive to fight customer-controlled automation.

## A Decision Test for Executives

Before choosing the closed approach, management should be able to answer ten questions. What unique value remains if model prices fall another 90 percent? Can a competitor expose equivalent functions through an open agent API? Does the product own authoritative data, or merely display it? Does it have the legal and technical authority to complete transactions? Can task completion be objectively audited? Is the company accepting operational or financial risk when the agent is wrong? Are customers standardizing on an enterprise-wide agent platform? Would blocking that agent cause the customer to replace the agent, or to replace this SaaS product? Can external-agent calls become metered platform revenue rather than lost revenue? And is the first-party agent superior *without* contractual captivity?

If the answer to the last question is no, that is the most important product problem to solve.

## Conclusion

A business model that buys foundation-model inference, adds a thin agent layer, prohibits alternatives, and captures the difference as markup is likely to produce short-term monetization but weak long-term strategic positioning. It depends on controlling the doorway while the intelligence behind the doorway becomes cheaper and more interchangeable.

The better model is to maintain a secure, governed, commercially metered action platform that any authorized agent can use, while offering a first-party agent that delivers the lowest total cost and the strongest outcome guarantee.

If AI continues advancing quickly, the companies most likely to win are not those that own every chatbot. They are those that own the authoritative context, the workflow, the permissions, the transaction, the evaluation, and the accountability.

The most concise principle is this: **open the capability layer, retain control of the policy and transaction layer, and charge for trusted execution rather than captive intelligence.**
