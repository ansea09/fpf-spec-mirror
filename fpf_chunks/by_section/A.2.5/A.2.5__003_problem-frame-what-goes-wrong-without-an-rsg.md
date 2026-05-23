---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "U.RoleStateGraph: The Named State Space of a Role"
section_id: "A.2.5:2"
section_title: "Problem frame (what goes wrong without an RSG)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__003_problem-frame-what-goes-wrong-without-an-rsg.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.2.5 — U.RoleStateGraph: The Named State Space of a Role"
  - "A.2.5:2 — Problem frame (what goes wrong without an RSG)"
line_start: 3406
line_end: 3416
dependencies:
  - "A.15"
  - "A.2.1"
  - "A.2.3"
  - "B.3"
  - "E.10.D1"
  - "F.9"
  - "U.RoleAssignment"
  - "U.RoleDescription"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:2 - Problem frame (what goes wrong without an RSG)

1. **Readiness blur.** Teams conflate “has the badge” with “is fit to act now”. Without explicit states (*Ready*, *Calibrated*, *Authorized*, *Suspended*…), enactment checks dissolve into ad‑hoc judgement.
2. **Checklist drift.** Criteria for “ready/approved” live in scattered documents; there is no single conceptual anchor tying them to the role.
3. **Workflow/role confusion.** “State” of a *workflow* (according to workplan) is mistaken for the *state of a role* (eligibility to enact).
4. **Status ≠ enactment.** Epistemic/Normative roles (e.g., *NormativeStandard*, *ApprovedSpecification*) need *statuses* that are **not enactable**, yet are used to gate decisions.
5. **Cross‑context substitution by name.** Labels like *Approved* or *Ready* silently cross contexts with different criteria; the loss is hidden and unaudited.

**Consequences.** Violations of **Strict Distinction (A.7)** and **Didactic Primacy (E.12)**: ambiguous authority to act, unsafe SoD, and non‑reproducible evaluations.


