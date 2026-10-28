---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuation: Distinguish Occurrences When Needed"
section_id: "A.6.REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__002_problem-frame.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuation: Distinguish Occurrences When Needed"
  - "A.6.REL:1 — Problem frame"
line_start: 15679
line_end: 15698
dependencies:
  - "A.6.0"
  - "A.6.5"
  - "C.2.1"
  - "C.29"
  - "E.24"
  - "E.24.UK"
  - "F.18"
keywords:
---

### A.6.REL:1 - Problem frame

**Plain name.** Relation occurrence.

**Primary EntityOfConcern.** One obtaining relation occurrence of an admitted relation kind, when a receiving use needs to reidentify it or distinguish it from another occurrence.

**Primary working reader.** An engineer who has stated a direct relation and must decide whether that sentence suffices or a receiving use needs explicit occurrence identity.

**Working concern and viewpoint.** Preserve the readable direct relation assertion. Add explicit occurrence identity when reidentification, comparison or another dependent use needs it, keeping the world-side occurrence distinct from its description, designation and representation.

**Use this when.** Use this pattern when a receiving use needs to reidentify one obtaining relation occurrence, distinguish it from another or use that specific occurrence as a participant or argument. A report that only needs to say `Robot-7 is assigned as inspector through InspectionAssignment-17` can keep that direct sentence and stop. A history distinguishing two `MaintenanceInspectionAssignment` episodes with the same `Robot-7` and `InspectorSystemRole` needs the identity branch. So does a dependent relation that requires one already distinguished occurrence as its participant; a second episode need not already have occurred.

**First useful move.** State the direct relation and participants using the subject pattern's meanings and obtaining predicate. Apply that test to the relevant facts or constituting history and state the supported result. Ask whether the receiving use needs to reidentify or distinguish this occurrence. If not, keep the direct sentence and stop; otherwise apply the identity and receiving-use steps in section 4.2.

**What goes wrong if missed.** An epistemic, designation, or representation-side object is treated as what creates the relation it is meant to describe or designate. Repeated assignments with the same participants then collapse into one. At the opposite extreme, every ordinary relational sentence is expanded into a relation-occurrence description episteme even though later work does not need to distinguish occurrences.

**What this buys.** Engineers can report a current relation in ordinary prose without opening unused apparatus. When history, comparison, evaluation, or another direct relation must distinguish repeated occurrences, a system can apply the domain identity rule while assertions, descriptions, designations, representations, and publication occurrences retain their own identities.

**Not this pattern when.** If the wording leaves the direct relation or participants unclear, use `A.6.P` or `A.6.RSIR`. If the defining content does not supply participant meanings, applicability and the obtaining predicate, recover that content first. When case facts do not establish obtaining, keep the claim and its actual polarity or uncertainty under its direct semantics; an assertion alone supplies no occurrence to individuate. Forecasts, scenarios, counterfactuals and permissions retain their own claim families. Use `A.10` or the current evaluation for a separate reliance judgement. For reusable declaration SlotSpecs use `A.6.5`. When the direct sentence already suffices for the receiving use, stop there.

