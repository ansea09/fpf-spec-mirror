---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "Viewpoint and View Recognition for Multi-View Describing"
section_id: "E.17.0:5"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__006_worked-cases.md"
commit_sha: "870fb0c2a5dcfe1e0165a111fdf2cf8659c85a54"
heading_path:
  - "E.17.0 — Viewpoint and View Recognition for Multi-View Describing"
  - "E.17.0:5 — Worked cases"
line_start: 106528
line_end: 106557
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
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

### E.17.0:5 - Worked cases

#### E.17.0:5.1 - Directly authored architecture view

Architecture episteme E concerns exact system T. Maintainability viewpoint episteme P concerns its selected viewpoint-convention structure and states the target-kind, concern, admitted-kind, coverage, and semantic-form rules. E satisfies those fixed rules, so `EpistemeViewpointConformanceRelation(E,P)` obtains and the same E is a `U.View`. No source episteme or A.6.3 viewing is required.

#### E.17.0:5.2 - Query output that is not yet a view

A query over source episteme X constructs episteme Y, and A.6.3 records the source-to-Y viewing relation. Y omits a concern component that exact viewpoint P requires. The construction relation obtains, but conformance does not; Y is not a `U.View` under P. A later repair may create Y2 with different claim content and a new C.2.1 identity.

#### E.17.0:5.3 - One episteme, two viewpoints, one selected use

Unchanged episteme E conforms to safety viewpoint P1 and maintenance viewpoint P2. Two participant-determined conformance occurrences obtain, while the named current review use selects only P1 through one singular `viewpointRef`. E remains one `U.View`; the selection neither creates the P1 conformance nor removes the P2 conformance.

#### E.17.0:5.4 - Viewpoint revision and library repackaging

Adding a reference to unchanged viewpoint episteme P to another E.17.1 local family declaration, or carrying it in another catalogue edition, changes only the catalogue declaration and provenance; it does not change P. Revising P's conformance rules creates another episteme `P_new`; conformance of E to `P_old` does not imply conformance to `P_new`. An `EpistemeEditionRelation` may relate the P editions, but it is not a conformance occurrence.

#### E.17.0:5.5 - Two publications of one view

View episteme E conforms to P. A web publication uses exact expression X1 following reusable form F1, borne by carrier K1; a printed publication uses X2, F2 and K2. Expression, bearing and selected form conformance obtain for each. Two exact publications make the same E available under their own audience, bounded-use and maximal availability intervals. E remains one view episteme. Broader availability of E can continue when an alternative expression or carrier replaces one of these exact publications.

#### E.17.0:5.6 - Cross-view correspondence

A functional view names transformation F and a structural view names module M. A project claim says M realizes F. The shared system EntityOfConcern and aligned diagram positions do not establish realization. Recover exact F and M, apply the direct realization-relation pattern, then identify an assertion episteme about that occurrence if review needs it. A traceability matrix may represent the assertion and occurrence through an explicit correspondence; C.29 applies when that use requires a mathematical lens. Its cell is not the realization relation.

#### E.17.0:5.7 - Procedural view is not a method description

A TEVB procedural view E concerns exact holon H and carries claims about methods, order, state, concurrency, and recovery through their exact relations to H. E may conform to procedural viewpoint P and therefore be a `U.View`, but it is not a `U.MethodDescription` because its exact EntityOfConcern is H rather than one admitted method. A true method-description view retargets to the method and uses a viewpoint whose target-kind criterion admits methods.

