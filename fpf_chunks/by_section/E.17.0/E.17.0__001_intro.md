---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "Viewpoint and View Recognition for Multi-View Describing"
section_id: "E.17.0:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__001_intro.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.17.0 — Viewpoint and View Recognition for Multi-View Describing"
  - "E.17.0:intro — Intro"
line_start: 79137
line_end: 79162
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.5"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10.D2"
  - "E.17"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
keywords:
---

## E.17.0 - Viewpoint and View Recognition for Multi-View Describing
> **Status:** Stable

**At a glance.** Use `E.17.0` to decide whether one exact engineering account is a view under one already defined viewpoint, without mistaking its label, layout, generation history, bundle position, or publication for conformance.

**Use this when.** A description, model slice, query result, diagram, or other claim-bearing episteme is being called a functional, safety, maintenance, architecture, or other view, and the next reading, comparison, construction, or publication depends on whether that claim is warranted.

**What goes wrong if missed.** A `viewpointRef`, familiar face name, generated table, or readable diagram is accepted as a view without testing the viewpoint's concerns and rules. The opposite failure is to rebuild a viewpoint convention, bundle, evaluation package, and publication dossier before an ordinary reuse can proceed.

**What this buys.** One stable test works for directly authored and derived epistemes: identify exact candidate E, resolve exact viewpoint edition P, and test P's fixed conformance predicate without changing either episteme's identity.

**First action.** Recover candidate E through C.2.1, resolve an existing `U.ViewpointRef` to exact P, and read the target, concern-coverage, semantic-form, completeness, consistency, and admitted-omission rules fixed by P. Do not author a new viewpoint or bundle merely to perform this test.

**First useful result.** State one readable direct judgment: either `episteme E conforms to viewpoint edition P`, in which case the same E is a `U.View`, or `E does not conform to P`, naming the failed fixed rule without inventing a negative relation occurrence. Keep exact E and P recoverable. If missing identity or interpretation prevents the fixed predicate from being evaluated, report that exact unresolved condition rather than manufacturing a negative result.

**Ordinary stop.** If the next work needs only view recognition, stop after that judgment. Do not add an occurrence designator, explicit result ValueKind, evaluation package, source-viewing relation, correspondence model, collection or structure, publication occurrence, form, or carrier. Add one of those only when a named receiving use depends on it.

> **Tech-name:** `MultiViewDescribing`
> **Plain-name:** recognizing viewpoints and views in multi-view describing

`MultiViewDescribing` names this pattern's method. It is not a public U-kind, a family record, or an extra entity beside the epistemes and relations recovered below.

**Builds on:** C.2.1 for episteme identity; C.13 for collections; A.22 for selected structures; A.6.5 for relation-signature participant SlotSpecs; A.6.3 for an optional source-to-view construction relation; E.10.D2 for Description epistemes and specification use; E.24.PUB for publication; C.29 for representations.

**Used by:** E.17 publication, E.17.1 viewpoint bundles, E.17.2 TEVB, E.18 transformation-flow descriptions, and domain patterns that compare several views.

