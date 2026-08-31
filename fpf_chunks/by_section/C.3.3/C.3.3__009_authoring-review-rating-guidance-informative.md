---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
section_id: "C.3.3:8"
section_title: "Authoring, Review & Rating Guidance (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__009_authoring-review-rating-guidance-informative.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "C.3.3 — KindBridge and CL^k — Cross-local Correspondence between Distinct Kinds"
  - "C.3.3:8 — Authoring, Review & Rating Guidance (informative)"
line_start: 45691
line_end: 45716
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

* **Compare identity before authoring a bridge.** A changed locality, source, team, spelling, or scheme first replays C.3.1. Stop without a bridge when the same kind continues.
* **Start narrow and honest.** For two distinct kinds, declare only the directional correspondence and subkind facts the receiving use actually relies on; mark the rest unknown.
* **Prefer independently identified target kinds.** If the target already has a suitable kind and declaration edition, relate that kind directly. If a new target declaration is required, author it separately before asserting bridge obtaining; list what the mapping predicate preserves, relaxes, or drops.
* **Write loss notes in plain language.** Example: “EV vs ICE subkinds collapsed; battery‑health invariants dropped.”
* **Fix the definedness area.** Bind to target Standards/versions and any environment selectors essential to classification.
* **Assign `CL^k` from exemplars.** Calibrate on concrete counter‑examples and preserved properties; resist optimistic ratings.

#### C.3.3:8.2 - Review playbook (10 minutes)

1. **Identity checked first?** Same kind reused without a bridge, or two distinct kinds and the obtaining correspondence shown? Add Scope or F.9 relations only when the receiving use consumes them.
2. **Order claims honest?** Any `⊑` inversions? Collapses disclosed?
3. **`CL^k` plausible?** Based on preserved properties, not name similarity?
4. **Loss notes present?** Will they force narrowing of Scope or extra tests?
5. **Definedness area clear?** Guard will **fail closed** outside it?
6. **Penalties wired to R?** No hidden tweaks to **F/G**?

#### C.3.3:8.3 - Rating `CL^k` (rules of thumb)

* **High `CL^k`**: signature equivalence or **up‑to‑iso**; `⊑` fragment preserved; only cosmetic losses.
* **Medium `CL^k`**: some invariants relaxed or lost; selected subkinds collapsed; order preserved on critical path.
* **Low `CL^k`**: name‑only correspondences; properties diverge; order not preserved. Expect significant **R** penalty and/or adapters.

