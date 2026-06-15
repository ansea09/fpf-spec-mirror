---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
section_id: "F.8:1"
section_title: "Intent & applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__002_intent-applicability.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias)"
  - "F.8:1 — Intent & applicability"
line_start: 74331
line_end: 74342
dependencies:
  - "A.11"
  - "A.7"
  - "A.8"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "decision lattice"
  - "minting new types"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:1 - Intent & applicability

**Intent.** Provide a **minimal, conceptual decision lattice** that answers, for any modelling need:

> “Do I **reuse** an existing label, add an **alias**, reference a **Concept‑Set row**, define a **Role Description**, or mint a **new U.Type**?”

The lattice enforces **locality of meaning** (Contexts), **senseFamily separation** (A.7), and **parsimony** (A.11) while remaining didactically simple.

**Applicability.** Use whenever a new name seems “needed” in any FPF pattern thread (**Role Assignment & Enactment**, Sys-CAL, KD-CAL, Kind-CAL, Method-CAL, LCA-CAL…).

**Non‑goals.** No workflows, no roles, no storage. This is **thinking discipline**, not process guidance.

