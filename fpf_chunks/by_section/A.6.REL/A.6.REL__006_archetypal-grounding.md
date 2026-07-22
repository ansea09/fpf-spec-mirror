---
chunk_kind: "child"
pattern_id: "A.6.REL"
pattern_title: "Relation Obtaining and Individuated Relation Occurrences"
section_id: "A.6.REL:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.REL/A.6.REL__006_archetypal-grounding.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.6.REL — Relation Obtaining and Individuated Relation Occurrences"
  - "A.6.REL:5 — Archetypal Grounding"
line_start: 10700
line_end: 10738
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

### A.6.REL:5 - Archetypal Grounding

#### A.6.REL:5.1 - Physical assembly through the relation-object architecture

Start with `Bearing_B isPartOf Pump_P` and trace only the objects needed by the current use.

1. **World-side entities and occurrence.** `Bearing_B` and `Pump_P` retain their independently governed holon kinds and names. In this occurrence, the bearing participates under the installed-part meaning and the pump under the assembly-whole meaning. The direct installed-part relation obtains while its domain predicate is satisfied.
2. **Relation-kind settlement.** The direct parthood pattern contains the two relation-participant meanings, the installed-part obtaining predicate, and the occurrence-identity rule. The identity rule states whether continuity is determined by one maximal continuous installation interval, constituting installation work, or another exact world-side discriminator stated by that pattern.
3. **Reusable declaration.** When several maintenance assertions use one `InstalledPartRelationSignature`, that signature contains `InstalledPartSlot` and `AssemblyWholeSlot`. Each SlotSpec states `U.Holon` as ValueKind and `U.HolonRef` as RefKind. These SlotKinds are declaration-local names corresponding to the two relation-participant meanings.
4. **Assertion and relation-participant designations.** A maintenance assertion may use `InstalledPartSlot` as the field label and `Bearing_B_Ref` as its value, and `AssemblyWholeSlot` with `Pump_P_Ref`. The two reference values are relation-participant designations. Resolution under the effective reference scheme yields the bearing and pump; the assertion content claims that the direct relation obtains. If current maintenance work needs no occurrence identity, the engineer stops here.
5. **Occurrence identity, designator, and reference.** A system performing reliability-analysis work compares the installation before removal with the installation after reinstallation. A system performing relation-identification work applies the direct identity rule and distinguishes two occurrences when the exact world-side discriminator stated by that rule differs. A system performing naming work can then associate a designator such as `Bearing_B installation in Pump_P, episode 2` with the second occurrence. A `U.EntityRef` constrained to the installed-part relation kind may serve as its relation-occurrence reference for a receiving reliability assertion.
6. **Representation.** A database row or diagram edge may represent the assertion episteme or relation-occurrence description episteme under `C.29`. Its key, fields, and edge endpoints keep their representation-side meanings. A declared C.29 correspondence relates each representation element to the assertion field, relation-participant designation, or occurrence reference used by the receiving episteme; row or edge identity does not replace the direct occurrence-identity rule.

The practical payoff is visible at each stop. Ordinary maintenance work keeps the readable relation sentence. Repeated typed assertions add the signature and designations. A system comparing repeated installation episodes performs explicit-individuation work when the comparison depends on occurrence identity. Stable cross-reference use motivates naming and reference work. No earlier object is renamed as a later one.

#### A.6.REL:5.2 - Repeated role assignment

**Tell.** `Robot_7 holds InspectorRole` is sufficient while the current assignment alone matters.

**Show identity-dependent use.** The robot holds the role during two separated inspection intervals, and later work attribution names the assignment current during the second work occurrence. Under `A.2.1`, each assignment occurrence is identified by its fixed holder, role value, role-taxonomy episteme, effective reference scheme, and one uninterrupted obtaining interval. The demonstrated gap ends the first occurrence; later resumption begins another. The attribution assertion explicitly designates the second occurrence. Assignment-signature, assertion, and roster epistemes may describe the assignment; an evidence relation may connect one of those epistemes to an attribution assertion about the assignment. Under a publication-relation occurrence, one selected edition may be available to its declared audience and use. None constitutes the assignment merely by form.

#### A.6.REL:5.3 - Formal reduced case

The expression `3 < 5` is assertion content written in a mathematical notation. Under the referenced arithmetic structure, the values three and five satisfy the less-than predicate. The expression is not thereby a relation occurrence. No receiving use in this case needs the obtaining less-than relation occurrence explicitly individuated under `U.Relation`, so the engineer stops at the assertion. A graph edge or RDF reifier introduced by tooling remains a representation of the proposition or assertion and is not an occurrence-identity rule in the formal subject domain.

#### A.6.REL:5.4 - Relation occurrence as a participant

`C.22.PFR` has one actual-condition relation occurrence and one problem-criterion-applicability relation occurrence as world-side participants. Each is individuated under its own direct identity rule. The PFR direct pattern states those two participant meanings, its obtaining condition, and its identity rule; the PFR `RelationSignature` episteme declares the corresponding SlotSpecs. A PFR assertion designates the two occurrences according to those SlotSpecs. PFR is a direct relation, not an episteme whose content merely groups two assertions.

#### A.6.REL:5.5 - Description and publication recursion through the relation-object architecture

Let `R1` be an already individuated installed-part relation occurrence between a bearing and a pump.

1. An installation-description episteme `E1` has `R1` as its EntityOfConcern. In the C.2.1 declaration, the entity-of-concern relation-participant meaning corresponds to `EntityOfConcernSlot`. In a card representation of `E1`, the field label `entityOfConcernRef` corresponds to that SlotKind and its `U.EntityRef` value is a relation-participant designation that resolves to `R1`.
2. A second episteme `E2` contains the result of evaluation work concerning the adequacy of `E1`. Its own `EntityOfConcernSlot` designation resolves to `E1`, not to `R1`. The two epistemes therefore have different EntitiesOfConcern and retain separate C.2.1 identities: `E1` describes `R1`, while `E2` evaluates the adequacy of `E1`.
3. Under a publication-relation occurrence, the current edition of `E1` is available to a declared audience and use. The selected episteme edition is an actual participant of that publication relation under the publication pattern's participant meaning. The publication form and its representation elements retain their own kinds and correspond to the published episteme only through the declared publication and representation relations.

A system performing revision work can establish another edition of `E1` or `E2`; a system performing publication work can establish another publication-relation occurrence for a selected edition. `R1` continues or ceases only as the installed-part obtaining predicate and occurrence-identity rule determine. This recursive case preserves the distinction: a description episteme can itself become the actual participant or EntityOfConcern of another relation without becoming the relation occurrence it describes.

