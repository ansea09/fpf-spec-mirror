---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:6"
section_title: "Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__007_invariants-normative.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:6 — Invariants (normative)"
line_start: 52741
line_end: 52779
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

### E.10.D2:6 - Invariants (normative)

**IDS‑1 (Plane purity).**
An intensional `U.T` **MUST NOT** be conflated with its Description/Spec or with any `U.Carrier` or `U.Work`.

**IDS‑2 (Context locality).**
Every `…Description/…Spec` **MUST** name a `U.BoundedContext`. Wording inside is read **as‑local**; no global meaning is implied.

**IDS-3 (Spec-gate).**
A episteme **MUST NOT** use the **–Spec** suffix unless: *(a)* the artefact declares **`U.Formality = Fk` with k ≥ 4** per **C.2.3**, *(b)* invariants are testable predicates, *(c)* an acceptance harness is linked (F.15), *(d)* Context is explicit.

**IDS‑4 (Characterisation verbs).**
Texts **MUST** say: *“`U.Role` is **characterised by** `U.RCS`/`U.RSG` in the RoleDescription”*.
They **MUST NOT** say: *“the role **contains** the RCS/RSG”*.

**IDS‑5 (RCS/RSG scope).**
`U.RCS`/`U.RSG` are **intensional structures**. Their **presentations** (characteristics, state names, admissible transitions, checklists) live in the **RoleDescription**, and in **RoleSpec** only when transitions and state predicates are fully testable.

**IDS‑6 (Evaluation semantics).**
`U.Evaluation` **MUST** operate over evidence against conformance checklists from the Description/Spec and **MUST** produce a **state attestation** (who/what is in state *S* @Context within window *W*). Evaluation **does not** mutate the intensional object.

**IDS‑7 (Status separation).**
Epistemic/deontic statuses (Evidence/Requirement/Standard) are roles over **knowledge units**; they **MUST NOT** be used as state names in `U.RSG`.

**IDS‑8 (Register discipline).**
Every Description/Spec **SHOULD** include both **Tech** and **Plain** labels. Symbolic aliases are optional and informative.

**IDS‑9 (No stealth bridges).**
Descriptions/Specs **MUST NOT** import meanings from other Contexts by shared labels. Cross‑context relations exist only as **F.9 Bridges**.

**IDS‑10 (Window honesty).**
When an evaluation is time‑bounded, the **window** **MUST** be stated in the attestation.

**IDS‑11 (Ladder clarity).**
A Description may mature into a Spec by satisfying IDS‑3; the opposite move requires a rationale (loss of testability) and must drop the **–Spec** suffix.

**IDS‑12 (Didactic bound).**
A RoleDescription **SHOULD** fit on one screen per state graph plus one screen of notes; sprawling documents belong to pedagogy, not to the core Description.

