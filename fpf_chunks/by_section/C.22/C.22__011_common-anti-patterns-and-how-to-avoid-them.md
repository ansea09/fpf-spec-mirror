---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__011_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 46396
line_end: 46406
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

### C.22:8 - Common Anti-Patterns and How to Avoid Them
* **AP‑1** Pre‑binding a Method into S2 (“problem as if task”); **Remedy:** keep S2 method‑agnostic; bind only admissible traits.
* **AP‑2** Silent `unknown→false` or `unknown→0` in Eligibility and Acceptance.
* **AP‑3** Cross‑ordinal averaging or ordinal–interval scalar mixes.
* **AP‑4** **DesignRunTag chimera** signatures (mixing stances).
* **AP‑5** **Domain** treated as governance (attach governance to **U.Discipline** and **CG‑Spec**, not Domain).
* **AP‑6** Implicit handling of data‑shift (assume iid); **Remedy:** declare `ShiftClass` (or `unknown`) and gate via Acceptance.
* **AP‑7** Tool or vendor tokens in normative text; **Remedy:** move to Plain‑register note; keep Tech references on CHR and CAL ids (LEX V‑4).

**Remedies:** tri‑state predicates; admissible order relations (lexi, Pareto, median, or medoid); explicit **GateCrossing** visibility through **CrossingBundle** (BridgeCard + UTS row + `CL/Φ` policy‑ids; **E.18**, **F.9**, **F.17**, **E.17**, and **A.21** where live); Domain stitched to **D.CTX + UTS** only.

