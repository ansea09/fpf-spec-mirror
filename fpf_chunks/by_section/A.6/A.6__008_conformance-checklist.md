---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__008_conformance-checklist.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:7 — Conformance Checklist"
line_start: 7303
line_end: 7315
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.MultiViewDescribing"
  - "U.Signature"
  - "U.View"
  - "U.Viewpoint"
  - "U.Work"
keywords:
  - "A.6.B L/A/D/E claims"
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "authority-wording split"
  - "boundary"
  - "boundary claim-classification fields"
  - "in invariants"
  - "probe/order/frame/export/state-reading claims"
  - "promise/commitment/API/policy wording"
  - "reference predicate IDs from CC when needed"
  - "register-backed status boundary"
  - "signature stack"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:7 - Conformance Checklist

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Purpose                                                             |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **CC‑A.6.1 (Stack declaration).**        | A conforming boundary description **SHALL** identify its stack layers (Signature, Mechanism, Realization/Work evidence, Publication faces) and state which boundary publication forms or sections belong to which layer.                                                                                                    | Prevents “one doc contains everything” ambiguity.                   |
| **CC‑A.6.2 (Square discipline).**        | A conforming boundary description **SHALL** conform to **A.6.B** (Boundary Norm Square), including atomicity, quadrant classification, and explicit cross‑quadrant references by claim ID.                                                                                                           | Makes the stack operational; prevents “contract soup” drift. |
| **CC‑A.6.5 (A.7 separation).**           | A conforming boundary description **SHALL** respect EntityOfConcern and Description-episteme / publication-carrier separation; statements about logs/metrics **SHALL** be written as carrier‑anchored evidence claims/policies, not as properties of the text itself. | Prevents category errors and improves auditability.                 |
| **CC‑A.6.6 (Viewpoint accountability).** | Every published MVPK face (`U.View`) **SHALL** specify `viewRef` and `viewpointRef`. Faces **SHALL** be projections of the boundary’s canonical L/A/D/E-classified claim set (A.6.B); normative content on faces **MUST** be expressed as citations to L/A/D/E claim IDs (not re‑stated prose), and faces **MUST NOT** introduce new semantic commitments beyond the underlying signature/mechanism (per **E.17** “no new semantics”). | Preserves viewpoint discipline and prevents view‑forking.    |
| **CC‑A.6.6a (MVPK face‑kind discipline).**  | A publication that claims MVPK alignment **MUST** conform to **E.17 / publication-face/form discipline** face‑kind closure (i.e., use only `{PlainView, TechCard, InteropCard, AssuranceLane}` and **MUST NOT** mint additional face kinds). Local “cards” may exist only as headings/sections inside those face kinds. | Aligns with MVPK/publication-face/form discipline; prevents new‑face drift.            |
| **CC‑A.6.7 (Contract unpacking).**       | When using “contract/guarantee/promise” language, a conforming text **SHOULD** apply the reusable discipline in **A.6.C** to disambiguate whether it refers to a promise content as promise content (`U.PromiseContent`, not execution), an utterance package, a published description, a speech act, a deontic commitment (`U.Commitment`), work effects, or evidence, and then classify each atomic statement via **A.6.B** (`L-*`, `A-*`, `D-*`, or `E-*`) with explicit claim‑ID references (no paraphrase drift). (**F.18** is a lexical anchor only.) | Stops agency attribution errors; clarifies responsibility.          |
| **CC‑A.6.8 (Causal/deontic split).**     | A boundary description that mixes causal support with duty, promise, commitment, release, or admissibility language SHALL split the sentence into atomic claims: causal-use support to `C.28`, deontic and boundary-gate claims to `A.6.B`, and contract/promise/utterance unpacking to `A.6.C`. A `CausalUseSupportVerdict` does not by itself create a duty, commitment, promise, release gate, or boundary admissibility predicate. | Prevents causal evidence from being recast as boundary authority or deontic obligation. |
| **CC-A.6.9 (Authority-wording split).** | A conforming boundary description SHALL split boundary, policy, API, schema, connector, or compliance prose using "approved", "allowed", "authorized", "guaranteed", "certified", "recommended", or equivalent wording into atomic `L-*`, `A-*`, `D-*`, and `E-*` claims before work use or reliance use. Any evidence, assurance, role effect, status effect, gate use, release use, commitment, speech-act, or work-occurrence use beyond the L/A/D/E-classified wording SHALL cite the exact `governingPatternRef` or `authoritySourceRef` rather than the wording itself. | Prevents boundary wording from becoming authority, evidence, assurance, gate passage, or work by slogan. |

