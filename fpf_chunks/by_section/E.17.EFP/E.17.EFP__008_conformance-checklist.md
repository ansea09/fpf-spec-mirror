---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__008_conformance-checklist.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:7 — Conformance Checklist"
line_start: 78843
line_end: 78880
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

### E.17.EFP:7 - Conformance Checklist

A conformance check is retained only if it changes the next bounded use of the explanation rendering, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared safe next action.

Use core ordinary checks first. Conditional rows open only when reader-fit, bundle-local class difference, bounded explanation class, connective reconstruction, derivative rendering, or downstream reliance use is present.

#### E.17.EFP:7.1 - EFP-Core ordinary checks

1. **CC-EF-1 — Explanation class is explicit.**
   The explanation class is explicitly named.
2. **CC-EF-3 — Source reference and blocked downstream use are explicit.**
   The compact note states source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition.
4. **CC-EF-5 — No new A.6.B boundary claims on explanation faces.**
   The no-new-boundary-claims rule is explicit on explanation faces; the blocked claims are A.6.B-governed law claims, use-boundary claims, deontic or commitment claims, and effect or evidence claims.
5. **CC-EF-7 — No second face family.**
   A publication-side reviewer can tell why the case remains explanation-facing rather than becoming a second semantic rule track.

#### E.17.EFP:7.2 - EFP-Conditional checks

1. **CC-EF-4 — Interpretant-side block is explicit when reader-fit does real work.**
   When onboarding, contrastive explanation, or other reader-fit shaping matters, `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedReaderUse`, and `overreadRisk` are visible enough to review.
2. **CC-EF-2 — Face and `publication-face kind` boundary is explicit when present.**
   When face placement, `publication face/form`, `interop publication form`, pinning, provenance, or reliability transport is not already inherited by visible source reference, the rendering states the bounded MVPK face, `publication-face kind` value, and required pinning or provenance boundary explicitly.
3. **CC-EF-6 — Boundary to interpretation, retargeting, coarsening, and world or gate use is explicit.**
   The boundary is explicit, including `A.6.3.CSC Controlled Semantic Coarsening` when a narrower bounded claim or effect, blocked downstream claim or effect, or source-bearing reopen condition becomes primary.
4. **CC-EF-8 — Bundle-local class differences are explicit.**
   When one publication bundle carries different explanation classes across faces, that difference is stated explicitly rather than hidden under one bundle-wide label.
5. **CC-EF-9 — Source-loss or downgraded-reliability classes publish forbidden downstream uses.**
   Didactic or speculative renderings, and any rendering with downgraded reliability transport or declared source-loss mode, state their forbidden downstream uses explicitly.
6. **CC-EF-10 — Reopen triggers match the class.**
   The published review note makes class-relevant reopen triggers visible when source claim set, pins, provenance, or face-use assumptions change.
7. **CC-EF-11 — `SourceLinkedExplanationReconstruction` publishes `addedLinkPolicy` when needed.**
   When bounded connective prose is doing real review work, the rendering states what link is added, why it remains bounded, and which unsupported link class is explicitly forbidden.
8. **CC-EF-12 — Derivative renderings keep source links operative.**
   A fork, adaptation, translation, generated explanation, tutorial, access-format conversion, or other derivative rendering that will guide work or reliance maps each operative claim to the exact source passage, carrier path, or project-side FPF kind and reference named by value that evidences it, or else downgrades to reader help or applies `A.6.3.CSC` as appropriate.
9. **CC-EF-13 — Generated explanation reliance boundary is explicit.**
   A generated explanation used beyond ordinary reader help states its explanation class, source-finding state, operative claims, governing pattern for each relied-on claim, and blocked downstream use. The explanation itself is not evidence, assurance, approval, gate passage, release reliance, or work authority.

