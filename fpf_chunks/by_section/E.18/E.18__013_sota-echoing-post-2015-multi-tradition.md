---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transduction Graph Architecture (E.TGA)"
section_id: "E.18:12"
section_title: "SoTA‑Echoing (post‑2015, multi‑Tradition)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__013_sota-echoing-post-2015-multi-tradition.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "E.18 — Transduction Graph Architecture (E.TGA)"
  - "E.18:12 — SoTA‑Echoing (post‑2015, multi‑Tradition)"
line_start: 65170
line_end: 65186
dependencies:
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.7"
  - "E.10"
  - "E.17"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "CSLC normalize-then-compare"
  - "CV⇒GF (ConstraintValidity → GateFit)"
  - "DesignRunTag"
  - "MVPK faces"
  - "OperationalGate(profile)"
  - "PathSlice/Sentinel refresh"
  - "Set-return selection"
  - "SquareLaw"
  - "UNM declaration locus"
  - "edge=U.Transfer (single-edge kind)"
  - "nodes=morphisms"
  - "transduction graph"
---

### E.18:12 - SoTA‑Echoing (post‑2015, multi‑Tradition)

> Each row states the source idea, the FPF invariant E.TGA adopts, the practitioner move it changes, and the shortcut it rejects. Vendor, tool, and literature tokens are informative; the invariant and practitioner move carry the pattern explanatory work.

| SoTA source idea | FPF invariant | Practitioner move | Rejected shortcut |
|---|---|---|---|
| **Applied category theory / compositional open systems** (Fong & Spivak, *Seven Sketches in Compositionality*, 2019) | Use one `TransductionGraph` whose nodes are typed morphism/transduction bindings and whose edges use the single graph edge kind `U.Transfer`; publication faces preserve composition rather than inventing a second publication meaning. | Name the graph object, node kinds, one `U.Transfer`, and any live path or crossing before drawing an ordered work/method sequence. | Treating category-theory prestige, tool pipelines, lineage packages, or work/method narratives as graph semantics. |
| **Operads, wiring diagrams, and hypergraph categories** (Spivak, *Operads of Wiring Diagrams*, 2021; Baez & Fong, *A Compositional Framework for Passive Linear Circuits*, 2015) | Typed ports and interface junctions motivate Bridge/CL/Phi pins at crossings; E.TGA adapts the math by requiring publication pins that the math alone does not supply. | When an interface or boundary crossing matters, publish the Bridge, UTS row, CL/CL^plane, and R-lane penalty placement instead of leaving an unpinned junction. | Reading an interface diagram, wiring diagram, or decorated cospan as sufficient crossing evidence. |
| **Open-graph and string-diagram rewriting** (Bonchi et al., *Graphical Linear Algebra*, 2019; Kissinger survey lineage) | Rewrites and subflow refactors are admissible only with edition bumps, sentinel scopes, and `PathSlice` locality sufficient for replay. | Localize the rewrite to the affected subflow or slice, pin editions, and re-emit the affected faces. | Treating a global rewrite as replay-safe because the diagram still looks equivalent. |
| **Research-package portability / RO-Crate-style research packaging** (RO-Crate 1.2; Soiland-Reyes et al., *Packaging research artefacts with RO-Crate*, 2022, as lineage) | Portable package descriptions belong in MVPK faces and InteropCards; packages and lineage metadata do not define graph semantics. | Publish package, provenance, and source refs as publication support while keeping graph meaning in the node/gate definitions. | Treating a crate, package, file bundle, or lineage record as the semantic authority for the graph. |
| **Reproducibility and content addressability** (Di Cosmo et al., *Referencing Source Code Artifacts: a Separate Concern in Software Citation*, 2020) | Stable identifiers become edition pins and entries in `E⃗`; they make references checkable but do not decide node, gate, or mechanism meaning. | Pin the exact editions of code, comparator, transport registry, descriptor map, or distance definition used by a face or path. | Treating an identifier, hash, or content-addressed source ref as semantic authority. |
| **TAMP and MPC planning and control practice** (Garrett, Lozano-Perez, Kaelbling 2021 as lineage; Zhao et al., *A Survey of Optimization-based Task and Motion Planning*, 2024, as a TAMP survey anchor; named MPC survey or named reference used when MPC is the live claim) | Iteration is allowed only as a budgeted Selection-Planning loop with freshness checks and launch values bound in `U.WorkEnactment`. | Declare the loop budget, freshness/request boundary, next `PathSlice`, and Work-only launch-value filling. | Turning E.TGA into an ordered work-method narrative, an unbounded loop, or pre-Work launch-value filling. |
| **Quality-Diversity / illumination search** (MAP-Elites and CMA-ME as lineage; QDax JMLR 2024 for QD library support; QDHF 2023/ICML 2024 or QDAIF 2023 refs only when feedback-guided QD is live) | Set and archive returns stay visible; E.TGA treats covert scalarization to one winner as non-conformant while leaving selector, archive, dominance, and comparator semantics to neighboring loci. | Return the set/archive, pin comparator and descriptor/distance editions, and cite the selector/comparator loci when live. | Collapsing a partially ordered or archive-like result into a single best score. |
| **Profunctor optics / modular projection practice** (Pickering, Gibbons, Wu, *Profunctor Optics*, 2019) | MVPK faces are projections of graph/morphism information; they carry views without adding new numeric or mechanism claims. | Publish views as MVPK faces with correspondence refs and pins, while leaving transformations and checks in their governing patterns. | Treating a view, projection, screen, or explanation as a transformation, evidence result, or gate decision. |

*Cross-tradition note.* Rows 1-3 (compositional graph practice), rows 4-5 (publication and reproducibility practice), row 6 (controls/robotics), row 7 (evolutionary search), and row 8 (PL/semantics) jointly anchor E.TGA across multiple traditions per E.8, but each row is retained only because it changes a practitioner move or rejected overread.

