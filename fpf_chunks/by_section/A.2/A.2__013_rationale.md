---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "System-Role Kinds and Assignments"
section_id: "A.2:11"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__013_rationale.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "A.2 — System-Role Kinds and Assignments"
  - "A.2:11 — Rationale"
line_start: 3349
line_end: 3363
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10.ROLE"
  - "F.4-F.6"
keywords:
  - "U.SystemRoleAssignment"
  - "ambiguous role wording"
  - "assignment"
  - "holder System"
  - "local System classification"
  - "system-role kind"
  - "work-facing contribution"
---

### A.2:11 - Rationale

System-role kinds solve a local classification problem. System-role assignments solve a relation-occurrence problem. The pump does not become another system because its contribution changes, and a kind does not become an assignment because one system currently counts under it.

The architecture therefore keeps these levels separate:

1. the local system-role kind, its candidate domain, work-facing membership distinction, boundary probes, continuity rule, and useful definition provenance;
2. the `KindSignature` and one C.3.2 judgment over a system and slice;
3. any directly declared `U.SystemRoleAssignment` occurrence;
4. direct neighboring relations for state, capability, Method, Work, responsibility, commitment, permission, authority, evidence, reliance, description, and publication.

A system-role kind is not a holon merely because its description has internal fields. Proposed “parts” repeatedly resolve into other kinds, relation predicates, assignments, Method or Work structures, or parts of description epistemes. The useful structure is the exact relation structure governed by A.2.7, not role mereology.

Semantic locality needs no universal context participant. C.3's candidate domain, operative membership distinction, boundary probes, and continuity rule recover the kind. A practice or source reference locates the definition and warns where comparison may be needed; it is not an identity participant. An assignment species declares only its real participants. A receiving assertion or use can cite a selected model-use structure when that structure actually changes interpretation.

