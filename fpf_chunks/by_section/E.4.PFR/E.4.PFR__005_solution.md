---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__005_solution.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:4 — Solution"
line_start: 69710
line_end: 69773
dependencies:
  - "A.10"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4.PFR:4 - Solution

Record relation claims through explicit relation records before using them for architecture, publication, dependency, or quality work.

```text
PatternFrameworkRelationRecord@Context:
  relationId
  sourceRef
  targetRef
  relationFunction
  governedUse
  directGoverningPatternRef
  dependencyOrEditionEffect?
  preservationOrAdmissionRef?
  blockedStrongerReading
  sourceReturnCondition?
  refreshOrSupersessionCondition?

FrameworkEditionDependencyRecord@Context:
  frameworkEditionRef
  dependsOnEditionRefs
  dependencyReason
  compatibilityBoundary
  deprecationOrSupersessionRefs?
  refreshConditionRefs?
  e53ConformanceNote

FrameworkPackageManifest@Context:
  frameworkEditionRef
  selectedPatternSetPublicationRef
  relationRecordRefs
  dependencyAndEditionRecordRefs
  editionStatus
  deprecationOrSupersessionRefs?
  sourcePackRefs
  qualityEvidenceRefs
  refreshPlanOrCurrentnessRefs
  firstEntryCarrierRefs
  blockedRuntimeOrBuildReading
```

Use relation functions by what they do:

| Relation function | Admissible use | Owner |
| --- | --- | --- |
| Pattern-use recommendation | Selects or sequences a pattern use for a concern. | `E.11.PUR` |
| Governing-pattern relation | Says which pattern owns a claim, relation, value, boundary, or publication form. | Direct governing pattern |
| Specialization | Narrows a parent pattern's EntityOfConcern, use, or publication form with inherited and changed obligations. | Parent pattern and `E.8` |
| Architecture decision link | Connects a decision relation to selected framework structures and consequences. | `E.4.PFAD`, `C.32.PAD` |
| Publication relation | Exposes selected content through all-in-one carrier, readme, preface, card, view, or table of contents. | `E.11`, `E.17` |
| Access relation | Exposes selected framework content or pattern-use routes through a skill pack, MCP-backed access service, retrieval route, or assistant integration with edition, bounded use, and blocked runtime/build overread. | `E.11`, `E.17`, with `C.35`, `A.15`, `A.10`, `B.3`, `E.9`, or `G.11` when generated output, work/tool action, evidence, assurance, decision, or currentness claims are live. |
| Framework edition dependency | Declares reliance on a more stable framework edition with compatibility and refresh conditions. | `E.5.3`, `G.11` |
| Preservation relation | Claims that one carrier, edition, profile, or projection preserves selected structure for a licensed use. | `C.34`, with `C.33` when loss is local to one carrier |
| Produced-carrier admission | Allows generated, searched, mined, or transformed carriers to seed framework work under declared conditions. | `C.35` |
| Quality framing, evaluation, or improvement | Frames the evaluation question, evaluates FPF-level adequacy, one DPF package, or one pattern, or records repeated improvement. | `E.22` for framing, `E.2.DA` for whole-FPF adequacy, `E.4.DPF.DA` for DPF package adequacy, `E.21` for individual pattern quality, `E.23` for improvement |
| Selected-set publication | Publishes a selected set with scope and selection conditions. | `G.5` |
| Source or decision reuse | Uses a source line, SoTA pack, `DRR`, accepted decision, or evidence/source claim by value for a bounded relation use. | `G.2` for source packs and SoTA, `E.9` for accepted DRR or decision rationale, `A.10` when an evidence or currentness claim is made |

Apply the edition rule: domain and local frameworks depend toward more stable editions. A local practice framework may depend on a domain principle framework and FPF Core. A domain principle framework may depend on FPF Core. FPF itself as a First Principles Framework edition is handled through `E.4.FPF`; FPF Core does not depend on domain or local frameworks except through a deliberate Core amendment.

Use compatibility practice narrowly: state compatibility boundary, dependency impact, deprecation, supersession, and refresh conditions. Do not import software build or performed-work semantics into pattern relations.

Use `FrameworkPackageManifest@Context` only when authors need one package-like index for a domain principle framework or local practice framework. For the form of FPF itself, use `E.4.FPF` and its `FPFFormMap`; do not force FPF into the DPF/local manifest shape. The manifest lists the selected pattern set publication, access carriers, relation records, dependency pins, edition status, deprecation or supersession refs, source-pack pins, quality evidence, refresh plan, and first-entry carrier. Listing a skill package, MCP endpoint, API route, or assistant integration records a framework access route only; it does not create imports, APIs, runtime dependencies, build semantics, module calls, tool permission, or authority over pattern-use relations. If the selected pattern set itself is being published, use `G.5`; if currentness is being planned, use `G.11`; if the manifest is used as architecture evidence, use `C.33` or `C.34` for captured and lost structure.

