---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__013_relations.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12 — Relations"
line_start: 21652
line_end: 21664
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.TGA"
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

### A.15.3:12 - Relations

* **Builds on and is governed by:**
  * **A.15.2 `U.WorkPlan`** — container + PlanItem discipline; baseline citeability.
  * **A.6.5 slot discipline** — SlotKind and RefKind hygiene and binding-time separation.
  * **E.10.D1 Context discipline** — explicit context and edition; no implicit “latest”.
  * **E.18 and TGA** — keeps `FinalizeLaunchValues` strictly in WorkEnactment; pin and guard discipline.
* **E.17 publication discipline** — views are projections; no new semantics on cards.
* **Interacts with and complements:**
  * **A.6.7 `MechSuiteDescription`** — suites may require the presence of a planned-baseline reference or pin without embedding planned fillers or launch values.
  * **A.15.1 Work and WorkEnactment discipline** — fulfilment and variance are recorded downstream against this baseline.
  * **C3.2-S-02 Time discipline** — time selection policy may be pinned by ref; run-time `Γ_time` stays in Work evidence.

