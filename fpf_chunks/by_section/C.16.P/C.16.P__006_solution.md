---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__006_solution.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:4 — Solution"
line_start: 48416
line_end: 48459
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

Minimum fields when a note is needed:

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
  indicatorRelationRef?: U.RelationRef for the selected indicated-characteristic, proxy, measurement-use, evidence-use, or other direct relation
  indicatorRelationDisposition: direct-relation | ordinary-indicator-wording | missing-governor
  comparisonReferenceOrComparatorSet?:
  thresholdRuleOrReference?:
  proxyDistortionRisk?:
  relationFunctionClaimRef:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse?:
  remainingReaderUse:
  disposition:
```

Use the full note only when the repair must remain inspectable. Use a local rewrite when one sentence clearly states the characteristic and scale construction and subject pattern. Keep necessary subject applicability or stop conditions in the repaired wording or `admissibleUse`. Include `nonAdmissibleUse` as an explanatory guard only under F.19:4's full independent-ground, plausible-reader, contribution, and smallest-clear-correction test; an unused guard needs no absence entry.

#### C.16.P:4.1 - Recovery sequence

1. **Capture the trigger.** Copy the exact word or phrase and the sentence that uses it.
2. **Recover the bearer.** Name what is being characterized: holon, pattern, design-rationale record, architecture description, structure, model, method, work result, publication, candidate, relation, decision option, evidence relation, or another subject identified by value. For a relational characteristic, retain the tuple of bearers required by its definition.
3. **Recover the construction.** Decide whether the trigger means `Characteristic`, `Scale`, coordinate, value, score, unit, scoring method, indicator, threshold, comparison reference or comparator set, proxy, Q-bundle, mathematical lens, gate, evidence, decision, or ordinary prose.
4. **Select subject pattern when possible.** If `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.29`, `E.21`, or another subject pattern is already recoverable, use it directly.
5. **Repair hidden characteristic and scale construction.** When construction is hidden, recover the minimal needed set: characteristic, scale, value set, score, unit, scoring method, indicated characteristic or claim, exact direct indicator or proxy relation, comparison reference or comparator set, threshold rule or reference, admissible use, and any necessary applicability or stop condition. Add an explanatory non-admissible-use guard only under the full F.19:4 test. If the text relies on an indicator relation but no governing rule can state or test that claim, return `missing-governor` rather than storing an `indicatorRole` label. Use `A.6.RCD:0.1` to distinguish an absent rule from missing case facts or a failed positive test.
6. **Separate adjacent claims.** Evidence, assurance, gate, work, decision, causal-use, release, benchmark, publication, or authority claims are governed by their direct patterns.
7. **State remaining reader use.** Say what the reader can now compare, measure, score, block, or assign to a neighboring pattern. If the result is type-correct but gives no action or recognition reason, the repair is incomplete.

