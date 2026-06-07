---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:10"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__011_consequences.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:10 — Consequences"
line_start: 29226
line_end: 29241
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:10 - Consequences

**Benefits**

* **Predictable composition:** Γ‑folds are reproducible and auditable across domains.
* **Cross‑scale clarity:** Resource and time additivity are preserved by routing to Γ\_work and Γ\_time.
* **Safer modelling:** WLNK cutsets surface true constraints; emergence is not “smuggled in”.
* **Didactic simplicity:** A small, fixed edge vocabulary makes reviews and onboarding faster.

**Trade‑offs / mitigations**

* **Up‑front discipline:** Declaring boundaries and independence requires effort.
  *Mitigation:* reuse the Proof Kit templates; keep small, local graphs and compose.
* **Refactoring legacy edges:** Replacing “generic part‑of” with precise relations can be noisy.
  *Mitigation:* use the decision guide (4.4) and anti‑pattern table (9) as a script.

