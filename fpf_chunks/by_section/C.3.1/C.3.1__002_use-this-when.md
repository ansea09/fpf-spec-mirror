---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__002_use-this-when.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:0 — Use This When"
line_start: 40555
line_end: 40571
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.8"
  - "C.2.3"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "kind"
  - "partial order"
  - "subkind"
  - "type hierarchy"
---

### C.3.1:0 - Use This When

Use this pattern when a context needs a minimal kind value and subkind order for typed claim reasoning.

**What goes wrong if missed.** A local kind order is confused with durable FPF U-kind governance: subkind links start standing in for construction, ontic admission, naming, scope, or dependency relations.

**What this buys.** The user gets a small, inspectable typed-reasoning core: `U.Kind` values stay context-local, `U.SubkindOf` remains a partial order, and durable U-kind admission stays with `E.24.UK`.

Typical moments:

- a claim needs a context-local kind value for what it quantifies over;
- a local kind order is needed for typed compatibility;
- `U.SubkindOf` is being mistaken for dependent durable U-kind relation;
- a source says "type" or "kind" and the author must decide whether the current use is C.3 typed reasoning or E.24.UK U-kind admission.

**Primary EntityOfConcern.** The EntityOfConcern is the C.3.1 core relation among context-local `U.Kind` values and the `U.SubkindOf` partial order.

