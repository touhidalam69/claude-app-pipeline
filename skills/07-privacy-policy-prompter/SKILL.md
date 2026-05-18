---
name: privacy-policy-prompter
description: Generate a prompt that produces a Play Store-compliant privacy policy for an ad-supported app — required for any app using AdMob. This is Stage 7, the final stage, of the claude-app-pipeline. Use this skill whenever the user needs a privacy policy or help with the Play Console Data Safety form. Trigger on phrases like "privacy policy", "data safety", "Play Store privacy", "privacy policy prompt", "make a privacy policy", "I need a privacy policy", "data safety form", or any similar request. Do not write the final policy yourself — this skill produces the PROMPT the user runs to generate it.
---

# Privacy Policy Prompter

**Stage 7 of the claude-app-pipeline — the final stage.** This skill produces a single prompt that generates a **Play Store-compliant privacy policy**. Google Play **requires** a privacy policy for every app, and especially for apps using ads (AdMob collects an advertising ID and device data).

The skill produces the **prompt**. The user runs it to get the policy. This is general drafting help, **not legal advice** — the produced prompt and the skill output must say so.

## Confirm inputs before generating

Ask **once** for anything critical missing; otherwise default and proceed.

- **App name** *(critical)* — the published app name.
- **Developer name** *(critical)* — person or company publishing the app.
- **Contact email** *(critical)* — a working address for privacy inquiries.
- **Data collection** — default for this pipeline: **the app collects no personal data from the user directly**; **AdMob (Google) collects an advertising ID + device/usage info** per Google's terms. Favorites/settings are local-only.
- **Targets children?** — default **no**. If **yes**, the policy adds **Designed for Families / COPPA** sections and the AdMob config must use child-directed treatment.
- **Developer country** — for jurisdiction wording. If unknown, keep jurisdiction wording generic and note it.

## Deliverable

Write the prompt to `outputs/07-privacy-policy-prompt.md` in the working directory (create `outputs/` if needed). The file contains a single prompt the user runs. The prompt must instruct the model to produce a complete privacy policy:

### Format

- The full policy in **both HTML and Markdown** (HTML to host at a public URL; Markdown for the repo). The HTML must be a standalone, hostable page.

### Required sections

1. **Introduction** — app name, developer, effective date.
2. **Data we collect** — state plainly that the app itself collects no personal data directly; favorites/settings stay on the device.
3. **AdMob & advertising data** — Google AdMob collects an advertising ID, device information, and usage data to serve ads; explain in plain English.
4. **Third parties** — Google AdMob / Google Play Services named; link to Google's policies.
5. **User rights — GDPR & CCPA** — access, deletion, opt-out of personalized ads (via device ad settings).
6. **Children's privacy — COPPA** — include a full COPPA section **only if the app targets children**; otherwise a short standard "not directed to children under 13" statement.
7. **Data retention** — what is kept and for how long (local data: until the user uninstalls).
8. **Security** — reasonable-measures statement.
9. **Changes to this policy** — how updates are communicated.
10. **Contact** — the developer's privacy contact email.

### Style & references

- **Plain English** — no dense legalese.
- Include a **direct link to Google's advertising privacy policy**: https://policies.google.com/technologies/ads
- The produced policy must carry a short line that it is a general template, not legal advice.

### Data Safety form helper

The produced prompt must also generate a **"How to fill the Play Console Data Safety form"** helper section that maps this policy to the Data Safety questionnaire — e.g.:

- **Data collected**: Device or other IDs (advertising ID) — collected, by the AdMob SDK.
- **Purpose**: Advertising or marketing.
- **Shared with third parties**: Yes — Google, for advertising.
- **Data encrypted in transit**: Yes.
- **Users can request deletion**: describe the mechanism.
- The Data Safety declaration **must match the privacy policy** — Google rejects mismatches.

### Policy references — cite in the produced file

- Play privacy policy requirement: https://support.google.com/googleplay/android-developer/answer/10787469
- Play Data Safety form guidance: https://support.google.com/googleplay/android-developer/answer/9888076

## Prompt-construction rules

- Fill the prompt with the real app name, developer name, and contact email.
- Make the children's-privacy depth conditional on the "targets children" answer.
- Make the prompt self-contained and runnable in one paste.

## After completing

Print to the console:
1. The path: `outputs/07-privacy-policy-prompt.md`.
2. A reminder: host the HTML policy at a public URL, paste that URL into Play Console, and ensure the Data Safety form matches the policy.
3. A note that this is general drafting help, not legal advice — recommend review for the developer's jurisdiction.

## Next step in the pipeline

**Stage 7 of 7 — the final stage.** Previous step: Stage 6 — `app-visual-assets-prompter` (`outputs/06-visual-assets-prompts.md`).

**Next: ship.** With all seven outputs done — idea, design, build, content, ASO copy, visual assets, privacy policy — the user has everything for a Play Store submission.

Sample closing message to the user:

> Privacy policy prompt ready at `outputs/07-privacy-policy-prompt.md` — that's the final pipeline stage. Run it, host the HTML policy, and you now have the full set: built app, content, listing copy, visual assets, and privacy policy. Time to submit to the Play Store. Good luck.
