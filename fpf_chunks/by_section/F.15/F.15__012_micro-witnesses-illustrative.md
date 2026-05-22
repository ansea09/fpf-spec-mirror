---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "SCR/RSCR Harness for Unification"
section_id: "F.15:11"
section_title: "Micro‑witnesses (illustrative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__012_micro-witnesses-illustrative.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "F.15 — SCR/RSCR Harness for Unification"
  - "F.15:11 — Micro‑witnesses (illustrative)"
line_start: 66646
line_end: 66658
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

### F.15:11 - Micro‑witnesses (illustrative)

**11.1 Activity vs Task (PROV‑O ↔ IEC 61131‑3).**
Contexts: `PROV‑O (run)`, `IEC 61131‑3 (run)`.
Local‑Senses: *activity(prov)*, *task(iec)*.
*Fire:* S7 (**Role Description** “Execution” points to **one SenseCell**), S12 (Bridge: **overlap**, CL=2, loss: *IEC task may be cyclic; PROV activity need not be periodic*), S13 (Contexts differ), S14 (Status windows for compliance later, not new types).

**11.2 Service Acceptance (ITIL 4 ↔ SOSA/SSN).**
Contexts: `ITIL 4 (design)`, `SOSA/SSN (run)`.
Row: **Service‑Availability** with cells ⟨ITIL\:SLO availability⟩, ⟨SOSA\:observation of uptime⟩.
*Fire:* S9 (row spans ≥2 Contexts), S12 (Bridge kind: *measure-for-target*, CL=3, loss: *sampling bias*), S16 (binding coherence), **S-RoleDesc-SingleCell**.


