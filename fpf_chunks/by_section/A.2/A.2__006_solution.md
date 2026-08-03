---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__006_solution.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:4 — Solution"
line_start: 2747
line_end: 2833
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "E.24"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:4 - Solution

Use `U.Role` for an enactment-facing role value interpreted through one role-taxonomy episteme and effective reference scheme. Ask: **which role value, under which role vocabulary and interpretation scheme, is assigned to this admitted system during the current window?**

Then keep three moves distinct. Interpret the role value. State `U.RoleAssignment` when holder or window identity matters. Add only the direct role-state, capability, method-admission, work, transformation, responsibility, evidence, or reliance relations needed by the current claim.

A selected `BoundedModelUseStructure` can qualify one receiving interpretation. Designate it in the receiving assertion or work use only when an independently established DDD-style organization changes that interpretation; it is not an optional participant of a generic role relation and does not assign, hold, or enact the role.

#### A.2:4.1 - Core Definitions

**`U.Role`.** A `U.Role` is an enactment-facing role value. Its meaning is recovered from a named role-taxonomy episteme under an effective `U.ReferenceScheme`; the value names what an admitted `U.System` holder is being when assignment, method admission, transformation or functioning participation, work attribution, or role-state checking is current. A role value is not the holder, assignment relation, taxonomy episteme, reference scheme, or selected model-use structure.

Plain gloss: a role says what one system is being in a particular participation without turning that participation into a new system kind. The role vocabulary and scheme make that statement interpretable; the assignment says who holds it and when.

**`U.RoleAssignment`.** A `U.RoleAssignment` is an assignment relation governed by `A.2.1`. Its four participants are an admitted `U.System` holder, one `U.Role` value, the role-taxonomy episteme that states its local vocabulary, and the effective reference scheme. Its actual assignment extent is the maximal continuous period during which the assignment predicate obtains; an assertion or occurrence description may state the currently known extent separately. A.2 explains the distinction; A.2.1 governs the complete SlotSpecs and relation-occurrence identity.

**Role holder.** A holder of `U.RoleAssignment` is an admitted `U.System`. A current method-admission, work, transformation, or functioning relation cites that assignment when system participation matters. Motors, pumps, organisms, teams, services, and people can therefore be holders without implying consciousness, social agency, legal responsibility, or ethical responsibility. An episteme remains a participant in the direct relation through which a system uses it to describe, constrain, evidence, or inform work.

**Role description.** A role description is a `U.Episteme` whose EntityOfConcern is a role value, role assignment, or selected role relation. It may contain claims about role admission, use, or interpretation. Systems may teach from it or store it, and a publication relation may expose it; those uses do not make the description the role value.

**No role mereology.** `U.Role` is not an admitted holon kind. If a proposed role decomposition matters, identify what the proposed element actually is. A narrower role value, a substitution or incompatibility relation, a role-state predicate, a holder-eligibility or capability-fit condition, a responsibility or commitment relation, and a method or work structure are governed separately. Rich slots in an assignment or a role description do not make those values parts of the role.

**Relations around a role value.** These direct relations make a role usable without becoming slots or parts of `U.Role`:

| Current claim | Governing pattern | Kept distinct |
| --- | --- | --- |
| Role interpretation and description | `A.2`, `C.2.1`, `F.4`, `F.5` | Role value, role-taxonomy episteme, effective reference scheme, and description episteme. |
| Role assignment | `A.2.1`, `A.6.5` | Four participants: holder system, role value, taxonomy episteme, and scheme; the separately described assignment extent. |
| Role state | `A.2.5` | The exact `U.RoleAssignment` occurrence and by-value `RoleStatePredicate` from A.2.5's two-participant relation; its maximal continuous joint-truth extent is derived from obtaining history. Target evaluation window, assertion polarity, evidence, and reliance remain separate. |
| Holder capability | `A.2.2` | Capability instance, envelope, measures, currentness, and fit predicate. |
| Method admission | `A.15`, `A.3.1`, `A.3.2` | Method, method description, and role-admission condition. |
| Work or transformation participation | `A.15`, `A.15.1`, `A.3.4` | Holder assignment, dated work occurrence, transformation relation, and their separately governed results. |
| Evidence or reliance concerning a role claim | `A.10`, `A.15.4`, `C.2.1`, `F.10` | Episteme, evidenced claim, reliance relation, provenance, and currentness. |

Select only the rows needed by the current claim. A long relation neighborhood is not a larger role.

#### A.2:4.2 - Role Assignment Boundary

Begin with a readable sentence: an admitted system holds a named role, interpreted through a named role taxonomy and reference scheme, during a stated assignment interval.

`A.2.1` directly governs `U.RoleAssignment`. It alone owns the relation's `RelationSignature`, four participant `SlotSpec` declarations, obtaining condition, and occurrence-identity rule. The relation connects the admitted holder system, enactment-facing role value, role-taxonomy episteme, and effective reference scheme; its actual assignment extent follows uninterrupted obtaining. Any selected model-use structure belongs to the receiving assertion or use, not this signature.

The role-taxonomy episteme and effective reference scheme make local interpretation explicit without introducing a universal context object. The optional model-use structure neither holds nor assigns the role. Assignment authority, role state, capability, method admission, performed work, responsibility, evidence, reliance, and publication remain separate claims under their direct governing patterns.

When another claim relies on assignment identity, cite the exact `U.RoleAssignment` occurrence declared under `A.2.1`; do not recreate its signature in this taxonomy pattern.

#### A.2:4.3 - Recover the Direct Relation behind Contribution Wording

In ordinary language, `the role of X` often means that X contributes to some use. First ask whether X is an admitted `U.System` being something in work, transformation, functioning, or method participation. If yes, recover `U.Role` and, when relied on, `U.RoleAssignment`. If no, keep X in its actual kind and name the direct relation that makes its contribution matter.

| Ordinary wording | Governed repair |
| --- | --- |
| `RFC 9110 plays a normative role in this design` | Keep the RFC publication as an episteme and state the current external-rule, constraint, source-use, or publication relation selected by the design claim. The engineering system holding the design role remains separate. |
| `this dataset plays the benchmark role` | Keep the dataset as an episteme and state the current evidence, measurement, benchmark, source-use, or currentness relation. |
| `this parameter has the control role` | Recover the method or model parameter, or an `A.6.5` relation SlotSpec, according to the direct declaration. |
| `this interface plays the integration role` | Recover the selected module-interface, port, signature, or protocol relation under its governing architecture or interface pattern. |

The alternatives in a row are triage questions, not a union kind. Select the one relation that the relied-on claim actually uses. If that relation is still unclear, apply `A.6.RSIR` and stop before minting a role value.

#### A.2:4.4 - Role Taxonomy Episteme and Role Relation Structure

A role-taxonomy episteme contains the role vocabulary and selected role-relation claims interpreted under one effective `U.ReferenceScheme`. The episteme does not assign a role. A `U.RoleAssignment` relates the holder system to one role value and declares participant SlotSpecs for the taxonomy episteme and scheme needed to interpret that value.

`A.2.7` governs a selected role relation structure made from exact substitution, incompatibility, qualification, and role-bundle relation occurrences. A receiving check may use an assertion about one of those occurrences alongside separately governed `U.RoleAssignment`, `RoleStateRelation`, or capability-fit claims. Those neighboring relations remain direct-owner objects; they are not A.2.7 relation participants, role parts, or system-kind subsumption.

Algebraic, graph, matrix, embedding, or neural representations are mathematical lenses over that selected role relation structure when a project declares such a lens use. A `BoundedModelUseStructure` remains a separate `U.Structure`; when it changes one receiving interpretation, the receiving assertion or use designates it without extending generic role-relation signatures.

| Role value | Recognition case | Boundary |
| --- | --- | --- |
| `CoolingCirculatorRole` | A pump circulates coolant under a plant-operations role taxonomy. | The pump is the holder; circulation capability and performed work remain separate claims. |
| `TestArticleRole` | The same pump participates in qualification work under a test role taxonomy. | The test assignment does not change pump identity. |
| `VerifierRole` | A person, team, or service performs verification work under a named assignment. | The verification report is an episteme, not the role holder. |
| `TransformerRole` | A system changes an EntityOfConcern through work under a method or transformation relation. | The holder performs work; the role value does not act. |

#### A.2:4.5 - Reduced Use and Stronger Claims

A role-like word may remain Plain when it only helps people recognize a local conversation and no decision, attribution, admission, or reliance depends on its identity. Do not materialize `U.Role` or `U.RoleAssignment` merely to improve wording.

When a stronger claim appears:

- name the role-taxonomy episteme and effective reference scheme when role meaning matters;
- add `U.RoleAssignment` when holder or assignment-window identity matters;
- add the direct role-state, capability-fit, method-admission, work, transformation, evidence, or reliance relation when that relation carries the claim;
- use `A.2.7` for selected role relations inside one interpretation; when a proposed comparison, substitution, translation, or reuse crosses role taxonomies or reference schemes, use `F.9` and `A.6.9` to establish the exact Bridge, then state a separate `C.2.1` assertion about that Bridge naming the bounded use, direction, correspondence rule, tolerated semantic loss, polarity, and effective scheme; recover current reliance through `A.10` or `B.3` before acting.

The earlier Plain mention is not evidence for any stronger claim. Complete only the smallest direct relation needed by the current use.

