---
chunk_kind: "child"
pattern_id: "A.6.7"
pattern_title: "MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
section_id: "A.6.7:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.7/A.6.7__012_sota-echoing.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.6.7 — MechSuiteDescription — Shared Conditions for Joint Use of Distinct Mechanisms"
  - "A.6.7:11 — SoTA-Echoing"
line_start: 21900
line_end: 21909
dependencies:
  - "A.21"
  - "A.6.1"
  - "A.6.5"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "G.10"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "CG-Spec"
  - "CN-Spec"
  - "P2W"
  - "crossing visibility"
  - "distinct mechanisms"
  - "mechanism suite"
  - "planned baseline"
  - "spec pins"
  - "suite obligations"
---

### A.6.7:11 - SoTA-Echoing

**Question and selected answer.** How can a practitioner reuse several operation contracts under one set of conditions without selecting an implementation prematurely? For this question, **adapt** the explicit process-reference, input/output and requirement separation in [CWL Workflow v1.2.1, §3.3 and §4.3](https://www.commonwl.org/v1.2/Workflow.html#WorkflowStep). Its [abstract Operation](https://www.commonwl.org/v1.2/Workflow.html#Operation) describes inputs and outputs before binding a concrete process. This is the best-known-line candidate for declaration-first composition here; it does not establish FPF admissibility or operation identity.

**Serious alternative.** A pinned executable pipeline is preferable when the task is already to fit and run compatible estimators. [scikit-learn 1.9.1 Pipeline, `steps`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) exposes named estimator steps; each has fit, and intermediate steps have transform. It is a substantive composition alternative, not evidence that every characterization contract should have that interface.

For OfferChoice, compare both approaches with the same two contracts, four operation uses and four specification references. **Adopt** explicit member/operation resolution and one common specification baseline; **reject** the shortcut of identifying these contracts only by stage names or selected realizers. An executable pipeline could carry the same facts through adapters and metadata, but those additions still need their declarations and checks. The suite keeps them inspectable before an implementation exists. The deliberate cost is another reference layer; it offers no execution or performance advantage. Once executable estimators and their composition fully answer the question, use that pipeline and do not add a suite merely for documentation.

This choice is expressed in §4.1's exact declaration/edition resolution, §4.4's separate protocol and the filled §4.6 case: a returned comparison binding supplies selection, and absent evidence stops the chain. The architectural comparison is a local inference from the stated use and these primary specifications, not a measured productivity result or a claim that either source defines FPF. Reopen it if a receiving use needs only one already complete executable pipeline, if an additional reference layer hides a required condition, or if a rival represents the same distinct contracts and joint conditions with less total reader work.

