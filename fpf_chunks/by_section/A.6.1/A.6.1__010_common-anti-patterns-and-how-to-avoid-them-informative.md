---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__010_common-anti-patterns-and-how-to-avoid-them-informative.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:8 — Common Anti-Patterns and How to Avoid Them (informative)"
line_start: 9421
line_end: 9433
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

### A.6.1:8 - Common Anti-Patterns and How to Avoid Them *(informative)*

| Anti-pattern | What it looks like | Remedy |
| --- | --- | --- |
| **SlotIndex treated as a 5th Signature row** | Reviews start comparing mechanisms by `SlotIndex` only; SlotSpecs disappear from operator declarations. | Keep SlotSpecs **inline per operator**; treat `SlotIndex` as a derived projection only (CC‑UM.0, CC‑UM.9). |
| **Admission tests put in LawSet** | “Eligibility” and “coverage” checks appear as laws; implementations silently diverge. | Move operational guards to `AdmissibilityConditions` (CC‑UM.1). |
| **Implicit crossings or hidden CL policy tables** | A mechanism is reused across Contexts or planes without a declared BridgeId or ReferencePlane; CL, Φ, or Ψ tables get copied into local prose. | Crossings must be explicit and **Bridge-only**; `Transport` references policy ids or registries (CC-UM.3). |
| **Penalties leak into F or G** | A plane, kind, or scope mismatch is handled by mutating Formality or Guarantee claims. | Record penalties in **R or R_eff only**; keep **F and G** invariant (CC-UM.4). |
| **Illegal scalarisation** | Ordinal means or cross-unit arithmetic is performed “because we need a number”. | Bind numeric comparison or aggregation to CG-Spec, MM-CHR, and CSLC; keep partial orders set-valued (CC-UM.5). |
| **Specialisation breaks SlotKind identity** | Refinements rename SlotKinds or add mandatory parameters to inherited operations. | SlotKinds are invariant; refinements only narrow ValueKinds or guards; add new operations via Extension (CC-UM.8). |
| **Unknown coerced to 0 or false** | Guard failures silently become “false” or scores become 0. | Use tri-state discipline: `unknown → {degrade, abstain}`; probing lives in LOG branches (CC-UM.7). |
| **In-place minting of BaseType** | A mechanism definition introduces a new `U.Type` ad hoc. | `BaseType` references an existing `U.Type`; mint new types through an accepted FPF naming and kind decision outside the mechanism (CC-UM.6). |

