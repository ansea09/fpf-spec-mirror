---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:12"
section_title: "SoTA-Echoing - Source-Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__015_sota-echoing-source-use.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:12 — SoTA-Echoing - Source-Use"
line_start: 92851
line_end: 92871
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RCD"
  - "A.7"
  - "A.8"
  - "C.11"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
keywords:
  - "admission before naming"
  - "alias"
  - "designation"
  - "durable naming"
  - "governed value or relation"
  - "local phrase"
  - "proposed naming use"
  - "row use"
  - "subject before name"
---

### F.8:12 - SoTA-Echoing - Source-Use

**Qualification and selection rule.** These decisions are qualified on 2026-08-15 for the cited editions and the F.8 questions below. The set is deliberately small. ISO 704 and SKOS are current standards or durable lineage, not claimed as research frontiers. The gUFO–OBO row combines a current formal comparator with an operational ontology-maintenance practice. The Cedar row is a current research-and-practice comparator. A source belongs here because it changes an F.8 disposition or boundary, not because it is official, popular, or easy to find.

| Source, status, and question | Decision for F.8 | What F.8 uses and rejects | Affected loci and smallest source-driven revisit |
| --- | --- | --- | --- |
| [ISO 704:2022](https://www.iso.org/standard/79077.html), edition 4 — current international terminology standard. Question: how should an expression, its designation use, the concept or other subject, and any definition stay distinguishable? Its Pareto position here is the latest general standard that directly treats links among objects, concepts, definitions, and designations across fields; it is not presented as a research frontier. | **Adopt the subject-before-designation order; adapt its terminology distinctions to FPF values, relations, and subject patterns.** | Keep expression, designation, governed subject, and any description separate. Reject using terminology work to admit an ontic kind, and reject a full terminology entry when a local phrase is sufficient. | §§0, 4.1–4.3, and checks 01–08. Revisit only if a later ISO 704 edition or a better general terminology account changes the designation–subject–definition distinction or preserves it with lower practitioner cost. |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009 Recommendation — current standard and representation lineage for lightweight labels and concept schemes. Question: what can preferred and alternative labels, scheme placement, and mapping links support without importing class identity? Its Pareto position is the small, explicit label model and its stated non-entailments, not its age. | **Adapt preferred/alternative-label and scheme discipline as a reuse stress test.** | Preserve the selected-designation/alias split and local-sense scope. Reject RDF or SKOS as required FPF representation; reject same spelling, `skos:exactMatch`, or scheme membership as FPF identity, F.9 Bridge, kind admission, or wider F.17 use; do not require a cell merely to keep wording local. | §§4.1–4.4, 7.2, and checks 03–09. Revisit if a normative SKOS successor or a better lightweight label model changes these label or mapping boundaries. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint, read with the current [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) and its [term-stability rule](https://obofoundry.org/principles/fp-019-term-stability.html) — accepted synthesis for the new-kind question. gUFO supplies a current typology-of-types and relational-aspect comparator; OBO supplies operational scope, reuse, identifier, relation-reuse, and stable-referent pressure. Together they cover formal category discipline and maintained-vocabulary cost better than either alone. | **Adapt the category/label separation and reuse pressure.** | A spelling or source class does not establish an FPF kind. Test existing values, relations, scopes, and stable meanings before proposing another kind. Reject gUFO's hierarchy, OWL commitments, OBO's biomedical scope and IRI rules, and any external source as FPF admission authority. | The pre-admission stop in §§0 and 4.1–4.2, case 7.5, invariants 3 and 8, and checks 05 and 12. Revisit if gUFO's type distinctions or the cited OBO scope, reuse, or stability principles change materially, or a better account reduces admission burden without losing these distinctions. |
| Cutler et al., [Cedar](https://arxiv.org/abs/2403.04651), 2024, read with current Cedar 4 and [Verified Permissions policy-name and policy-id practice](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/terminology.html), checked 2026-08-15 — current research-and-operation comparator for policy references. Question: how should policy content, a name or identifier, request evaluation, and enforcement stay separate? Its Pareto position is a modern readable and formally analysed policy language with active operational use, not vendor popularity. | **Adapt only the separation of policy reference, policy content, evaluation, and effect.** | Keep a policy identifier resolvable to its specification and keep any decision occurrence, result, Work, or enforcement separate. Reject Cedar and AWS types, stores, API identifiers, and authorization semantics as FPF ontology; reject any inference that an identifier grants permission or makes a policy claim true. | The policy target and step 10, case 7.4, §8.1, and checks 10 and 13. Revisit if the cited line changes the separation among policy name or identifier, policy content, and decision, or a more general current source preserves it with less domain-specific machinery. |

**Internal FPF basis, not external SoTA.**

- F.14, F.5, F.17, and F.18 supply the local-phrase, designation, alias, row-use, and durable-naming ladder.
- A.2, C.3, F.4, A.2.1, F.6, and A.15.1 keep designation `L`, local system-role kind `K`, optional description `D`, assignment `A`, and performed Work distinct.
- E.24.CD, E.24.UK, A.8, and A.11 recover an unclear object and decide kind admission before F.8 names the result.
- A.6.RCD, C.11, C.2.1, and E.9 govern any accountable decision occurrence, separate result, result episteme, and policy-history record.
- F.1–F.3 and F.9 govern local-sense discovery and an obtaining Bridge; A.1.1 and A.22 govern any selected bounded-model-use Structure. F.8 cites those objects only when the naming use needs them.

**Source-use boundary.** External sources can supply candidate expressions, a comparison pressure, or a narrow representation test. They do not select the F.8 disposition, establish the governed subject, make a relation obtain, admit a kind, or grant authority. Those results remain with the named FPF pattern and the recovered facts.

