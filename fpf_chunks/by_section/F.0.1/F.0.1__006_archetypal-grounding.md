---
chunk_kind: "child"
pattern_id: "F.0.1"
pattern_title: "Source-Local Meaning Recovery"
section_id: "F.0.1:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.1/F.0.1__006_archetypal-grounding.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "F.0.1 — Source-Local Meaning Recovery"
  - "F.0.1:5 — Archetypal Grounding"
line_start: 92768
line_end: 92840
dependencies:
  - "E.10"
  - "E.10.D1"
  - "F.0.2"
  - "F.1"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "actual cross-local relation"
  - "exact source and edition"
  - "local expression"
  - "optional durable address"
  - "source-local meaning"
  - "troubling word use"
---

### F.0.1:5 - Archetypal Grounding

#### F.0.1:5.1 - Entry, stop, and continuation

Start with one troublesome use in one already selected source. Return one ordinary sentence plus a source pointer. Stop when it answers the question.

Continue only for the next result actually needed:

- `F.1` for a question-relative source cut;
- `F.17` for a durable local-sense address and, when current, its basis relation;
- `F.9` for an actual relation between distinct recovered cells;
- `F.0.2` for a bounded comparison or synthesis among source ontologies;
- `F.18` for naming after the subject distinction is settled; or
- the rule that defines or tests the exact entity, relation, claim, measurement, permission, or Work question itself, with its pattern ID as locator.

#### F.0.1:5.2 - Compact worked results and recognition cues

A **worked result** below names the exact source, edition, passage, and meaning used. A **recognition cue** only marks a likely false friend; it establishes no local meaning until the practitioner supplies those four values. This distinction keeps a broad set of examples useful without dressing an unresolved pointer as source-backed knowledge.

##### F.0.1:5.2.1 - *process* and *activity*

- **Worked result — OMG BPMN 2.0.2 (January 2014), §10.1, Processes.** *Process* denotes the designed sequence or flow of Activities in an organization.
- **Worked result — W3C PROV-O Recommendation (30 April 2013), §3.1, Starting Point Terms.** *Activity* denotes something that occurs over a period of time and acts upon or with entities, including using or generating them.

The first question may need only one of these readings. If a later use relates the designed structure to performed occurrences, recover two F.17 cells and state the exact F.9 relation, including concurrency or trace information that does not carry across. Do not call the two meanings identical.

##### F.0.1:5.2.2 - *actuation* and *control output*

- **Recognition cue — control theory.** If *actuation* may mean a signal applied to plant actuators, select one exact control-theory publication, edition, and passage before using that reading.
- **Recognition cue — IEC 61131-3.** If *control output* may mean a program-produced value sent to field I/O, identify the exact edition and clause before using that reading.

These cues establish no relation. After both readings become worked results, F.9 may test whether the PLC output can be read as the controller's actuation signal for one stated operating regime while keeping hardware and scan-cycle limits visible.

##### F.0.1:5.2.3 - *observation* and *service metric*

- **Worked result — W3C SOSA/SSN Recommendation (19 October 2017), §4.3.2.2, `sosa:Observation`.** *Observation* denotes the act of carrying out a procedure to estimate or calculate a value of a property of a feature of interest.
- **Recognition cue — ITIL 4.** If *service-level metric* is used for a quantity that evaluates a service-level objective, identify the exact ITIL 4 publication, edition, and passage before using that reading.

The verified SOSA reading alone establishes no service-metric relation. Once the second reading is source-backed, a named use may ask whether the observation supplies evidence for that metric; that is a subject relation, not lexical identity or same-row membership.

##### F.0.1:5.2.4 - *subclass-of* and *is-a*

- **Worked result — W3C OWL 2 Structural Specification and Functional-Style Syntax, Second Edition (11 December 2012), §9.1.1, Subclass Axioms.** `SubClassOf(CE1 CE2)` states that the first class expression is a subclass of the second.
- **Recognition cue — engineering glossary.** If *is-a* is being used as a less formal kind-of relation, identify the exact glossary, edition, and entry before relying on that reading.

Keep the verified formal reading and the unresolved cue separate. Relate them only when the receiving artifact needs the formal relation and an exact second passage supports the correspondence.

##### F.0.1:5.2.5 - *permission* and RBAC *role*

- **Worked result — W3C ODRL Information Model 2.2 Recommendation (15 February 2018), §2.6.1, Permission Class.** A Permission allows an action on an Asset when its refinements and constraints are satisfied and its duties are fulfilled.
- **Recognition cue — NIST RBAC.** If *role* is being used for an access-control grouping through which permissions are assigned, identify the exact NIST publication, edition, and passage before using that reading.

The verified permission reading is not the unresolved role reading. A later access-control use may relate two source-backed meanings, but familiar wording alone establishes neither the relation nor interchangeability.

#### F.0.1:5.3 - Quick checks for later use

- **String check.** If the only evidence is the same spelling, no cross-source relation has been established.
- **Stance check.** If one source describes a design and another a performed occurrence, state that difference before any relation or row use.
- **Direction check.** Preserve the direction and limits of the actual relation; a reverse or broader reading needs its own support.
- **Chain check.** Keep intermediate meanings and accumulated loss visible; test a direct endpoint relation separately when needed.
- **Contradiction check.** Incompatible relation claims about the same cells remain explicit rather than being averaged into a vague alignment.
- **Row check.** A Concept-Set row needs the relation and bounded receiving-use judgment required by F.7 and F.9; a label or confidence level cannot admit a member.

#### F.0.1:5.4 - Quick reference

- **Ordinary result:** one source-backed plain meaning statement.
- **Durable local meaning:** an optional F.17 `SchemeSenseCell`.
- **Current support:** an optional obtaining `LocalSenseBasisRelation`.
- **Different local meanings:** separate cells; use F.9 only for an actual relation.
- **Source selection:** F.1; **synthesis:** F.0.2; **naming:** F.18; **subject reasoning:** the defining or testing rule for the recovered claim.

> **Mental checklist:** Name the source and edition → locate the passage → say what the expression means → stop if sufficient → add only the durable address or relation a named receiver needs.

