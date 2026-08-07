---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__003_problem.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:2 — Problem"
line_start: 4157
line_end: 4170
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:2 - Problem

Source text may name `U.EvidenceRole` or evidence-like role labels for a real need: an episteme can be used as evidence for a claim inside a bounded context, with scope, polarity, time, assurance use, weight, and provenance constraints. The FPF repair is to model that use as an evidence-use relation, not as a non-behavioral role held by the episteme through `U.RoleAssignment`.

That creates several failures:

1. **Episteme-as-holder drift.** A paper, proof, dataset, standard, or dashboard cell is treated as if it held a work-facing role.
2. **Evidence role ontology drift.** `ModelFitEvidenceRole`, `MeasurementEvidenceRole`, or `AxiomaticProofRole` look like role kinds instead of evidence-use relation classifications or local evidence-use labels.
3. **Claim relation collapse.** Target claim, grounding holon, claim scope, polarity, relevance window, assurance use, weight model, and provenance constraints are hidden behind one role name.
4. **Evidence and status collapse.** A status badge, standard reference, approval-looking display, publication face, or requirement source is treated as evidence, status assertion, gate passage, permission, and assurance at once.
5. **Work confusion.** The work that produced an episteme and the later use of that episteme as evidence are folded into one relation.
6. **Causal-use laundering.** Observational association, intervention, realized counterfactual sample, identified counterfactual estimate, and simulation-only output are relabelled by evidence-wording instead of being governed by `C.28`.
7. **Cross-context leakage.** Evidence accepted in one context is reused in another without an explicit bridge, source-currentness relation, or assurance-use statement.

