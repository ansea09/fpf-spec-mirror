---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF (LEX‑BUNDLE)"
section_id: "E.10:15"
section_title: "Closing notes (governance & purity)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__020_closing-notes-governance-purity.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF (LEX‑BUNDLE)"
  - "E.10:15 — Closing notes (governance & purity)"
line_start: 51257
line_end: 51268
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

### E.10:15 - Closing notes *(governance & purity)*

* **Notation‑agnostic.** ULR is a **language constitution**, not a scanner or template. Apply it in prose, sketches, or formal models.
* **Where checks live.** Convenience checks belong to Tooling; ULR itself stays notation‑agnostic. Conformance code lives in **SCR‑LEX / RSCR‑LEX** as referenced above.
* **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance:
  `LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)` (§ 7.5).
* **Guards honoured.** DevOps Lexical Firewall and Unidirectional Dependency remain intact.
* **Reserved “plane”.** Only **`CHR:ReferencePlane`** uses the bare word *plane*; I/D/S are **layers**; all other category talk is expressed as **Characteristics** in a **CharacteristicSpace**.

> **One‑line memory:** *“ULR keeps words honest so ideas stay composable.”*


