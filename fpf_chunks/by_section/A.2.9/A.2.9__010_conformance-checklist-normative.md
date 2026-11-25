---
chunk_kind: "child"
pattern_id: "A.2.9"
pattern_title: "U.SpeechAct — Communicative Work and Its Intended Use"
section_id: "A.2.9:7"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.9/A.2.9__010_conformance-checklist-normative.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "A.2.9 — U.SpeechAct — Communicative Work and Its Intended Use"
  - "A.2.9:7 — Conformance Checklist (normative)"
line_start: 9522
line_end: 9538
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.2.8"
  - "A.2.9"
  - "A.6.C"
  - "A.7"
  - "F.6"
  - "U.Work"
keywords:
  - "A.13-qualified actual performer"
  - "containment"
  - "enacted Method"
  - "evidence carrier"
  - "independently admitted speech-act Work"
  - "institutional target and effect"
  - "named receiving use"
  - "optional SpeechActRecord"
  - "publication relation"
  - "response versus achievement"
  - "same obtaining assignment"
  - "separate later performedUnderAssignment"
  - "smallest repair or stop"
  - "time"
  - "utterance description"
---

### A.2.9:7 — Conformance Checklist (normative)

1. **CC‑A.2.9‑1 (Occurrence, performer, and assignment).** One Work individual is admitted as `SA : U.SpeechAct` only through the independent A.13/A.15.1 route: the grounded communicative history, enacted Method, extent and containment, with each actual performer System’s A.13 basis (local agential kind and criterion, classification, obtaining assignment, scope, working situation, window, core evidence and any conditionally required profile). Any precise assignment-bound attribution is then checked separately through F.6 with the same obtaining assignment; its declared species, holder, other participants, predicate, and coverage remain recoverable.

   A `SpeechActRecord` **MUST** identify all actual performers using §4.2. For each exact assignment-bound attribution it claims, `performedUnderAssignmentRef` **MUST** resolve to F.6 for this act and that performer’s A.13 assignment. Establish authority under the applicable rule.
   - **CC‑A.2.9‑1a (Occurrence identity and segmentation).** Several satisfied `actTypes` classify one communicative Work unless distinct performance history, enacted Methods, institutional actions, or another admitted discriminator establishes distinct occurrences. Shared utterance, carrier, or interval is not enough; unresolved competing segmentations retain an explicit continuity or segmentation question.
2. **CC‑A.2.9‑2 (Exact Method and auxiliary description).** The actual occurrence independently satisfies `enactsMethod -> U.Method`. A current `methodDescriptionRef` resolves to a separate C.2.1 episteme used to identify, constrain, or justify that Method or intended Work; neither the reference nor the description is enacted.
3. **CC‑A.2.9‑3 (Recognition taxonomy and scheme).** The actual occurrence satisfies at least one `SpeechActTypeRef` defined by the exact recognition-taxonomy episteme under the stated effective reference scheme. Merely writing a token into `SpeechActRecord.actTypes` is insufficient.
4. **CC‑A.2.9‑4 (Actual extent versus effect interval).** The occurrence has an actual temporal extent, and a record's `window` truthfully states it at the required precision. Every instituted relation keeps its own occurrence or validity interval.
5. **CC‑A.2.9‑5 (Observable relied-on occurrence and attribution branch).** If a checklist, guard, or judgement about a commitment or grant relies on the occurrence, apply SA-C4: one `SpeechActRecord` identifies it and cites an applicable utterance, carrier, or direct evidence relation. Evidence-critical uses **SHOULD** cite at least one carrier through A.10. If that checklist, guard, gate, or claim relies on exact assignment-bound attribution, the record **MUST** include `performedUnderAssignmentRef` for every act–assignment pair on which the decision relies. Apply SA-C1 to each relation, including several assignments of one actual performer. An omitted relation leaves the corresponding attribution open.
6. **CC‑A.2.9‑6 (Current policy and typed world-side effects).** A record's `institutes.*` branch references only an exact commitment or obtaining relation occurrence through its declared relation-occurrence RefKind. An `otherGovernedRelations` item also names the rule that defines and tests that exact relation. An institutional effect obtains only when the current policy or procedure supplies the applicable constitutive rule and current facts satisfy the direct predicate defined in its pattern or declaration; a status claim and its evidence stay separate.
7. **CC‑A.2.9‑7 (F.9 only for cross-locality dependence).** A receiving claim cites an F.9 Bridge only when it compares, substitutes, or transfers speech-act or policy meaning across different local taxonomies, schemes, or policies. A new consumer or locality label alone neither requires a Bridge nor transfers force.
8. **CC‑A.2.9‑8 (No fabricated method anchor or candidate record).** If the actual `enactsMethod -> U.Method` relation cannot be recovered well enough to establish A.15.1 admission, do not create a conformant `SpeechActRecord`. Put the unresolved claim, source-gap provenance, known observations, and explicit unknowns in the separate candidate observation stub; that stub remains observation-only and cannot support a gate or deontic provenance. A placeholder `U.MethodDescription` never closes the gap. After actual admission, create a distinct complete record rather than promoting the stub in place.
9. **CC‑A.2.9‑9 (Subject, target, and effect stay distinct).** A record uses `utteranceSubjectRefs` for aboutness and `institutionalTargetRefs` only for a policy-selected target. It claims actual change or institutional effect only through the exact direct relation; an informative act needs no changed target.
10. **CC‑A.2.9‑10 (Optional channel stays separate).** A `channelRef`, utterance description, carrier, or trace may support identification or observation.
11. **CC‑A.2.9‑11 (Receiving use, evidence, and later effect).** Judge the act against what the named recipient was to obtain. When the applicable terms make a particular response constitute acceptance, establish the authorised act and its other conditions. Where the criterion concerns understanding, use, permission or causal contribution, identify what establishes that claim. A revised use applies to later communication or to an explicitly named reevaluation.

