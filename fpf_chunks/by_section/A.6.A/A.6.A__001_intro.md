---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "Affordance and Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__001_intro.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.6.A — Affordance and Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:intro — Intro"
line_start: 19222
line_end: 19274
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.3"
  - "A.6.B"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "action-first language"
  - "affordance"
  - "detection"
  - "inquiry question"
  - "physical opportunity"
  - "wording recovery"
---

## A.6.A - Affordance and Action-Invitation Precision Restoration (ACT-INV)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Affordance and action-invitation precision restoration.

**Use this pattern when** wording such as “affords”, “invites”, “calls for” or “actionable” leaves the intended claim or question unclear: who could do what, in which situation, on what grounds, and what the reader may do with that statement.

**What goes wrong if missed.** A physical opportunity, detected cue, proposed inquiry or interface prompt is read as a capability, duty, permission or completed action. The reader acts on the wording without recovering the claim that would justify that action.

**What this buys.** A sufficient statement of the actual opportunity, prompt, claim or question, with the participants, conditions and subject rule needed for its use. An unresolved rule or fact is returned as an exact gap. An ordinary sentence can be the complete result.

**First useful move.** Recover what the speaker means in this use. Compare the live alternatives—for example, an available physical action, detection of that opportunity, an operator prompt, or a proposed inquiry. State the supported interpretation or the question that distinguishes the remaining alternatives. Apply the recovered subject rule before asserting its result.

**Not this pattern when.** If the claim and its subject are already clear, use that subject pattern directly—for example, for a Method, MethodDescription, WorkPlan, actual Work, ability, duty, gate, evidence, evaluation or publication. A sufficient existing sentence needs no further recovery note.

**Governed move.** This pattern recovers the meaning of affordance-like and action-first wording. Its interpretation menu and optional recovery note do not define one common relation kind or a durable U-kind. Any actual opportunity, relation occurrence, Method, ability or Work that the result names keeps its own subject, obtaining conditions and identity rule.

**Intent.**
Provide a reusable discipline for repairing overloaded **affordance-like and action-first** language in FPF texts.

Use **A.6.P** when the recovered content is a relation claim. Other recovered results, including an open inquiry question, go directly to their governing patterns. The recurring repair is to recover meaning, relevant participants and conditions, then express the result sufficiently for the receiving use.
Preserve an insufficiently articulated cue through `A.16.1` or publish its possible continuations through `B.4.1`. A question can become clear enough for inquiry while its answer remains unknown.
When the recovered result selects a Method for enactment, identify that independently admitted `U.Method`; a cited MethodDescription is a separate C.2.1 episteme used to identify, constrain or justify it. A proposed action or question need not invent a Method merely to become expressible. Intended Work remains a `U.WorkPlan`, and actual enactment remains dated `U.Work` with exact `enactsMethod` under **A.15**.

It allows ecological-psychology, phenomenological, active-inference, control-theoretic, interface, engineering-operations, and robotics uses to coexist **without false identity by label**.

**Placement.**
Part A > cluster **A.6 Signature Stack & Boundary Discipline** > recovery of under-specified affordance-like and action-first language, using **A.6.P** for its relation-claim branch.

**Builds on.**
A.3, A.6, A.6.B, A.6.P, A.6.REL, A.6.RSIR, A.6.S, A.6.0, A.6.5, A.2.6, A.7, A.15, E.8, E.10, F.9, F.18.

**Coordinates with.**
**C.16.Q** for evaluative-language repair; **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, articulation and closure coordination, admissible moves, early cue classification, next-use docking, and admissible retreat when a published recovery result must be reopened; use **A.16.0** only when lineage, branch, loss, or an actual responsibility-handoff history itself must be published as an explicit trajectory account; **B.5.2.0** when the recovered result is an explanatory question or candidate inquiry; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for articulation, closure, anchoring, and representation-factor facets referenced but not governed here; **A.10** and **B.3** for evidence and assurance; **B.4** and **B.5** for anomaly-driven cycles; **E.17.0**, **E.17**, and **E.18** for viewpoint reference resolution, independent view conformance, and viewpoint publication; **F.9** for Bridges and bounded-use claims; **F.9.1** for optional stance notes about those claims; **C.3.3** for kind-bridge repair when endpoint kind mismatches appear.

**E.10.ARCH relation.**
A.6.A supplies the wording-recovery method when an `E.10` or `E.10.ARCH` use leaves an affordance-like or action-first phrase ambiguous. Recover the actual claim or question and then its direct governor. Evaluative content goes to `C.16.Q`; ability, Method, Work, duty, evidence, assurance, gate and decision claims use their own patterns. Keep a recovery note only when a later reader needs the interpretation or its grounds.

**Non-goal.**
This pattern does **not** assert that physical affordances, interface affordances, social affordances, epistemic probe moves, articulation-closure moves, latent policy cues, and control opportunities are one concept.

Its job is to publish a disciplined treatment of action-first language across those traditions, using a direct contrast when that is enough and an F.9 Bridge only for an exact cross-context semantic-correspondence claim, while preventing false identity by shared language.

The recovered meaning selects the next pattern:

* where the repaired statement is primarily **evaluative**, use **C.16.Q**;
* where it is primarily about **general capability**, capability wording, method wording, or method-description wording, use **A.6.F**, A.2.2 qualified holder capability, `U.Method`, or `MethodDescription` according to the claim being made;
* where it is primarily **deontic**, apply **A.6.B**;
* where it is primarily about **scheduled or executed enactment**, use the governing **A.15** pattern family: exact `U.Method`, separate `U.MethodDescription`, intended `U.WorkPlan`, and actual `U.Work` with exact `enactsMethod` once execution has occurred. Keep any wording-recovery note separate from those objects.

