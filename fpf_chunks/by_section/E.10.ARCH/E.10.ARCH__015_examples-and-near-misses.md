---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:9"
section_title: "Examples and near misses"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__015_examples-and-near-misses.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:9 — Examples and near misses"
line_start: 77486
line_end: 77509
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
  - "E.10.DEV"
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

Read each wording with its stated use. Apply a route only while that FPF question remains unresolved; clear ordinary wording closes under `F.19`.

| Wording | Applicable result | Grounded distinction in this near-miss |
| --- | --- | --- |
| `MaintenanceReport_42` says “Bearing_B is installed in Pump_P.” | The report's mereology claim is already clear, so bypass E.10.ARCH. `MaintenanceReport_42` is the claim-bearing episteme asserting `Bearing_B isPartOf Pump_P`. If a named later use needs world-side occurrence identity, establish that the parthood relation obtains before identifying its occurrence or temporal extent under the exact defining `ClaimGraph`. If it instead needs the installation act that established the condition, first identify a separate dated Work occurrence under A.15.1. Add an actual transformation under A.3.4 only when a current claim says that the installation changed a continuing referent, and state the exact direct relation between Work and transformation when that relation is also claimed. An asserted Work-to-transformation relation needs its own defining predicate. | The report's assertion, the obtaining parthood relation, and any separately requested installation Work or transformation. |
| Graph edge `Edge_17(Bearing_B, Pump_P)` presents that assertion. | The representation use is already clear, so bypass E.10.ARCH to C.29. Keep `Edge_17` as a representation element with an explicit correspondence to the represented assertion or direct-relation claim; the edge does not make `Bearing_B isPartOf Pump_P` obtain or identify its occurrence. | The graph element, the represented assertion, and any separately established world-side relation occurrence. |
| A reusable `RelationSignature` declares `ParticipantSlot`, and a row shows `Bearing_B_Ref`. | The declaration use is already clear, so bypass E.10.ARCH to A.6.5. `ParticipantSlot` is a `SlotSpec`; `Bearing_B` is the actual governed participant; `Bearing_B_Ref` is a participant designation only inside the current assertion or occurrence-description episteme. | The declared `SlotSpec`, the actual participant, and a designation inside an assertion. |
| Another source calls something `input`, but its exact object or use remains hidden. | Recover the exact source sentence and what `input` refers to. Use only the applicable source, Method/Work, transformation, result, or representation branch in section 3.1; return to the direct defining or testing rule once the object and predicate are clear. The repaired sentence states the exact direct relation or representation correspondence established by that predicate. Use `A.6.P.WMR` only while the Method/Work boundary relation remains hidden, and return its exact reason-specific result when a claim cannot be established. | The source word, its referent, and the particular relation or representation use that must be recovered. |
| "The architecture is the diagram." | Use `C.30.P` to recover whether the diagram is publication form, structure view, architecture description, source relation, or ordinary source-finding cue; then state a C.30 or C.30.ASV subject assertion only after the selected architecture or structural-view use is recovered. | The diagram's publication or representation use and the architecture claim about the holon and selected structure. |
| "For PlantOps use U, selected structure S1 organizes holon H in the declared way; C.30 records the obtaining `ArchitectureRelation` and a separate `ArchitectureClaim` about it." | Direct `C.30`; no `C.30.P` unless another selected structure, architecture-description use, structural-view use, source relation, model relation, diagram relation, graph relation, dashboard relation, or ordinary prose remains hidden. | An already explicit `ArchitectureRelation` and its separate `ArchitectureClaim`. |
| "The model has three layers." | Use `C.30.STRAT` to treat `layers` as a source label until the recovered FPF kind, relation, claim-use, or source-relation disposition is clear: control-layer relation, neural-network block sequence, publication relation set, mathematical scale or coarse-graining relation, or ordinary source wording. Then state the recovered subject assertion under its defining or constraining rule. | The source label `layer` and the particular structural, publication, or mathematical claim it carries. |
| "The query plan calls the next pattern." | `C.2.P.DR` recovers whether the query plan is a representation, a one-method description episteme, formal substrate, evidence or provenance relation, or ordinary source wording; if a pattern relation is current, state it declaratively rather than as a call. | A declarative pattern relation versus an actual invocation or work sequence. |
| "The evidence path authorizes release." | If a provenance relation for a claim is current, state its exact A.10 assertion; if authorization or release is current, state the separate authority, gate, or release assertion under its defining rule. Use `C.2.P.DR` only when `path` wording turns the relation into an action route or permission. | The provenance or evidence claim and the separately justified authorization or release decision. |
| "The solver algorithm is the mechanism." | Use `A.3.1` to recover whether the wording denotes one exact method or a direct method-side relation. A current A.3.2 assertion obtains only when one exact episteme describes that Method. Formal substrate, C.29 representation, mechanism declaration or realization, Work, result, and quote-only wording remain separate subject assertions under their own defining or constraining rules. | The method or method-side relation and any independently admitted mechanism claim. |
| "This record is admissible." | State the record's admissible use and the exact assertion under the rule that establishes it. Recover the bearer, claim kind, source relation, or value frame only while that basis remains unclear. Use `A.19.SPR` only if a state-family object or frame remains hidden; otherwise use the direct subject rule. | The use for which the record is admissible and the rule establishing it. |
| "This score proves readiness." | Use `C.16.P` to recover characteristic, scale, value, score, threshold, and comparison reference set; state gate, evidence, and decision assertions separately under their own defining or constraining rules. | The measured score, readiness criterion, and evidence or decision supporting the readiness claim. |
| "This source supports the claim." | Use the direct subject rule for an already clear support claim. Use `C.2.P` while a source-currentness relation or publication relation set remains unresolved, and `A.6.P` only while the direct predicate or an actual participant remains hidden. State the recovered relation or grounded non-use result. | What the identified source contributes to the identified claim. |
| "Quality improved." | Use `C.16.Q` to recover quality characterization or evaluative characterization, or state the exact characteristic, evaluation, relation, action, Work, or bridge assertion under the rule located through `C.16.P`, `C.16.Q`, `C.25`, or the pattern that defines or tests the recovered assertion. | The quality or evaluative characterization and the particular change being claimed. |
| "The function improved maintainability." | Use `A.6.F` to recover the FPF kind, relation, or claim when hidden; then state the exact quality or maintainability assertion under the rule located through `C.16.P`, `C.16.Q`, `C.25`, or the pattern that defines or tests the recovered assertion. | The recovered function claim and the separately stated maintainability change. |
| "Read this pattern for improvement proposals." | Follow an ordinary reading instruction without restoration. Use `E.22` only when a declared pattern-under-improvement evaluation makes this an improvement-oriented quality review. Distinguish source-publication use or a bounded comparative review unit only when that use is claimed. | An ordinary reading instruction versus a declared improvement-oriented quality review. |
| "This summary is enough for action." | `E.10` checks whether the wording is precision restoration or controlled precision reduction. If coarsened source-to-rendering use is current, `A.6.3.CSC` names source-bearing side, loss mode, narrower admissible use, non-admissible downstream use, and reopen condition. | The source-to-summary loss, the narrower admissible use, and the condition for returning to the source. |

