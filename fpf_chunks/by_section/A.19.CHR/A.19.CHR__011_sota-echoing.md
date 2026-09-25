---
chunk_kind: "child"
pattern_id: "A.19.CHR"
pattern_title: "CHRMechanismSuite: Shared Rules for Characterization and Selection"
section_id: "A.19.CHR:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.CHR/A.19.CHR__011_sota-echoing.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.19.CHR — CHRMechanismSuite: Shared Rules for Characterization and Selection"
  - "A.19.CHR:11 — SoTA-Echoing"
line_start: 34610
line_end: 34623
dependencies:
  - "A.15.2"
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "A.6.7"
  - "A.6.RCD"
  - "C.23"
  - "E.10"
  - "E.18"
  - "E.19"
  - "G.0"
  - "G.10"
  - "G.5"
keywords:
  - "Bridge-only transport"
  - "CG-Spec"
  - "CHR suite"
  - "CN-Spec"
  - "P2W seam"
  - "SlotFillingsPlanItem"
  - "admissibility gate"
  - "characterization core"
  - "crossing visibility"
  - "no hidden scalarization"
  - "no hidden thresholds"
  - "penalties→R_eff"
  - "planned baseline"
  - "set-return selection"
  - "suite obligations"
  - "tri-state guard decision"
---

### A.19.CHR:11 - SoTA-Echoing

**Working question.** How should a team connect normalization, indicator choice, scoring, comparison and selection so that the final result still follows from the selected scales, evidence and method conditions when one of them changes?

For this question, **adapt** declaration-first workflow composition, the selected line compared in A.6.7 §11. [CWL v1.2.1's process references, requirements and abstract operations](https://www.commonwl.org/v1.2/Workflow.html#Operation) supply the substantive external model for distinguishing a described operation from a concrete process. The CHR adaptation makes the shared CN/CG conditions and each operation's result bindings explicit. CWL supplies neither these FPF laws nor the justification of the offer comparison.

The serious alternative is one pinned executable estimator pipeline, exemplified by [scikit-learn 1.9.1 Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html). It is attractive when fitting and sequential transformation already express the whole task. For the same five used CHR stages, compare it with the suite while holding the methods, data, policy and evidence requirements fixed. Both can calculate the two offers correctly. A pipeline plus explicit checks can also reject expired normalization. Its executable composition alone, however, does not state the case's scale-preservation argument or resolve the separately governed selection policy; those facts still need an inspectable account.

**Adopt** explicit method/specification resolution and **reject** a stage-name-only chain as sufficient justification. The suite accepts the extra reference cost to expose these conditions before choosing implementations. This is a trade-off in explanation and reuse, not a claimed runtime benefit or measured authoring saving. If a single existing pipeline already exposes every condition needed by the receiving use, reuse its account; creating another suite copy adds no gain.

The concrete effect is in §§4.0, 4.5 and 4.8.1: choose each contract before using a stage, retain every transformation's basis through the actual comparison, and stop the normalization-based path when its selected validity window fails. The final {A,B} remains a set even though the five stages could be packaged behind one callable interface. That packaging cannot add a singleton preference or purchase approval.

The two primary specifications are source models and a serious comparator; the choice for CHR is an explicit local architectural inference. They establish no empirical superiority of this pattern. Reopen the comparison if the receiving task becomes one fully self-contained executable pipeline, if its account already makes the same conditions cheaper to recover, or if a changed member contract makes the common baseline insufficient.

