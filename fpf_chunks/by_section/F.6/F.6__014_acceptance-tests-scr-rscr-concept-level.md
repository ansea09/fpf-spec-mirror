---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "Role Assignment & Enactment Cycle (Six-Step)"
section_id: "F.6:13"
section_title: "Acceptance tests (SCR/RSCR — concept‑level)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__014_acceptance-tests-scr-rscr-concept-level.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "F.6 — Role Assignment & Enactment Cycle (Six-Step)"
  - "F.6:13 — Acceptance tests (SCR/RSCR — concept‑level)"
line_start: 74022
line_end: 74040
dependencies:
  - "A.15"
  - "A.2.1"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.RoleAssignment"
keywords:
  - "asserting status"
  - "conceptual moves"
  - "enactment"
  - "role assignment"
---

### F.6:13 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.6:13.1 - Static conformance (SCR)

* **SCR-F6-S01 (Local address).** Every assignment/status claim states `address(τ)=σ` where `σ` is a **SenseCell** (per F.3); no bare labels.
* **SCR‑F6‑S02 (SenseFamily clarity).** Each claim is typed **Role** or **Status**, never both; subjects are of the correct kind. Claim records both **senseFamily** and **stance** explicitly or by inheritance.
* **SCR‑F6‑S03 (Stance compatibility).** `stance(Context)` and `stance(τ)` are compatible by `DesignRunTag`.
* **SCR‑F6‑S04 (Eligibility first).** For each claim, `eligible(H, τ@context)` is derivable prior to assertion.
* **SCR‑F6‑S05 (Window explicit).** Each claim has a Window (explicit or inherited) consistent with stance.
* **SCR‑F6‑S06 (Evidence‑ability).** For each claim, an **evidence shape Σ(Context)** is stated using only that Context’s vocabulary plus KD‑CAL/MM‑CHR primitives.
* **SCR‑F6‑S07 (Locality guard).** No Cross‑context terms appear inside a claim; any reference to other Contexts is flagged as **F.9 Bridge (informative)**, not used to justify the claim.

#### F.6:13.2 - Regression (RSCR)

* **RSCR‑F6‑E01 (Edition stability).** Adding a new edition/Context does not mutate existing claims’ Contexts or Windows.
* **RSCR‑F6‑E02 (Name stability).** Changing labels per F.5 leaves addresses and conclusions invariant.
* **RSCR‑F6‑E03 (Bridge neutrality).** Introducing or revising an **F.9 Bridge** does not auto‑flip claim truth values; at most it enables explicit translations with loss notes.
* **RSCR‑F6‑E04 (Evidence refresh).** When KD‑CAL procedures or **MM‑CHR characteristic scales** change, only **γ** is re‑evaluated; the claim’s semantics remain.

