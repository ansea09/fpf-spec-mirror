---
chunk_kind: "child"
pattern_id: "A.6.8"
pattern_title: "Service Polysemy Unpacking (RPR‑SERV)"
section_id: "A.6.8:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.8/A.6.8__002_problem-frame.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.6.8 — Service Polysemy Unpacking (RPR‑SERV)"
  - "A.6.8:1 — Problem frame"
line_start: 16394
line_end: 16423
dependencies:
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.9"
  - "A.6.5"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "C.26.1"
  - "C.26.3"
  - "E.10"
  - "E.15"
  - "F.17"
  - "F.18"
  - "F.8"
  - "U.Commitment"
  - "U.PromiseContent"
  - "U.SpeechAct"
  - "U.Work"
keywords:
  - "API read/export"
  - "boundary exchange"
  - "interface semantics"
  - "promise content"
  - "provider principal"
  - "service polysemy"
  - "service situation"
  - "service/cell analogy"
  - "viability envelope"
---

### A.6.8:1 - Problem frame

In real engineering language, *service* can denote (and routinely collapses) multiple **facets** that admit different predicates and different governance rules:

* a **promise content** (`U.PromiseContent`),
* a **promised work kind or effect kind** (“what is to be delivered”, as a kind/template),
* a **service provider role** (role kind in the clause),
* a **service provider principal** (role‑enactor accountable for delivery and capable of holding commitments),
* a **service access point** (an addressable system/facility/desk/endpoint host),
* a **service access spec** (API surface, endpoint set, or SOP visible to consumers),
* a **service delivery / realization system** (the socio‑technical system that actually performs fulfillment work),
* a **service delivery method** (workflow, runbook, or procedure used to fulfill),
* a **service commitment** (deontic binding, e.g., SLA/SLO as obligation),
* a **service promise act** (promissory speech act: offer/promise/accept/agree/publish),
* a **service delivery work** episode (run/incident/fulfillment work + evidence).

FPF’s kernel uses `U.PromiseContent` as **promise content**, which is SoTA‑consistent for contracts and decision lanes, but clashes with the everyday addressability-centric use of “service”. This makes “service” a high‑risk metonymy attractor: authors start using the same word for (a) the clause, (b) the provider system, and (c) the delivery work, and readers cannot reliably recover which is meant.

In addition, lived “service talk” is rarely isolated to the token *service*: it co‑moves with **server** and **service provider** (and with “API service”, “service desk”, “service team”). Treating only the word *service* as ambiguous is an underfit to the domain.

Critically, everyday “service” often conflates **three different participants** that are frequently *not identical*:

1. the **provider principal** (accountable role‑enactor: a team/org/vendor),
2. the **delivery / realization system** (the socio‑technical system that does the work),
3. the **access point** (the addressable entrypoint/gateway/front desk/endpoint host).

This pattern forces those participants apart, because different predicates and different governance rules apply to each.

This pattern makes “service” an **always‑unpack token** in normative prose: you may use it only as part of a **qualified head phrase** that states which facet is meant.

