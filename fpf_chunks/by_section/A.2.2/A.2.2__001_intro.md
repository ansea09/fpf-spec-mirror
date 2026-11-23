---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "System Capability: Conditions, Measures and Fit"
section_id: "A.2.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__001_intro.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "A.2.2 — System Capability: Conditions, Measures and Fit"
  - "A.2.2:intro — Intro"
line_start: 5434
line_end: 5463
dependencies:
  - "A.1"
  - "A.15"
  - "A.2.3"
  - "A.2.6"
  - "C.2.1"
  - "C.32.MWA.PP"
  - "E.23.CDI"
keywords:
  - "Method-relative capability"
  - "attained bounds"
  - "capability fit"
  - "currentness"
  - "holder ability"
  - "qualification"
  - "support"
  - "usable Method structure"
  - "work conditions"
---

## A.2.2 - System Capability: Conditions, Measures and Fit
> **Status:** Stable

Capability is a System's ability to perform a work family or produce a result class under stated conditions, to a stated criterion of performance. Give attained bounds when the criterion calls for a measure.

**Use this when** planning, promising or admitting work requires a justified answer to “can this holder do what is needed here?” The holder may be a person, team, machine, deployed software System, organization or composite cell. Identify that System independently under A.1, then state its qualified ability. The claim needs no separate capability individual.

**Primary EntityOfConcern.** The holder System whose ability is being asserted. A capability statement that needs an identified account is an episteme under C.2.1; its subject is the holder, and its claims state what that holder can do. Actual ability, the assertion, its support, current qualification and fit to a receiving demand remain distinguishable.

**Working reader.** A practitioner deciding whether a holder can meet a Work, Method-step, service-promise or architecture need.

**First useful move.** What must the recipient obtain, and which part must this particular holder decide or perform? Identify the holder, its conditions of work and the evidence that it can meet the criterion with the help allowed. An existing assessment can settle that question. To assign several contributions, establish how they can be supplied together alongside work already promised. Section 2.1 distinguishes what the holder can do with help from what the helper supplies.

**What goes wrong if missed.** A practitioner may infer ability from an assignment, a MethodDescription, one successful run or a promise. An expired report can change reliance on the assessment while the holder retains its ability. Individually capable holders can depend on the same help at the same time.

**What this buys.** Planning can separate ability from its warrant and fit: change the demand without inventing a new capability, or reopen an actual ability claim when the holder's configuration changes. Independently required authority, assignment state, Method-side conditions and assurance remain separate receiving checks.

**Not this pattern when.**

- If the current claim is which admitted System is assigned to an exact local system-role kind, use `A.2.1`.
- If the current claim is whether that assignment is in an enactable state, use `A.2.5`.
- If the current claim is a local system-role kind, its classification, description, designation, exact assignment, relation structure, or bundle, use `A.2`, `A.2.1`, `F.4`, `F.18`, or `A.2.7` for that object.
- If the current claim is a way of doing, use `A.3.1`; if it is an episteme describing that way, use `A.3.2`.
- If the current claim is dated performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is a promise to others, use the promise-content and commitment patterns.
- If the current claim is evidence, source, status, assurance, publication, or description use of an episteme, use the direct episteme-use pattern. Do not make the episteme a capability holder.
- If the current claim is one measured aspect with a declared scale, use `U.Characteristic` through `C.16.P`, `A.19`, and the applicable characteristic or Scale pattern.
- If the current claim is a composite quality family such as availability, resilience, security, or maintainability, use `C.25` Q-Bundle.
- If the current claim is an architecture-characteristic starter head, project criteria row, architecture eval reading, or architecture-description concern, use `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, or `C.30` as applicable.

