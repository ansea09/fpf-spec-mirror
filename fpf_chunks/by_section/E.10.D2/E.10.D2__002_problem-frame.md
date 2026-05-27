---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__002_problem-frame.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:1 — Problem frame"
line_start: 56515
line_end: 56524
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

### E.10.D2:1 - Problem frame

**Intent.** Prevent perennial confusions such as “the role contains the checklist” or “the method is the document.” Establish a universal discipline so that:

* **Intensions** (e.g., `U.Role`, `U.Method`) remain I/D/S layer‑pure and context‑agnostic entities in the kernel.
* **Descriptions** (KUs) capture human‑readable, **Context‑local** semantics (labels, glosses, characterisations, state graphs, checklists).
* **Specifications** (KUs) exist **only** when there are verifiable invariants, an acceptance harness, **and a declared Formality F adequate for checkability (C.2.3; default F ≥ F4)**, making claims testable.

**Applicability.** Whenever an FPF text introduces or uses an intensional `U.Type` (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`, `U.RoleEnactment`) in any part (A–H).

