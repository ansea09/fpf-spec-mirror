---
chunk_kind: "child"
pattern_id: "G.2"
pattern_title: "Harvest and Synthesize SoTA for a CG-Frame"
section_id: "G.2:5"
section_title: "Archetypal Grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/G.2/G.2__006_archetypal-grounding-system-episteme.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "G.2 — Harvest and Synthesize SoTA for a CG-Frame"
  - "G.2:5 — Archetypal Grounding (System / Episteme)"
line_start: 111924
line_end: 111950
dependencies:
  - "A.10"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.19"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.13"
  - "G.3-G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "BridgeMatrix"
  - "DeclaredSubstrateAtlasView"
  - "FlowRecord"
  - "GammaEpistSynthId"
  - "SoTA Synthesis Pack@CG-Frame"
  - "SoTA harvest"
  - "SoTAPaletteDescription"
  - "Tradition"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "palette-first"
  - "state of the art"
  - "synthesis"
---

### G.2:5 - Archetypal Grounding (System / Episteme)

| Template element   | `U.System` illustration                                                                                                                                                                                                                                                  | `U.Episteme` illustration                                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tell** | A safety engineering team needs to choose a control stack across robust-control, learning-based, and formal-verification lineages. It identifies the exact CG-frame (the declared framing episteme), vehicle and operating-envelope EntityOfConcern, source editions, claim regions, test or comparison basis, evidence anchors, and intended decision use. | A research group synthesizes SoTA on decision quality across named causal, evidential, bounded-rationality, and active-inference lineages, keeping each source edition, local claim, evidence norm, comparison basis, and intended research use explicit. |
| **Show (failure)** | The team merges source-local terms, treats incompatible test protocols and populations as comparable, and collapses partially ordered trade-offs into one unqualified score. A later safety review cannot recover which source, claim region, basis, or evidence supported the choice. | The group publishes one “best” metric and retrofits definitions to it. Conflicting claims cannot be traced because source editions, evidence anchors, comparison bases, and any actual cross-source relation were never made explicit. |
| **Show (repair)** | Keep parallel Claim Sheets with exact sources, editions, claim regions, EntitiesOfConcern, comparison bases, and evidence. Cite an F.9 Bridge and loss only for an actual relation. Authors of CHR, CAL, and selection methods can then use the citable claims without attributing authority to a card. | Preserve plural claims, represent indicators as families or variants, and expose freshness and evidence. Any justified alignment names its exact cells and obtaining relation; the card or matrix merely represents that result. |

#### G.2:5.1 - Count one pack under a declared basis

Consider this illustrative control-stack pack, extending the System case above. These are stipulated source entries for a counting example, not a finding that a real corpus has adequate breadth.

| Entry and distinct claim region | Lineage | Declared family unit |
| --- | --- | --- |
| e1: robust controller's operating-envelope claim | robust control | method M-R |
| e2: that family's distinct disturbance-rejection claim | robust control | method M-R |
| e3: learned controller's adaptation claim | learning-based control | method M-L |
| e4: scenario generator's counterexample-generation claim | formal verification | generator G-S |

For the question “which control-method families can be selected?”, policy P-method counts method families only and equates entries exactly when they name the same declared method-family unit. The classes are {e1,e2} and {e3}: count 2, below k=3. Additional cards for e1 or citations for M-R leave the count at 2.

For the different question “which method and scenario-generator families can support building and evaluating this control stack?”, policy P-combined includes the three declared units M-R, M-L and G-S. Its overlap rule merges repeated references to one unit; these three units are stipulated distinct and G-S is not also M-R or M-L. Count 3 meets k=3 for that receiving purpose. This is not a passing method-only judgement and cannot be substituted after P-method fails. If one generator also qualified as a counted method, the overlap rule would have to resolve it before the count.

Four claim regions remain four material entries. The example independently has three lineages, so its two-lineage and three-material-entry pluralism duties pass under the stated facts in both policies. With no counted-family basis, family coverage is unassessable even though that pluralism result remains available. A justified k=2 override for P-method changes its threshold result while leaving its count at 2 and those independent duties unchanged.

G.1 M2 and the G.3–G.5 consumers cite the chosen pack judgement with its purpose and policy; they do not reconstruct a more convenient count from the cards.

