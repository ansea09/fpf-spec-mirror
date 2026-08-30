---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:5"
section_title: "Retained-set and optional applied readings"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__007_retained-set-and-optional-applied-readings.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:5 — Retained-set and optional applied readings"
line_start: 49329
line_end: 49375
dependencies:
  - "A.0"
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "B.4"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "E.10.LRN"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "ConstraintFit"
  - "Novelty"
  - "Use-Value"
  - "bounded quantitative result"
  - "evidence"
  - "incomparability"
  - "named comparison basis"
  - "qualitative-first evaluation"
  - "uncertainty"
---

### C.17:5 - Retained-set and optional applied readings

#### C.17:5.1 - Diversity and illumination

`Diversity_P` describes coverage or dispersion of one declared retained set under a named measurement policy. A local policy may, for example:

- take the average pairwise distance among the admitted members under one declared descriptor map, distance Method, and Scale; or
- report how much of a declared feature partition is covered, using a stated covering radius or k-cover rule.

Neither construction is universal. The result identifies the retained set and membership rule, measurement-policy and Scale editions, descriptor or feature source editions, distance or covering definition, comparison window, and evidence. A distance matrix or coverage map can show the calculation. When the reading affects a decision, vary a plausible kernel, distance definition, covering threshold, or admitted-member set and report whether the conclusion changes.

For a candidate `h` and retained set `S`, the same local policy may use the marginal reading `DeltaDiversity_P`, also written `ΔDiversity_P`:

`DeltaDiversity_P(h | S) = Diversity_P(S plus h) - Diversity_P(S)`

Illumination is a report over `Diversity_P`, such as a coverage map or QD-score summary. It is telemetry, not a primitive characteristic and not part of the default dominance set. Use `C.18` to maintain an Archive or Front and `C.19` to state any pool policy that uses these readings.

Optional retained-set readings include:

- `FamilyCoverage`: coverage of locally defined families under a named policy and Scale;
- `MinInterFamilyDistance`: the smallest distance among declared families, with descriptor map, distance definition, Scale, and family-representation rule;
- `AliasRisk`: a near-duplicate or alias diagnostic with collision policy, descriptor source edition, and Scale;
- `DescriptorVector`: an optional descriptor payload whose dimensions and interpretation the same local policy declares.

These readings characterize the named set. They do not admit sources, select members, establish universality, or widen applicability. For naming candidate sets, apply `F.18`'s head-term-family anti-inflation rule rather than restating that lexical rule here.

#### C.17:5.2 - Optional applied characteristics

The following are executable local examples, not required universal templates. Use one only when the receiving question needs it and identify its bearer, rule, Scale, and evidence.

- **`ReframeDelta`.** The bearer is an ordered pair of problem-frame epistemes. One local rule compares the earlier and later frame on an ordinal Scale such as `None | Local | BoundaryShift | Systemic`; a boundary or scope diff and a changed causal map support the reading. The frame change does not by itself prove improvement, so state Use-Value separately.
- **`Compositionality`.** The bearer is the design or episteme being assessed. One local rule requires reuse of at least a declared number of components and evidence of at least one new relation among them; it may return a boolean plus a separately defined structure reading. Cite the component graph and component provenance.
- **`Transferability`.** The bearer is the design, result, or episteme whose use is tested in one named receiving setting. One local ordinal Scale is `not supported | supported with stated loss | supported for the stated use`. Cite receiving-use pilot evidence and the preserved and lost meaning; use an F.9 Bridge only when a relation between different reference-scheme senses actually obtains.
- **`DiversityOfSearch`.** The bearer is a finite set of dated Work attempts. Count distinct approach classes under a declared local typology, optionally as a rate over a stated time window, and cite the tagged Work and typology. Cosmetic variants do not create new classes.
- **`Time-to-First-Viable`.** The bearer is one Work episode. Measure elapsed time from a declared start to the first dated result that passes the stated viability criterion; cite the timestamps and passing evidence. If no result passed, report `not yet obtained` or a right-censored duration rather than the time to the first runnable output.
- **`Risk-BudgetedExperimentation`.** Compare the applicable WorkPlan with the resulting dated Work set. One local rule reports planned exploratory resource use divided by the allowed risk budget and the realized ratio separately, with any overrun visible. Cite the WorkPlan, actual Work, and resource evidence; the reading does not grant the budget or authorize the Work.

These examples do not create another universal characteristic family. Readings about actual attempts, elapsed time, or realized experimentation depend on dated Work; planned experimentation depends on a WorkPlan.

#### C.17:5.3 - Other domain characteristics

The six applied readings above are examples, not the extension boundary. A configuration may select other Characteristics already established for the current use—for example, time or cost to probe, evidence sufficiency, safety or ethical risk, option value, or regret risk. Keep each selected Characteristic's bearer, Scale, polarity, defining source, Method, and evidence. A safety or ethical must remains an eligibility condition through ConstraintFit; evidence sufficiency does not become creativity; and scope does not become another coordinate merely because every claim needs one.

When one comparison covers several components, attempts, or Work occurrences, identify the lawful aggregation separately for each Characteristic. For example, compatible costs may sum, all declared must-constraints may have to pass, a domain risk rule may use its own conservative combination, and evidence may follow an applicable `B.3` relation. These are examples, not C.17 defaults. If no declared aggregation supports the combined reading, keep the component results separate.

Any prior or default used for Novelty, evidence, risk, or another selected reading remains a separately supported model or policy claim with its source and edition. C.17 does not publish domain priors merely because a reusable configuration is convenient.

