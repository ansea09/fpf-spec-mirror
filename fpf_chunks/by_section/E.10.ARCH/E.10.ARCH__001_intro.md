---
chunk_kind: "child"
pattern_id: "E.10.ARCH"
pattern_title: "Wording-Use Ontological Precision Restoration Architecture"
section_id: "E.10.ARCH:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.ARCH/E.10.ARCH__001_intro.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.10.ARCH — Wording-Use Ontological Precision Restoration Architecture"
  - "E.10.ARCH:intro — Intro"
line_start: 72839
line_end: 72865
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.SPR"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.F"
  - "A.6.P"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.25"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.P"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.18"
  - "E.19"
  - "E.2"
  - "E.20"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
---

## E.10.ARCH - Wording-Use Ontological Precision Restoration Architecture

> **Type:** Architectural (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Wording ontology repair architecture.

**Intent.**
Keep FPF wording-use precision restoration distributed without letting every pattern of concern or subject pattern grow its own first-stage wording-recognition table. `E.10` recognizes overloaded wording use; `E.10.ARCH` says which applicability rows exist, how one row selects the first applicable restoration or governing pattern, and when repeated repair-only prose should be extracted from a subject pattern.

`E.10.ARCH` is not a generic language-cleanup pattern. Its mechanism is ontological reconstruction: recover what kind of thing is being talked about, which adjacent EntityOfConcern values, relation records, claim records, current ontic slots, relation positions, use relations, claim kinds, and FPF kinds named by value or references are admissibly involved, which relation, source-relation disposition, or state-family value is current, and, when plain ontology is not enough, which mathematical lens under `C.29` or which pattern-defined formal apparatus makes the candidate structure checkable. The output returns to wording only after that kind, position, and use structure is recoverable. When the kind is recoverable but phrase-level apparatus still hides it, use `F.19` for ontology-first plain technical rewriting.

**Use this pattern when** a recurring wording-use problem hides stable ontological recovery work that should be shared instead of copied into each subject pattern.

**What goes wrong if missed.** Subject patterns accumulate local wording-repair catalogues and stop foregrounding their own governed object, invariant, and first useful move.

**What this pattern buys.** One distribution architecture keeps recognition in `E.10`, recovery architecture in `E.10.ARCH`, and object-specific ontology in the direct governing or realization pattern.

**Rationale.** Precision restoration needs an ontology-first distribution rule because a recurring trigger word may hide different kinds, slots, relations, claims, publications, or mathematical lenses in different places.

**SoTA-Echoing.** The pattern follows FPF's current ontology-first restoration practice: typed object recovery, direct governing-pattern use when available, and thin pointers in subject patterns instead of repeated repair doctrine.

**Builds on.** `E.10`, `A.6.P`, `A.6.F`, `C.2.P`, `C.2.P.DR`, `C.30.STRAT`, `A.19.SPR`, `A.6.3.CSC`, `A.3.1`, `A.3.2`, `A.6.0`, `A.6.1`, `E.20`, `E.24`, `E.24.CD`, `E.24.PUB`, `F.18`, `E.8`, `E.19`, and `E.2`.

**Coordinates with.** `A.22`, `C.30`, `C.30.P`, `C.30.STRAT`, `C.30.ASV`, named `C.30.*` structure or view patterns, `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.27.TA`, `C.27`, `C.29`, `A.3.1`, `A.3.2`, `A.3.3`, `A.3.4`, `A.6.0`, `A.6.1`, `E.18`, `E.20`, `E.24`, `E.24.CD`, `E.24.PUB`, `A.15.2`, `A.15.1`, `A.10`, `F.19`, `E.21`, `E.11`, `I.2`, and evidence, assurance, gate, work, decision, causal-use, release, and publication patterns governing those claims when those claims are being made.

