---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "SCR/RSCR Harness for Unification"
section_id: "F.15:4"
section_title: "Core idea (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__005_core-idea-didactic.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "F.15 — SCR/RSCR Harness for Unification"
  - "F.15:4 — Core idea (didactic)"
line_start: 74180
line_end: 74190
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.1-F.14"
  - "F.14"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:4 - Core idea (didactic)

The harness is a **two-part net of assertions**:

* **SCR — Static Conformance Rules.** context‑local and cross‑artefact checks that must hold **now**.
* **RSCR — Regression & Stability Rules.** Checks that must hold **across changes** (editions, rows, names).

**Registry-reference note (normative).** When an SCR/RSCR mentions `BridgeId`, policy identifiers, or edition identifiers, these are treated as **registry references**. They MUST be validated by registry presence/version checks, but MUST NOT be treated as symbols that have to appear in any `provides` list (e.g., `SignatureManifest.provides`) or be satisfied via `imports` closure, because they are not part of a signature’s exported vocabulary; they are external registry keys.

All checks are expressed as **judgement schemas** (premises ⊢ conclusion). They **never** prescribe artefact formats, roles, or workflows.

