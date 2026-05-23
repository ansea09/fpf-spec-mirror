---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:5"
section_title: "Archetypal Grounding (Tell–Show–Show)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__006_archetypal-grounding-tell-show-show.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:5 — Archetypal Grounding (Tell–Show–Show)"
line_start: 61115
line_end: 61129
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

**Show 0 (suite member, no new mechanism meaning).** A suite adds an already-defined `U.Mechanism.IntensionRef` as an optional member and changes no operation, law set, admissibility condition, slot interface, transport boundary, audit semantics, planned-baseline pins, or wiring semantics. E.20 records the suite-governing locus and stops; no new mechanism-governing card and no MIP-run manifest are opened.

|  | Tell | Show #1 — add a mechanism to an existing suite *variant* | Show #2 — introduce a new mechanism family + suite |
|---|---|---|---|
| **Scene** | Mechanisms evolve: new stages appear, methods mature, and planning records need to remain citeable. | A team wants an additional “stage” in a characterization pipeline, but does not want to mutate the kernel suite. | A new domain needs a mechanism family or species not yet present in any existing mechanism-profile cluster (for characterization: `A.19.*`), plus a suite that composes several distinct mechanisms with a P2W hook. |

| **Governing-definition assignment** | Each change item has one governing definition; changes are assigned there, not smeared. | 1) Add the new mechanism card under the mechanism-governing pattern. 2) Add a suite variant under the suite-governing pattern. 3) Pin the variant via a planned-baseline specialization. 4) Wire the variant via a `GPatternExtension`. | 1) Add a new archetypal grounding under the governing pattern. 2) Add `A.6.7.<FamilyKey>` describing the suite. 3) Add a suite-specific `SlotFillingsPlanItem` specialization. 4) Add SoTA packs and wiring modules. |
| **Card-first** | No suite enumerates a missing `…IntensionRef`. | Create the new `…IntensionRef` card stub first; then update the suite variant membership. | Create the new mechanism-governing card(s) first; then publish suite membership by `…IntensionRef`.
 |
| **Suite discipline** | Suites are descriptive: membership, obligations, pins, protocols; not mechanisms and not gates. | The variant’s `suite_protocols` explicitly names the new stage; publish/telemetry remains outside the suite. | The new suite defines shared obligations and allowed pipelines without embedding mechanism semantics. |
| **P2W seam** | Planning pins refs; enactment witnesses runs. | The plan item pins the chosen suite variant and any method/spec refs; no launch values or decision logs. | The plan item specialization defines the planned fillers/pins that downstream flows cite. |
| **SoTA updates** | Methods change faster than kernel meaning; wiring is where choices live. | A `GPatternExtension` selects a post-2015 scoring method by edition‑pinned ref; no kernel mutation required. | The family ships method packs and wiring modules; kernel cards remain the semantic source of mechanism meaning. |

