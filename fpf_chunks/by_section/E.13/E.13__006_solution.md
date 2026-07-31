---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility and Value Alignment"
section_id: "E.13:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__006_solution.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "E.13 — Pragmatic Utility and Value Alignment"
  - "E.13:4 — Solution"
line_start: 76927
line_end: 76990
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

Use `ProxyToValueAlignment` as a short repair note, not a new bureaucracy.

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

Keep the note as small as the case allows. The fields exist to restore the value relation, not to create another checklist target.

#### E.13:4.1 - Name the Value Before the Proxy

Name the intended value, objective, or practical payoff in terms of the work it is supposed to improve. If only the proxy can be named, lower the claim: the project has a measure, not a demonstrated value relation.

#### E.13:4.2 - Type the Proxy Use

A proxy can be harmless as an orientation cue and dangerous as a target. State the current proxy use explicitly.

| Proxy use | Admissible use | Danger |
| --- | --- | --- |
| Orientation cue | Helps decide where to look next. | Mistaken for evidence of value. |
| Measure | Reports one declared characteristic under `C.16`. | Treated as the whole objective. |
| Target | Work is optimized to move the proxy. | Goodhart pressure. |
| Incentive | People or agents are rewarded for the proxy. | Behavioral distortion and gaming. |
| Gate or release argument | Passage depends on the proxy. | Proxy becomes authority. |
| Reputation or status signal | People, teams, models, or patterns are ranked by the proxy. | Surrogation and status gaming. |
| Repair target | The object is changed to raise a coordinate or score. | Apparatus is added instead of value. |

#### E.13:4.3 - Ask What Got Worse

Whenever a proxy improves under optimization pressure, ask what became worse or more fragile. Check at least usability, affordability, safety or harm boundary, maintainability, domain fit, source preservation, decision quality, learning, and neighboring-pattern fit when they are live in the case.

If nothing worsened, say which loci were checked. If no loci were checked, do not claim value alignment.

#### E.13:4.4 - Require a Minimally Viable Value Slice

Do not require every project to create a lifecycle artifact named MVE. Require a minimally viable value slice: one compact case, worked slice, observation, trial, user/operator moment, or decision replay where the intended value is visible enough for the declared use.

The value slice may be small. It must show the value, not merely the proxy.

#### E.13:4.5 - Repair by Value Movement

When the proxy has displaced the value, repair one of these:

- change the proxy use from target/gate/incentive to orientation or bounded measure;
- add a protected quality or counter-metric that names the value at risk;
- change the work or design so the value slice improves, not only the proxy;
- split the claim: one measure report, one value claim, one assurance or gate claim if needed;
- stop the value claim until a value slice or better proxy relation exists.

