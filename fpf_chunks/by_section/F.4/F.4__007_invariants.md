---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "SystemRoleKindDescription — Describing an Exact System-Role Kind"
section_id: "F.4:5"
section_title: "Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__007_invariants.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.4 — SystemRoleKindDescription — Describing an Exact System-Role Kind"
  - "F.4:5 — Invariants"
line_start: 91867
line_end: 91880
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "C.3.2"
  - "E.10.D2"
  - "E.10.ROLE"
  - "E.24"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.5"
  - "F.9"
keywords:
  - "classification criterion"
  - "description episteme"
  - "effective scheme"
  - "local kind"
  - "non-inference boundary"
  - "system-role-kind description"
---

### F.4:5 - Invariants

1. **One described kind.** A `SystemRoleKindDescription` describes exactly one local system-role kind.
2. **Direct kind identity.** Bounded context, contribution identity, and current criterion remain recoverable; taxonomy rows and schemes are evidence or interpretation aids, not identity authorities.
3. **Description boundary.** The description is a `U.Episteme`; it is not the kind, candidate, classification judgment, assignment, holder system, capability, Method, Work, or status-use relation.
4. **System range.** A candidate must independently pass A.1 as `U.System`. No description or kind name performs that admission, and `SystemRole` does not narrow the candidate to non-human technical systems.
5. **No hidden assignment.** Classification under a local kind neither creates nor proves a `U.SystemRoleAssignment` occurrence.
6. **No hidden capability.** Capability requirements may be cited, but the description proves no capability.
7. **No hidden Method.** Method requirements may be cited, but the description is not a MethodDescription.
8. **No hidden Work.** The description may support later Work-attribution checks, but it is not evidence that Work occurred.
9. **No status or episteme-use fusion.** Status, evidence, source, requirement, publication, and assurance uses remain direct relations, not another description branch.
10. **Position discipline.** Bare *role* that denotes participation, a declaration slot, interface place, or representation position is recovered through E.10.ROLE and A.6.RSIR rather than made a system-role kind.
11. **Name after meaning.** Durable naming follows F.18 only after the exact kind, description, scheme, and local sense are recovered.

