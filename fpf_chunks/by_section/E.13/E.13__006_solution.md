---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Proxy-to-Value Alignment"
section_id: "E.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__006_solution.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "E.13 — Pragmatic Utility and Proxy-to-Value Alignment"
  - "E.13:4 — Solution"
line_start: 112543
line_end: 112619
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "E.12"
  - "E.14"
  - "E.19"
  - "E.2"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
keywords:
  - "Campbell"
  - "Goodhart"
  - "minimally viable value slice"
  - "pragmatic utility"
  - "proxy-to-value alignment"
  - "surrogation"
---

### E.13:4 - Solution

Use `ProxyToValueAlignment` to recover the intended value, the proxy's current use, the value at risk, and the justified repair or stop. A short answer or local repair is enough when it settles the case.

When later review, reuse, or reliance needs a note, use the fields below that change the conclusion.

```text
ProxyToValueAlignment:
  ObjectOfConcern:
  IntendedValueOrObjective:
  ProxyOrVisibleMeasure:
  ProxyKind:
  CurrentProxyUse: <orientation | measure | target | incentive | gate | release argument | decision driver | reputation signal | repair target>
  AffectedDecisionOrWork:
  ProtectedQualities:
  WhatImproved:
  WhatGotWorse:
  MinimallyViableValueSlice:
  AdmissibleUseNow:
  BlockedOverread:
  RepairOrStop:
  ReopenCondition:
```

Record only the fields needed for the current conclusion, repair, stop, or later reliance. Use them to explain the relationship between the proxy and the intended value.

#### E.13:4.1 - Name the Value Before the Proxy

Name the intended value, objective, or practical payoff in terms of the work it is supposed to improve. If only the proxy can be named, report that the project has a measure. Its connection to the intended value has yet to be shown.

#### E.13:4.2 - Type the Proxy Use

A proxy can be harmless as an orientation cue and dangerous as a target. State how the proxy is being used.

| Proxy use | Admissible use | Danger |
| --- | --- | --- |
| Orientation cue | Helps decide where to look next. | Mistaken for evidence of value. |
| Measure | Reports one declared characteristic under `C.16`. | Treated as the whole objective. |
| Decision driver | Informs a choice under the applicable decision rule. | The proxy displaces the intended objective or protected qualities in the choice. |
| Target | Work is optimized to move the proxy. | Goodhart pressure. |
| Incentive | People or agents are rewarded for the proxy. | Behavioral distortion and gaming. |
| Gate or release argument | Passage depends on the proxy. | Proxy becomes authority. |
| Reputation or status signal | People, teams, models, or patterns are ranked by the proxy. | Surrogation and status gaming. |
| Repair target | The object is changed to raise a coordinate or score. | Apparatus is added instead of value. |

#### E.13:4.3 - Ask What Got Worse

Whenever a proxy improves under optimization pressure, ask what became worse or more fragile.

Check at least usability, affordability, safety or harm boundary, maintainability, domain fit, source preservation, decision quality, learning, and neighboring-pattern fit when they are live in the case.

Report whose decisions, protected qualities and interactions the comparison covers. An effect on each part, a dependence between parts and an effect of their organization are different claims. For example, if two shifts need one specialist at the same time, their joint outcome depends on how that time is allocated. A claim about the improvement of one shift can be settled with the other shift's outcome still open.

#### E.13:4.4 - Require a Minimally Viable Value Slice

A minimally viable value slice gives the recipient enough grounds to judge the practical value claimed. For an expected consequence, relate the proposed change to the recipient's work and establish the conditions under which the consequence follows. A general argument, a worked comparison or an available observation may supply the needed grounds. For a claim about actual improvement, examine use and the comparison needed to attribute the change.

Identify the grounds the value slice supplies, whose outcome it concerns and which variations its reasoning covers. A consequence of a binding obligation and an observed change in someone’s work support different claims.

A short account is sufficient when the recipient can recover the connection over the range in question. If a measure concerns a proxy, explain why it bears on the intended value.

A worked illustration can explain how a proposed repair would serve that value; it does not by itself establish an observed gain. Keep any claim about actual improvement within the comparison and evidence that support it.

A wrong dispatch costs 20 minutes and an extra check costs one minute per dispatch. If the check reduces the probability of a wrong dispatch by at least 0.1 in the intended work, the expected net saving is at least one minute per dispatch, with other costs unchanged. Describing how the check might catch an error identifies the mechanism. For the saving, establish the probability difference or a sufficient bound. A decline in recorded errors can also reflect changes in staffing, reporting or the jobs accepted.

Use partial evidence when it already settles the decision. For a course of twelve people, five verified successes, three verified failures and four unknown outcomes give five to nine successes. An at-least-40% target is met and an at-least-80% target is missed. A 60% target remains open. Reports of ease from the same respondents answer a question about their experience. A rate for future courses needs a basis covering those participants and conditions.

#### E.13:4.5 - Repair by Value Movement

When the proxy has displaced the value, choose one or more of these repairs:

- where the governing rule permits it, change the proxy use from target/gate/incentive to orientation or bounded measure. If a binding requirement must change, propose the amendment under its authority and keep the current requirement in force until that amendment takes effect;
- add a protected quality or counter-metric that names the value at risk;
- change the work or design where the proxy can improve while the intended value deteriorates, and assess what the change does to that value.
- split the claim: one measure report, one value claim, one assurance or gate claim if needed;
- suspend an unsupported claim, or state the consequence and conditions the available grounds already establish.

