---
chunk_kind: "child"
pattern_id: "A.10.1"
pattern_title: "Revalidate Affected Uses When a Relied-on Source Changes"
section_id: "A.10.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10.1/A.10.1__006_archetypal-grounding.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.10.1 — Revalidate Affected Uses When a Relied-on Source Changes"
  - "A.10.1:5 — Archetypal Grounding"
line_start: 23208
line_end: 23252
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.11"
  - "B.3"
  - "C.2.1"
  - "E.15"
  - "G.11"
  - "G.6"
keywords:
---

### A.10.1:5 - Archetypal Grounding

**Tell.** A source change matters through a claim that a receiving use actually relied on. Search helps find possible receivers; the receiver and its direct subject rule decide whether action changes.

#### A.10.1:5.1 - Show: Sensor-Calibration Range in an Actual Engineering Host

A pump-controller project used edition E2 of a sensor-calibration `MethodDescription`. E2 states that temperature compensation for module `TS-2` is valid from `-20 °C` to `50 °C`. E3 narrows ordinary validity to `-10 °C` through `50 °C` and requires a new calibration Method and evidence below that range.

The search frame is the named pump-controller project, `TS-2` configurations, current service-release interval, and the model, test, safety, interface-architecture, and decision stores used for that release question. Other hardware configurations are excluded when they do not use `TS-2` under the changed condition.

The source-outward route follows exact E2 references and established traces. The receiver-oriented route scans the included stores for the old temperature range and equivalent cold-start premises. Inspection finds:

- the thermal-model parameter bound `depends`;
- the cold-start test condition `depends`;
- the safety claim's use of evidence produced under that condition `depends`, and its action-changing reach continues to the service-release premise; and
- the interface description's bibliography entry `mentions only`.

The affected reach stops at the last service-release action that can change. A practitioner or admitted System applies `SYSE.19` to the discovery-and-reach statement. The independently governed engineering revalidation result records evidence that supports units `S006`–`S008` under the tested conditions and leaves `S009`–`S010` without the needed calibration evidence. That result goes directly to `SYSE.14`, where the authorized release decision remains. Only afterward does the common account cite that result, preserve the bibliography-only use and unaffected configurations, and summarize the affected release branches.

#### A.10.1:5.2 - Show: Financial Model and Data Refresh

A market-data supplier corrects a yield-curve claim for a named date range. The old claim was used by a valuation model and a cash forecast; a nearby finance memo merely cites the vendor report.

The search frame fixes the corporation and portfolio, jurisdiction, decision date, currency and instrument families, model and dataset inventory, finance-account stores, and the desks and periods explicitly excluded from the current question. Data lineage and source identifiers provide the source-outward route. A receiver-side scan checks model inputs, forecast assumptions, liquidity-account premises, and exposure calculations for the same or an equivalent claim.

The valuation input and forecast assumption are `depends`. The nearby memo is `mentions only`. One local workbook cannot be accessed, so that workbook is a discovery-coverage gap; it is not called unaffected. A practitioner or admitted System applies `FIN.17` to the resolved discovery-and-reach statements, retaining finance-specific model, data, jurisdiction, accounting, reconciliation, evidence, and authority judgments within that application. The independently governed finance result goes as revision feedback directly to `FIN.4`. The common account cites that finance result afterward and keeps the inaccessible workbook as an explicit continuation item.

#### A.10.1:5.3 - Show: A Changed Research Estimate Is Only One Kind of Strategic Signal

An industry-research edition corrects an adoption estimate used as a premise for one strategic assumption and option. Nearby scenario prose cites the report without using the estimate.

The search frame fixes the named strategic decision, assumption and option registers, current scenario set, decision horizon, and source store. Source references and a receiver-side assumption scan identify the relied-on assumption branch as `depends` and the nearby citation as `mentions only`. An inaccessible business-unit assumption store remains a coverage gap.

A practitioner or admitted System applies `STR.2` to the discovery-and-reach statement. That application keeps signal qualification, uncertainty, the affected strategic assumption, option or commitment consequences, horizon, and the assumption-impact result within `STR.2`'s governing scope. The independently governed assumption-impact result goes directly to `STR.3` and `STR.4`. A market or competitor change with no changed source claim goes straight to `STR.2`; it is not forced through A.10.1.

#### A.10.1:5.4 - Reduced Boundary Cases

| Case | A.10.1 response | Direct continuation |
| --- | --- | --- |
| The same source episteme appears at a new URL with a new layout. | No material claim change; take the cheap stop. | `C.2.1`, `E.17`, `E.24.PUB`, and `A.10` when availability affects one bounded use. |
| A bibliography or catalogue mentions the changed source but uses none of its claims. | `mentions only`; no affected reach. | No subject revalidation follows from mention alone. |
| Candidate content appears to use the claim, but the premise or applicability cannot be recovered. | `unresolved` with the exact missing fact. | Recover the missing source, relation, evidence, or subject-result basis before classifying the branch. |
| An included repository is inaccessible or its index is stale. | Record a discovery-coverage gap; finish independent resolved branches. | Do not call possible uses in that surface unaffected. |
| The source is unchanged but the represented world changed. | Outside this pattern's selected branch. | Use the direct configuration, currentness, change, or decision pattern. |

