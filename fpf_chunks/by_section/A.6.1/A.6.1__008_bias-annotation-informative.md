---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:6"
section_title: "Bias-Annotation (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__008_bias-annotation-informative.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:6 — Bias-Annotation (informative)"
line_start: 9215
line_end: 9224
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.6.0"
  - "C.16"
  - "E.10.D1"
  - "G.10"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:6 - Bias-Annotation *(informative)*

This pattern intentionally biases Mechanism declaration toward explicit signatures and laws, context-local semantics, and auditable reuse.

* **Gov (governance).** Bias toward publishable declaration rows, conformance checks, and explicit policy-ids for crossings. Risk: perceived declaration overhead. Mitigation: reuse the `MechanismDeclaration` template; keep Realizations opaque and put operational details outside the Kernel.
* **Arch (architecture).** Bias toward locality-first semantics and **Bridge-only** transport with costs recorded in **R or R_eff**. Risk: reduced convenience for ad-hoc cross-context reuse. Mitigation: publish adapter mechanisms and make crossings explicit via `Transport` (CC-UM.3 and CC-UM.4).
* **Onto and Epist (ontology and epistemology).** Bias toward lawful comparability (CHR legality; CG-Spec binding) and against illegal scalarisation (e.g., ordinal means). Risk: some heuristic scoring practices become non-conformant. Mitigation: represent uncertainty explicitly and use `unknown → {degrade, abstain}` rather than coercions (CC-UM.7).
* **Prag (practice).** Bias toward notation-independence and against tool or vendor tokens in the Kernel. Risk: teams may want to inline CI or telemetry fields. Mitigation: keep audit surfaces conceptual (`Audit`) and reference operational hooks by id only (CC-UM.6).
* **Did (didactic).** Bias toward explicit SlotKinds and SlotSpecs over positional parameters. Risk: steep learning curve. Mitigation: allow non-normative projections (`ValueKindView`) and include a “60-second” script plus a mechanism declaration checklist (A.6.1:4.7 and 4.8).

