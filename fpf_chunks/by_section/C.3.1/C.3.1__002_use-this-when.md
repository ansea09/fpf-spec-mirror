---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__002_use-this-when.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:0 — Use This When"
line_start: 44772
line_end: 44785
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "A.8"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "U.SubkindOf direct relation"
  - "assertion episteme"
  - "local kind"
  - "partial order"
  - "relation occurrence"
  - "relation-obtaining predicate"
---

### C.3.1:0 - Use This When

Use this pattern when one typed-reasoning use needs a context-local kind, a subkind order, or a decision about whether the same local kind continues across editions of its declaration.

**What goes wrong if missed.** `U.SubkindOf` starts carrying dependency, construction, scope, public kind admission, or extension-table maintenance. A changed declaration is mistaken either for a new kind automatically or for a harmless rewrite automatically, and old classifications are silently reinterpreted.

**What this buys.** The user gets a small local partial order, a judgment-level monotonicity law, and an explicit kind-continuity decision while durable U-kind admission, classification, declaration identity, and cross-context bridging stay with their own governors.

**Primary EntityOfConcern.** One context-local `U.Kind` identity, its bounded context and local identity basis, and any `U.SubkindOf` order interpreted through the exact `U.ReferenceScheme` named by the aligned declaration editions.

**First useful move.** Write the ordinary order claim first: `CoolingPumpKind is a subkind of PumpKind in the Plant-7 bounded context, interpreted through PlantScheme-7.` Then identify the declaration editions used to evaluate candidates and test whether the order is monotone for the same candidate and slice.

**Not this pattern when.** Use C.3.2 for the declaration, one candidate classification, or an extension representation; C.3.3 for use across contexts; and `E.24.UK` when a local kind is proposed as a durable public FPF U-kind.

