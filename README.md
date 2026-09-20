# AI Management

A business and management website written and maintained entirely by AI: polished,
HBR / MIT Sloan-style writing on what artificial intelligence is doing to companies,
strategy, and work — published as case studies that attack one business problem from
five publication angles at once.

**Read it online: <https://hevangel.github.io/ai_management/>**

## What you'll find

- **Case Studies** — one business problem, five readings. The same investigation
  written as five separate essays in the editorial styles of MIT Sloan Management
  Review, Harvard Business Review, McKinsey & Company, BCG, and Bain & Company, with
  a plain-language title page, tabbed reading, and per-publication cover art.
  First up: *VIBEITDA — why AI-native companies can grow without growing headcount.*
- **Articles** — standalone management essays on AI strategy, organization design,
  and value creation (growing).

## How it's made

Every article starts as a raw conversation with AI, then goes through the repo's
[five-styles skill](.agents/skills/five-styles/SKILL.md): a source-synthesis memo
extracts the intellectual core, the facts are verified against primary research, and
the idea is rewritten five times — each version a structurally different article with
its own cover-art brief, not a synonym-swapped copy.

The site itself has no build step and no package manager: a single-page app
(`index.html` + `content.json`) over plain markdown, bilingual (English / Hong Kong
Traditional Chinese) with light and dark themes. Instructions for the AI agents that
maintain this repository live in [AGENTS.md](AGENTS.md).

## How to read

Visit the site above, or browse the markdown directly under `articles/`. To preview
the site locally:

```bash
python -m http.server 8123
# then open http://localhost:8123/
```

## For humans

This is an AI-only repository: content is created and edited by AI agents following
[AGENTS.md](AGENTS.md). You are welcome to read everything, open issues, and suggest
topics — but please don't push direct edits.

## License

Released under the [MIT License](LICENSE).
