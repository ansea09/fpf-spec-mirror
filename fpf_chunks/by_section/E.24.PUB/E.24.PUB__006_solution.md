---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__006_solution.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:4 — Solution"
line_start: 77437
line_end: 77516
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.22"
  - "C.2.1"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.UK"
  - "E.8"
  - "E.9.DA"
  - "F.19"
keywords:
---

### E.24.PUB:4 - Solution

Use a local relation-position field set before writing or revising publication-facing text. The field set names four different objects and the bounded use; it is not a new `U.*` kind, reusable record family, or coordination pattern.

```text
Ontic-description publication relation positions:
  OnticEoC:
  OnticDescriptionEpisteme:
  DescriptionClaims:
  Publication:
  PublicationForm:
  StructuralNamePressure:
  GovernedUse:
  BlockedOverread:
  NeighboringPatternIfCurrent:
```

Read the field set this way:

- `OnticEoC` is the ontic itself: for example `U.Ontic`, `U.Episteme`, `U.Structure`, `U.CharacteristicSpace`, `U.BoundedContext`, or another accepted ontic.
- `OnticDescriptionEpisteme` is the claim structure that describes the ontic and its slot relation.
- `DescriptionClaims` are the specific claims about identity, slots, admissible values, dependent patterns, invariants, examples, and use boundary.
- `Publication` is the made-available expression of that episteme.
- `PublicationForm` is the selected form: pattern host, card, record, table, schema, diagram, view, source packet, or another publication form.
- `StructuralNamePressure` names any `U.*`, type or kind wording, title, filename, heading, ToC row, table column, or record field whose visible publication position could over-admit kindhood.
- `GovernedUse` says what a user may do with the publication in the current pattern.
- `BlockedOverread` blocks the main confusion without listing every generic semio boundary.
- `NeighboringPatternIfCurrent` names the governing neighboring pattern when the current claim belongs elsewhere.

#### E.24.PUB:4.1 - Minimal Boundary Formula

When a subject pattern needs a publication boundary, use the shortest formula that preserves the EoC:

```text
This [publication form] publishes an ontic-description episteme about [OnticEoC].
It is not [OnticEoC].
Use it for [governed use].
Use [neighboring pattern] when the current claim is about [neighboring EoC].
```

Do not expand that local formula into a general catalogue of all things a description is not. If a neighboring EoC or claim is current, name the governing neighboring pattern and apply it for that EoC or claim.

#### E.24.PUB:4.2 - Description Claims Stay About the Ontic

An ontic-description episteme may claim:

- what identifies the ontic;
- which slot relation gives the ontic its structure;
- which values may fill the slots and which governing pattern owns each value;
- which invariants and non-use boundaries preserve the ontic;
- which dependent patterns may rely on the ontic;
- which examples show first use without turning the example form into the ontic.

It should not carry generic warnings about all possible uses of descriptions. Those warnings belong to `C.2.1`, `E.17`, `E.10`, `F.19`, source patterns, evidence patterns, gate patterns, decision patterns, or another subject pattern when that subject is current.

#### E.24.PUB:4.3 - Publication Forms Stay Downstream

A publication form may improve usability, inspection, currentness, source return, or multi-view handling. It does not decide ontology by itself.

Use this test:

1. If changing the table layout, card fields, diagram notation, or section order changes only how the ontic is published, the ontic is unchanged.
2. If changing a description claim changes what the ontic is asserted to be, inspect the ontic-description episteme through `C.2.1`.
3. If changing a slot relation or identity criterion changes the ontic itself, apply the governing ontic pattern or `E.24`.
4. If changing viewpoint or publication packaging changes which reader concern is served, use `E.17` or the relevant view or publication pattern.
5. If the publication form's title, filename, heading, ToC row, table column, or visible structural name carries `U.*` force while the primary EoC is not that U-kind, recover the governed object and use `E.24.UK` for structural-name U-kind settlement.

#### E.24.PUB:4.4 - Subject Pattern Placement

In a subject pattern, keep the positive subject spine first:

1. name the EoC and practical situation;
2. state identity, slot relation, invariants, first-use move, and governed use;
3. add one compact publication boundary only where needed;
4. when a description-use or publication-use claim is current, recover that claim and apply the neighboring pattern that governs it.

This prevents semio-bias. A pattern about architecture should teach architecture first. A pattern about structure should teach structure first. A pattern about characteristic space should teach characteristic space first. Publication and description boundaries protect those patterns; they do not become their main subject unless the pattern EoC is itself a description or publication.

If the EoC is a description, repeat the same test one level up. A pattern about an architecture description should center that description as the EoC; claims about descriptions of that description, publication of that description, and use of that publication stay in a bounded publication section or neighboring patterns.

