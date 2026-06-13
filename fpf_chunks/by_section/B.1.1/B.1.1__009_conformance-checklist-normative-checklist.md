---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:8"
section_title: "Conformance Checklist (normative checklist)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__009_conformance-checklist-normative-checklist.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:8 — Conformance Checklist (normative checklist)"
line_start: 30013
line_end: 30029
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:8 - Conformance Checklist (normative checklist)

| ID             | Requirement                                                                                                                                                | Purpose                             |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **CC‑B1.1.1**  | `D` **SHALL** be acyclic (DAG).                                                                                                                            | Ensure foldability.                 |
| **CC‑B1.1.2**  | All nodes in `D` **SHALL** share a single `DesignRunTag ∈ {design, run}`.                                                                                 | Ban DesignRunTag chimeras.            |
| **CC‑B1.1.3**  | All edges in `E` **SHALL** belong to the **normative `V_rel`** (**ComponentOf, ConstituentOf, PortionOf, PhaseOf** only). | Keep mereology crisp and finite. |
| **CC‑B1.1.4**  | Cross‑holon influences **SHALL** be modelled as `U.Interaction`, **NOT** parthood.                                                                         | Preserve locality (LOC).            |
| **CC‑B1.1.5**  | Every top‑level holon **SHALL** declare a `U.Boundary`; if Γ\_work will be used, a Boundary Ledger **SHALL** be produced.                                  | Make results comparable/auditable.  |
| **CC‑B1.1.6**  | If COMM/LOC is claimed, an **IND‑LOC** independence declaration **SHALL** be attached.                                                                     | Make locality explicit.             |
| **CC‑B1.1.7**  | A **WLNK‑CUT** set **SHALL** be stated for the chosen Γ‑flavour.                                                                                           | Make caps explicit; avoid optimism. |
| **CC‑B1.1.8**  | **MONO‑AX** **SHALL** enumerate the monotone characteristics used by the Γ‑flavour.                                                                                   | Avoid hidden regress.               |
| **CC‑B1.1.9**  | A **IDEM‑WIT** singleton case **SHALL** be shown or referenced.                                                                                            | Ground identity.                    |
| **CC‑B1.1.10** | Order/time/resource **SHALL NOT** be encoded via structural edges; they must be routed to Γ\_ctx/Γ\_method, Γ\_time, Γ\_work respectively.                   | Maintain A.15 Strict Distinction.   |
| **CC‑B1.1.11** | If a cycle or a locality violation persists, the modeller **SHALL** either refactor or declare a **Meta‑Holon Transition (B.2)**.                          | Make emergence explicit.            |
| **CC‑B1.1.12** | Any mapping edges (`RepresentationOf`, `Implements`, etc.) **SHALL** be kept outside `E` (value‑level), or recast as `U.Interaction` if cross‑boundary.    | Eliminate category errors.          |

