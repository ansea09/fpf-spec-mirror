---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:3"
section_title: "Forces (what we must balance)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__004_forces-what-we-must-balance.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:3 — Forces (what we must balance)"
line_start: 20471
line_end: 20490
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.8"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:3 - Forces (what we must balance)

* **Strict distinction:** planned baseline is not a run-time witness; launch values are finalized only in Work enactment.
* **Context must be explicit:** every normative claim/rule is context-bound; the PlanItem must carry its context rather than relying on file location or prose.
* **Time must be explicit:** no implicit “latest”; any plan that will be cited by comparability/launch checks needs an explicit `Γ_time` selector/rule.
* **SlotKind meaning is stable:** the plan may choose fillers, but must not reinterpret SlotKinds or smuggle new semantics into indices.
* **Derived indices must not become “places of meaning”:** projections like “planned spec refs” are useful, but must remain derivable from the authoritative rows.
* **Conceptual, not procedural:** no solver steps, no lints, no “data governance”; this is an epistemic object used by humans in review.
* **Supports universalization:** one PlanItem pattern must be usable across the whole of Part G, not just G.5.
* **Integrates with suites/kits:** suites may require a planned-baseline ref and may act as slot-bearing descriptions.

| Force | Tension |
| --- | --- |
| Plan/run split | Plan must be citeable without containing run-time values. |
| Slot meaning stability | SlotKinds must not drift by implicit slot-bearing-description changes. |
| Edition honesty | Baselines must pin editions where meaning changes; avoid “latest”. |
| Suite/kit modularity | Suite descriptions define slot interfaces and obligations; baselines choose fillers for a plan instance. |
| Auditability | A reader must reconstruct “what was planned” without chasing hidden defaults. |
| Extensibility | Allow suite-specialized variants without breaking universal core. |

