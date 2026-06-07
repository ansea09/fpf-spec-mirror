---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:17"
section_title: "Didactic distillation (90-second script)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__019_didactic-distillation-90-second-script.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:17 — Didactic distillation (90-second script)"
line_start: 71820
line_end: 71826
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:17 - Didactic distillation (90-second script)

> A **Bridge** translates between **local senses** from different **Contexts**. It always declares **what relation** holds (`Equivalence`, `Narrower-than`, `Broader-than`, `Partial-overlap`, `Disjoint`, or an interpretation such as `Design-spec -> Run-trace`), **which CL value applies** (`CL 0-3`), **which way** (when direction matters), and **what is lost**. **Substitution** is supported only on the **same senseFamily** and only with **CL >= 2**; **Type-structure** needs **CL = 3**. **Interpretation Bridges** explain, never substitute. Rows in the Concept-Set table obey the **weakest-link**: their scope cannot exceed the lowest `CL` among their Bridges. When editions change or counter-examples appear, lower `CL` or change bridge kind; if two senses truly converge and invariants match, raise to **CL = 3**, rarely and with reasons. Translate across Contexts; never collapse them.

#### F.9:17.1 - Bridge stance overlay compatibility
A bridge card may carry a `F.9.1` Bridge Stance Overlay such as `localRename`, `operationalizes`, `partialAnalogy`, `projection`, or `nonEquivalent`. The overlay is a local interpretive annotation and **does not replace** the underlying bridge kind, direction, `CL`, or loss notes.

