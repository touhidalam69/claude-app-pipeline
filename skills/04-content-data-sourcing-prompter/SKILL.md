---
name: content-data-sourcing-prompter
description: Generate a prompt that produces the actual JSON dataset a content-driven app consumes. This is Stage 4 of the claude-app-pipeline. Use this skill whenever the user needs the content/data their app will load. Trigger on phrases like "content prompt", "generate dataset", "create app content", "JSON content", "data for my app", "make the content", "fill my app with content", "make a content prompt", or any similar request. Do not generate the dataset yourself — this skill produces the PROMPT the user runs to generate the data.
---

# Content Data Sourcing Prompter

**Stage 4 of the claude-app-pipeline.** This skill produces a single prompt that, when run, generates the **JSON dataset** the built app loads — the curated content that is the actual product.

The skill produces the **prompt**. The user runs it (in Claude.ai or Claude Code) to get the dataset.

## Confirm inputs before generating

Read from context (Stage 1 `outputs/01-idea-research.md` has niche + sample entries; Stage 3 build prompt has the JSON schema the app expects). Ask **once** for anything critical missing; otherwise default and proceed.

- **Chosen idea + niche** *(critical)* — what the content is about.
- **Content schema** — categories, fields per entry, entry-count target. If unknown, default to: a flat JSON array of objects with `id`, `title`, `category`, `body`, `tags` (array). Adapt field names to the niche.
- **Entry count** — default **200** total.
- **Category balance** — default **8 categories × 25 entries each = 200**. Adjust to the idea.
- **Tone / voice** — default: clear, friendly, concise. Use any voice direction from the design spec.
- **Source approach** — `AI-generated` (default), `public domain`, `manually authored`, or `hybrid`.

## Deliverable

Write the prompt to `outputs/04-content-prompt.md` in the working directory (create `outputs/` if needed). The file contains a single prompt the user runs. The prompt must instruct the model to:

### Generate the dataset

- Produce **N entries** (default 200) matching the **specified JSON schema** exactly — every entry has every field, correct types.
- Hit **category balance targets** — e.g. 25 entries each across 8 named categories. List the categories explicitly in the prompt.
- Assign stable, unique `id` values (sequential integers or slugs).
- Output as **one single valid JSON array**, ready to host at the app's JSON endpoint — no commentary inside the JSON, no markdown fences around it in the final answer block.

### Quality rules — bake these into the prompt

- **No duplicates** — no repeated or near-duplicate entries; vary phrasing and angle.
- **No copyrighted material** — no song lyrics, no copyrighted poems/books, no movie/TV quotes under copyright, no brand IP, no celebrity content.
- **No PII** — no real people's personal data, no contact details.
- **No harmful advice** — no medical, legal, or financial instructions that could cause harm; keep guidance general and add a "consult a professional" framing where the topic touches health/legal/finance.
- **Age-appropriate language** — match the app's audience; family-friendly if the app targets kids.
- **Factual accuracy** — content presented as fact must be correct.

### Validator suggestion

The prompt must include a short note suggesting a **validator script** the user can run on the output — a tiny script (Python or Node) that checks: valid JSON, no duplicate `id`s, every required field present and correctly typed, category counts match targets, no empty strings. Provide the gist so Claude Code can generate it on request.

## Prompt-construction rules

- Fill the prompt with the real niche, the real category names, real sample entries (2–3 fully written examples so the model matches style and depth).
- State the exact schema the Stage 3 app expects — field names must match what the app deserializes.
- Make the prompt self-contained and runnable in one paste.

## Strong note — put this in the skill's console output and in the produced prompt

**AI-generated content is fine, but it is not verified.** The user must **spot-check entries for accuracy and remove anything wrong** before shipping. Factual errors in a reference/study/health-adjacent app damage trust and can draw Play Store / AdMob policy attention. Curation is the product.

## After completing

Print to the console:
1. The path: `outputs/04-content-prompt.md`.
2. The spot-check warning above.
3. A note that the generated JSON goes to the endpoint the Stage 3 app fetches from.

## Next step in the pipeline

**Stage 4 of 7.** Previous step: Stage 3 — `app-build-prompter` (`outputs/03-build-prompt.md`).

**Next: Stage 5 — `play-store-aso-prompter`.** With the app built and content ready, the next skill produces a prompt for the Play Store listing copy.

Sample handoff message to the user:

> Content prompt ready at `outputs/04-content-prompt.md`. Run it, **spot-check the entries**, then host the JSON at your app's endpoint. Next, run the `play-store-aso-prompter` skill (say *"make an ASO prompt"*) and I'll produce a prompt for your Play Store title and description copy.
