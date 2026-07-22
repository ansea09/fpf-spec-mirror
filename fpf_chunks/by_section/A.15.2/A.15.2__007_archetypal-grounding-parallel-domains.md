---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:6"
section_title: "Archetypal grounding (parallel domains)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__007_archetypal-grounding-parallel-domains.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:6 — Archetypal grounding (parallel domains)"
line_start: 24913
line_end: 24935
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.2.2"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.32.P2S"
  - "E.17"
  - "E.24"
  - "E.24.UK"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "PlanItem content"
  - "horizon"
  - "intended-work episteme"
  - "no actuality by plan"
  - "performer and capability conditions"
  - "positive or governed-negative local fulfilment assertion"
  - "possible future performance"
  - "present EntityOfConcern"
  - "reusable predicate semantics"
  - "variance"
---

### A.15.2:6 - Archetypal grounding (parallel domains)

#### A.15.2:6.1 - Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025-08-12`, whose present EntityOfConcern is the exact operating service system for that day; the proposed cases remain plan-content designators until surgery Work occurs.
* **`PlanItem` content:** `Case_1_Appendectomy`, `Case_2_Hernia`, with windows and intended surgeon and anesthetist holder and `U.Role` conditions; cite an exact `U.RoleAssignment` only when it already obtains.
* **Budgets:** OR time blocks, consumables envelopes, and exact reservation claims.
* **Later local assertion:** Each exact surgery Work occurrence is identified independently as an individual admitted under `U.Work`. A separate assertion about the plan edition then names the fulfilment policy and maps the independently obtaining `performedBy`, `enactsMethod`, temporal, affected-referent, binding, and performed resource-use relations involving each occurrence to the intended case content before any duration, substitution, resource, or acceptance comparison is made.

#### A.15.2:6.2 - Fab maintenance weekend (asset reservations)

* **WorkPlan:** `Fab_Maintenance_W36`, whose present EntityOfConcern is the exact fab system or governed asset group under concern.
* **`PlanItem` content:** `Tool_42 chamber clean`, `Tool_13 calibration`; the ClaimGraph carries an exact exclusivity constraint with production windows under the named scheduling policy, not a reusable `MutuallyExclusive_pl` relation kind.
* **Reservations:** nitrogen, DI water, metrology window.
* **Later local assertion:** The exact chamber-cleaning Work occurrence is identified independently as an individual admitted under `U.Work`. A separate assertion about this plan edition states how independently obtaining relations involving that Work individual satisfy the item under the named policy; its temporal extent and resource-use relations are then compared under A.15.1 and B.1.6 with the planned window and budget to state early completion and cost underrun.

#### A.15.2:6.3 - Data-center rollout (multi-context plan)

* **WorkPlan:** `DC_Rollout_Phase-2`, whose present EntityOfConcern is the exact rollout-owning system or current service system named by the plan.
* **Interpretation boundary:** Operations and Security Audit use separately pinned reference schemes and direct acceptance criteria. Reuse of a term such as “ready” or “passed” may cite F.9 only through an exact Bridge between two `SenseCell` values with stated losses and admitted use; F.9 does not translate target values or transfer a verdict.
* **`PlanItem` content:** `Deploy Service A`, `Pen-test A`; exact dependency and window claims name their predicates and conditions inside the plan ClaimGraph.
* **Later local assertions:** Exact deployment and audit Work occurrences are identified independently as individuals admitted under `U.Work`. Separate operations and audit evaluations apply their own targets and produce separately governed verdicts; plan-use assertions state exact local fulfilment and per-context comparison without adding those actual facts to the plan content or creating one cross-context fulfilment relation.

