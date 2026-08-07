---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__002_use-this-when.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:0 — Use This When"
line_start: 4418
line_end: 4443
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:0 - Use This When

**Plain name.** Role-state relation.

Use this pattern when an admitted system already holds a `U.Role`, but a method step, work occurrence, incompatibility check, or operational gate depends on the assignment being in a particular state during a particular window.

The first useful question is not "What status word is displayed?" It is: **Which current `U.RoleAssignment` satisfies which exact state predicate, during which window, and what evidence-use relation supports the assertion on which the next work decision relies?**

Typical working moments include these:

- a calibrated inspection robot is assigned `InspectorRole`, but inspection work should start only while calibration, synchronization, and operating-envelope predicates hold;
- an incident commander is on call, yet a conflict or fatigue predicate may make the assignment non-admitting for a particular response window;
- a method description declares a role-state predicate for its admission rule, while the current assignment and evidence have not yet been connected to that predicate;
- two role assignments are incompatible only while both satisfy the predicates that make them work-admitting;
- a DDD-style model-use organization changes the meaning of an otherwise identical state predicate.

**Primary EntityOfConcern.** The EntityOfConcern is one obtaining `RoleStateRelation`, a direct relation kind admitted under `U.Relation`. Its two participants are one current `U.RoleAssignment` occurrence and one by-value `RoleStatePredicate`; the occurrence's maximal continuous temporal extent is derived from uninterrupted predicate truth while the assignment obtains.

**Primary working reader.** The first reader is an engineer, operator, method designer, safety checker, or manager deciding whether a current assignment can support the next method or work claim without confusing assignment, capability, state, evidence, gate outcome, and performed work.

**What goes wrong if missed.** A role label is treated as current readiness. A dashboard value is substituted for the world-side role-state relation. Missing evidence is read as proof that the predicate is false. Capability is mistaken for work admission. A state-machine diagram silently becomes both the ontology and the method order.

**What this buys.** The reader can identify repeated role-state episodes, keep evidence and world-side obtaining distinct, combine several simultaneous predicates, and pass the exact state claim to the direct pattern governing the next decision or work use.

**Not this pattern when.** Use `A.2` for the role value, `A.2.1` for who holds it and when, `A.2.2` for capability and operating envelope, `A.2.7` for role substitution, incompatibility, and bundle relation structures, and `A.15.1` for work that actually occurred. Use `A.2.4` or `A.10` when the current object is the evidence-use relation rather than the role-state relation.

