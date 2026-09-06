---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:8"
section_title: "Archetypal Grounding (SoTA-aligned Local Tests)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__009_archetypal-grounding-sota-aligned-local-tests.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:8 — Archetypal Grounding (SoTA-aligned Local Tests)"
line_start: 83228
line_end: 83246
dependencies:
  - "A.10"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.2"
  - "A.6.3"
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

Read these examples as local tests for MVPK invariants, not as source citations by reputation.

**Ordinary two-reader publication.** An accepted interface account already states the service boundary, messages, and failure conditions. A project lead needs a short explanation and an integrator needs the typed details. Publish one `PlainView` and one `TechCard`, both pointing to that same account and stating what they omit; do not create `InteropCard`, `AssuranceLane`, a new viewpoint bundle, or a formal composition witness unless a later use actually needs them. The face labels establish neither `U.View` membership nor assurance.

The remaining examples exercise optional formal or load-bearing branches.

1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability face whose path claim matches the declared relational composition of the two source claims; `AssuranceLane(g∘f)` cites the A.10 evidence/provenance path and, only when replay needs a stable path address, its G.6 `PathId` or `PathSliceId`. The faces neither establish that composition nor become evidence carriers.
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed specification toolchains.)
3. **Optics-informed composition witness.**
    * Profunctor and optic accounts are useful only as a source idea for why compositional publication matters. The local FPF test is still the MVPK witness: emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them. If the comparison is not supplied or fails, the face stays non-compositional or explanatory-only; optics vocabulary does not carry the rule by analogy.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces can help inspect that relation and prepare a work plan, but they do not become work, gate passage, evidence, engineering justification, or control architecture. When one of those claims is current, recover its concrete `A.15`/`A.15.1`, `A.10`, `B.3`, `A.20`/`A.21`, or `B.2.5` record; if none exists, create only a prospective repair, decision, or work-plan request rather than backdating the claim.

