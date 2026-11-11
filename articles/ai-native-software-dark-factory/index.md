# The AI-Native Software Dark Factory: From Goldratt to Generative Software Systems

*Why the software dark factory is not a Ford assembly line—and why compiler architecture, program synthesis, and the template generators of the low/no-code era give us a better operating model.*

**Research report · November 11, 2026**

## Executive summary

Calling an autonomous, AI-operated software organization a **dark factory** is a useful provocation—and an easily misunderstood analogy. A Ford factory repeatedly transforms physical inputs into more physical units. Software is not produced that way. Recompiling an application does not manufacture an economically distinct unit; copying code has negligible marginal cost; and a failed synthesis attempt can produce useful information rather than waste material.

Eliyahu Goldratt's Theory of Constraints (TOC) still has an important role, but principally **outside the computational engine**: it tells management to identify the condition limiting valuable outcomes and avoid optimizing activity that does not improve the whole system. It does not require us to model an AI agent as a workstation on an assembly line.

Three other traditions describe the engine more accurately:

1. **Compiler architecture and program synthesis:** intent becomes increasingly formal representations, candidate implementations, diagnostics, and executable artifacts. The generator searches; the checker supplies feedback. A Counterexample-Guided Inductive Synthesis (CEGIS) loop is a stronger analogy than a conveyor belt.
2. **Generative programming and software product lines:** the system uses reusable templates, component families, feature models, architectures, and generation rules. The low/no-code era already understood that many applications should be *configured and generated*, not hand-written from scratch.
3. **An AI-native extension:** an LLM can synthesize variations that the original generator designer did not anticipate. If a variation recurs, an agent can propose turning that solution into a reusable generator, verifier, or skill. Promotion must be gated by independent, cross-variant evidence.

The resulting system is best described as an **AI-native generative software product line with probabilistic synthesis and independent assurance**. Its central loop is:

> **Describe intent → reuse known engineering knowledge → configure and compose → synthesize the missing variation → verify → deliver → extract recurring knowledge → validate a reusable asset → repeat.**

The most valuable output may not be a specific application. It may be an enduring **software-producing asset**: a template, generator, domain model, reference implementation, test oracle, verification harness, or reusable architectural constraint that makes future work cheaper and safer.

For management, the recommended engineering metric is **cost per independently and correctly accepted solution**, alongside human attention, elapsed time, escaped defects, and downstream value. That engineering metric is *not* Goldratt's accounting definition of throughput, which concerns money generated through sales less truly variable costs.

This report develops the architecture, economics, failure modes, measurement system, experiments, and implementation roadmap.

---

## 1. Goldratt's factory is useful—but only up to a point

In *The Goal*, Goldratt asks managers to stop confusing local efficiency with overall progress. A machine can run at maximum utilization while inventory builds in front of another machine. Producing more at a non-constraint can make the whole factory worse, not better. TOC's five focusing steps—identify, exploit, subordinate, elevate, and repeat—ask managers to improve the system at its actual constraint rather than optimizing every work center independently. Goldratt's work separately develops manufacturing-oriented mechanisms such as Drum-Buffer-Rope (DBR). See the [Goldratt Five Focusing Steps](https://www.toc-goldratt.com/en/toc-application/five-focusing-steps) and [Drum-Buffer-Rope](https://www.toc-goldratt.com/en/toc-application/drum-buffer-rope).

For AI coding, this insight immediately challenges attractive but weak productivity metrics. How many agents were running? How many tokens were consumed? How many commits did they create? How many pull requests passed their own tests? None of those answers establishes whether the organization solved more valuable problems.

An AI coding fleet could increase generated code by a factor of ten while making an engineering team less productive because human review, integration, or defect investigation became the real constraint. Alternatively, the team might discover that the apparent bottleneck is not verification capacity but *underspecified intent*: the generator is very fast at producing wrong answers to an ambiguous request.

The distinction matters because not all constraints are simple queues. They may be:

- **Capacity constraints:** scarce compute, long-running CI, limited human review, slow integration environments.
- **Information constraints:** unclear requirements, absent reference behavior, inaccessible domain knowledge.
- **Capability constraints:** a model or algorithm cannot find a satisfactory candidate under the budget.
- **Assurance constraints:** the available oracle cannot distinguish correct behavior from plausible-looking mistakes.
- **Value constraints:** the organization can produce features faster than users adopt them.

DBR can be useful for the *capacity-constrained subproblems*—for example, controlling how many concurrent agent runs feed a scarce hardware-in-the-loop verification server. It is not a universal description of the software creation process.

### Where the Ford metaphor breaks

A physical assembly line typically makes another product from another batch of material. A software synthesis run constructs and evaluates a candidate description of behavior. It can be repeated, branched, rolled back, compared, or revised at negligible copying cost. Its route is not fully predictable. Failure can refine the specification, uncover an architectural impossibility, or show where tests are inadequate.

Even the word *rework* changes meaning. Recompiling correct code is not re-manufacturing a car; searching for an implementation is not repeating a rivet operation. The better management question is not *How many units can this station produce?* It is *What is limiting the rate at which the system resolves valuable, trustworthy engineering problems?*

Goldratt remains a discipline of global optimization, not the computational blueprint.

## 2. The compiler is a better computational analogy

A conventional compiler transforms source code according to defined language semantics. Its front end parses and analyzes input; intermediate representations make transformations manageable; optimization and lowering stages produce a target artifact; and deterministic checks reject invalid programs.

An AI-native compiler starts from a much less precise source language: human intent. Its front end may need to discover what the user actually means, what interfaces already exist, which nonfunctional constraints are binding, and what must remain invariant.

A useful conceptual contract is:

\[
\mathrm{IEC}(I,C,E,A)\rightarrow(P,\mathcal{E})
\]

Here **IEC** means *Intent-to-Executable Compiler* (a proposed architectural name, not an established research term). \(I\) is intent, \(C\) is constraints, \(E\) is execution environment, \(A\) is the library of reusable production assets, \(P\) is the resulting product, and \(\mathcal{E}\) is the evidence supporting acceptance.

A correct IEC must also be able to return *ambiguous specification*, *contradictory constraints*, *search budget exhausted*, or *verification inconclusive*. Success is not the only legitimate output.

| Conventional compiler | AI-native interpretation | Fundamental difference |
|---|---|---|
| Source language | Natural-language intent and structured requirements | Meaning may be ambiguous |
| Front end | Requirements analysis, interface discovery, constraint extraction | May need conversation and investigation |
| Intermediate representation | Domain model, feature model, API contracts, invariants | No universal IR for all application classes |
| Optimization | Search and compare implementation strategies | Probabilistic, cost-sensitive, sometimes divergent |
| Back end | Generate or assemble source, configuration, tests, schemas | May invent new structures |
| Diagnostics | Compile errors, test failures, counterexamples | Feedback must be preserved across attempts |
| Driver/runtime | Agent harness, sandbox, tool and model routing | Determines budgets and action policy |
| Acceptance | Executable tests, static analysis, formal methods, independent checks | Correctness relative to a contract, not automatically to intent |

The most important design implication is **the LLM should not be the whole compiler**. Explicit state, domain models, templates, deterministic transformations, build tools, and independent verification should exist outside a model's ephemeral conversation.

A compiler analogy also clarifies a critical caveat: unlike trusted compiler optimization passes, an unconstrained LLM transformation does *not* preserve program semantics by construction. Semantic preservation is an obligation to test or prove, not an assumption.

## 3. Program synthesis and the value of counterexamples

Program synthesis asks a computer to find a program satisfying a specification. The established literature is broader than LLM code generation: it includes constraint solving, examples, sketches, grammars, deductive techniques, and oracle-guided search. See Gulwani, Polozov and Singh's [*Program Synthesis* survey (2017)](https://www.microsoft.com/en-us/research/publication/program-synthesis/).

The particularly relevant framework is **Counterexample-Guided Inductive Synthesis (CEGIS)**, prominent in Armando Solar-Lezama's synthesis-by-sketching work and teaching. Its loop is not simply *generate → run → retry*. A checker produces a counterexample, and that counterexample narrows the permissible search space. See [Solar-Lezama's MIT synthesis lecture](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture17.htm) and [*Program Synthesis by Sketching* (2008)](https://people.csail.mit.edu/asolar/papers/thesis.pdf).

The logical difference is profound.

If an agent tries one implementation of an arbiter and discovers a starvation trace, a useful harness remembers the fairness obligation, the trace, and the class of flawed arbitration policies it rules out. A second attempt is now better informed. If the agent forgets the trace and repeats a superficially different version of the same approach, the organization has bought more inference without gaining much knowledge.

A robust task state therefore includes at least:

| Persistent state | Reason it must outlive the conversation |
|---|---|
| Specification and versions | Know exactly what the agent is trying to satisfy |
| Architectural decisions | Avoid undoing intentional tradeoffs |
| Invariants and constraints | Protect requirements across revisions |
| Candidate history | Compare strategies rather than only final patches |
| Counterexamples and failure fingerprints | Prevent correlated, uninformative retries |
| Reused template and generator versions | Make generated results reproducible |
| Checker and evidence versions | Prevent moving the acceptance criteria silently |
| Budget and risk tier | Decide whether to continue, branch, escalate, or stop |

This is closer to a **stateful search controller** than a chat transcript. Not every failed test is a formal counterexample, and not every LLM retry implements CEGIS. But CEGIS provides the right design goal: **failures should accumulate information that changes the next decision**.

## 4. The crucial correction: this is also a low/no-code template generator

The compiler analogy explains transformation, but it misses the most economically important historical precedent: **software generators were already a major idea before LLMs**.

Greenfield and Short's [*Software Factories: Assembling Applications with Patterns, Models, Frameworks, and Tools* (2004)](https://www.softwarefactories.com/TheBook.html) described systems built through reusable patterns, domain-specific languages, models, frameworks, and generators. Czarnecki and Eisenecker's [*Generative Programming: Methods, Tools, and Applications* (2000)](https://gsd.uwaterloo.ca/publications/view/86.html) established a discipline for building generative domain models and using them to construct members of a software family. The [Software Engineering Institute's software product-line work](https://www.sei.cmu.edu/library/software-product-lines-collection/) emphasizes managed commonality, variability, and shared core assets.

The low-code/no-code era operationalized part of this insight. A platform could generate a form, CRUD interface, workflow, report, or service from configuration. The platform builder anticipated a set of variation points, and the user chose among them.

This is a more faithful antecedent of a software dark factory than Ford's conveyor belt. **You are not producing a physical unit repeatedly; you are instantiating and customizing software from reusable engineering knowledge.**

Historically, the principal limitation was the boundary of the generator's design. If a low-code platform did not support a particular authorization rule, database pattern, or distributed-system behavior, a human developer had to extend it or work around it.

An LLM changes the boundary. It can:

1. Recognize that a requirement matches an existing product family.
2. Retrieve a vetted template, component, feature model, or reference design.
3. Configure the known variation points deterministically.
4. Synthesize a bounded residual feature that the original generator did not anticipate.
5. Validate the whole result using a domain-specific verification contract.
6. Propose adding a *repeated* new variation to the future generator's model.

That is neither ordinary compilation nor ordinary low-code. It is **template-first generation with an open-ended synthesis fallback**.

### The product-line advantage

| Production mode | Typical situation | Default decision |
|---|---|---|
| Template instantiation | Known family, bounded permitted variation | Configure and generate |
| Template plus synthesis | Familiar architecture with one novel rule or integration | Reuse stable core, synthesize delta |
| Specification-guided synthesis | New algorithm with strong checker | Search and refine against counterexamples |
| Exploratory design | Ambiguous intent or weak oracle | Investigate and formalize before building |
| Generator investment | Repeated problem class with clear expected future uses | Create and validate a reusable software-producing asset |

The most promising default is **reuse → configure → synthesize the delta → independently verify**. It preserves the economics of validated knowledge while allowing greater flexibility than the old low-code platforms.

## 5. Two distinct outputs: products and production capabilities

A traditional coding task produces an implementation. A mature dark factory should produce two classes of artifact:

**Software product:** a deployable feature, application, migration, service, or hardware-development utility that solves a specific problem.

**Software-producing asset:** a reusable generator, template, feature model, benchmark, verification contract, architectural pattern, test harness, reference implementation, transformation rule, or skill that changes the economics of solving *future* problems.

The second class is the source of compounding returns.

Consider a team repeatedly building FIFO variants. Producing a single correct FIFO is valuable. Producing a parameterized RTL generator with documented depth/width/configuration constraints, ready/valid semantics, independent reference model, SVA properties, lint and synthesis checks, and a validated matrix of configurations creates a much more durable capability.

The same principle applies to API services, migration scripts, dashboards, protocol adapters, and testing environments.

But this **does not** imply every successful solution should become a template. Generalization has fixed cost, maintenance cost, obsolescence risk, and a possibility of propagating one hidden error to many outputs. A generator built for an imagined reuse case is a liability, not automatically an asset.

A governed promotion process should be:

**Observed recurrence → candidate abstraction → explicit applicability and variation model → cross-variant verification → versioned trusted asset → monitored reuse → maintenance or deprecation.**

The agent may propose an abstraction. The agent should not declare its own new generator trusted merely because its first example passes.

## 6. Unified reference architecture

The proposed system combines compiler decomposition, product-line reuse, synthesis, and independent assurance. The diagrams are conceptual; they do not imply each box must be a separate service.

### System architecture

    Human / machine intent
               |
               v
    Specification + constraints + invariants
               |
               v
    Domain model / feature model / task IR
               |
               v
       Harness and search controller
               |
        +------+----------------------+ 
        |             |              |
        v             v              v
    Validated      Partial       Uncovered
    family         coverage      novelty
        |             |              |
        v             v              v
    Configure      Retrieve       Synthesize
    generator      core assets    from spec
        |             |              |
        +-------------+--------------+
                      |
                      v
                Candidate software
                      |
                      v
             Sandbox + tool execution
                      |
                      v
             Independent assurance
               /        |         \
         Counterexample  |       Uncertain
              |        Accept       |
              v           |         v
         Persistent       v     Clarify/escalate
         task state   Evidence bundle
              |           |
              +---retry   v
                  Deployed product
                      |
                      v
          Candidate recurring pattern
                      |
                      v
            Cross-variant validation
                      |
                      v
             Trusted asset registry
                      |
                      +----> future harness runs

The architecture deliberately separates **build plane** and **assurance plane**. The generation system may write tests as part of development, but those tests are not the only acceptance authority.

The system should select among four kinds of output: accepted implementation, accepted reusable asset, explicit escalation, or principled failure. These distinctions help avoid confusing plausible code with finished engineering work.

### Harness responsibilities

The harness owns the control plane: state persistence, task decomposition, tool permissions, sandboxes, model routing, context construction, resource budgets, branch/retry policy, failure deduplication, evidence collection, and escalation.

Evidence that harness design matters is not merely intuitive. [SWE-agent (2024)](https://arxiv.org/abs/2405.15793) studied the agent-computer interface as part of coding-agent performance. [*An Empirical Study of Harness Design for Coding Agents* (2026)](https://arxiv.org/abs/2609.20804) reports model-dependent effects from harness choices such as context management and action interfaces. This does not prove that a harness always matters more than the model; it supports treating **model × harness × tools × assets × verifier** as the unit of performance.

## 7. Assurance must be structurally independent

A passing compilation proves that a program passes certain language checks. Passing a test suite proves it met the expectations encoded in those tests. Neither establishes that the specification captured the user's real intent.

An AI-native compiler has two separate correctness problems:

1. **Implementation correctness:** did the generated artifact satisfy its stated contracts?
2. **Specification correctness:** were those contracts the right expression of the user's needs?

Formal methods can offer strong guarantees about the first question *relative to adequately expressed properties*. They cannot, by themselves, make an ambiguous or incomplete human requirement correct.

This is why the verifier must be more than another LLM asked to say whether a patch "looks good." It should draw on independent and heterogeneous evidence: hidden specification-first tests, property checks, model checking, reference models, regression tests, static and security analysis, integration environments, and runtime observations.

Recent research illustrates both directions of oracle failure. [SWE-Gate (2026)](https://arxiv.org/html/2609.04167v1) finds that functional test success can coexist with violations of other objective constraints. [OpenAI's February 2026 SWE-bench Verified audit](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) details issues with benchmark tests and contamination—evidence that externally supplied tests can also mismeasure progress. A [2026 preprint on independent assurance](https://arxiv.org/html/2610.28667v1) motivates fresh-context review, while its small study should not be treated as universal proof.

An assurance design can distinguish four internally proposed tiers:

| Tier | Representative changes | Acceptance and release approach |
|---|---|---|
| A0 — Non-executable | Documentation, comments, examples | Syntax and schema checks; policy-gated automatic acceptance |
| A1 — Low-risk reversible | Bounded refactors, isolated UI changes | Independent tests, static checks, rollback; automation only after reliability is measured |
| A2 — Production behavior | APIs, persistent workflows, transformations | A1 plus constraints, integration, security, and canary; human approval initially |
| A3 — Critical/irreversible | Access control, payments, destructive migrations | Explicit contracts, threat analysis, heterogeneous oracles, recovery plans, accountable human approval |

These tiers are **proposals**, not an external standard.

Every accepted higher-risk artifact should carry an **evidence bundle**: specification version, generator and template versions, model/harness versions, input and environment revisions, diff hashes, verification results, counterexamples, residual uncertainty, required approvals, and deployment/rollback provenance. [SLSA provenance](https://slsa.dev/spec/v1.2/build-provenance) and [NIST's Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) provide established foundations for the supply-chain and security aspects.

## 8. Economics of reusable templates versus bespoke synthesis

The correct question is not "Can an AI agent build a generator?" It is "Will investing in this generator improve future outcomes more than repeatedly synthesizing the solutions?"

Let:

- \(F\): fixed cost to build and validate a generator.
- \(C_b\): expected cost per bespoke future solution.
- \(C_t\): expected cost per template-derived solution.
- \(M\): template maintenance allocation per use.
- \(R_b,R_t\): expected defect/risk cost per use under each approach.

Ignoring discounting, the break-even use count is:

\[
N^*=\frac{F}{(C_b+R_b)-(C_t+M+R_t)}
\]

when the denominator is positive.

Suppose the fixed investment is **$2,000**, bespoke synthesis costs **$200** per applicable problem, and template-derived customization and validation cost **$20**. Temporarily ignoring maintenance and risk, the investment breaks even on the **12th use**, since \(2000/(200-20)=11.11\).

That example is illustrative, not observed operating data. If the generator never sees 12 applicable future uses, it is a poor investment. If a hidden template defect is copied across 100 deployments, the risk term can dominate the apparent savings.

The more general investment rule discounts uncertain future reuse:

\[
NPV_{asset}=-F+\sum_{t=1}^{T}
\frac{q_t\left(C_{b,t}-C_{t,t}-M_t-\Delta R_t\right)}{(1+r)^t}
\]

Here \(q_t\) represents expected applicable uses during period \(t\); \(r\) is the discount rate; and \(\Delta R_t\) is additional risk cost for the template approach. This is a planning model, not a claim that every cost can be estimated precisely at the outset.

### Search has different economics from an assembly line

Under a toy model with independent attempts, fixed cost \(c\), and success probability \(p\), expected attempt cost to first success is \(c/p\). In real coding, retries are correlated, costs vary, and failure diagnostics intentionally change later success probabilities.

Thus the harness's decision is not simply *run more agents*. It can choose to revise, branch into alternative designs, switch model, retrieve an asset, improve the verifier, ask for clarification, or stop.

At fleet level, compute should be allocated where its **expected marginal contribution to correctly solved, valuable tasks** is highest. Brute-force concurrency is only attractive where the diversity and extra success probability justify compute and human-review costs. Research on [test-time compute allocation](https://arxiv.org/html/2408.03314v1), although originally based on reasoning tasks rather than production software, motivates experiments rather than a fixed universal policy.

## 9. What to measure

A productive dark factory is not necessarily the one using the most tokens or generating the most lines of code.

At the **engineering** layer, use **cost per correctly accepted solution (CCAS)** as the central efficiency measure:

\[
CCAS=\frac{C_{model}+C_{tool}+C_{CI}+C_{human}
+C_{rework}+E[L_{escaped}]}{N_{correctly\ accepted}}
\]

It must be interpreted alongside correctness, elapsed time, human attention, task difficulty, and severity-weighted escaped risk. Otherwise the metric can reward picking easy tasks or underinvesting in assurance.

At the **business** layer, track value realized by users or customers. Accepted code is not itself Goldratt throughput, and neither is a completed pull request. [DORA's current delivery metrics](https://dora.dev/guides/dora-metrics/) remain useful downstream guardrails; its [2026 discussion of tokenmaxxing](https://dora.dev/insights/finding-balance-in-the-era-of-tokenmaxxing/) warns against promoting activity into the objective.

| Measurement | Why it matters |
|---|---|
| Independently adjudicated acceptance rate, stratified by difficulty | Whether the factory solves the intended work |
| Total economic cost per accepted task | Tradeoffs between model, CI, tools and human time |
| Wall-clock time to accepted solution | Responsiveness and queueing effects |
| Human minutes per accepted task | Actual autonomy, not agent utilization |
| False acceptance and escaped failures | Whether "green" means trustworthy |
| Repeated-failure fingerprints | Search waste and missing state |
| Asset reuse and savings per use | Economic return on templates/generators |
| Template defect delta and useful life | Compounding reliability versus propagated mistakes |
| Verification and CI queue latency | Genuine shared-capacity constraints |
| Delivery stability and business outcomes | Whether engineering acceptance leads to value |

Use a private, fresh evaluation suite representative of real repositories; treat public benchmarks as external calibration rather than the final acceptance authority. Track model, harness, template, verifier, and environment versions with every run. [OpenTelemetry's 2026 GenAI observability guidance](https://opentelemetry.io/blog/2026/genai-observability/) offers a useful tracing baseline, with careful avoidance of indiscriminate prompt/secret capture.

## 10. Three experiments to run before scaling the fleet

The research is not a reason to build a massive generic platform immediately. It suggests a small set of controlled experiments.

### Experiment A — Model capability versus harness architecture

Use matched tasks, identical acceptance criteria, and comparable budgets in a **2 × 2 factorial**: stronger/weaker model crossed with baseline/enhanced harness.

The question is whether improvements come from the model, the harness, or their interaction. Success should be measured by correct acceptance, cost, latency, and human intervention—not an agent's self-assessment. Then ablate individual harness mechanisms: explicit persistent state, context management, tool interfaces, planning, and failure memory.

### Experiment B — Verification investment

Evaluate the same candidate patches with a basic test suite and an independently authored, enhanced assurance suite. Include held-out cases, constraint compliance, property/mutation checks where practical, and manually adjudicated disagreements.

The question is how much investment in the oracle lowers incorrect acceptance and downstream rework. A second model reviewer should not be assumed independent merely because it uses a different vendor.

### Experiment C — Scheduling and search economics

For difficult tasks, compare three policies under equal **total economic budget**:

- Sequential repair of one candidate with preserved failure knowledge.
- Multiple independent parallel candidates with comparison and selection.
- An adaptive controller that can revise, branch, change model, improve checker, retrieve templates, escalate, or stop.

Measure true acceptance, diversity of failure, cost, time, and review burden. A pilot of around 80–120 matched tasks can expose large effects and estimate variance; it does not automatically establish statistically small differences. Plan confirmatory work accordingly.

All cost figures and sample sizes here are **illustrative engineering starting points**, not measured facts about a particular team.

## 11. Operating model for a small AI-native engineering team

A four-engineer team directing an agent fleet needs ownership of *production knowledge and assurance*, not only a backlog of generated code.

One workable responsibility split is:

| Primary ownership | Responsibility |
|---|---|
| Harness and infrastructure | Execution control, tool interfaces, sandboxes, context/state, tracing and budget policy |
| Assurance and evaluation | Private benchmarks, independent test oracles, correctness adjudication, evidence bundles |
| Generative assets | Template catalog, product-family models, versioning, cross-variant validation, asset economics |
| Integration and delivery | Product contracts, repository integration, security/release policy, downstream feedback |

Responsibilities should overlap through review and rotation. Otherwise an ostensibly automated factory merely creates four new organizational silos.

A weekly constraint review should ask: **What prevented the greatest amount of valuable, trustworthy work from being accepted last week?** The answer might be ambiguous requirements, the wrong template, a repeated model failure, a slow shared verifier, inconsistent architecture, reviewer decisions, or lack of downstream demand. The team should elevate the leading constraint, not indiscriminately increase concurrency.

Three behaviors deserve explicit policy:

1. **Choose reuse before reinvention** when an applicable trusted asset exists.
2. **Preserve and classify failures** so retries contribute information.
3. **Separate production from certification** so the generator cannot award itself a pass.

The role of the engineer then shifts toward establishing intent, hardening oracles, managing production assets, and adjudicating genuinely novel tradeoffs.

## 12. A phased roadmap

| Horizon | Build | Learn | Exit condition |
|---|---|---|---|
| Days 0–30 | Task taxonomy, assurance tiers, reproducible traces, initial private task corpus, sandbox rules, evidence schema | Baseline task cost and verification accuracy | Every run has known inputs, versions, cost, and independently recorded result |
| Days 31–60 | Versioned asset registry, candidate failure memory, independent verifier plane | Model × harness pilot, false-accept study | Can explain the current limiting constraint with evidence |
| Days 61–90 | Template-first routing and first validated product families | Search strategy experiment, per-asset break-even estimates | Measurable cost or reliability gain without higher escaped risk |
| Days 91–180 | Asset-promotion gates, adaptive compute budget, selective A0/A1 automation, provenance and rollback | Repeat experiments as architecture changes | Trusted assets reduce total cost and human attention across real repeated tasks |

**Do not begin by auto-promoting every AI-generated skill or template.** Begin by identifying genuinely recurring classes of work; specify their permitted variability; build independent tests for the *family*, not just one instance; and only then allow the new generator to become trusted infrastructure.

The first high-quality production assets may be unglamorous: reference models, assertion libraries, known-good project scaffolds, robust smoke-test suites, environment reproducers, or stable interface contracts. Those assets can outperform a fancy "self-improving" agent when they remove repeated uncertainty.

## 13. Principal risks and unanswered questions

**Specification error.** A generator can be perfectly compliant with the wrong contract. Acceptance must include requirements review, examples, invariants, and feedback from the actual user or environment.

**Oracle overfitting.** If the builder sees every test, it can optimize for the tests instead of the intended behavior. Hidden checks, orthogonal methods, and runtime observations reduce—not eliminate—this risk.

**Correlated retries.** Re-running the same model from the same prompt may consume resources without exploring distinct alternatives. Preserve failure fingerprints and use branching only where it produces meaningful diversity.

**Template amplification.** A hidden bug in a frequently reused generator can spread much farther than a one-off bug. Stronger cross-variant tests and version pinning are part of the economic case for reuse.

**Asset proliferation.** Automatically abstracting every success creates a library nobody can understand or trust. Reuse evidence, ownership, deprecation, and maintenance budgets are necessary.

**Architectural drift.** Synthesizing unbounded variations can silently violate the assumptions of an otherwise stable product family. Keep applicability boundaries explicit, and elevate unknown variations for review.

**Security and authority.** Coding agents execute commands and touch repositories, secrets, networks, and data. Sandboxing, least privilege, review gates, secure-development controls, and provenance cannot be reduced to prompt instructions. See [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [its GenAI community profile](https://csrc.nist.gov/pubs/sp/800/218/a/final), and [SLSA provenance](https://slsa.dev/spec/v1.2/build-provenance).

**Model/harness lock-in.** Templates written as opaque prompts for one model can lose value during upgrades. Prefer versioned explicit contracts, language- and tool-neutral data formats where possible, and benchmark-based migrations.

**Self-modification.** Agents can propose changes to the harness, evaluation suite, and generator catalog. They should not immediately deploy modifications to the systems that judge their own work. Use frozen benchmarks, independent evaluation, canaries, and rollback.

The open research questions are consequential: How often does template-first synthesis outperform unconstrained synthesis for different task families? What is the optimal granularity of reusable knowledge? Can a system learn new feature models reliably from repeated examples? When is a human clarification cheaper than further compute? How do we detect that an oracle's definition of success has drifted away from the real user's goal? How much of the long-run performance advantage belongs to reusable assets rather than the current frontier model?

## 14. Conclusion: a generator of generators

The phrase *dark factory* suggests a physical building that can run without lights because robots do the repetitive labor. That is not an adequate theory of AI-native software engineering.

The better analogy begins with **compilers**, extends through **program synthesis**, and reaches back to the **low/no-code generation and software-product-line tradition**. The LLM is one part of the machinery, not the whole system. The harness orchestrates a constrained search. The template library captures recurring engineering knowledge. Independent assurance determines which results are trustworthy. Goldratt's Theory of Constraints helps management improve the overall economics rather than the activity of individual components.

The defining AI-era extension is that the system can help **build and improve its own reusable production capabilities**—new templates, test oracles, reference models, and generators—subject to evidence-based promotion.

There are therefore two distinct production loops:

**Loop 1: Produce software.** Intent → configure/reuse → synthesize → verify → deliver.

**Loop 2: Produce software-producing assets.** Observe repeated solutions → generalize → validate across variations → version and promote → lower the cost of Loop 1.

The long-run asset is not merely generated source code. It is **a growing, independently checkable body of executable organizational knowledge**.

> **A software dark factory is not an assembly line that writes code. It is a generative compiler and template system that converts intent into verified software—and, when reuse justifies it, converts engineering experience into better software generators.**

---

## Selected primary sources and further reading

**Foundations**

1. Goldratt, E. M. *The Goal* (1984), and Goldratt TOC resources: [Five Focusing Steps](https://www.toc-goldratt.com/en/toc-application/five-focusing-steps) and [Drum-Buffer-Rope](https://www.toc-goldratt.com/en/toc-application/drum-buffer-rope).
2. Greenfield, J., and Short, K. *Software Factories: Assembling Applications with Patterns, Models, Frameworks, and Tools* (2004). [Book information](https://www.softwarefactories.com/TheBook.html).
3. Czarnecki, K., and Eisenecker, U. W. *Generative Programming: Methods, Tools, and Applications* (2000). [University of Waterloo bibliography](https://gsd.uwaterloo.ca/publications/view/86.html).
4. Carnegie Mellon Software Engineering Institute. [Software Product Lines collection](https://www.sei.cmu.edu/library/software-product-lines-collection/); [Feature-Oriented Domain Analysis (FODA), 1990](https://www.sei.cmu.edu/library/feature-oriented-domain-analysis-foda-feasibility-study/).
5. Gulwani, S., Polozov, O., and Singh, R. [*Program Synthesis* (2017)](https://www.microsoft.com/en-us/research/publication/program-synthesis/).
6. Solar-Lezama, A. [*Program Synthesis by Sketching* (2008)](https://people.csail.mit.edu/asolar/papers/thesis.pdf); [CEGIS teaching material](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture17.htm).

**Modern agent, harness and assurance research**

7. Yang et al. [*SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering* (2024)](https://arxiv.org/abs/2405.15793).
8. Fan et al. [*An Empirical Study of Harness Design for Coding Agents* (2026)](https://arxiv.org/abs/2609.20804). Recent preprint.
9. [*SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents* (2026)](https://arxiv.org/html/2609.04167v1). Recent research.
10. [*Who Verifies the Builder? Toward Independent Assurance for Agent-Produced Software* (2026)](https://arxiv.org/html/2610.28667v1). Recent preprint with a limited study.
11. Snell et al. [*Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters* (2024)](https://arxiv.org/abs/2408.03314). Reasoning-domain results; software transfer requires validation.
12. [*SWE-Bench Pro*](https://arxiv.org/html/2509.16941v1) and [OpenAI's SWE-bench Verified evaluation audit (2026)](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/).

**Measurement, governance and provenance**

13. DORA. [Software delivery performance metrics](https://dora.dev/guides/dora-metrics/), [2025 State of AI-assisted Software Development](https://dora.dev/dora-report-2025/), and [Finding Balance in the Era of Tokenmaxxing (2026)](https://dora.dev/insights/finding-balance-in-the-era-of-tokenmaxxing/).
14. OpenTelemetry. [GenAI Observability (2026)](https://opentelemetry.io/blog/2026/genai-observability/).
15. NIST. [Secure Software Development Framework, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) and [AI-specific profile, SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final).
16. SLSA. [Build Provenance Specification](https://slsa.dev/spec/v1.2/build-provenance).

*Methodological note: This is a conceptual synthesis of established software-engineering traditions and selected contemporary empirical work. Proposed architectural terms, governance tiers, cost equations and roadmap are recommendations, not externally validated industry standards. Numerical examples are illustrative; recent preprints are explicitly distinguished from foundational literature.*
