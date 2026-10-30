---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__012_sota-echoing.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:11 — SoTA-Echoing"
line_start: 128494
line_end: 128509
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
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
  - "F.6"
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
  - "U.ClaimScope"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:11 - SoTA-Echoing

These sources contribute to particular CAL clauses or extensions under the stated conditions. Reconsider the affected use when its source assumptions or adopted contract change.

| Source and adopted contribution | Use in CAL | Applicability limit | Return when |
| --- | --- | --- | --- |
| Angelopoulos, Bates, Fisch, Lei, and Schuster, [*Conformal Risk Control*, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) — **adapt** bounded monotone-loss risk control only for a CAL clause whose statistical assumptions are explicit. | C3 and `CC-G4-04` require loss, risk/coverage target, calibration population/window, exchangeability or declared shift treatment, and failure/abstain behavior before such a clause is published. Only an actual application under §4.4a supplies the required binding and verdict. | “Conformal”, a calibration set, or a coverage target does not make a universal acceptance guarantee, authorize deployment, or establish that evaluation occurred. | Reopen only C3, `CC-G4-04`, and the one worked clause/test that claims this guarantee when its assumptions or guarantee change. |
| Fontaine, Togelius, Nikolaidis, and Hoover, [*Covariance Matrix Adaptation for the Rapid Illumination of Behavior Space*, GECCO 2020](https://doi.org/10.1145/3377930.3390232) — **adapt** only the need to pin descriptor, distance, insertion, archive, and reporting policy when `G.4:Ext.NQD` is actually used. | C6, `G.4:Ext.NQD`, and `CC-G4-13` keep QD method semantics in C.18 while making the CAL wiring reproducible. | Archive occupancy, coverage, QD-score, or the presence of CMA-ME wiring is not dominance, acceptance, selection, or a runtime result. | Reopen only C6, `G.4:Ext.NQD`, `CC-G4-13`, and its one NQD example/test if the adopted descriptor/archive contract changes. |
| Wang et al., [*Enhanced POET: Open-ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions*, ICML/PMLR 119 (2020)](https://proceedings.mlr.press/v119/wang20l.html) — **reject as a source of G.4 core or acceptance semantics**; retain it only as an exact lineage reference for optional exploration wiring under the applicable pattern. | C6 and `CC-G4-11` require an exact current pattern and present-task entry and stop condition before any exploration extension is admitted; no POET-specific rule enters the CAL core. | Open-ended generation, transfer, or progress telemetry does not become a CAL acceptance rule, task authority, or selected governor by citation. | Reopen only C6, `CC-G4-11`, and the exact C.19/C.23 extension block if the applicable pattern explicitly adopts a changed POET-family rule set. |

Use A.18/A.19 for comparison, partial-order and selected-set rules. Distributionally robust and broader multi-objective methods are further candidates to investigate when the receiving question needs them. Revisit only the clauses, extensions and applications that depend on a changed source claim.

#### G.4:11.1 - CAL architecture and publication inventory

The charter fixes the pack's scope and assumptions. Typed operators and clauses define admissible applications; flows compose them; evidence profiles and the ProofLedger expose their required grounds. The `TaskMap` connects these declarations to selection. Later applications bind actual inputs and produce results under §4.4a. Extensions add only the method-specific declarations needed by that use.

