---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Part G Core Invariants"
section_id: "G.Core:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__013_relations.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "G.Core — Part G Core Invariants"
  - "G.Core:12 — Relations"
line_start: 101155
line_end: 101179
dependencies:
  - "A.15.3"
  - "A.19"
  - "A.19.CHR"
  - "A.6.7"
  - "E.10"
  - "E.19"
  - "E.8"
  - "G.0"
  - "G.13"
  - "G.Core"
keywords:
  - "Default Governing Definition Index"
  - "ID continuity"
  - "Part‑G invariants"
  - "RSCR trigger kinds"
  - "core linkage"
  - "delegation-first core"
---

### G.Core:12 - Relations

* **Builds on:**

  * `E.8` pattern template and section discipline
  * `E.10` lexical/ontological rules (strict distinction; twin naming; kind‑suffix discipline)
* `E.18` CrossingBundle (crossing visibility bundle)
  * `E.19` conformance discipline
  * `A.6.7` SuiteObligations + suite protocol pins (delegation support)
  * `A.15.3` SlotFillingsPlanItem (planned baseline anchor)
  * `A.19` CN‑Spec governance card
  * `G.0` CG‑Spec legality gate
  * `A.19.CHR` CHR suite boundary and "governance cards and legality gates are cited as pins, not copied locally" discipline
  * `C.23` SoS‑LOG (tri‑state branches; sandbox/probe‑only)
  * `F.17` UTS (identifier registry; alias/deprecation discipline)
  * `F.15` RSCR (regression/conformance loop)

* **Used by:**

  * `G.0…G.13` patterns (each adds `Builds on: G.Core`, linkage section, CoreRef CC item)

* **Constrains:**

  * Part‑G authoring: no shadow specs, no silent scalarization, tri‑state guards, penalties routing, typed RSCR causes, defaults with one governing definition, and ID‑continuity refactors.

