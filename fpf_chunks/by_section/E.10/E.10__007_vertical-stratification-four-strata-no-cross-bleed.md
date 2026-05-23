---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:5"
section_title: "Vertical Stratification (four strata; no cross-bleed)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__007_vertical-stratification-four-strata-no-cross-bleed.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:5 — Vertical Stratification (four strata; no cross-bleed)"
line_start: 51468
line_end: 51484
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.7"
  - "B.1"
  - "B.3"
  - "E.10.SEMIO"
  - "E.5"
  - "F.18"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:5 - Vertical Stratification (four strata; no cross-bleed)

> **Rule V‑0 (Strata).** Every lexical item in a conformant text belongs to exactly one **stratum**:

1. **Kernel** — `U.*` types, kernel relations, invariants (e.g., `U.Holon`, `U.Role`, `U.Method`, `U.Work`, `U.PromiseContent`).
2. **Extension patterns** — CAL/LOG/CHR exports (e.g., **Sys‑CAL**, **KD‑CAL**, **Agency‑CHR**) that **extend** but do not override Kernel.
3. **Context** — a **`U.BoundedContext`** with its **Glossary, Invariants, Roles**, and **Bridges** (local Context of meaning).
4. **Instance** — concrete identifiers (holders, role assignments, works, carriers).

**V‑1 (Unidirectional meaning).** Meaning **flows downward** only: Kernel → Extention patterns → Context → Instance. No stratum may redefine a higher stratum’s term; it may only **specialise** or **bridge** it.

**V‑2 (Strata vs authoring stances).** The four lexical strata above constrain **tokens**. They are independent of a claim-bearing unit's **stance** (its `CtxState` pins such as `DesignRunTag`, `ReferencePlane`, and `Locus`). Strata answer “what words mean here”; stance answers “where this claim lives in the flow” and which evidence‑lane expectations apply.

**V‑3 (Citation style).** When a Context term is used, its **Context** must be visible at first mention (e.g., `OwnerRole:ITIL_2020`). If an author needs Cross‑context reuse, they **MUST** cite a **Bridge** with a stated **Congruence Level (CL)** (see F.9).

**V‑4 (Firewall).** Tooling/Pedagogy idioms shall not leak into Kernel prose (DevOps Lexical Firewall). CI/CD jargon, file formats, or API names **MUST NOT** appear in Core definitions. (Pedagogy may use them **as examples** only, in the **Plain** register, with Tech anchors present.)

