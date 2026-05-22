---
chunk_kind: "child"
pattern_id: "A.6.Q"
pattern_title: "U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
section_id: "A.6.Q:7"
section_title: "Conformance Checklist (CC-A.6.Q)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.Q/A.6.Q__008_conformance-checklist-cc-a-6-q.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.6.Q — U.QualityTermPrecisionRestoration — Quality Term Precision Restoration (Q-TERM)"
  - "A.6.Q:7 — Conformance Checklist (CC-A.6.Q)"
line_start: 13346
line_end: 13405
dependencies:
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.17"
  - "A.18"
  - "A.2.6"
  - "A.6.A"
  - "A.6.B"
  - "A.6.P"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "C.25"
  - "E.17.0"
  - "E.17.2"
  - "F.9"
  - "F.9.1"
keywords:
  - "bridge reading"
  - "endpoint classification"
  - "evaluative ascription"
  - "language-state seam"
  - "quality senses"
  - "quality-term precision restoration"
---

### A.6.Q:7 - Conformance Checklist (CC-A.6.Q)

A text or pattern conforms to A.6.Q iff:

1. **CC-A.6.Q-1 - Explicit endpoint classification and explicit sense.**
   Every in-scope use of *quality* resolves either to one declared endpoint-pattern-governed evaluative form or to one declared `evaluativeAscription(...)` transitional record with one declared `QualitySense` and explicit endpoint classification.
2. **CC-A.6.Q-2 - Explicit bearer and arity.**
   The evaluated bearer tuple is explicit.

3. **CC-A.6.Q-3 - Explicit frame.**
   Evaluation frame is explicit and reviewable.

4. **CC-A.6.Q-4 - Evaluator/viewpoint is explicit.**
   The ascription states who evaluates, from which viewpoint, or under which selector/observer policy.

5. **CC-A.6.Q-5 - Substrate and referencePlane are declared when relevant.**
   Cross-talk between preconceptual, latent-distributed, symbolic-local, and world/concept/epistemic uses is not allowed without an explicit substrate and/or `referencePlane` declaration when those distinctions are live.

6. **CC-A.6.Q-6 - Scope and `Γ_time` are explicit when omission changes meaning.**
   If scope or time selection affects interpretation, the ascription declares `U.Scope` and/or `Γ_time` explicitly.

7. **CC-A.6.Q-7 - Lawful normal form.**
   The ascription is published as `SignalPack`, `Characteristic`, `Bundle`, or `Objective`, with the corresponding discipline observed.

8. **CC-A.6.Q-8 - No illegal scalarisation.**
   Composite senses are not collapsed into one score without an explicit scoring method.

9. **CC-A.6.Q-9 - No silent sense rewrite.**
   Any semantic change in the ascription uses the declared change lexicon; changing sense silently is forbidden.

10. **CC-A.6.Q-10 - QD default.**
   In search/selection/NQD contexts, *quality* resolves to `QS.UseValue` unless overridden explicitly.

11. **CC-A.6.Q-11 - Engineering family discipline.**
   Engineering `-ility` uses resolve to one explicit `U.Characteristic` or one explicit `Bundle` (preferably authored as `Q-Bundle` when composite); they are not left as free-floating adjectives.

12. **CC-A.6.Q-12 - Functional separation.**
    Function/capability claims remain distinct from quality-family claims.

13. **CC-A.6.Q-13 - Bridge accountability.**
    Cross-tradition parallels publish bridge stance and loss notes; cross-context or cross-plane reuse cites explicit Bridge ids and CL policy where applicable.

14. **CC-A.6.Q-14 - Boundary-claim hook when needed.**
    If a repaired quality ascription is used for admissibility, commitments, publication, or adjudication, the downstream `L/A/D/E` hooks are explicit rather than carried implicitly by the word *quality*.

15. **CC-A.6.Q-15 - Lexical firewall.**
    Bare *quality* is absent from Tech/normative prose except as quoted metalinguistic discussion.

16. **CC-A.6.Q-16 - `evaluativeAscription` relation specification skeleton is published.**
    The family-specific `RelationKind` token `evaluativeAscription` resolves to a relation specification skeleton that publishes polarity, participant SlotSpecs, qualifier expectations, repair paths for bearer-kind mismatches, witness discipline, admissible change classes, and cross-context or cross-plane policy.

17. **CC-A.6.Q-17 - Candidate-Set Note is used when ambiguity is live.**
    If sense selection, bearer facet, or A.7 lane (`Object | Description | Carrier`) is non-obvious, the text records a short Candidate-Set Note before the rewrite is treated as decision-bearing or publication-bearing.

18. **CC-A.6.Q-18 - Evaluator and viewpoint are not silently collapsed.**
    When both an evaluator and a `U.Viewpoint` matter, they are represented as separate slots or fields.

19. **CC-A.6.Q-19 - Family-specific change verbs dock cleanly with A.6.P / A.6.5.**
    `retargetBearer(...)` is used only for ref retargeting; sense/frame/bundle/scale/view edits are narrated as explicit by-value revisions; silent retyping is forbidden.

