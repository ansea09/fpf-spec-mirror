---
chunk_kind: "child"
pattern_id: "C.22"
pattern_title: "Problem Typing & TaskSignature Assignment (Problem-CHR)"
section_id: "C.22:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22/C.22__001_intro.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR)"
  - "C.22:intro — Intro"
line_start: 47754
line_end: 47767
dependencies:
  - "A.6.0"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.1"
  - "C.22.2"
  - "C.23"
  - "C.32.P2S"
  - "E.10"
  - "E.18"
  - "G.0"
  - "G.4"
  - "G.5"
keywords:
---

## C.22 - Problem Typing & TaskSignature Assignment (Problem-CHR)
> **Status:** Stable
> **Type:** Calculus (C)

**Purpose.** Give FPF an admissible, minimal, and portable `TaskSignature@Context` declaration for selector-facing use after the problem-side representation is stable enough for Principles-to-Work, eligibility, acceptance, or policy-governed choice. `C.22.2` carries the first problem-framing episteme for a messy signal. `C.22` constructs one CHR-grounded `U.Signature` species and, when a receiving use is current, relates the exact problem-side episteme to that signature through `TaskSignatureAssignmentRelation@Context`. The signature is Context-local, evidence-relation-traceable, tri-state-aware, and bridge-visible.

**Body-level kind boundary.** `TaskSignature@Context` is a Context-local species of existing `U.Signature`, governed here and conformant to the A.6.0 four-row declaration; it is not a record format and introduces no new root U-kind. `TaskSignatureAssignmentRelation@Context` is the local `U.Relation` that assigns one such signature to one exact problem-side episteme for one receiving use. `ProblemCard@Context` is the C.22.2 problem-side episteme used before that assignment. `KindSet` contains C.3 `U.Kind` values for selected entities. Descriptor maps, telemetry hooks, policy ids, and selector fields remain local signature vocabulary or projection fields unless a direct governing pattern admits another kind.

**Primary EntityOfConcern.** The governed value in C.22 is one `TaskSignature@Context`, a Context-local `U.Signature` declaration that makes a typed task or work target usable by later eligibility, acceptance, and selector relations. `TaskSignatureAssignmentRelation@Context` is a separate dependent relation to the upstream problem-side episteme and receiving use. `TaskKind`, optional `TaskFamilyRef`, `KindSet`, characteristic bindings, and scope slices are content of the signature's four-row declaration. A later `SelectorOutcome` is a downstream result. A project-entity reference inside a scope relation identifies the entity addressed by the task; it is not the TaskSignature or its publication.

**Placement.** Part C (Kernel Extensions Specifications) -> Cluster C.I (Core CHRs and CALs).
**Depends on:** **C.16 MM-CHR** (measurement admissibility), **G.5** (selector S2 and S3), **G.0** (CG-Spec invariants).
**Coordinates with:** **G.4** (Acceptance and Evidence profiles), **C.23** (MethodFamily admissibility and maturity), **C.18 NQD‑CAL** (QD and illumination), **C.19 E/E‑LOG** (emitters and policies), **E.10** (LEX).

