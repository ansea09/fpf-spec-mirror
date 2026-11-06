---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:5"
section_title: "Archetypal Grounding (Worked Slices)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__008_archetypal-grounding-worked-slices.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:5 — Archetypal Grounding (Worked Slices)"
line_start: 42087
line_end: 42098
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2"
  - "B.2.P"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:5 - Archetypal Grounding (Worked Slices)

**Manufacturing sequence.** A frame is prepared, welded, inspected, painted and packed. For a planning or comparison question, specify the selected steps, actual precedence, any joins used and the required result. That order specification can be the sufficient B.1.4 result. Actual shop-floor Work occurrences use `A.15.1`; energy and material roll-ups use `B.1.6`; a changed frame state uses `A.3.4`.

**Paper edition history.** When draft, reviewed and camera-ready texts change claim content, EntityOfConcern or effective ReferenceScheme, C.2.1 identifies distinct epistemes and tests each claimed `EpistemeEditionRelation` independently. B.1.4 can return a bounded chronology over those identities, obtaining relations and relevant applicability or publication windows. The editions retain their distinct identities. If one unchanged episteme is needed over a proper interval, A.14 `PhaseOf` states that restriction. Source-currentness and publication-use claims use `A.10`, `G.11` and `E.17` as applicable; chronology establishes none of them.

**Cross-regime evidence window.** A dashboard combines observations from two operating regimes. Identify the exact observation sets, their subject populations or carriers, temporal reference and aggregation window. Choose the operation and the claim it is meant to support. Under `C.16`, establish the measurement meanings, specification, scale and unit semantics, model/calibration conditions and population or time basis needed for direct comparability. Any cross-basis conversion or comparison retains its own operation rule and loss or uncertainty conditions. Use `C.29` when a separate mathematical correspondence or reliance question remains. If the required compatibility is unestablished, retain separate results or narrow the claim rather than pool them as one supported aggregate.

**Order-dependent calculation.** In this constructed case, start with `x = 1` and combine `f(x) = x + 1` and `g(x) = 2x` by sequential application. Applying f then g gives `g(f(1)) = 4`; applying g then f gives `f(g(1)) = 3`. An OrderSpec permitting both orders does not establish one numerical answer or the independence needed to ignore order. If the use needs a unique answer, establish the required precedence or a justified operator property that makes all permitted orders equivalent. Otherwise retain the two supported outcomes. If the task needs only the partial-order specification, that specification already answers it.

**Work-interval aggregate.** In this constructed case, independently admitted Work occurrences W1 and W2 occupy `[0,2)` and `[3,5)` hours under one declared clock reference, within window `[0,5)`. For covered time, take the union `[0,2) ∪ [3,5)`: its duration is 4 hours. For elapsed span from first start to last end, take the convex hull `[0,5)`: its duration is 5 hours, including the gap. These are different warranted answers to different questions, following the A.15.1:9.1 Work-interval profile. Union counts a shared instant once when intervals overlap. Its set-based policy and the hull policy are idempotent for duplicate input and independent of input order; another operator needs its own laws. The two occurrences keep their separate identities and require no invented common Work or `PhaseOf` relation.

