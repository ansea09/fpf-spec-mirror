---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__001_intro.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:intro — Intro"
line_start: 39054
line_end: 39070
dependencies:
  - "A.2.6"
  - "C.3.x"
keywords:
  - "ESG"
  - "Kind-CAL"
  - "Method-Work"
  - "Typed guard"
  - "USM"
  - "regulatory profile"
---

## C.3.A - Typed Guard Macros for Kinds + USM (Annex)

> **One‑line summary.** Provides **normative guard macros** that combine **USM Scope** (A.2.6) with **Kind‑CAL** (C.3.x) so authors can gate state changes and compositions that **quantify over kinds** without conflating **describedEntity** (Kinds) with **applicability** (Scope **G**) or **assurance** (**R**). Includes **decision trees, anti‑patterns, and examples** (informative). **AT (KindAT)** is **never** used in guards.

**Status.** Mixed:
— **Normative**: guard macro clauses, evaluation order, fail‑closed discipline, conformance checklist.
— **Informative**: …  decision trees, anti‑patterns, worked examples, macro skeletons.

**Placement.** Part C (Kinds), identifier **C.3.A** (Annex). Audience: engineering managers, editors, reviewers, assurance leads.

**Depends on.**
— **A.2.6 USM**: `U.ContextSlice`, `U.ClaimScope` (**G**), `U.WorkScope`, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridge + **CL** (scope).
— **C.3.1**: `U.Kind`, `U.SubkindOf (⊑)`; **C.3.2**: `KindSignature` (with **F**) and `Extension/MemberOf`; **C.3.3**: **KindBridge** + `CL^k` (kind‑congruence) & loss notes; **C.3.4**: **RoleMask**.
— **C.3.5**: **KindAT** (facet) — **explicitly forbidden** in guards.
— **C.2.2 F–G–R**: weakest‑link, penalties to **R** only; **C.2.3 F**: F0…F9 (expression rigor).
— **Part B Bridges & CL**: scope bridge semantics and CL ladder.

