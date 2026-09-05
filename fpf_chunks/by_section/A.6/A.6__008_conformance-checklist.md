---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__008_conformance-checklist.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:7 — Conformance Checklist"
line_start: 10592
line_end: 10604
dependencies:
  - "A.10"
  - "A.15"
  - "A.2.3"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.C"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.Mechanism"
  - "U.Signature"
  - "U.View"
keywords:
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "Work versus non-Work effect"
  - "acceptance"
  - "actual occurrence"
  - "and evidence"
  - "atomic L/A/D/E claims"
  - "delivery"
  - "in invariants"
  - "publication face"
  - "reference predicate IDs from CC when needed"
  - "separate result"
  - "signature and mechanism declarations"
  - "six-way authority-word branch"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:7 - Conformance Checklist

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Purpose                                                             |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **CC‑A.6.1 (Stack declaration).** | A conforming boundary description **SHALL** identify Signature, Mechanism, actual-occurrence, consequence/evidence, and Publication placements. A dated Work claim **SHALL** remain separate from any application result, production, change, delivery/transfer, evidence, or acceptance claim selected through `A.15.1:4.6`. | Prevents one “work and evidence” layer from recreating intrinsic outputs. |
| **CC‑A.6.2 (Square discipline).** | A conforming boundary description **SHALL** classify each atomic claim by its own modality and adjudication position. Every permission-looking claim **SHALL** cite one selected `A6-AW-*` row and that row's direct object; the selected subject pattern or kind of direct object alone never sets the quadrant. | Makes one actionable choice replace repeated permission catalogues. |
| **CC‑A.6.5 (Actual-occurrence, description, and carrier separation).** | An `E-*` claim **SHALL** identify the exact actual occurrence or evaluated finding under its subject pattern and **SHALL NOT** infer Work merely because change or a carrier exists. Any carrier used for reliance **SHALL** enter the exact evidence relation. | Preserves non-Work change and blocks carrier-as-effect errors. |
| **CC‑A.6.6 (Viewpoint accountability).** | Every published MVPK face use **SHALL** identify the selected episteme and bounded reader/use. When `U.View` membership or viewpoint identity is used, the face **SHALL** identify the exact `viewpointRef`. `U.View` membership still requires E.17.0 conformance. Face content **MUST** cite canonical L/A/D/E claim IDs and direct objects and **MUST NOT** introduce a new commitment or any new object or claim selected through `A6-AW-*`. | Preserves viewpoint discipline without letting a publication face create governance or permission claims. |
| **CC‑A.6.6a (MVPK face‑kind discipline).**  | A publication that claims MVPK alignment **MUST** use E.17’s declared `publication-face kind` values: **publication face/form** and **interop publication form**. `PlainView`, `TechCard`, `InteropCard`, and `AssuranceLane` are face designators, with profiles selected under E.17. A publication **MUST NOT** mint additional MVPK face kinds. Local “cards” may exist only as headings or sections inside the selected faces. | Aligns with MVPK and publication-face or publication-form discipline; prevents new‑face drift.            |
| **CC‑A.6.7 (Contract unpacking).** | When using “contract”, “guarantee”, “permission”, or “promise” language, a conforming text **SHOULD** use A.6.C for the object split and `A.6.B:8.4.1` for classification. Promise content, instituting speech-act Work, commitment or grant, dated performed Work, application/result binding, production, delivery/transfer, evidence, and acceptance **MUST** remain independently optional objects under their subject patterns. | Stops agency attribution and result/output rebundling. |
| **CC-A6-CAUSAL-DEONTIC-SPLIT (Causal/deontic split).** | When causal support and authority wording share a sentence, a conforming description **SHALL** use C.28 for the causal-use question and route each permission-looking claim to one `A6-AW-*` row. Neither result creates the other. | Prevents causal evidence from becoming hidden authority. |
| **CC-A.6.9 (Authority-wording split).** | Before authority-looking wording guides work or reliance, a conforming description **SHALL** select one `A6-AW-*` row per atomic permission claim and cite that row's source and direct object. | Prevents a visible word from becoming authority or evidence. |

