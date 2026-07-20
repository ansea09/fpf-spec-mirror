---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__005_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:4 — Solution"
line_start: 67661
line_end: 67706
dependencies:
  - "C.32.ADR"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:4 - Solution

Create one `PrincipleFrameworkArchitectureDecision@Context` relation before publishing the decision through any ADR-like carrier.

```text
PrincipleFrameworkArchitectureDecision@Context:
  frameworkDecisionId
  governedFrameworkRef
  boundedContextRef
  frameworkEditionRef
  fpfCoreEditionRef
  decisionQuestion
  sourceBasisRefs
  sotaSynthesisPackRefs?
  namingDecisionRefs
  selectedPatternSetRefs
  selectedPatternRelationRefs
  publicationUnitRefs
  accessCarrierRefs?
  dependencyAndEditionRefs
  qualityEvaluationRefs
  admissionReviewRefs
  rejectedAlternatives
  rationaleRefs
  consequences
  publicationCarrierRefs?
  sourceReturnConditions
  refreshOrSupersessionConditions
```

Fill the relation in this order:

1. State the decision question as an architecture question about the framework edition.
2. Name the bounded context, governed framework, and FPF Core edition dependency.
3. List the source basis and SoTA synthesis packs that make the decision admissible.
4. Select the pattern set and relation records, or state why the decision is not yet ready.
5. Select the publication or access carrier only after the structure being exposed is clear.
6. Record dependency and edition effects under `E.5.3` and `E.4.PFR`.
7. Record naming decisions or required `F.18` name-card work.
8. Record rejected alternatives, rationale, consequences, quality route, source-return route, and refresh or supersession conditions.
9. Publish the decision projection through `C.32.ADR` or `E.17` only after the decision relation exists.

`qualityEvaluationRefs` and `admissionReviewRefs` are distinct reference families. `qualityEvaluationRefs` point to `E.4.DPF.DA` package adequacy, `E.21` pattern-quality evaluation, or `E.23` improvement evidence. `admissionReviewRefs` point to `E.19` only when the decision is being used to claim admission, profile gating, external-review readiness, or landing readiness.

Demotion condition: if no framework-specific slots are live, do not keep this pattern in play. Use `E.9` for rationale, `C.32.PAD` for project architecture decision structure, and `C.32.ADR` for the publication projection.

