---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__006_archetypal-grounding.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:5 — Archetypal Grounding"
line_start: 63982
line_end: 64015
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
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:5 - Archetypal Grounding

Tell: A team wants a hydroponic-cucumber domain principle framework. The PFAD decision asks whether the framework depends directly on FPF Core only, or also on an agriculture-domain framework edition; which crop-growth concerns become first patterns; which source packs are strong enough; and which local monolith or publication unit will expose the framework.

Show: A Codex local practice framework has process patterns for baton handoff and prelanding checks. The decision records that these are local practice framework patterns, not FPF Core patterns. It names the FPF Core edition, selected local process patterns, local publication unit, source-return owners, and refresh conditions.

Show: An ADR-like file saying "accepted: create domain framework" is insufficient. The decision relation must name selected pattern set, dependencies, source basis, rejected alternatives, consequences, and repair conditions before the ADR-like carrier can be trusted as a projection.

Filled decision slice:

```text
PrincipleFrameworkArchitectureDecision@HydroponicCucumberDomain:
  frameworkDecisionId: PFAD-HC-001
  governedFrameworkRef: HydroponicCucumberPrincipleFramework@GreenhouseCropDomain
  boundedContextRef: commercial greenhouse cucumber production
  frameworkEditionRef: HC-DPF-0.1-draft
  fpfCoreEditionRef: FPFCorePatternSet@current
  decisionQuestion: Which first pattern set and relation structure should carry crop-growth architecturing guidance?
  sourceBasisRefs: G2-HC-source-pack, greenhouse-control source notes, accepted FPF ecosystem DRR
  namingDecisionRefs: F18-HC-framework-name-card-required
  selectedPatternSetRefs: problem-framing, nutrient-monitoring, climate-control interpretation, harvest-feedback patterns
  selectedPatternRelationRefs: PFR-HC-source-reuse, PFR-HC-specialization, PFR-HC-publication
  publicationUnitRefs: HC-local-monolith-readme-and-toc
  dependencyAndEditionRefs: depends on FPFCorePatternSet@current; no Core reverse dependency
  qualityEvaluationRefs: E21-HC-first-pattern-evaluation
  admissionReviewRefs: none until admission is claimed
  rejectedAlternatives: land into FPF-Spec.md; publish only a crop checklist
  rationaleRefs: source-pack claim sheet and E.4 family map
  consequences: faster domain guidance; explicit refresh debt when sources or Core edition change
  localMonolithLandingRefs: HC-local-monolith-draft
  sourceReturnConditions: return to G.2 when source pack loses a rival horticulture tradition
  refreshOrSupersessionConditions: G.11 refresh when Core edition or greenhouse practice changes
```

