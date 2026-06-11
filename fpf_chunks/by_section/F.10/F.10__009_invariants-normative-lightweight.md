---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping (Evidence • Standard • Requirement)"
section_id: "F.10:8"
section_title: "Invariants (normative, lightweight)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__009_invariants-normative-lightweight.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "F.10 — Status Families Mapping (Evidence • Standard • Requirement)"
  - "F.10:8 — Invariants (normative, lightweight)"
line_start: 73400
line_end: 73411
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:8 - Invariants (normative, lightweight)

1. **Modality purity.** A StatusCell’s **StatusModality** is explicit and **must not change** during reasoning; cross‑modality claims require an **Interpretation Bridge** (F.9).
2. **Target typing.** A status **must name its Target kind**: claim, artefact, or clause. Inferences that ignore the Target kind are invalid.
3. **Window discipline.** Every positive/negative status **names a Window**; contradictions are detected **within the same Window** only.
4. **Local monotonicity.** Within one context, a higher-support EvidenceStatus implies all lower-support positives for the same Target & Window.
5. **Mutual exclusivity (requirement).** For a given clause & Window: **not** (Satisfied ∧ Violated).
6. **No free promotion.** **StandardStatus** (Approved) **does not** entail **RequirementStatus** (Applicable or Satisfied).
7. **Bridge gate.** Any Cross‑context comparison or reuse of a status **must cite a Bridge** (kind, CL, Loss); otherwise only **context‑local** reading is permitted.
8. **Weakest‑link propagation.** When multiple Bridges contribute to a Cross‑context interpretation, the **effective CL** is the **minimum** (cf. F.7/F.9).
9. **Naming restraint.** Status labels used across Contexts **without** a Bridge are **Naming-only** and **non-operative** for Role Assignment & Enactment decisions.

