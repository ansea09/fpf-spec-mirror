---
chunk_kind: "child"
pattern_id: "A.6.3.NAR"
pattern_title: "Structure-to-Narrative Rendering"
section_id: "A.6.3.NAR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.NAR/A.6.3.NAR__002_problem-frame.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "A.6.3.NAR — Structure-to-Narrative Rendering"
  - "A.6.3.NAR:1 — Problem frame"
line_start: 14822
line_end: 14856
dependencies:
  - "A.16.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.11"
  - "E.17"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.6"
  - "G.11"
  - "G.2"
keywords:
---

### A.6.3.NAR:1 - Problem frame

Use this pattern when selected source structure must become a sequential narrative rendering for a declared reader or listener use. Typical cases include a scientific mechanism turned into a paper section, an architecture trade-off turned into a team explanation, a conceptual graph turned into a lesson sequence, or an event graph turned into a generated story draft.

Primary `EntityOfConcern`: one `A.6.3` epistemic-viewing relation in which an admitted source basis, such as an episteme, publication, model, graph, architecture view, evidence set, situation record, event stream, proof field, or `G.2` source pack, is rendered as a narrative path while the same EntityOfConcern is preserved or a declared correspondence is used.

Plain starting vocabulary:

| Term | Plain meaning |
| --- | --- |
| `source basis` | The admitted source object or record used for rendering: episteme, publication, graph, model, architecture view, evidence set, situation record, event stream, proof field, or `G.2` source pack. |
| `selected source structures` | The relations, constraints, events, mechanisms, dependencies, conflicts, alternatives, or changes that must remain recoverable. |
| `source-structure selection rationale` | The reason these structures, rather than other possible structures, are needed for the declared reader or listener use. |
| `source temporal posture` | Whether the selected source structure or admitted source basis concerns retrospective or reverse-engineered actual structure or event record, live unfolding, prospective planned structure, prospective fictional structure or canon, or a mixed case. |
| `rendering mediation mode` | Whether the narrative rendering is direct source-structure narrativization or architecture-mediated narrativization through architecture understanding, description, view, viewpoint, decision, or telemetry. |
| `narrating or rendering worker` | The person, team, or tool-mediated role arranging the selected source structures into the narrative path. This role does not own authority over the source basis by default. |
| `reader or listener role` | The role and use whose interests constrain source-basis selection, ordering, viewpoint, recoverability, engagement, and source-basis return. This is narrower than a generic audience. |
| `reader-interest or use hypothesis` | The explicit guess about what the reader or listener needs to do with the narrative and what problem the selected structures help solve. |
| `narrative rendering` | The receiving sequential account that makes the source usable by a reader or listener. |
| `ordering rationale` | The reason this sequence is used: event order, causal order, discovery order, didactic order, tension order, traversal rule, or another declared rule. |
| `source-basis return condition` | The condition that names the exact source basis or receiving governing pattern to return to when the narrative no longer carries the needed selected structure for the declared use. |
| `epiplexity question` | The question "how much selected source structure did this rendering pull into an inspectable description for this observer and use?" NAR supplies the relation fields; structural-information and evaluation patterns answer the value claim. |

First useful move: write one compact `StructureToNarrativeRenderingCase@Context` for the case. Name the source basis, selected source structures, source-structure selection rationale, source temporal posture, rendering mediation mode, narrating or rendering worker, reader-interest or use hypothesis, receiving narrative rendering, intended reader or listener role and use, ordering rationale, preserved structure, foregrounded structure, coarsened or lost structure, recoverability, admissible use, non-admissible use, and source-basis or governing-pattern return condition.

What goes wrong if missed: a useful story becomes a substitute for the selected source structure. Readers remember a sequence, example, protagonist, conflict, or conclusion, but cannot reconstruct the relations inside the selected source structure that made the narrative worth using.

What this buys: the narrative can help human use without pretending to be neutral compression, proof, authority, ethics, evidence, architecture, or the selected source structure, source basis, or source episteme itself.

Ordinary use: for low-reliance teaching, orientation, or internal explanation, one compact case note near the narrative is enough. It must still state what the narrative preserves, what it leaves behind, and when to return to the source.

Reliance-facing use: use the full field spine when the narrative will guide architecture work, design decisions, policy communication, safety work, generated-output admission, external teaching, or cross-context reuse.

Not this pattern when the current change is only same-regime wording (`A.6.3.CR`), only representation-scheme transition (`A.6.3.RT`), only coarsened narrower-use rendering (`A.6.3.CSC`), explanation-use adequacy on an existing MVPK face (`E.17.EFP`), changed EntityOfConcern (`A.6.4`), carrier export or serialization, generated-output admission (`C.35`), evidence, assurance, ethics, publication, or work authorization. Use the direct governing pattern first and return here only when the structure-to-sequence narrative relation is live.

