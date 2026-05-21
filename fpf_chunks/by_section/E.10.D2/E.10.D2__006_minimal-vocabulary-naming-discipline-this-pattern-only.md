---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:5"
section_title: "Minimal vocabulary & naming discipline (this pattern only)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__006_minimal-vocabulary-naming-discipline-this-pattern-only.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:5 — Minimal vocabulary & naming discipline (this pattern only)"
line_start: 52706
line_end: 52740
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

### E.10.D2:5 - Minimal vocabulary & naming discipline (this pattern only)

**Core trio (per intensional `U.T`).**

* **`U.T` — the Intension.**
  Kernel object (e.g., `U.Role`, `U.Method`, `U.PromiseContent`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *Never* a document, *never* an event, *never* a file.

* **`U.TDescription(@Context)` — the Description Episteme.**
  Context‑local characterisation of `U.T`: Tech/Plain labels, gloss, notes; for roles, may **characterise** with an `U.RCS` (characteristics/traits), an `U.RSG` (states/transitions), and **state conformance checklists** (per state). *Readable; precise; not yet a set of testable “shall”s.*

* **`U.TSpec(@Context)` — the Specification Episteme.**
  Context‑local, **testable** invariant set for `U.T`, explicitly **bound to an acceptance harness** (SCR/RSCR matrices per F.15). Use **–Spec** only through the Spec‑gate (Sec. 4.2).

**Suffix rules.**

* Use **`…Description`** by default (M‑mode or F‑mode without harness).
* Use **`…Spec`** *only* when **all** Spec‑gate conditions (Sec. 4.2) hold.
* No alternative suffixes (“Profile”, “Definition”, “Guide”) inside the Core; such epistemes live in pedagogy/tooling layers, not in the I/D/S discipline.

**Naming morphology (recap of F.5 as it applies here).**

* Two registers: **Tech** and **Plain** labels on every Description/Spec.
* Roles use **count nouns** (e.g., *Operator*); states use **state nouns** (e.g., *Approved*).
* Statuses over knowledge (e.g., Evidence/Requirement) are **not** role states; they name **roles over Epistemes** (F‑R family), not nodes in `U.RSG`.

**Context anchoring.**
Every Description/Spec is **local to** a `U.BoundedContext` (E.10.D1). Phrases in the episteme must read correctly once prefixed by the Context name (e.g., “(ITIL4) Acceptance criteria …”).

**Carriers.**
`U.Carrier` holds **encodings** of a Description/Spec; the Episteme’s identity is **not** the file. *Never* say “the role contains the checklist in the PDF”; say “the **RoleDescription** characterises the role with checklists; this **carrier** encodes them.”

**Time stance.**
Descriptions/Specs must declare DesignRunTag when inherent (e.g., RoleDescription is design‑time; state attestation via `U.Evaluation` is run‑time).

