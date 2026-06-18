---
chunk_kind: "parent"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/C.3.1.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
line_start: 38538
line_end: 38605
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

## C.3.1 - U.Kind and U.SubkindOf Core

> **Type:** Typed reasoning core pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3.1:0 - Use This When

Use this pattern when a context needs a minimal kind value and subkind order for typed claim reasoning.

Typical moments:

- a claim needs a context-local kind value for what it quantifies over;
- a local kind order is needed for typed compatibility;
- `U.SubkindOf` is being mistaken for dependent durable U-kind relation;
- a source says "type" or "kind" and the author must decide whether the current use is C.3 typed reasoning or E.24.UK U-kind admission.

**Primary EntityOfConcern.** The EntityOfConcern is the C.3.1 core relation among context-local `U.Kind` values and the `U.SubkindOf` partial order.

### C.3.1:1 - Problem Frame

C.3.1 gives FPF a small object for typed reasoning without importing a full ontology stack. `U.Kind` names a kind of thing in one context. `U.SubkindOf` orders such kinds. This is different from durable FPF U-kind admission. A C.3 `U.Kind` can later become part of a U-kind admission question, but it is not admitted merely by being a `U.Kind`.

### C.3.1:2 - Core Objects

| Object | Meaning |
| --- | --- |
| `U.Kind` | Context-local kind value used by claims for typed quantification. |
| `U.SubkindOf` | Partial-order relation over `U.Kind` values. |
| Kind identity | The local identity criterion that says when two kind refs in the same context name the same kind. |
| Parent and child links | Declared or computed `U.SubkindOf` links. |

### C.3.1:3 - Norms

1. `U.SubkindOf` is reflexive, transitive, and antisymmetric over `U.Kind` values.
2. A `U.Kind` carries no claim scope. Scope belongs to claims or capabilities under USM.
3. Intent and membership are governed by C.3.2, not by this core pattern.
4. Cross-context sameness or translation uses kind bridge discipline, not shared spelling.
5. `U.SubkindOf` is not the relation that makes a dependent durable U-kind under `E.24.UK`.
6. A structural `U.*` name that looks like a root FPF kind is governed by `E.24.UK`.

### C.3.1:4 - Decision Split

| Source pressure | C.3.1 disposition |
| --- | --- |
| "This claim ranges over cooling pumps." | Create or cite the context-local `U.Kind` for cooling pump. |
| "Cooling pump is a subkind of pump." | Declare `U.SubkindOf(CoolingPumpKind, PumpKind)` in the context. |
| "CoolingPump should become a public FPF U-kind." | Use `E.24.UK`, `A.11`, and `A.8` as needed. |
| "`U.WorkPlan` depends on `U.Work`." | Do not encode as `U.SubkindOf` unless C.3 typed reasoning actually claims a subkind order. Use the governing work or E.24.UK settlement. |

### C.3.1:5 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C31-1` | Every `U.Kind` use is context-local unless a bridge says otherwise. |
| `CC-C31-2` | Every `U.SubkindOf` use is a partial-order claim over `U.Kind` values. |
| `CC-C31-3` | Scope is not stored on the kind value. |
| `CC-C31-4` | Dependent durable U-kind relations are not modeled as `U.SubkindOf` by default. |
| `CC-C31-5` | U-kind admission and structural `U.*` repair are governed by `E.24.UK`; public naming pressure is handled by Part F after the governed value is recovered. |

### C.3.1:6 - Relations

- **Builds on:** `C.3`, USM, F-G-R, and C.2.3 formality.
- **Coordinates with:** `E.24.UK`, `A.8`, `A.11`, `F.8`, and `F.5`.
- **Does not replace:** C.3.2 intent and membership, C.3.3 bridges, or E.24-family U-kind governance.

### C.3.1:End

