---
chunk_kind: "child"
pattern_id: "C.36.P"
pattern_title: "Cultural-Evolution Wording-Use Precision Restoration"
section_id: "C.36.P:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36.P/C.36.P__002_use-this-when.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "C.36.P — Cultural-Evolution Wording-Use Precision Restoration"
  - "C.36.P:0 — Use This When"
line_start: 68191
line_end: 68223
dependencies:
  - "A.1"
  - "A.15"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.2.5"
  - "B.2.P"
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
  - "C.30.ILC"
  - "C.36"
  - "D.2"
  - "D.3"
  - "D.4"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18.1"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
---

### C.36.P:0 - Use This When

Use this pattern when source or project prose uses cultural-evolution wording and the FPF object under concern is still hidden.

Trigger words include culture, cultural evolution, style, tradition, genre, scene, technique, practice, platform, platform regime, measurement regime, attractor, developmental machinery, lineage, canon, school, and close local labels.

#### C.36.P:0.1 - What Goes Wrong If Missed

The repair becomes a synonym swap. `Style` becomes `method`, `platform regime` becomes `context`, `practice` becomes a generic process label, or `attractor` becomes `dynamics` before the sentence says which FPF value, relation, claim, or bridge is current. The result looks cleaner but still carries an accidental ontology.

#### C.36.P:0.2 - What This Buys

The practitioner records one recovery line: current wording, recovered object or relation, applicable pattern, admissible use, blocked use, and next use. Use `C.36` for cultural-evolution case work. For a method, Work, discipline, bridge, archive, pool, selected-set result declaration, publication, architecture, dynamics, measurement, choice, or refresh claim, use the pattern that defines and tests that claim.

#### C.36.P:0.3 - First Useful Move

Write one `CulturalEvolutionWordingRecoveryLine@Context`.

```text
CulturalEvolutionWordingRecoveryLine@Context:
  triggerSpan:
  sourceOrProjectContext:
  recoveredCurrentObject:
  recoveredRelationOrSlot:
  subjectPatternLocator:
  retainedSourceLabelUse:
  admissibleUse:
  blockedUse:
  nextUse:
```

If `recoveredCurrentObject`, `recoveredRelationOrSlot`, or `subjectPatternLocator` cannot be filled, keep the label as quoted source wording, ordinary prose, or a blocked-use cue. Do not repair it by choosing a smoother umbrella word.

