---
chunk_kind: "child"
pattern_id: "F.0.1"
pattern_title: "Contextual Lexicon Principles"
section_id: "F.0.1:3"
section_title: "Minimal Conceptual Objects (conceptual, notationally neutral)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.0.1/F.0.1__004_minimal-conceptual-objects-conceptual-notationally-neutral.md"
commit_sha: "308edacfa2bdb2c60d07e4e10c0deb1f260a6a31"
heading_path:
  - "F.0.1 — Contextual Lexicon Principles"
  - "F.0.1:3 — Minimal Conceptual Objects (conceptual, notationally neutral)"
line_start: 88190
line_end: 88218
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.4"
  - "A.7"
  - "A.8"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "U.BoundedContext"
  - "bridge"
  - "congruence"
  - "context"
  - "lexicon"
  - "local meaning"
  - "semantic boundary"
---

### F.0.1:3 - Minimal Conceptual Objects (conceptual, notationally neutral)

> These conceptual objects are **thought‑objects**; they specify **what must exist conceptually**, not how it is stored.

#### F.0.1:3.1 - **Context Card** (for each `U.BoundedContext`)

A terse descriptor used in the **Context Map** (F.1):

* `id` (stable local handle) - `title` - `edition/year`
* `family` (discipline family; informal) - `scope gist`
* `timeStance?` (`design` / `run`, if inherent)
* `trip‑wires` (few lexical caveats that often mislead, e.g., “*process*≠thermo process”)

#### F.0.1:3.2 - **SenseCell** (unit of local meaning, inside one context)

* `label.tech` / `label.plain` (two registers)
* `gloss` (minimal generality, Context‑true)
* `notes?` (warnings, edition shifts)
* **No** behaviour/deontics/equations (C‑6)

> **Where it comes from.** F.2 describes how SenseCells can be *derived* from local term evidence; F.0.1 only **requires** that local meaning be expressible as a SenseCell.

#### F.0.1:3.3 - **Alignment Bridge** (between SenseCells from different Contexts)

* `left: SenseCell⟨-@A⟩`, `right: SenseCell⟨-@B⟩`
* `relation` (e.g., *equivalent‑under‑assumptions*, *overlaps*, *broader‑than*)
* `CL` (Congruence Level; feeds B.3 Trust & Assurance)
* `loss/fit` (explicit statement of what is lost or assumed)

