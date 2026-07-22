---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__006_archetypal-grounding.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:5 — Archetypal Grounding"
line_start: 50538
line_end: 50551
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
  - "actual condition"
  - "actual problematic-for relation"
  - "applicability predicate"
  - "problem-for entity"
  - "relation occurrence"
---

### C.22.PFR:5 - Archetypal Grounding

**Engineering case: battery below the start bound.** The battery voltage-state relation is the actual-condition participant. A vehicle-start applicability relation carries the start predicate, exact vehicle, intended-start scope, and declared criterion-applicability window. Its actual extent is the maximal continuous period in which that applicability obtains. PFR obtains when the voltage condition is on the adverse side. An alarm, measurement report, or maintenance card may later support and publish that claim; none is the Problem occurrence.

**Formal case: a proof gap.** An unresolved-consequence relation is the actual-condition participant. A proof-acceptance applicability relation carries the exact proof-use entity, acceptance scope, predicate, and declared criterion-applicability window. PFR is actual for that proof use when the unresolved relation is adverse under the predicate; it need not be a Problem for every use of the proof episteme.

**Clinical case: patient-specific adversity.** A clinical-condition relation is the actual-condition participant. The applicability occurrence carries a patient-specific predicate, the patient as problem-for entity, admitted care scope, and declared criterion-applicability window. Diagnosis and assessment remain epistemes. PFR has no copied patient or diagnosis slot.

**Organizational case: hand-off failure.** A missed-transfer relation is the condition participant. A service applicability relation carries the service predicate, affected receiving work, scope, and declared criterion-applicability window. Coordination participants remain inside the missed-transfer relation; the receiving work is projected from applicability rather than duplicated in PFR.

**One condition, two affected uses.** One hot-surface condition is paired with two applicability occurrences carrying the same by-value predicate but different exact receiving work or system participants and scopes. When the condition is adverse under both applicability occurrences, two PFR occurrences obtain and are distinguished by their applicability-relation references; PFR copies neither receiving participant nor scope.

**Unnoticed and repaired.** A condition and applicability can make PFR obtain before monitoring exists. Selecting a repair method changes the solvability claim. Performing repair work that ends the adverse condition ends PFR; the work and its result relations remain separately governed.

