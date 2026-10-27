---
chunk_kind: "child"
pattern_id: "A.6.RSIG"
pattern_title: "Recognition Signatures: Find the Defining Episteme for a Description"
section_id: "A.6.RSIG:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIG/A.6.RSIG__012_sota-echoing.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.6.RSIG — Recognition Signatures: Find the Defining Episteme for a Description"
  - "A.6.RSIG:11 — SoTA-Echoing"
line_start: 14473
line_end: 14485
dependencies:
  - "A.6"
  - "A.6.P"
  - "E.10"
  - "F.18"
keywords:
---

### A.6.RSIG:11 - SoTA-Echoing

The following sources contribute to cue economy, recoverable definition and bounded expectations. Their contributions apply to the recognition question; the defining subject account still supplies its substantive semantics.

| Recognition question | Source contribution | Connection to this pattern | Use and limits |
| --- | --- | --- | --- |
| First-contact recognition is narrower than general information architecture or documentation UX. | Jorge Arango (2018), *Living in Information: Responsible Design for Digital Places*; ISO/IEC/IEEE 26514:2022, *Systems and software engineering - Design and development of information for users*. | These sources support purposeful information places and user information shaped around what the user needs. `A.6.RSIG` narrows that to one encountered description: what it is for, what applies, what excludes, what carrier exposed it, and which `definitionEpistemeRef` identifies the defining episteme. | Use the recognition and information-need contribution for one encountered description; broader UX and layout remain outside this task. In the boundary sentence slice, the first repair is not "what does the complete Contract Bundle mean?" but "what description is this, what does it apply to, and which definitionEpistemeRef applies?" |
| Information scent helps first-contact cue economy but is not the defining episteme. | Raluca Budiu (2020), "Information Scent: How Users Decide Where to Go Next", Nielsen Norman Group. | Information scent treats visible labels, context, and prior knowledge as imperfect estimates of source value. `A.6.RSIG` uses the cue-economy insight and adds definition-episteme and exclusion discipline, with false-neighbor rejection under §4.1's grounded-guard condition. | Visible cues guide inspection; the defining episteme remains the source to inspect. In the API slice, an endpoint label can attract attention and state deployment initiation without promising successful completion. |
| Description-recognition signatures help human and AI-assisted readers manage applicability and limitation expectations. | Amershi et al. (2019), "Guidelines for Human-AI Interaction", CHI 2019. | Human-AI guidance emphasizes making capabilities and limits clear enough for users to calibrate trust. `A.6.RSIG` adapts that pressure into `applies_to`, `excludes`, `definitionEpistemeRef`, and admissible entry stop for human and AI-assisted readers. | Clarify expectations for the encountered description. In the method-note slice, the reader learns what the note can and cannot settle before using it for a decision. |
| Description-recognition cues need controlled wording without becoming synonym or alias governance. | Helen Lippell, ed. (2022), *Taxonomies: Practical Approaches to Developing and Managing Vocabularies for Digital Information*. | Taxonomy practice supports governed terms, validation, and maintenance for search and browse. `A.6.RSIG` uses stable cue language while leaving wording repair to `E.10` cues within `F.19`, durable naming, aliases, and collision checks to `F.18`, actual Bridge claims to `F.9`, and under-specified relation claims to `A.6.P`. | Use stable terms that discriminate the intended description. The worked slices state definitionEpistemeRef, exclusions, and a false neighbor when §4.1's grounded-guard condition holds, instead of adding more query phrases. |
| Thin echoes and projection snippets need definition-episteme anchors before a reader or retrieval system treats them as the defining episteme. | Lewis et al. (2020), "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"; Liu, Zhang, and Liang (2023), "Evaluating Verifiability in Generative Search Engines"; Gao et al. (2023), "Enabling Large Language Models to Generate Text with Citations". | Retrieval and citation work makes source context, support, and verifiability load-bearing. Before relying on a retrieved fragment, public projection, or local example to identify a particular defining description, recover the defining `U.Episteme` and the projection relation when relevant. An unresolved fragment may still guide further inspection. | Recover the defining source and support for the cue. A retrieved applicability cue does not by itself settle selection semantics. |
| Description-recognition-signature adequacy is reviewable through small, case-linked checks. | Riehle, Harutyunyan, and Barcomb (2020), *Pattern Discovery and Validation Using Scientific Research Methods*, Technical Report CS-2020-01. | Pattern-validation practice supports explicit evidence and case adequacy. `A.6.RSIG` keeps that pressure lightweight: use the first-contact shape, false-neighbor rejection when §4.1's grounded-guard condition holds, and worked slices first; add `C.25` only for a composite quality-family claim, `C.16.Q` only for overloaded evaluative wording, and empirical evidence when the recognition claim requires it. | Choose evidence for the recognition conclusion being made; an ordinary wording repair need not establish measured reader performance. |

