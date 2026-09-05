---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuated Relation Occurrences"
section_id: "A.6.REL:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__002_problem-frame.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuated Relation Occurrences"
  - "A.6.REL:1 — Problem frame"
line_start: 12223
line_end: 12242
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

**Primary EntityOfConcern.** One obtaining relation occurrence of an admitted relation kind, opened only when later work must distinguish it from another occurrence of that same relation.

**Primary working reader.** An engineer who has stated a direct relation and must decide whether a readable current report is enough or later work must distinguish repeated occurrences.

**Working concern and viewpoint.** Preserve the readable direct relation assertion and ask first what later work must distinguish. Open occurrence identity only when that work must tell this occurrence from another; do not substitute an epistemic, designation, or representation-side object for the world-side relation.

**Use this when.** Use this pattern when later use must tell one obtaining relation occurrence from another occurrence of the same relation. With `Robot-7 is assigned as inspector through InspectionAssignment-17`, a report that only says who is currently assigned can keep that direct sentence and stop. A history or comparison that must tell a second `MaintenanceInspectionAssignment` episode from the first, even with the same `Robot-7` and `InspectorSystemRole`, needs the occurrence-identity branch. A dependent direct relation may likewise require one already distinguished occurrence as its participant.

**First useful move.** Write the direct relation with its named participants, using the subject pattern's participant meanings and obtaining predicate only as far as needed to state that relation accurately. The subject pattern defines the test. Apply it to the relevant world facts or constituting history in the current case, and record the resulting polarity in a claim-bearing episteme. Then ask: **Will later work need to tell this occurrence from another occurrence of the same relation, including another episode with the same participants?** If no, keep the readable direct sentence and stop. If yes, recover and apply the subject pattern's same-versus-new-occurrence rule. Only after you use that rule to distinguish the occurrence should you designate it in a receiving assertion or description episteme, use it as a participant of another direct relation, or bind it as the actual value of a named A.6.1 argument. Add a designator or reference only when stable reference is needed.

**What goes wrong if missed.** An epistemic, designation, or representation-side object is treated as what creates the relation it is meant to describe or designate. Repeated assignments with the same participants then collapse into one. At the opposite extreme, every ordinary relational sentence is expanded into a relation-occurrence description episteme even though later work does not need to distinguish occurrences.

**What this buys.** Engineers can report a current relation in ordinary prose without opening unused apparatus. When history, comparison, evaluation, or another direct relation must distinguish repeated occurrences, a system can apply the domain identity rule while assertions, descriptions, designations, representations, and publication occurrences retain their own identities.

**Not this pattern when.** If the wording does not yet identify the direct relation and participants, start with `A.6.P` or `A.6.RSIR`. If no exact ClaimGraph yet defines the participant meanings, applicability, and obtaining predicate, recover that content rather than inventing a case test here. If the current case lacks relevant world facts or constituting history, keep the statement as a `C.2.1` claim under the exact direct predicate. Keep denials, forecasts, scenarios, counterfactuals, and permissions in their exact claim families; keep evidence and reliance results under their separate governors. Individuate an occurrence only when the relevant facts or history satisfy the predicate. Record supported, refuted, or unresolved reliance under `A.10` or the current evaluation when that separate judgement is needed. When current-case facts satisfy the direct predicate, A.6.REL remains available only if later work must tell this occurrence from another occurrence of the same relation. If the question concerns only the SlotSpecs of a reusable relation declaration, apply `A.6.5`. If later work only reports the current relation, keep the direct sentence and stop.

