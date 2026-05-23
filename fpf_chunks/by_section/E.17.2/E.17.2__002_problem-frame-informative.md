---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:1"
section_title: "Problem frame  (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__002_problem-frame-informative.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:1 — Problem frame  (informative)"
line_start: 56302
line_end: 56320
dependencies:
  - "A.1"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.TGA"
  - "F.18"
  - "U.Episteme"
  - "U.EpistemeSlotGraph"
  - "U.MultiViewDescribing"
  - "U.System"
  - "U.ViewpointBundleLibrary"
keywords:
  - "E.TGA bindings"
  - "EoIClass = U.Holon"
  - "Functional/Procedural/Role-Enactor/Module-Interface views"
  - "ISO 42010 mapping"
  - "engineering viewpoints"
  - "holon"
---

### E.17.2:1 - Problem frame  *(informative)*

Engineering teams almost always talk about systems and their models through a **small set of recurring “views”**:
* *What capabilities and behaviours does the system enact?* — function‑oriented, transduction‑oriented talk.
* *What sequences, workflows, and control logics does it realise?* — procedure/process/state‑oriented talk.
* *Who or what enacts which roles?* — role‑enactment, organisational and socio‑technical talk.
* *How is the system decomposed into modules and interfaces?* — physical/logical architecture talk.

In industry, these lenses show up under many names: *functional view, logical view, behavioural view, process view, structural/physical view, deployment view, responsibility view,* and so on. Modern standards and tools (ISO/IEC/IEEE 42010:2022, INCOSE SE Handbook, SysML v2 “views as queries”) all recognise that **viewpoints should be reusable structures**, not ad‑hoc labels.

In FPF, E.17.0 and E.17.1 give the **generic machinery**:
* `U.Viewpoint` as an intensional specification (stakes/concerns/allowed D/S kinds),
* `U.View` as an episteme‑level view (epistema under a viewpoint),
* `U.ViewpointBundle` / `ViewFamilyId` as reusable collections of viewpoints.

E.TGA (E.18:5.12) already assumes a **canonical engineering family** with names like “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, “Module‑Interface”. Without a formal bundle tying these together, those names drift and the mapping between E.TGA, MVPK and I/D/S becomes fragile.

TEVB addresses this by defining a **single, explicit engineering bundle** with a fixed `ViewFamilyId` and a small set of canonical engineering viewpoints over `U.Holon`.

