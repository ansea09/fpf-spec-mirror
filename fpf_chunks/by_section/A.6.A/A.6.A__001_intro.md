---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "U.ActionInvitationPrecisionRestoration - Affordance / Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__001_intro.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "A.6.A — U.ActionInvitationPrecisionRestoration - Affordance / Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:intro — Intro"
line_start: 13565
line_end: 13602
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

## A.6.A - `U.ActionInvitationPrecisionRestoration` - Affordance / Action-Invitation Precision Restoration (ACT-INV)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Affordance / action-invitation precision restoration.

**Intent.**
Provide a reusable discipline for repairing overloaded **affordance / action-first** language in FPF texts.

This pattern is an **A.6.P RPR specialisation** for **post-threshold** action-oriented content: it turns bare action-oriented prose into one explicit, slot-explicit **action invitation** relation family with a declared **sense family**, admissible **normal forms** (`CuePack | ActionOption | OptionSet | PolicyHook`), explicit **change semantics**, and lexical guardrails.
Pre-threshold action-guiding cue content remains with `A.16.1` / `B.4.1` until the cue is articulated enough for `actionInvitation(...)` publication.
It does **not** mint a parallel execution ontology: whenever an invitation is articulated far enough to reference executable method descriptions, work plans, or work occurrences, publication SHALL dock to the exact **A.15** lane (`U.Method`, `U.MethodDescription`, `U.WorkPlan`, or actual `U.Work` once execution has occurred) rather than inventing new action kinds by prose.

It allows ecological-psychology, phenomenological, active-inference, control-theoretic, interface, engineering-operations, and robotics uses to coexist **without false identity by label**.

**Placement.**
Part A > cluster **A.6 Signature Stack & Boundary Discipline** > specialisation of **A.6.P** for under-specified affordance / action-first language.

**Builds on.**
A.3, A.6, A.6.B, A.6.P, A.6.S, A.6.0, A.6.5, A.2.6, A.7, A.15, E.8, E.10, F.9, F.18.

**Coordinates with.**
**A.6.Q** for evaluative-language repair; **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, articulation/closure coordination, admissible moves, early cue routing, responsibility handoff, and admissible retreat when a published invitation must be reopened; use **A.16.0** only when lineage, branch, loss, or handoff history itself must be published as an explicit trajectory account; **B.5.2.0** when the admissible continuation is still an open probe question rather than an invitation; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for articulation, closure, anchoring, and representation-factor facets referenced but not governed here; **A.10/B.3** for evidence and assurance; **B.4/B.5** for anomaly-driven cycles; **E.17/E.18** for viewpoint publication; **F.9.1** for bridge-stance annotations; **C.3.3** for kind-bridge repair when endpoint kind mismatches appear.

**Non-goal.**
This pattern does **not** assert that physical affordances, interface affordances, social affordances, epistemic probe moves, articulation-closure moves, latent policy cues, and control opportunities are one concept.

Its job is to publish a disciplined **bridge reading** across those traditions while preventing false identity by shared language.

It also does **not** assert that every trigger use of action-first language is admissibly repaired by `actionInvitation(...)`:

* where the repaired statement is primarily **evaluative**, use **A.6.Q**;
* where it is primarily about **general capability**, use functional / method description;
* where it is primarily **deontic**, apply **A.6.B**;
* where it is primarily about **scheduled or executed enactment**, dock to **A.15** (`U.Method` / `U.MethodDescription` / `U.WorkPlan`, or actual `U.Work` once execution has occurred) rather than letting `actionInvitation(...)` become a shadow execution model.

