---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:11"
section_title: "Anti-patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__013_anti-patterns-remedies.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:11 — Anti-patterns & remedies"
line_start: 71265
line_end: 71281
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:11 - Anti-patterns & remedies

| ID    | Anti-pattern | Symptom | Why it breaks thinking | Remedy (conceptual move) |
| --------- | -------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AP-1** | **String-equals = sense-equals** | Same spelling used across Contexts with silent identity claims. | Violates locality; invites false substitution. | Always state a **Bridge kind**; if unsure, default to **Partial-overlap** with **Naming-only** scope. |
| **AP-2**  | **Stealth substitution**         | “We’ll just treat A like B for now.”                                              | Hidden policy with unknown loss; leaks into Role Assignment & Enactment.    | Publish a **Bridge Card** with **Loss Notes** and **CL**; if CL<2, substitution remains **unsupported**.      |
| **AP-3** | **Stance jump by wording** | -Activity (PROV) is a Process (BPMN).- | DesignRunTag confusion; swaps graphs for events. | Use a **Design-spec -> Run-trace** Interpretation Bridge, not a substitution bridge; keep **Explanation-only** scope. |
| **AP-4** | **Symmetry hallucination** | Treating directional bridges as if they were symmetric. | Narrows broadened, broadens narrowed; unsafe reuse. | Record **direction** explicitly; only **Equivalence** is symmetric. |
| **AP-5** | **Disjoint but reused** | Declare `Disjoint` and still borrow labels or Role Description constraints (RCS/RSG). | Contradiction between declaration and use. | Either retract `Disjoint` or stop reuse; if a thin thread exists, rename it as **contrastive explanation** (no row). |
| **AP-6** | **CL without counter-example** | -These are CL=3- with no invariant check. | Inflates trust; over-supports structural rows. | For **CL=3**, cite the **matching invariants**; otherwise, demote to **CL=2** and add a counter-example. |
| **AP-7** | **Bridge inflation** | Dozens of nearly identical Bridges between the same Contexts. | Noise masks the few material alignments. | Prefer **one Bridge per pair of Cells per senseFamily**; fold variants into **Loss Notes**. |
| **AP-8** | **Row outruns Bridge** | A Concept-Set row claims Role Assignment & Enactment-eligibility where some participating Bridges are `CL = 1`. | Row scope exceeds the weakest link. | Apply the **weakest-link rule** (F.7/F.8): row scope <= `min(CL)`; otherwise split the row. |
| **AP-9** | **Bridge as new U.Type** | Using a Bridge to justify minting a new universal Type. | Re-globalises meaning; breaks A.11 parsimony. | Keep Types context-local; where reuse is needed, use **rows** + Bridges, not new primitives. |
| **AP-10** | **Silent unit-and-scale mismatch** | Transporting measurements without unit and scale notes. | Hidden dimensional error. | Record units and scales in **Loss Notes**; if units cannot be related, use **Disjoint** or **Partial-overlap** with **Naming-only** scope. |
| **AP-11** | **Coarsened note treated as bridge support** | A summary, redacted comparison, or partner-facing simplification is used as if it already supported substitution or interoperability claims. | A bridge claim is being smuggled through a coarsened rendering that only made lighter review or orientation admissible. | Reopen the source-bearing episteme or source publication needed for bridge support and publish the actual Bridge Card before any bridge-bearing or substitution use. |


