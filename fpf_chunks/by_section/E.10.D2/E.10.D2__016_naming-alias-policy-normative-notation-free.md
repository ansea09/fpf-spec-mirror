---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:15"
section_title: "Naming & alias policy (normative, notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__016_naming-alias-policy-normative-notation-free.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:15 — Naming & alias policy (normative, notation‑free)"
line_start: 53045
line_end: 53080
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

### E.10.D2:15 - Naming & alias policy (normative, notation‑free)

#### E.10.D2:15.1 - Suffix discipline (recap).**

* **Preferred default:** **`…Description`** for Role/Method/Service/Work.
* **Reserved:** **`…Spec`** only if the item passed the **Spec‑gate** (F‑mode, testable invariants, harness id, Context named).
* **Banned:** Using **–Spec** as a synonym for “detailed description”.

#### E.10.D2:15.2 - Canonical/alias map (current edition).**

| Concept (intension) | Preferred episteme name      | Allowed alias (equal scope)   | Deprecated alias | Notes                                                                                 |
| ------------------- | ---------------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------- |
| Role                | **RoleDescription**    | RoleCard *(Pedagogy only)*    | —                | *RoleCard* is informal (teaching layer), not a normative episteme name.                     |
| Role (F‑mode)       | **RoleSpec**           | —                             | —                | Only after Spec‑gate.                                                                 |
| Method              | **MethodDescription**  | —                             | **MethodSpec**   | Global rename complete; legacy references should be updated.                          |
| Method (F‑mode)     | **MethodSpec**         | —                             | —                | Now reserved for harnessed, testable methods.                                         |
| Work (schedule)     | **U.WorkPlan**         | **WorkDescription**           | **WorkSpec**     | *WorkSpec* alias removed; *WorkDescription* remains as didactic alias for *WorkPlan*. |
| Service             | **ServiceDescription** | ServiceCard *(Pedagogy only)* | —                | As above: Card is informal only.                                                      |
| Service (F‑mode)    | **ServiceSpec**        | —                             | —                | Requires acceptance harness id (F.15).                                                |

#### E.10.D2:15.3 - Verb & morphology rules.**

* **Verbs.** Use *characterised by*, *recorded in*, *encoded by*; avoid *contains*, *is stored in*, *is implemented by* when speaking at the conceptual level.
* **Morphology.**

  * Roles name **masks** as **count nouns** (*Operator, ChangeAuthority*).
  * States as **state nouns/participles** (*Authorized, Active*).
  * Status names are **classifiers over knowledge** (*SupportsClaim, NormativeStandard*).
  * Descriptions/Specs use neutral nouns (*RoleDescription, MethodSpec*).

#### E.10.D2:15.4 - Deprecations (effective now).**

* **MethodSpec** (as a general name) → **MethodDescription** unless Spec‑gate is met.
* **WorkSpec** (alias for WorkPlan) → **WorkDescription** (allowed alias), or **U.WorkPlan** (preferred).
* Texts must avoid “contains RSG/RCS” phrasing (see RSCR‑D2‑E04).

