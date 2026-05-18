---
name: content-app-idea-research
description: Research and shortlist content-driven mobile app ideas where the value comes from curated content the developer controls (served via a simple JSON CMS endpoint), monetized 100% with AdMob (banner, interstitial, rewarded, app open). Use this skill whenever the user wants help finding a small mobile app idea to build solo, especially when they mention .NET MAUI, Xamarin, Flutter, native Android (Kotlin), native iOS (Swift), AdMob, ad monetization, content app, niche app, JSON backend, static data, or wants market research / niche validation for a small mobile app. Trigger on phrases like "find me an app idea", "what app should I build", "market research for an app", "niche app idea", "AdMob app", "content app idea", "app with banner and rewarded ads", or any similar request — even if the user does not say the word "skill" or "research" explicitly. Use this in preference to giving generic startup advice.
---

# Content App Idea Research

This skill produces a market-validated, evidence-backed shortlist of small content-driven mobile app ideas a single developer can build to a polished v1 in 3–6 weeks and monetize with AdMob.

It is a structured research workflow, not a brainstorm. Every recommendation must be backed by real sources (Play Store / App Store listings, Reddit threads, forum posts, search trends). Unsourced claims must be cut.

## What "content-driven" means here

Apps where:
- The value is **curated content the developer controls** — quotes, recipes, reference cards, prompts, facts, exercises, study material, fact-of-the-day, cheat sheets, scripts, templates, etc.
- The "backend" is a simple JSON endpoint the developer updates manually — could be a static JSON file on GitHub Pages, Firebase Realtime DB, Supabase, Cloudflare R2, or a tiny Express service. **No user accounts, no UGC, no realtime, no chat, no payments inside the app.**
- The app is read-only from the user's perspective; favorites/bookmarks are local-only.
- Monetization is **100% AdMob**, with natural surfaces for all four formats: banner, interstitial, rewarded, app open.

This is distinct from:
- **API mashup apps** (which wrap third-party live APIs like weather, sports, flights, finance)
- **SaaS apps** (which require backend logic, accounts, and subscriptions)

If the user is asking about either of those, this skill is not the right fit — say so.

## Confirm inputs before researching

Defaults if the user hasn't specified:
- **Stack**: .NET MAUI, Android-first (codebase also builds for iOS)
- **Monetization**: AdMob with all four formats — banner, interstitial, rewarded, app open
- **Scope**: solo developer, 3–6 weeks to polished v1
- **Audience**: global, English-first

If the user has specified a different mobile stack (Flutter, native Android/Kotlin, native iOS/Swift, React Native, Xamarin), use theirs — the methodology is identical. If the user explicitly wants a different monetization (IAP, subscription, Play Billing only), adjust the scoring on monetization but keep everything else.

If anything important is unclear (target region, family-friendly requirement, language preference), ask once before starting. Otherwise proceed.

## Research process — execute in order

Use WebSearch and WebFetch heavily. Read actual threads, reviews, and listings — don't just cite domains.

### Step 1: Identify 4–6 candidate niches with content appetite

Niches that historically support content apps include: hobby reference (knots, chess openings, guitar chords, origami, knitting), profession cheat sheets (nurses, EMTs, electricians, chefs), study/exam prep (driving tests by country, medical mnemonics, vocabulary), affirmations/inspiration by demographic, recipes by diet/culture/constraint, workouts for specific demographics, language phrasebooks for niche use (travelers, business, medical), kids' content (animal facts, riddles, story starters), self-help frameworks, journaling prompts, dream interpretation, name suggestions (baby, business, pet), speech/toast/condolence templates, drawing/coloring inspiration, gardening calendars, pet care by breed, DIY craft ideas, meditation scripts, etiquette guides, daily challenges, country/culture facts.

Skip commodity categories (generic quotes, generic jokes, generic wallpapers, generic horoscope) unless you find a genuinely sharp niche angle.

Pick 4–6 niches to investigate seriously. State each as a one-line audience description.

### Step 2: Verify niche demand

For each candidate niche:
- **Play Store**: search relevant keywords. Note download tier (10K+, 100K+, 1M+, 10M+), rating, and last-update date for the top 5 apps. **Sweet spot**: total downloads in the niche in the 500K–10M range, with top apps rated 3.5–4.2 and many recent complaints. **Bad signs**: <50K total downloads (no demand) or one dominant app with 10M+ downloads and 4.5+ stars (saturated).
- **Reddit / niche forums**: search for active communities, posts asking for tools or resources, recurring requests. Quote 2–3 real posts with URLs.
- **Adjacent content demand**: check Pinterest, TikTok hashtags, YouTube search volume — does the topic have a real content audience? If millions of people search for "knot tying" videos, a knot-tying app has appetite.

### Step 3: ASO (App Store Optimization) opportunity check

For each surviving niche:
- List 10–20 specific long-tail keywords a user might type in Play Store search.
- For each keyword, look at top 3–5 results. Note if they're weak (low downloads, ugly UI, last update >1 year ago, generic names) or strong (top apps dominate).
- **Win condition**: at least 5 keywords where current top results are weak. That's your ASO foothold.

### Step 4: Verify content is producible and legal

For each idea, answer concretely:
- Where does the content come from — manually written by the dev, AI-generated, public domain, openly licensed (CC0 / CC-BY), licensed dataset, scraped from a permissive source?
- Minimum content volume for a credible v1 (e.g., "200 entries across 8 categories")
- Maintenance cadence (hours/week to keep fresh)
- **Legal status — must be clean**: no copyrighted song lyrics, no copyrighted poems/books, no movie/TV quotes under copyright, no brand IP, no celebrity photos. Flag any gray areas with red 🚨.

### Step 5: Verify AdMob ad-surface fit

Sketch the app flow (Home → List → Detail, etc.) and identify natural slots for:
- **Banner**: persistent on list/detail screens
- **Interstitial**: at category switches or after every N content views (5+ is typical to avoid policy issues)
- **Rewarded**: a genuine "unlock" or "earn this" moment — premium category, daily bonus item, shuffle, ad-free hour, hint, etc. Must feel optional, not coercive.
- **App open**: cold/warm starts (per Google policy — never on first launch after install, no overlap with splash, frequency-capped)

If an idea can't surface all four naturally without being user-hostile, downgrade it.

### Step 6: AdMob policy + RPM check

For each surviving idea:
- Is the content in a restricted AdMob category? (graphic content, dangerous products, misleading health/financial claims, sensitive religious framing, hate speech, sexual content) — flag any policy risk.
- Estimate ad RPM. Some niches have high CPM (finance, business, B2B, professional study) and some have low CPM (kids' entertainment, casual quotes). Note this honestly per idea.
- For kids' content: trigger Designed for Families and COPPA-compliant ad config. Note this constraint.

### Step 7: Score and rank

Score each remaining idea 1–5 on:
- **Niche demand** — addressable installs
- **ASO opportunity** — gap between demand and incumbent quality
- **Content producibility** — can the dev realistically build and maintain the dataset?
- **Ad-surface fit** — do all 4 formats appear naturally?
- **Session frequency** — daily / weekly / monthly use (daily beats monthly)
- **Policy + copyright safety** — green / yellow / red
- **Defensibility** — can a competitor clone it in a weekend? (specific niche, curated quality, localization, brand)

Drop anything red on policy/copyright or below 3 on demand or ad fit.

## Deliverable

Write the full report to `./content-app-research.md` in the working directory. Structure:

1. **Executive summary** — top 3 ideas in one paragraph each, plus the single top pick with reasoning.
2. **For each of the 5–8 finalists**:
   - **One-line pitch** ("X for Y")
   - **The niche** — who exactly, with evidence (Reddit, forum, YouTube, Pinterest URLs)
   - **Content theme + 3–5 sample entries** so the dev can see what the app shows
   - **Content sourcing plan** — origin, legal status, v1 size, maintenance cadence
   - **App flow** — screen-by-screen sketch in text, marking where each AdMob format fits
   - **Play Store competition** — 3–5 competitors with download tier, rating, what they do badly
   - **ASO keyword shortlist** — 10–20 specific keywords with opportunity notes
   - **Monetization detail** — expected RPM range, primary ad surfaces, rewarded ad unlock moment
   - **Distribution plan** — concrete channels to seed first 5,000 installs (specific subreddits, niche forums, TikTok hashtags, Pinterest boards, ASO). Not "do marketing."
   - **Scoring table** with the 7 criteria
   - **Risks** — policy, copyright, niche-too-small, incumbent retaliation
3. **Ideas I rejected and why** — at least 5 entries, so the dev sees the filtering.
4. **Sources** — flat list of every URL used.

## Process rules

- Cite sources inline with URLs. Unsourced claims get deleted.
- Be ruthless about commodity categories — generic quotes/jokes/wallpapers/horoscope/flashlight rarely win for a new entrant.
- Be honest about ad RPM realities — don't pad weak niches with optimistic revenue estimates.
- Flag every AdMob policy edge case explicitly. Religious content, health claims, anything targeting kids, and anything political need careful framing.
- Don't recommend ideas requiring user accounts, UGC, realtime sync, or in-app purchases — they violate the constraints.
- Avoid country-locked ideas unless the country is large and English-friendly (or the user has specified a target region).
- "AI-generated content" is fine **as a sourcing method**, but the workflow and curation must be the product — not "an AI chatbot inside the app."
- If the user has specified a stack other than .NET MAUI, use theirs throughout the report.

## After completing

Print a one-paragraph summary of the top pick. Ask the user which idea to go deeper on. Offer this follow-up explicitly: *"I can produce a v1 feature spec, screen-by-screen wireframe outline, content sourcing plan, and ASO keyword plan for the chosen idea — just say the word."*

## Notes for adapting to neighboring use cases

If the user later asks for similar research for **API-mashup mobile apps** (apps wrapping third-party live APIs like weather/sports/finance) or **web micro-SaaS** (web tools sold via Lemonsqueezy/Stripe), the methodology transfers but the constraints, sources, and scoring change meaningfully. Don't try to force this skill onto those use cases — tell the user this skill is for content-driven ad-monetized mobile apps specifically, and that a separate skill or prompt should be used for the other categories.
