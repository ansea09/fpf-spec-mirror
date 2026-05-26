---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__001_intro.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:intro — Intro"
line_start: 42187
line_end: 42194
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

**Purpose.** Give FPF an **admissible, minimal, and portable** way to type a problem for downstream selector-facing use after the problem-side representation is stable enough for Principles-to-Work, eligibility, acceptance, or policy-governed choice. `C.22.2`-governed use carries the first problem-framing record for a messy signal; `C.22`-governed use attaches the stabilized problem to CHR-grounded traits and a minimal `TaskSignature (S2)` record for downstream selector-facing use. The `TaskSignature` attachment is **Context-local**, evidence-anchored, tri-state-aware, and bridge-visible. TaskSignature is *minimal* but sufficient for **eligibility**, **acceptance**, and **policy-governed** choice.

**Status & placement.** Part C (Kernel Extensions Specifications) → Cluster C.I (Core CHRs/CALs).
**Depends on:** **C.16 MM‑CHR** (measurement admissibility), **G.5** (selector S2/S3), **G.0** (CG‑Spec invariants).
**Coordinates with:** **G.4** (Acceptance and Evidence profiles), **C.23** (MethodFamily admissibility and maturity), **C.18 NQD‑CAL** (QD and illumination), **C.19 E/E‑LOG** (emitters and policies), **E.10** (LEX).

