---
chunk_kind: "child"
pattern_id: "C.3"
pattern_title: "Kinds, Intent and Extent, and Typed Reasoning"
section_id: "C.3:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3/C.3__007_solution.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.3 — Kinds, Intent and Extent, and Typed Reasoning"
  - "C.3:5 — Solution"
line_start: 44055
line_end: 44068
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.22.CGUS"
  - "A.6.0"
  - "A.7.1"
  - "A.8"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
  - "F.18"
  - "F.8"
  - "F.9"
keywords:
  - "KindBridge"
  - "SubkindOf"
  - "bounded-context local kind"
  - "effective ReferenceScheme"
  - "intent-bearing KindSignature"
  - "optional slice-indexed extension"
  - "three-valued candidate judgment"
---

### C.3:5 - Solution

Use the lightest object that answers the current typed-reasoning question.

1. **Recover the local kind.** Name its bounded context and the local identity basis by which later claims can refer to the same kind. Do not store the current use, claim scope, or effective `U.ReferenceScheme` on the kind. A local `U.Kind` is not automatically a durable FPF U-kind.
2. **Use C.3.1 for order and continuity.** `U.SubkindOf` is a partial order over local kinds. C.3.1 also decides whether the same local kind continues when a declaration edition changes.
3. **Use C.3.2 for declaration and judgment.** A repeated criterion may justify a `KindSignature` whose claim content pins the effective `U.ReferenceScheme`; one application judges an exact candidate against one exact edition in one exact slice.
4. **Let direct features decide.** Direct qualities, relations, constructive grounding, or other governed candidate features make the criterion hold or fail. Measurements, observations, schemas, sources, and evidence support claims about those features; they do not constitute membership.
5. **Keep three results.** A satisfied criterion gives `true`; a known failed criterion gives `false`; missing evidence, an unavailable declared dependency, or an out-of-domain candidate gives `unknown`. A guard may decline use on `unknown` without changing that judgment to `false`.
6. **Materialize an extension only for use.** A query, quantification, comparison, or review may need `KindExtension(k, slice)`. The representation contains the true candidates for the fixed signature edition and slice; notation, rows, or set membership do not create an ontic collection or classification relation.
7. **Keep scope, formality, and work separate.** Formality characterizes the declaration episteme. Scope belongs to claims or capabilities. `U.Work` is the admitted U-kind; `W : U.Work` is one independently grounded, world-side, dated 4D work occurrence; a plan, log, card, field bundle, or database row about W is a separate episteme. No kind symbol or record occupies an individual-occurrence position.

Typed reasoning composes with F-G-R and USM in this order: recover typed compatibility and the exact judgment; separately check claim-scope coverage; then apply evidence, assurance, freshness, and bridge consequences when the receiving use requires them.

