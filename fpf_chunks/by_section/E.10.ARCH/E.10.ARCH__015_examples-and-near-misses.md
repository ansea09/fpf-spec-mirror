---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:9"
section_title: "Examples and near misses"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__015_examples-and-near-misses.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:9 — Examples and near misses"
line_start: 64140
line_end: 64157
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.F"
  - "A.6.P"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

### E.10.ARCH:9 - Examples and near misses

| Wording | Applicable result | Blocked overread |
| --- | --- | --- |
| "The architecture is the diagram." | `C.30.P` recovers whether the diagram is publication form, structure view, architecture description, source relation, or ordinary source cue; then `C.30` or `C.30.ASV` applies only after the selected architecture or structural-view use is recovered. | diagram-as-architecture; diagram-as-proof; diagram-as-gate. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless selected structure, architecture-description use, structural-view use, source use, model use, diagram use, graph use, dashboard use, or ordinary prose remains hidden. | unnecessary restoration detour. |
| "The model has three layers." | `C.30.STRAT` treats `layers` as a source label until the recovered FPF kind, relation, claim-use, or source-use disposition is recovered: control-layer relation, neural-network block sequence, publication relation set, mathematical scale or coarse-graining relation, or ordinary source wording. Then the governing pattern applies to the recovered result. | layer-as-universal-kind; source label as proof of structure. |
| "The query plan calls the next pattern." | `C.2.P.DR` recovers whether the query plan is a representation, method description, formal substrate, evidence or provenance relation, or ordinary source wording; if a pattern relation is current, the relation is stated declaratively rather than as a call. | query-as-work sequence; pattern relation as invocation. |
| "The evidence path authorizes release." | If a provenance relation for a claim is current, use `A.10`; if authorization or release is current, use the authority, gate, or release pattern. `C.2.P.DR` applies only when `path` wording turns the relation into an action route or permission. | evidence path as permission; graph relation as release. |
| "The solver algorithm is the mechanism." | `A.3.1` first recovers whether the current slot is method, method description, formal substrate, mathematical-lens use, mechanism declaration or realization, work, evidence, or quote-only wording. Use `A.6.1` and `E.20` only when operation algebra, laws, admissibility predicates, transport, audit, or governing-definition assignment is current. | algorithm-as-default-method; method-as-mechanism by vocabulary. |
| "This record is admissible." | Recover bearer, claim kind, source relation, value frame, admissible use, and governing pattern. Use `A.19.SPR` only if hidden state-family wording remains; otherwise use the direct evidence, gate, mechanism, temporal, authority, release, or source-use pattern. | admissible-as-generic status; pass-looking word as gate. |
| "This score proves readiness." | `C.16.P` recovers characteristic, scale, value, score, threshold, comparison reference set, and gate, evidence, and decision pattern applications. | score-as-proof; score-as-release permission. |
| "This source supports the claim." | `C.2.P` is used if source-currentness relation or publication relation set is current; relation slice applies `A.6.P`; final use states recovered relation or non-use disposition. | source-as-proof; support-as-generic relation. |
| "Quality improved." | `C.16.Q` recovers quality characterization or evaluative characterization, or names the `C.16.P`, `C.25`, `E.21`, `A.6.P`, action, work, or bridge pattern application governing the recovered claim. | quality-as-one scalar; quality-as-gate. |
| "The function improved maintainability." | `A.6.F` first recovers the FPF kind named by value, relation, or claim when hidden; quality or maintainability wording is then governed by `C.16.P`, `C.16.Q`, `C.25`, or the quality pattern governing the current claim. | function-as-default-architecture; maintainability-as-unscaled verdict. |
| "Read this pattern for improvement proposals." | Recover whether the current FPF-governed use is source-publication use, bounded comparative review unit, or improvement-oriented evaluation. Use `E.22` only for improvement-oriented quality review under a declared pattern-under-improvement evaluation. | generic reading as a pattern. |
| "This summary is enough for action." | `E.10` checks whether the wording is precision restoration or controlled precision reduction. If coarsened source-to-rendering use is current, `A.6.3.CSC` names source-bearing side, loss mode, narrower admissible use, non-admissible downstream use, and reopen condition. | summary-as-full source; coarsening without declared loss. |

