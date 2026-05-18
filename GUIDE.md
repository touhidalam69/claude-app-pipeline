# The Complete Beginner's Guide

> From "I want to build an app" to a live Play Store listing — using the claude-app-pipeline. **No prior experience assumed.**

This guide walks you through the **entire pipeline**, end to end. Every stage shows you the **exact words to type**, what the skill will **ask you back**, and a **sample of what it produces**. One example app — a knot-tying reference — is carried through all seven stages so you can see how each output feeds the next.

If you have never used Claude, never written code, and have never published an app, this guide is for you. Read it top to bottom. Don't skip Part 1.

---

## Table of contents

- [Part 0 — What you are about to build](#part-0--what-you-are-about-to-build)
- [Part 1 — Before you start (accounts & tools)](#part-1--before-you-start-accounts--tools)
- [Part 2 — Install the skills](#part-2--install-the-skills)
- [Part 3 — The pipeline, stage by stage](#part-3--the-pipeline-stage-by-stage)
  - [Stage 1 — Idea research](#stage-1--idea-research)
  - [Stage 2 — Design prompt](#stage-2--design-prompt)
  - [Stage 3 — Build prompt](#stage-3--build-prompt)
  - [Stage 4 — Content data](#stage-4--content-data)
  - [Stage 5 — ASO listing copy](#stage-5--aso-listing-copy)
  - [Stage 6 — Visual assets](#stage-6--visual-assets)
  - [Stage 7 — Privacy policy](#stage-7--privacy-policy)
- [Part 4 — Ship to the Play Store](#part-4--ship-to-the-play-store)
- [Part 5 — Troubleshooting & FAQ](#part-5--troubleshooting--faq)

---

## Part 0 — What you are about to build

This pipeline helps a **solo developer** ship a small **content-driven Android app** monetized with **AdMob ads**.

"Content-driven" means the app's value is **curated information you control** — knots, recipes, flashcards, reference cards, facts — delivered from a simple JSON file. No user logins, no chat, no payments inside the app. Just content + ads.

By the end you will have:

| Thing | Where it comes from |
|-------|--------------------|
| A validated app idea | Stage 1 |
| An interactive UI prototype | Stage 2 |
| A built, working Android app (.NET MAUI) | Stage 3 |
| The app's content as a JSON file | Stage 4 |
| Play Store title & description text | Stage 5 |
| App icon, feature graphic, screenshots | Stage 6 |
| A privacy policy (required by Google) | Stage 7 |
| A published app | Part 4 |

**How the skills work:** each skill (Stages 2–7) does **not** do the work itself. It writes a **prompt** — a carefully structured instruction — into a file. You copy that prompt and paste it into the right tool (Claude.ai, Claude Code, or an image generator), and *that* tool does the work. The skill is the expert that knows what to ask for; the destination tool is the worker.

**Realistic time:** 3–6 weeks of part-time work for a polished first version. The pipeline removes guesswork, not effort.

---

## Part 1 — Before you start (accounts & tools)

Set these up **before** Stage 1. Skipping ahead and hitting a missing account mid-pipeline is the most common way to get stuck.

### 1.1 — A Claude account (required, used in every stage)

1. Go to <https://claude.ai> and sign up.
2. A **paid plan (Pro or higher)** is strongly recommended — the research and build stages are long and the free tier will run out of capacity. Check current plans at <https://claude.ai/upgrade>.
3. **Skills** — the feature this whole repo depends on — is under **Settings → Capabilities**. Confirm you can see it. If you can't, see [Part 5](#part-5--troubleshooting--faq).

### 1.2 — Claude Code (required for Stage 3, recommended for the rest)

Claude Code is Claude in your terminal — it can create and edit files on your computer. Stage 3 (building the app) needs it.

- Install instructions: <https://docs.claude.com/en/docs/claude-code/overview>
- It runs on macOS, Windows, and Linux. There is also a VS Code extension.
- You sign in with the **same Claude account** from step 1.1.

If the word "terminal" is new to you: it's a text window where you type commands instead of clicking. Claude Code uses it, but Claude Code itself will write the code — you mostly type plain English.

### 1.3 — A development environment for the app (required for Stage 3)

The pipeline defaults to **.NET MAUI** — Microsoft's framework for building one app that runs on Android and iOS.

1. Install the **.NET 8 SDK (LTS)**: <https://dotnet.microsoft.com/download/dotnet/8.0>
2. Install the **MAUI workload** — open a terminal and run:
   ```
   dotnet workload install maui
   ```
3. Install **Android Studio** (you need its Android SDK and emulator): <https://developer.android.com/studio>

> **Don't want .NET?** The pipeline also supports **Flutter**, **native Android (Kotlin)**, and **native iOS (Swift)**. Just tell the skill your stack in Stage 1 and it adapts. If you pick one of those, install that toolchain instead.

You don't need to *know* .NET — Claude Code writes the code. You need it *installed* so the app can build and run.

### 1.4 — A Google Play Developer account (required to publish)

1. Register at <https://play.google.com/console/signup>.
2. There is a **one-time US$25 fee**.
3. Approval can take a few days — **register early**, during Stage 1, so it's ready by Part 4.

### 1.5 — An AdMob account (required for ads / money)

1. Sign up at <https://admob.google.com>.
2. After your app exists you'll create **ad units** (banner, interstitial, rewarded, app open) and get their IDs.
3. You don't need this until Stage 3. Until then the pipeline uses Google's **official test ad IDs**, so you can build and test without real ads.

### 1.6 — Somewhere to host two files (required, free options exist)

You need a public web address for two things:

- **The content JSON** (Stage 4) — the data your app downloads.
- **The privacy policy HTML** (Stage 7) — Google requires a public privacy-policy URL.

Easiest free option: **GitHub Pages**. Create a free GitHub account at <https://github.com>, make a public repository, enable Pages in its settings, and any file you commit becomes a public URL. Other options: Firebase Hosting, Cloudflare Pages, Netlify.

### 1.7 — An image generator (required for Stage 6)

Stage 6 produces prompts for an **image generator** to draw your app icon and feature graphic. Any of these work:

- **Ideogram** (<https://ideogram.ai>) — best when text must appear crisply in an image.
- **Midjourney**, **Google Imagen**, **DALL·E** — good for icon and feature-graphic art.

A free tier of any one is enough to start.

### Checklist before Stage 1

- [ ] Claude.ai account (paid plan recommended), Skills visible in Settings
- [ ] Claude Code installed and signed in
- [ ] .NET 8 SDK + MAUI workload + Android Studio installed (or your chosen stack)
- [ ] Google Play Developer registration started ($25, may take days)
- [ ] AdMob account created
- [ ] A place to host public files (e.g. GitHub Pages)
- [ ] An image generator account

---

## Part 2 — Install the skills

The skills live in this repo. You install them once. There are two places you'll use skills — Claude.ai (Stages 1, 2, 4, 5, 7 are easiest there) and Claude Code (Stage 3, and any stage where you want the output file written straight to disk).

### 2.1 — Get the skill files

Download or clone this repository. If you have `git`:

```
git clone https://github.com/touhidalam69/claude-app-pipeline.git
```

Or click the green **Code → Download ZIP** button on the GitHub page and unzip it.

Inside you'll find two relevant folders:

- `dist/` — seven pre-packaged `.skill` files, ready to upload to Claude.ai.
- `skills/` — the same seven skills as plain folders, for Claude Code.

### 2.2 — Install in Claude.ai

Do this for **all seven** `.skill` files in `dist/`:

1. Open <https://claude.ai>.
2. Go to **Settings → Capabilities → Skills**.
3. Click **Upload skill**.
4. Select one `.skill` file from `dist/` (e.g. `01-content-app-idea-research.skill`).
5. Repeat for the other six.

Once uploaded, a skill triggers **automatically** when you ask something matching it. You do not type the skill's name — you describe what you want, and Claude picks the skill.

### 2.3 — Install in Claude Code

Claude Code reads skills from a folder. Copy the seven folders from `skills/` into one of these locations:

- **User scope** (available in every project): `~/.claude/skills/`
- **Project scope** (just this project): `<your-project>/.claude/skills/`

So for example `skills/01-content-app-idea-research/` becomes `~/.claude/skills/01-content-app-idea-research/`. After copying, the skills trigger from matching requests in any Claude Code session.

> **Tip:** install in **both** places. Use Claude.ai for the conversational stages and Claude Code when you want the `outputs/*.md` file written directly into your project folder.

### 2.4 — Make a project folder

Create one empty folder for your whole app project, e.g. `my-knot-app/`. Every skill writes its output into an `outputs/` subfolder here, and Stage 3 builds the app here. Open this folder when you start Claude Code.

---

## Part 3 — The pipeline, stage by stage

**The worked example.** From here on, this guide follows one imaginary developer building one app, so you can see how each stage's output becomes the next stage's input. The example app: **a knot-tying reference for sailors and climbers**.

Each stage below has the same layout:

- **What it does** — the point of the stage.
- **What you type** — the exact words to give Claude.
- **What it asks you** — questions the skill may ask back, and how to answer.
- **Sample output** — an excerpt of what you get.
- **What you do next** — your action before moving on.

---

### Stage 1 — Idea research

**What it does.** Researches real market demand and hands you a shortlist of app ideas that a solo developer can realistically build and monetize — each one backed by actual Play Store listings, Reddit threads, and search interest. This is the only stage that does research instead of writing a prompt.

**Where to run it.** Claude.ai (or Claude Code if you want the report saved to disk automatically).

**What you type:**

> what content app should I build? I can do .NET MAUI, I want to monetize with AdMob, and I'd like a niche reference-style app.

You can be vaguer than that — even *"find me an app idea"* triggers the skill. The more you say about your stack, interests, and constraints, the better the research.

**What it asks you.** The skill may ask **once** about anything important you left out — for example your target region, whether the app must be family-friendly, or your language. Answer briefly. If you don't care, say *"use the defaults"* and it proceeds (defaults: .NET MAUI, global English audience, all four AdMob formats, 3–6 week solo build).

> **Faster pass:** add the word *"quick"* (e.g. *"quick research, find me an app idea"*) to get a trimmed report with 3 ideas instead of 5–8.

**Sample output.** The skill writes a full report to `outputs/01-idea-research.md`. An excerpt:

```markdown
## Executive summary

Top pick: **Knot Tying Guide for Sailors & Climbers** — a step-by-step
reference app for practical knots, organized by use case. The niche has
proven content appetite (knot-tying YouTube videos draw millions of
views; r/sailing and r/climbing regularly ask for offline references)
yet the top Play Store results are dated, ad-heavy, and poorly rated
(3.4–3.9 stars). Clear ASO gaps on long-tail terms.

### Finalist 1 — Knot Tying Guide for Sailors & Climbers

**One-line pitch:** "A pocket knot reference for people who actually
tie knots — sailors, climbers, scouts, arborists."

**Content theme + sample entries:**
  - Bowline — "The rescue knot. Forms a fixed loop that won't slip..."
  - Clove Hitch — "Fast, adjustable attachment to a post or rail..."
  - Figure-8 Follow-Through — "The climber's tie-in knot..."

**App flow:** Home → Category list → Knot detail (steps + diagram)
  - Banner: pinned on the category list and knot detail screens
  - Interstitial: on category switch, capped at 1 per 5 knot views
  - Rewarded: unlock the "Advanced / Arborist" knot pack
  - App open: on cold start (never on first launch)

**Scoring:** Demand 4 · ASO opportunity 5 · Content producibility 4 ·
Ad-surface fit 5 · Session frequency 3 · Policy safety 5 · Defensibility 4

Sources: <reddit.com/r/sailing/...>, <play.google.com/store/apps/...>, ...
```

**What you do next.** Read the report. Pick the idea you want to build. Tell Claude which one:

> I'll go with the knot tying app.

---

### Stage 2 — Design prompt

**What it does.** Turns your chosen idea into a **design prompt** — a detailed instruction you paste into Claude.ai to generate an **interactive UI prototype** (clickable mock screens) plus a design spec (colors, fonts, spacing).

**Where to run the skill.** Same Claude session as Stage 1 is ideal — it already knows your idea.

**What you type:**

> make a design prompt

**What it asks you.** It may confirm brand direction (color, mood) and which screens you want. Defaults are sensible — *"use the defaults"* is a fine answer. Default screens: Home, List/Browse, Detail, Settings/About.

**Sample output.** The skill writes the prompt to `outputs/02-design-prompt.md`. You then **open a new Claude.ai chat**, and paste:

1. A short intro line the skill gives you:

   > Hi Claude — please enable Artifacts and follow the prompt below to build an interactive UI prototype for my app. Produce the prototype artifact first, then the design spec, then the plain-text design spec summary at the end.

2. The entire contents of `outputs/02-design-prompt.md` below it.

Claude.ai then produces a **clickable prototype** in an Artifact (you can tap through the screens) and, at the end, a **design spec summary** that looks like this:

```
DESIGN SPEC SUMMARY
Colors:  primary #1B4965  accent #FF7F11  bg #F7F9FB  surface #FFFFFF
         text #1A1A1A  muted #6B7280   (dark: bg #0E1721 surface #16232F)
Type:    Inter — display 28 / title 20 / body 15 / caption 12
Spacing: 4 / 8 / 12 / 16 / 24 / 32
Screens: Home, Categories, Knot Detail, Favorites, Settings
  Home          → Shell tab + ContentPage
  Categories    → CollectionView in a ContentPage
  Knot Detail   → ContentPage bound to a ViewModel
Ads: banner on Categories+Detail; interstitial on category switch;
     rewarded unlocks Advanced pack; app open on cold start
```

**What you do next.** Look at the prototype. If you want changes, ask Claude.ai in that same chat ("make the accent color green", "add a search screen"). When happy, **copy the plain-text design spec summary** — you need it for Stage 3.

---

### Stage 3 — Build prompt

**What it does.** Turns the design spec into a **Claude Code prompt** that builds the **actual working app** — real .NET MAUI code, AdMob wired in, ready to run on an emulator.

**Where to run the skill.** Bring the design spec summary back to your pipeline chat (Claude.ai or Claude Code).

**What you type:**

> make a build prompt

Then, when asked, **paste the design spec summary** you copied from Stage 2.

**What it asks you.** Up to three things:

- **The design spec summary** — paste it (critical; it will ask if missing).
- **JSON endpoint URL** — the web address where your content will live. You don't have it yet — say *"use a placeholder"* and it inserts a clearly-marked TODO.
- **App package name** — a unique ID like `com.yourname.knotguide`. Pick one now, or accept the `com.example` placeholder and fix it later.
- **AdMob ad unit IDs** — you don't have these yet — say *"use test IDs"*. The app will use Google's official test ads until you swap in real ones.

**Sample output.** The skill writes the prompt to `outputs/03-build-prompt.md`. Now:

1. Open **Claude Code** in your empty project folder.
2. Paste the entire contents of `outputs/03-build-prompt.md`.
3. Claude Code scaffolds the project, writes the screens, wires AdMob, and works through an acceptance checklist like:

   ```
   [x] App cold-starts and loads content from JSON (or cache when offline)
   [x] App-open ad does NOT fire on the first launch after install
   [x] Interstitial respects its frequency cap
   [x] Rewarded ad grants its unlock and the unlock persists across restarts
   [x] Banner renders without overlapping interactive elements
   [x] Dark-mode toggle switches all screens and persists
   [x] DEBUG build uses AdMob test IDs; RELEASE uses real IDs
   [x] A signed AAB builds successfully
   ```

**What you do next.** Let Claude Code build and run the app on the Android emulator. Click around. The app will show **test ads** and **placeholder content** (no real data yet) — that's expected. The content comes next.

---

### Stage 4 — Content data

**What it does.** Produces a **prompt that generates your app's content** as a single JSON file — the actual knots, recipes, or facts your app displays.

**What you type:**

> make a content prompt

**What it asks you.** It may confirm the content schema (field names), how many entries, and category balance. Defaults: **200 entries**, 8 categories × 25 each, fields `id` / `title` / `category` / `body` / `tags`. Match the schema to whatever Stage 3's app expects — if unsure, *"use the defaults"*.

**Sample output.** The skill writes the prompt to `outputs/04-content-prompt.md`. You **run that prompt** (paste it into Claude.ai or Claude Code). It generates one big JSON array:

```json
[
  {
    "id": 1,
    "title": "Bowline",
    "category": "Boating",
    "body": "Forms a fixed loop that will not slip or jam. Make a small loop, pass the working end up through it, around the standing line, and back down through the loop. Dress and tighten.",
    "tags": ["loop", "rescue", "essential"]
  },
  {
    "id": 2,
    "title": "Clove Hitch",
    "category": "Boating",
    "body": "A fast, adjustable hitch for securing a line to a post or rail...",
    "tags": ["hitch", "quick", "adjustable"]
  }
]
```

> **⚠️ Important — spot-check the content.** AI-generated content is **not verified**. Read through the entries and fix anything wrong **before you ship**. A knot reference with a wrong tying step, or a study app with a wrong fact, loses user trust fast and can attract Play Store policy attention. Curation is your product.

**What you do next.** Save the JSON, spot-check it, then **host it** at a public URL (your GitHub Pages address from Part 1.6). Go back into Claude Code and replace the placeholder JSON URL from Stage 3 with this real one.

---

### Stage 5 — ASO listing copy

**What it does.** Produces a **prompt that writes your Play Store listing text** — app title, short and long descriptions, "what's new" — tuned for search (ASO = App Store Optimization) and compliant with Google Play policy.

**What you type:**

> make an ASO prompt

**What it asks you.** Your app's main features and a list of target keywords. If you ran a full Stage 1, the keyword shortlist is already there — *"use the keywords from the research"* works.

**Sample output.** The skill writes the prompt to `outputs/05-aso-prompt.md`. Run that prompt and you get listing copy with exact character limits respected:

```
TITLE (max 30):  Knot Tying Guide — Sailing
SHORT (max 80):  Step-by-step knots for sailing, climbing & camping — works offline.

LONG DESCRIPTION (max 4000):
Tie the right knot, every time.

Whether you're rigging a sailboat, setting an anchor on a climb, or
pitching a tent, the wrong knot costs you time — or safety. Knot Tying
Guide is a clear, offline reference for the knots that matter.

• Step-by-step instructions for 200+ practical knots
• Organized by use: boating, climbing, camping, fishing, rescue
• Works fully offline — no signal needed on the water or the wall
• Save your go-to knots to Favorites
• Clean, distraction-free reading with a dark mode

This app is free and supported by ads.

Made for sailors, climbers, scouts, arborists, and anyone who works
with rope. Download Knot Tying Guide and never forget a knot again.

WHAT'S NEW (max 500):  First release — 200+ knots across 8 categories...
```

**What you do next.** Open Play Console, paste each field into the matching listing box, and re-check the character counts there (Play Console counts strictly).

---

### Stage 6 — Visual assets

**What it does.** Produces **image-generation prompts** for the visuals Google requires: app icon (512×512), feature graphic (1024×500), and phone screenshots.

**What you type:**

> make a visual assets prompt

**What it asks you.** Your app's mood/brand direction and color palette. If Stage 2 produced a design spec, *"use the palette from the design spec"* works.

**Sample output.** The skill writes prompts to `outputs/06-visual-assets-prompts.md`. Excerpt:

```
=== APP ICON — 512×512 (3 variants) ===

[Minimalist]
A single clean bowline knot rendered as a smooth continuous rope loop,
deep navy (#1B4965) rope on a soft off-white background, flat vector
style, no text, no shadows, centered with generous margin, legible at
small size. Square 512x512.

[Illustrative]  ...
[Geometric]     ...

=== FEATURE GRAPHIC — 1024×500 ===
A coil of nautical rope arranged on the right third of the frame against
a deep navy gradient, warm orange accent light, calm and practical mood.
No text in the image — leave the left two-thirds clean. 1024x500.

=== PHONE SCREENSHOTS — 5 designs ===
Screenshot 1 — real "Categories" screen of the app.
  Headline overlay: "Every knot, organized by what you're doing"
  Background: deep navy band, white headline text
...
```

**What you do next.** Paste the icon and feature-graphic prompts into your image generator. For screenshots, take **real screenshots from your built app** running in the emulator, then add the headline overlays the skill gave you.

---

### Stage 7 — Privacy policy

**What it does.** Produces a **prompt that writes a privacy policy** — which Google **requires** for every app, especially ad-supported ones (AdMob collects an advertising ID). It also generates a helper for filling Play Console's Data Safety form.

**What you type:**

> make a privacy policy prompt

**What it asks you.** Three things it needs (it will ask if missing):

- **App name** — e.g. `Knot Tying Guide`
- **Developer name** — your name or company
- **Contact email** — a working address for privacy questions

It also asks whether the app **targets children** (default no — if yes, it adds COPPA sections).

**Sample output.** The skill writes the prompt to `outputs/07-privacy-policy-prompt.md`. Run it and you get a complete policy in **both HTML and Markdown**, plus a Data Safety form guide:

```
DATA SAFETY FORM — how to answer in Play Console

Data collected:           Device or other IDs (advertising ID)
  Collected by:           the Google AdMob SDK
  Purpose:                Advertising or marketing
Shared with third parties: Yes — with Google, for advertising
Data encrypted in transit: Yes
Users can request deletion: Yes — describe the device ad-settings reset

⚠ The Data Safety answers MUST match the privacy policy. Google
  rejects submissions where they disagree.
```

> This is general drafting help, **not legal advice**. For anything beyond a simple ad-supported app, have it reviewed for your jurisdiction.

**What you do next.** Host the **HTML** policy at a public URL (GitHub Pages again). Keep the URL — Play Console asks for it.

---

## Part 4 — Ship to the Play Store

You now have everything. Final assembly in the **Play Console** (<https://play.google.com/console>):

1. **Create the app** — click *Create app*, enter the name and default language.
2. **Build the release file** — in Claude Code, ask it to produce a **signed AAB** (Android App Bundle). It will walk you through creating a **keystore** — a signing key. **Back up that keystore file and its passwords somewhere safe.** Lose it and you can never update the app again.
3. **Swap in real AdMob IDs** — in AdMob, create your four ad units, copy their IDs, and replace the test IDs in the app. Rebuild the RELEASE AAB.
4. **Upload the AAB** — under *Production → Create release*.
5. **Store listing** — paste the Stage 5 title and descriptions; upload the Stage 6 icon, feature graphic, and screenshots.
6. **Privacy policy** — paste the Stage 7 policy URL into the listing.
7. **Data Safety form** — fill it using the Stage 7 helper. **It must match the privacy policy.**
8. **Content rating** — complete the IARC questionnaire (Stage 5 output suggested answers).
9. **App access & ads declaration** — declare that the app **contains ads** (it does — AdMob).
10. **Submit for review.** First reviews typically take a few days.

When it's approved, your app is live. 🎉

> **Before you submit, re-check:** real AdMob IDs in the RELEASE build (not test IDs) · the JSON endpoint is the live public URL · the privacy-policy URL loads · the Data Safety form matches the policy · you have backed up the keystore.

---

## Part 5 — Troubleshooting & FAQ

**I don't see "Skills" in Claude.ai settings.**
Skills availability depends on your plan and account. Confirm you're on a paid plan and look under **Settings → Capabilities**. See Anthropic's docs: <https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>

**The skill didn't trigger when I asked.**
Skills trigger on matching phrasing. Be explicit and use the trigger phrases in this guide — e.g. *"make a build prompt"*, *"make an ASO prompt"*. If it still doesn't fire, name the skill directly: *"use the app-build-prompter skill"*.

**A skill asked me questions I don't know how to answer.**
Reply *"use the defaults"*. Every skill has sensible defaults for everything non-critical. It only hard-requires a few things (your chosen idea, the design spec, your app name/email for the policy).

**Where do the output files go?**
Into an `outputs/` folder in whatever directory you're working in. Run the skills from your project folder so they collect in one place. Stage 1 → `outputs/01-idea-research.md`, Stage 2 → `outputs/02-design-prompt.md`, and so on through `07-`.

**Do I have to use .NET MAUI?**
No. Tell the skill in Stage 1 if you prefer **Flutter**, **Kotlin** (Android only), or **Swift** (iOS only). Every skill adapts its guidance. The pipeline just defaults to .NET MAUI.

**The build prompt mentions test ad IDs — will I earn money?**
Test IDs show real-looking ads but **never pay** and must **never** ship in a release build. Clicking your own real ads gets your AdMob account banned — test IDs exist to let you develop safely. Swap in real IDs only for the RELEASE build (Part 4, step 3).

**Can I run the whole pipeline in one Claude chat?**
Stages 1, 2, 4, 5, 7 can share one Claude.ai chat — context carries forward, which helps. Stage 3 must run in **Claude Code**. Stage 6's prompts go into an **image generator**. Stage 2's design prompt is run in a **fresh** Claude.ai chat with Artifacts on.

**My app got rejected by Google.**
Read the rejection reason carefully — it's usually specific. Common causes: Data Safety form doesn't match the privacy policy, missing or unreachable privacy-policy URL, ads placed too close to buttons (accidental-click policy), or undeclared ads. Fix and resubmit.

**Is AI-generated content safe to ship?**
Only after **you spot-check it**. The content prompt (Stage 4) generates a draft; factual errors are your responsibility to catch. A reference app with wrong information loses trust and risks policy issues.

**How much does all this cost?**
Claude paid plan (monthly) · Google Play registration ($25 one-time) · hosting (free tier is fine) · image generator (free tier is fine). AdMob is free and pays *you*.

---

*This is a community pipeline, not affiliated with or endorsed by Anthropic or Google. Built for use with [Claude](https://claude.ai). Questions or improvements — open an [issue](../../issues).*
