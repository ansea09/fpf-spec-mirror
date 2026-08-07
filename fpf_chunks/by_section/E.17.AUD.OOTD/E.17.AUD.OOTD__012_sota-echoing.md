---
chunk_kind: "child"
pattern_id: "E.17.AUD.OOTD"
pattern_title: "PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject"
section_id: "E.17.AUD.OOTD:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.OOTD/E.17.AUD.OOTD__012_sota-echoing.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.17.AUD.OOTD — PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject"
  - "E.17.AUD.OOTD:11 — SoTA-Echoing"
line_start: 83235
line_end: 83245
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.2.2a"
  - "E.10"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "F.18"
keywords:
---

### E.17.AUD.OOTD:11 - SoTA-Echoing

**Source boundary.** These sources support topic focus, scope/non-scope, reader-need organization, and explicit document structure. None establishes a universal ontological rule that every publication unit has one subject, and none supplies a `C.2.1` entity participant. OOTD therefore keeps the one-primary-subject rule as a defeasible local heuristic and compares it with transition, sectioning, and splitting.

| Publication-unit obligation | Exact source and current contribution | Local repair of the source limit | Working implication here |
| --- | --- | --- | --- |
| Keep the current unit focused and expose its scope and non-scope. | [Google Technical Writing One — Documents](https://developers.google.com/tech-writing/one/documents) (updated 2025-07-07) tells authors to state scope and non-scope, then refocus or revise the scope when content veers; [Paragraphs](https://developers.google.com/tech-writing/one/paragraphs) (updated 2025-03-28) treats a paragraph as one independent unit of logic focused on one topic. | Paragraph focus does not imply one subject for every memo, packet, or document. OOTD scales the move by naming the bounded unit and comparing retention, explicit transition, sectioning, and splitting. | `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:4.3`, `E.17.AUD.OOTD:5.1`, `E.17.AUD.OOTD:5.6` |
| Organize documentation around the user's need and keep different action/cognition modes visible. | [Diátaxis](https://diataxis.fr/) organizes content, architecture, and form around four distinct user needs; its [compass](https://diataxis.fr/compass/) tests whether material informs action or cognition and supports acquisition or application, at sentence or whole-document scale. | The four modes diagnose a use shift but are not an FPF ontology or a formula for document count. OOTD names the actual carried move and downstream use, then keeps one structured unit only when a shared reader goal makes that cheaper and still clear. | `E.17.AUD.OOTD:4.1.a`, `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:5.2`, `E.17.AUD.OOTD:5.6` |
| Use a single-subject reusable topic when modular reuse is the main need. | [OASIS DITA 1.3 `<topic>`](https://docs.oasis-open.org/dita/dita/v1.3/os/part1-base/langRef/base/topic.html) defines the top-level topic as a single-subject topic or article. This is established structured-authoring lineage (2015), not the current source of OOTD's whole-document rule. | A DITA topic is one valid reusable unit architecture, not evidence that a deliberately sectioned review packet is defective. OOTD selects it when independent reuse or retrieval dominates and otherwise permits the coherent multi-section unit. | `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:5.6` |
| Keep object words and local designations precise without importing another concept system. | ISO 704:2022 and ISO 1087:2019 terminology practice distinguishes objects, concepts, definitions, designations, and terms. | Terminology discipline repairs overloaded heads but does not choose the publication architecture. OOTD first uses `E.17.AUD.LHR`, then makes subject, concern, carried move, and use explicit only when unit-level instability remains. | `E.17.AUD.OOTD:4.1.a`, `E.17.AUD.OOTD:4.2`, `E.17.AUD.OOTD:5.3` |

