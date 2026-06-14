---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:8"
section_title: "Anti‑patterns (normative):"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__009_anti-patterns-normative.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:8 — Anti‑patterns (normative):"
line_start: 45349
line_end: 45359
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

### C.22:8 - Anti‑patterns (normative):
* **AP‑1** Pre‑binding a Method into S2 (“problem as if task”); **Remedy:** keep S2 method‑agnostic; bind only admissible traits.
* **AP‑2** Silent `unknown→false` or `unknown→0` in Eligibility and Acceptance.
* **AP‑3** Cross‑ordinal averaging or ordinal–interval scalar mixes.
* **AP‑4** **DesignRunTag chimera** signatures (mixing stances).
* **AP‑5** **Domain** treated as governance (attach governance to **U.Discipline** and **CG‑Spec**, not Domain).
* **AP‑6** Implicit handling of data‑shift (assume iid); **Remedy:** declare `ShiftClass` (or `unknown`) and gate via Acceptance.
* **AP‑7** Tool or vendor tokens in normative text; **Remedy:** move to Plain‑register note; keep Tech references on CHR and CAL ids (LEX V‑4).

**Remedies:** tri‑state predicates; admissible order relations (lexi, Pareto, median, or medoid); explicit **GateCrossing** visibility through **CrossingBundle** (BridgeCard + UTS row + `CL/Φ` policy‑ids; **E.18**, **F.9**, **F.17**, **E.17**, and **A.21** where live); Domain stitched to **D.CTX + UTS** only.

