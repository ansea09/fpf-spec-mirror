---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuated Relation Occurrences"
section_id: "A.6.REL:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__003_problem.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuated Relation Occurrences"
  - "A.6.REL:2 — Problem"
line_start: 11609
line_end: 11622
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

### A.6.REL:2 - Problem

When a later engineering use needs one obtaining relation occurrence to remain distinguishable from another, descriptions often state five different claim contents as if one assertion or identifier established them all. The claims have this dependency order; the order does not turn them into five project-time decisions:

1. the direct relation obtains for the named participants, those participants jointly satisfy its semantic predicate, one occurrence therefore exists, and the direct identity rule governs its reidentification and distinction from another occurrence;
2. FPF ontology settlement already admits occurrences of that relation kind under `U.Relation`; the direct pattern states the relation-specific participant meanings, obtaining condition, and occurrence-identity rule, while a compatible `RelationSignature` episteme declares corresponding SlotSpecs for reusable descriptions;
3. a system performing explicit-individuation work applies the admitted identity rule so the named receiving use can recoverably distinguish one occurrence; a separate relation-occurrence description episteme is produced only when the selected receiver needs that description;
4. an identifier designates that already recoverable occurrence under a reference scheme;
5. the selected receiving object is either an episteme whose content designates that occurrence, another direct relation that has the occurrence as a participant, or an assertion episteme whose content states that one exact A.6.1 operation application binds the occurrence as its actual argument value under one named `ArgumentDeclaration`.

The later claim contents do not make the earlier relation obtain. Root `U.Relation` admission is a corpus ontology decision governed by `E.24.UK`. `A.6.REL` supplies the common occurrence discipline, while each direct relation pattern supplies the relation-specific participant meanings, obtaining condition, and occurrence-identity rule used as the admission witness. Project work does not repeat that classification decision. A system performing explicit-individuation work applies the direct identity rule so one existing occurrence is recoverably distinguishable for the current use; that work neither creates the occurrence nor by itself requires a separate description episteme. A system performing naming work may subsequently associate a designator with the occurrence, and a receiving episteme may subsequently contain a reference that designates it.

Relation-heavy work often begins from a table row, graph edge, identifier, or reified statement. An engineer can then mistake the represented row, edge, identifier, or reifier identity for world-side relation identity. Applying this method permits exact use of relation-occurrence identity without reversing representation and ontology and without forcing a relation-occurrence description episteme into every readable sentence.

