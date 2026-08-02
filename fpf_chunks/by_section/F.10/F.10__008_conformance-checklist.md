---
chunk_kind: "child"
pattern_id: "F.10"
pattern_title: "Status Families Mapping: Evidence, Standard, and Requirement Status"
section_id: "F.10:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/F.10/F.10__008_conformance-checklist.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "F.10 — Status Families Mapping: Evidence, Standard, and Requirement Status"
  - "F.10:7 — Conformance Checklist"
line_start: 92433
line_end: 92447
dependencies:
  - "A.2.4"
  - "B.3"
  - "F.1"
  - "F.18"
  - "F.3"
  - "F.9"
keywords:
  - "applicability windows"
  - "evidence"
  - "polarity"
  - "requirement"
  - "standard"
  - "status"
---

### F.10:7 - Conformance Checklist

| Check | Question |
| --- | --- |
| `CC-F10-01` Status family | Is the status value mapped to `EvidenceStatus`, `StandardStatus`, `RequirementStatus`, or another direct status pattern named by value? |
| `CC-F10-02` Context | Is the bounded context or edition that gives the status value meaning named? |
| `CC-F10-03` Target kind | Does the statement name the exact target kind: claim, quantity, method description, standard-governed entity, requirement clause, gate record, role assignment, work result, publication, or another direct-pattern target? |
| `CC-F10-04` Window | Does every positive or negative status name the window, edition, condition, freshness policy, or source-currentness relation that bounds it when current? |
| `CC-F10-05` Source and provenance | Is the status source, governing register, publication source, proof, measurement, verification, or provenance constraint recoverable when the use depends on it? |
| `CC-F10-06` Modality | Is epistemic status kept distinct from deontic standard or requirement status? |
| `CC-F10-07` Bridge | Does any cross-context comparison, explanation, or substitution cite an `F.9` bridge with kind, direction, congruence level, and loss? |
| `CC-F10-08` Substitution | If one status is substituted for another, do bridge kind, congruence level, window alignment, target kind, and local evaluation rule admit that substitution? |
| `CC-F10-09` No role ontology drift | Is there no claim that an episteme holds an evidence role, status role, standard role, or requirement role merely because it is used? |
| `CC-F10-10` Direct-pattern boundary | Are evidence provenance, assurance, causal use, source use, publication use, gate passage, permission, performed work, and work-role assignment governed by their direct patterns when those claims are current? |

