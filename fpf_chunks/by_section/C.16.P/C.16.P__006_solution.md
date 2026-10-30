---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Restore Precision to Characteristic and Scale Wording"
section_id: "C.16.P:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__006_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.16.P — Restore Precision to Characteristic and Scale Wording"
  - "C.16.P:4 — Solution"
line_start: 59232
line_end: 59275
dependencies:
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.6.P"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
keywords:
---

### C.16.P:4 - Solution

Rewrite the claim so the reader can recover its subject, the relevant characterization or comparison, its basis and the use it supports. Keep necessary applicability and stop conditions.

When the receiving work needs a separate inspectable note, the following scaffold can retain the repair. Include only fields relevant to that claim:

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
  indicatorRelationDisposition?: direct-relation | ordinary-indicator-wording | missing-governor
  comparisonReferenceOrComparatorSet?:
  thresholdRuleOrReference?:
  proxyDistortionRisk?:
  relationFunctionClaimRef?:
  repairedWordingOrDemotion:
  admissibleUse:
  nonAdmissibleUse?:
  remainingReaderUse:
  disposition:
```

A local rewrite is sufficient when the sentence conveys the needed meaning and conditions. An ordinary PatternID can locate the governing rule. Include `relationFunctionClaimRef` only when the use depends on the identity of its defining or constraining ClaimGraph. Include `indicatorRelationDisposition` when an indicator or proxy relation is under repair, following §4.1. An explanatory `nonAdmissibleUse` guard is optional under F.19:4's independent-ground, plausible-reader, contribution and smallest-clear-correction test; its absence needs no entry.

#### C.16.P:4.1 - Recovery sequence

1. **Read the trigger in its sentence.** Recover the complete assertion. Retain the source wording when the repair needs an inspectable comparison.
2. **Recover the bearer.** Name the subject being characterized. For a relational Characteristic, retain the tuple required by its definition.
3. **Recover the construction.** Use §5 to identify what the wording means. A trigger can be ordinary prose; its appearance does not create an FPF kind.
4. **Use a recovered subject rule directly.** Once the construction is clear, apply its subject pattern from §6 or the relevant domain practice.
5. **Repair what remains hidden.** Recover the contributions needed by this claim: for a measurement, its Characteristic, Scale and interpretation; for a comparison, its reference or comparator set; for a threshold, its predicate and applicability; for an indicator, the indicated property or claim and the direct relation, including distortion risk when it is a proxy. Keep necessary use and stop conditions. If an indicator relation is required but no governing rule can state or test it, return `missing-governor` rather than storing an `indicatorRole` label. Use A.6.RCD:0.1 to distinguish that absent rule from missing case facts or a failed positive test. Add explanatory non-use guards only under the F.19:4 test.
6. **Separate further claims.** A measurement or score may contribute to evidence, a decision or another use. Apply the governing conditions for that additional claim; repairing the characterization alone does not establish it.
7. **Return a useful statement.** Say what the reader can now recognize, compare or conclude, or which missing contribution leaves the claim unresolved. Type-correct wording with no useful interpretation is insufficient.

