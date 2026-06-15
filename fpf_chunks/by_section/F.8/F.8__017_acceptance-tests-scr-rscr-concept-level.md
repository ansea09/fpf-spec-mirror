---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:15"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__017_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:15 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 74624
line_end: 74640
dependencies:
  - "A.11"
  - "A.7"
  - "A.8"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.8:15.1 - Static conformance (SCR)

* **SCR‑F8‑S01 (senseFamily purity).** Every decision record names **one senseFamily**; mixed needs are split.
* **SCR‑F8‑S02 (Proper anchoring).** Every Role Description cites **one SenseCell**; **no row** is used as a assignment/enactment anchor.
* **SCR‑F8‑S03 (Row scope).** Whenever a row is reused, its **Scope** is stated and **Row CL(min) ≥ τ(scope)** holds.
* **SCR‑F8‑S04 (Alias modesty).** Aliases introduced in F.5 do **not** claim new semantics or change senseFamily.
* **SCR‑F8‑S05 (Kernel restraint).** Any new U.Type proposal includes **≥ 3 domain families** of evidence and an **irreducibility** note.

#### F.8:15.2 - Regression (RSCR)

* **RSCR‑F8‑E01 (CL drift).** If any Bridge’s CL changes, re‑evaluate dependent rows; **downgrade or split** where τ(scope) is no longer met.
* **RSCR-F8-E02 (Row overuse).** Scan examples: no case uses **Naming-only** rows to justify **Assignment-eligibility** or **Type-structure** claims.
* **RSCR‑F8‑E03 (Alias creep).** Ensure no Alias has accreted senseFamily‑specific semantics; if it has, migrate to a **row** or **Role Description**.
* **RSCR‑F8‑E04 (Kernel hygiene).** New U.Type proposals are rejected if a **SenseCell + row** construction suffices.

