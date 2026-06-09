---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment & Bridge across Contexts"
section_id: "F.9:6"
section_title: "Bridge kinds (senseFamily-aware)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__007_bridge-kinds-sensefamily-aware.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "F.9 — Alignment & Bridge across Contexts"
  - "F.9:6 — Bridge kinds (senseFamily-aware)"
line_start: 71740
line_end: 71782
dependencies:
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.9"
  - "B.3"
  - "C.16.Q"
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

### F.9:6 - Bridge kinds (senseFamily-aware)

> **Two families** of Bridges: **Substitution Bridges** (senseFamily-preserving; can support Concept-Set rows) and **Interpretation Bridges** (explanatory; **not** for substitution).

#### F.9:6.1 - Substitution Bridges (sense-preserving)

These relate **SenseCells of the same senseFamily** and may support **limited substitution**:

1. **Equivalence** - *near-identity of sense*. Symmetric. Rare.
   *Use:* May support **Type-structure** rows when CL=3 and invariants match.
   *Loss Notes:* usually “none” or “profiling differences”.

2. **Narrower-than / Broader-than** - *proper inclusion of sense*. Directional.
  *Use:* Safe to substitute **narrower > broader** in **Naming-only** and sometimes **Role Assignment & Enactment**; **broader > narrower** is unsafe.
   *Loss Notes:* “loses special cases X”.

3. **Partial-overlap** - *non-empty intersection, neither includes the other*.
  *Use:* **Naming-only** at best. **Never** justifies Role Assignment & Enactment / Type-structure.
   *Loss Notes:* “A-only senseFamily”, “B-only senseFamily”.

4. **Disjoint** - *explicit contrast*.
   *Use:* For **didactic warnings**; not reuse support.
   *Loss Notes:* n/a (it asserts incompatibility).

#### F.9:6.2 - Interpretation Bridges (cross-senseFamily, explanatory)

These **do not support substitution** but **explain connections** across senseFamilies:

5. **Design-spec -> Run-trace** - a design concept relates to its run-time occurrence.
   *Example:* *BPMN\:Process* -> *PROV\:Activity*.
   *Use:* Explain design-to-execution correspondence. No Concept-Set rows.
   *Loss Notes:* “graph vs event”, “control-flow vs temporal extent”.

6. **Measure-of / Evidence-for (->)** — a measurement SenseCell evidences or quantifies another **senseFamily** (e.g., a Requirement clause).
   *Example:* *SOSA\:Observation* -> *ITIL\:SLO fulfilment*.
   *Use:* Explain evaluation. No substitution.

7. **Policy-implies / Obliges (->)** — a deontic statement constrains another **senseFamily**.
   *Example:* *ODRL\:Duty* -> *Service behaviour*.
   *Use:* Explain constraint propagation.

> **Rule of thumb.** If you want **rows** or **substitution**, you need a **Substitution Bridge** on the **same senseFamily**. If you want to **explain** why artefacts relate without claiming sameness, use **Interpretation Bridges**.

