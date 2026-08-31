---
chunk_kind: "child"
pattern_id: "C.36"
pattern_title: "Cultural Evolution and Cultural-Evolution Engineering"
section_id: "C.36:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36/C.36__002_problem-frame.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "C.36 — Cultural Evolution and Cultural-Evolution Engineering"
  - "C.36:1 — Problem frame"
line_start: 67276
line_end: 67332
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.6"
  - "A.15.PROD"
  - "A.2.1"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
  - "A.6.1"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.20"
  - "C.23"
  - "C.27"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.35"
  - "C.36.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.18"
  - "E.18.1"
  - "F.17"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
---

### C.36:1 - Problem frame

Use this pattern when the current project question is about how a culture, style, tradition, discipline practice, method family, work family, canon, recognition regime, selection regime, or mediating system changes and can be deliberately influenced.

Typical first-use situations:

- an engineering group treats its product family, toolchain, platform family, research program, or AI-agent framework as an evolving set of variants rather than one fixed system;
- a scientific, medical, pedagogical, engineering, music, dance, organizational, or AI-agent discipline is changing through related methods, work products, training forms, memory epistemes, recognition regimes, and selected variants;
- a music or dance steward needs to compare style, genre, technique, scene, canon, platform, or tradition labels without assuming that the label names one root kind;
- a project lead wants to influence the evolving practice—for example by changing how variants are generated, transmitted, recognized, selected, remembered, measured, or refreshed, or by changing a Method family, Work family, assignment, mediating architecture, or performed intervention.

#### C.36:1.1 - What goes wrong if missed

The team treats culture as shared vocabulary, treats style as a genre tree, treats a platform as the cultural object, treats a QD archive as the decision, or treats one scalar popularity or quality score as cultural development. The project can then generate many variants but still lose the relations that make those variants transmissible, recognizable, selectable, retained, refreshed, or turned into work.

#### C.36:1.2 - What this buys

The practitioner gets one small statement of what is changing, which relations transmit, recognize, select, retain, or mediate variants, what intervention is current, and what to do next. Add collective holons, local system-role kinds, classifications, assignments, Work and Method families, canon or memory epistemes, architectures, measurements, and refresh relations only when the current claim actually needs them.

#### C.36:1.3 - First useful move

Start with one ordinary sentence. For example: `In this dance school, teachers transmit variants through teaching, the festival archive retains and presents records of variants, jury recognition and peer copying select variants, and the current intervention changes how new variants enter the syllabus.` Add the next pattern only when its definition or test changes the action.

When the result must be retained or handed on, use a small card:

```text
CulturalEvolutionCaseCard@Context:
  CaseRef:
  CaseScopeOrModelUseBoundary:
  CollectiveHolonOrDisciplineScope:
  VariantRefsOrDescription:
  TransmissionRecognitionSelectionOrMemoryRelations:
  MediationOrMeasurementRefs?:
  PublicationRefs?:
  CurrentEvolutionaryQuestion:
  ApplicablePatternRefs?:
  NextActionOrStop:
```

`@Context` is part of the card's retrieval name; it names no universal Context. `CaseScopeOrModelUseBoundary` names the actual project, discipline, scene, product-family, publication, or model-use boundary. This boundary stops a local trend from becoming the whole culture merely by wording. `PublicationRefs` is optional: when a publication distinction matters, name only the exact E.17 source-backed face or exact E.24.PUB publication occurrence, publication form, presentation carrier, audience-declaration episteme, bounded-use-declaration episteme, or availability claim needed by this case. The card does not require a complete publication record. Actual access, reliance, use, and Work stay outside this field unless their own direct relations or occurrences are separately current.

Variants may be generated, retained, inherited, or observed. An archive or front claim still uses C.18 or C.19.

Expand the card only when later use needs more detail. Possible additions include direct participation or position relations; local system-role kinds, separate System-classification judgments, assignment species and obtaining occurrences; Work and Method families; Method relation structures and descriptions; canon or memory epistemes; recognition and selection regimes; mediation systems or architectures; characteristic spaces; style or tradition term rows; publication relations; measurement; and refresh. Each addition identifies its own object or obtaining relation; the card creates none of them.

The card is optional. It is not a root U-kind, lifecycle step, evidence, decision, publication authority, or substitute for the patterns that define or test its referenced claims.

#### C.36:1.4 - Working scope

Many current projects no longer develop one isolated object. They shape evolving sets, for example product families, methods, research directions, medical and pedagogical practices, AI-agent frameworks, artistic styles, engineering traditions, canons, archives, frontiers, and recognition regimes. The project often generates variants cheaply, while the hard work shifts to the relations that determine what is produced, recognized, retained, selected, used, changed, or kept current. That work can include, for example, problem production, characterization, archive stewardship, comparison, selected-set result declaration, actual publication, local choice, performed Work, effect measurement, and refresh.

Cultural evolution is current when the question is how a collective or discipline generates, transmits, recognizes, selects, retains, or changes variants. Memory or canon epistemes, recognition and selection relations, comparison, platform or algorithmic mediation, and changing Method families may all matter.

When the case says that Work was performed, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work occurrence and enacted Method. Add A.2.1 and F.6 only when the case or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the Work intact. A local system-role kind, classification judgment, assignment species, assignment occurrence, Work occurrence, Method, effect claim, responsibility relation, and family description remain separate.

This pattern gives FPF a first-use cultural-evolution case without adding a new top-level part or a root ontology of culture. The same pattern can serve engineering product families, scientific research programs, medical disciplines, pedagogy, music styles, dance styles, organizational cultures, and AI-agent framework evolution because it begins with existing FPF objects and relations rather than domain labels.

