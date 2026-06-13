---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__002_use-this-when.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:0 — Use this when"
line_start: 53474
line_end: 53520
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
  - "C.16.P"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.8"
  - "F.18"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:0 - Use this when

Use this pattern when an architecture description is the EntityOfConcern under repair: a durable description, multi-view description set, architecture documentation set, model set, generated architecture relation graph, view set, or specification-use record over one `ArchitectureOf@Context`.

Use `C.30.AD` when the practitioner needs to know:

- which `ArchitectureOf@Context` claim the description is about;
- which selected structures or architecture structure kinds are described;
- which views are used under which viewpoints;
- which correspondences, source returns, freshness boundaries, or specification-use boundaries make the description usable;
- what the description can guide and which uses are non-admissible.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, or architecture model starts acting as architecture, proof, gate, assurance, decision, work authority, or release permission by presentation alone.

**What this buys.** The practitioner can keep one architecture description inspectable across views, viewpoints, selected structures, correspondences, publications, source returns, and neighboring-pattern applications.

**First useful move.** Write one `ArchitectureDescriptionUseCard@Project`:

```text
ArchitectureDescriptionUseCard@Project:
  architectureClaimRef:
  describedHolonRef:
  boundedContextRef:
  descriptionPurpose:
  selectedStructureRefs:
  structureKindRefs:
  viewpointRefs:
  architectureStructuralViewRefs:
  correspondenceRefs:
  sourceReturnCondition?:
  specificationUseBoundary?:
  admissibleUse:
  nonAdmissibleUse:
  firstExactNeighborPatternApplication?:
```

The use card is a controlled first-pass slice. It can close ordinary use only when it names one architecture claim, one usable description purpose, the selected structures or structure kinds being described, viewpoint refs being used, admissible use, non-admissible use, and one remaining architecture move or neighboring-pattern application. Expand to the fuller `ArchitectureDescription@Context` record when cross-view correspondence, reuse, source return, freshness, specification use, regulated use, comparison, or project-side authority use is being made.

**Not this pattern when.**

- If the use under repair is a grounded architecture claim or one first architecture question, use `C.30`.
- If the use under repair is a selected structure or structural description outside architecture, use `A.22`.
- If the use under repair is one architecture structural view, use `C.30.ASV`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the use under repair is only a publication face, carrier, report, dashboard, file, or source-current relation, use `C.2.P`, `E.17`, or the publication or source pattern governing the claim.
- If the description is being used as evidence, assurance, gate passage, decision, work authority, causal-use claim, release permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and apply the neighboring pattern governing that claim to the claim being made.

