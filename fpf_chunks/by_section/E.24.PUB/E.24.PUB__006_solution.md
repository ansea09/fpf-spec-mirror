---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Episteme Publication: Availability, Form and Carrier"
section_id: "E.24.PUB:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__006_solution.md"
commit_sha: "d5df418106507cff0972788834c0bf8825597de0"
heading_path:
  - "E.24.PUB — Episteme Publication: Availability, Form and Carrier"
  - "E.24.PUB:4 — Solution"
line_start: 117080
line_end: 117251
dependencies:
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "A.6.REL"
  - "C.2.1"
  - "C.29"
  - "C.3.2"
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

> Publication occurrence `<P>` makes episteme `<E>` available to the audience identified by `<A>` for the use bounded by `<U>`, through expression `<X>` recoverable from carrier `<C>`.

The sentence names the five participant meanings without asking the user to fill a record. If it supplies the distinction needed by the receiving use, stop. When the selected expression follows reusable form F and that conformance matters, name F separately. For disputed availability, identity or change, recover the predicates below.

#### E.24.PUB:4.1 - Identify the publication occurrence

`EpistemePublicationRelation` is the direct relation kind whose occurrence makes one selected episteme edition available to a declared audience for a declared bounded use.

Its actual participants are:

| Participant meaning | Admitted value | What the value supplies |
| --- | --- | --- |
| selected episteme edition | one exact `U.Episteme` identified under `C.2.1` | the claims made available |
| audience declaration | one `U.Episteme` whose claims identify the intended receiving entities or a C.3-governed local kind and its membership criterion | who is included; a reader label alone is insufficient when the boundary matters |
| bounded-use declaration | one `U.Episteme` whose claims state the operations or decisions supported, the conditions of that use, and any stronger-use boundary needed to interpret those claims | what availability is for; actual reliance remains another relation |
| publication expression | one independently identified `U.Entity`, X, under its expression domain's formation and equality rules | the particular sign construction from which the required claims can be recovered |
| presentation carrier | one independently identified `U.Entity`, C, under its physical or digital domain's identity rule | the entity whose actual state or realization provides that exact expression |

The `U.Entity` ranges leave X, F and C with their independently established domain identities. The positive predicates below determine expression, conformance and bearing. E.8 supplies FPF pattern-form rules, E.17 selects multi-view publication forms, and a domain publication pattern can supply another form.

**Obtain X with an identity that answers the actual comparison.** X is an independently identified sign construction: specified elements organized under the formation and equality rules of an expression domain. The domain tells a receiver which differences change that construction. A construction can be compared before anyone establishes which episteme it expresses. Two useful domains are:

- An ordered Unicode text has the declared codepoint sequence as its value. Changing a codepoint or its position changes X. Encoding the same sequence in UTF-8 or UTF-16 can preserve X while changing the stored bytes. Any normalization of line endings or Unicode variants must be part of the selected domain's equality or its decoding rule before comparison; it is not inferred from visual similarity.
- A keyed typed table has its column definitions, key-to-row mapping and typed cell values as its value. Keys are unique; missing, unknown and numeric zero have separately declared representations. Under an unordered-row domain, displaying rows in another order preserves X. A domain that includes row order instead gives a different X after that permutation. If the receiving use or selected F relies on order, the expression domain must retain it.

These are independently specified domains, not a closed taxonomy. Another notation supplies its own elements, organization, equality and formation conditions. The chosen domain remains fixed in a comparison. A move between domains requires an explicit correspondence and cannot obtain identity merely by choosing a coarser equality after the change. Concrete copies of a construction do not multiply X when the domain gives them the same value; their carrier tokens can differ.

**Obtain F as reusable rules.** F is an independently identified collection of rules for constructing or arranging eligible expressions. Its identity is the interpreted rules, their application domains and imported dependencies. A layout-only F can leave subject claims unconstrained; another F can require fields, units, coverage or particular interpretations. The episteme that describes F retains its own C.2.1 identity. An expression X conforms to F when it belongs to the applicable expression domain and satisfies each applicable rule and dependency. A rule referring to R uses C.2.1:4.1.1's distinction; a label such as format does not exclude a semantic requirement.

**Obtain C through its own domain.** C is a physical or digital entity from which X can actually be recovered under the stated conditions. For a continuing file object, a write can preserve C while changing its state and X. For an immutable digital snapshot identified by its complete byte value, different bytes identify another C. For a physical sheet or copy token, another copy has another identity. A route such as a URL is the designation or access path used to reach the chosen carrier; it does not determine that carrier's continuity. State which domain the current comparison uses before judging it.

A snapshot value alone establishes no actual availability. Its bearing and publication claims require an actual retrievable realization with a decoding path to X. When several copies realize the same snapshot value, a value-based availability claim can remain true while one copy disappears. A claim about which physical or managed file copy was supplied instead selects that copy as C. These choices preserve the question each consumer actually asks.

The reusable declaration is:

```text
EpistemePublicationRelationSignature:
  RelationKind: EpistemePublicationRelation
  SlotSpecs:
    SelectedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    AudienceDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    PresentationCarrierSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

These SlotKinds name participant meanings only inside this `RelationSignature`. They do not create five new U-kinds, and a card field with a similar label does not become one of these SlotSpecs.

The audience-declaration episteme identifies the audience criterion; it is not the audience and does not prove access by any particular system. A concrete system's access, reading, reliance, or later work is another direct relation or work occurrence. This lets one publication be available to every entity satisfying a stable criterion without inventing `U.Audience` or treating a changing set of readers as changing participants of the same publication occurrence.

`EpistemePublicationRelation` obtains while all of the following are true:

1. `PublicationExpressionRelation(E,X,U)` relates the selected episteme, exact expression and bounded-use declaration;
2. `PublicationExpressionBearingRelation(C,X)` relates the exact carrier and that same expression;
3. entities admitted by the audience declaration can obtain X from C and recover the required content of E under the conditions stated by the bounded-use declaration;
4. E, A, U, X and C remain the identified participants of this occurrence.

One occurrence is reidentified by those five fixed participants and their maximal continuous interval of availability. Changing any participant yields another publication occurrence. Demonstrated loss of availability followed by restoration yields a later occurrence. Missing or stale evidence leaves current obtaining unresolved; it does not prove a gap.

Rendering, printing, uploading, indexing, or granting access are activities separate from the publication occurrence. When a precise performed-Work claim is independently current, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work; add F.6 only when that claim or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact. Follow A.6.1 for an operation binding, C.11 for a `ChoiceResult`, or the exact access, reliance, or use relation without reproducing its test here. The activity and any result remain separate from the publication-relation participants.

#### E.24.PUB:4.2 - Recover expression and bearing only when needed

1. `PublicationExpressionRelation(E,X,U)` obtains when interpreting X through its specified decoding conventions and E's effective R yields the claims of that selected E needed for U, with their operative participants, qualifications, modal force and asserted dependencies, and X supports the operations named by U. The recovered content must be traceable to E. If the bounded use requires only a selection, identify that selection and retain the conditions needed to use it; A.6.3's direct construction or loss rule governs any stronger claim of viewing or coarsening. A newly introduced claim belongs to the resulting episteme under C.2.1. It cannot be counted as content expressed from unchanged E.
2. `PublicationExpressionBearingRelation(C,X)` obtains while an actual state or realization of C provides a recovery procedure that yields that exact X under the specified decoding conditions. For a digital value, the procedure reaches an actual accessible realization. The predicate retains the distinction between a continuing carrier and its changing state.
3. `PublicationFormConformanceRelation(X,F)` obtains when the independently identified X satisfies the applicable rules, domains and dependencies of F. It establishes neither which E is expressed nor audience access.

Each of these occurrences is identified by its ordered participant values and maximal continuous interval of predicate truth. Missing evidence leaves obtaining unresolved; it does not itself establish an interruption.

Their reusable declarations are:

```text
PublicationExpressionRelationSignature:
  RelationKind: PublicationExpressionRelation
  SlotSpecs:
    ExpressedEpistemeEditionSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required
    PublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BoundedUseDeclarationSlot: ValueKind=U.Episteme, refMode=U.EpistemeRef, Required

PublicationExpressionBearingRelationSignature:
  RelationKind: PublicationExpressionBearingRelation
  SlotSpecs:
    PresentationCarrierSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BornePublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required

PublicationFormConformanceRelationSignature:
  RelationKind: PublicationFormConformanceRelation
  SlotSpecs:
    PublicationExpressionSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    PublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

**Form-mediated uses.** `PublicationFormExpressionRelation(E,F,U)` obtains while at least one independently identified X conforms to F and satisfies `PublicationExpressionRelation(E,X,U)`. It states that the selected form has an actual adequate expression for this E and U. The existence of a template alone is insufficient.

`PublicationFormBearingRelation(C,F)` obtains while C bears at least one independently identified X that conforms to F. It establishes the recoverability of a conforming construction; the expressed episteme and audience access require their own predicates.

Each of these form-mediated occurrences retains its fixed participants and maximal continuous interval of predicate truth. X is a witness for the quantified claim. Replacing X1 by X2 can preserve either occurrence when that predicate remains continuously true. Changing a filename or storage address does not by itself settle carrier identity; apply the carrier's direct identity and currentness pattern.


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
    PresentationCarrierSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
    BornePublicationFormSlot: ValueKind=U.Entity, refMode=U.EntityRef, Required
```

For form-mediated availability through C, the same X must witness expression, bearing and F-conformance. An adequate X1 elsewhere and a different X2 on C do not establish that E is available through C. Recover the shared witness whenever the availability claim depends on both form-mediated relations.

##### E.24.PUB:4.2.1 - Keep the granularity of the availability claim

A consumer can claim continuous availability of E to A for U over an interval when, at every time in that interval, at least one appropriate X and C provides that availability. If the consumer fixes F, C or a set of permitted carriers, retain those constraints in that claim. A change of exact publication does not prove an interruption of this broader availability. A gap is established when the required availability fails across the permitted alternatives. Failure of one copy or route alone does not establish that broader gap. This broader statement needs no new public publication kind or generic occurrence unless a receiving use independently needs its identity.

#### E.24.PUB:4.3 - Use progressive explicitness

Use the smallest statement that supports the current work:

1. **Ordinary use:** name the selected episteme, audience, bounded use, expression and carrier in one sentence; add selected form conformance when needed.
2. **Changed-object use:** say which one of those objects changed and which relation must be re-evaluated.
3. **Contested availability:** state the `EpistemePublicationRelation` participants, obtaining evidence, and occurrence identity.
4. **Contested expression:** open `PublicationExpressionRelation` and the applicable representation, preservation or loss pattern; inspect form conformance when the claim relies on it.
5. **Contested carrier availability:** open `PublicationExpressionBearingRelation` plus the direct carrier-currentness or access pattern; preserve the fixed or quantified alternatives of the actual availability claim.

Do not materialize all five levels as a standing publication card. Stop as soon as the receiving use can distinguish the operative object and relation.

#### E.24.PUB:4.4 - Classify the encountered form by current use

Ask one question at a time:

| Current question | Governed object or relation |
| --- | --- |
| Do the selected claims form an identifiable whole about an EntityOfConcern under an effective reference scheme? | a `U.Episteme` under `C.2.1`; the filled card or diagram supplies its expression |
| Does `EpistemeViewpointConformanceRelation(E,P)` obtain for that episteme E and at least one exact viewpoint episteme P? | the same E has dependent-kind membership as `U.View` under `E.17.0`; any A.6.3 construction remains a separate optional relation |
| Does the particular expression follow selected reusable formation or arrangement rules? | `PublicationFormConformanceRelation(X,F)`; expression of E for U is checked separately |
| Do selected elements correspond to independently recovered objects and support modeling or reasoning operations? | a representation and its correspondence under A.6.3.RT and A.6.3.RT.OE; C.29 supplies the additional grounds for a mathematical lens |
| Does an actual state or realization of the selected carrier yield exact X? | `PublicationExpressionBearingRelation(C,X)` |
| Is the selected episteme available to the declared audience for the declared use through X and C? | one `EpistemePublicationRelation(E,A,U,X,C)` occurrence |

The answers can be jointly positive because they concern different objects or relations. They do not follow from the words `card`, `record`, `table`, `schema`, `diagram`, `view`, `file`, or `publication` alone.

#### E.24.PUB:4.5 - Keep direct verbs with their relations

- an episteme carries claims and designations;
- a `U.View` is the same episteme individual for which E.17.0 conformance to at least one exact viewpoint episteme obtains;
- a particular expression conveys the selected episteme's required claims for a bounded use;
- a reusable publication form constrains eligible expressions;
- a representation stands in an identified correspondence to its subject; C.29 governs the mathematical-lens branch;
- a carrier bears a particular expression through its actual state or realization;
- a publication occurrence makes one selected episteme edition available;
- a system may perform publication activity and may later access or rely on the published episteme, but those are separate claims under their direct patterns; publication availability establishes none of them;

A designator designates and a governed reference resolves to a referent. Neither operation publishes, bears, represents, or makes the subject-side predicate obtain.

#### E.24.PUB:4.6 - Keep subject patterns subject-first

In a pattern about an ontic, structure, architecture, characteristic space, method, or another subject, explain the subject's identity, relations, practical problem, and solution before publication details. Add E.24.PUB only when the receiving use depends on distinguishing the description, selected edition, form, carrier, audience, or bounded use.

When the EntityOfConcern is itself a description episteme, the same rule applies one level up. The description stays the subject; publication of that description is a neighboring relation.

