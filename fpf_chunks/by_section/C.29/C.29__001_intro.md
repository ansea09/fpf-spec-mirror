---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__001_intro.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:intro — Intro"
line_start: 58098
line_end: 58115
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18.1"
  - "C.19.1"
  - "C.2.P"
  - "C.26"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.31.ASAP"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.19"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
  - "LensUseBoundaryValue"
  - "coarse-graining"
  - "invariants"
  - "learned lens"
  - "lens mapping mode"
  - "lost structure"
  - "mathematical lens"
  - "ontology smuggling"
  - "preserved structure"
  - "rival lens"
  - "scale window"
  - "stop condition"
  - "structure-preserving representation"
  - "validation boundary"
---

## C.29 - Mathematical Lens Use

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Mathematical lens use.

**Primary EntityOfConcern.** The use of a mathematical representation to answer a stated working question, with an explicit correspondence to the phenomenon and limits on the resulting inference.

**Use this when.** Use C.29 when choosing or transferring a mathematical representation could expose a needed relation, invariant, obstruction, approximation or resource limit, or when an existing representation is being relied on beyond what its correspondence supports.

**What goes wrong if missed.** The reader either misses a useful mathematical construction or carries a result into a situation where a needed assumption or distinction has been lost.

**What this buys.** A concrete mathematical question, a representation that makes it tractable, and a consequence that changes what to calculate, observe, compare or rule out.

**Not this pattern when.** An adequate local equation, algorithm or domain model already answers the question and no separate representation or transfer issue remains. Complete that work without a C.29 note. A one-off metaphor used only for orientation also needs no card.

