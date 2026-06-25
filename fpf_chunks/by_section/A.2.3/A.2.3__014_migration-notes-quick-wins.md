---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:10"
section_title: "Migration notes (quick wins)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__014_migration-notes-quick-wins.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:10 — Migration notes (quick wins)"
line_start: 3309
line_end: 3319
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.3.1"
  - "A.3.2"
  - "A.6.8"
  - "A.6.C"
  - "E.10"
  - "F.12"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Scope"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
---

### A.2.3:10 - Migration notes (quick wins)

1. **Name the promises.** List 5–15 consumer‑facing promises your context lives by; reify each as `U.PromiseContent` with `acceptanceSpec` and, if needed, `accessSpec` and `unitOfDelivery`.
2. **Separate provider from promise content.** Keep systems or teams as `U.System`; make them providers via `...#ServiceProviderRole:Context`.
3. **Wire evidence.** Ensure every relevant `U.Work` has `claimsPromiseContent` (and `fulfilsPromiseContent` post‑verdict).
4. **Choose metrics.** For each promise content, including local service labels that resolve to promise content, define 2-4 KPIs and the declared Work-based formulas (availability, lead-time, rejection rate, cost-to-serve), declare the **Claim scope (G)** and **Gamma_time** policy used for each KPI, and - when KPIs are numeric or comparable - define the underlying `U.Characteristic` plus measurement procedure and evidence (C.16 and C.25) and pin `{UnitType, ScaleKind, ReferencePlane, EditionId}`.
   → For each **promise content**, define 2–4 KPIs and the Work-based formulas named by value
, with explicit `Γ_time`.
5. **Bridge domains.** If a business ontology already exists ("business service", "technical service", or "internal service"), keep it in its own context and map to FPF Kinds via Bridges.
6. **Tidy language.** Apply **A.6.8 (RPR-SERV)** and **L-SERV**: ban unqualified "service" as a synonym for server, team, process, or ticket in normative prose; map them explicitly.

