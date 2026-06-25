---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__002_intent-applicability.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:1 — Intent & applicability"
line_start: 82127
line_end: 82141
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
keywords:
  - "Actuation"
  - "Method"
  - "MethodDescription"
  - "Role–Method–Work alignment"
  - "Work"
---

### F.11:1 - Intent & applicability

**Intent.** Provide a **notation‑free, Context‑aware map** that keeps four notions distinct and connectable:

* **`U.Method`** — the abstract **way of doing** (design‑time concept).
* **`U.MethodDescription`** — the **recipe episteme** that describes a Method.
* **`U.Work`** (informal: *Execution*) — the **run‑time occurrence** of doing (recorded event).
* **`U.Actuation`** — the **control output** applied to a plant (domain‑specific Work in Sys‑CAL).

The pattern makes the split **usable across FPF patterns** (Role Assignment & Enactment, Sys-CAL, KD-CAL, Kind-CAL, planned LCA-CAL) and **legible across Contexts** (SPEM/BPMN for design; PROV-O/SOSA for run; IEC 61131-3/state-space for control).

**Applicability.** Any time a discussion risks **mixing designs with executions**, **recipes with runs**, or **workflow with control signals**; whenever you need to **name** or **reason** about “how we do X”, “the SOP/script/model”, “the actual run”, or “the actuator push”.

**Non‑goals.** No team workflow, no editors, no tools. No prescriptive file formats. **Only** conceptual distinctions and safe reasoning moves.

