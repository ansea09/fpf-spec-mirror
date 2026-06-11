---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__008_conformance-checklist.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:7 — Conformance Checklist"
line_start: 10779
line_end: 10808
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "C.26"
  - "C.26.1"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "coarsened rendering"
  - "controlled semantic coarsening"
  - "dashboard tile"
  - "lookup handle"
  - "narrower admissible use"
  - "non-admissible downstream use"
  - "redaction"
  - "reopen trigger"
  - "source-bearing episteme or source publication"
  - "state-representation shortcut"
---

### A.6.3.CSC:7 - Conformance Checklist

A conformance check is retained only if it changes the next admissible use of the coarsened rendering, blocks a concrete overclaim, or preserves the source-bearing reopen path needed for the declared admissible use.

#### A.6.3.CSC:7.1 - CSC-Core

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-1 (Source visible).** | A conforming controlled-coarsening card SHALL name the source-bearing side or inherit it from the immediate source context. | Prevents the coarsened rendering from resetting provenance. |
| **CC-CSC-2 (Rendering explicit).** | A conforming card SHALL identify the coarsened rendering and keep it distinct from the source-bearing side. | Prevents citation laundering and source-to-rendering collapse. |
| **CC-CSC-3 (Admissible use).** | A conforming card SHALL state the narrower admissible use. | Keeps ordinary convenience from becoming broad authority. |
| **CC-CSC-4 (Non-admissible downstream use).** | A conforming card SHALL state the non-admissible downstream use. | Makes over-read and misuse visible early. |
| **CC-CSC-5 (Reopen or handoff).** | A conforming card SHALL state the source-bearing reopen trigger or governing-pattern handoff condition. | Gives readers an admissible next move under dispute, citation, reliance, policy, bridge, work, gate, privacy, assurance, release, or adjudication use. |
| **CC-CSC-6 (Ordinary economy).** | Authors SHOULD keep ordinary cases to the mini-card unless dispute, citation, external reliance, policy, bridge, work, gate, privacy, or assurance use is live. | Preserves usability and avoids daily-process inflation. |

#### A.6.3.CSC:7.2 - CSC-Conditional

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-7 (Use-specific assurance).** | Claim-bearing cases SHALL add only the admissibility fields needed for the use under repair, dispute, or reliance case. | Keeps the assurance section tied to real risk. |
| **CC-CSC-8 (Branch and use split).** | Load-bearing or disputed cases SHALL keep `coarseningBranch` and `admissibleUseValue` separate. | Prevents the coarsening branch from implying source-loss mode or authority. |
| **CC-CSC-9 (Source-loss mode and recoverability).** | Cases affecting claim admissibility, accountability, admissible-use value, or later citation SHALL state source-loss mode and recoverability class. | Prevents recoverability from being mistaken for admissible use. |
| **CC-CSC-10 (Coarsening-chain continuity).** | A coarsening chain SHALL satisfy `CSC-WF-3` or reopen the source-bearing side. | Prevents provenance reset by repeated summarization. |
| **CC-CSC-11 (Governing-pattern exits).** | Bridge, stance, work, gate, adjudication, and changed-entity claims SHALL be handled by their governing patterns or publications with named authority-reference relations. | Prevents CSC from stealing neighboring pattern duties. |
| **CC-CSC-12 (No authority by repetition).** | A conforming card SHALL satisfy `CSC-WF-2`. | Blocks authority laundering through fluency or citation. |
| **CC-CSC-13 (Source, rendering, and publication separation).** | Claim-bearing cases SHALL separate source-bearing side, coarsened rendering, `PublicationUnit`, publication face, E.17 publication-face kind value `publication face/form`, E.17 publication-face kind value `interop publication form`, and carrier when those could be confused. | Keeps `PublicationUnit`, publication face, and carrier roles distinct. |
| **CC-CSC-14 (Privacy and redaction).** | Privacy or redaction cases SHALL name the sharing boundary, withheld distinctions, risk rationale, non-admissible accountability or gate uses, and source-bearing review path. | Prevents redaction from becoming closure. |
| **CC-CSC-15 (Interop simplification).** | Exceptional interop-facing simplifications SHALL name the operative relation kind and hand bridge or equivalence pressure to `F.9` or `F.9.1`. | Prevents simplified relation language from carrying bridge or substitution use. |
| **CC-CSC-16 (Source relation class).** | Claim-bearing source-relation cases SHALL use the `E.17:5.1b` vocabulary where needed: source pointer, source availability, source retrieval, source use, source faithfulness, claim admissibility, contradiction, plausibility-only, omission, declared source-loss mode, added commitment, added linkage, independent verification, admissible use, non-admissible downstream use, and reopen trigger. | Keeps helpful renderings from passing as evidence. |

