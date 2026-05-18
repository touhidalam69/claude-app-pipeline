---
name: play-store-aso-prompter
description: Generate a prompt that produces Google Play Store listing copy — title, short description, long description, what's new, promo text — fully compliant with Google Play policies. This is Stage 5 of the claude-app-pipeline. Use this skill whenever the user needs store listing text or ASO copy for an app. Trigger on phrases like "ASO prompt", "Play Store listing", "store listing copy", "app description", "ASO writing", "write my app description", "make an ASO prompt", "play store copy", or any similar request. Do not write the listing yourself — this skill produces the PROMPT the user runs to generate it.
---

# Play Store ASO Prompter

**Stage 5 of the claude-app-pipeline.** This skill produces a single prompt that generates **Google Play Store listing copy** — title, short and long descriptions, what's-new, promo text — written to be **policy-compliant** and **ASO-effective**.

The skill produces the **prompt**. The user runs it to get the listing copy.

## Confirm inputs before generating

Read from context (Stage 1 `outputs/01-idea-research.md` has features + an ASO keyword shortlist; Stage 2/3 have feature detail). Ask **once** for anything critical missing; otherwise default and proceed.

- **Chosen idea + main features** *(critical)* — what the app does, top 5–8 features.
- **Target ASO keywords** — 10–20, ideally from the Stage 1 keyword shortlist. If absent, ask or derive from the niche.
- **Tone** — default: professional, benefit-led, plain English.
- **Target locale** — default `en-US`.

## Deliverable

Write the prompt to `outputs/05-aso-prompt.md` in the working directory (create `outputs/` if needed). The file contains a single prompt the user runs. The prompt must ask the model to produce:

- **App title** — **max 30 characters**. Natural, readable. **No keyword stuffing. No superlatives** ("Best", "#1", "Top", "Free" as a hook).
- **Short description** — **max 80 characters**. A real hook; one keyword woven in naturally. At most 1–2 emoji.
- **Long description** — **max 4000 characters**, structured:
  1. **Hook** — 1 sentence.
  2. **Problem / use-case** — 2 sentences.
  3. **Feature bullets** — 5–8 bullets.
  4. **Why this app** — one short paragraph.
  5. **Target user** — one short paragraph ("Made for…").
  6. **Call to action** — one closing line.
  Keyword density **under 3%** — keywords must read naturally, never stuffed.
- **What's new** — first-release snippet, **max 500 characters**.
- **Promo text** — **max 170 characters**.
- **Recommended Play category** + a **content-rating self-assessment** (which IARC questionnaire answers apply).

### Hard policy rules — bake these into the prompt

The produced prompt must explicitly forbid:

- **False or misleading claims** — no functionality the app does not have.
- **References to other brands/apps** — only if factual and permitted; no implying endorsement.
- **"As seen on TV"-style claims and fake reviews / fake ratings.**
- **Medical / financial advice or health claims** without backing and a clear disclaimer.
- **Mentioning features the app doesn't have.**
- **Superlatives and ranking claims** ("Best", "#1", "Top-rated") in the title.
- More than **1–2 emoji** in the short description.

And must **require**:

- **Family-friendly language** if the app targets children.
- **One transparent mention of the ad-supported nature** in the long description (e.g. "This app is free and supported by ads.") — a Play transparency expectation for ad-funded apps.

### Policy references — cite these in the produced prompt

- Google Play metadata / store-listing policy: https://support.google.com/googleplay/android-developer/answer/9898842
- Play store-listing & promotional content guidelines: https://play.google.com/about/storelisting-promotional/

## Prompt-construction rules

- Fill the prompt with the real app name, real features, the real keyword list.
- State every character limit explicitly so the output can't overflow Play Console fields.
- Make the prompt self-contained and runnable in one paste.

## After completing

Print to the console:
1. The path: `outputs/05-aso-prompt.md`.
2. A reminder to paste each generated field into the matching Play Console listing field and re-check character counts there.

## Next step in the pipeline

**Stage 5 of 7.** Previous step: Stage 4 — `content-data-sourcing-prompter` (`outputs/04-content-prompt.md`).

**Next: Stage 6 — `app-visual-assets-prompter`.** The listing also needs an icon, feature graphic, and screenshots. The next skill produces image-generation prompts for them.

Sample handoff message to the user:

> ASO prompt ready at `outputs/05-aso-prompt.md`. Run it, paste the results into Play Console. Next, run the `app-visual-assets-prompter` skill (say *"make a visual assets prompt"*) and I'll produce image-generation prompts for your app icon, feature graphic, and screenshots.
