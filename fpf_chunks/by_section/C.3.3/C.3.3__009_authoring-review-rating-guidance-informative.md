---
chunk_kind: "child"
pattern_id: "C.3.3"
pattern_title: "KindBridge & CL^k — Cross‑context Mapping of Kinds"
section_id: "C.3.3:8"
section_title: "Authoring, Review & Rating Guidance (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.3/C.3.3__009_authoring-review-rating-guidance-informative.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.3.3 — KindBridge & CL^k — Cross‑context Mapping of Kinds"
  - "C.3.3:8 — Authoring, Review & Rating Guidance (informative)"
line_start: 45203
line_end: 45227
dependencies:
  - "A.2.6"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.2"
  - "C.3.1"
  - "C.3.2"
  - "F.9"
keywords:
  - "CL^k"
  - "KindBridge direct relation"
  - "R penalty"
  - "bridge assertion episteme"
  - "loss"
  - "target judgment"
---

### C.3.3:8 - Authoring, Review & Rating Guidance (informative)

#### C.3.3:8.1 - Authoring a KindBridge assertion

* **Start narrow & honest.** Declare only the kinds and `⊑` links you **actually preserve**; mark the rest **unknown**.
* **Prefer independently identified target kinds.** If the target already has a suitable kind and declaration edition, relate that kind directly. If a new target declaration is required, author it separately before asserting bridge obtaining; list what the mapping predicate preserves, relaxes, or drops.
* **Write loss notes in plain language.** Example: “EV vs ICE subkinds collapsed; battery‑health invariants dropped.”
* **Fix the definedness area.** Bind to target Standards/versions and any environment selectors essential to classification.
* **Assign `CL^k` from exemplars.** Calibrate on concrete counter‑examples and preserved properties; resist optimistic ratings.

#### C.3.3:8.2 - Review playbook (10 minutes)

1. **Two bridges present?** Scope Bridge **and** KindBridge?
2. **Order claims honest?** Any `⊑` inversions? Collapses disclosed?
3. **`CL^k` plausible?** Based on preserved properties, not name similarity?
4. **Loss notes present?** Will they force narrowing of Scope or extra tests?
5. **Definedness area clear?** Guard will **fail closed** outside it?
6. **Penalties wired to R?** No hidden tweaks to **F/G**?

#### C.3.3:8.3 - Rating `CL^k` (rules of thumb)

* **High `CL^k`**: signature equivalence or **up‑to‑iso**; `⊑` fragment preserved; only cosmetic losses.
* **Medium `CL^k`**: some invariants relaxed or lost; selected subkinds collapsed; order preserved on critical path.
* **Low `CL^k`**: name‑only correspondences; properties diverge; order not preserved. Expect significant **R** penalty and/or adapters.

