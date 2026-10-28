---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge and CL^k — Correspondence between Distinct Kinds"
section_id: "C.3.3:8"
section_title: "Authoring, Review & Rating Guidance (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__009_authoring-review-rating-guidance-informative.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.3.3 — KindBridge and CL^k — Correspondence between Distinct Kinds"
  - "C.3.3:8 — Authoring, Review & Rating Guidance (informative)"
line_start: 55006
line_end: 55031
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
---

### C.3.3:8 - Authoring, Review & Rating Guidance (informative)

#### C.3.3:8.1 - Authoring a KindBridge assertion

* **Compare identity before authoring a bridge.** For a changed locality, source, team, spelling, or scheme, first repeat the kind-definition comparison under C.3.1. Stop without a bridge when the same kind continues.
* **Start narrow and honest.** For two distinct kinds, declare only the directional correspondence and subkind facts the receiving use actually relies on; mark any required but unsettled order result unknown.
* **Prefer an existing suitable target kind.** If the target already has a suitable kind and declaration edition, relate that kind directly. If a new target declaration is required, author it separately before asserting bridge obtaining; list what the mapping predicate preserves, relaxes, or drops.
* **Write loss notes in plain language.** Example: “EV vs ICE subkinds collapsed; battery‑health invariants dropped.”
* **Fix the definedness area.** Bind to target Standards/versions and any environment selectors essential to classification.
* **Assign `CL^k` from exemplars.** Calibrate on concrete counter‑examples and preserved properties; resist optimistic ratings.

#### C.3.3:8.2 - Review prompts

1. **Identity checked first?** Same kind reused without a bridge, or two distinct kinds and the obtaining correspondence shown? Add Scope or F.9 relations only when the receiving use consumes them.
2. **Order claims honest?** Any `⊑` inversions? Collapses disclosed?
3. **`CL^k` plausible?** Based on preserved properties, not name similarity?
4. **Loss consequences clear?** Do they change the justified inference, require more basis or leave the intended use adequate?
5. **Definedness area clear?** Outside it, does the guard decline this bridge use while preserving the independent classification result?
6. **Reliance consequence justified?** Any numerical change to R needs its receiving model; F and G remain unchanged.

#### C.3.3:8.3 - Rating `CL^k` (rules of thumb)

* **High `CL^k`**: signature equivalence or **up‑to‑iso**; `⊑` fragment preserved; only cosmetic losses.
* **Medium `CL^k`**: some invariants relaxed or lost; selected subkinds collapsed; the source-order facts required by the use remain preserved.
* **Low `CL^k`**: name-only correspondences; properties diverge; order not preserved. Establish that the KB-01 correspondence predicate holds before bridge use, even for a name-only match. Determine which inferences remain justified; narrow the use or repair the correspondence if a required distinction is lost. A numerical R penalty requires the receiving model under C.2.2/B.3.

