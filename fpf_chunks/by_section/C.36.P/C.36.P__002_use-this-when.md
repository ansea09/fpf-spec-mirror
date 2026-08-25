---
chunk_kind: "child"
pattern_id: "C.36.P"
pattern_title: "Cultural-Evolution Wording-Use Precision Restoration"
section_id: "C.36.P:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.36.P/C.36.P__002_use-this-when.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.36.P — Cultural-Evolution Wording-Use Precision Restoration"
  - "C.36.P:0 — Use This When"
line_start: 65868
line_end: 65908
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.RCD"
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
  - "E.10.ROLE"
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

Use this pattern when source or project prose uses cultural-evolution wording and a current claim or action depends on what that wording means here. If the word is only ordinary or quoted language and no FPF claim relies on it, leave it alone.

Trigger expressions include, for example, culture, cultural evolution, style, tradition, genre, scene, technique, practice, platform, platform regime, measurement regime, attractor, developmental machinery, lineage, canon, and school. They are recognition cues, not a lexical taxonomy.

#### C.36.P:0.1 - What Goes Wrong If Missed

The repair becomes a synonym swap. `Style` becomes `method`, `platform regime` becomes `context`, `practice` becomes a generic process label, or `attractor` becomes `dynamics` before the sentence says which object, relation, or claim is current. The result looks cleaner but still carries an accidental ontology.

#### C.36.P:0.2 - What This Buys

The first result is a short ordinary statement: what the expression means in this use and which pattern supplies the next needed definition or test. For example: `Here “platform” refers to the short-video recommendation System and to the visibility and recognition relations around it. The claim is that changes in those relations altered which dance variants were copied; use C.36 for the cultural-evolution case and C.18 only if archive retention is the next question.`

Use C.36 for a cultural-evolution case. For a Method, Work, discipline, bridge, archive, pool, selected-set result declaration, publication, architecture, dynamics, measurement, choice, or refresh claim, use the pattern that defines or tests that claim.

#### C.36.P:0.3 - First Useful Move

Write the short ordinary statement first. Stop when it makes the next project action clear.

When a handoff or repeated use needs durable memory, keep the same result in this optional line:

```text
CulturalEvolutionWordingRecoveryLine:
  triggerSpan:
  wordingUse:
  sourceRef?:
  claimScope?:
  modelUseBoundary?:
  recoveredObjects?:
  recoveredRelations?:
  recoveredClaim:
  applicablePatternRefs:
  retainedSourceLabelUse?:
  admissibleUse?:
  blockedUse?:
  nextUseOrStop:
```

Fill only the fields the receiving use needs. If the object, relation, claim, or applicable rule cannot yet be recovered, keep the label as quoted source wording, ordinary prose, or a blocked-use cue. Do not choose a smoother umbrella word merely to fill the line.

