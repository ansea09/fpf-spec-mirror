---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work: Dated Performed Work Occurrence"
section_id: "A.15.1:11"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.15.1 — U.Work: Dated Performed Work Occurrence"
  - "A.15.1:11 — Common Anti-Patterns and How to Avoid Them"
line_start: 29633
line_end: 29648
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:11 - Common Anti-Patterns and How to Avoid Them

* **"The log is the performed occurrence."** Dumping telemetry without recoverable candidate-action facts—every actual performer System's A.13 basis, at least one Method actually followed, time window, and at least one obtaining local containing-system relation, plus any other relation the receiving claim uses—does not establish Work. Recover and admit the occurrence independently, keep the log as evidence, and add F.6 only afterward when precise assignment-bound attribution is current.
* **Record-handling-as-transformation.** ETL, copying, formatting, evaluation, or publication work is treated as proof that a record or dataset changed -> Keep the grounded Work occurrence, but assert actual change only after A.3.4 identifies the transformation and either a declared domain predicate with the exact Work and transformation participants obtains or a C.2.1 local compound claim under A.6.RCD disposition 2 exposes its substrate-admitted constructor, governed base predicates, actual participants, and case facts; otherwise return `missing-governor[work-to-change]`.
* **Silent cross-locality acceptance.** "Ops accepted it, so audit accepts it." -> Name the criterion and verdict for each receiving use. Assert acceptance only through that use's declared predicate and actual participants. If no predicate governs the asserted acceptance, return `missing-governor[acceptance]`. Identify evaluation or acceptance Work separately when that occurrence claim is needed; identify a C.2.1 evaluation-result episteme when the result content needs its own reference. If the criteria use different local senses, test the F.9 Bridge, state the proposed cross-local comparison or substitution in a separate bounded-use claim, and check reliance; the Bridge itself transfers no acceptance.
* **Description-change-as-occurrence-change.** Selecting another MethodDescription episteme is treated as automatically splitting or preserving Work -> State the description-selection change separately. For an identity question raised by an actual history change, first use the direct facts. Apply the named use's continuity-policy criterion only if the grouping remains ambiguous; the policy revises the judgment, not the occurrence. Call the descriptions editions only when their exact C.2.1 relation obtains.
* **Performed cost and estimate collapse.** Treating an estimate or Method-level statistic as actual resource use -> recover the dated Work and its resource-use relations. Keep forecasts, allocation and derived statistics under their own accounting rules.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Independently admit the participating Work occurrences, then assert the relation whose §4.1a predicate holds. For a retry claim, use the locally declared species required by §5.2.
* **Timetable-as-Work-architecture.** Rows with similar labels or one planned window are treated as one Work whole, its parts, or overlapping Work → Recover every actual Work occurrence first; then establish each Work-part and temporal relation separately. Keep an unperformed or ungrounded row as plan or description content.
* **Slice-as-episode.** A monitoring interval, telemetry window, crank-angle segment, or one-second reception trace is called an episode only because it has timestamps -> Keep it as a C.27.TA temporal aspect, evidence relation, or telemetry relation. Use `TemporalPartOf_work` or `EpisodeOf_work` only after the first participant is independently admitted as Work and the corresponding §4.1a predicate passes; add a continuity policy only if direct boundary facts leave its grouping ambiguous.
* **Episode-as-new-work by habit.** A pause, retune, or interruption is always recorded as either a new occurrence or the same one -> Preserve the boundary events first. Use direct facts when they settle the grouping. If a named use still has more than one defensible grouping, apply its `workContinuityPolicyRef`; without the needed criterion, leave that segmentation unresolved.
* **Method-factor-as-work-part by label.** A step, stroke, receiver component, graph node, or method-description section is treated as a work part or submethod by name -> Recover the current object: `U.Method` factor, `U.MethodDescription` constituent, `TemporalPartOf_work`, `OperationalPartOf_work`, evidence segment, mechanism material, system-component behavior, or missing-source-relation note.
* **Granularity inflation.** Every interval or trace row receives a durable Work-part name -> admit the Work part independently and name it only when the receiving use needs a distinct reference under §5.1.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> recover the exact `B.1.4` temporal aggregation and cite its policy per KPI.
* **Double-count in overlaps.** Summing child and parent resource facts as one ledger -> recover the `B.1.6` aggregation claim and apply its exact overlap or deduplication policy.

