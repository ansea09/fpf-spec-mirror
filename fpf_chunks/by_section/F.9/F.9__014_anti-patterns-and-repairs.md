---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:13"
section_title: "Anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__014_anti-patterns-and-repairs.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:13 — Anti-patterns and repairs"
line_start: 74781
line_end: 74796
dependencies:
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "E.10.D1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
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

### F.9:13 - Anti-patterns and repairs

| ID | Anti-pattern | Symptom | Why it breaks thinking | Repair |
| --- | --- | --- | --- | --- |
| AP-1 | String-equals becomes sense-equals | Same spelling used across contexts with silent identity claims. | Violates locality and invites false substitution. | State a Bridge kind; if unsure, default to Partial-overlap with Naming-only admitted use. |
| AP-2 | Stealth substitution | "Treat A like B for now." | Hidden policy with unknown loss; bridge result is used as role assignment, status transfer, or work attribution. | Publish a Bridge Card; then open the direct governing pattern for the non-F9 claim. |
| AP-3 | Stance jump by wording | "Activity is a Process." | Design sense and run occurrence are collapsed. | Use a design-spec-to-run-occurrence interpretation bridge and keep Explanation-only admitted use. |
| AP-4 | Symmetry hallucination | Directional bridges are treated as symmetric. | Narrower becomes broader or broader becomes narrower. | Record direction; only Equivalence is symmetric. |
| AP-5 | Disjoint but reused | `Disjoint` is declared, then a label or RoleDescription constraint is borrowed. | Declaration and use conflict. | Retract Disjoint, or stop reuse; if a thin comparison remains, mark contrastive explanation. |
| AP-6 | CL without counter-example | "These are CL=3" with no invariant check. | Inflates row scope. | For `CL = 3`, cite invariants; otherwise demote and add a counter-example. |
| AP-7 | Bridge inflation | Many near-duplicate Bridges between the same contexts. | Noise hides material alignments. | Prefer one Bridge per pair of cells per relevant `senseFamily`; fold variants into Loss Notes. |
| AP-8 | Row outruns Bridge | A Concept-Set row claims stronger use than the weakest participating Bridge admits. | Row scope exceeds the stated evidence. | Apply weakest-link discipline: row admitted use is no stronger than the weakest Bridge. |
| AP-9 | Bridge as new `U.Type` | A Bridge is used to justify a new universal type. | Re-globalizes meaning. | Keep types context-local unless A.11 and F.8 admit a durable type candidate. |
| AP-10 | Silent unit or scale mismatch | Measurements cross contexts without unit and scale notes. | Hidden dimensional error. | Put units and scales in Loss Notes; if they cannot be related, use Disjoint or Partial-overlap. |
| AP-11 | Coarsened note treated as Bridge Card | A summary or redacted comparison is used as if it made substitution admissible. | A bridge claim is smuggled through a lighter rendering. | Reopen the source-bearing episteme or publication and write the Bridge Card before bridge-bearing use. |

