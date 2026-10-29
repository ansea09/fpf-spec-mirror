---
chunk_kind: "child"
pattern_id: "C.2.P.DR"
pattern_title: "Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
section_id: "C.2.P.DR:5"
section_title: "Worked slices"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P.DR/C.2.P.DR__007_worked-slices.md"
commit_sha: "c3b34de07a6bd2df85c7081a4c367fd09978079c"
heading_path:
  - "C.2.P.DR — Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)"
  - "C.2.P.DR:5 — Worked slices"
line_start: 54217
line_end: 54311
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.19.SPR"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.20"
  - "E.8"
  - "F.19"
keywords:
---

### C.2.P.DR:5 - Worked slices

#### C.2.P.DR:5.1 - Graph path in a transformation-flow structure

Wording: "The P2W path routes the team from principle to work."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: P2W graph expression with a highlighted path or path slice
  CurrentDirectObjectOrRelation: exact E.18 `PathSlice` and E.18.1 carry-through relation among the named records when those objects are current
  RepresentationOrCorrespondenceUse: highlighted nodes and edges render the selected E.18 `PathSlice`; the highlight adds no work ordering
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: ordered work route for the team
  RecoveredGoverningPattern: E.18.1, with A.15.2 or A.15.1 only if planned or dated work is current
  RetainedUse: selected graph path and carry-through relation for inspection
  BlockedStrongerActionClaim: no work route or prescribed workflow by path shape alone
  StopOrReopenCondition: stop at inspection of the selected path and carry-through relation; use A.15.2 for a prescribed work sequence. If a separate mathematical transfer is proposed, establish its C.29 correspondence and limits before relying on that transfer. Reopen when the selected graph, source or intended work relation changes
```

A graph publication or pattern publication remains a separately governed publication object. If one is current, state its exact source or publication relation and participants in the neighbouring claim; neither publication object belongs in `SourceOrPublicationRelation` by mention alone.

#### C.2.P.DR:5.2 - Evidence path near release

Wording: "The evidence path authorizes release."

Repair: name the claim or bounded use and recover the descriptive evidence-provenance path through `A.10`, with each cited direct relation established under its own subject pattern. Release, permission, or gate passage requires the authority, gate, or release pattern that defines or constrains that claim. This pattern is used only if `path` wording itself is causing the representation to be overread as a permission route.

#### C.2.P.DR:5.3 - Query plan and access path

Wording: "The query plan calls the production work sequence."

Repair: recover whether the query plan represents optimizer choices, expresses claims about an exact method, presents a formal substrate, supplies a source cue or evidence relation, states a work plan, or records an actual query run. If it only represents query-evaluation choices, stop at the representation. Use A.3.1 for a reusable semantic way-of-doing claim. Use A.3.2 only when the claim-bearing episteme passes the MethodDescription membership guard in 4.4. Use A.15.1 for a performed query run, together with the exact evidence or source-use relation when that later claim is current.

#### C.2.P.DR:5.4 - Dashboard predicate

Wording: "The dashboard green path lets the release move."

Repair: recover dashboard face, source relation, status or state bearer, value frame, source currentness, and gate or release claim. The dashboard may be a publication face and source cue. Recover release permission through the applicable gate decision (`A.21`) or authority relation, including any source contribution required by its governing rule.

#### C.2.P.DR:5.5 - Pattern relation

Wording: "This pattern exits to A.10."

Repair: if the current relation is "use `A.10` when an evidence relation or provenance relation is current", write that declarative boundary. Keep ordinary ownership or navigation wording when its relation and participants are clear. Use exit, receiver, route, owner, home, dispatch, or call language to assert action or control only when the pattern is actually about an action occurrence, work plan, control mechanism, or communication relation that has those semantics.

#### C.2.P.DR:5.6 - Solver algorithm

Wording: "The solver algorithm is the mechanism."

Repair: first identify the direct object or relation, any representation use, and which claim is current. A solver configuration may represent claims carried by an episteme that qualifies as `U.MethodDescription` only after the 4.4 membership guard; the configuration is not that episteme by file form or executability. The reusable semantic way of solving may be `U.Method`; the MILP formulation may expose a formal substrate and mathematical-lens use; a reusable operation algebra with laws and admissibility predicates may be `U.Mechanism`; a solver run may be `U.Work`; and a run result may support another claim through its direct evidence relation. Select A.6.1 and E.20 only when their mechanism fields are present in the current claim.

#### C.2.P.DR:5.7 - Reactor-cooling flow graph

Wording: "The preserved heat-flow path authorizes the valve change."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: reactor-cooling heat-flow graph with one highlighted preserved path
  CurrentDirectObjectOrRelation: exact E.18 heat-flow path or `PathSlice`; keep boundary conditions and any flow valuation under their subject patterns
  RepresentationOrCorrespondenceUse: the rendering identifies the selected E.18 path; a proposed inference from its edges to physical heat flow still lacks its correspondence and boundary conditions
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: graph path authorizes physical valve-change work
  RecoveredGoverningPattern: E.18 and C.29 for graph and lens use; A.21, A.10, A.15.2, and A.15.1 only if gate, evidence, work plan, or dated work is current
  RetainedUse: graph inspection and identification of the missing heat-flow correspondence
  BlockedStrongerActionClaim: no release, gate passage, physical intervention, or work occurrence by highlighted path alone
  StopOrReopenCondition: keep the proposed physical inference unresolved until the correspondence, material losses and boundary conditions support it under C.29; operational reliance also needs the applicable validation and gate or authority result. Reuse adequate existing domain/model documentation. Reopen when that basis or intended intervention changes
```

An engineering-review publication and a gate record remain separate objects. State any exact source or publication relation with its participants, and keep any gate relation under its subject pattern; neither object belongs in `SourceOrPublicationRelation`.

#### C.2.P.DR:5.8 - CRISPR guide-selection table

Wording: "The guide-selection table approves the edit."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: CRISPR guide-selection table with off-target scores and candidate ranking
  CurrentDirectObjectOrRelation: candidate-guide comparison and exact characteristic values under C.16 or A.19; use A.10 to recover any independently established direct support relation needed for reliance
  RepresentationOrCorrespondenceUse: rows identify the compared candidate guides and columns reproduce named score values with their scales and source references; the ranking adds no approval relation
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: ranked row approves biological intervention
  RecoveredGoverningPattern: C.16 or A.19 for characteristics when current; A.10 for evidence; A.15.2 for experimental work plan; A.21 or authority pattern only if approval or gate claim is current
  RetainedUse: source-finding, candidate comparison, and constraint review
  BlockedStrongerActionClaim: no edit approval, work occurrence, safety claim, or gate passage from table rank alone
  StopOrReopenCondition: stop at the supported comparison under the stated score meanings and source conditions. Use C.29 only if a separate model or transfer claim is made. Intervention approval needs its applicable authority or gate result; resolve unclear “role authorization” through E.10.ROLE, distinguishing a missing rule from missing facts under a known rule. Reopen when the scores, protocol or intended use changes
```

A lab notebook, protocol publication, source episteme, and review record remain separate objects. State an exact source or publication relation and its participants only when it obtains; none of these objects belongs in `SourceOrPublicationRelation` by mention alone.

