---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:1"
section_title: "Problem frame  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__002_problem-frame-informative.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:1 — Problem frame  (informative)"
line_start: 67725
line_end: 67743
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:1 - Problem frame  *(informative)*

Engineering teams almost always talk about systems and their models through a **small set of recurring “views”**:
* *What capabilities and behaviours does the system enact?* — function‑oriented, transformation‑oriented talk.
* *What method descriptions, procedure structures, and control-logic descriptions does it realize?* — procedure-, method-, and state-oriented talk.
* *Which systems or acting holons are assigned which work-facing roles, responsibilities, or allocation expectations?* — role-assignment, organisational and socio-technical talk.
* *How is the system decomposed into modules and interfaces?* — physical and logical architecture talk.

In industry, these lenses show up under many names: *functional view, logical view, behavioural view, process view, structural and physical view, deployment view, responsibility view,* and so on. Modern standards and tools (ISO/IEC/IEEE 42010:2022, INCOSE SE Handbook, SysML v2 “views as queries”) all recognise that **viewpoints should be reusable structures**, not ad‑hoc labels.

In FPF, E.17.0 and E.17.1 give the **generic machinery**:
* `U.Viewpoint` as a viewpoint specification (stakes, concerns, and allowed Description kinds and specification-use gates),
* `U.View` as an episteme‑level view (epistema under a viewpoint),
* `U.ViewpointBundle` / `ViewFamilyId` as reusable collections of viewpoints.

`E.18` already uses a **canonical engineering viewpoint-family map** with names like “Functional”, “Procedural”, “allocation-responsibility or device-structure”, “Module-Interface”. Without a formal bundle tying these together, those names drift and the mapping between `E.18`, MVPK, EntityOfConcern, Description-episteme boundary, and specification use becomes fragile.

TEVB addresses this by defining a **single, explicit engineering bundle** with a fixed `ViewFamilyId` and a small set of canonical engineering viewpoints over `U.Holon`.

