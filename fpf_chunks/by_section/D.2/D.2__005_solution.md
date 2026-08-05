---
chunk_kind: "child"
pattern_id: "D.2"
pattern_title: "Multilevel Ethics For Holon Work"
section_id: "D.2:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.2/D.2__005_solution.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "D.2 — Multilevel Ethics For Holon Work"
  - "D.2:2 — Solution"
line_start: 68588
line_end: 68614
dependencies:
  - "A.1"
  - "A.15"
  - "A.3.4"
  - "B.1"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
  - "D.3"
  - "D.4"
  - "D.5"
keywords:
---

### D.2:2 - Solution

Open a `MultilevelEthicsEntry@Context`:

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  boundedContextRef
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  roleAssignmentRefs
  interestOrConcernRefs
  capabilityOrFunctioningConcernRefs?
  methodOrWorkRefs?
  transformationRefs?
  expectedConsequenceRefs
  evidenceRefs
  uncertaintyOrCurrentnessCondition
  nextOwnerRef
```

The entry record has one job: recognize that multilevel ethics is live and choose the next owner. It does not itself resolve the conflict.

For this pattern, holon work includes material systems and epistemes when they are the affected EntityOfConcern. An architectural description, standard, model card, policy publication, or research program may be the affected episteme; the pattern still asks which levels, scopes, affected holons, interests, responsibilities, and consequences are live.

