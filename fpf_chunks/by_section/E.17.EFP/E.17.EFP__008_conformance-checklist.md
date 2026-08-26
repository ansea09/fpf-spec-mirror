---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__008_conformance-checklist.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:7 — Conformance Checklist"
line_start: 80667
line_end: 80706
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
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

These checks apply only after EFP's use condition survives the simpler-note comparison. Retain a check only if it changes the next bounded use, blocks a concrete overclaim, or preserves the source or reopen condition needed for that action.

Use core ordinary checks first. Conditional rows open only when reader-fit, bundle-local class difference, bounded explanation class, connective reconstruction, derivative rendering, or downstream reliance use is present.

#### E.17.EFP:7.1 - EFP-Core ordinary checks

0. **CC-EF-0 — Exact episteme and ClaimGraph branch are recoverable.**
   The text is identified as a form or representation of the same source ClaimGraph, or as a form of an exact target episteme connected by an obtaining source-to-target relation. A speculative causal or counterfactual claim is a separate B.5.2 hypothesis episteme.
1. **CC-EF-1 — Explanation class follows identity.**
   The class is explicitly named for the publication form after CC-EF-0; it is not used as episteme identity or source-to-target evidence.
2. **CC-EF-3 — Source reference and blocked downstream use are explicit.**
   The compact note states source reference, bounded explanation-reader use, blocked downstream use, and reopen or boundary condition.
4. **CC-EF-5 — No new A.6.B boundary claims on explanation faces.**
   The no-new-boundary-claims rule is explicit on explanation faces; the blocked claims are law claims tested under A.6.B, use-boundary claims, deontic or commitment claims, and effect or evidence claims.
5. **CC-EF-7 — No second face family.**
   A publication-side reviewer can tell why the case remains explanation-facing rather than becoming a second semantic rule track.

#### E.17.EFP:7.2 - EFP-Conditional checks

1. **CC-EF-4 — Interpretant-side block is explicit when reader-fit does real work.**
   Only the reader-fit distinctions that change the current class, bounded use, blocked use, or reopen condition are stated. The five optional prompts are not a required block.
2. **CC-EF-2 — Face and `publication-face kind` boundary is explicit when present.**
   State face, pinning, provenance, or reliability details only when the present form choice, dispute, derivative, or receiving use makes that boundary material and it is not already recoverable by source reference.
3. **CC-EF-6 — Boundary to interpretation, retargeting, coarsening, and world or gate use is explicit.**
   The boundary is explicit, including `A.6.3.CSC Controlled Semantic Coarsening` when a narrower bounded claim or effect, blocked downstream claim or effect, or source-bearing reopen condition becomes primary.
4. **CC-EF-8 — Bundle-local class differences are explicit.**
   When one publication bundle carries different explanation classes across faces, that difference is stated explicitly rather than hidden under one bundle-wide label.
5. **CC-EF-9 — Source-loss or changed-claim cases retain exact identity and use boundaries.**
   A didactic target names its exact A.6.3 or other relation; a speculative form names its exact B.5.2 hypothesis episteme. Any material source loss or reliability downgrade states its bounded and forbidden uses without pretending that the EFP class supplies identity or relation evidence.
6. **CC-EF-10 — Reopen triggers match the class.**
   The published review note makes class-relevant reopen triggers visible when source claim set, pins, provenance, or face-use assumptions change.
7. **CC-EF-11 — Every non-obvious source-linked connective has an actual basis.**
   The exact source claims and effective scheme yield a stated derivation, or those source claims already report an exact relation occurrence whose obtaining is independently established. `addedLinkPolicy` points to that basis; without it, the added claim becomes an exact target episteme under its direct pattern or exits EFP.
8. **CC-EF-12 — Derivative renderings keep source links operative.**
   A fork, adaptation, translation, generated explanation, tutorial, access-format conversion, or other derivative rendering that will guide work or reliance maps each operative claim to the exact source passage, carrier path, or project record that evidences it and names that record's FPF kind when material, or else downgrades to reader help or applies `A.6.3.CSC` as appropriate.
9. **CC-EF-13 — Generated explanation reliance boundary is explicit.**
   A generated explanation used beyond ordinary reader help states its explanation class, source-finding state, operative claims, the FPF pattern used to test each relied-on claim, the exact project record that carries it, and blocked downstream use. The explanation itself is not evidence, assurance, approval, gate passage, release reliance, or work authority.

