---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:8"
section_title: "Invariants (normative, lightweight)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__009_invariants-normative-lightweight.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:8 — Invariants (normative, lightweight)"
line_start: 62938
line_end: 62947
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

### F.8:8 - Invariants (normative, lightweight)

1. **Context‑first.** Every decision cites at least one **Context**; no global senses.
2. **senseFamily purity.** A single decision covers **one senseFamily**. Mixed needs are split.
3. **Row honesty.** Any Cross‑context reuse occurs **via a Concept‑Set row** at or above **τ(scope)**; no stealth equivalence.
4. **Role Description anchoring.** Role Descriptions are **single-Context**, **single-cell** anchors (F.4).
5. **Alias modesty.** Aliases **never** change semantics and live under F.5.
6. **Kernel restraint.** New **U.Types** are **rare**; A.8 **(≥ 3 families)** is mandatory, and duplication with existing U.Types must be ruled out.


