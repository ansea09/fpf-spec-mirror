---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
section_id: "C.3.4:6"
section_title: "Norms and Invariants"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__008_norms-and-invariants.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "C.3.4 — KindUseAdaptationDeclaration — Contextual Adaptation of Kinds without Cloning"
  - "C.3.4:6 — Norms and Invariants"
line_start: 46131
line_end: 46160
dependencies:
  - "A.2.6"
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
  - "F.9"
keywords:
---

### C.3.4:6 - Norms and Invariants

#### C.3.4:6.1 - Definition and Shape

**KUA-01 (Definition).** A `KindUseAdaptationDeclaration` SHALL be a named, versioned C.2.1 declaration episteme with exact base kind as EntityOfConcern, effective scheme, pinned base signature, receiving use, adaptation type, candidate constraints, vocabulary bindings, applicability, dependencies, intended guard use, and separate scope expectations. Its formality characterizes the episteme.

**KUA-02 (Not a new kind).** A declaration MUST NOT introduce a kind or subkind fact. Stable refinement requires an independently recovered kind and C.3.1 obtaining test.

**KUA-03 (Admissibility before judgment).** Fixed candidate, kind, base-signature edition, adaptation-declaration edition, and slice first yield `admissible` or `not-applicable`. Only an admissible request yields `true`, `false`, or `unknown`; implicit `latest` and guard-result coercion are forbidden.

**KUA-04 (Adaptation type).** A vocabulary declaration preserves the base judgment. Constraint and composite declarations use governed candidate conditions: any known `false` gives `false`, all known `true` gives `true`, and unresolved required facts give `unknown`.

#### C.3.4:6.2 - Separation of Channels

**KUA-05 (Scope versus candidate).** Conditions of the candidate may enter the adaptation judgment. Claim- or Work-scope conditions remain under A.2.6. A declaration may cite both, but a guard routes them separately.

**KUA-06 (Guard use).** A guard MAY designate a declaration only when its exact edition, base signature, dependencies, applicability, and candidate conditions are recoverable. It checks admissibility before the judgment and makes its use decision separately.

#### C.3.4:6.3 - Stable Refinement and Catalog Representation

**KUA-07 (Stable refinement).** Broad reuse triggers a review for another kind. If that kind and an obtaining subkind fact are established, retain the adaptation declaration only for any remaining local use or retire it. Declaration reuse, catalog action, or labeling performs no kind admission and establishes no subkind fact.

**KUA-08 (Addressability).** Every guard-addressable adaptation declaration resolves to its exact edition, base signature, dependencies, applicability, and intended use. A correspondence declaration also resolves its source declaration as EntityOfConcern, target declaration, direction, deterministic rule, effective scheme, definedness, and loss. A catalog represents those references; it is neither the declaration episteme nor ontology, and consolidation does not merge kind identities.

#### C.3.4:6.4 - Cross-local Use

**KUA-09 (Identity check before bridge).** On a locality change, first compare exact base-kind definitions. Same-kind reuse needs no `KindBridge` but still uses the receiving declaration and a fresh judgment. Distinct-kind use establishes a `KindBridge` only when its directional correspondence predicate obtains. Differing adaptation constraints or bindings may additionally require an exact correspondence declaration. Source judgments are never copied as receiving truth; justified bridge consequences affect R only.

**KUA-10 (Definedness and fail-closed use).** Outside adaptation applicability, return `not-applicable` and form no judgment. For an admissible request with an unavailable dependency, return `unknown`. Outside correspondence definedness, the guard declines that cross-local use without rewriting an independently evaluated receiving result.

