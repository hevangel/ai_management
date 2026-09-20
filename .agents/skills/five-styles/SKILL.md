---
name: five-styles
description: Transform raw material — a conversation transcript, brainstorming notes, rough draft, or existing article — into five structurally different management/business articles in the editorial logics of MIT Sloan Management Review, Harvard Business Review, McKinsey & Company, BCG, and Bain & Company, each with its own cover-art brief, preceded by a one-page Source Synthesis Memo. Use when the user asks to "rewrite this in the five styles", wants "a Sloan/HBR/McKinsey/BCG/Bain version", mentions the five-styles rewriter or a source synthesis memo, wants cover-art briefs for a management idea, or wants one idea developed into a five-publication case study. Never produces five synonym-swapped copies; extracts the intellectual core and verifies facts first.
---

# Five-Style Management Article Rewriter Skill

Origin: the owner's ChatGPT conversation "Explain Vibeitda"
(https://chatgpt.com/share/6aa621ef-59d0-83e8-9cb4-0083364b9f6b), whose final message is
this specification. The scraped transcript is archived at
`sratchpad/vibeitda_chatgpt_transcript.md`; strip chat-export artifacts (favicon citation
images, `utm_source=chatgpt.com` links, `citeturn` tokens) when quoting from it.

## Purpose

Rewrite raw management material — conversation history, brainstorming notes, rough
drafts, research notes, memos, or existing articles — into five distinct
management-publication styles:

1. MIT Sloan Management Review
2. Harvard Business Review
3. McKinsey-style insight article
4. BCG-style strategy article
5. Bain-style value-creation article

Also produce:

- a one-page **Source Synthesis Memo** before any rewriting (Stage 0) — the canonical
  source of truth for every later output;
- a publication-specific **cover-art brief** for each version (`references/cover-art.md`);
- an optional **comparative summary** explaining how the five treatments differ.

The five articles must be intellectually distinct. Do not merely change vocabulary,
headings, tone, or brand colors.

## Core Rule

All five articles must derive from the same underlying intellectual source, but each
must answer a different question:

| Style | Central question |
|---|---|
| Sloan | What new model explains what is changing? |
| HBR | What management practice should leaders change? |
| McKinsey | What operating model should the enterprise build? |
| BCG | How is the basis of competition changing? |
| Bain | Where is the economic value, and how should resources be allocated? |

Preserve the author's original insight whenever possible. Do not invent personal
experiences, examples, data, research findings, or beliefs that were not present in the
source material or independently verified. When the source is a conversation, use the
most developed version of the argument and distinguish early exploratory ideas, ideas
the author later rejected, refined positions, and the final position.

## Pipeline

1. **Stage 0** — write the Source Synthesis Memo.
2. **Stage 1** — reconstruct the intellectual core.
3. **Stage 2** — research and verify current facts.
4. **Stage 3** — generate five independent treatments.
5. Run the **differentiation test**; rewrite if the five collapse into one article with
   different headings.
6. Deliver in the **standard order**: memo → five articles with cover-art briefs →
   comparative summary.

---

## Stage 0 — Source Synthesis Memo

Before generating any article, write a one-page analytical memo (600–1,000 words). It is
the canonical source of truth for all later outputs; do not optimize it for any
publication style.

Required sections: **Working Thesis, Conventional View, What Changed, Causal Chain, Core
Mechanism, Key Concepts, Evidence (empirical / business examples / practitioner /
logical), Strongest Counterarguments, Unresolved Questions, Managerial Implications,
Claims Requiring Verification, Authorial Position, One-Sentence Version.**

Read `references/source-synthesis-memo.md` for the section-by-section spec before writing
it. When the author's thinking changes later, revise the memo first (see Revision
Workflow).

---

## Stage 1 — Reconstruct the Intellectual Core

When the source is a conversation, do not summarize it chronologically. Instead:

1. Identify the initial observation.
2. Identify how the argument evolved.
3. Remove dead ends and repetition.
4. Preserve useful disagreements and unresolved questions.
5. Recover the strongest causal logic.
6. Separate facts from hypotheses.
7. Preserve memorable original language where useful.

Example — raw discussion: "VC grows companies." / "PE optimizes EBITDA." / "AI means
growth may no longer require lots of hiring." / "So AI-native companies may combine
both." Do not reproduce that as dialogue. Reconstruct it as:

> Traditional corporate finance treated growth and operating leverage as partially
> opposing objectives, because rapid growth required rapid expansion of labor. AI may
> weaken that trade-off by enabling output to scale faster than headcount, creating the
> possibility of VC-style growth combined with PE-style operating leverage.

When the author changed their mind, prefer the later refined view unless they explicitly
ask to preserve the evolution. When uncertainty remains unresolved, keep it unresolved —
do not silently choose a convenient answer.

---

## Stage 2 — Research and Verification

If current facts materially affect the article, verify them before writing: current AI
capabilities, recent research, company strategy, employment effects, market data,
regulation, workforce trends, current consulting research.

Prefer, in order: original research; academic journals; NBER; government data; company
filings; company statements; high-quality industry research; consulting research when
primary sources are unavailable.

Do not use a consulting firm's claim as evidence simply because the output is written in
consulting style.

Label every claim as one of: demonstrated fact; evidence-supported interpretation;
working hypothesis; analogy; forward-looking speculation.

Never invent precise numbers to make an argument look rigorous. If the evidence is
uncertain, preserve the uncertainty.

---

## Stage 3 — Generate Five Independent Treatments

Each article should feel as if a different editorial team independently developed the
same underlying insight. The five outputs must not share identical article structures; do
not copy paragraphs between versions; each version must develop a different implication
of the common thesis.

### 1. MIT Sloan Management Review Version

**Editorial question: What new management model or conceptual framework is needed to
understand this change?**

Character: analytical; evidence-oriented; conceptually rigorous; research-friendly;
accessible to senior managers; comfortable with uncertainty.

Typical structure:

1. Introduce an observed phenomenon or contradiction.
2. Explain why the old model is insufficient.
3. Develop a new conceptual model.
4. Introduce terminology or a framework.
5. Support the framework with evidence.
6. Explore second-order consequences.
7. Discuss limitations.
8. Translate the model into managerial implications.
9. End with a broader conceptual shift.

Use equations or formal conceptual models when useful:

```
Output = f(Human judgment, AI capacity, other constraints)
```

```
Traditional capacity unit → Headcount
Emerging capacity unit → Human + machine productive capacity
```

Avoid: excessive listicles; premature action checklists; fake certainty; management
clichés; overly promotional language.

Reader takeaway: **"I now have a new way of understanding this organization or
phenomenon."**

### 2. Harvard Business Review Version

**Editorial question: What management practice is becoming inadequate, and what should
leaders do instead?**

Character: direct; polished; practical; executive-friendly; action-oriented; memorable.

Typical structure:

1. Start with a recognizable management problem, anecdote, or decision.
2. Explain why conventional practice is becoming wrong.
3. Introduce the new reality.
4. Present an actionable framework.
5. Give concrete examples.
6. Provide 3–5 actions leaders can take.
7. End with the new management question.

Preferred rhetorical structure: "Managers traditionally do X. That worked because Y. Y
is changing. Leaders should now do Z."

Avoid: long theoretical setup; overcomplicated frameworks; unnecessary equations;
excessive nuance before stating the implication.

Reader takeaway: **"I need to change how I manage this."**

### 3. McKinsey-Style Version

**Editorial question: What operating model should the enterprise build to respond?**

Character: structured; enterprise-wide; transformation-oriented; systematic;
capability-based; future-state focused.

Typical structure:

1. Define the structural shift.
2. Explain why the current operating model is insufficient.
3. Describe the future-state operating model.
4. Break it into 4–6 dimensions.
5. Show "from → to" transitions.
6. Discuss organization-wide implications.
7. Provide a maturity model or transition path.
8. End with the capabilities required for execution.

Preferred transitions:

- Headcount planning → Capacity planning
- Equal AI access → ROI-based allocation
- Task automation → End-to-end workflow redesign
- Span of control → Span of agency
- Technology usage → Business outcomes
- Annual planning → Dynamic allocation

Include at least one exhibit-style table when useful, e.g.:

| Traditional model | AI-enabled model | AI-native model |
|---|---|---|
| Headcount allocation | Copilot access | Human-agent capacity allocation |
| Functional staffing | AI overlays | Outcome-based teams |
| Annual budgeting | Tool budgets | Dynamic capacity budgets |
| Productivity metrics | Usage metrics | Economic output metrics |

Reader takeaway: **"I can see what the future operating model looks like and how to
build it."**

### 4. BCG-Style Version

**Editorial question: How is the basis of competition changing, and what separates
winners from losers?**

Character: strategic; provocative; archetype-driven; competitive; economic;
future-oriented.

Typical structure:

1. Identify a changing basis of competition.
2. Contrast old and emerging economics.
3. Explain why incremental adoption is insufficient.
4. Define 3–5 company archetypes.
5. Show which structural characteristics create advantage.
6. Explain the cost curve, scale advantage, or asymmetry.
7. Describe the risk to incumbents.
8. End with the strategic question for CEOs.

Preferred frameworks — strong contrasts such as AI-augmented incumbent vs. AI-native
scaler, headcount-led growth vs. capacity-led growth, or a four-archetype ladder:
labor-intensive incumbent → AI-augmented incumbent → aggressive automator → AI-native
scaler.

Focus on structural competitive advantage, cost curves, operating leverage, scalability,
industry structure, competitive asymmetry, moat creation, and new winner/loser dynamics.
Do not turn the piece into a generic "five steps to use AI" article.

Reader takeaway: **"This could change who wins in my industry."**

### 5. Bain-Style Version

**Editorial question: Where is the economic value, and how should the next dollar be
allocated?**

Character: economically grounded; ROI-oriented; execution-focused; measurable;
capital-allocation driven.

Typical structure:

1. Start with a concrete economic decision.
2. Explain why current budgeting creates poor allocation.
3. Introduce a measurable decision framework.
4. Identify sources of value.
5. Explain marginal returns.
6. Identify diminishing returns and bottlenecks.
7. Connect operational outcomes to the P&L.
8. Give decision rules.
9. End with a capital-allocation question.

Compare marginal returns when appropriate:

```
ROI_human  = Incremental business value from additional human capacity / Fully loaded human cost
ROI_AI     = Incremental business value from additional AI capacity / AI + infrastructure + oversight cost
ROI_hybrid = Incremental business value from combined human-AI capacity / Combined incremental cost
```

Use the three economic zones when relevant: **complementarity** (more AI increases the
productivity of humans), **substitution** (AI reduces the quantity of human labor needed
for the same output), **saturation** (additional AI creates little value because another
bottleneck dominates).

Connect AI to revenue growth, cost reduction, asset efficiency, avoided hiring, cycle
time, customer retention, EBITDA, margin, working capital, and risk reduction.

Reader takeaway: **"I know what to measure and where the next dollar should go."**

---

## Differentiation Test

Before finalizing, compare all five versions. If they can be reduced to the same article
with different headings, rewrite them. The correct distinction is the central-question
table in Core Rule; the central insight may remain consistent, but each article must
develop a different implication of it.

---

## Deliverable Format

Return outputs in this order:

0. **Source Synthesis Memo**
1. **MIT Sloan Management Review Version** — article, then cover-art brief
2. **Harvard Business Review Version** — article, then cover-art brief
3. **McKinsey-Style Version** — article, then cover-art brief
4. **BCG-Style Version** — article, then cover-art brief
5. **Bain-Style Version** — article, then cover-art brief
6. **Comparative summary** — `| Version | Core question | Main framework | Best audience | Main contribution |`, comparing the editorial treatments rather than repeating the articles.

---

## Cover Art

Each article carries its own cover-art concept; the five covers must visualize different
aspects of the argument — never one image recolored. Use the editorial design logic of
each publication rather than brand imitation: do not copy proprietary mastheads, logos,
or exact publication layouts unless the user explicitly asks for a parody or mockup and
the context permits it.

Read `references/cover-art.md` for the per-publication briefs (visual objective, style,
typical concept, image question) and the required output format: cover concept, key
metaphor, composition, art direction, avoid, image-generation prompt.

---

## Revision Workflow

If the author's thinking changes:

1. Revise the Source Synthesis Memo first and identify what changed.
2. Update the causal chain, evidence, or unresolved questions.
3. Regenerate only the affected versions unless asked to regenerate all five.
4. Update the corresponding cover-art concepts if the thesis changes.

Do not independently patch five articles after the core thesis has shifted.

---

## Handling Existing Articles

When the input is already polished, do not merely paraphrase it five times:

1. Extract its intellectual core.
2. Generate the Source Synthesis Memo.
3. Separate evidence from editorial framing.
4. Rebuild the argument independently for each style.
5. Retain factual substance.
6. Change hierarchy, emphasis, structure, and managerial implication.

---

## Tone Rules

Write for intelligent senior business readers.

Avoid: generic AI enthusiasm; excessive buzzwords; fake certainty; simplistic "AI will
replace everyone" arguments; filler such as "in today's rapidly changing world";
consulting clichés without analytical content; invented quantitative claims.

Prefer: strong causal reasoning; explicit assumptions; counterarguments; concrete
examples; economic mechanisms; memorable but defensible frameworks.

---

## Length

Unless the user specifies otherwise:

- Source memo: 600–1,000 words
- MIT Sloan: 2,500–4,000 words
- HBR: 1,800–3,000 words
- McKinsey: 2,000–3,500 words
- BCG: 2,000–3,500 words
- Bain: 1,800–3,000 words

Do not pad thin material to meet a word count; preserve quality over length.

---

## User Controls

Allow optional inputs (defaults after each):

- **Length**: short / standard / publication-length (default publication-length).
- **Audience**: CEO / CTO / engineering management / investors / board / general
  executives / employees (default senior executives).
- **Evidence level**: source only / source + verification / research-heavy (default
  source + verification when external or current claims matter).
- **Voice**: neutral editorial / first-person practitioner / institutional consulting
  voice (default neutral editorial).
- **Anecdotes**: preserve / minimize / remove (default preserve strong anecdotes).
- **Provocativeness**: conservative / balanced / provocative (default balanced but
  intellectually provocative).
- **Cover art**: briefs only / prompts only / generate images / none (default briefs +
  prompts).

---

## Final Quality Check

Before delivering, confirm:

- the memo accurately represents the source and the strongest original insight has been preserved
- facts and hypotheses are distinguished; current claims have been verified when necessary
- no personal experience has been invented; no research result has been fabricated; uncertainty has not been hidden
- all five pieces derive from the same source thesis
- Sloan has the strongest conceptual model; HBR the strongest managerial action; McKinsey the clearest operating model; BCG the strongest competitive-strategy framing; Bain the strongest economic and capital-allocation framework
- the five structures are materially different
- cover concepts are materially different and reflect each version's argument, not only its visual brand
- proprietary publication visual identities are not directly copied unless specifically requested

---

## In This Repo

Publishing the output is the site workflow (AGENTS.md), not this skill. The five articles
form one case study: one folder under `articles/case-studies/<slug>/` holding
`problem.md` (the plain-language title page), one markdown file per publication
(`sloan.md`, `hbr.md`, `mckinsey.md`, `bcg.md`, `bain.md`), and the five publication
logos as committed image files — all registered in `content.json`. Chinese versions
follow the site's bilingual `chinese_`-prefix conventions. First line of each file is
the `# Title`; the SPA renders titles from `content.json`. Cover art for the case-study
folder follows the site's `cover.png` conventions (AGENTS.md / the ai_philosophy
recipe); the briefs here feed those image-generation prompts.
