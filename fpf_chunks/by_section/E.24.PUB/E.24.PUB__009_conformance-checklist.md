---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__009_conformance-checklist.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:7 — Conformance Checklist"
line_start: 88683
line_end: 88697
dependencies:
  - "A.6.3"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.30.AD"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.UK"
  - "E.8"
  - "E.9.DA"
  - "F.19"
  - "U.EpistemePublication"
  - "U.View"
  - "U.Work"
keywords:
---

### E.24.PUB:7 - Conformance Checklist

| Check | Observable conformance condition |
| --- | --- |
| `CC-E24PUB-1` | The named receiving `U.Work` and the publication use it depends on are explicit. A claimed actual use names either the exact declared predicate, participant order, and actual values for a premise, reference, other participant, or work-to-referent use, or the identified A.6.1 application and exact declaration-local binding for a declared operation argument; otherwise the text stops at publication availability or returns the applicable A.15.1 `missing-governor` result. Choice work keeps its C.11 `ChoiceResult` separate from the Work and publication participants. |
| `CC-E24PUB-2` | The selected episteme edition, audience declaration, bounded-use declaration, publication form, and presentation carrier are distinguishable. |
| `CC-E24PUB-3` | `EpistemePublicationRelation` has the five exact participant meanings, the availability predicate, and the maximal-continuous-occurrence identity rule stated in section 4.1. |
| `CC-E24PUB-4` | `PublicationFormExpressionRelation` and `PublicationFormBearingRelation` are recoverable when expression or carrier availability is load-bearing. |
| `CC-E24PUB-5` | Plain `published episteme` is used only for contingent participation; `U.EpistemePublication` is not used as a durable kind. |
| `CC-E24PUB-6` | A `U.View` remains a same-individual dependent specialization of `U.Episteme` under an obtaining E.17.0 conformance relation; graphical appearance and A.6.3 construction alone supply no membership. |
| `CC-E24PUB-7` | C.29 representation elements and correspondence remain distinct from the publication form and direct subject-side objects. |
| `CC-E24PUB-8` | Publication work, actual access, reliance, evidence, decision, and performed work remain under their direct patterns. |
| `CC-E24PUB-9` | A changed edition, form, carrier, audience, or bounded use leads to the smallest affected object or relation rather than a whole-stack rewrite. |
| `CC-E24PUB-10` | Ordinary use stops at the readable sentence when no receiving work needs fuller relation detail. |

