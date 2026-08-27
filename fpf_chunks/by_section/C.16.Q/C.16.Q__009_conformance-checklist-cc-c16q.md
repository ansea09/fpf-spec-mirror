---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:7"
section_title: "Conformance Checklist (CC-C16Q)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__009_conformance-checklist-cc-c16q.md"
commit_sha: "3f6714ae3235e0d771dce32835be7696f626d2ee"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:7 — Conformance Checklist (CC-C16Q)"
line_start: 48368
line_end: 48410
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.16.P"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "C.30.AD"
  - "C.30.ASV"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
  - "U.ClaimScope"
  - "U.ContextSlice"
  - "U.ViewpointRef"
keywords:
---

### C.16.Q:7 - Conformance Checklist (CC-C16Q)

A text or pattern conforms to C.16.Q iff:

1. **CC-C16Q-1 - Explicit endpoint classification and explicit sense.**
   Every in-scope use resolves either to the evaluative form for one declared endpoint or to one declared `qualityTermAscription(...)` transitional record with a `QualitySense` and explicit endpoint classification.
2. **CC-C16Q-2 - Exact bearer and arity.**
   The evaluated bearer designator or tuple is explicit; description, carrier, evaluator, viewpoint, work, and result are not substituted for it.
3. **CC-C16Q-3 - Exact probe/model and comparison frames.**
   The domain-local probe or model frame and the separately governed comparison frame or explicit `none` are stated and reviewable; no generic field silently selects either frame.
4. **CC-C16Q-4 - Effective scheme, evaluator, and viewpoint reference.**
   The effective `U.ReferenceScheme` is explicit. Evaluator and `U.ViewpointRef` are separate; a non-`none` reference resolves one exact viewpoint episteme and grants no conformance, membership, authority, or result.
5. **CC-C16Q-5 - Substrate and referencePlane are declared when relevant.**
   Cross-talk between preconceptual, latent-distributed, symbolic-local, and `ReferencePlane` values `world`, `concept`, and `episteme` is not allowed without explicit substrate and, when live, plane declarations.
6. **CC-C16Q-6 - ClaimScope, slices, and `Γ_time` are explicit.**
   One `U.ClaimScope`, its meaning-changing `U.ContextSlice` members, and any meaning-changing `Γ_time` are stated; work or publication scope does not substitute for claim scope.
7. **CC-C16Q-7 - Admissible normal form and result boundary.**
   The ascription uses `SignalPack`, `Characteristic`, `Bundle`, or `Objective` with the corresponding normal-form discipline; any checked object, assessment work, result claim, witnesses, evidence-provenance path, and empirical-grounding relation remain independently identified.
8. **CC-C16Q-8 - No illegal scalarization.**
   Composite senses are not collapsed into one score without an explicit admissible scoring and comparison method.
9. **CC-C16Q-9 - No silent sense rewrite.**
   Any semantic change uses the declared change lexicon; changing sense, scheme, frame, scope, or neighboring relation silently is forbidden.
10. **CC-C16Q-10 - QD default.**
    In search, selection, or NQD practice, *quality* resolves to `QS.UseValue` unless overridden explicitly.
11. **CC-C16Q-11 - Engineering family discipline.**
    Engineering `-ility` uses resolve to one explicit `U.Characteristic` or one explicit `Bundle`, preferably a `Q-Bundle` when composite; they do not remain free-floating adjectives.
12. **CC-C16Q-12 - Functional separation.**
    Function or capability claims remain distinct from quality-family claims.
13. **CC-C16Q-13 - Bridge accountability.**
    Cross-local comparison resolves exact F.17 cells and cites an obtaining F.9 Bridge plus the exact bounded-use claim when a use is proposed. Any optional Card and F.9.1 stance note remain separate; the stance note's `EntityOfConcern` is that claim. A stance word, `CL`, shared label, or loss note establishes none of them.
14. **CC-C16Q-14 - Boundary-claim hook when needed.**
    If a repaired ascription is used for admissibility, commitment, publication, evidence-bearing decision, or adjudication, the downstream `L/A/D/E` claims and the patterns used to define or test them are explicit.
15. **CC-C16Q-15 - Lexical firewall.**
    Bare *quality* is absent from Tech and normative prose except as quoted and marked metalinguistic discussion.
16. **CC-C16Q-16 - Transitional skeleton is complete.**
    The published skeleton carries bearer position and bearer-kind mismatch repair, sense, effective scheme, exact frames, evaluator, `U.ViewpointRef`, ClaimScope, qualifier expectations, normal form, result, witness/evidence/grounding discipline, admissible change classes, and cross-local boundaries without minting universal context, frame, evidence, or grounding kinds.
17. **CC-C16Q-17 - Candidate-Set Note is used when ambiguity is live.**
    If sense selection, bearer facet, or A.7 lane or kind (`EntityOfConcern being described`, `description`, `episteme` or publication face, or carrier when the carrier itself is evaluated) is non-obvious, the text records a short Candidate-Set Note before decision-bearing or publication-bearing use.
18. **CC-C16Q-18 - Reference resolution is not object substitution.**
    Designators, governed refs, their resolved viewpoint or bearer objects, evaluator, result, frame, scope, grounding holon, and any selected structure remain distinct.
19. **CC-C16Q-19 - Change verbs dock cleanly with A.6.P and A.6.5.**
    `retargetBearer(...)` and the other declared reference moves are used only for ref retargeting; by-value revisions use their declared verbs; a scheme or scope change triggers claim-identity review; edits to witnesses, evidence paths, grounding, Bridge, bounded-use-claim, Card, or stance-note refs do not silently rewrite one another; and silent retyping is forbidden.

