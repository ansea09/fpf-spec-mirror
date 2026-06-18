---
chunk_kind: "parent"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/C.3.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
line_start: 38439
line_end: 38537
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.8"
  - "C.2.3"
  - "C.3.1"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "classification"
  - "extension"
  - "intension"
  - "kind"
  - "subkind"
  - "type"
  - "typed reasoning"
  - "vocabulary"
---

## C.3 - Kinds, Intent and Extent, and Typed Reasoning

> **Type:** Typed reasoning discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3:0 - Use This When

Use this pattern when a claim needs to say what kind of thing it quantifies over, which instances belong to that kind in a context slice, how intent and extent are related, and how typed compatibility affects composition.

Typical moments:

- two claims may be about different kinds of entities;
- scope is being widened by abstract wording instead of supported slices;
- a local kind needs membership, extension, bridge, or subkind reasoning;
- a `U.Kind` or `U.SubkindOf` occurrence must be kept distinct from durable FPF U-kind admission.

**Primary EntityOfConcern.** The EntityOfConcern is the typed reasoning claim: kind, intent, extent, membership, and typed compatibility in a bounded context.

**First useful move.** Ask whether the current question is C.3 typed reasoning or U-kind admission. If it is U-kind admission, use `E.24.UK`. If it is claim quantification, stay in C.3.

When a source ontology, schema, standard, class hierarchy, or top-level ontology supplies type, class, category, or subtype wording, C.3 may govern the local typed-reasoning claim. Use `E.24.UK` only when the source construct is being proposed as a public durable FPF U-kind or as part of an E.24 ontic settlement.

### C.3:1 - Problem Frame

Across contexts, "type" can mean ontology class, programming type, schema shape, category, source label, or public FPF U-kind. C.3 provides a smaller discipline: `U.Kind` is a context-local value used for typed reasoning about claims. It is not automatically a durable FPF U-kind and it does not by itself admit a `U.*` structural name. A C.3 `U.Kind` may be backed by construction, recognition, membership, or extent criteria in its bounded context, but that basis remains local typed-reasoning law until E.24.UK admits durable FPF kindhood.

### C.3:2 - Core Split

Keep four objects separate:

| Object | Meaning |
| --- | --- |
| `U.Kind` | Context-local kind value naming what a claim quantifies over. |
| Intent | The kind's signature, predicates, invariants, and formality-bearing definition. |
| Extent | The instances belonging to the kind in one context slice. |
| Scope | Where a claim holds; this belongs to claims or capabilities, not to kinds. |

Typed reasoning composes with F-G-R and USM by order: first typed compatibility, then scope coverage, then assurance and freshness penalties where relevant.

### C.3:3 - Solution

Use C.3 when the current claim is about typed compatibility, membership, kind intent, kind extent, or cross-context kind bridges.

Do not use C.3 to admit durable U-kind names. That decision belongs to `E.24.UK`, with `A.8`, `A.11`, `F.8`, and `F.18` when kernel-level or public naming force is current.

Normative decisions:

1. `U.Kind` is context-local and intent-bearing.
2. `U.SubkindOf` is a partial-order relation over C.3 `U.Kind` values.
3. Kind intent and kind extent are different claims and may have different evidence.
4. Kinds do not carry scope; claim scope and work scope remain USM values.
5. Cross-context kind reuse requires bridge discipline and loss notes.
6. Public `U.*` spelling in a heading, title, filename, or ToC row does not follow from C.3 typed reasoning.

### C.3:4 - Relations To E.24.UK

Use this decision split:

| Current question | Governing pattern |
| --- | --- |
| What kind of thing does this claim quantify over? | `C.3`, `C.3.1`, and dependent C.3 patterns |
| Is this local kind a subkind of that local kind? | `C.3.1` |
| Does this context-local kind deserve a durable public FPF `U.*` name? | `E.24.UK`, then `F.8` and `F.5` or `F.18` |
| Is the candidate universal enough for kernel-level status? | `A.8` after `E.24.UK` |
| Can existing ontology express it without a new kind? | `A.11` after object recovery |

### C.3:5 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | The text distinguishes C.3 `U.Kind` from durable FPF U-kind admission. |
| `CC-C3-2` | Intent, extent, and scope are not collapsed. |
| `CC-C3-3` | `U.SubkindOf` is used only as a partial-order relation over C.3 kinds unless another governing pattern explicitly says otherwise. |
| `CC-C3-4` | Public `U.*` spelling, structural headings, and new U-kind pressure are governed by `E.24.UK` before C.3 typed-reasoning values are published as public FPF names. |
| `CC-C3-5` | Cross-context reuse uses bridge discipline rather than pretending that same wording gives sameness. |

### C.3:5.1 - Detail Map

C.3 is the head pattern for typed reasoning. It should not replay all C.3 mechanics, but it must leave the detailed loci visible.

| Needed detail | Governing locus | Content carried there |
| --- | --- | --- |
| Intent and membership | `C.3.2` | `KindSignature`, formality, extension, membership, definedness, and the rule that kinds carry no claim scope. |
| Cross-context kind reuse | `C.3.3` | KindBridge, the two-bridge rule for kind and scope, loss notes, and target-context membership evaluation. |
| Local adaptation without cloning a kind | `C.3.4` | RoleMask, mask registration, mask adapters, and the boundary between masks and subkinds. |
| Abstraction facet | `C.3.5` | KindAT levels, use limits, and catalog expectations. |
| Typed guards and applied examples | `C.3.A` | Guard macros, regulatory categories, evidence and assurance use, method and work compatibility, and worked cross-context cases. |

If a host package contains C.3 without these neighboring loci, do not treat the compact head pattern as full carry-through. Bring the needed C.3 subpattern into the source set or cite the monolith section by value.

### C.3:6 - Relations

- **Builds on:** USM scope discipline, F-G-R, C.2.3 formality, and bridge patterns.
- **Coordinates with:** `C.3.1` through `C.3.5`, `C.3.A`, `E.24.UK`, `A.8`, `A.11`, `F.8`, and `F.5`.
- **Does not replace:** ontic settlement in `E.24`, U-kind admission in `E.24.UK`, or naming in Part F.

### C.3:End

