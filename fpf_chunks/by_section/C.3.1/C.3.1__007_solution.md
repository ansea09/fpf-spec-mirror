---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:5"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__007_solution.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:5 — Solution"
line_start: 43889
line_end: 43900
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

### C.3.1:5 - Solution

1. **Bound the typed-reasoning use.** Name the local kind values, exact effective `U.ReferenceScheme` edition, and the applicability in which the order is asserted. Do not infer a public `U.*` name.
2. **State the direct order relation.** Use `U.SubkindOf` only for an obtaining relation whose narrower-kind and broader-kind participants satisfy `SubkindOfObtains` under that scheme. Keep the predicate, any `R_sub` occurrence designator, and any C.2.1 assertion episteme separate.
3. **Keep a partial order over obtaining facts.** Reflexivity, transitivity, and antisymmetry constrain the obtaining `U.SubkindOf` relations among local kind values; they do not make a diagram edge or affirmative assertion true by form.
4. **Test the obtaining predicate over judgments.** For the aligned signature editions, if both C.3.2 judgments are defined for the same candidate and context slice and the judgment for `k1` is `true`, then the judgment for `k2` must be `true`. A universal proof or adequate domain basis establishes the implication; `unknown` remains non-settlement.
5. **Diagnose counterexamples at their owner.** A counterexample indicates that the proposed relation does not obtain, that the signature editions are incompatible, or that a context bridge is undeclared. Do not repair it by silently adding or deleting a row in `KindExtension`.
6. **Separate signature change from kind continuity.** A changed criterion, evaluation domain, `EntityOfConcern` referent, or effective reference scheme creates another `U.Signature` episteme edition under A.6.0 and C.2.1. C.3.1 then decides independently whether the same local kind continues.
7. **Record the continuity consequence.** If the local identity basis is preserved, the same kind may continue while every classification still cites the edition actually used; the new edition does not retroactively rewrite old judgments. If the identity basis is not preserved, identify a different local kind and state any genuinely obtaining `U.SubkindOf` relation or C.3.3 bridge separately.
8. **Do not infer change from the extension alone.** A changed candidate state or later `U.ContextSlice` can change `KindExtension(k, slice)` without changing the signature, kind, or a still-obtaining subkind relation.
9. **Keep scope and Work outside the kind.** A kind carries no claim scope. `U.Work` is the admitted U-kind, whereas `W : U.Work` is one independently grounded, world-side, dated 4D work occurrence; a plan, log, card, or row about W is a separate episteme and does not establish either W or a local subkind classification.

