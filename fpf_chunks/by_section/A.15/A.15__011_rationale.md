---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__011_rationale.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:10 — Rationale"
line_start: 24240
line_end: 24249
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "appearance-based reliance boundary"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:10 - Rationale

This pattern solves a problem that has plagued systems modeling for decades: the conflation of what a system *is* with what it *does*. Its rigor is not arbitrary but is grounded in several key intellectual traditions.

*   **Ontology Engineering:** The pattern is a direct application of best practices from foundational ontologies (like UFO), which have long insisted on the distinction between *endurants* (objects like a `U.System`) and *perdurants* (events and Work individuals admitted under `U.Work`), and between intrinsic properties and relational roles. FPF makes these powerful distinctions accessible to practicing engineers.
*   **Process-theory source tradition:** Formalisms like the Pi-calculus or Petri Nets model dynamic interactions under terms often translated as processes. A.15 does not import `process` as a new FPF object; it maps the useful local use to `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work` as the admitted kind, one actual dated Work occurrence, or a separate episteme about it. FPF adds the exact holder and four-participant role assignment, holder `U.Capability` instance when capability reliance is current, any separate capability statement or currentness assessment used for that reliance, any separate capability-fit condition over that capability instance when work admission is current, enacted `U.Method`, and separate `U.MethodDescription` that make the occurrence inspectable.
*   **Pragmatism and Practice:** The framework is deeply pragmatic. The distinctions it makes between a `MethodDescription`, a capability instance, and a Work individual admitted under `U.Work` are precisely the ones that matter in project management, compliance, and debugging. When a failure occurs, a manager needs to know whether the recipe was wrong, the holder lacked the required capability, or this particular Work occurrence departed from the method. This framework provides the vocabulary to ask and answer that question precisely.

By creating this clean, stratified alignment for enactment, FPF provides a stable and scalable foundation for downstream resource accounting, decision, constraint, gate, evidence, assurance, ethics, and transformation patterns without letting any one of those neighboring claims collapse into A.15.

