---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:9"
section_title: "Examples and near misses"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__015_examples-and-near-misses.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:9 — Examples and near misses"
line_start: 77102
line_end: 77124
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
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
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.16"
  - "C.2.1"
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
  - "E.10.MOVE"
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
| `MaintenanceReport_42` says “Bearing_B is installed in Pump_P.” | The exact mereology predicate is already clear, so bypass E.10.ARCH. State `Bearing_B isPartOf Pump_P`; keep `MaintenanceReport_42` as the claim-bearing episteme that asserts that exact predicate. If a named later use needs occurrence identity, identify the obtaining parthood occurrence or its temporal extent under the exact defining `ClaimGraph`. If it instead needs the installation act that established the condition, first identify a separate dated Work occurrence under A.15.1. Add an actual transformation under A.3.4 only when a current claim says that the installation changed a continuing referent, and state the exact direct relation between Work and transformation when that relation is also claimed. Neither object nor their coexistence is the parthood occurrence or supplies that relation. | report-as-relation; assertion-as-obtaining; report fields as world-side participants; parthood occurrence as installation Work or transformation. |
| Graph edge `Edge_17(Bearing_B, Pump_P)` presents that assertion. | The representation use is already clear, so bypass E.10.ARCH to C.29. Keep `Edge_17` as a representation element with an explicit correspondence to the represented assertion or direct-relation claim; the edge does not make `Bearing_B isPartOf Pump_P` obtain or identify its occurrence. | edge-as-world-relation; adjacency-as-obtaining; graph identity as relation-occurrence identity. |
| A reusable `RelationSignature` declares `ParticipantSlot`, and a row shows `Bearing_B_Ref`. | The declaration use is already clear, so bypass E.10.ARCH to A.6.5. `ParticipantSlot` is a `SlotSpec`; `Bearing_B` is the actual governed participant; `Bearing_B_Ref` is a participant designation only inside the current assertion or occurrence-description episteme. | SlotSpec-as-participant; designation-as-participant; type-correct filling as obtaining. |
| `MethodDescription_NormalizeCustomer`, which describes one exact `U.Method` `NormalizeCustomer`, says “input x is CustomerRow_17” beside the worked formula `normalize(x)`. | The current use is the worked formula's argument representation, so bypass E.10.ARCH to C.29. Keep `Arg_x` as the representation element and state the explicit correspondence from `Arg_x` to the described value `CustomerRow_17`. The repaired practitioner sentence is: “In the worked formula `normalize(x)`, argument `x` represents `CustomerRow_17`.” That correspondence neither asserts a universal input relation nor establishes participation in dated Work or an actual transformation. | universal input ontology; argument place as world-side participant; method description as actual Work or transformation; representation correspondence as obtaining. |
| Another source calls something `input`, but its exact object or use remains hidden. | Bound the exact sentence, then use the wider dispatch only until its subject and predicate are clear: A.3.2 for a declared or represented value inside a `U.MethodDescription` about one exact method; A.15.2 for intended planned use; A.15.1 plus the exact participation or resource predicate for dated Work; A.3.4.P plus the direct transformation predicate for an actual transformation participant; the exact production, measurement, evaluation, delivery, or acceptance predicate for a result claim; or C.29 for an argument, tuple component, edge, or other representation place. The repaired sentence states the exact direct relation or representation correspondence established by that predicate; naming only the pattern is incomplete. Use A.6.P.WMR only while that relation remains hidden. | routing list as repair; universal input ontology; one generic result relation; premature Work or transformation actuality. |
| "The architecture is the diagram." | Use `C.30.P` to recover whether the diagram is publication form, structure view, architecture description, source relation, or ordinary source-finding cue; then state a C.30 or C.30.ASV subject assertion only after the selected architecture or structural-view use is recovered. | diagram-as-architecture; diagram-as-proof; diagram-as-gate. |
| "For PlantOps use U, selected structure S1 organizes holon H in the declared way; C.30 records the obtaining `ArchitectureRelation` and a separate `ArchitectureClaim` about it." | Direct `C.30`; no `C.30.P` unless another selected structure, architecture-description use, structural-view use, source relation, model relation, diagram relation, graph relation, dashboard relation, or ordinary prose remains hidden. | unnecessary restoration detour. |
| "The model has three layers." | Use `C.30.STRAT` to treat `layers` as a source label until the recovered FPF kind, relation, claim-use, or source-relation disposition is clear: control-layer relation, neural-network block sequence, publication relation set, mathematical scale or coarse-graining relation, or ordinary source wording. Then state the recovered subject assertion under its defining or constraining rule. | layer-as-universal-kind; source label as proof of structure. |
| "The query plan calls the next pattern." | `C.2.P.DR` recovers whether the query plan is a representation, a one-method description episteme, formal substrate, evidence or provenance relation, or ordinary source wording; if a pattern relation is current, state it declaratively rather than as a call. | query-as-work sequence; pattern relation as invocation. |
| "The evidence path authorizes release." | If a provenance relation for a claim is current, state its exact A.10 assertion; if authorization or release is current, state the separate authority, gate, or release assertion under its defining rule. Use `C.2.P.DR` only when `path` wording turns the relation into an action route or permission. | evidence path as permission; graph relation as release. |
| "The solver algorithm is the mechanism." | Use `A.3.1` to recover whether the wording denotes one exact method or a direct method-side relation. A current A.3.2 assertion obtains only when one exact episteme describes that Method. Formal substrate, C.29 representation, mechanism declaration or realization, Work, result, and quote-only wording remain separate subject assertions under their own defining or constraining rules. | algorithm-as-default-method; method-as-mechanism by vocabulary. |
| "This record is admissible." | Recover bearer, claim kind, source relation, value frame, admissible use, exact subject assertion, and its defining or constraining rule. Use `A.19.SPR` only if hidden state-family wording remains; otherwise state the exact evidence, gate, mechanism, temporal, authority, release, or source-relation assertion. | admissible-as-generic status; pass-looking word as gate. |
| "This score proves readiness." | Use `C.16.P` to recover characteristic, scale, value, score, threshold, and comparison reference set; state gate, evidence, and decision assertions separately under their own defining or constraining rules. | score-as-proof; score-as-release permission. |
| "This source supports the claim." | `C.2.P` is used if source-currentness relation or publication relation set is current; relation slice applies `A.6.P`; final use states recovered relation or non-use disposition. | source-as-proof; support-as-generic relation. |
| "Quality improved." | Use `C.16.Q` to recover quality characterization or evaluative characterization, or state the exact characteristic, evaluation, relation, action, Work, or bridge assertion under the rule located through `C.16.P`, `C.16.Q`, `C.25`, or the pattern that defines or tests the recovered assertion. | quality-as-one scalar; quality-as-gate. |
| "The function improved maintainability." | Use `A.6.F` to recover the FPF kind, relation, or claim when hidden; then state the exact quality or maintainability assertion under the rule located through `C.16.P`, `C.16.Q`, `C.25`, or the pattern that defines or tests the recovered assertion. | function-as-default-architecture; maintainability-as-unscaled verdict. |
| "Read this pattern for improvement proposals." | Recover whether the current FPF-governed use is source-publication use, bounded comparative review unit, or improvement-oriented evaluation. Use `E.22` only for improvement-oriented quality review under a declared pattern-under-improvement evaluation. | generic reading as a pattern. |
| "This summary is enough for action." | `E.10` checks whether the wording is precision restoration or controlled precision reduction. If coarsened source-to-rendering use is current, `A.6.3.CSC` names source-bearing side, loss mode, narrower admissible use, non-admissible downstream use, and reopen condition. | summary-as-full source; coarsening without declared loss. |

