---
name: app-prototype-design-prompter
description: Generate a comprehensive design prompt the user pastes into Claude.ai (with Artifacts enabled) to produce an interactive HTML/React UI prototype of a content-driven mobile app. This is Stage 2 of the claude-app-pipeline, consuming a finalized idea from Stage 1 (content-app-idea-research). Use this skill whenever the user wants to turn a chosen app idea into a visual UI design or prototype. Trigger on phrases like "make a design prompt", "prototype prompt", "design my app", "design prompt for Claude", "Claude design prompt", "next step after idea", "I picked an idea, now what", "prototype my app", or any similar request. Do not do the prototyping yourself — this skill produces the PROMPT; Claude.ai produces the prototype.
---

# App Prototype Design Prompter

**Stage 2 of the claude-app-pipeline.** This skill takes a finalized app idea (from Stage 1) and produces a single, comprehensive prompt the user pastes into a Claude.ai session with **Artifacts** enabled. That session produces an interactive HTML/CSS/JS UI prototype of the app.

The skill structures, contextualizes, and adds guardrails to the prompt. It does **not** build the prototype itself — the user runs the prompt in Claude.ai. ("Claude Design" in user shorthand just means a Claude.ai session that renders UI via Artifacts — not a separate Anthropic product.)

## Confirm inputs before generating

Read these from context (the Stage 1 output `outputs/01-idea-research.md` usually has them). Ask **once** for anything critical that's missing; otherwise default and proceed.

- **Chosen idea** *(critical)* — 1-line pitch + niche + content theme. If absent, ask.
- **Target stack** — default `.NET MAUI`. Respect a stack the user already stated.
- **Brand direction** *(optional)* — color, mood. Default: clean, modern, content-first; one accent color picked to fit the niche.
- **Screens expected** — default: Home, List (browse/categories), Detail, Settings/About. Optional: Categories screen, Favorites screen, Search.
- **Ad placements** — default set: banner on List + Detail; interstitial on category switch / every 5+ detail opens; rewarded to unlock a premium category or daily bonus; app open on cold/warm start. Adjust to the idea.

## Deliverable

Write the prompt to `outputs/02-design-prompt.md` in the working directory (create `outputs/` if needed).

The file contains a single prompt block the user copies wholesale into Claude.ai. The prompt must instruct Claude.ai to produce:

### The prototype artifact

- A **single interactive HTML + CSS + JS artifact** showing **4–6 screens** with realistic, niche-specific mocked content (not lorem ipsum — use sample entries from the idea).
- **Tailwind-style utility styling** (Tailwind via CDN is fine inside the artifact), clean and modern.
- A **mobile-frame viewport**, 390×844 px typical (iPhone-class). Screens shown side by side or navigable via tap.
- Working tap navigation between screens (Home → List → Detail → back, Settings reachable).
- Realistic empty states, a loading shimmer, and a dark-mode toggle.

### Mocked ad slots — labeled placeholders, NOT real ads

The prototype must visually mock every ad surface as a **clearly labeled placeholder box** — never a real ad SDK, never a real ad:

- **Banner** — a 320×50-ish bar pinned at the bottom of List and Detail, labeled `[ AdMob Banner ]`.
- **Interstitial** — a button or simulated transition labeled `[ Interstitial trigger ]` showing where a full-screen ad fires.
- **Rewarded** — a button labeled `[ Rewarded: unlock X ]` at the genuine unlock moment.
- **App open** — a splash/overlay screen labeled `[ App Open ad ]` shown on simulated cold start.

### Design spec appendix

After the prototype, the prompt must ask Claude.ai to append a **design spec**:

- **Color tokens** — named hex values (primary, accent, background, surface, text, muted), light + dark.
- **Typography scale** — font family + sizes for display / title / body / caption.
- **Spacing scale** — the spacing steps used (e.g., 4 / 8 / 12 / 16 / 24 / 32).
- **Navigation map** — which screen links to which.
- **Key interactions** — taps, transitions, the favorite/bookmark action, dark-mode toggle.
- **Accessibility notes** — contrast ratios, tap-target sizes (≥44 px), font scaling.

### Mapping to the target stack

The prompt must ask Claude.ai to add a short **"Maps to {stack}"** note per screen. For the default .NET MAUI stack:

- List screens → `CollectionView` (with `DataTemplate`).
- Navigation → `Shell` (flyout or tab bar) with `ContentPage` per screen.
- Detail screens → `ContentPage` bound to a ViewModel.
- Reusable cards → `ContentView` / `ControlTemplate`.
- Theming → `ResourceDictionary` in `Resources/Styles/`, `AppThemeBinding` for dark mode.

If the user picked Flutter, map to `Scaffold` / `ListView.builder` / `Navigator` / widgets instead. Kotlin → Jetpack Compose. Swift → SwiftUI.

### Handoff instruction inside the prompt

The produced prompt **must end** by telling Claude.ai to also output a **plain-text "design spec summary"** — a compact, copy-pasteable block (color tokens, typography, spacing, screen list with the stack mapping, ad placements). This is what the user carries into Stage 3.

## Prompt-construction rules

- Fill the prompt with the actual idea — real niche, real sample entries, real screen names. No placeholders left for the user to fill.
- Keep the prompt self-contained: a person who never saw Stage 1 can paste it and get a coherent result.
- Be explicit that ad slots are **mock labeled placeholders only** — no ad SDKs, no real ad markup.
- Specify the mobile frame dimensions and that it must be interactive (tappable), not static images.
- Tell Claude.ai to use the chosen stack's vocabulary in the per-screen mapping notes.

## After completing

Print to the console:
1. The path: `outputs/02-design-prompt.md`.
2. A short sample message the user pastes into Claude.ai **above** the prompt, e.g.:

> Hi Claude — please enable Artifacts and follow the prompt below to build an interactive UI prototype for my app. Produce the prototype artifact first, then the design spec, then the plain-text design spec summary at the end.

## Next step in the pipeline

**Stage 2 of 7.** Previous step: Stage 1 — `content-app-idea-research` (`outputs/01-idea-research.md`).

**Next: Stage 3 — `app-build-prompter`.** Once the user has the prototype and the design spec summary from Claude.ai, the next skill turns them into a Claude Code prompt that builds the real app.

Sample handoff message to the user:

> Design prompt ready at `outputs/02-design-prompt.md`. Paste it into Claude.ai, get your prototype, then **copy the plain-text design spec summary it produces**. Bring that back here and run the `app-build-prompter` skill (say *"make a build prompt"*) — I'll turn the design spec + your idea into a Claude Code prompt that builds the .NET MAUI app.
