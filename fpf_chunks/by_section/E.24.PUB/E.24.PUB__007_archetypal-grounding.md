---
chunk_kind: "child"
pattern_id: "E.24.PUB"
pattern_title: "Ontic Description and Publication Discipline"
section_id: "E.24.PUB:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.PUB/E.24.PUB__007_archetypal-grounding.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "E.24.PUB — Ontic Description and Publication Discipline"
  - "E.24.PUB:5 — Archetypal Grounding"
line_start: 89749
line_end: 89778
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

A hospital procedure description is an episteme about how a procedure is performed. Treat it as a `U.MethodDescription` only when its EntityOfConcern is one independently admitted `U.Method` and its claims describe how that Method is carried out. A wall poster expresses a selected edition for quick pre-procedure orientation; the laminated sheet is the carrier. A separate controlled publication makes the same edition available to clinicians for authoritative use during the procedure. The two publication occurrences differ in bounded use even if the words are identical. Neither publication proves access, reliance, Method enactment, or clinical Work. When a clinician System performs admitted Work, the account names the Work's Method, time, containing System, a covering clinical assignment held by that clinician, and the F.6 relation linking the Work to that assignment; a short sentence may omit only an assignment identifier that its receiving claim does not use. Keep access, reliance, assignment, Method, Work, publication occurrence, and result separate. Words such as *role assignment*, *method*, and *work* in source prose are cues for this recovery, not admissions by themselves.

#### E.24.PUB:5.4 - FPF pattern host

An E.24 pattern host can be a publication form expressing an ontic-description episteme about `U.Ontic`. The repository file is a presentation carrier. A selected edition becomes a published episteme only while an exact publication occurrence makes it available to the declared FPF audience and use. The host layout does not create `U.Ontic`, and changing the carrier does not by itself change the ontic-description episteme.

#### E.24.PUB:5.5 - Training availability and later choice work

One instruction edition is available to a training group for studying a method. That `EpistemePublicationRelation` occurrence establishes availability to the declared audience for that bounded use; it establishes neither that anyone read the instruction nor that adjustment, inspection, acceptance, or release work occurred. The same availability alone does not support an acceptance commission's choice about releasing one named lot.

If an admitted commission System later performs dated choice `U.Work` and applies C.11, use A.15.1 to name the Work's Method, time, and containing System. For every performer, name the assignment occurrence that covers the Work and its declared species, confirm that the performer is the holder, and establish the F.6 relation linking the Work to that assignment. A short account may omit an assignment identifier that the receiving claim does not use. Name the Work and the resulting C.11 `ChoiceResult` separately.

When an instruction claim participates in that Work, name the claim-bearing episteme and how the Work uses its claim. For a premise, reference, other participant, or work-to-referent use, name the declared predicate, participant order, and values. For a declared operation argument, name the A.6.1 application and its declaration-local binding. If neither route exists, stop at publication availability or return the applicable A.15.1 `missing-governor` result instead of asserting use. The `ChoiceResult` is neither the choice Work, the bounded-use declaration, nor a participant of the publication occurrence.

