---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__006_archetypal-grounding.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:5 — Archetypal Grounding"
line_start: 68589
line_end: 68626
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

### E.4.PFR:5 - Archetypal Grounding

Tell: A hydroponic-cucumber framework edition depends on an FPF Core edition. It has a publication relation to its all-in-one publication carrier, an access relation to a grower-assistant skill pack or MCP-backed advisory route when those are built, a source relation to greenhouse-control source packs, a specialization relation where one pattern narrows an FPF authoring pattern for crop-domain use, and quality relations for evaluated pattern drafts.

Show: A local Codex process framework depends on FPF Core and on selected architecture patterns. Its baton-handoff pattern may coordinate with `E.11.PUR`, but that relation is not an instruction to perform that method. The relation record states the governed use and the direct pattern owner.

Show: A generated relation graph says pattern A "depends on" pattern B. PFR does not accept the word at face value. It asks whether the relation is recommendation, specialization, publication, edition dependency, preservation, admission, quality, or source use, then records the decided function.

Dependency and specialization example:

```text
PatternFrameworkRelationRecord@CodexProcessFramework:
  relationId: PFR-CODEX-DEP-001
  sourceRef: CodexPrelandingAttentionPattern@LocalPracticeFramework
  targetRef: FPFCorePatternSet@current
  relationFunction: Framework edition dependency
  governedUse: local process pattern uses FPF Core authoring and quality rules
  directGoverningPatternRef: E.5.3
  dependencyOrEditionEffect: local framework depends on Core; no Core reverse dependency
  blockedStrongerReading: not specialization and not instruction to perform Core patterns
  refreshOrSupersessionCondition: refresh when Core edition changes relevant authoring rules
```

Source and decision reuse example:

```text
PatternFrameworkRelationRecord@HydroponicCucumberDomain:
  relationId: PFR-HC-SRC-001
  sourceRef: G2-HC-nutrient-source-pack
  targetRef: HC.NutrientMonitoringPattern@draft
  relationFunction: Source or decision reuse
  governedUse: pattern solution uses source-pack claim sheet by value for nutrient-monitoring guidance
  directGoverningPatternRef: G.2
  preservationOrAdmissionRef: C.33-source-pack-summary-loss-note
  blockedStrongerReading: not framework edition dependency, not specialization, not publication relation
  sourceReturnCondition: return to G.2 when the source pack drops a rival horticulture tradition
```

