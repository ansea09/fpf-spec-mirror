---
chunk_kind: "child"
pattern_id: "A.6.H"
pattern_title: "Wholeness Language Unpacking — RPR-WHOLE"
section_id: "A.6.H:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.H/A.6.H__006_archetypal-grounding.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "A.6.H — Wholeness Language Unpacking — RPR-WHOLE"
  - "A.6.H:5 — Archetypal Grounding"
line_start: 21256
line_end: 21276
dependencies:
  - "A.14"
  - "A.15"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1.1"
  - "B.1.4"
  - "F.18"
keywords:
  - "boundary"
  - "completeness"
  - "environment"
  - "integrity"
  - "mereology"
  - "order/time"
  - "part-of"
  - "publication-carrier and EntityOfConcern/Description distinction"
  - "role-method-work"
  - "wholeness"
---

### A.6.H:5 - Archetypal Grounding

**Tell.** “Wholeness” is not one concept in practice; it is a shorthand for boundary, composition rule, and coverage. Precision comes from unpacking the shorthand into the smallest set of explicit claims that make disagreements decidable.

**Show — System vignette (lab automation).**
A team says: “The whole chromatography pipeline is turnkey, and the chemist owns the whole thing.” This collapses three meanings: workflow order, capability completeness, and role boundary. A precise rewrite becomes:

* “Pipeline” is a **MethodDescription** with steps connected by **SerialStepOf**; the composite procedure is aggregated by **Γ_method and Γ_ctx**.
* “Turnkey” is **capability/spec coverage**: which required roles/capabilities cover which steps under which scope (G).
* “Chemist owns” is a **role assignment boundary** inside a bounded context (who is authorized/required), not a ComponentOf structure.

Now the discussion can separate: “Is the workflow correct?” vs “Do we have capability coverage?” vs “Who is responsible in this context?”

**Show — Episteme vignette (paper + proof + revision).**
A reviewer writes: “Section 3 is part of the proof, and v2 is part of v1.” Both “part” usages differ.

* “Section 3” is typically **ConstituentOf** the paper (content inclusion), while “step 3 of the proof” is **SerialStepOf** in the proof’s reasoning order.
* “v2 part of v1” is usually **PhaseOf** the same carrier across time, aggregated by **Γ_time**—unless the identity changed, in which case an explicit transformation produced a new holon, episteme, or publication according to the live identity criterion.

The author can now fix the prose and the model without guessing what “part” meant.

