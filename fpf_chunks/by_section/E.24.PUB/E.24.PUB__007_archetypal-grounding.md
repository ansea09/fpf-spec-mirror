---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__007_archetypal-grounding.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:5 — Archetypal Grounding"
line_start: 91761
line_end: 91790
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

### E.24.PUB:5 - Archetypal Grounding

#### E.24.PUB:5.1 - Maintenance inspection card

A completed pump-inspection card states measured clearances and identified defects about Pump #37 under the maintenance reference scheme. The completed card is a claim-bearing `U.Episteme`. Its reusable arrangement is the inspection-card publication form. The PDF file is a `U.PresentationCarrier`. One publication occurrence makes edition 4 of the card episteme available to the maintenance-planning team for planning the next repair.

Changing the PDF filename changes neither the card episteme nor necessarily the carrier identity. Correcting a measured clearance changes the episteme edition. Replacing the card layout changes the form. Making the same edition available to a supplier for quotation creates another publication occurrence because the audience or bounded use changed.

#### E.24.PUB:5.2 - Architecture diagram

An architecture diagram can carry claims about selected structures of one holon and therefore be an architecture-description episteme. When that exact episteme conforms to one exact architectural viewpoint episteme under E.17.0, the same individual is a `U.View`; direct authoring and A.6.3 construction are independent construction routes. Its graphical notation can be the publication form, selected nodes and edges can participate in a C.29 representation, and a screen or sheet can be the presentation carrier.

The diagram does not become the architecture by being published. `C.30` governs the `ArchitectureOf@Context` claim and `A.22` governs selected `U.Structure` values. E.24.PUB lets the architect locate a publication defect without replacing the architectural question with a discussion of diagrams.

#### E.24.PUB:5.3 - Clinical procedure edition

A hospital procedure description is an episteme about how a procedure is performed. Treat it as a `U.MethodDescription` only when its EntityOfConcern is one independently admitted `U.Method` and its claims describe how that Method is carried out. A wall poster expresses a selected edition for quick pre-procedure orientation; the laminated sheet is the carrier. A separate controlled publication makes the same edition available to clinicians for authoritative use during the procedure. The two publication occurrences differ in bounded use even if the words are identical. Neither publication proves access, reliance, Method enactment, or clinical Work. If later clinical Work is independently claimed, route that claim to its direct Work and attribution patterns rather than restating their basis here. Keep the publication occurrence and every separately current access, reliance, assignment, Method, Work, or result claim distinct.

#### E.24.PUB:5.4 - FPF pattern host

An E.24 pattern host can be a publication form expressing an ontic-description episteme about `U.Ontic`. The repository file is a presentation carrier. A selected edition becomes a published episteme only while an exact publication occurrence makes it available to the declared FPF audience and use. The host layout does not create `U.Ontic`, and changing the carrier does not by itself change the ontic-description episteme.

#### E.24.PUB:5.5 - Training availability and later choice work

One instruction edition is available to a training group for studying a method. That `EpistemePublicationRelation` occurrence establishes availability to the declared audience for that bounded use; it establishes neither that anyone read the instruction nor that adjustment, inspection, acceptance, or release work occurred. The same availability alone does not support an acceptance commission's choice about releasing one named lot.

If a commission later makes a release choice and that stronger claim is current, recover each exact actual choice-work performer through A.13 and let A.15.1 independently admit any dated choice Work. Add F.6 only when the choice account or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the choice Work intact. Identify the resulting `ChoiceResult` separately under C.11. Keep both Work and result separate from the publication occurrence; the publication statement need not carry their identity, staffing, or omission rules.

When the later claim says that the published instruction was actually used, state that exact use under its direct relation, or under A.6.1 only when a declared operation application is current. If no such route is established, stop at publication availability and let the receiving pattern identify its own blocker. The `ChoiceResult` is neither the choice Work, the bounded-use declaration, nor a participant of the publication occurrence.

