---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "SystemRoleKindRelationStructure - Relations among System-Role Kinds"
section_id: "A.2.7:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__002_use-this-when.md"
commit_sha: "d9170ae93b035896511bce82dfb5d9082a50b8a2"
heading_path:
  - "A.2.7 — SystemRoleKindRelationStructure - Relations among System-Role Kinds"
  - "A.2.7:0 — Use This When"
line_start: 5895
line_end: 5926
dependencies:
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.22"
  - "A.6.REL"
  - "C.3"
  - "C.3.1"
  - "E.10.ROLE"
keywords:
  - "U.SubkindOf"
  - "incompatibility"
  - "joint assignment requirement"
  - "relations among system-role kinds"
  - "selected structure"
  - "substitution"
---

### A.2.7:0 - Use This When

**Plain designation.** Say “structure of relations among system-role kinds” for `SystemRoleKindRelationStructure`.

Use this pattern when several exact context-local system-role kinds are already admitted, and a later admission, allocation, or interpretation check needs one of these results:

- an assignment to one system-role kind may satisfy a condition written for another kind;
- two system-role kinds are incompatible under one exact holder, Work, and time rule;
- several independently obtaining assignments are required together under one allocation rule; or
- one system-role kind narrows another, and the practitioner must decide whether that narrowing is monotonic `U.SubkindOf` or a different residual relation.

Typical working moments include these:

- a pressure-test MethodDescription names `HydraulicsTechnicianSystemRole`, while the proposed holder is assigned to `SeniorHydraulicsTechnicianSystemRole`;
- the same system must not hold author and approver assignments for the same hazard-analysis Work during overlapping windows;
- a surgical procedure needs surgeon, anesthetist, and scrub-practitioner assignments together, with three distinct holders;
- `RoboticsEngineerSystemRole` may be a subkind of `EngineerSystemRole`, but neither a nested label nor one assignment can establish that order.

**First useful result.** Write the readable direct relation or `U.SubkindOf` claim needed by the receiving use. Recover its exact predicate. Stop there unless another claim needs one relation occurrence as an identifiable object or needs several obtaining relations selected into one structure.

**Primary EntityOfConcern.** For one direct question, the EntityOfConcern is the exact relation occurrence or exact `C.3.1 U.SubkindOf` occurrence. When several such occurrences must be selected together, it is one `SystemRoleKindRelationStructure`: a dependent `U.Structure` whose substrate is an exact finite set of local system-role kinds and whose selected organization consists only of exact obtaining relations among those kinds.

The structure contains neither holder systems nor system-role-assignment occurrences. A graph, taxonomy table, policy file, or organization chart may describe it but does not become the structure or any selected relation by form.

**Primary working reader.** The first reader is an engineer, Method designer, safety practitioner, clinical team designer, or manager deciding which relations a later check may rely on. The reader should be able to recover the exact system-role kinds, relation rule, applicability, occurrence identity, and assignment inputs without treating a name hierarchy or policy row as the relation itself.

**What goes wrong if missed.** A job-title order is used as admission authority. An independence rule omits the holder, Work, or overlap condition. A bundle name hides whether one or several systems must hold the assignments. A semantic restriction is called `U.SubkindOf` although a known broader classification can be false. A scheme or taxonomy edition is then inserted as a participant of every relation even when it changes no meaning.

**What this buys.** Admission substitution, incompatibility, joint allocation, monotonic kind order, and residual qualification remain different claims with different truth and identity laws. Actual holders remain systems, actual assignments remain direct species of `U.SystemRoleAssignment`, and the system performing a receiving check remains visible.

**Not this pattern when.** Use `A.2` and `C.3` to admit and classify exact local system-role kinds. Use `A.2.1` for assignments and their holders, `A.2.5` for `SystemRoleAssignmentStatePredicate` and `SystemRoleAssignmentStateRelation`, `A.2.2` for capability, A.3 patterns for Methods, and A.15 patterns for planned or performed Work. Use `F.9` and `A.6.9` for an actual cross-scheme Bridge, then a separate bounded-use assertion and reliance decision. Use `C.29` when a graph, matrix, algebra, embedding, or table is the object under evaluation.

