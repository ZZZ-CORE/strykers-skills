# Strykers Creative Studio — 24-Skill Library

**Version:** 1.0
**Created:** October 26, 2026
**Purpose:** GitHub repository planning and implementation reference
**Originating chat:** Strykers Creative Studio GPT configuration
**Prepared by:** ChatGPT
**Source task:** Document all 24 proposed skills for the Empire Strykers creative production workflow.

> **Implementation status:** These are proposed skill specifications. Listing a skill here does not mean it is implemented, installed, connected to an external service, or production-tested.

## Overview

Strykers Creative Studio is a proposed modular creative production system for the Empire Strykers. It supports brand-compliant graphics, image editing, video production, Canva and Higgsfield handoffs, social content, asset management, and team approval workflows.

The **Empire Strykers Official Brand Kit** is the primary source of truth. Approved original logo assets and verified team materials must be used for production.

### Brand requirements

* **Official colors:** `#FFFFFF`, `#B8BABC`, `#A3A5A9`, `#6E6E71`, `#000000`, `#953493`, `#9F3E97`.
* **Off-season titles:** Beachwood UltraBold.
* **In-season titles:** Impact.
* **Subtitles:** Dharma Gothic Exbold Italic.
* **Professional body text:** Futura Condensed Medium.
* **Artsy body text:** Sketchnote Text Italic.
* **Accent typography:** Snell Roundhand.
* **Brand messaging:** “Inspire The Empire,” Inland Empire community, family-friendly professional arena soccer, team pride, energy, and inclusivity.
* **Brand verification:** Official logos, player likenesses, sponsor identities, factual claims, typography, colors, and platform dimensions must be reviewed.

---

# Category 1 — Brand Identity and Protection

## 01. Brand Guardian

**Suggested folder:** `skills/brand/brand-guardian/`

**Description:** Enforces the official Empire Strykers brand guidelines across all generated images, videos, captions, campaigns, and exported assets.

**Responsibilities:**

* Read and prioritize the official Brand Kit.
* Apply approved colors, typography, logo rules, and messaging.
* Identify noncompliant design choices.
* Prevent unsupported substitutions for official logos and team imagery.
* Produce a brand-compliance summary.

**Inputs:** Creative request, official Brand Kit, approved assets, platform requirements.

**Outputs:** Brand-locked creative brief, compliance notes, recommended corrections.

**Acceptance criteria:** Every reviewed design is assessed against applicable official brand rules.

## 02. Logo & Lockup Validator

**Suggested folder:** `skills/brand/logo-validator/`

**Description:** Checks correct use of Empire Strykers logos, wordmarks, and co-branded arrangements.

**Responsibilities:**

* Verify original approved logo artwork.
* Check proportions, placement, contrast, and approved colorways.
* Validate partner-logo arrangements.
* Flag altered or AI-reconstructed logos.

**Outputs:** Logo validation report and placement corrections.

**Acceptance criteria:** No unapproved logo modification is treated as compliant.

## 03. Brand Typography Manager

**Suggested folder:** `skills/brand/typography-manager/`

**Description:** Selects and validates approved typography for seasonal campaigns, social graphics, and professional communications.

**Responsibilities:**

* Apply the appropriate in-season or off-season title font.
* Define subtitle, body, and accent text hierarchy.
* Check legibility and spacing.
* Flag missing or substituted fonts for review.

**Outputs:** Typography specification and font compliance report.

**Acceptance criteria:** Font choices align with the official Brand Kit or are explicitly marked for review.

## 04. Brand QA Inspector

**Suggested folder:** `skills/brand/brand-qa/`

**Description:** Conducts a final brand-compliance review before creative assets are approved or exported.

**Responsibilities:**

* Check logos, colors, typography, messaging, and layouts.
* Verify visual consistency.
* Report specific issues with recommended fixes.
* Assign PASS, NEEDS REVIEW, or BLOCKED status.

**Outputs:** Structured QA checklist and findings report.

**Acceptance criteria:** No asset is labeled PASS without supporting checks.

---

# Category 2 — Image Creation and Editing

## 05. Creative Brief Builder

**Suggested folder:** `skills/images/creative-brief-builder/`

**Description:** Converts short user requests into detailed, brand-compliant production briefs.

**Responsibilities:**

* Determine campaign purpose and audience.
* Select output dimensions and creative direction.
* Identify required approved assets.
* Prepare headlines, layout instructions, and brand rules.

**Outputs:** Production-ready creative brief.

**Acceptance criteria:** The brief contains enough information to create a usable first draft without inventing essential facts.

## 06. Background Removal Studio

**Suggested folder:** `skills/images/background-removal/`

**Description:** Removes photo backgrounds while preserving authentic player, mascot, jersey, and logo details.

**Responsibilities:**

* Create transparent PNG cutouts.
* Refine hair, clothing, and object edges.
* Preserve source-subject appearance.
* Verify transparency using alpha-channel checks.
* Flag altered identity or uniform details.

**Outputs:** Transparent PNG and quality-control report.

**Acceptance criteria:** Transparency and subject fidelity are actually verified, not merely assumed from a preview.

## 07. Player Image Integrity

**Suggested folder:** `skills/images/player-image-integrity/`

**Description:** Protects the visual identity and authenticity of Empire Strykers players during AI-assisted editing.

**Responsibilities:**

* Preserve faces and recognizable features.
* Protect jersey numbers, badges, and sponsor marks.
* Compare edits against original source images.
* Flag fabricated or inconsistent details.

**Outputs:** Image-integrity assessment.

**Acceptance criteria:** Material changes to player identity or official uniform details are identified for correction.

## 08. Social Template Factory

**Suggested folder:** `skills/images/social-template-factory/`

**Description:** Creates repeatable branded designs for common team communications.

**Responsibilities:**

* Build game-day graphics.
* Build final-score and player-announcement templates.
* Build ticket-promotion and community-event layouts.
* Prepare reusable dimensions and editable design elements.

**Outputs:** Branded template files and usage instructions.

**Acceptance criteria:** Templates follow official brand requirements and target platform dimensions.

---

# Category 3 — Canva and Higgsfield

## 09. Canva Export & Handoff

**Suggested folder:** `skills/integrations/canva-handoff/`

**Description:** Offers users a Canva editing workflow after generating an image.

**User choices:**

1. Finished PNG — flattened graphic for Canva upload.
2. Editable Canva-importable PPTX — separate editable elements where technically feasible.
3. Reusable team template — approved layout starter for shared Canva use.

**Responsibilities:**

* Present the three options after image generation.
* Prepare the selected format.
* Verify brand compliance before handoff.
* Check authenticated connection status when supported.
* Provide manual import instructions if direct transfer is unavailable.

**Outputs:** Import-ready file, instructions, and connection-status message.

**Acceptance criteria:** No unverified direct Canva connection or guaranteed layer editability is claimed.

## 10. Canva Brand Kit Setup

**Suggested folder:** `skills/integrations/canva-brand-kit/`

**Description:** Guides configuration of the Empire Strykers brand identity inside Canva.

**Responsibilities:**

* Organize approved logos and brand assets.
* Configure official colors and licensed fonts where supported.
* Prepare reusable layouts.
* Define team editing and sharing guidance.
* Review imported designs for brand consistency.

**Outputs:** Canva setup checklist and brand asset inventory.

**Acceptance criteria:** Setup status is confirmed by evidence rather than assumption.

## 11. Higgsfield Video Handoff

**Suggested folder:** `skills/integrations/higgsfield-handoff/`

**Description:** Helps users continue image-based creative work in Higgsfield for video and motion effects.

**User choices:**

1. Animate a generated image.
2. Apply cinematic motion or effects.
3. Use an image as a video concept reference.

**Responsibilities:**

* Prepare compatible source imagery.
* Create motion prompts and production instructions.
* Preserve approved logo and player details.
* Verify available connection options.
* Review returned videos for brand and continuity issues.

**Outputs:** Source image, motion brief, upload instructions, and review checklist.

**Acceptance criteria:** No external transfer is reported as completed without a verified operation.

## 12. Integration & Account Checker

**Suggested folder:** `skills/integrations/account-checker/`

**Description:** Checks the availability and authorization status of supported creative integrations.

**Responsibilities:**

* Identify available connected tools.
* Distinguish connected, disconnected, and unverified accounts.
* Check supported permissions.
* Explain manual alternatives.
* Avoid exposing tokens or account secrets.

**Outputs:** Integration status report.

**Acceptance criteria:** Connection claims are supported by authenticated tool results.

---

# Category 4 — Video Production and Motion

## 13. Video Storyboard Director

**Suggested folder:** `skills/video/storyboard-director/`

**Description:** Develops branded storyboards for game promotions, player features, ticket campaigns, and social video.

**Responsibilities:**

* Build scene sequences.
* Define shot framing and timing.
* Suggest transitions and motion.
* Incorporate approved campaign messaging.
* Identify footage and assets required.

**Outputs:** Storyboard and shot list.

**Acceptance criteria:** The storyboard is executable with available or clearly identified required assets.

## 14. Motion Graphics & Captions

**Suggested folder:** `skills/video/motion-captions/`

**Description:** Produces specifications for branded video graphics and bilingual subtitles.

**Responsibilities:**

* Create title and lower-third treatments.
* Design score and match-information graphics.
* Prepare English and Spanish caption text.
* Check caption timing, legibility, and placement.

**Outputs:** Motion graphics specification and caption assets.

**Acceptance criteria:** Captions and graphic details match verified content.

## 15. Video Brand & Continuity Inspector

**Suggested folder:** `skills/video/video-continuity-qa/`

**Description:** Reviews video output for brand consistency, player fidelity, and temporal artifacts.

**Responsibilities:**

* Inspect logo consistency between frames.
* Detect obvious subject or uniform changes.
* Review visual continuity and motion artifacts.
* Validate caption and sponsor accuracy.
* Report required fixes.

**Outputs:** Video quality and brand-compliance report.

**Acceptance criteria:** Frame-level or temporal checks are not claimed unless performed.

## 16. Video Export Validator

**Suggested folder:** `skills/video/export-validator/`

**Description:** Validates finished video files before release.

**Responsibilities:**

* Check file format, dimensions, duration, and frame rate.
* Verify audio and caption requirements.
* Inspect encoding and playback integrity.
* Confirm required approval status.
* Block release when mandatory checks fail.

**Outputs:** Technical validation report and export status.

**Acceptance criteria:** An MP4 is not declared complete without an actual file and successful verification.

---

# Category 5 — Marketing and Content Production

## 17. Campaign Style Selector

**Suggested folder:** `skills/marketing/campaign-style-selector/`

**Description:** Helps select campaign directions from approved creative references while maintaining the official brand identity.

**Responsibilities:**

* Evaluate the content objective.
* Recommend relevant campaign concepts.
* Use PostPick styles as secondary creative inspiration.
* Keep official Brand Kit rules authoritative.

**Outputs:** Campaign style recommendation and visual brief.

**Acceptance criteria:** Inspiration never overrides official brand requirements.

## 18. Game & Player Fact Checker

**Suggested folder:** `skills/marketing/fact-checker/`

**Description:** Verifies team-related information used in graphics and promotional copy.

**Responsibilities:**

* Check opponents, match dates, venues, and scores.
* Verify player names and available roster details.
* Identify missing or conflicting information.
* Require source confirmation for time-sensitive claims.

**Outputs:** Fact-check report and approved content fields.

**Acceptance criteria:** Unverified facts are clearly labeled and not silently invented.

## 19. Bilingual Caption Writer

**Suggested folder:** `skills/marketing/bilingual-captions/`

**Description:** Creates English and Spanish social copy aligned with the Strykers brand voice.

**Responsibilities:**

* Draft engaging promotional captions.
* Preserve meaning across languages.
* Use correct arena soccer terminology.
* Select appropriate hashtags from official guidance.
* Check names, dates, and calls to action.

**Outputs:** English and Spanish caption drafts.

**Acceptance criteria:** Copy is linguistically reviewed and factually consistent.

## 20. Sponsor & Partnership Manager

**Suggested folder:** `skills/marketing/sponsor-manager/`

**Description:** Coordinates sponsor requirements and approved co-branded creative.

**Responsibilities:**

* Maintain sponsor asset references.
* Verify names and logo usage.
* Apply approved co-brand arrangements.
* Identify contractual or campaign-specific requirements for review.

**Outputs:** Co-brand creative brief and sponsor QA checklist.

**Acceptance criteria:** Sponsor identity and placement comply with available approvals and agreements.

---

# Category 6 — Team Operations and Publishing

## 21. Creative Approval Manager

**Suggested folder:** `skills/operations/approval-manager/`

**Description:** Manages creative review, revision requests, and authorized release decisions.

**Responsibilities:**

* Track draft and review status.
* Record requested changes.
* Require independent approval when applicable.
* Maintain approval evidence.
* Prevent unauthorized final export.

**Outputs:** Approval record and release decision.

**Acceptance criteria:** A creator cannot satisfy an independent approval requirement by self-approving.

## 22. Asset Library & Rights Manager

**Suggested folder:** `skills/operations/asset-library/`

**Description:** Organizes approved creative assets and their permitted uses.

**Responsibilities:**

* Index logos, player photos, video clips, and templates.
* Track asset provenance and version.
* Record rights or usage restrictions.
* Identify missing permissions.
* Avoid publishing restricted assets to public repositories.

**Outputs:** Asset manifest and rights-status report.

**Acceptance criteria:** Asset usage is traceable to an approved source and applicable permissions.

## 23. Platform Format Optimizer

**Suggested folder:** `skills/operations/platform-optimizer/`

**Description:** Prepares graphics and videos for target publishing platforms.

**Responsibilities:**

* Apply current output dimensions.
* Check aspect ratios and safe zones.
* Validate text readability.
* Prepare platform-specific variants.
* Review export quality.

**Outputs:** Platform-ready variants and formatting report.

**Acceptance criteria:** Deliverables meet verified target-platform requirements.

## 24. Content Calendar & Performance

**Suggested folder:** `skills/operations/content-calendar/`

**Description:** Helps plan, coordinate, and evaluate Strykers content campaigns.

**Responsibilities:**

* Build content calendars.
* Track creative production stages.
* Organize campaign themes and deadlines.
* Review available engagement data.
* Recommend improvements grounded in performance evidence.

**Outputs:** Editorial calendar, status tracker, and performance recommendations.

**Acceptance criteria:** Performance claims are supported by actual data.

---

# Recommended GitHub Structure

```text
strykers-creative-studio/
├── README.md
├── skills/
│   ├── brand/
│   │   ├── brand-guardian/
│   │   ├── logo-validator/
│   │   ├── typography-manager/
│   │   └── brand-qa/
│   ├── images/
│   │   ├── creative-brief-builder/
│   │   ├── background-removal/
│   │   ├── player-image-integrity/
│   │   └── social-template-factory/
│   ├── integrations/
│   │   ├── canva-handoff/
│   │   ├── canva-brand-kit/
│   │   ├── higgsfield-handoff/
│   │   └── account-checker/
│   ├── video/
│   │   ├── storyboard-director/
│   │   ├── motion-captions/
│   │   ├── video-continuity-qa/
│   │   └── export-validator/
│   ├── marketing/
│   │   ├── campaign-style-selector/
│   │   ├── fact-checker/
│   │   ├── bilingual-captions/
│   │   └── sponsor-manager/
│   └── operations/
│       ├── approval-manager/
│       ├── asset-library/
│       ├── platform-optimizer/
│       └── content-calendar/
├── references/
│   ├── brand-guidelines/
│   ├── campaign-styles/
│   └── platform-specifications/
├── templates/
├── scripts/
└── tests/
```

Each individual skill folder should contain a `SKILL.md` with activation conditions, required inputs, workflow steps, outputs, failure handling, and verification criteria. Add scripts and tests where executable operations are necessary.

# Implementation Roadmap

## Phase 1 — Core Creative Workflow

Prioritize:

1. Brand Guardian
2. Brand QA Inspector
3. Creative Brief Builder
4. Background Removal Studio
5. Social Template Factory
6. Canva Export & Handoff
7. Higgsfield Video Handoff

**Goal:** Generate a branded image, verify it, and prepare it for editing in Canva or Higgsfield.

## Phase 2 — Production and Publishing

Add video storyboarding, motion graphics, captions, continuity checks, export validation, fact checking, and platform formatting.

**Goal:** Support reliable branded multimedia production.

## Phase 3 — Team Collaboration

Add asset rights management, account verification, approvals, sponsorship management, content planning, and performance analysis.

**Goal:** Enable a coordinated, auditable production workflow for Seth's team.

# Security and Operational Notes

* Do not commit API keys, OAuth secrets, or private credentials to GitHub.
* Keep licensed fonts, restricted team imagery, and confidential sponsor materials in approved private storage.
* Verify account connections through authenticated tools.
* Treat generated artwork as a draft until required brand checks are complete.
* Do not claim a file was exported, uploaded, or published without evidence.
* Require independent approval before final MP4 release when the workflow calls for it.
* Separate skill instructions from actual service integrations and implementation code.
* Use the official Empire Strykers Brand Kit as the authoritative reference whenever creative examples conflict with brand rules.

# Definition of Success

The system should allow a team member to:

1. Request an Empire Strykers graphic or video.
2. Receive a design aligned with the official brand.
3. Review the result and identify needed corrections.
4. Choose Canva, Higgsfield, or no further editing.
5. Prepare an appropriate handoff file or use a verified connected integration.
6. Recheck the edited result for brand and factual accuracy.
7. Route final material through the required approval process.
8. Export or publish only after the necessary validations succeed.

**End of 24-Skill Library Specification**
