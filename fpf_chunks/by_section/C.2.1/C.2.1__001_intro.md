---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__001_intro.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:intro — Intro"
line_start: 43278
line_end: 43301
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

## C.2.1 - `U.Episteme`: Constitution, Empirical Grounding, and Edition Relations

> **Type:** Pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly marked informative

**Plain name.** Episteme constitution.

**Use this pattern when.** You need to identify or compare a body of knowledge: what it claims, the exact entity those claims concern, and the rules under which they are interpreted. A pump specification with a changed pressure threshold carries different claims. Publishing the same claims about the same pump under the same interpretation in another file preserves the episteme.

**First useful move.** Ask: what is claimed; what exact entity are the claims about; and what designation and interpretation rules make those claims readable about that entity? Include measurement, comparison or evaluation rules where the claims use them. If identity is all the task needs, stop after those answers. Otherwise name the concrete receiving use and open only the corresponding branch in :4.0. An unresolved uncertainty or choice is needed only when the use involves a real inquiry or decision.

**One-line summary.** A `U.Episteme` is a knowledge holon identified by exact claim content, one exact EntityOfConcern, and the effective `U.ReferenceScheme` that makes the claims interpretable about that entity. Changing any of these three discriminators identifies another episteme.

**Primary working reader and viewpoint.** The engineer or researcher comparing, revising, teaching, grounding or publishing that knowledge object. The working concern is to reidentify it through those uses and locate a change when it occurs.

**Primary governed object and architecture.** One `U.Episteme` and its `EpistemeConstitutionRelation`, `EpistemeEmpiricalGroundingRelation` and `EpistemeEditionRelation`. The EntityOfConcern of the episteme is the entity its claims concern; for a pump specification, it is the pump, while C.2.1 governs the specification's identity.

**What goes wrong if missed.** A shared filename hides changed claims, subject or interpretation; or a changed display is reported as a changed model. **What this buys.** The practitioner can identify the changed knowledge object or update only the relation affected by a new grounding, view or publication use.

A theory, model, specification, proof or diagnosis can be an episteme when the selected object is that claim-bearing whole. A diagram can carry such claims too. When the task concerns its layout or the calculations available through its notation, use the publication or representation branch in :4.0.

**Not this pattern when.** To inspect or change the pump, perform work, or apply a method, use that subject's direct pattern. Open C.2.1 when the identity of the claims describing it matters. A separately inspected classification assertion has its own claim content, subject and scheme; its governing criterion remains under `A.1` or `C.3.2`, with `E.24.UK` used for public U-kind admission.

