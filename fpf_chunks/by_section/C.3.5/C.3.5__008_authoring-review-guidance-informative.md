---
chunk_kind: "child"
pattern_id: "C.3.5"
pattern_title: "KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
section_id: "C.3.5:7"
section_title: "Authoring & Review Guidance (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.5/C.3.5__008_authoring-review-guidance-informative.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.3.5 — KindAT — Intentional Abstraction Facet for Kinds (K0…K3)"
  - "C.3.5:7 — Authoring & Review Guidance (informative)"
line_start: 39386
line_end: 39402
dependencies:
  - "C.3.1"
keywords:
  - "K0-K3"
  - "KindAT"
  - "abstraction tier"
  - "informative facet"
  - "planning"
---

### C.3.5:7 - Authoring & Review Guidance (informative)

#### C.3.5:7.1 - How to tag (fast rubric)

* If the card lists **concrete items/cohorts**, tag **K0**.
* If the card defines **behavioral obligations** in prose/templates but few global invariants, tag **K1**.
* If the card states **predicates/invariants** and participates in a **subkind lattice**, tag **K2**.
* If the card explicitly reasons **up to isomorphism**, tag **K3**.

#### C.3.5:7.2 - Review checklist (5 minutes)

1. Is the **carrier** a **`U.Kind`** (not a claim)?
2. Does the **tag** match the **signature** (intent)?
3. Are **ΔF**/**ΔR** implications noted for planning (not gating)?
4. Any **RoleMasks** that should be promoted to subkinds (K2 hygiene)?
5. Any **Cross‑context reuse** that suggests **bridge style** (pattern/type/iso)?

