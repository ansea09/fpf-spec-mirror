---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:intro — Intro"
line_start: 54351
line_end: 54358
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

## E.16 - RoC‑Autonomy Budget & Enforcement

**Intent.** Make any claim of autonomous behavior testable and enforceable via a published **AutonomyBudgetDecl**, **Guarded enactment**, **Override SpeechActs with SoD**, and a **Work‑anchored AutonomyLedger**.
**Rule (summary).** If a Role/Method/Service claims autonomy, authors **MUST**: (i) publish an `AutonomyBudgetDecl` with `AdmissibilityConditionsId` and `OverrideProtocolRef`; (ii) gate Method steps with `requiresAutonomyBudget`; (iii) write a `AutonomyLedgerEntry` on every admitted Work; (iv) block on depletion until a `ResumeAutonomy` SpeechAct passes SoD; (v) surface autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.15 / A.21; B.3; C.16; E.8; E.10; E.18; F.4; F.6; F.8; F.15; F.17.
**Coordinates with:** A.13 (Agential Role), C.9 (Agency‑CHR), C.24 (Agent‑Tools‑CAL) where applicable; G.4–G.5–G.8–G.9–G.10 (method authoring/selection/shipping).

