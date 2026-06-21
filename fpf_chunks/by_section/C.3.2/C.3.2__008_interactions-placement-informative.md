---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "KindSignature (+F) & Extension/MemberOf"
section_id: "C.3.2:7"
section_title: "Interactions & Placement (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__008_interactions-placement-informative.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "C.3.2 — KindSignature (+F) & Extension/MemberOf"
  - "C.3.2:7 — Interactions & Placement (informative)"
line_start: 40132
line_end: 40139
dependencies:
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
keywords:
  - "Formality F"
  - "KindSignature"
  - "MemberOf"
  - "determinism"
  - "extension"
  - "intension"
---

### C.3.2:7 - Interactions & Placement (informative)

* **With C.3.1.** Kinds carry identity and `⊑`; **no Scope** on kinds. This pattern adds the **intent/extent** layer under those constraints.
* **With A.2.6 (USM).** A typed claim’s guard normally evaluates, in the order specified by **Annex C.3.A §5 (E‑01)**: (1) typed compatibility, (2) **Scope coverage** at `TargetSlice`, (3) **`MemberOf(?, k, TargetSlice)`** definedness and any instantiation, followed by penalties to **R** and freshness checks. Use **Guard_TypedClaim** / **Guard_TypedJoin** rather than ad‑hoc shapes.
* **With C.2.3 (F).** Signature F influences claims **only if** the claim **depends on** the signature content; weakest‑link min applies along the claim’s support path.
* **With C.3.3 (KindBridge).** When `MemberOf` is computed via a **kind mapping across Contexts**, kind‑congruence `CL^k` contributes a **monotone penalty to **R** only (Ψ(`CL^k`)); **F/G MUST NOT** be adjusted.
* **With Role‑CAL (C.3.4).** A **RoleMask** may **narrow** membership (context‑local adaptation). Frequent masks that encode stable narrowing **SHOULD** be promoted to subkinds (`⊑`).

