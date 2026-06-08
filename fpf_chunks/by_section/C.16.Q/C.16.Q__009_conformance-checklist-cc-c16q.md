---
chunk_kind: "child"
pattern_id: "C.16.Q"
pattern_title: "Quality-Term Precision Restoration"
section_id: "C.16.Q:7"
section_title: "Conformance Checklist (CC-C16Q)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.Q/C.16.Q__009_conformance-checklist-cc-c16q.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "C.16.Q — Quality-Term Precision Restoration"
  - "C.16.Q:7 — Conformance Checklist (CC-C16Q)"
line_start: 41856
line_end: 41915
dependencies:
  - "A.10"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.19"
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
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.17.2"
  - "E.21"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### C.16.Q:7 - Conformance Checklist (CC-C16Q)

A text or pattern conforms to C.16.Q iff:

1. **CC-C16Q-1 - Explicit endpoint classification and explicit sense.**
   Every in-scope use of *quality* resolves either to one declared endpoint-pattern-governed evaluative form or to one declared `qualityTermAscription(...)` transitional record with one declared `QualitySense` and explicit endpoint classification.
2. **CC-C16Q-2 - Explicit bearer and arity.**
   The evaluated bearer tuple is explicit.

3. **CC-C16Q-3 - Explicit frame.**
   Evaluation frame is explicit and reviewable.

4. **CC-C16Q-4 - Evaluator and viewpoint are explicit.**
   The ascription states who evaluates, from which viewpoint, or under which selector or observer policy.

5. **CC-C16Q-5 - Substrate and referencePlane are declared when relevant.**
   Cross-talk between preconceptual, latent-distributed, symbolic-local, and `ReferencePlane` values `world`, `concept`, and `episteme` is not allowed without an explicit substrate declaration and, when live, `referencePlane` declaration when those distinctions are live.

6. **CC-C16Q-6 - Scope and `Γ_time` are explicit when omission changes meaning.**
   If scope or time selection affects interpretation, the ascription declares `U.Scope` and, when live, `Γ_time` explicitly.

7. **CC-C16Q-7 - Admissible normal form.**
   The ascription uses `SignalPack`, `Characteristic`, `Bundle`, or `Objective` as its endpoint or evaluative normal form, with the corresponding discipline observed.

8. **CC-C16Q-8 - No illegal scalarisation.**
   Composite senses are not collapsed into one score without an explicit scoring method.

9. **CC-C16Q-9 - No silent sense rewrite.**
   Any semantic change in the ascription uses the declared change lexicon; changing sense silently is forbidden.

10. **CC-C16Q-10 - QD default.**
   In search, selection, or NQD contexts, *quality* resolves to `QS.UseValue` unless overridden explicitly.

11. **CC-C16Q-11 - Engineering family discipline.**
   Engineering `-ility` uses resolve to one explicit `U.Characteristic` or one explicit `Bundle` (preferably published as `Q-Bundle` when composite); they are not left as free-floating adjectives.

12. **CC-C16Q-12 - Functional separation.**
    Function or capability claims remain distinct from quality-family claims.

13. **CC-C16Q-13 - Bridge accountability.**
    Cross-tradition parallels publish bridge stance and loss notes; cross-context or cross-plane reuse cites explicit Bridge ids and CL policy where applicable.

14. **CC-C16Q-14 - Boundary-claim hook when needed.**
    If a repaired quality ascription is used for admissibility, commitments, publication, or adjudication, the downstream `L/A/D/E` hooks are explicit rather than carried implicitly by the word *quality*.

15. **CC-C16Q-15 - Lexical firewall.**
    Bare *quality* is absent from Tech and normative prose except as quoted metalinguistic discussion.

16. **CC-C16Q-16 - `qualityTermAscription` repair-form skeleton is published.**
    The family-specific transitional token `qualityTermAscription` resolves to a repair-form skeleton that publishes bearer position, evaluator and viewpoint slots, qualifier expectations, repair paths for bearer-kind mismatches, witness discipline, admissible change classes, and cross-context or cross-plane policy.

17. **CC-C16Q-17 - Candidate-Set Note is used when ambiguity is live.**
    If sense selection, bearer facet, or A.7 lane or kind (`EntityOfConcern being described`, `description`, `episteme` or publication face, or carrier when the carrier itself is evaluated) is non-obvious, the text records a short Candidate-Set Note before the rewrite is treated as decision-bearing or publication-bearing.

18. **CC-C16Q-18 - Evaluator and viewpoint are not silently collapsed.**
    When both an evaluator and a `U.Viewpoint` matter, they are represented as separate slots or fields.

19. **CC-C16Q-19 - Family-specific change verbs dock cleanly with A.6.P and A.6.5.**
    `retargetBearer(...)` is used only for ref retargeting; sense, frame, bundle, scale, and view edits are narrated as explicit by-value revisions; silent retyping is forbidden.

