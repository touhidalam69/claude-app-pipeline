---
name: app-visual-assets-prompter
description: Generate image-generation prompts for the visual assets a content app needs to ship to the Play Store — app icon, feature graphic, and screenshots. This is Stage 6 of the claude-app-pipeline. Use this skill whenever the user needs visual assets or image prompts for their app. Trigger on phrases like "logo prompt", "feature graphic prompt", "app icon", "visual assets", "screenshots prompt", "image generation for app", "make a visuals prompt", "icon for my app", or any similar request. Do not generate images yourself — this skill produces the PROMPTS the user pastes into an image generator.
---

# App Visual Assets Prompter

**Stage 6 of the claude-app-pipeline.** This skill produces a set of **image-generation prompts** for the visual assets needed to ship the app to the Play Store. The user pastes each prompt into an image generator (Midjourney, Imagen, DALL·E, Ideogram).

The skill produces the **prompts**. The image generator produces the images.

## Confirm inputs before generating

Read from context (Stage 1 `outputs/01-idea-research.md` for niche/mood; Stage 2 design spec for the color palette). Ask **once** for anything critical missing; otherwise default and proceed.

- **Chosen idea + niche + mood/brand direction** *(critical)* — what the app is and how it should feel.
- **Color palette** — from the Stage 2 design spec if available. If absent, pick a palette that fits the niche and state it.
- **Target image generator** — default: write generator-neutral prompts plus a short syntax note for Midjourney (`--ar`, `--style`), Imagen, DALL·E, and Ideogram (best for any in-image text). Adjust if the user names one.

## Deliverable

Write the prompts to `outputs/06-visual-assets-prompts.md` in the working directory (create `outputs/` if needed). Produce **one prompt per asset**:

### 1. App icon — 512×512

- Simple, recognizable, **no transparency**, **no text** (or minimal). Must stay legible at **48 dp**.
- Note the **adaptive icon**: 108×108 dp canvas with a **72×72 dp safe zone** — keep the core mark inside it; the outer ring may be cropped to any mask shape.
- Provide **3 alternative prompts**: **minimalist**, **illustrative**, **geometric**.

### 2. Feature graphic — 1024×500

- Place the main visual on the left or right; keep a **~20% safe margin** for Play's overlaid text/badges.
- **No text inside the image** — Play overlays its own.
- Describe mood + scene; match the app's palette.

### 3. Phone screenshots — 1080×1920 (or larger, 16:9 portrait)

- Describe **5–8 screenshot designs**. Each = **a real app screen** + a **headline overlay** + supporting **benefit text**.
- The user produces these from the **built app** (real screens), so provide the **headlines and overlay copy** plus layout/background direction — not a fully synthetic image prompt for the screens themselves.

### 4. Optional — 7" and 10" tablet screenshots

- Include only if the user is **targeting tablets**. Same approach: real app screens + overlay copy, sized for tablet.

### Hard rules — bake these into every prompt

- **No copyrighted characters, no brand IPs, no celebrity likenesses.**
- **No text in the app icon or the feature graphic** (icon may have a minimal monogram only).
- **Respect the adaptive-icon safe zone** — core mark inside 72×72 dp of the 108×108 dp canvas.
- **Family-friendly imagery** if the app targets children or a general audience.
- Icon: no photographic clutter; flat or simple depth; readable at small size.

### Reference — cite in the produced file

- Android store-listing asset best practices: https://developer.android.com/distribute/best-practices/launch/store-listing

## Prompt-construction rules

- Fill prompts with the real niche, mood, and palette — concrete colors, concrete subject matter.
- Each prompt is self-contained and pasteable into an image generator as-is.
- Include exact pixel/aspect-ratio specs in each prompt.

## After completing

Print to the console:
1. The path: `outputs/06-visual-assets-prompts.md`.
2. A note on which generator suits which asset (Ideogram for anything needing crisp in-image text; Midjourney/Imagen for icon and feature-graphic art).

## Next step in the pipeline

**Stage 6 of 7.** Previous step: Stage 5 — `play-store-aso-prompter` (`outputs/05-aso-prompt.md`).

**Next: Stage 7 — `privacy-policy-prompter`.** The last required listing item is a privacy policy — mandatory for any app using ads.

Sample handoff message to the user:

> Visual asset prompts ready at `outputs/06-visual-assets-prompts.md`. Generate the icon and feature graphic, capture screenshots from the built app. Last step — run the `privacy-policy-prompter` skill (say *"make a privacy policy prompt"*) and I'll produce a prompt for the Play Store-compliant privacy policy your AdMob app requires.
