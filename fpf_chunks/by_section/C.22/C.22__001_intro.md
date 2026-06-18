---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__001_intro.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:intro — Intro"
line_start: 44248
line_end: 44258
dependencies:
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.23"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
  - "Problem‑CHR"
  - "ScopeSlice(G)"
  - "TaskKind"
  - "TaskSignature"
  - "specialization anchor"
  - "unknown handling"
---

## C.22 - Problem Typing & TaskSignature Assignment (Problem-CHR)
> **Status:** Stable

**Purpose.** Give FPF an **admissible, minimal, and portable** way to type a problem for downstream selector-facing use after the problem-side representation is stable enough for Principles-to-Work, eligibility, acceptance, or policy-governed choice. `C.22.2`-selector-facing use carries the first problem-framing record for a messy signal; `C.22`-selector-facing use attaches the stabilized problem to CHR-grounded traits and a minimal `TaskSignature (S2)` record for downstream selector-facing use. The `TaskSignature` attachment is **Context-local**, evidence-relation-traceable, tri-state-aware, and bridge-visible. TaskSignature is *minimal* but sufficient for **eligibility**, **acceptance**, and **policy-governed** choice.

**Body-level U-kind settlement.** `TaskSignature` is a context-bound typed attachment record governed by this pattern, not a durable root U-kind. `ProblemCard@Context` is the C.22.2 problem-side record used before selector-facing binding, not an ontic-context suffix and not a separate root kind. `KindSet` contains C.3 `U.Kind` values for selected entities. `DescriptorMap`, telemetry hooks, policy ids, and selector input/output fields are local record fields unless a direct governing pattern admits them. `PathSliceId` is an E.18 path-slice reference only when a transformation-flow path slice is current; otherwise it is a telemetry field id with no path ontology.

**Status & placement.** Part C (Kernel Extensions Specifications) → Cluster C.I (Core CHRs/CALs).
**Depends on:** **C.16 MM‑CHR** (measurement admissibility), **G.5** (selector S2/S3), **G.0** (CG‑Spec invariants).
**Coordinates with:** **G.4** (Acceptance and Evidence profiles), **C.23** (MethodFamily admissibility and maturity), **C.18 NQD‑CAL** (QD and illumination), **C.19 E/E‑LOG** (emitters and policies), **E.10** (LEX).

