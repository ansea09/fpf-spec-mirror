---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__003_problem.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:2 — Problem"
line_start: 15215
line_end: 15241
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:2 - Problem

Without a dedicated pattern for EpistemicRetargeting:
1. **Retargeting is silently confused with viewing.**
   Structural reinterpretations (e.g., component→function, signal→spectrum, data→model) can be mistakenly treated as “just another view” with the same EntityOfConcern, even though they change `entityOfConcernRef`. This hides the fact that the **EntityOfConcern** has changed and that a `KindBridge` and invariant are required.

2. **Invariants float untyped.**
   Fourier‑style moves, structural reinterpretations, and abstraction/refinement steps are often justified by “energy is preserved”, “this component realises that function”, or “this model summarises those data” — but these invariants are not connected to the episteme morphism class. Without a dedicated species:

   * invariants remain only in prose,
   * CL‑penalties and ReferencePlane crossings cannot be tracked systematically (Part F).

3. **Cross‑kind reasoning has no canonical morphism.**
   A general EFEM (A.6.2) can change `entityOfConcernRef` by setting `entityOfConcernChangeMode = retarget`, but:

   * nothing states what that means at the level of kinds (`Kind(entityOfConcernRef(X))` vs `Kind(entityOfConcernRef(Y))`),
   * nothing connects these moves to `KindBridge` and ReferencePlane policies.

4. **StructuralReinterpretation is ad‑hoc.**
   `E.18` positions `StructuralReinterpretation` as a transformation-flow locus, but its retargeting semantics are the generic “retargeting under a bridge” relation governed here, not a special graph-position ontology. Without a core pattern:

   * StructuralReinterpretation risks duplicating retargeting logic,
   * other discipline packs may reinvent their own ad‑hoc re‑targetings.

5. **EntityOfConcern and Description-episteme boundary and specification-use discipline is left underspecified.**
   For Description epistemes and Description epistemes admitted for specification use (`...Description` and `...Spec`), retargeting **changes `EntityOfConcernRef` in `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩`** (E.10.D2), but must say what happens to context and viewpoint. Without an explicit pattern, these decisions get scattered across different E‑patterns instead of being governed centrally.

