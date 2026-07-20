---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:21"
section_title: "Closing notes (governance and purity)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__023_closing-notes-governance-and-purity.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:21 — Closing notes (governance and purity)"
line_start: 72551
line_end: 72561
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.SPR"
  - "A.2"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6.0"
  - "A.6.5"
  - "A.6.P"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.18"
  - "F.19"
  - "F.5"
keywords:
---

### E.10:21 - Closing notes *(governance and purity)*

* **Notation-agnostic.** `E.10` is a wording-use governance pattern, not a scanner or template. Apply it in prose, sketches, or formal models.
* **Where checks belong.** Convenience checks belong to Tooling; `E.10` itself stays notation-agnostic. Conformance code belongs in **SCR-LEX** or **RSCR-LEX** as referenced above.
* **Acts and tokens.** LEX applies to **tokens**; USM applies to **acts**: mint, rename, and use. Conformance:
  `LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)` (§ 7.5).
* **Guards honoured.** DevOps Lexical Firewall and Unidirectional Dependency remain intact.
* **Reserved “plane”.** Only **`CHR:ReferencePlane`** uses the bare word *plane*. E.10.D2 is the EntityOfConcern and Description-episteme boundary plus specification-use gates, with publication faces, publication forms, `PublicationUnit`s, carriers, and renderings kept separate; all other category talk is expressed as **Characteristics** in a **CharacteristicSpace** when scale semantics are declared.

> **One-line memory:** *“E.10 keeps words honest so ideas stay composable.”*

