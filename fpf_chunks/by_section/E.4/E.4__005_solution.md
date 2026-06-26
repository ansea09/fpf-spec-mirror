---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__005_solution.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:4 — Solution"
line_start: 63754
line_end: 63824
dependencies:
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.1"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.19"
  - "E.2"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.5.3"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4:4 - Solution

Describe an FPF-grounded pattern ecosystem as a family of framework editions and publication units over selected structures, then route each claim to the pattern that owns that kind of work.

Create a family-and-structure map with these fields:

```text
FPFFamilyAndStructureMap@Context:
  ecosystemScopeRef
  boundedContextRef
  frameworkFamilyMembers
  selectedPatternSetRefs
  selectedRelationRecordRefs
  selectedDependencyAndEditionRefs
  selectedPublicationUnitRefs
  selectedSourcePackRefs
  selectedDecisionRefs
  qualityAndImprovementRefs
  currentnessAndRefreshRefs
  blockedOverreadRefs
  receivingPatternRefs
```

This map is a context record. It is not a new root kind and not a substitute for the patterns that own the referenced claims.

Classify the family members as follows:

`Conceptual Core` is the legacy authority and publication-family partition. `FPF Core pattern set` is the framework-edition view of the general FPF Core used for dependency, relation, and edition reasoning. They are two views over the Core, not two competing core objects.

| Family member | Architecture role | Main owners |
| --- | --- | --- |
| Conceptual Core | Core FPF distinctions, rules, and patterns that other FPF-grounded frameworks depend on. | `E.4`, `E.5.3`, direct pattern owners |
| Tooling Reference | Optional tools, schemas, scripts, machine checks, or helper publications that inspect or support FPF use. | `E.17`, `G.5`, relevant tool patterns |
| Pedagogical Companion | Tutorials, playbooks, worked examples, and learning material that teach FPF without changing Core meaning. | `E.17`, didactic patterns |
| Foundational principle pattern set | Foundational threshold material or principle patterns that may support FPF-grounded use but need settled names and dependency boundaries. | `F.18`, `E.4.PFR` |
| FPF Core pattern set | The current general FPF pattern core as a framework edition. | `E.4`, `E.5.3`, Core pattern owners |
| Domain principle framework | A domain-bounded framework grounded in FPF and in domain SoTA. | `E.4.DPF`, `G.2`, `E.4.PFAD`, `E.4.PFR` |
| Local practice framework | A project, organization, or role-context framework grounded in FPF and often in a domain framework. | `E.4.DPF`, `E.4.PFAD`, `E.4.PFR`, `G.11` |

The ordinary method is:

1. Declare the ecosystem scope and bounded context.
2. Name the family member being created, used, or changed.
3. List the selected structures that matter for the architecture claim: pattern set, pattern-use relations, pattern-framework relations, decision records, dependency and edition records, publication units, source packs, quality records, and currentness records.
4. Apply `E.5.3`: dependencies point toward more stable framework editions. FPF Core does not depend on domain or local frameworks.
5. Send publication and first-entry claims to `E.11` and `E.17`.
6. Send pattern-use recommendation claims to `E.11.PUR`.
7. Send architecture-decision claims for a framework to `E.4.PFAD`, and general project architecture decisions to `C.32.PAD`.
8. Send relation, dependency, compatibility, deprecation, and edition claims to `E.4.PFR`.
9. Send naming settlement to `F.18`.
10. Send SoTA and source-pack claims to `G.2`.
11. Send currentness, refresh, and edition-change claims to `G.11` and the edition owners.
12. Before using a monolith, table of contents, relation graph, summary, or generated carrier as evidence, state source-return or preservation through `C.33`, `C.34`, or `C.35`.
13. Evaluate framework and pattern adequacy through `E.21`, improve through `E.23`, and use `E.19` only when the local process asks for admission review.

Use this routing table when a proposed change is ambiguous:

| Proposed work | Route to | Blocked overread |
| --- | --- | --- |
| A distinction, rule, or pattern must govern ordinary FPF use across many domains and downstream frameworks depend on it. | FPF Core amendment through the current campaign and direct pattern owners. | Do not promote a local checklist or domain technique to Core merely because it is useful. |
| A reusable principle supports FPF-grounded work but is not a general Core rule for all domains. | Foundational principle pattern set or other named framework edition, with `E.4.PFR` dependency records. | Do not hide a new framework edition inside the Core table of contents. |
| A source tradition or professional domain needs FPF-shaped patterns. | Domain principle framework through `E.4.DPF`, `G.2`, `E.4.PFAD`, and `E.4.PFR`. | Do not treat a literature summary as the framework. |
| One project, organization, role, or tool setting needs local practice guidance. | Local practice framework through `E.4.DPF`, with local source, owner, publication, quality, and refresh records. | Do not make local policy a general FPF rule. |
| Existing material is hard to find, teach, or publish. | `E.11`, `E.17`, `G.5`, or the relevant publication and pedagogy owner. | Do not call publication repair architecture repair. |
| A cross-reference claims use, specialization, dependency, publication, source reuse, preservation, quality, deprecation, or supersession. | `E.4.PFR` for the relation function and edition effect. | Do not let a link label decide the relation meaning. |
| A framework split, dependency boundary, publication unit, or adoption consequence must be decided. | `E.4.PFAD`; use `C.32.PAD` or `C.32.ADR` for project architecture decisions. | Do not replace the decision with a diagram, folder, or package manifest. |
| A source, search result, transformed view, or generated carrier supplies candidate material. | `G.2`, `C.33`, `C.34`, or `C.35` before architecture use. | Do not treat a carrier as authoritative because it has plausible names. |
| Quality, repeated improvement, admission gating, or currentness is the live problem. | `E.21`, `E.23`, `E.19`, and `G.11` according to the claim. | Do not run all quality gates when only one evaluation or refresh owner is live. |

This pattern should leave the reader with one architecture sentence: "This framework edition belongs to this family member, depends on these stable editions, publishes through these carriers, preserves these selected structures, and sends each non-owned claim to this receiving pattern."

