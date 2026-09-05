---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__006_solution.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:4 — Solution"
line_start: 92019
line_end: 92140
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
keywords:
---

### E.24.PUB:4 - Solution

Start with this readable publication statement:

> Publication occurrence `<P>` makes episteme edition `<E>` available to the audience identified by `<A>` for the use bounded by `<U>`, through publication form `<F>` borne by presentation carrier `<C>`.

The sentence names the five participant meanings without asking the user to fill a record. If it supplies the publication distinction needed by the receiving use, stop. If availability, identity, or a change is disputed, recover the three direct relations below.

#### E.24.PUB:4.1 - Identify the publication occurrence

`EpistemePublicationRelation` is the direct relation kind whose occurrence makes one selected episteme edition available to a declared audience for a declared bounded use.

Its actual participants are:

| Participant meaning | Admitted value | What the value supplies |
| --- | --- | --- |
| selected episteme edition | one exact `U.Episteme` identified under `C.2.1` | the claims made available |
| audience declaration | one `U.Episteme` whose claims identify the intended receiving entities or a C.3-governed local kind and its membership criterion | who is included; a reader label alone is insufficient when the boundary matters |
| bounded-use declaration | one `U.Episteme` whose claims state the operations or decisions supported, the conditions of that use, and the excluded stronger use | what availability is for; actual reliance remains another relation |
| publication form | one exact `U.Entity` used as the selected arrangement, notation, or rendering convention that expresses the edition for the bounded use | how the edition is expressed; visible shape alone does not establish this use |
| presentation carrier | one exact `U.PresentationCarrier` | what physically or digitally bears the selected form |

The use of common `U.Entity` for the publication-form participant does not admit a universal publication-form U-kind. `Publication form` is a relation-defined participant meaning here: the exact entity keeps the more specific kind and identity supplied by its direct pattern, and it fills `PublicationFormSlot` only while `PublicationFormExpressionRelation` obtains for the selected edition and bounded use. This is one predicate over a real common kind, not a prose union of cards, tables, diagrams, and files. E.8 governs FPF pattern form; E.17 governs multi-view publication forms and faces; a domain publication pattern may govern another form.

The reusable declaration is:

```text
EpistemePublicationRelationSignature:
  RelationKind: EpistemePublicationRelation
  SlotSpecs:
    SelectedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    AudienceDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    PresentationCarrierSlot: ValueKind=U.PresentationCarrier, refMode=U.EntityRef, Required
```

These SlotKinds name participant meanings only inside this `RelationSignature`. They do not create five new U-kinds, and a card field with a similar label does not become one of these SlotSpecs.

The audience-declaration episteme identifies the audience criterion; it is not the audience and does not prove access by any particular system. A concrete system's access, reading, reliance, or later work is another direct relation or work occurrence. This lets one publication be available to every entity satisfying a stable criterion without inventing `U.Audience` or treating a changing set of readers as changing participants of the same publication occurrence.

`EpistemePublicationRelation` obtains while all of the following are true:

1. `PublicationFormExpressionRelation` relates the selected edition, publication form, and bounded-use declaration;
2. `PublicationFormBearingRelation` relates the exact carrier and publication form;
3. entities admitted by the audience declaration can obtain the expressed edition from that carrier under the conditions stated by the bounded-use declaration;
4. the selected edition, declarations, form, and carrier remain the identified participants of this occurrence.

One occurrence is reidentified by those five fixed participants and their maximal continuous interval of availability. Changing any participant yields another publication occurrence. Demonstrated loss of availability followed by restoration yields a later occurrence. Missing or stale evidence leaves current obtaining unresolved; it does not prove a gap.

Rendering, printing, uploading, indexing, or granting access are activities separate from the publication occurrence. If one is independently claimed as dated Work, apply its direct Work and attribution patterns; E.24.PUB does not restate their admission, assignment, or compact-reporting rules. The activity and any result remain separate from the publication-relation participants.

#### E.24.PUB:4.2 - Recover expression and bearing only when needed

`PublicationFormExpressionRelation` relates one selected episteme edition, one exact publication form, and one bounded-use declaration. It obtains when the form expresses enough of that edition, under its effective reference scheme, for the declared use. One occurrence is reidentified by those three fixed participants and their maximal continuous interval of predicate truth. Omission, coarsening, changed notation, or changed admitted operations can end this relation even while the carrier remains unchanged. `A.6.3`, `C.29`, or `E.17` governs the more specific preservation, loss, view, or representation claim when that claim is current.

`PublicationFormBearingRelation` relates one exact `U.PresentationCarrier` and one exact publication form. It obtains while that carrier bears or renders that form as the same recoverable form. One occurrence is reidentified by the two fixed participants and their maximal continuous interval of bearing. Changing a filename or storage address does not by itself settle carrier identity; apply the carrier's direct identity and currentness pattern.

Their reusable declarations are:

```text
PublicationFormExpressionRelationSignature:
  RelationKind: PublicationFormExpressionRelation
  SlotSpecs:
    ExpressedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required

PublicationFormBearingRelationSignature:
  RelationKind: PublicationFormBearingRelation
  SlotSpecs:
    PresentationCarrierSlot: ValueKind=U.PresentationCarrier, refMode=U.EntityRef, Required
    BornePublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

These supporting relations prevent two shortcuts. A form does not make itself available, and a carrier does not express claims merely by storing bytes, ink, or another physical state. The publication occurrence depends on both relations but remains a distinct availability occurrence.

#### E.24.PUB:4.3 - Use progressive explicitness

Use the smallest statement that supports the current work:

1. **Ordinary use:** name the selected episteme edition, audience, bounded use, form, and carrier in one sentence.
2. **Changed-object use:** say which one of those objects changed and which relation must be re-evaluated.
3. **Contested availability:** state the `EpistemePublicationRelation` participants, obtaining evidence, and occurrence identity.
4. **Contested expression:** open `PublicationFormExpressionRelation` and the exact view, representation, preservation, or loss pattern.
5. **Contested carrier availability:** open `PublicationFormBearingRelation` plus the direct carrier-currentness or access pattern.

Do not materialize all five levels as a standing publication card. Stop as soon as the receiving use can distinguish the operative object and relation.

#### E.24.PUB:4.4 - Classify the encountered form by current use

Ask one question at a time:

| Current question | Governed object or relation |
| --- | --- |
| Does the filled card, diagram, or record carry identifiable claims about an EntityOfConcern under an effective reference scheme? | a `U.Episteme` under `C.2.1` |
| Does `EpistemeViewpointConformanceRelation(E,P)` obtain for that episteme E and at least one exact viewpoint episteme P? | the same E has dependent-kind membership as `U.View` under `E.17.0`; any A.6.3 construction remains a separate optional relation |
| Is an arrangement, notation, or rendering convention selected to express the edition for this bounded use? | the publication-form participant of `PublicationFormExpressionRelation` |
| Do selected elements correspond to independently recovered objects and change the admitted modeling or reasoning operations? | a C.29 representation and its correspondence |
| Does a physical or digital entity bear the form? | a `U.PresentationCarrier` in `PublicationFormBearingRelation` |
| Is the selected edition available to the declared audience for the declared use through that form and carrier? | one `EpistemePublicationRelation` occurrence |

The answers can be jointly positive because they concern different objects or relations. They do not follow from the words `card`, `record`, `table`, `schema`, `diagram`, `view`, `file`, or `publication` alone.

#### E.24.PUB:4.5 - Keep direct verbs with their relations

- an episteme carries claims and designations;
- a `U.View` is the same episteme individual for which E.17.0 conformance to at least one exact viewpoint episteme obtains;
- a publication form expresses a selected episteme edition for a bounded use;
- a C.29 representation stands in a declared correspondence to independently recovered objects;
- a presentation carrier bears a publication form;
- a publication occurrence makes one selected episteme edition available;
- a system may perform publication activity and may later access or rely on the published episteme, but those are separate claims under their direct patterns; publication availability establishes none of them;

A designator designates and a governed reference resolves to a referent. Neither operation publishes, bears, represents, or makes the subject-side predicate obtain.

#### E.24.PUB:4.6 - Keep subject patterns subject-first

In a pattern about an ontic, structure, architecture, characteristic space, method, or another subject, explain the subject's identity, relations, practical problem, and solution before publication details. Add E.24.PUB only when the receiving use depends on distinguishing the description, selected edition, form, carrier, audience, or bounded use.

When the EntityOfConcern is itself a description episteme, the same rule applies one level up. The description stays the subject; publication of that description is a neighboring relation.

