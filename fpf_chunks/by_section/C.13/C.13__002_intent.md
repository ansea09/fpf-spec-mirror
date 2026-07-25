---
chunk_kind: "child"
pattern_id: "C.13"
pattern_title: "Constructional Mereology (Compose‑CAL)"
section_id: "C.13:1"
section_title: "Intent"
source_path: "FPF-Spec.md"
output_path: "by_section/C.13/C.13__002_intent.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.13 — Constructional Mereology (Compose‑CAL)"
  - "C.13:1 — Intent"
line_start: 46069
line_end: 46080
dependencies:
  - "A.14"
  - "B.3.5"
keywords:
  - "composition"
  - "extensional identity"
  - "mereology"
  - "part-whole"
  - "set"
  - "slice"
  - "sum"
---

### C.13:1 - Intent

Provide a single, generative calculus for part–whole structure so that **all** structural relations in FPF are *constructed* (not merely declared) from three primitives and thereby inherit extensional identity by design. The calculus is hidden from day‑to‑day users behind relation aliases; its artefacts are traces that witness how a whole arises from its parts.

Also known as *“Γₘ mereology”*, *“constructor‑based composition”*.

**Layer.** *calculus.*
**Depends on.** Kernel only (no upward imports).
**Consumed by.** CT2R‑LOG (B.3.5) Working‑Model alias logic and any FPF pattern that needs part–whole semantics. Compose‑CAL does **not** import alias definitions; it merely emits traces that others may reference.

Compose‑CAL introduces a **single construction operator Γₘ** with exactly three constructors—**sum**, **set**, **slice**—sufficient to build structural wholes, collections‑as‑wholes, and aspects **without** extending the Kernel’s type set. No “parallel” or “temporal slice” constructor is added. Every construction yields a **trace** that serves as the witness for structure. Human‑facing relations such as *ComponentOf*, *MemberOf*, *AspectOf* are defined elsewhere as **Working‑Model aliases** and are *grounded* in these traces; Compose‑CAL itself remains purely generative and extensional.

