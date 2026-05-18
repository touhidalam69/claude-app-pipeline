---
name: app-build-prompter
description: Generate a Claude Code prompt that builds a content-driven mobile app to a polished v1, using the design spec from Stage 2 and the idea from Stage 1. This is Stage 3 of the claude-app-pipeline. Use this skill whenever the user wants to turn a design/prototype into actual built code. Trigger on phrases like "build prompt", "claude code prompt for app", "implement the app", "code the prototype", "build my app", "next step after design", "make a build prompt", "turn my design into code", or any similar request. Do not build the app yourself — this skill produces the PROMPT the user runs in Claude Code.
---

# App Build Prompter

**Stage 3 of the claude-app-pipeline.** This skill takes the design spec (from Stage 2) and the chosen idea (from Stage 1) and produces a single comprehensive prompt the user runs in **Claude Code** to build the actual app to a polished v1.

The skill produces the **prompt**. Claude Code, when given the prompt, builds the app. Default stack is .NET MAUI.

## Confirm inputs before generating

Read from context where possible (Stage 1 `outputs/01-idea-research.md`, Stage 2 `outputs/02-design-prompt.md` and the design spec summary). Ask **once** for anything critical missing; otherwise default and proceed.

- **Design spec summary** *(critical)* — from Stage 2's Claude.ai output. If absent, ask the user to paste it.
- **Chosen idea** *(critical)* — pitch + niche + content theme.
- **Target stack** — default `.NET MAUI` (.NET 8 LTS).
- **JSON endpoint URL** — the content data source. If unknown, default to placeholder `https://example.com/content.json` and mark it `// TODO: replace`.
- **AdMob ad unit IDs** — banner / interstitial / rewarded / app open. If unknown, default to Google's **official test IDs** and mark real IDs as a TODO.
- **App package name / bundle ID** — e.g. `com.yourname.appname`. If unknown, default to `com.example.appname` and mark it `// TODO`.

## Deliverable

Write the prompt to `outputs/03-build-prompt.md` in the working directory (create `outputs/` if needed). The file contains a single prompt the user runs in Claude Code. The prompt must instruct Claude Code to:

### Scaffold & structure

- Scaffold a **.NET MAUI** project targeting **.NET 8 (LTS)**, Android-first (iOS targets retained).
- MVVM via **`CommunityToolkit.Mvvm`** (`ObservableObject`, `RelayCommand`, `[ObservableProperty]`).
- Project structure:
  ```
  Models/         — JSON-mapped data records
  ViewModels/     — one per screen, CommunityToolkit.Mvvm
  Views/          — ContentPages per screen
  Services/       — content fetch, caching, ads, preferences
  Resources/Styles/ — colors, typography, theme dictionaries
  ```

### Features

- **Content**: fetch JSON from the endpoint via `HttpClient`; **local cache** (file cache or SQLite) so the app works offline after first load; cache-then-network refresh.
- **Navigation**: `Shell`-based (tab bar or flyout per the design spec).
- **Screens**: implement every screen in the design spec — Home, List/Browse, Detail, Settings/About, plus any Categories/Favorites/Search the spec includes.
- **Theme + dark mode**: `ResourceDictionary` color tokens from the design spec, `AppThemeBinding`, a user-facing light/dark toggle.
- **Favorites**: local-only, via `Preferences` API or SQLite. No account, no sync.

### AdMob integration — all four formats

Use `Plugin.MauiMTAdmob` **or** a Google Mobile Ads SDK binding. Implement:

- **Banner** — persistent on List and Detail screens.
- **Interstitial** — **frequency-capped** (e.g. min 5 content views or 3+ minutes between shows), fired between content views / on category switch. Never on app close.
- **Rewarded** — at one genuine unlock moment (premium category, daily bonus, ad-free hour). Reward must **persist** locally.
- **App open** — via a lifecycle handler on cold/warm start. **Never on the first launch after install.** Frequency-capped. No overlap with the splash screen.

### Build configuration & privacy

- **AdMob test IDs in `DEBUG`, real IDs in `RELEASE`** — switched via a compilation constant or config (`#if DEBUG`).
- **Privacy**: collect no PII. Favorites and settings stored locally only.
- Wire the AdMob App ID into `AndroidManifest.xml`.

### Build & ship steps

The prompt must tell Claude Code to:
- Restore, build, and run the app on an Android emulator.
- Produce a **signed AAB** suitable for Play Store upload (document the keystore step).

### Acceptance checklist

The produced prompt must end with an **8–12 item acceptance checklist** Claude Code verifies, e.g.:

1. App cold-starts and loads content from JSON (or cache when offline).
2. App-open ad does **not** fire on the first launch after install.
3. App-open ad fires correctly on subsequent cold/warm starts, frequency-capped.
4. Interstitial respects its frequency cap (does not fire every screen).
5. Interstitial never fires on app close/background.
6. Rewarded ad grants its unlock and the unlock **persists** across restarts.
7. Banner renders on List and Detail without overlapping interactive elements.
8. Dark-mode toggle switches all screens and persists.
9. Favorites persist across restarts (local storage).
10. Navigation works for every screen in the design spec.
11. DEBUG build uses AdMob test IDs; RELEASE uses real IDs.
12. A signed AAB builds successfully.

### AdMob policy warnings — append to the produced prompt

The produced prompt must end with these explicit warnings for Claude Code:

- **Do not place ads near interactive elements** — keep a clear gap between banners and tappable controls (accidental-click policy).
- **Do not fire an interstitial on app close / background** — only between content views or at natural breaks.
- **Do not show an app-open ad on the first install run** — and never overlapping the splash screen.
- Respect interstitial/app-open **frequency caps**; over-showing ads risks AdMob policy strikes.
- Reference: AdMob program policies — https://support.google.com/admob/answer/6128543

## Prompt-construction rules

- Fill the prompt with the real idea and the real design spec — concrete screen names, color tokens, ad placements.
- If the stack is not .NET MAUI, adapt scaffold/structure/ad-plugin guidance to Flutter (`google_mobile_ads`), Kotlin (Compose + Google Mobile Ads SDK), or Swift (SwiftUI + Google Mobile Ads SDK) and keep the policy warnings.
- Keep the prompt self-contained and runnable in a fresh Claude Code session.

## After completing

Print to the console:
1. The path: `outputs/03-build-prompt.md`.
2. A note that the user should open Claude Code in an empty project folder and paste the prompt.

## Next step in the pipeline

**Stage 3 of 7.** Previous step: Stage 2 — `app-prototype-design-prompter` (`outputs/02-design-prompt.md`).

**Next: Stage 4 — `content-data-sourcing-prompter`.** The built app needs its JSON dataset. The next skill produces a prompt that generates that content.

Sample handoff message to the user:

> Build prompt ready at `outputs/03-build-prompt.md`. Run it in Claude Code to build the app. Your app still needs its content — run the `content-data-sourcing-prompter` skill next (say *"make a content prompt"*) and I'll generate a prompt that produces the JSON dataset the app loads.
