---
chunk_kind: "child"
pattern_id: "F.16"
pattern_title: "Worked‑Example Template (Cross‑Domain)"
section_id: "F.16:8"
section_title: "Worked micro‑example (didactic)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.16/F.16__009_worked-micro-example-didactic.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "F.16 — Worked‑Example Template (Cross‑Domain)"
  - "F.16:8 — Worked micro‑example (didactic)"
line_start: 96364
line_end: 96377
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

### F.16:8 - Worked micro‑example (didactic)

> **Title.** *Alarms Should Not Satisfy Uptime*
> **Claim.** An **alarm‑only Execution (IEC)** cannot satisfy the **SLO (ITIL)** because **observation (SOSA)** windows exclude time in “alarm state.”

**Contexts.** IEC 61131‑3 (run), SOSA/SSN (run), ITIL 4 (design).
**SenseCells.** ⟨IEC\:execution‑task⟩, ⟨SOSA\:observation⟩, ⟨ITIL\:SLO⟩.
**Row ρ.** { ⟨ITIL\:uptime‑SLO⟩ ↔ ⟨SOSA\:observed‑availability⟩ } — comparable magnitudes in the *calendar‑month* window.
**Bridge β.** ⟨IEC\:alarm‑state⟩ **narrower‑than** ⟨SOSA\:observation‑qualifier⟩, **CL=2**, *loss:* SOSA does not prescribe plant‑specific alarm semantics.
**Role-Description hooks.** `AvailabilityStatus` → ⟨ITIL\:SLO⟩; `EvidenceObservation` → ⟨SOSA\:observation⟩.
**Window.** *Calendar month, business‑hours*, exclusion: *alarm‑state intervals*.
**Micro‑narrative (4 lines).** A **task (IEC)** runs; when the plant is in **alarm state**, **observations (SOSA)** are flagged and **excluded** from the availability window. We then compare the remaining interval to the **SLO (ITIL)** via row ρ. The Bridge β clarifies why the flag is a **qualifier** in SOSA, not a Status type in ITIL.
**Harness pings.** *S‑Row‑Cross*, *S‑RoleDescr‑SingleCell*, *S‑Window*, *S‑TemporalHonesty*.

