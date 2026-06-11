---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:2"
section_title: "Problem (what breaks without it)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__003_problem-what-breaks-without-it.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:2 — Problem (what breaks without it)"
line_start: 20700
line_end: 20716
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

### A.15.3:2 - Problem (what breaks without it)

Without an explicit `SlotFillingsPlanItem` baseline, at least six failure modes recur:

1. **Hidden slot-bearing-description reference and meaning drift:** a planned filler is stated without making explicit *whose* slot set is being filled, allowing silent reinterpretation of `SlotKind`s across kits or suites.

2. **Planning and enactment collapse:** plan documents get “backfilled” with run-time values, so there is no stable planned baseline and no clean variance trail. WorkPlan explicitly warns against this.

3. **Implicit time (“latest”) and implicit recency:** planned claims about comparability or launch readiness omit an explicit `Γ_time`, which violates the time discipline (“no implicit recency”).

4. **Edition ambiguity:** references to method, policy, and specification references are not edition-pinned where reproducibility requires it, or the plan mutates the edition vector instead of citing pinned editions (edition changes are crossings, not “plan edits”).
   A particularly harmful subtype is **edition-key backfill**: retroactively editing a previously used baseline so that an edition-key change looks like an innocent PlanItem edit (hiding the required GateCrossing witness and breaking audit traceability).

5. **Crossing invisibility:** cross-context or cross-plane expectations (Bridge + policy ids) are not stated at plan time, so downstream gate crossings appear as “magic” rather than traceable expected constraints.

6. **G-pattern fragmentation:** each Part G pattern invents its own place to stash planned refs (method pick, comparator pick, QD archive config, etc.), blocking a clean “G.Core” universal layer and making modular reuse brittle.

