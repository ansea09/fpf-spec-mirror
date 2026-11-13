---
chunk_kind: "child"
pattern_id: "C.27.TA"
pattern_title: "Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
section_id: "C.27.TA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.27.TA/C.27.TA__006_solution.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.27.TA — Temporal Aspect: Time Windows, Rhythm, Cadence, and Currentness"
  - "C.27.TA:4 — Solution"
line_start: 70557
line_end: 70663
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.3.4"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.18"
  - "E.24"
  - "G.11"
  - "G.9"
keywords:
  - "cadence"
  - "currentness"
  - "freshness"
  - "recovery timing"
  - "rhythm"
  - "temporal aspect"
  - "time window"
  - "validity window"
---

### C.27.TA:4 - Solution

#### C.27.TA:4.1 - Definition

A temporal-aspect claim says that an object or claim has a time-bearing or order-bearing property. Its temporal reference and extent must make that property interpretable: these may be a dated interval, a duration from an event, or a relation among recurring event types. For example, "each approval follows its corresponding review" specifies relative order without selecting a calendar window. A separate adequacy judgement under `C.27` is needed only when its answer could change the receiving use.

Typical temporal predicates and qualifiers include:

- `timeWindow`;
- `duration`;
- `latency`;
- `freshness`;
- `currentness`;
- `validityWindow`;
- `cadence`;
- `rhythm`;
- `synchronization`;
- `trajectory`;
- `recoveryTiming`;
- `stabilizationTiming`;
- `effortOverTime`;
- `inertiaOrResidue`;
- `refreshOrReopenCondition`.



#### C.27.TA:4.2 - Temporal Aspect Statement

Use this fuller statement when the receiving use needs the corresponding references or distinctions:

```text
TemporalAspectStatementClaimContent:
  entityOfConcernRef:
  aspectPredicate:
  temporalReference:
  windowOrInterval?:
  entityRulePatternCitation?:
  effectiveReferenceSchemeRef?:
  claimOrWorkScopeRef?:
  selectedStructureRef?:
  sourceOrUseBoundaryRef?:
  localUseCondition?:
  measuredReadingRef?:
  directRelationDeclarationRef?:
  obtainingRelationOccurrenceRef?:
  receivingUseRulePatternCitation?:
  validityOrCurrentnessCondition?:
  refreshOrReopenCondition?:
  blockedLocalOverread?:
```

When the statement is materialized, its claim content belongs to a `C.2.1` episteme. `entityOfConcernRef` resolves the bearer or claim being qualified; `aspectPredicate` states the property; `temporalReference` supplies the clock, event order or other timing basis. Include `windowOrInterval` when the claim is restricted to that extent or its interpretation requires one. Preserve any interval already asserted by the claim.

Add the remaining fields only when their values change the claim or receiving action. PatternID citations identify applicable rules. A claim about another direct relation needs that relation's declaration; an assertion of an obtaining occurrence also needs its actual participants and conditions. Scheme, scope, Structure, source and use references retain the identity and conditions defined by their respective patterns.

#### C.27.TA:4.3 - Direct Use and Rule Citation

| Temporal use | Direct pattern or rule citation |
| --- | --- |
| positive temporal-aspect claim about an object or claim | `C.27.TA` |
| adequacy or supported use of an authored temporal claim | `C.27` |
| bounded transformation under conditions with temporal reference | `A.3.4` plus `C.27.TA` |
| state-space or transition-law model | `A.3.3` |
| planned work timing | `A.15.2` |
| dated work occurrence or trace | `A.15.1` for the occurrence; `A.10` for evidence and provenance when a claim relies on the trace |
| measurement construction for rate, duration, latency, or freshness | `C.16` and related characterization patterns |
| causal-use timing, intervention window, comparator, or follow-up interval | `C.28` |
| benchmark freshness, baseline window, comparator edition, or parity window | `G.9` |
| source currentness, evidence decay, provenance, or assurance refresh | evidence, source, provenance, assurance, and refresh patterns |



#### C.27.TA:4.4 - Rhythm, Cadence, And Synchronization

A rhythm or cadence claim needs its bearer, recurrence or ordering property and timing reference. An empirical assertion such as a weekly cadence observed during R14 also needs that observation window. A planned rule such as "run a review every Friday while this plan applies" can state its recurrence and applicability directly. Add phase, synchronization, entrainment or other cross-bearer relations when the claim depends on them.

Optional reference-bearing form:

```text
RhythmAspectClaimContent:
  entityOfConcernRef:
  aspectPredicate: rhythm | cadence | synchronization
  timingReference:
  rhythmWindowRef?:
  intervalStructure?:
  rulePatternCitation?:
  directCouplingRelationDeclarationRef?:
  obtainingCouplingOccurrenceRef?:
  validityWindowRef?:
```

The optional fields appear only when the receiving use relies on them. A PatternID citation identifies the rule used to judge a claim; it is not the coupling relation.

A plain "release cadence" or "workshop rhythm" may remain ordinary prose. It needs C.27.TA when cadence or rhythm changes transformation, work planning, benchmark, source, assurance, coordination, or claim-use decisions.

#### C.27.TA:4.5 - Currentness, Freshness, And Validity Window

A currentness or freshness claim identifies the bearer, the property asserted, and the reference time or edition for the intended use. State a validity interval when the claim promises or establishes validity over that interval. "The registry entry was current when checked on 3 June" establishes no later validity period. A source, benchmark, model, dashboard, or claim may be fresh enough for one use and stale for another.

Add a source-use boundary, currentness condition, refresh condition, or reopen condition only when the receiving use changes when that value changes. Use the direct source, evidence, benchmark, assurance, or refresh pattern for the separate provenance, parity, assurance, or refresh-work claim.

#### C.27.TA:4.6 - Recovery, Stabilization, Inertia, And Effort Over Time

For recovery, stabilization, inertia or effort over time, identify the bearer and property, then recover the relevant starting event, timing reference and duration or observation interval. State the extent supported. Use C.27 when an unresolved question about the claim's adequacy changes the receiving action; a sufficient temporal-aspect claim can finish here.

Add the disturbance or starting condition, measured reading, effort, resistance, residue, inertia relation, rule citation, or direct-relation reference when the receiving use needs that distinction.

