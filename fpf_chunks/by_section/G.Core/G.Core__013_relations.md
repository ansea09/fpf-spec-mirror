---
chunk_kind: "child"
pattern_id: "G.Core"
pattern_title: "Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
section_id: "G.Core:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/G.Core/G.Core__013_relations.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "G.Core — Discipline SoTA Kit Invariants, Defaults and Refresh Triggers (Part G)"
  - "G.Core:12 — Relations"
line_start: 134866
line_end: 134890
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
  * `A.15.2` WorkPlan content for the edition/reference baseline; `A.15.3` only for applicable typed planned fillings
  * `A.19.CN` CN‑Spec governance card
  * `G.0` CG‑Spec legality gate
  * `A.19.CHR` CHR suite boundary and "governance cards and legality gates are cited as pins, not copied locally" discipline
  * `C.23` SoS‑LOG (tri‑state branches; sandbox/probe‑only)
  * `F.17` UTS (identifier registry; alias/deprecation discipline)
  * `F.15` static and regression conformance checks for unification slices

* **Used by:**

  * `G.0…G.13` patterns cite `G.Core` for the obligations they use (§4.2). A `Builds on: G.Core` entry can name that dependency. For checklist changes when a shared norm moves into `G.Core`, see §4.5.

* **Constrains:**

  * Part‑G authoring: no shadow specs, no silent scalarization, tri‑state guards, penalties routing, typed RSCR causes, defaults with one governing definition, and ID‑continuity refactors.

