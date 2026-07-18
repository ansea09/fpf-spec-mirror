---
chunk_kind: "child"
pattern_id: "C.30.AD"
pattern_title: "Architecture Description Adequacy"
section_id: "C.30.AD:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD/C.30.AD__002_use-this-when.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.30.AD — Architecture Description Adequacy"
  - "C.30.AD:0 — Use this when"
line_start: 56630
line_end: 56679
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.5"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.3.NAR"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD.BA"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "G.5"
keywords:
  - "ArchitectureDescription@Context"
  - "architecture description"
  - "architecture description use card"
  - "architecture structural view"
  - "candidate-description boundary"
  - "correspondence"
  - "source return"
  - "specification-use boundary"
  - "viewpoint"
---

### C.30.AD:0 - Use this when

Use this pattern when an architecture description is the current EntityOfConcern: a durable description, multi-view description set, architecture documentation set, model set, generated architecture relation graph, view set, or specification-use record over one `ArchitectureOf@Context`.

Use `C.30.AD` when the practitioner needs to know:

- which `ArchitectureOf@Context` claim the description is about;
- which selected structures or architecture structure kinds are described;
- which views are used under which viewpoints;
- which correspondences, source returns, freshness boundaries, or specification-use boundaries make the description usable;
- what the description can guide and which uses are non-admissible.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, or architecture model starts acting as architecture, proof, gate, assurance, decision, work authorization, or release authorization by presentation alone.

**What this buys.** The practitioner can keep one architecture description inspectable across views, viewpoints, selected structures, correspondences, publications, source returns, and direct governing-pattern applications.

**First useful description-use output.** Write one `ArchitectureDescriptionUseCard@Project`:

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
  firstGoverningPatternApplication?:
```

`@Project` guard: in this card name, `@Project` marks a project-side use card for first-pass triage or specification-use control. It is not `U.Project`, not a bounded context, not project authority, and not a part-whole relation. If one of those claims is current, use the governing project, context, authority, or part-whole pattern named by value.

The use card is a controlled first-pass slice. It can close ordinary use only when it names one architecture claim, one usable description purpose, the selected structures or structure kinds being described, viewpoint refs being used, admissible use, non-admissible use, and one remaining architecture candidate use or direct governing-pattern application. Expand to the fuller `ArchitectureDescription@Context` record when cross-view correspondence, reuse, source return, freshness, specification use, regulated use, comparison, or project-side authority use is being made.

**Not this pattern when.**

- If the current use is a grounded architecture claim or one first architecture question, use `C.30`.
- If the current use is a selected structure or structural description outside architecture, use `A.22`.
- If the current use is one architecture structural view, use `C.30.ASV`.
- If the current use is built-asset architecture-description, BIM, IFC, asset-information, digital-twin, or reference-designation specialization, use `C.30.AD.BA`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the current use is only a publication face, publication form, report, dashboard, file, or source-current relation, use `C.2.P`, `E.17`, or the publication or source pattern governing the claim.
- If the description is being used as pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, decision, work authorization, causal-use claim, release authorization, deontic permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and apply the direct pattern governing that claim to the claim being made.

