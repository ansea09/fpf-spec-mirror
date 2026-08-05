---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability - System Ability Envelope and Measures"
section_id: "A.2.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__001_intro.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.2 — U.Capability - System Ability Envelope and Measures"
  - "A.2.2:intro — Intro"
line_start: 3291
line_end: 3320
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.3"
  - "E.24.UK"
keywords:
  - "ability envelope"
  - "capability-fit condition"
  - "currentness"
  - "holder-dependent capability instance"
  - "measure set"
  - "qualification window"
---

## A.2.2 - U.Capability - System Ability Envelope and Measures
> **Status:** Stable

`U.Capability` is the FPF object for "can do within bounds".

Use this pattern when a project claim says that a person, team, machine, software service, organization, composite cell, or other system can produce a kind of result, perform a class of work, or meet a performance threshold. The claim is about a holder's capability instance, not about who is assigned, which method is described, which work occurred, or what was promised to another party.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Capability`: an `E.24.UK`-admitted dependent durable U-kind name for holder-dependent capability instances. An individual `U.Capability` instance is a holder-dependent concrete governed object of a named `U.System`, recognized as that system's ability to perform a work family or produce a result class within a declared envelope, measure set, qualification window, and currentness condition. A statement, report row, certification, evidence relation, source-use relation, dashboard display, or currentness assessment about that instance is a neighboring governed record or relation, not the capability instance itself.

**Primary working reader.** A manager, architect, engineer, safety assessor, scheduler, or model author who needs to decide whether a holder can be used for a work claim, method step, service promise, or architecture move without smuggling role assignment, method description, past work, evidence, or quality wording into the capability instance.

**First useful move.** Ask: who is the holder system, what work family or result class is the ability about, under what envelope, with what declared measures, during which qualification window, and which separate statement, evidence relation, source-use relation, or currentness assessment currently supports reliance on that capability?

**What goes wrong if missed.** A role label becomes a hidden proof of ability, a method description is treated as if it can perform work, a phrase such as "the system possesses algorithm A" is taken to admit an unspecified episteme as `U.MethodDescription`, a single successful run is generalized into a stable ability, or a promise is made without a measured capability behind it.

**What this buys.** Capability becomes checkable and reusable: a work-admission claim can test role assignment, role state, method-side admission conditions, and capability thresholds separately.

**Not this pattern when.**

- If the current claim is who holds a work-facing role in a bounded context, use `A.2.1`.
- If the current claim is whether that assignment is in an enactable state, use `A.2.5`.
- If the current claim is a role value, role description, role name, role relation structure, or role bundle, use `A.2`, Part F role patterns, or `A.2.7`.
- If the current claim is a way of doing, use `A.3.1`; if it is an episteme describing that way, use `A.3.2`.
- If the current claim is dated performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is a promise to others, use the promise-content and commitment patterns.
- If the current claim is evidence, source, status, assurance, publication, or description use of an episteme, use the direct episteme-use pattern. Do not make the episteme a capability holder.
- If the current claim is one measured aspect with a declared scale, use `U.Characteristic` through `C.16.P`, `A.19`, and the current characteristic or scale owner.
- If the current claim is a composite quality family such as availability, resilience, security, or maintainability, use `C.25` Q-Bundle.
- If the current claim is an architecture-characteristic starter head, project criteria row, architecture eval reading, or architecture-description concern, use `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, or `C.30` as applicable.

