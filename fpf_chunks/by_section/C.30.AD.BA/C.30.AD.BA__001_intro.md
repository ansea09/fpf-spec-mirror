---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__001_intro.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:intro — Intro"
line_start: 59685
line_end: 59702
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.PUB"
  - "F.18"
keywords:
---

## C.30.AD.BA - Built-Asset Architecture Description and Reference Designation

> **Type:** Architecture-description subpattern under `C.30.AD`
> **Status:** Stable
> **Normativity:** Normative for built-asset architecture-description, asset-information, digital-twin, and reference-designation use.

**Builds on.** `C.30`, `C.30.AD`, `C.30.ASV`, `A.1`, `A.22`, `E.17`, `E.17.0`, `E.17.1`, `E.17.2`, `E.24.PUB`, and `A.7`.

**Coordinates with.** `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.29`, `C.16`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, `C.27`, and `F.18`.

**Use this when.** Use this pattern when a BIM model, IFC exchange, asset register, dashboard, digital-twin view, handover table, maintenance information set, cost or energy view, or ISO/IEC 81346-style reference designation is used as an architecture description for a built asset.

**Not this pattern when.** If the current question is the architecture claim itself, use `C.30`. If the current question is the general architecture-description mechanism, use `C.30.AD`. If the current question is one structural view, use `C.30.ASV`. If the current question is selected structure as such, use `A.22`. If the current claim is evidence, assurance, decision, causal use, work, or gate passage, keep this pattern only for the built-asset description boundary and use the direct governing pattern.

**What goes wrong if missed.** A BIM model, asset register, dashboard, digital-twin view, or reference designation starts acting as the built asset, architecture, evidence, assurance, gate, work, or decision.

**What this buys.** Built-asset descriptions remain usable while the asset, architecture claim, views, designations, publications, source relations, and currentness boundaries stay separate.

