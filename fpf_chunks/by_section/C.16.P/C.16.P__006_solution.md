---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__006_solution.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:4 — Solution"
line_start: 42223
line_end: 42265
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.20"
  - "A.21"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
  - "G.0"
  - "G.5"
  - "G.9"
keywords:
---

### C.16.P:4 - Solution

Repair compressed characterization wording by producing a `characteristic-scale repair note` or equivalent local rewrite.

Minimum fields:

```text
CharacteristicScaleRepairNote:
  triggerSpan:
  boundedTextSpanOrPublicationUnit:
  bearer:
  candidateConstruction:
  recoveredCharacteristic?:
  recoveredScale?:
  recoveredCoordinate?:
  recoveredValue?:
  recoveredScore?:
  unit?:
  scoringMethod?:
  indicatorRole?:
  comparisonReferenceOrComparatorSet?:
  thresholdRuleOrReference?:
  proxyDistortionRisk?:
  governingPatternRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse:
  remainingReaderMove:
  disposition:
```

Use the full note only when the repair must remain inspectable. Use a local rewrite when one sentence clearly states the characteristic and scale construction and governing pattern.

#### C.16.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the exact word or phrase and the sentence that uses it.
2. **Recover the bearer.** Name what is being characterized: holon, pattern, DRR, architecture description, structure, model, method, work result, publication, candidate, relation, decision option, evidence path, or another FPF kind named by value.
3. **Recover the construction.** Decide whether the trigger means `Characteristic`, `Scale`, coordinate, value, score, unit, scoring method, indicator, threshold, comparison reference or comparator set, proxy, Q-bundle, mathematical lens, gate, evidence, decision, or ordinary prose.
4. **Select direct governing pattern when possible.** If `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another governing pattern is already recoverable, use it directly.
5. **Repair hidden characteristic and scale construction.** When construction is hidden, recover the minimal needed set: characteristic, scale, value set, score, unit, scoring method, indicator role, comparison reference or comparator set, threshold rule or reference, admissible use, and non-admissible use.
6. **Exit adjacent claims.** Evidence, assurance, gate, work, decision, causal-use, release, benchmark, publication, or authority claims go to governing patterns.
7. **State remaining reader move.** Say what the reader can now compare, measure, score, block, or assign to a neighboring pattern. If the result is type-correct but gives no action or recognition reason, the repair is incomplete.

