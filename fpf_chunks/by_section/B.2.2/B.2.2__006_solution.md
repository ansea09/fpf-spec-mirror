---
chunk_kind: "child"
pattern_id: "B.2.2"
pattern_title: "Meta-System Transition - System Specialization of MHT"
section_id: "B.2.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.2/B.2.2__006_solution.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "B.2.2 — Meta-System Transition - System Specialization of MHT"
  - "B.2.2:4 — Solution"
line_start: 38453
line_end: 38526
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.1"
  - "A.2.2"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "B.1.2"
  - "B.2"
  - "B.2.4"
  - "B.2.5"
  - "B.3"
  - "B.3.5"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.30"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "E.24.UK"
keywords:
---

### B.2.2:4 - Solution

After B.2 leaves a whole-reidentification question open, continue with the same exact candidate new whole and direct facts. Add no system-specific result species or context-shaped slice.

#### B.2.2:4.1 - Reuse The B.2 Candidate And Complete System Recognition

Keep B.2's one `resultHolonRef` for the exact candidate new whole and its one `resultHolonKindRef`, which here resolves to the already admitted `U.System` kind. The references may appear in B.2's optional `HolonReidentificationRecord` when a receiving use needs a durable account; B.2.2 adds no second record.

Before calling the candidate a system result:

1. execute the complete A.1 criterion over the candidate's exact constituents, obtaining constructive relations, governed assembly, reidentification rule, and composition-grounded whole characteristic;
2. show that its actual boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy at least one applicable governed larger-assembly construction method or rule under which it can remain a constituent;
3. apply the direct `U.System` criterion to that same individual: its actual physical or operational organization must make it eligible to act causally in work or transformation while preserving its identity;
4. recover only the additional system facts used by the concrete case—including any delimitation, objective, commitments, coordination, capability, system-role kind or assignment, method, work, transformation, functioning, architecture, evidence, assurance, or temporal claim—and state each through the pattern that defines its object or relation; and
5. keep the classification judgment, evidence or assurance, currentness, and receiving reliance separate from those world-side facts.

If a required A.1 component or the acting-eligibility criterion fails, do not identify the candidate as the system result. If an additional system fact needed for another claim is absent, withhold that claim rather than treating its absence as failure of the `U.System` criterion. If missing evidence or an unavailable dependency prevents a determination, report `unknown`; neither a filled reference nor an optional record changes that result.

#### B.2.2:4.2 - Carry Result-System Claims Through Subject Patterns

When the candidate is recognized as `U.System`, state every changed result-system fact or claim under its subject pattern:

- system-role assignments through `A.2.1`, relations among system-role kinds through `A.2.7`, and other relations through the patterns that define them;
- capabilities through `A.2.2` and `C.16`;
- methods and mechanisms through `A.15`, `A.6.1`, and any other applicable method or mechanism pattern;
- transformations through `A.3.4`;
- work occurrences through `A.15.1`;
- functioning and functional structure through `A.6.F` and `C.30.TFS-REL`;
- architecture through `C.30`, `A.22`, and `C.30.ASV`;
- evidence and assurance through `A.10`, `B.3`, and `B.3.5`;
- temporal and dynamics claims through `C.27`, `A.19`, and the direct temporal patterns.

Do not reuse old component evidence as if it automatically covered the proposed new whole after recognition under `U.System`. Carry an unchanged component claim only through its exact continuing relation; establish each changed result-system fact under its subject pattern and support the associated claim through a separate evidence or assurance relation.

#### B.2.2:4.3 - System Trigger Interpretation

When a receiving use has materialized B.2's optional `MHTTriggerProfile`, read its cues for a system case as follows:

| Cue recorded in `MHTTriggerProfile` | System-case reading | Subject pattern kept visible |
| --- | --- | --- |
| Delimitation change | The operating whole now has an external delimitation and crossing relations that differ from the old aggregate. | `A.1`, `B.1.2`, `A.14`, `C.13` |
| Objective or evaluation change | The whole is now evaluated by a system-level objective, mission, SLO, safety case, or viability claim. | `C.16`, `E.13`, `A.10`, decision or assurance patterns |
| Supervision or coordination change | A controller, protocol, governance relation, or distributed coordination relation regulates constituent behavior for the result whole. | `B.2.5`, `A.12`, `A.3.4`, `A.15.1` |
| Capability or closure claim | Recover the exact capability envelope and closure relations of the proposed new whole after recognition under `U.System`; keep supporting evidence separate. | `A.2.2`, `C.16`, `A.10` for evidence use, and `B.2.4` when whole reidentification is current |
| Agency threshold | The result whole crosses a concern-specific agency threshold in characteristic space. | `A.13`, `A.19`, `C.16` |
| Temporal consolidation | A commissioning, phase, release, or operating-time consolidation changes the current system identity claim. | `C.27`, `A.15.1`, temporal patterns |
| Context reframe | The relevant bounded context changes the operating whole under concern. | `A.1`, bounded-context patterns, architecture patterns |

No cue is enough by itself. Each row points to facts and claims to inspect; B.2's direct existing-whole/new-whole comparison, complete A.1 recognition, and the system-kind criterion decide the result.

#### B.2.2:4.4 - Delimitation and External Acting Systems

For system-result MHT, distinguish:

- a part of the result system;
- an external acting system that changes the result system or a constituent;
- an environment or resource that participates in work;
- a description, dashboard, twin, model, diagram, or publication about the result system.

A lathe making a workpiece, a controller steering a plant, or a teacher changing a learner does not thereby become a part of the changed holon or the larger whole containing it. Use `A.12`, `A.3.4`, and `A.15.1` for acting side, transformation, and work. Use part-whole patterns only when parthood itself is admitted.

#### B.2.2:4.5 - Assurance Re-Basing

When the exact candidate new whole is recognized as `U.System`, test old assurance against that system rather than transferring it by name.

Ask:

- Which component evidence still applies unchanged?
- Which evidence applies only through explicit correspondence or source-use relation?
- Which assurance claims must be rewritten for the result system?
- Which architecture, capability, functioning, work, temporal, or evidence claims now have different subject patterns?

A claim about the recognized result system may reuse component evidence only through an exact correspondence or source-use relation and a fresh evaluation of applicability. That system does not inherit safety, reliability, responsibility, or performance claims by label.

