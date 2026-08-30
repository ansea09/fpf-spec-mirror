---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__003_problem.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:2 — Problem"
line_start: 4628
line_end: 4641
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "G.11"
  - "G.6"
  - "U.SystemRoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use relation"
  - "provenance"
  - "role-shaped source phrase"
  - "source-use wording"
  - "status-use relation"
---

### A.2.4:2 - Problem

Source text may use `U.EvidenceRole` or another evidence-like *role* label for a real need: an episteme can be used as evidence for a claim under an effective source scheme and exact ClaimScope, with polarity, time, assurance use, weight, and provenance constraints. Treat those spellings as source-word triggers. The FPF repair states an evidence-use relation; it does not classify the episteme under a system-role kind or place it in a `U.SystemRoleAssignment`.

That creates several failures:

1. **Episteme-as-holder drift.** A paper, proof, dataset, standard, or dashboard cell is treated as if it were classified under a work-facing system-role kind or filled the holder position of an assignment.
2. **Evidence-word ontology drift.** `ModelFitEvidenceRole`, `MeasurementEvidenceRole`, or `AxiomaticProofRole` is treated as a kind merely because the source label ends in *Role*, instead of being resolved to an evidence-use relation classification or local evidence-use label.
3. **Claim relation collapse.** Target claim, grounding holon, claim scope, polarity, relevance window, assurance use, weight model, and provenance constraints are hidden behind one source label ending in *Role*.
4. **Evidence and status collapse.** A status badge, standard reference, approval-looking display, publication face, or requirement source is treated as evidence, status assertion, gate passage, permission, and assurance at once.
5. **Work confusion.** The work that produced an episteme and the later use of that episteme as evidence are folded into one relation.
6. **Causal-use laundering.** Observational association, intervention, realized counterfactual sample, identified counterfactual estimate, and simulation-only output are relabelled by evidence-wording instead of being governed by `C.28`.
7. **Cross-local leakage.** Evidence accepted under one source scheme, ClaimScope, and use is reused under another without recovering the changed meaning, source currentness, reliance, or assurance-use conditions and any actual F.9 relation.

