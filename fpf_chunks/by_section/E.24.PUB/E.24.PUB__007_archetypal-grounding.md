---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__007_archetypal-grounding.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:5 — Archetypal Grounding"
line_start: 88755
line_end: 88782
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

### E.24.PUB:5 - Archetypal Grounding

#### E.24.PUB:5.1 - Maintenance inspection card

A completed pump-inspection card states measured clearances and identified defects about Pump #37 under the maintenance reference scheme. The completed card is a claim-bearing `U.Episteme`. Its reusable arrangement is the inspection-card publication form. The PDF file is a `U.PresentationCarrier`. One publication occurrence makes edition 4 of the card episteme available to the maintenance-planning team for planning the next repair.

Changing the PDF filename changes neither the card episteme nor necessarily the carrier identity. Correcting a measured clearance changes the episteme edition. Replacing the card layout changes the form. Making the same edition available to a supplier for quotation creates another publication occurrence because the audience or bounded use changed.

#### E.24.PUB:5.2 - Architecture diagram

An architecture diagram can carry claims about selected structures of one holon and therefore be an architecture-description episteme. When that exact episteme conforms to one exact architectural viewpoint episteme under E.17.0, the same individual is a `U.View`; direct authoring and A.6.3 construction are independent construction routes. Its graphical notation can be the publication form, selected nodes and edges can participate in a C.29 representation, and a screen or sheet can be the presentation carrier.

The diagram does not become the architecture by being published. `C.30` governs the `ArchitectureOf@Context` claim and `A.22` governs selected `U.Structure` values. E.24.PUB lets the architect locate a publication defect without replacing the architectural question with a discussion of diagrams.

#### E.24.PUB:5.3 - Clinical procedure edition

A hospital procedure description is an episteme about a method. A wall poster expresses a selected edition for quick pre-procedure orientation; the laminated sheet is the carrier. A separate controlled publication makes the same edition available to clinicians for authoritative procedure enactment. The two publication occurrences differ in bounded use even if the words are identical. Neither publication proves that a clinician read the procedure or performed work according to it; those are access, reliance, role-assignment, method, and work claims under their direct patterns.

#### E.24.PUB:5.4 - FPF pattern host

An E.24 pattern host can be a publication form expressing an ontic-description episteme about `U.Ontic`. The repository file is a presentation carrier. A selected edition becomes a published episteme only while an exact publication occurrence makes it available to the declared FPF audience and use. The host layout does not create `U.Ontic`, and changing the carrier does not by itself change the ontic-description episteme.

#### E.24.PUB:5.5 - Training availability and later choice work

One instruction edition is available to a training group for studying a method. That `EpistemePublicationRelation` occurrence establishes availability to the declared audience for that bounded use; it establishes neither that anyone read the instruction nor that adjustment, inspection, acceptance, or release work occurred. The same availability alone does not support an acceptance commission's choice about releasing one named lot.

If the commission later performs exact choice `U.Work` under A.15.1 and applies C.11, name that Work and the resulting C.11 `ChoiceResult` separately. When an instruction claim actually participates in that Work, name the exact claim-bearing episteme and its direct route. For a premise, reference, other participant, or work-to-referent use, name the exact declared predicate, participant order, and actual values. For a declared operation argument, name the identified A.6.1 application and its exact declaration-local binding. If neither route exists, stop at publication availability or return the applicable A.15.1 `missing-governor` result instead of asserting actual use. The `ChoiceResult` is neither the choice Work, the bounded-use declaration, nor a participant of the publication occurrence.

