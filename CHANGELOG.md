# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/); this project uses [Semantic Versioning](https://semver.org/).

## [0.1.0] — 2026-05-18

Initial release of the claude-app-pipeline — seven Claude skills covering the full path from app idea to Play Store submission.

### Added

- **Skill 01 — `content-app-idea-research`** — researches and shortlists market-validated content app ideas. Improved with pipeline awareness, a stack-adaptation table (.NET MAUI / Flutter / Kotlin / Swift), a Quick mode, an anti-pattern callout, and a standardized `outputs/01-idea-research.md` output.
- **Skill 02 — `app-prototype-design-prompter`** — generates a prompt for Claude.ai (Artifacts) to build an interactive UI prototype.
- **Skill 03 — `app-build-prompter`** — generates a Claude Code prompt that builds the .NET MAUI app with AdMob integration to a polished v1.
- **Skill 04 — `content-data-sourcing-prompter`** — generates a prompt that produces the app's JSON dataset.
- **Skill 05 — `play-store-aso-prompter`** — generates a prompt for policy-compliant Play Store listing copy.
- **Skill 06 — `app-visual-assets-prompter`** — generates image-generation prompts for app icon, feature graphic, and screenshots.
- **Skill 07 — `privacy-policy-prompter`** — generates a prompt for a Play Store-compliant privacy policy and Data Safety form guidance.
- **Tooling** — `scripts/build_all_skills.py` validates and packages every skill into `dist/*.skill`.
- **Repo meta** — `README.md`, `LICENSE` (MIT), `.gitignore`, and an `examples/` placeholder.

[0.1.0]: https://github.com/your-name/claude-app-pipeline/releases/tag/v0.1.0
