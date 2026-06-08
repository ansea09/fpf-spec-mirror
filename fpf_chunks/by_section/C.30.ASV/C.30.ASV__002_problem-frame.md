---
chunk_kind: "child"
pattern_id: "C.30.ASV"
pattern_title: "Architecture Structural View Adequacy (ASV)"
section_id: "C.30.ASV:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ASV/C.30.ASV__002_problem-frame.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "C.30.ASV — Architecture Structural View Adequacy (ASV)"
  - "C.30.ASV:1 — Problem frame"
line_start: 53185
line_end: 53219
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureStructureKindRef"
  - "VF.ARCH.STRUCTURE"
  - "architecture structural view"
  - "correspondence"
  - "hidden/lost structure"
  - "source return"
  - "structure kind"
  - "viewpoint bundle"
---

### C.30.ASV:1 - Problem frame

Use this pattern when an architecture discussion needs to say which selected structure is being viewed, not merely that there is a diagram, model, table, dashboard, ADR, generated relation graph, or generic "view".

The first useful move is `ArchitectureStructureKindTriage@Project`:

```text
ArchitectureStructureKindTriage@Project:
architectureClaimRef?:
describedHolonRef?:
boundedContextRef?:

architecture concern cue:
suspected wrong collapse:
practitioner prompt label:
candidate structure kinds:
smallest useful structure-kind set:
primaryGoverningPatternApplicationRef:
admissibleArchitectureMove:
governingPatternApplicationRefs:
stop condition:
```

Ordinary minimum: name the architecture claim being made or selected structure, or the described holon and bounded context when the claim is not yet recoverable, the one structure kind or structure-kind set that changes action, one non-admissible overread, and the next admissible architecture move or stop. All other fields are conditional and may be `not used`.

Start with `C.30` when the architecture claim itself is unclear. Use C.30.ASV only when a view over selected architecture-relevant structure changes the next architecture move. Use the triage record when it names the structure kind under consideration and the next admissible architecture move. Use a full `ArchitectureStructuralView@Context` only when the view changes action, selected reliance relation, correspondence, source return, publication, comparison, or another governing-pattern use.

What goes wrong if C.30.ASV is missed: "architecture" silently means "module diagram"; a view becomes a publication face; a viewpoint becomes a structure kind; TEVB is stretched into a full architecture ontology; a Transduction Graph Architecture (TGA) graph, Layered Control Architecture (LCA) control sketch, code-agent relation graph, or neural-network block diagram becomes the architecture by appearance.

What C.30.ASV buys in practice: the practitioner can name the architecture claim, selected structures, structure kind, viewpoint, selected relation kinds, selected constraints, selected invariants, operation or dynamics descriptions being used, hidden or lost structure, correspondence, source or reliance relation, source-return condition, admissible use, and non-admissible use before relying on a view.

Not this pattern when the question under repair is only the general architecture claim, structure as such, or a TGA graph relation, path relation, or crossing relation. Use `C.30`, `A.22`, `E.18`, or `C.30.TGA-FLOW-REL` as appropriate. If the view is used for another claim being made, use the governing pattern and keep C.30.ASV only to the view portion.

Thin precision-restoration pointer: if the issue under repair is still whether *view*, *architecture view*, *architecture structural view*, *diagram*, *model*, *graph*, *layer*, or *functional architecture* names a structural view, an architecture description, a publication face, a carrier, a source relation, or another governed claim or relation named by value, use `C.30.P` first. Do not copy the `C.30.P` trigger table here; apply C.30.ASV only after the architecture structural-view claim or non-ASV claim named by value is recoverable.

