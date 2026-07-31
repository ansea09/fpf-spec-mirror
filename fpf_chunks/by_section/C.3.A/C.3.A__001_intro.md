---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__001_intro.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:intro — Intro"
line_start: 45710
line_end: 45728
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2.6"
  - "C.2.2"
  - "C.2.3"
  - "C.3"
  - "C.3.1-C.3.5"
keywords:
  - "ESG"
  - "Method-Work"
  - "assurance"
  - "declaration compatibility"
  - "exact candidate judgment"
  - "guard refusal"
  - "regulatory"
  - "true/false/unknown"
---

## C.3.A - Typed Guard Macros for Kinds + USM (Annex)

> **One-line summary.** These guard macros combine C.3 declaration compatibility, the exact C.3.2 candidate judgment when an actual candidate is current, RoleMask and KindBridge declarations/relations, and A.2.6 Scope without collapsing them. A claim quantified over a kind can be checked at declaration level; applying that claim or a capability to one candidate additionally requires `J(candidate, kind, signatureEdition, slice)`. `true`, `false`, and `unknown` remain classification values, while allow/refuse remains a separate guard disposition. KindAT never appears in a guard.

**Status.** Normative for macro obligations, evaluation order, three-valued/fail-closed discipline, and the conformance checklist; informative for decision trees, examples, and implementation-like skeletons.

**Placement.** Part C (Kinds), identifier **C.3.A**. Audience: engineering managers, editors, reviewers, assurance leads, and authors of regulatory, evidence, ESG, and Method–Work checks.

**Depends on.**

- **A.2.6 USM:** exact `U.ContextSlice`, Claim/Work scope, `Gamma_time`, scope bridges, and SpanUnion.
- **C.3/C.3.1:** exact local kinds and obtaining `U.SubkindOf` relations.
- **C.3.2:** `KindSignature` declaration epistemes, `J(candidate, kind, signatureEdition, slice)`, `true`/`false`/`unknown`, and optional extension representations.
- **C.3.3:** obtaining `KindBridge` relations and separate bridge-assertion epistemes carrying `CL^k`, loss, evidence, definedness, and admitted use.
- **C.3.4:** `RoleMask` and `MaskAdapter` declaration epistemes and `J_mask(candidate, kind, kindSignatureEdition, roleMaskEdition, slice)`.
- **C.3.5:** KindAT as an editorial facet forbidden in guards.
- **C.2.2/C.2.3 and Part B:** F–G–R, formality on the owning episteme, bridge consequences, and scope congruence.
- **A.15/A.15.1:** the separation of capability, plan, exact actual Work occurrence, and every episteme about it.

