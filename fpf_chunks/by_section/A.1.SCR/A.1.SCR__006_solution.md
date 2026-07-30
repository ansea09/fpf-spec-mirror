---
chunk_kind: "child"
pattern_id: "A.1.SCR"
pattern_title: "Finding the Acting or Changed System"
section_id: "A.1.SCR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.SCR/A.1.SCR__006_solution.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "A.1.SCR — Finding the Acting or Changed System"
  - "A.1.SCR:4 — Solution"
line_start: 2287
line_end: 2375
dependencies:
  - "A.1"
  - "A.1.STM"
  - "A.15.6"
  - "A.6.P"
  - "A.6.RCD"
  - "E.10"
  - "F.18"
keywords:
---

### A.1.SCR:4 - Solution

#### A.1.SCR:4.1 - State the system-dependent decision

Start with four plain statements:

1. the claim you are trying to use;
2. the exact entity proposed as actor, change bearer, capability holder, persistent subject, or project system-of-interest;
3. the decision or action that would differ if this entity were or were not a system; and
4. the observation, boundary fact, or construction fact that would settle that difference.

Do not use bare *system candidate* as a working noun. Before referent recovery say *the proposed system reading of the phrase*. Once an actual referent is identified, say *the exact `U.Entity` being evaluated under the already admitted `U.System` kind*. Say *an alternative being considered for designation as the project system-of-interest* only when one named project plan or decision compares possible referents. None of these expressions creates a status kind or a pre-system lifecycle state.

#### A.1.SCR:4.2 - Take the direct-owner exit first

Before testing systemhood, ask whether the current decision already concerns one of these objects:

| Current object | Direct owner or exit |
| --- | --- |
| Holder-dependent capability | A.2.2 |
| Role value or obtaining role assignment | A.2 and A.2.1 |
| Reusable way of doing or its description | A.3.1 and A.3.2 |
| Intended work | A.15.2 `U.WorkPlan` |
| Dated performed occurrence | A.15.1 `U.Work` |
| Actual bounded change | A.3.4 and the exact transformation owner |
| Claim-bearing model, rule, report, code, or other episteme | C.2.1 |
| Selected structure or transformation-flow structure | A.22 or E.18 |
| Promise, commitment, speech act, or permission result | A.2.3, A.2.8, A.2.9, or A.2.8.PER |
| Service/access referent, status, evidence, evaluation, delivery, acceptance, or other relation | A.6.P §4.11a and then the exact direct owner |

If this result answers the decision, stop here. Name the object, its governing pattern, and what you can now do. Do not apply A.1 as a recurring project ritual.

If a needed relation has no current governor, state the exact participants and blocked receiving use, return `missing-governor[...]`, and continue under A.6.RCD. Do not substitute `relatedTo`, a graph edge, or a local bundle.

#### A.1.SCR:4.3 - Apply A.1 only when systemhood remains load-bearing

When the decision still depends on systemhood, recover all six A.1 constructive components. A.1 remains the criterion owner.

| A.1 component | Practical recovery question |
| --- | --- |
| Exact entity | Which one entity is being tested, and what identity rule distinguishes it from its name, description, parts, environment, and successor? |
| Exact constituents | Which entities actually constitute it rather than merely being nearby, listed, sampled, or described with it? |
| Constructive part relations and assembly | Which obtaining part relations and assembly make these constituents this whole? |
| Reidentification rule | Which changes preserve it, and which replacement, disassembly, completion, or termination ends it? |
| Composition-grounded whole-level characteristic | Which characteristic follows from the actual assembly rather than from a label, plan, measurement, or one constituent? |
| Possible participation in a larger constructive assembly | Which boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy the applicable governed construction rule? |

Then apply the already admitted `U.System` condition: the whole has an actual physical or operational organization through which it can causally participate in Work or transformation while preserving identity. A role assignment, capability, Work occurrence, plan, codebase, or description may provide evidence but does not create the system.

#### A.1.SCR:4.4 - Return one decision-bearing result

| Disposition | Required first result |
| --- | --- |
| Direct-owner exit | Exact non-system object or relation, its owner, and the action now possible; no A.1 test. |
| System recognized | Exact system, identity and boundary, decisive construction facts, acting-eligibility basis, and the system-dependent next use. |
| Proposed system reading rejected | Exact non-system subject or relation, its direct owner, and the action that remains possible. |
| Evaluation unresolved | Exact `U.Entity`, missing A.1 component or kind-specific condition, needed information, and the decision that stays blocked. |

These are response forms, not a schema. Persist a classification assertion or evaluation-result episteme only when another use must inspect or cite it; C.2.1 then owns that episteme. `true | false | unknown` describes an evaluation and changes no kind extent.

#### A.1.SCR:4.5 - Add only the neighbors used now

After the first result, add only claims consumed by the decision. Shared extent, one carrier, a common label, or co-occurrence establishes none of their identities or relations. The system does not become its role assignment, capability, Work, transformation, Method, plan, evidence, or description.

#### A.1.SCR:4.6 - Keep service/access recovery independent

When service/access wording is the unresolved phrase, start in A.6.P §4.11a. A.6.P names the exact service-provision Work, Method, PromiseContent, role assignment, bearer, access-providing arrangement, permission, status, or direct relation. Return to A.1.SCR only if the repaired sentence makes a separate system-dependent assertion about the exact entity recovered there—an exact bearer or access-providing arrangement.

“My service stopped” does not by itself say that a system stopped. Service-provision Work may have ceased, an exact deployed or physical bearer may have stopped or become unavailable, an access-providing arrangement may be proposed as the exact system whose functioning stopped, or promised availability/fulfilment may have failed. A.1.SCR owns only a separately proposed exact bearer or access-providing-arrangement reading when its system boundary matters to the decision.

#### A.1.SCR:4.7 - Preserve the project system-of-interest bridge

The primary expression is **project system-of-interest**, inherited from systems engineering without adding target, aim, or goal semantics. `systemOfConcern` may serve as a historical systems-engineering Plain synonym; it creates no U-kind, role, relation, or second designation.

A project plan or decision may designate one system as the project system-of-interest. Keep six questions separate:

1. identify the exact actual system, or keep a merely intended future referent as a designator in plan, decision, or description content;
2. name the plan or decision that designates it and the intended change or use;
3. admit composite project Work only after A.15.1 and A.15.6 qualifications hold;
4. state each actual work-to-referent, transformation, production, evaluation, delivery, acceptance, or later-use fact under its own governor;
5. test any `SystemOfInterestRole` interpretation and any A.2.1 assignment separately; and
6. when the recognized system must be returned to the long dependency from outside use through architecture, Work, change, and recursive builders, continue through A.1.STM. Otherwise open the direct owner of the next claim.

Infer no project designation from system recognition, affectedness, familiar wording, a role label, or shared realization. If the decision needs the unsupported compound project-selection truth, preserve `missing-substrate[project-selection-conjunction]` until one constructor substrate and edition define that claim.

#### A.1.SCR:4.8 - Use physical grounding without cross-kind identity

Ask what physically or operationally exists, where its boundary lies, and what preserves or ends its identity. This pressure helps test a proposed system reading and reject description-only substitutes. It does not identify a system with its role, assignment, capability, Work, transformation, Method, plan, evidence, or description. Do not import BORO categories, unrestricted composition, or a new 4D record.

