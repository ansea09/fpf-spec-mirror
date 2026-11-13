---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
section_id: "E.20:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__010_consequences.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.20 — Mechanism Introduction Protocol: Introduce or Revise FPF Mechanisms"
  - "E.20:9 — Consequences"
line_start: 120864
line_end: 120876
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "alias docking"
  - "authoring protocol"
  - "declaration-local operation members"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "planned baseline"
  - "resolvable MechanismDefinitionRef"
  - "suite boundary"
  - "trigger triage"
  - "wiring"
---

### E.20:9 - Consequences

**Benefits**
* Mechanism introductions become **trainable and reviewable** because authors can apply the same rule to assign each changed item to its definition.
* Assigning each mechanism meaning to one subject pattern reduces drift. Its semantics stay with that definition.
* Keeps suites descriptive and the P2W planning-to-work boundary inspectable.
* Supports SoTA evolution without destabilizing kernel meaning.

**Costs**
* Introductions use more explicit assignment records (governing-definition map, PQG coverage).
* Some changes will be split into multiple governed edits, which takes additional authoring work.
* Kernel stability discipline can feel “slow” when a team wants a quick mutation.

