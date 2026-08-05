---
chunk_kind: "child"
pattern_id: "A.14"
pattern_title: "Advanced Mereology: Components, Portions, Aspects & Phases"
section_id: "A.14:9.1"
section_title: "Relation-use decision procedure"
source_path: "FPF-Spec.md"
output_path: "by_section/A.14/A.14__011_relation-use-decision-procedure.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.14 — Advanced Mereology: Components, Portions, Aspects & Phases"
  - "A.14:9.1 — Relation-use decision procedure"
line_start: 23886
line_end: 23911
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.2"
  - "B.3.5"
  - "C.13"
keywords:
  - "ComponentOf"
  - "PhaseOf"
  - "PortionOf"
  - "composition"
  - "mereology"
  - "part-of"
---

### A.14:9.1 - Relation-use decision procedure

**Step 0 — Firewall check.**
If your sentence is about *who does what*, *how it is done* (role or method), or *what happened when* (run or work occurrence), you are **not** in A.14 merely because ordinary speech names a thing. Use the role, method, work, or evidence owner. For an episteme, A.14 may participate in content parthood or a proper temporal restriction of one unchanged C.2.1 identity. Changed episteme content, EntityOfConcern, or effective reference scheme opens another episteme and the separate C.2.1 edition-continuity test; a dated Work part stays under A.15.1.

**Step 1 — Is it measured stuff?**
If yes, pick **PortionOf**. Confirm μ is declared (CC‑POR‑1/2). Test additivity on a toy split (CC‑POR‑3). If flows cross a boundary, remodel as interactions, not portions (CC‑POR‑4).

**Step 2 — Is it a discrete inside part?**
If yes, pick **ComponentOf** (physical) or **ConstituentOf** (conceptual). Do **not** use PortionOf here.

**Step 3 — Is it the same carrier restricted to a proper time slice?**
If yes, pick **PhaseOf**. Verify that the proposed part is not the whole carrier, its interval is a proper sub-interval, and identity and non-overlap conditions hold (CC‑PHA‑1/2/3). A whole-lifetime or self-reference needs no phase object. If identity criteria break, escalate to **B.2** (CC‑PHA‑4).

**Step 4 — Is it a membership statement?**
Use **MemberOf** only; avoid any part‑inferences (CC‑MEM‑2). If you need a **collection as a whole**, use **C.13** (`Γ_m.set`) and **B.3.5** when assurance grounding is current. If you need **collective action**, first admit an acting collective `U.System`, then use the role, method, work, and evidence owners.

**Quick spot-tests.**

| Smell                          | Likely error                      | Fix                                                                                                                          |
| ------------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| “20% of the chassis”           | Treating structure as stuff       | Use **ComponentOf**; if truly laminar material, PortionOf applies to **material stock**, not the assembled chassis.          |
| “Chapter 2 is 15% of the book” | Mixing measures and constituents  | Use **ConstituentOf**; the 15% is **length‑of‑text** as a separate statement.                                                |
| “Spec v2 overlaps v1” | A version label is asked to decide episteme identity and temporal parthood | Compare the exact C.2.1 identity triples. If they differ, identify two epistemes and test `EpistemeEditionRelation` separately; use A.15.1 for overlapping drafting Work. If one unchanged episteme is merely referenced at two times, no second episteme or phase object follows without a proper-interval use. |
| “Team is part of the project”  | Member vs part confusion          | Use **MemberOf(Team, ProjectCollective)**, not partOf.                                                                       |

