---
chunk_kind: "child"
pattern_id: "A.19.USCM"
pattern_title: "Unified Scoring Mechanism, USCM"
section_id: "A.19.USCM:6"
section_title: "Bias-Annotation — informative"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.USCM/A.19.USCM__008_bias-annotation-informative.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.19.USCM — Unified Scoring Mechanism, USCM"
  - "A.19.USCM:6 — Bias-Annotation — informative"
line_start: 28662
line_end: 28673
dependencies:
keywords:
  - "CG-Spec.MinimalEvidence"
  - "CSLC-lawful transforms"
  - "ScaleComplianceProfile (SCP)"
  - "ScoringMethodDescription"
  - "score profile"
  - "scoring"
  - "tri-state admissibility (pass"
---

### A.19.USCM:6 - Bias-Annotation — informative

* **Gov (governance).** Bias toward explicit admissibility and evidence surfaces (`CGSpecRef`, `SCP`, `MinimalEvidence`) rather than "standard practice" arithmetic. Risk: perceived overhead. Mitigation: keep the kernel signature small and push method specifics into SoTA packs and wiring modules.

* **Arch (architecture).** Bias toward stable interfaces and strict step boundaries (no implicit UNM; no hidden scalarization). Risk: reduced room for ad‑hoc shortcuts. Mitigation: allow richer scoring method families via wiring, without mutating the USCM intension.

* **Onto/Epist.** Bias toward treating scores as measures with declared semantics, not as “the truth.” Risk: teams accustomed to one‑number rankings may resist. Mitigation: treat scalarization as an explicit, auditable commitment, not as the default.

* **Prag (pragmatics).** Bias toward fail‑closed guards and traceability under uncertainty. Risk: more `degrade/abstain` outcomes early. Mitigation: couple `degrade` with explicit downstream behavior policies, rather than silent coercion.

* **Did (didactics).** Bias toward “one place to learn the mechanism”: the problem/forces/solution narrative is co‑located with the canonical Mechanism.Intension.

