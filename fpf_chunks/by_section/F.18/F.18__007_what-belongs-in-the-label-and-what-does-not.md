---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local‑First Unification Naming Protocol"
section_id: "F.18:6"
section_title: "What belongs in the label—and what does not"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__007_what-belongs-in-the-label-and-what-does-not.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "F.18 — Local‑First Unification Naming Protocol"
  - "F.18:6 — What belongs in the label—and what does not"
line_start: 66816
line_end: 66833
dependencies:
  - "A.19.SUPPORT-VIEW"
  - "A.6.P"
  - "E.10"
  - "E.10.SEMIO"
  - "F.0.1"
  - "F.1-F.17"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:6 - What *belongs* in the label—and what does not

**Belongs (keeps the label clean and durable):**

* The **core head word** that names the thing *(the **Kind** is recorded on the Card; the string need not encode it)* (e.g., “Pump”, “Standard”, “Requirement”, “Surgeon”, “Cooling”).
* A **purpose qualifier** if it is essential to the local sense and stable across editions (e.g., “Cooling” vs “Fuel”).
* A **scope qualifier** only if it is part of the *meaning* rather than the current plan (“Surgical Ward” rather than dates or batch numbers).

**Does not belong (move elsewhere):**

* **Numbers and thresholds** (put on steps, capabilities, acceptance clauses).
* **States** (use Role State Graphs and checklists).
* **Temporal windows** (work plans and history).
* **Organisational authorisations** (speech acts and assignments).
* **Imported acronyms** from other Contexts (use Bridges with loss notes instead).

**Quick litmus for authors.** If removing a number, date, or state *does not* change the *meaning* of the thing, it should **not** be in the label.

