---
chunk_kind: "child"
pattern_id: "A.1"
pattern_title: "Holonic Foundation: Entity → Holon"
section_id: "A.1:8"
section_title: "Common Anti‑Patterns and How to Avoid Them — Manager’s quick checks"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1/A.1__009_common-anti-patterns-and-how-to-avoid-them-manager-s-quick-checks.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.1 — Holonic Foundation: Entity → Holon"
  - "A.1:8 — Common Anti‑Patterns and How to Avoid Them — Manager’s quick checks"
line_start: 1243
line_end: 1251
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.14"
  - "A.2"
  - "B.1"
  - "U.Boundary"
  - "U.Episteme"
  - "U.Holon"
  - "U.System"
keywords:
  - "U.Episteme"
  - "U.System"
  - "entity"
  - "holon"
  - "part-whole composition"
  - "system boundary"
---

### A.1:8 - Common Anti‑Patterns and How to Avoid Them — Manager’s quick checks

1. **“Ports on a theory.”** Treating a proof corpus as if it had physical connectors. *Fix:* model `U.Interaction` only across **boundaries**; for epistemes, interactions are **symbolic flows** via carriers and citations (see A.10), not power or mass.
2. **“Document edited itself.”** Assigning actions to an episteme. *Fix:* actions are executed by a **system bearing a role** (A.12/A.15); epistemes are transformed **via external transformers** acting on their **symbol carriers**.
3. **“Parts everywhere.”** Forcing a part–whole onto atomic entities (e.g., prime numbers). *Fix:* if no meaningful parts exist, stay at `U.Entity`; apply Γ only to `U.Holon`.
4. **“Scope ≡ section.”** Using “scope” as a text region rather than a modeled boundary. *Fix:* define a `U.Boundary` and state what crosses it (`U.Interaction`).

> **When in doubt:** first decide **what is a holon**, then state **its boundary**, then list **what crosses**. Roles and methods come *after* (see A.2 and A.15).

