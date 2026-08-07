---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__012_sota-echoing.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:11 — SoTA-Echoing"
line_start: 100017
line_end: 100032
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:11 - SoTA-Echoing

Source qualification was checked on 2026-07-30. The source identities below are immutable publications; the G.4 adoption decisions remain qualified through 2027-07-30 unless a governing neighbour adopts a successor earlier or a new result contradicts the named assumption boundary.

| Exact source and source-use decision | Visible G.4 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| Angelopoulos, Bates, Fisch, Lei, and Schuster, [*Conformal Risk Control*, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) — **adapt** bounded monotone-loss risk control only for a CAL clause whose statistical assumptions are explicit. | C3 and `CC-G4-04` require loss, risk/coverage target, calibration population/window, exchangeability or declared shift treatment, and failure/abstain behavior before such a clause is published. The ordinary §4.4a chain still owns any performed application and verdict. | “Conformal”, a calibration set, or a coverage target does not make a universal acceptance guarantee, authorize deployment, or establish that evaluation occurred. | Reopen only C3, `CC-G4-04`, and the one worked clause/test that claims this guarantee when its assumptions or guarantee change. |
| Fontaine, Togelius, Nikolaidis, and Hoover, [*Covariance Matrix Adaptation for the Rapid Illumination of Behavior Space*, GECCO 2020](https://doi.org/10.1145/3377930.3390232) — **adapt** only the need to pin descriptor, distance, insertion, archive, and reporting policy when `G.4:Ext.NQD` is actually used. | C6, `G.4:Ext.NQD`, and `CC-G4-13` keep QD method semantics in C.18 while making the CAL wiring reproducible. | Archive occupancy, coverage, QD-score, or the presence of CMA-ME wiring is not dominance, acceptance, selection, or a runtime result. | Reopen only C6, `G.4:Ext.NQD`, `CC-G4-13`, and its one NQD example/test if the adopted descriptor/archive contract changes. |
| Wang et al., [*Enhanced POET: Open-ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions*, ICML/PMLR 119 (2020)](https://proceedings.mlr.press/v119/wang20l.html) — **reject as a source of G.4 core or acceptance semantics**; retain it only as an exact lineage reference for optional exploration wiring owned elsewhere. | C6 and `CC-G4-11` require an exact current governor and present-task entry/stop condition before any exploration extension is admitted; no POET-specific rule enters the CAL core. | Open-ended generation, transfer, or progress telemetry does not become a CAL acceptance rule, task authority, or selected governor by citation. | Reopen only C6, `CC-G4-11`, and the exact C.19/C.23 extension block if its governing pattern explicitly adopts a changed POET-family contract. |

Distributionally robust and broad multi-objective families are discovery leads, not G.4 decision sources. Current comparison, partial-order, and selected-set law stays with A.18/A.19; a future external source enters this table only after it changes a present C1–C9 action, worked case, or conformance row. Source refresh is local to the row's named rule, example, and check.

#### G.4:11.1 - Owner-facing architecture and publication inventory

G.4 is a design-time authoring pattern. It publishes a notation-independent `CAL Pack@CG-Frame` with charter, stable operator/clause/flow ids, evidence/currentness refs, proof-or-gap records, worked examples/tests, continuity notes, and a minimal `TaskMap`. It uses G.Core/G.0/G.1–G.3 for Part-G, Context, SoTA, CHR, and legality disciplines; A.6.1/A.15.1/C.2.1 for the declaration/runtime/result-episteme split; and A.10/G.11/B.3/C.11 for provenance, currentness, assurance, and decisions. G.6 is used only when `G.4:Ext.EvidenceGraphWiring` is present. Method-specific semantics remain with the exact extension governor. The detailed manifests, schemas, and interfaces above are owner-facing citation surfaces for this one practitioner path, not a second workflow.

