---
chunk_kind: "child"
pattern_id: "B.1.1"
pattern_title: "Dependency Graph & Proofs"
section_id: "B.1.1:7"
section_title: "Archetypal grounding (worked micro‑examples)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.1/B.1.1__008_archetypal-grounding-worked-micro-examples.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "B.1.1 — Dependency Graph & Proofs"
  - "B.1.1:7 — Archetypal grounding (worked micro‑examples)"
line_start: 28783
line_end: 28808
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.2"
  - "B.1.3"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
keywords:
  - "dependency graph"
  - "proofs"
  - "set"
  - "slice"
  - "structural aggregators"
  - "sum"
---

### B.1.1:7 - Archetypal grounding (worked micro‑examples)

> Each row is self‑contained and can be used as a template.

#### B.1.1:7.1 - U.System (assembly & production)

| Aspect           | Example                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Graph**        | `Motor ComponentOf Chassis`; `Harness ComponentOf Motor`; *(for method demo only, outside `D`)* `QC SerialStepOf Seal`; all nodes scope=`run`; BIC declares ports for power, data. |
| **Independence** | Two subassemblies: `{Chassis, Motor, Harness}` and `{Cabin}` with disjoint interfaces.                                                                     |
| **WLNK‑CUT**     | Tensile path through front mount + harness connector; weakest tensile rating caps assembly load rating.                                                    |
| **MONO‑AX**      | Improving mount alloy or connector strain relief cannot reduce system load rating.                                                                         |
| **IDEM‑WIT**     | Standalone chassis as singleton: Γ\_sys returns chassis unchanged.                                                                                        |
| **Routing**      | `SerialStepOf` belongs to Γ\_method; Γ\_sys ignores order and composes structure; Γ\_work separately composes energy/material costs through boundary ports. |

#### B.1.1:7.2 - U.Episteme (paper & dataset)

| Aspect           | Example                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Graph**        | `Lemma1 ConstituentOf ProofA`; `DatasetX MemberOf CorpusQ`; `ProofA ConstituentOf PaperP`; scope=`design`.                                            |
| **Independence** | Two argument branches that do not reuse premises: `{Lemma1 → ProofA}` and `{Background → Discussion}`.                                                |
| **WLNK‑CUT**     | The least supported premise in the entailment path to the main theorem.                                                                               |
| **MONO‑AX**      | Replacing a weak premise with a stronger one or raising CL of a mapping cannot reduce overall credibility.                                            |
| **IDEM‑WIT**     | Single lemma as singleton: Γ\_epist returns it unchanged.                                                                                             |
| **Routing**      | `MemberOf` for CorpusQ is collection structure; not used to average “truth”. Γ\_epist aggregates via min/penalty and produces a SCR for sources. |

