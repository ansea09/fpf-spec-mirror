---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:8"
section_title: "Archetypal Grounding (SoTA-aligned Local Tests)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__009_archetypal-grounding-sota-aligned-local-tests.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:8 — Archetypal Grounding (SoTA-aligned Local Tests)"
line_start: 115599
line_end: 115619
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "A.6.9"
  - "A.7"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.View"
keywords:
---

### E.17:8 - Archetypal Grounding (SoTA-aligned Local Tests)

Use these examples to test the MVPK invariants. A source’s reputation does not establish that a face passes a test.

**Ordinary two-reader publication.** An accepted interface account already states the service boundary, messages, and failure conditions. A project lead needs a short explanation and an integrator needs the typed details. Publish one `PlainView` and one `TechCard`, both pointing to that same account and stating what they omit. Do not create `InteropCard`, `AssuranceLane`, a new viewpoint bundle, or a formal composition witness unless a later use needs them. The face labels establish neither `U.View` membership nor assurance.

Suppose the interface account permits a retry after an explicit rejection before processing and requires a status inquiry after a lost acknowledgement. A short card for finding the interface account can stop at its reference. A card for deciding whether to retry must make the two cases distinguishable before the next send. An integrator can follow the reference to the identified rule in time. An offline shift can use a checked local copy of that edition too. If the shift has no timely authorized route to the rule, put its operative terms on the card with the source edition, or limit the card to orientation. If the lead must explain why the actions differ, a list of the two instructions can leave the question open. The source may establish that the first request could already have taken effect when an acknowledgement is lost. Carry that ground into the lead’s account. If the source gives only the instructions, publish those and identify the missing ground for the requested explanation.

The remaining examples exercise optional formal or load-bearing branches.

1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability face whose path claim matches the declared relational composition of the two source claims. `AssuranceLane(g∘f)` cites the A.10 evidence/provenance path and, only when replay needs a stable path address, its G.6 `PathId` or `PathSliceId`. The faces neither establish that composition nor become evidence carriers.
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed specification toolchains.)
3. **Optics-informed composition witness.**
    * Emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them using the selected equality. This decides the question about the Parse–Normalize–Score pair. If these are the only two generating arrows in a free path category, extending their assigned images by path composition and sending empty paths to identities supplies a functor on it. For a published mapping defined independently, check that its action agrees with that extension. Additional generators or equations change the proof obligation.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces can help inspect that relation and prepare a work plan, but they do not become work, gate passage, evidence, engineering justification, or control architecture. When one of those claims is current, recover its concrete `A.15`/`A.15.1`, `A.10`, `B.3`, or `A.20`/`A.21` grounds and any record required by the receiving use, or, for control architecture, the grounds for the architecture claim governed by `C.30` and `A.22`. Use `C.30.LCA` for a separately current control-structure-view record and `B.2.5` for a separately current supervisor-subholon feedback record. Recover any earlier object or relation under §5.1a without inventing a prior record or authority. If the required grounds cannot be recovered, withhold the dependent claim and return the specific gap or a prospective repair, decision, or work-plan request.

