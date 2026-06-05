---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "SCR/RSCR Harness for Unification"
section_id: "F.15:15"
section_title: "Worked “dry‑runs” (composite slices)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__016_worked-dry-runs-composite-slices.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "F.15 — SCR/RSCR Harness for Unification"
  - "F.15:15 — Worked “dry‑runs” (composite slices)"
line_start: 73402
line_end: 73446
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.1-F.14"
  - "F.14"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:15 - Worked “dry‑runs” (composite slices)

> Each dry‑run shows **how the checks fire** when something evolves. These are **thinking rehearsals**, not procedures.

#### F.15:15.1 - New edition of ITIL (services) arrives

**Slice.** Contexts: ITIL 4(2020)@t0 → ITIL 4(2024)@t1; Row: *Service-Availability*; **Role Description**: `AvailabilityStatus`; Bridges: to SOSA/SSN observations.

**Fire.**
E1 (**no silent replacement**): decide **new Context** ITIL 4(2024) because SLO definitions narrowed.
E5 (**row identity**): row *Service‑Availability*@t1 **new** (cells now ⟨ITIL2024\:SLO⟩ + ⟨SOSA\:obs⟩). Retire old row with note.
E9 (**bridge re‑validate**): sampling assumptions changed → **lower CL** by one and update loss note (*new calc window*).
E7 (**single-cell Role Description**): `AvailabilityStatus` still points to exactly one cell (ITIL2024\:SLO). Name unchanged → **no alias** needed.

**Pay‑off.** History is preserved; reuse remains safe; acceptance bindings (F.12) still compare anchored things.

#### F.15:15.2 - Rename a Role Description without changing meaning

**Slice.** **Role Description** `IncidentStatus`@t0 → `ServiceIncidentStatus`@t1; same SenseCell.

**Fire.**
E8 (**alias‑then‑rename**): create **Alias** `IncidentStatus → ServiceIncidentStatus` (F.13).
S8 (**name discipline**): new name fits the suffix rules (F.5).

**Pay‑off.** Readers find both names; semantics untouched.

#### F.15:15.3 - Tighten a Bridge (low-CL overlap → equivalence)

**Slice.** Bridge β between ⟨OWL\:subclass⟩ and ⟨FCA\:order‑edge⟩ was *overlap, CL=2*. New formal result proves equivalence in the covered fragment.

**Fire.**
E10 (**no drift to identity**): to move from overlap→≡, present a **new witness set** (fragment constraints).
S12 (**bridge explicit**): update β(kind=≡, CL=3) with precise scope/loss (“only within acyclic concept lattices with…”)

**Pay‑off.** Equivalence is **scoped and auditable**, not hand‑waved.

#### F.15:15.4 - Window misuse detected

**Slice.** Team proposes *PeakHoursAvailabilityStatus* as a new Status type.

**Fire.**
S14/E11 (**window honesty**): reject new type; define a **window** for *peak hours* on `AvailabilityStatus`.

**Pay‑off.** No type explosion; the evaluation logic in F.12 stays uniform.

