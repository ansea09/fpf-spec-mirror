---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:8"
section_title: "Archetypal Grounding (SoTA-aligned Local Tests)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__009_archetypal-grounding-sota-aligned-local-tests.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:8 — Archetypal Grounding (SoTA-aligned Local Tests)"
line_start: 75929
line_end: 75943
dependencies:
  - "A.15.4"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
keywords:
---

### E.17:8 - Archetypal Grounding (SoTA-aligned Local Tests)

Read these examples as local tests for MVPK invariants, not as source citations by reputation.

1. **Composite service pipeline (`InteropCard` + `AssuranceLane`).**
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability **view** whose path set equals the **relational composition** of the two cards; `AssuranceLane(g∘f)` cites test records as evidence **carriers** with edition pins. (Carriers, not semantics; concrete envelope formats are outside Part E.)
2. **Control loop morphism (`TechCard` + `PlainView`).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed specification toolchains.)
3. **Optics-informed composition witness.**
    * Profunctor and optic accounts are useful only as a source idea for why compositional publication matters. The local FPF test is still the MVPK witness: emit the face for `g∘f`, compose the emitted faces for `f` and `g`, and compare them. If the comparison is not supplied or fails, the face stays non-compositional or explanatory-only; optics vocabulary does not carry the rule by analogy.

4. **Functional-description publication (`PlainView` + `TechCard`).**
    A principle scheme or functional diagram can publish a readable relation from signature or principle episteme content to method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, and result measurement. The MVPK faces can help a team inspect that relation and prepare a work plan, but they do not turn the diagram, table, screen, or export into work occurrence, gate passage, evidence, engineering justification, or supervisory or control architecture. For those uses, the team first recovers the existing typed project-side FPF kind and reference named by value that carries the claim when available: `A.15.4` appearance-based reliance repair when the face is being used as the reason before the governing pattern slot or relation is named, project `U.Method`, `U.WorkPlan`, and dated `U.Work` occurrence under `A.15` and `A.15.1`, evidence or provenance path under `A.10`, engineering-justification record under `B.3`, gate or constraint decision under `A.20` or `A.21`, or supervisory or control architecture record under `B.2.5`. If no existing typed project-side FPF record or source relation carries the needed claim, create only a prospective repair request, prospective decision request, prospective work-plan entry, or explicit missing-source-relation note; do not backdate evidence, gate passage, work occurrence, release permission, engineering justification, or assurance for the earlier claim.

