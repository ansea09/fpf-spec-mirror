---
chunk_kind: "child"
pattern_id: "F.6"
pattern_title: "SystemRoleAssignment and Performed-Work Attribution Check"
section_id: "F.6:13"
section_title: "SoTA-Echoing and Source Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.6/F.6__015_sota-echoing-and-source-use.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "F.6 — SystemRoleAssignment and Performed-Work Attribution Check"
  - "F.6:13 — SoTA-Echoing and Source Use"
line_start: 94526
line_end: 94539
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.3"
  - "A.6.9"
  - "A.6.REL"
  - "C.3.3"
  - "E.10.ROLE"
  - "E.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.9"
keywords:
  - "already admitted U.Work"
  - "complete post-admission A.13/A.15.1/F.6 basis"
  - "conditional profile"
  - "deprecated performedBy compatibility only"
  - "direct case fact"
  - "exact Work-assignment relation"
  - "holder equality"
  - "performedUnderAssignment"
  - "same obtaining A.13 assignment"
  - "separate evidence"
  - "temporal coverage"
---

### F.6:13 - SoTA-Echoing and Source Use

**Internal basis, not an external SoTA claim.** A.2.1 and A.6.5 supply the declaration-local slot, domain, and participant-value discipline. A.2.5 keeps assignment state distinct from the assignment occurrence. A.6.REL supplies relation obtaining and occurrence identity. A.15.1 supplies dated Work and the actual-performer basis. F.6 uses these as its governing FPF neighbours; they do not replace comparison with external work.

| Source and status | Decision for F.6 | What F.6 uses and does not import | Affected loci and smallest source-driven revisit |
| --- | --- | --- | --- |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint — current ontology comparator for this narrow question | **Adapt.** Use its separation of classification, relational aspects, and relation occurrences to test whether F.6 keeps a system-role kind, an assignment species, an assignment occurrence, and Work–assignment attribution distinct. | Keep the distinctions. Do not import gUFO's category hierarchy, OWL commitments, reified-aspect design, or a direct identity between a gUFO category and an FPF kind. | §§4.1–4.3 and the assignment examples. Revisit them if this source materially changes the distinctions used here or a better direct Work–assignment account preserves more of FPF's identity and use requirements without greater practitioner burden. |
| W3C [PROV-O](https://www.w3.org/TR/prov-o/), 2013 Recommendation — representation lineage | **Adapt as a representation contrast.** Its qualified association keeps activity, agent, role, and plan separately addressable. | Use the separation when checking reports and provenance. Do not treat a PROV association as an FPF assignment occurrence, its role as a system-role kind, its activity as dated Work, or a provenance record as proof that attribution obtains. | §§4.2, 4.5, and §7.3. Revisit only if the qualified-association meaning used in this contrast changes materially. |
| [OCEL 2.0 Specification](https://www.ocel-standard.org/2.0/ocel20_specification.pdf), 2023 — event-log stress test | **Adapt as a logging stress test.** Its separate events, objects, and qualified relations test whether an exported log can preserve the identities F.6 needs. | Use the separation, not the log's identities as the world-side ontology. An event is not thereby FPF Work, a qualifier is not thereby an assignment or system-role kind, and a row does not establish that attribution obtains. | §§4.2, 7.2, and 7.3. Revisit only if the event/object/qualified-relation structure used by this test changes materially. |

The comparison is qualified on 2026-08-15 for this question and these source editions. gUFO is the current comparator because it directly addresses the classification–relational-aspect–occurrence separation at issue; PROV-O and OCEL answer narrower representation and logging questions and therefore serve as lineage and stress tests. A new edition number, publication status, or harmless wording change does not reopen the comparison. A material change to a distinction used above, or a competitor that offers a better direct Work–assignment attribution solution with at least the same exactness, readability, and use cost, reopens only the affected row and F.6 loci.

**Refresh by meaning, not by publication.** If A.2.1 or A.6.5 changes how an assignment species declares slot domains or how an occurrence supplies participant values, revisit §§4.3, 5, 7.1, and 9. If A.6.REL changes relation obtaining or occurrence identity, revisit §§4.1–4.2, 5, 7, and 9. If A.15.1 changes the actual-performer or covering-assignment basis, revisit §§4.4–4.6, 7, and 9. If a better direct Work–assignment solution changes the source decision, revisit §13 and only the solution or examples that depend on it. Wording or publication changes that leave these meanings intact require no refresh.

