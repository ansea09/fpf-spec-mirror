---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__009_conformance-checklist.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:7 — Conformance Checklist"
line_start: 36221
line_end: 36232
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.22.CGUS:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 Identity and profile.** | The four A.22 discriminators identify one `U.Structure`; local locus bindings, relations, and constraints define at least two potential continuations across allowed cases. | Recover the missing value or keep the artifact as an explanation. |
| **CC-CGUS-2 Local loci and relation participants.** | Every `CGUSLocusBinding` uses a locus declared inside this CGUS and binds one constituent for a stated meaning. A needed relation participant retains its definition, occurrence, order, and binding; `RelationSignature` and `SlotSpec` appear together only for declaration-level replay. | Restore the locus or complete relation-participant basis. Never use a free-standing `SlotSpec` as a structure position. |
| **CC-CGUS-3 Explanation and description separation.** | An ordinary or persisted provisional explanation concerns the domain question or proposed alternatives. Post-qualification descriptions and slices concern the CGUS. None is the structure or a membership condition. | Restore the right `EntityOfConcern` or keep the explanation ordinary. |
| **CC-CGUS-4 Current continuation result.** | Each judgement retains its test or obtaining-relation basis, applicability, inputs, facts, polarity, dependent occurrences, window, outcome, and reason. The enabled set may contain zero, one, or several alternatives. | Mark the affected candidate unknown or stop on the missing value. |
| **CC-CGUS-5 Separate decisions.** | Identity and membership, case result, description adequacy, and each neighboring claim are judged separately. | Reopen only the affected decision. |
| **CC-CGUS-6 Work-order boundary.** | The selected structure and display expose branches and conditions. | Put any prescribed or performed Work order under the Method, work-plan, or Work pattern that establishes it. |
| **CC-CGUS-7 Graph-shaped coverage.** | Branches, joins, cycles, partial order, and live alternatives are preserved or explicitly omitted for the declared use. | Keep a chain provisional or state what its demonstrative slice omits. |

