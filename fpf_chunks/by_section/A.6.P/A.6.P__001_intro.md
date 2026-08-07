---
chunk_kind: "child"
pattern_id: "A.6.P"
pattern_title: "Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims"
section_id: "A.6.P:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.P/A.6.P__001_intro.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.6.P — Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims"
  - "A.6.P:intro — Intro"
line_start: 15708
line_end: 15719
dependencies:
  - "A.1.SCR"
  - "A.1.STM"
  - "A.10"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.B"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "F.9"
keywords:
---

## A.6.P - Relational Precision Restoration - Recovering Direct Relations from Under-Specified Claims

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Relation precision restoration.

**Mint or reuse.** This pattern reuses direct relation kinds, direct obtaining predicates, relation-participant meanings, `RelationSignature`, `SlotSpec`, `U.Relation`, `U.Episteme`, designators, references, descriptions, publications, and representations from the patterns that define or constrain those relations and objects. It introduces no U-kind, universal record-shaped relation object, qualification object, or generic relation-change object. A `RelationKind` token designates an already settled relation kind in a local or public vocabulary; the token is neither the kind nor an occurrence.

**Plain object stack.** A direct relation is what obtains among its actual participants under the participant meanings and obtaining condition stated by its direct pattern. Each participant keeps its independently governed kind. A compatible `RelationSignature` is a declaration episteme; one declaration-local `SlotSpec` can correspond to one participant meaning when reusable typed use is current. An assertion or occurrence-description episteme may designate the participants or an already recoverable occurrence. A table row, tuple, record, graph edge, functional expression, or arrow is a representation only through an explicit `C.29` correspondence. None of those epistemic or representational objects makes the relation obtain or supplies occurrence identity by form.

