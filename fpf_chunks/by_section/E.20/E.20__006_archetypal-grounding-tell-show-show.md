---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__006_archetypal-grounding-tell-show-show.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 85783
line_end: 85795
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:5 - Archetypal Grounding *(Tell–Show–Show)*

**Show 0 (suite member, no new mechanism meaning).** A suite adds an already-introduced `U.Mechanism` episteme by its `MechanismDefinitionRef` and changes no identity component, declaration content, or neighboring relation on which the suite use relies. E.20 records the suite-governing locus and stops; no new mechanism declaration target or MIP-run manifest is opened.

|  | Tell | Show #1 — add a mechanism to an existing suite *variant* | Show #2 — introduce a new mechanism family + suite |
|---|---|---|---|
| **Scene** | Mechanisms evolve: new stages appear, methods mature, and planning records need to remain citeable. | A team wants an additional “stage” in a characterization pipeline, but does not want to mutate the kernel suite. | A new domain needs a mechanism family or species not yet present in any existing mechanism-profile cluster (for characterization: `A.19.*`), plus a suite that composes several distinct mechanisms with a P2W hook. |
| **Definition-locus assignment** | Each change item has one definition locus; make the change there rather than smearing it across several patterns. | 1) Add the introduced `U.Mechanism` episteme under the mechanism-subject pattern. 2) Add a suite variant under the suite-subject pattern. 3) Pin the variant in rows kept inside one WorkPlan. 4) Wire the variant through a `GPatternExtension`. | 1) Add the new operation-family declaration and archetypal grounding under the subject pattern. 2) Add `A.6.7.<FamilyKey>` describing the suite. 3) Add suite-specific planned values as rows inside one WorkPlan. 4) Add SoTA packs and wiring modules. |
| **Resolvable target first** | No suite treats a dangling designator or reservation stub as an introduced mechanism. | Create the reservation stub or introduced mechanism target first; add only an introduced mechanism to admitted suite membership. | Create each mechanism target first; then publish suite membership by designator. |
| **Suite discipline** | Suites are descriptive: membership, obligations, pins, protocols; not mechanisms and not gates. | The variant’s `suite_protocols` explicitly names the new stage; publish/telemetry remains outside the suite. | The new suite defines shared obligations and allowed pipelines without embedding mechanism semantics. |
| **P2W planning-to-work boundary** | One exact WorkPlan is the planning record; its declaration-local rows pin references and planned values, while enactment witnesses actual runs. | The exact WorkPlan's local rows pin the chosen suite variant and any method or specification references; no row carries launch values or decision logs. | Declaration-local rows in the exact WorkPlan state the planned fillers and pins that downstream flows cite through that WorkPlan edition. |
| **SoTA updates** | Methods change faster than kernel meaning; wiring is where choices are governed. | A `GPatternExtension` selects a post-2015 scoring method by edition‑pinned ref; no kernel mutation required. | The family ships method packs and wiring modules; the identity-bearing content of each introduced `U.Mechanism` remains at its mechanism-subject pattern. |

