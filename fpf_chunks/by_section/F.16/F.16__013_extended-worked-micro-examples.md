---
chunk_kind: "child"
pattern_id: "F.16"
pattern_title: "Worked‑Example Template (Cross‑Domain)"
section_id: "F.16:12"
section_title: "Extended worked micro‑examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.16/F.16__013_extended-worked-micro-examples.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "F.16 — Worked‑Example Template (Cross‑Domain)"
  - "F.16:12 — Extended worked micro‑examples"
line_start: 83991
line_end: 84032
dependencies:
  - "A.15"
  - "A.3"
  - "B.1.5"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.1-F.12"
  - "F.15"
keywords:
  - "cross-domain illustration"
  - "didactic template"
  - "example"
  - "pedagogy"
---

### F.16:12 - Extended worked micro‑examples

> Each example fits the **one‑page canvas** (§5) and makes the **row** and **bridges** do the work.

#### F.16:12.1 - Type alignment: OWL class vs FCA concept (design‑time only)

**Title & claim.** *“Two Lenses on *Pump*: OWL class and FCA concept align for catalogue reasoning.”*
**Unification line.** Kind-CAL (design) + FCA (design).
**Contexts.** **OWL 2 (profiles)** — classes, `subClassOf` (design). **FCA corpus** — formal concepts, lattice order (design).
**SenseCells.** ⟨OWL\:class ‘Pump’⟩, ⟨FCA\:formal‑concept ‘Pump’⟩.
**Row ρ.** { ⟨OWL\:Pump⟩ ↔ ⟨FCA\:Pump⟩ } — *same practical extension in this product catalogue*.
**Bridge β.** ⟨FCA\:lattice‑order⟩ **overlaps** ⟨OWL\:subclass‑order⟩, **CL=2**, *loss:* FCA intents may include context attributes not modeled in OWL restrictions.
**Role-Description hooks.** `TypeLabel` → ⟨OWL\:class⟩ (for naming), no runtime **Role Assignment/Enactment**.
**Micro‑narrative (3 lines).** For catalogue queries, the **instances** covered by OWL class *Pump* match those of the FCA concept created from the same attributes; we treat them as one row. The **orderings** diverge in nuance (β), but not for membership in this example.
**Harness pings.** *S‑Row‑Cross*, *S‑TemporalHonesty* (design only), *S‑Bridge‑Kind‑CL*.

#### F.16:12.2 - Role vs permission: SoD in enactment vs access control

**Title & claim.** *“Behavioral role (BPMN) is disjoint from access role (RBAC); keep duties separate.”*
**Unification line.** Role Assignmnent and Enactment (design & run) + access/deontics (design).
**Contexts.** **BPMN 2.0** — participant/lanes (design). **NIST RBAC (2004)** — roles/permissions (design).
**SenseCells.** ⟨BPMN\:participant⟩, ⟨RBAC\:role⟩.
**Row ρ.** — *(intentionally none)* — we do **not** treat them as the same.
**Bridge β.** ⟨BPMN\:participant⟩ **disjoint** ⟨RBAC\:role⟩, **CL=3**, *loss:* none—*different dimensions* (behavioral mask vs permission grouping).
**Role-Description hooks.** `Operator` → ⟨BPMN\:participant⟩; `AccessRole` → ⟨RBAC\:role⟩. **SoD:** `Operator` ⟂ `AccessRole‑Admin`.
**Window.** Not applicable.
**Micro‑narrative (3 lines).** We show SoD by prohibiting the same actor from holding **Operator** and **AccessRole‑Admin**. The disjoint **β** prevents leakage between behavioral masks and permission bundles.
**Harness pings.** *S‑RoleDescr‑SingleCell*, *S‑SoD*, *S‑Bridge‑Disjoint*.

#### F.16:12.3 - Method quartet: from MethodDescription to Work with observations

**Title & claim.** *“Behavioral role (BPMN) is disjoint from access role (RBAC); keep duties separate.”*
**Unification line.** **Role Assignment & Enactment** (design & run) + access/deontics (design).
**Contexts.** **SPEM 2.0** (design: Method or MethodDescription), **PROV‑O** (run: Activity), **SOSA/SSN** (run: Observation), **ITIL 4** (design: SLO).
**SenseCells.** ⟨SPEM\:MethodDescription⟩, ⟨PROV\:activity⟩, ⟨SOSA\:observation⟩, ⟨ITIL\:SLO⟩.
**Row ρ.** { ⟨ITIL\:SLO\:build‑time⟩ ↔ ⟨SOSA\:observed‑build‑duration⟩ } — *compare promised vs observed duration on the same window*.
**Bridges.** β₁: ⟨SPEM\:MethodDescription⟩ **narrower‑than** ⟨PROV\:activity‑plan⟩, **CL=2**, *loss:* PROV lacks prescriptive structure; β₂: ⟨SOSA\:observation⟩ **narrower‑than** ⟨ITIL\:measurement⟩, **CL=2**, *loss:* ITIL abstracts from procedure.
**Role-Description hooks.** `Operator` → ⟨BPMN\:participant⟩; `AccessRole` → ⟨RBAC\:role⟩. **SoD:** `Operator` ⟂ `AccessRole-Admin`.
**Window.** *Release window: calendar week*.
**Micro‑narrative (4 lines).** The **MethodDescription (SPEM)** implies a target **build‑time**; **Work (PROV activity)** occurs; **observations (SOSA)** provide actuals; we compare against the **SLO (ITIL)** via row ρ over the *calendar week* window. Bridges β₁–β₂ explain why plan/measure semantics do not collapse.
**Harness pings.** *S‑Row‑Cross*, *S‑Window*, *S‑RoleDesc‑SingleCell*, *S‑TemporalHonesty*.

