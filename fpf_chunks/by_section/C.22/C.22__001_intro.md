---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__001_intro.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:intro — Intro"
line_start: 41324
line_end: 41331
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

**Purpose.** Give FPF a **lawful, minimal, and portable** way to speak about “the problem we face” so that the **selector** (G.5) can legally admit/abstain without prose or guesswork. We do this by (i) **typing problems** with CHR‑grounded traits and (ii) **attaching** them to a **TaskSignature (S2)** record that downstream patterns can consume. The Standard is **Context‑local**, evidence‑anchored, tri‑state‑aware, and bridge‑savvy. TaskSignature is *minimal* but sufficient for **eligibility**, **acceptance**, and **policy‑governed** choice.

**Status & placement.** Part C (Kernel Extentions Specifications) → Cluster C.I (Core CHRs/CALs).
**Depends on:** **C.16 MM‑CHR** (measurement legality), **G.5** (selector S2/S3), **G.0** (CG‑Spec invariants).
**Coordinates with:** **G.4** (Acceptance/Evidence profiles), **C.23** (MethodFamily admissibility & maturity), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **E.10** (LEX).

