---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet (UTS)"
section_id: "F.17:7"
section_title: "Block Plan (didactic grouping)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__008_block-plan-didactic-grouping.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "F.17 — Unified Term Sheet (UTS)"
  - "F.17:7 — Block Plan (didactic grouping)"
line_start: 74782
line_end: 74794
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.15"
  - "A.7"
  - "A.8"
  - "E.10"
  - "E.10.D1"
  - "E.10.P"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:7 - Block Plan (didactic grouping)

A UTS **MUST** declare a **Block Plan**—the sequence of blocks that group rows. Blocks are **thread‑specific**. Example **Block Plan** for *Role Assignment & Enactment* (matches your earlier tables):

* **Block A - Context & Roles** — `U.BoundedContext`, `U.Role`, `U.RoleAssignment`, `U.Capability`.
* **Block B - Method & Description** — `U.Method`, `U.MethodDescription`, Access/Acceptance descriptions (fields of `U.PromiseContent`).
* **Block C - Execution & Schedule** — `U.Work`, `U.WorkDescription`, `U.Observation`.
* **Block D - Service & Deontics** — `U.PromiseContent`, `U.SpeechAct`, `U.Commitment`, `U.PromiseContent`, `U.PromiseFulfillmentEvaluation`.
* **Block E - Carriers & Bridges** — `U.Carrier`, *Alignment (Bridge entry)*.
* **Block R - Knowledge Units & Statuses** — `U.Episteme`, `U.EvidenceRole`, `U.StandardStatus`, `U.RequirementStatus`, `U.DefinitionRole`, `U.AxiomaticCoreRole`.

> **Rule.** Block names are **didactic**, not ontological. Do **not** infer mereology or subtyping from blocks.

