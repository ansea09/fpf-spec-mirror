---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__001_intro.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:intro — Intro"
line_start: 4121
line_end: 4150
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "E.23.CDI"
keywords:
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "work conditions"
---

## A.2.2 - System Capability: Conditions, Measures and Fit
> **Status:** Stable

Capability is a System's ability to perform a work family or produce a result class under stated conditions and measured bounds.

**Use this when** planning, promising or admitting work requires a justified answer to “can this holder do what is needed here?” The holder may be a person, team, machine, deployed software System, organization or composite cell. Identify that System independently under A.1, then state its qualified ability. The claim needs no separate capability individual.

**Primary EntityOfConcern.** The holder System whose ability is being asserted. A capability statement that needs an identified account is an episteme under C.2.1; its subject is the holder, and its claims state what that holder can do. Actual ability, the assertion, its support, current qualification and fit to a receiving demand remain distinguishable.

**Primary working reader.** A manager, architect, engineer, safety assessor, scheduler or model author deciding whether a holder can meet a Work, Method-step, service-promise or architecture need.

**First useful move.** Name the holder, work or result, conditions and attained bounds. Then compare the receiving demand with that qualified claim, using the support and currentness required for this use. An adequate existing claim and fit result may be reused without another record.

**What goes wrong if missed.** Assignment, a MethodDescription, one successful run or a promise is mistaken for measured ability. Conversely, an expired report is treated as if it physically removed the holder's ability. Both errors conceal which fact needs attention.

**What this buys.** Planning can separate ability from its warrant and fit: change the demand without inventing a new capability, or reopen an actual ability claim when the holder's configuration changes. Independently required authority, assignment state, Method-side conditions and assurance remain separate receiving checks.

**Not this pattern when.**

- If the current claim is which admitted System is assigned to an exact local system-role kind, use `A.2.1`.
- If the current claim is whether that assignment is in an enactable state, use `A.2.5`.
- If the current claim is a local system-role kind, its classification, description, designation, exact assignment, relation structure, or bundle, use `A.2`, `A.2.1`, `F.4`, `F.18`, or `A.2.7` for that exact object.
- If the current claim is a way of doing, use `A.3.1`; if it is an episteme describing that way, use `A.3.2`.
- If the current claim is dated performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is a promise to others, use the promise-content and commitment patterns.
- If the current claim is evidence, source, status, assurance, publication, or description use of an episteme, use the direct episteme-use pattern. Do not make the episteme a capability holder.
- If the current claim is one measured aspect with a declared scale, use `U.Characteristic` through `C.16.P`, `A.19`, and the applicable characteristic or Scale pattern.
- If the current claim is a composite quality family such as availability, resilience, security, or maintainability, use `C.25` Q-Bundle.
- If the current claim is an architecture-characteristic starter head, project criteria row, architecture eval reading, or architecture-description concern, use `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, or `C.30` as applicable.

