---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:7"
section_title: "Conformance and counterexample replay"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__008_conformance-and-counterexample-replay.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:7 — Conformance and counterexample replay"
line_start: 13872
line_end: 13914
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.NAR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.33"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.CSC:7 - Conformance and counterexample replay

A check is retained only if it changes the next admissible use, blocks a concrete overclaim, or preserves the exact source-return path.

#### A.6.3.CSC:7.1 - CSC-Core

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-1 (Exact endpoints).** | Exact `X` and `Y` each have recoverable claim content, EntityOfConcern, and effective `U.ReferenceScheme`. | Blocks a source set, model, graph, evidence set, publication, form, carrier, or readable tile from replacing an episteme. |
| **CC-CSC-2 (Exact construction).** | Exact `c : X -> Y` states same EntityOfConcern, claim construction, endpoint scheme relation, preservation, controlled loss, prohibited strengthening, applicability, and return. | Makes coarsening a testable A.6.3 construction rather than a label. |
| **CC-CSC-3 (Admissible use).** | `Y` has one stated narrower admissible use. | Keeps convenience from becoming broad authority. |
| **CC-CSC-4 (Non-admissible use).** | Stronger downstream use is explicit and cannot be inferred from `Y` or its publication. | Blocks authority laundering. |
| **CC-CSC-5 (Return).** | Return resolves to exact `X`, exact governed source relations, or the named direct governor. | Prevents provenance reset. |
| **CC-CSC-6 (Neighbor separation).** | Actual Work, additional source epistemes, correspondence, C.29 representation, viewpoint/`U.View`, grounding, publication occurrence, form, carrier, audience, and bounded use retain direct owners. | Prevents a filled coarsening card from becoming an omnibus ontology. |
| **CC-CSC-7 (Ordinary economy).** | Ordinary cases stop at the mini-card after endpoint/construction identity is recoverable. | Preserves usability. |

#### A.6.3.CSC:7.2 - Claim-bearing conditions

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-CSC-8 (Branch/use split).** | `coarseningBranch`, `sourceLossMode`, and `admissibleUseValue` remain separate. | A branch or loss label grants no authority. |
| **CC-CSC-9 (Loss/recoverability).** | Claim-bearing cases state exact preserved, dropped, and return-only claims plus recoverability class. | Distinguishes recoverability from admissibility. |
| **CC-CSC-10 (Chain continuity).** | Every coarsening chain keeps exact original source episteme, each intermediate episteme, each construction, accumulated loss, and return; otherwise reopen exact `X`. | Prevents summarization from resetting source identity. |
| **CC-CSC-11 (Privacy).** | Redaction cases name sharing boundary, withheld claims, risk rationale, blocked accountability/gate uses, and exact source review path. | Prevents redaction-as-closure. |
| **CC-CSC-12 (Interop).** | Interop simplification names exact relation claims and routes Bridge/equivalence pressure to F.9/F.9.1. | Prevents simplified wording from asserting correspondence. |
| **CC-CSC-13 (No authority by repetition).** | Fluency, citation, repetition, publication visibility, or a more convenient carrier cannot widen use. | Keeps `Y` within its declared use. |

#### A.6.3.CSC:7.3 - Counterexample replay

| Case | Required result |
| --- | --- |
| Preserve vs retarget | Exact same EntityOfConcern permits CSC; aggregation into a new proxy subject exits to A.6.4. |
| Same vs different scheme | Coarsening can occur within one scheme; material representation-semantic change additionally opens RT, but scheme difference alone establishes neither `c` nor controlled loss. |
| Candidate vs `U.View` | Exact coarsened `Y` can be valid under CSC and still fail E.17.0 conformance; a tile or layout is not a View. |
| Source publication/form/carrier | A publication occurrence may make exact `X` available; form and carrier express it. None becomes `X`, and changing one does not reidentify unchanged `X`, `Y`, or `c`. |
| Controlled loss | Omitted qualifiers, uncertainty, alternatives, evidence paths, or scope are named; the narrower use and return condition actually block the stronger use. |
| Source set/model/graph/evidence set | Such an object is an endpoint only when the selected claim-bearing whole passes C.2.1; otherwise exact `X` claims about or cites it. |
| Work or description | Actual coarsening Work and a coarsening-description/card episteme remain separate from `c`; editing either does not change unchanged endpoints. |
| Grounded source, ungrounded coarsening | Grounding, evidence, or authority attached to `X` does not transfer to `Y`; `Y` needs its own direct grounding/evidence/authority path for any use that requires one. |
| Selected structure overread | A selected architecture or other A.22 structure may be designated by `X`; it is not `X`, `Y`, the coarsening constructor, viewpoint, `U.View`, publication, form, or carrier. |

After a bounded correction replay its local counterexample; after the batch run this complete table once. Do not repeat the whole host audit after every correction.

