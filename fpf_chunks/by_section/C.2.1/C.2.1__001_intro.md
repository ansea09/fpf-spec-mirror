---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__001_intro.md"
commit_sha: "5018da7d3b2b6a6e722fb76defe5cf991a64ba14"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:intro — Intro"
line_start: 50982
line_end: 51005
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

**Use this pattern when.** You are developing, using or changing an account and need to recover what it says, how its claims can guide work, or what a change affects. Use the common method in :4.0, then the identity, grounding or edition branch needed for the question. A pump specification with a changed pressure threshold carries different claims. Publishing the same claims about the same pump under the same interpretation in another file preserves the episteme.

**First useful move.** Establish what the account must help its recipient understand or do. Recover the relevant claims, their subject and interpretation; write or draw what is understood when the account is still developing. A corrected sentence, an interpretable table or a justified answer about a changed dependency can finish the task. Section :4.0 connects these moves; :4.1.1 gives the exact identity comparison when needed.

**One-line summary.** A `U.Episteme` is a claim-bearing holon identified by exact claim content, one exact EntityOfConcern, and the effective `ReferenceScheme` that makes the claims interpretable about that entity. Changing any of these three discriminators identifies another episteme.

**Primary working reader and viewpoint.** The engineer or researcher comparing, revising, teaching, grounding or publishing that knowledge object. The working concern is to reidentify it through those uses and locate a change when it occurs.

**Primary governed object and architecture.** One `U.Episteme` and its `EpistemeConstitutionRelation`, `EpistemeEmpiricalGroundingRelation` and `EpistemeEditionRelation`. The EntityOfConcern of the episteme is the entity its claims concern; for a pump specification, it is the pump, while C.2.1 governs the specification's identity.

**What goes wrong if missed.** The reader confuses a whole account with selected claims, its subject or its expression; a shared filename can also hide changed claims or interpretation. **What this buys.** The practitioner can recover the needed meaning and grounds, locate a consequential change and repair the dependent account, expression or use.

A theory, model, specification, proof or diagnosis can be an episteme when the selected object is that claim-bearing whole. A diagram can carry such claims too. When the task concerns its layout or the calculations available through its notation, use the publication or representation branch in :4.0.

**Not this pattern when.** Use the subject's direct method to inspect or change the pump, perform work or apply a calculation when its account and grounds already suffice. Open C.2.1 when interpretation, episteme identity, grounding or a change in the account leaves the receiving use unclear. A separately inspected classification assertion has its own claim content, subject and scheme; its criterion remains under `A.1` or `C.3.2`, with `E.24.UK` used for public U-kind admission.

