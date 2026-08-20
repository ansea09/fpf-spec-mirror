---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:3"
section_title: "Forces (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__005_forces-normative.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:3 — Forces (normative)"
line_start: 32427
line_end: 32437
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UINDM"
  - "A.19.ULSAM"
  - "A.19.USCM"
keywords:
  - "CG-Spec.SCP"
  - "CG-Spec.Γ_fold"
  - "MinimalEvidence"
  - "fold_Γ?"
  - "lawful aggregation"
  - "scale-lawful fold"
  - "tri-state guard (pass"
  - "ΓFoldRef"
---

### A.19.ULSAM:3 - Forces (normative)

- **Lawfulness vs convenience.** The most “convenient” aggregation (e.g., weighted sums) is often illegal across scales/units; lawful folds require explicit constraints.
- **Explicitness vs brevity.** A single scalar is short to discuss, but expensive in hidden assumptions.
- **Kernel stability vs method evolution.** Aggregation methods evolve; the kernel must not.
- **Evidence gating vs “always return a number.”** The mechanism must support abstain/degrade rather than coercion.
- **Optional stage vs pipeline clarity.** `fold_Γ?` is optional in CHR protocols; optionality must be explicit (not implicit “sometimes scoring folds”).
- **Auditability vs minimal overhead.** Recording contributor sets and effective pins adds overhead but prevents semantic drift.
- **Declared-set locality vs reuse.** A fold is valid for one admitted measure set, grouping or membership basis, policy editions, scope and window, evidence basis, contributors, and intended result; a later use must recheck those premises and cite any relation it actually relies on.
- **P2W separation and gate/guard separation.** ULSAM must expose eligibility and audit pins without turning into (i) a WorkPlanning baseline binder or (ii) an admissibility gate: planned slot fillings belong to WorkPlanning plan items, while GateDecision/GateLog live in gate patterns / WorkEnactment (suite protocols remain mechanism-steps only).

