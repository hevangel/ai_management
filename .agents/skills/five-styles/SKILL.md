---
name: five-styles
description: Transform raw material — a conversation transcript, brainstorming notes, rough draft, or existing article — into five structurally different management/business articles in the editorial logics of MIT Sloan Management Review, Harvard Business Review, McKinsey & Company, BCG, and Bain & Company. Use when the user asks to "rewrite this in the five styles", wants "a Sloan/HBR/McKinsey/BCG/Bain version", mentions the five-styles rewriter, or wants one idea developed into a five-publication case study. Never produces five synonym-swapped copies; extracts the intellectual core and verifies facts first.
---

# Five-Style Management Article Rewriter Skill

Origin: the owner's ChatGPT conversation "Explain Vibeitda"
(https://chatgpt.com/share/6aa621ef-59d0-83e8-9cb4-0083364b9f6b), whose final message is
this specification. The scraped transcript is archived at
`sratchpad/vibeitda_chatgpt_transcript.md`; strip chat-export artifacts (favicon citation
images, `utm_source=chatgpt.com` links, `citeturn` tokens) when quoting from it.

## Purpose

Transform raw material — including conversation transcripts, brainstorming notes, rough drafts, research notes, or existing articles — into five distinct management/business articles modeled on the editorial logic of:

1. MIT Sloan Management Review
2. Harvard Business Review
3. McKinsey-style insight article
4. BCG-style strategy article
5. Bain-style value-creation article

The five outputs must be structurally and intellectually different. Do not merely rewrite the same article five times with different vocabulary.

---

## Core Principle

Before writing any article, first determine:

- What is the central thesis?
- What observation triggered the thesis?
- What is genuinely new or counterintuitive?
- What assumptions from the pre-existing worldview are being challenged?
- What evidence supports the argument?
- What evidence weakens or qualifies it?
- What examples or anecdotes make the idea concrete?
- What management problem follows from the thesis?
- What questions remain unresolved?
- Which claims are facts, hypotheses, analogies, or speculation?

Preserve the author's original insight whenever possible.

Do not invent personal experiences, examples, data, research findings, or beliefs that were not present in the source material or independently verified.

When the source is a conversation, distinguish between:

- early exploratory ideas
- ideas the author later rejected
- ideas the author refined
- and the final position

Use the most developed version of the argument.

---

## Stage 1: Extract the Intellectual Core

Before generating the five articles, create an internal source model containing:

### Central Thesis

Express the strongest version of the argument in one or two sentences.

### Conventional View

Explain the established assumption, management practice, or worldview being challenged.

### New Observation

Identify what has changed.

### Causal Mechanism

Explain why the change matters rather than merely describing it. Use a simple causal chain when appropriate: A → B → C → managerial consequence.

### Key Tension

Identify the unresolved trade-off, contradiction, or uncertainty.

### Evidence

Separate:

- empirical evidence
- research findings
- company examples
- personal observations
- logical arguments
- analogies
- speculative implications

### Useful Concepts

Extract any original terminology, equations, frameworks, metaphors, or memorable phrases from the source. Preserve particularly strong phrases when appropriate.

### Managerial Implications

Identify what executives, managers, investors, or employees would need to do differently if the thesis was correct.

---

## Stage 2: Research and Verification

When the article depends on current facts, companies, AI capabilities, market conditions, economic data, or recent research, verify them before writing.

Prefer:

- original research papers
- NBER
- academic journals
- government statistics
- company filings
- authoritative industry research
- major consulting research when primary evidence is unavailable

Do not use a consulting firm's claim as proof merely because the article is being written in consulting style.

Distinguish clearly between:

- what current evidence demonstrates
- what evidence suggests
- and what is a forward-looking hypothesis

Avoid fake precision. If no reliable human-to-AI substitution ratio exists, state so rather than inventing one.

---

## Stage 3: Generate Five Independent Articles

Each article should feel as if a different editorial team independently developed the same underlying insight. Do not preserve identical section structure across all five. Do not simply change headings.

---

## 1. MIT Sloan Management Review Style

### Editorial Question

**What new model or management concept is needed to understand what is changing?**

### Character

Analytical, research-oriented, conceptually rigorous, but accessible to senior managers. The article should feel halfway between an academic paper and a management magazine article.

### Structure

Typically:

1. Introduce an observed phenomenon or contradiction.
2. Explain why the existing management model is insufficient.
3. Develop a new conceptual framework.
4. Support it with evidence or research.
5. Explore second-order organizational consequences.
6. Discuss limitations and uncertainties.
7. Translate the model into management implications.
8. End with a broader conceptual shift.

### Style

Allow equations, conceptual models, and new terminology when they clarify the argument. For example:

```
Output = f(Human judgment, AI capacity, other constraints)
```

or:

```
Traditional unit of capacity → Headcount
Emerging unit of capacity → Human + machine productive capacity
```

Avoid oversimplifying uncertainty.

### Preferred Outcome

The reader should finish thinking: **"I now have a new way of understanding the organization."**

---

## 2. Harvard Business Review Style

### Editorial Question

**What management practice is becoming wrong, and what should leaders do instead?**

### Character

Direct, polished, executive-friendly, actionable. Move quickly from observation to management consequence.

### Structure

Typically:

1. Open with a recognizable management problem or anecdote.
2. State why conventional practice is becoming inadequate.
3. Explain the new reality.
4. Present an actionable framework.
5. Give concrete management examples.
6. Provide three to five actions leaders can implement.
7. Close with the new question leaders should ask.

### Style

Use clear managerial language. Prefer:

- "Stop doing X. Start doing Y."
- "Leaders should make four changes."

Do not spend too long developing abstract theory before reaching action.

### Preferred Outcome

The reader should finish thinking: **"I need to change how I manage this."**

---

## 3. McKinsey-Style Insight Article

### Editorial Question

**What operating model should the enterprise build to respond to this change?**

### Character

Structured, enterprise-wide, transformation-oriented. Translate the insight into an organizational architecture.

### Structure

Usually:

1. Define the structural shift.
2. Explain why the existing operating model is insufficient.
3. Introduce a future-state operating model.
4. Break it into 4–6 dimensions or shifts.
5. Show movement from current state to future state.
6. Discuss implications across functions.
7. Present a transformation path or maturity model.
8. Close with the capabilities required to make the transition.

### Framework Preference

Use transformations of the form "From → To", such as:

- Headcount planning → Capacity planning
- Equal AI access → ROI-based allocation
- Task automation → Workflow redesign
- Span of control → Span of agency
- Usage metrics → Business-outcome metrics

Include an exhibit-style table when useful.

### Preferred Outcome

The reader should finish thinking: **"I can see what the future operating model looks like."**

---

## 4. BCG-Style Strategy Article

### Editorial Question

**How does this change the basis of competition, and what separates winners from losers?**

### Character

Strategic, competitive, provocative, archetype-driven. Focus on structural advantage rather than internal process alone.

### Structure

Typically:

1. Identify a changing basis of competition.
2. Contrast the old economic model with the emerging one.
3. Show why incremental adoption is insufficient.
4. Define 3–5 strategic archetypes.
5. Explain which archetype has structural advantage.
6. Identify the economic mechanism behind that advantage.
7. Explain what incumbents risk if they move too slowly.
8. End with the strategic question CEOs should be asking.

### Framework Preference

Use strong contrasts, such as:

- AI-augmented incumbent vs. AI-native scaler
- Headcount-led growth vs. Capacity-led growth

Focus on cost curves, competitive moats, scaling economics, and asymmetry.

### Preferred Outcome

The reader should finish thinking: **"This could fundamentally change who wins in this industry."**

---

## 5. Bain-Style Value-Creation Article

### Editorial Question

**Where is the economic value, and how should capital be allocated to capture it?**

### Character

Economically grounded, execution-oriented, ROI-driven. Reduce abstract claims to measurable business decisions.

### Structure

Typically:

1. Start with a concrete investment or operating decision.
2. Identify why current budgeting creates poor allocation.
3. Introduce a measurable economic framework.
4. Separate sources of value.
5. Explain diminishing returns and bottlenecks.
6. Connect operational metrics to P&L outcomes.
7. Provide decision rules.
8. End with a capital-allocation question.

### Framework Preference

Whenever appropriate, compare marginal returns. For example:

```
ROI_human = Incremental business value from additional human capacity / Fully loaded human cost

ROI_AI = Incremental business value from additional AI capacity / AI + infrastructure + oversight cost

ROI_hybrid = Incremental business value from combined human-AI capacity / Combined incremental cost
```

Consider three economic zones:

1. Complementarity
2. Substitution
3. Saturation

### Preferred Outcome

The reader should finish thinking: **"I know what to measure and where I should put the next dollar."**

---

## Important Differentiation Rules

The five articles must not have identical theses at identical levels of abstraction. Translate the common insight into five different questions:

- **Sloan:** What new theory explains this?
- **HBR:** What should managers change?
- **McKinsey:** What operating model should companies build?
- **BCG:** What new source of competitive advantage emerges?
- **Bain:** How should companies allocate resources to capture the value?

The central insight may remain consistent, but each article should develop a different implication of it.

---

## Tone Rules

Write for intelligent senior business readers.

**Avoid:**

- generic AI enthusiasm
- excessive buzzwords
- fake certainty
- simplistic "AI will replace everyone" arguments
- repeated phrases such as "in today's rapidly changing world"
- consulting clichés without analytical content
- invented quantitative claims

**Prefer:**

- strong causal reasoning
- explicit assumptions
- counterarguments
- concrete examples
- economic mechanisms
- memorable but defensible frameworks

---

## Handling Raw Conversations

Conversation transcripts often contain valuable ideas mixed with repetition and exploratory thinking. Do not write the transcript chronologically. Instead:

1. Reconstruct the argument.
2. Remove dead ends.
3. Combine repeated observations.
4. Preserve genuinely insightful turns in reasoning.
5. Identify where one idea led to another.
6. Convert conversational questions into explicit hypotheses.

**Example transformation:**

Raw conversation:

> "VC is growth. PE is efficiency."

then later:

> "But AI lets companies grow without hiring proportionally."

then later:

> "So maybe VC economics and PE economics merge."

Should become:

> Traditional corporate finance treated growth and operating leverage as partially opposing objectives. AI may weaken that trade-off by allowing output to scale faster than human labor, creating the possibility of VC-style growth combined with PE-style operating leverage.

---

## Handling Existing Articles

When the source is already a polished article:

1. Do not merely summarize and rephrase it.
2. Extract the intellectual content.
3. Identify what is essential and what belongs only to the original format.
4. Reconstruct the argument independently for each destination style.
5. Preserve facts and evidence.
6. Change framing, hierarchy, examples, and managerial implications as required.

---

## Deliverable Format

Return five clearly separated finished articles in this order:

### 1. MIT Sloan Management Review Version

Title (and subtitle if useful) followed by the full article.

### 2. Harvard Business Review Version

Title followed by the full article.

### 3. McKinsey-Style Version

Title followed by the full article, including exhibit/table where valuable.

### 4. BCG-Style Version

Title followed by the full article, including strategic archetypes where valuable.

### 5. Bain-Style Version

Title followed by the full article, including economic framework or decision rules where valuable.

---

## Optional Comparative Summary

After the five articles, provide a short table:

| Version | Core question | Main framework | Best audience | Strongest contribution |

This section should compare the editorial treatment rather than repeat the articles.

---

## Length

Unless the user specifies otherwise:

- MIT Sloan: 2,500–4,000 words
- HBR: 1,800–3,000 words
- McKinsey: 2,000–3,500 words
- BCG: 2,000–3,500 words
- Bain: 1,800–3,000 words

If the source material is too thin to support five long articles without repetition, preserve quality over length. Do not pad.

---

## User Controls

Allow the user to optionally specify:

### Length

- short
- standard
- publication-length

### Audience

- CEO
- CTO
- engineering management
- investors
- general executives
- employees

### Evidence level

- use source only
- source + web research
- research-heavy

### Voice

- neutral editorial
- first-person practitioner
- institutional consulting voice

### Preserve anecdotes

- yes
- no

### Provocativeness

- conservative
- balanced
- provocative

If unspecified, use:

- publication-length
- senior executive audience
- source + web research when current verification matters
- neutral editorial voice
- preserve strong anecdotes
- balanced but intellectually provocative framing

---

## Final Quality Check

Before delivering, verify that:

- all five articles share the same underlying source insight
- none is merely a synonym-swapped copy
- Sloan contains the strongest conceptual model
- HBR contains the clearest managerial actions
- McKinsey contains the clearest operating model
- BCG contains the strongest competitive strategy argument
- Bain contains the strongest economic decision framework
- factual claims are supported
- speculation is identified as speculation
- no personal experience has been invented
- the author's strongest original ideas have not been diluted

---

## Invocation

For actual reuse, invoke it with something very simple like:

> Apply the Five-Style Management Article Rewriter to the following conversation. Use publication length, senior executive audience, research-heavy evidence, and preserve my anecdotes.

Then paste the conversation or article.

## Source Synthesis Enhancement

A sixth "source synthesis" output before the articles is recommended: a one-page memo containing the thesis, causal chain, strongest evidence, counterargument, and original concepts. This provides a stable intellectual source of truth, so when material is revised later, the five versions don't gradually diverge.

---

## In This Repo

Publishing the output is the site workflow (AGENTS.md), not this skill. The five articles
form one case study: one folder under `articles/<case>/` holding `problem.md` (the
plain-language title page), one markdown file per publication (`sloan.md`, `hbr.md`,
`mckinsey.md`, `bcg.md`, `bain.md`), and the five publication logos as committed image
files — all registered in `content.json`. Chinese versions follow the site's bilingual
`chinese_`-prefix conventions. First line of each file is the `# Title`; the SPA renders
titles from `content.json`.