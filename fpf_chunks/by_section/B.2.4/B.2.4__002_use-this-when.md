---
chunk_kind: "child"
pattern_id: "B.2.4"
pattern_title: "Do Capability or Functioning Changes Require Whole Reidentification?"
section_id: "B.2.4:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.4/B.2.4__002_use-this-when.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "B.2.4 — Do Capability or Functioning Changes Require Whole Reidentification?"
  - "B.2.4:0 — Use This When"
line_start: 44205
line_end: 44224
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2.2"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.2"
  - "B.2.P"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.18"
keywords:
---

### B.2.4:0 - Use This When

Use this pattern when capability, functioning, or transformation-flow facts, established under their subject patterns, raise a B.2 whole-reidentification question.

The first useful question is whether those facts can still be explained by the existing whole. If they can, keep that whole and use the direct pattern for the capability, functioning relation, transformation, Method, Work, module, characteristic, or architecture claim. If they cannot, use B.2 for the residual question. Evidence and measurement support, challenge, or leave unresolved the claims about those facts. Use the supported facts in B.2's comparison of the existing and candidate wholes.

**What goes wrong if missed.** A genuine new whole is hidden under ordinary capability improvement; or every impressive capability, function, method chain, module allocation, or metric gain is overclaimed as emergence.

**What this buys.** The practitioner can distinguish a change within an existing whole from a capability or functioning change that requires testing a new whole.

**Not this pattern when.**

- If the claim is ordinary capability, use `A.2.2`; use `C.16` for its measured-characteristic claims.
- If function-like wording hides the exact claim, use `A.6.F` to recover its direct subject pattern; an already precise functioning claim returns directly to that pattern.
- If the claim is transformation or transformation-flow structure, use `A.3.4` or `E.18` respectively; use `C.30.TFS-REL` for the selected structure's bounded architecture use.
- Use `A.3.1` for Method identity, `B.1.5` for Method composition, `A.3.2` for a MethodDescription, `A.15.2` for a WorkPlan, and `A.15.1` for a Work occurrence; `A.15` aligns roles, Methods, and Work.
- If bearer allocation is the question, use the direct allocation or parthood pattern. Use `A.6.M` only for unresolved module/interface wording, and `C.30`, `A.22` or `C.30.ASV` only for the current architecture, selected-structure or architectural-view claim.
- If the claim is measurement, threshold, score, robustness, quality, or a whole-level characteristic, use `C.16` and `A.19` for that claim and `A.10` only when evidence use is current.
- If the wording is ambiguous emergence, synergy, or title-mnemonic language, use `B.2.P` before selecting B.2.4.

