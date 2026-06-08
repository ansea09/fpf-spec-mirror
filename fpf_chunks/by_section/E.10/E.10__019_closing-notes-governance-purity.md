---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:15"
section_title: "Closing notes (governance & purity)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__019_closing-notes-governance-purity.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:15 — Closing notes (governance & purity)"
line_start: 60122
line_end: 60132
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.6.P"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.P"
  - "E.22"
  - "E.23"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
  - "U.Types"
keywords:
---

### E.10:15 - Closing notes *(governance & purity)*

* **Notation‑agnostic.** ULR is a **language constitution**, not a scanner or template. Apply it in prose, sketches, or formal models.
* **Where checks live.** Convenience checks belong to Tooling; ULR itself stays notation‑agnostic. Conformance code lives in **SCR‑LEX / RSCR‑LEX** as referenced above.
* **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance:
  `LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)` (§ 7.5).
* **Guards honoured.** DevOps Lexical Firewall and Unidirectional Dependency remain intact.
* **Reserved “plane”.** Only **`CHR:ReferencePlane`** uses the bare word *plane*. E.10.D2 is the EntityOfConcern and Description-episteme boundary plus specification-use gates, with publication lanes kept separate; all other category talk is expressed as **Characteristics** in a **CharacteristicSpace** when scale semantics are declared.

> **One‑line memory:** *“ULR keeps words honest so ideas stay composable.”*

