---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:12"
section_title: "Worked examples (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__014_worked-examples-didactic.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:12 — Worked examples (didactic)"
line_start: 63380
line_end: 63482
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "A.6.Q"
  - "B.3"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "E.10.D1"
  - "E.17.1"
  - "E.17.ID.CR"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.8"
  - "F.9.1"
  - "U.BoundedContext"
  - "U.Mechanism"
keywords:
  - "Bridge-supported use"
  - "CL"
  - "bridge"
  - "bridge reading"
  - "cross-context alignment"
  - "direction"
  - "loss notes"
  - "state export"
  - "weakest-link scope"
---

### F.9:12 - Worked examples (didactic)

#### F.9:12.1 - Service acceptance (design) vs executions & observations (run)

* **Cells & Contexts**
  `ITIL4:SLO` *(Status, design)* <- `SOSA:Observation(availability)` *(Measurement, run)*
  `BPMN:Process` *(Method, design)* -> `IEC61131:Task-Execution` *(Execution, run)*
* **Narrative**
  Availability SLOs are **evaluated** by observations of task executions. No substitution follows: an SLO is not an observation, and a process is not an execution occurrence.
* **Bridge Cards (sketch)**
  *ITIL\:SLO <- SOSA\:Observation* - **CL=2** - Loss: sampling window, clock skew.
  *BPMN\:Process -> IEC\:Execution* - **CL=2** - Loss: control-flow vs temporalization, concurrency collapse.
* **Supported use**
  Explanation-only; Concept-Set rows may be **Naming-only** ("availability") with **CL >= 1** label coherence across Contexts.


#### F.9:12.2 - Behavioural role vs access role

* **Cells & Contexts**
  `BPMN:Participant` *(Role)* - `NIST-RBAC:Role` *(Status)*
* **Narrative**
  Both talk about -who acts-, but one is a **behavioural mask** in a process model, while the other is an **authorization grouping**.
* **Bridge**
  **Kind:** `Partial-overlap`, **CL=2**; Loss: assignment moment, enforcement placement, multiplicity.
* **Supported use**
* **Naming-only** row “actor”; **no Role Assignment & Enactment reuse** across senseFamilies.


#### F.9:12.3 - Equivalence of subtype notions for structural rows

* **Cells & Contexts**
  `OWL2:SubClassOf` *(Type-structure)* - `TaxX:is-a` *(Type-structure curated)*
* **Bridge**
  **Kind:** `Equivalence`, **CL=3** **iff** the curated taxonomy is **acyclic and anti-symmetric** and uses class-level reasoning.
* **Supported use**
  **Type-structure** rows supported (`CL = 3`); Loss: OWL profile limitations (RL/EL/QO).


#### F.9:12.4 - Accuracy (metrology) vs accuracy (data-quality)

* **Cells & Contexts**
  `ISO80000:measurement-accuracy` *(Measurement)* - `ISO25024:data-accuracy` *(Measurement)*
* **Bridge**
  **Kind:** overlap, **CL=2**; Loss: “true value” notion differs (instrument vs dataset), scale transformations.
* **Supported use**
  **Naming-only** row “accuracy” used for reports; no shared methods.


#### F.9:12.5 - Setpoint (control) vs target (service)

* **Cells & Contexts**
  `CTRL:text:setpoint` *(Status/Control)* - `ITIL:target` *(Status/Service)*
* **Bridge**
  **Kind:** `Disjoint` - Rationale: physical reference value vs business objective; different target kinds (control parameters vs requirement clause).
* **Supported use**
  Didactic contrast only; prevents accidental substitution in SLO calculus.

#### F.9:12.6 - Role substitution & CL gating (RoleAssignment/enactment scope)

> **Use.** A worked, role-focused restatement of Bridge usage for the recurring question:
> “May `Role_B@B` satisfy `Role_A@A` for `requiredRoles` / enactment checks-”

**Rule.** **No cross-context substitution by name.** If a step in **Context A** needs `Role_A`, and the performer only holds `Role_B` in **Context B**, an explicit **Bridge** **MUST** state how `Role_B@B` relates to `Role_A@A`, with direction, **CL**, and Loss Notes.

##### F.9:12.6.1 - Directional substitution (role-oriented shorthand)

A Bridge may assert, *directionally*:

* **`substitutesFor(Role_B@B > Role_A@A)`** with a CL and a list of **kept** and **lost** characteristics (for roles: typical losses are RCS characteristics and/or RSG nuances).
* The reverse direction **does not** follow unless declared (F.9:13.7).

##### F.9:12.6.2 - CL > gating policy (didactic default)

| **CL** | Meaning (intuitive)                     | **Supported scope** | **Extra condition**                                                                  | **Unsupported by default** |
| :----: | --------------------------------------- | :--------: | ------------------------------------------------------------------------------------ | :-------: |
|  **3** | Near-isomorphic sense; no material loss | Yes | None beyond ordinary gates (e.g., window + RSG state) | - |
|  **2** | Close but with stated losses            |    Yes     | Require **extra evidence** (e.g., additional checklist item) **or** a named checker |     —     |
|  **1** | Distant analogy; risky                  | Exception  | Only by explicit **Waiver SpeechAct** naming the Bridge + loss rationale             |  Default  |
|  **0** | Incompatible                            |     No     | —                                                                                    |    Yes    |

*Notes.* The **substitution scope** is defined in **F.9:13.2-13.3** (Role-Assignment/Enactment-eligible substitution requires **CL >= 2**; Naming-only is **CL >= 1**).
CL penalties feed assurance (R) per **B.3**; safety-critical policies may require **CL >= 2** by default (D.2).

##### F.9:12.6.3 - Typical bridges (worked patterns)

* **BPMN Task - PROV Activity.**
  `substitutesFor(Task@BPMN > Activity@PROV)` with **CL=2**; **lost:** BPMN control-flow guards; **kept:** “bounded occurrence consuming/producing entities.”
  *Effect.* A Work logged as `Activity@PROV` may satisfy a step requiring a `Task@BPMN` **iff** an extra guard enforces the BPMN pre-/post-conditions.

* **Essence Alpha-State - RoleStateGraph state.**
  `substitutesFor(“Alpha.State:Ready”@Essence > “Ready”@RSG)` with **CL=2**; **lost:** Alpha-specific narrative criteria; **kept:** checklist-based readiness.
  *Effect.* A team may reuse Essence states as labels in RSG, but still maintains local checklists as **StateAssertions**.

* **ITIL Service Owner - RBAC Administrator.**
  Typically **CL=1** and **directional** (Administrator\@RBAC > ServiceOwner\@ITIL) **rejected** unless a policy Bridge enumerates compensating controls.
  *Effect.* Prevents “ops admin = service-accountability role” conflations without an explicit waiver.

##### F.9:12.6.4 - Bridge invariants (role-relevant reminders)

* **Local first.** Substitution never overrides in-Context role algebra (its own role relations, guards, and exclusions).
* **Loss honesty.** If a Bridge’s loss notes indicate that a dropped characteristic is required by a step, substitution is invalid (regardless of CL).
* **No silent inversion.** Direction is explicit; substitution does not reverse unless declared (F.9:13.7).

