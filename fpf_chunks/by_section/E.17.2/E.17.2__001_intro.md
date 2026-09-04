---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
section_id: "E.17.2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__001_intro.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "E.17.2 — TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons"
  - "E.17.2:intro — Intro"
line_start: 82368
line_end: 82395
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.6"
  - "C.13"
  - "C.2.1"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.24.PUB"
  - "U.View"
  - "U.Viewpoint"
  - "U.ViewpointRef"
keywords:
---

## E.17.2 - TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons
> **Status:** Stable authoring template; no TEVB catalogue value is shipped by this pattern.

**Use this when.** A project wants to author one small local family of engineering viewpoints for descriptions of holons, so that functional, procedural, allocation-responsibility, and module-interface claims remain distinguishable and comparable.

**What goes wrong if missed.** A functional, procedural, responsibility, structural, diagram, or report label starts doing several jobs at once: it is treated as the viewpoint, the view, the described holon, a publication face, or proof of an engineering relation. The opposite failure is to require all four viewpoints and their full authoring machinery for one local reading.

**What this buys.** TEVB supplies a four-position authoring template. Once a project has constituted its own catalogue L and bound four exact local references to four exact viewpoint epistemes, that project can reuse the resulting local family while keeping candidate episteme, described holon, conformance, cross-view relations, and publication separate. One use may select just one bound member.

**First action.** Resolve the already admitted project-local catalogue edition L and the local declaration designated by `f_eng`, then resolve only the `U.ViewpointRef` needed for the present question. If L or the declaration is new, missing, or disputed, use E.17.1:4.2 to constitute or verify `<G_L, K_L, R_L>` for that edition. If a needed P edition is missing, author and admit it under E.17.0 before binding its reference. Reuse those results while the catalogue edition, effective scheme, declaration, and relied-on premises remain unchanged.

**First useful result.** For materialization: one exact project-local L, ordinary family designator `f_eng`, four exact local references `r_functional`, `r_procedural`, `r_allocation`, and `r_module`, and four exact local P targets to which those references resolve under `R_L`. For later use: the admitted L and declaration, one needed reference resolving one exact P, and a readable E/P conformance judgment. Before the four bindings exist, the result is only an authoring template, not a reusable family value.

**Ordinary stop.** For materialization, stop when the exact local catalogue triple, declaration claim block, four reference bindings, and four exact P targets are recoverable. For later use, stop after resolving the admitted L and declaration, the one needed P, and its E/P judgment; reopen full catalogue constitution only under the E.17.1:4.2 triggers. Add another member, structured viewpoint-authoring witness, C.13/A.22 organization, construction history, cross-view relation, evaluation, or publication object only when a named receiving use depends on it.

**Not this pattern when.** Keep a one-off viewpoint local when no recurring four-position family is needed. Author another E.17.1 declaration for safety, assurance, information, mission, deployment, business, publication, or architecture-framework-specific concerns outside the four TEVB positions. TEVB is not a universal architecture framework.

> **Tech-name:** `TEVB` — the template name, not a family designator or catalogue value
> **Plain-name:** project-local typical engineering viewpoint bundle template for holons

**Product-form boundary.** This pattern ships no exact catalogue edition, effective scheme, family designator, `U.ViewpointRef`, or viewpoint episteme edition. Every `L`, `f_eng`, `r_*`, `P_*`, `C_*`, `Q_*`, and `S_*` symbol below is a variable in the template until one project supplies and verifies its exact binding. Equal labels in two projects establish no shared family or cross-project reuse. Such reuse begins only when both uses resolve the same exact L and member references.

The template does not by itself constitute an architecture framework, a `U.Method`, a set of publication forms, or an additional entity alongside exact catalogue L and its referenced P editions. It prescribes no modelling notation, storage format, or tool API.

**Builds on:** E.17.0 for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View`; E.17.1 for bundle packaging by `U.ViewpointRef`; C.2.1 for episteme identity; C.13 for the constituent collections of viewpoint conventions; A.22 for their selected structures; A.6.6 and E.17.0 for exact constituent-dependency relations; A.6.3 for optional view construction; E.24.PUB for publication.

**Used by after a project materializes the bindings:** E.18 transformation-flow descriptions, E.17 multi-view publication, architecture-description patterns, and domain patterns that need that exact local engineering concern family for holons.

