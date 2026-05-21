---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "U.ActionInvitationPrecisionRestoration - Affordance / Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:7"
section_title: "Conformance Checklist (CC-A.6.A)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__008_conformance-checklist-cc-a-6-a.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "A.6.A — U.ActionInvitationPrecisionRestoration - Affordance / Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:7 — Conformance Checklist (CC-A.6.A)"
line_start: 14095
line_end: 14160
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.3"
  - "A.6.B"
  - "A.6.P"
  - "A.6.Q"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.17"
  - "E.18"
  - "F.9"
keywords:
  - "A.15 docking"
  - "action invitation"
  - "action-first language"
  - "affordance"
  - "language-state seam"
  - "post-threshold classification"
---

### A.6.A:7 - Conformance Checklist (CC-A.6.A)

A text or pattern conforms to A.6.A iff:

1. **CC-A.6.A-1 — Explicit post-threshold relation family and explicit sense.**
   Every in-scope post-threshold action-first use resolves to one declared `actionInvitation(...)` instance and one declared `ActionInvitationSense`; earlier cue-like content stays under `A.16.1` or `B.4.1` instead of being forced into A.6.A prematurely.
2. **CC-A.6.A-2 — Explicit site and site-facet docking.**
   The site tuple is explicit; when ambiguous or mixed, the A.7 lane map (`Object | Description | Carrier`) is explicit.

3. **CC-A.6.A-3 — Explicit invited enactor.**
   The invited enactor tuple is explicit.

4. **CC-A.6.A-4 — Enactor discipline.**
   When the invited enactor is meant as the actual would-be enactor, it resolves to a `U.System` or role assignment with system holder.

5. **CC-A.6.A-5 — Explicit candidate action.**
   The candidate action tuple is explicit and reviewable.

6. **CC-A.6.A-6 — Explicit coupling frame.**
   The coupling frame is explicit.

7. **CC-A.6.A-7 — Detector/viewpoint separation.**
   When both matter, `detector` and `viewpoint` are not silently collapsed.

8. **CC-A.6.A-8 — Lawful normal form.**
   The invitation is published as `CuePack`, `ActionOption`, `OptionSet`, or `PolicyHook`, with corresponding discipline observed.

9. **CC-A.6.A-9 — Articulation-hint discipline.**
   If omission changes meaning, `articulationHint` is explicit and is not treated as **F** or as an acceptance state.

10. **CC-A.6.A-10 — No invitation-as-obligation.**
    An invitation is not silently published as a duty or gate.

11. **CC-A.6.A-11 — No invitation-as-work.**
    An invitation is not silently published as a work occurrence.

12. **CC-A.6.A-12 — No capability collapse.**
    A situated invitation is not silently rewritten as a general capability claim.

13. **CC-A.6.A-13 — No object-property collapse.**
    Affordance language is not published as a monadic object property when actor/site/frame matter.

14. **CC-A.6.A-14 — No hidden scalarisation.**
    `OptionSet` publication does not introduce a hidden total score or ranking without an explicit comparator / policy.

15. **CC-A.6.A-15 — No silent sense rewrite.**
    Sense changes use the declared change lexicon.

16. **CC-A.6.A-16 — No silent relation-family switch.**
    Moving from invitation to quality ascription, capability, commitment, or work uses `changeRelationKind(...)` or an explicit split.

17. **CC-A.6.A-17 — Bridge accountability.**
    Cross-tradition parallels publish bridge stance and loss notes.

18. **CC-A.6.A-18 — Boundary-claim hook when needed.**
    If the repaired invitation is used for admissibility, commitments, publication, or automation, downstream `L/A/D/E` hooks are explicit.

19. **CC-A.6.A-19 — Lexical firewall.**
    Bare action-first trigger tokens are absent from Tech / normative prose except as quoted metalinguistic discussion.

20. **CC-A.6.A-20 — `actionInvitation` relation specification skeleton is published.**
    The family-specific `RelationKind` token resolves to a relation specification skeleton with SlotSpecs, enactor/site discipline, qualifier expectations, repair paths, witness discipline, admissible change classes, and cross-context policy.

21. **CC-A.6.A-21 — Candidate-Set Note is used when ambiguity is live.**
    If the site lane map, enactor lane, relation family, or sense selection is non-obvious, the text records a short Candidate-Set Note before decision-bearing use.

