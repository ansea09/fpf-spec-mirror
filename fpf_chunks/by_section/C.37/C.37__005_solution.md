---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Use-Bounded Representation Selection and Co-Use"
section_id: "C.37:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__005_solution.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.37 — Use-Bounded Representation Selection and Co-Use"
  - "C.37:4 — Solution"
line_start: 68002
line_end: 68127
dependencies:
  - "A.10"
  - "A.2.4"
  - "A.22"
  - "A.6.3.RT"
  - "C.11"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
keywords:
---

### C.37:4 - Solution

Use one action spine:

1. name the receiving System and exact action or decision;
2. recover each candidate and its direct subject result;
3. separate the direct subject result, optional first-use classification, bounded reliance, receiving result, and auxiliary facts;
4. state what the candidate exposes or preserves and what it withholds, loses, transforms, or leaves uncertain;
5. mark the row `select`, `decline`, or `unresolved` for the named use and give its return trigger;
6. co-record only rows that support the same receiver and exact action or decision.

**Local mantra.** *One receiver, one action. Recover each candidate under its direct pattern. Name the claim, reliance, loss, receiving result, disposition, and return. Put rows together only for that action.*

The mantra is a recall aid, not a decision rule. The receiving pattern still emits the choice, gate, permission, authorization, or domain result.

#### C.37:4.1 - Fix the receiving use before inspecting candidates

Write one sentence:

```text
<receiving System> must <take this exact action or make this exact decision>.
```

Every row in the account uses that same receiver and action. A diagram used to select a proposed Method edition and the same diagram used later to tailor that Method belong to different accounts. Adjacent actions, one project, one carrier, or one meeting do not merge their use boundaries.

If one direct pattern already returns the complete representation–operation choice and limits for this use, take that direct exit. Do not add C.37 merely to rename its result.

#### C.37:4.2 - Recover each row through five separate layers

Open only the layers required by the attempted use.

| Layer | What must be recoverable | What it does not establish |
| --- | --- | --- |
| Direct subject result | The candidate's independently governed kind or result, its subject, and any exact representation, conformance, correspondence, transition, structure, collection, mathematical, plan, Work, or domain relation on which the selected claim depends. | Intended evidence use, reliance, receiving decision, permission, gate passage, or authorization. |
| Optional A.2.4 first-use classification | When the candidate episteme is being used as evidence or as a status carrier, the exact episteme, target claim or status, scope, polarity or value, window, and intended use. | Provenance, sufficiency, `RelianceDisposition`, assurance, permission, or receiving action. |
| A.10 bounded reliance, when material | The exact relied-on claim, source and provenance path, premise, reference, decision-use, operation-argument, or other direct use relation, time/currentness boundary, bounded evidence use, unsupported attempted use, challenge when current, one current `RelianceDisposition`, and its reopen or stop condition. | Claim truth, selector outcome, gate result, approval, permission, assurance, or Work authorization. |
| Receiving result | The exact `ChoiceResult`, gate result, permission, authorization, acceptance, or domain result supplied by the pattern that defines or tests the receiving action. | Candidate identity or evidence merely by mentioning the row. |
| Auxiliary facts | Lens, publication, form, carrier, repair, provenance, source, or rendering facts needed to interpret or recover the row. | Any missing positive subject result, reliance, or receiving result. |

If a layer required by the attempted use is negative, missing, or unresolved, do not borrow support from another layer. Decline the row or mark it unresolved and name the missing fact or direct result.

#### C.37:4.3 - State exposure, loss, and the row disposition

For each candidate, state only distinctions that change the receiving action:

- what it exposes, foregrounds, or preserves;
- what it withholds, omits, loses, transforms, or leaves uncertain;
- the exact claim for which it is selected or declined;
- the direct result and, when material, A.10 disposition that bounds that claim;
- the condition that sends the reader back to the source or reopens selection.

Use exactly these ordinary row dispositions:

| Disposition | Use |
| --- | --- |
| `select` | The required direct subject result is positive, every required reliance condition supports the exact bounded use, and the receiving result permits this candidate's stated contribution. Narrow the selected claim when A.10 says `degrade`; do not invent a second disposition vocabulary. |
| `decline` | A required direct result is negative, the receiving result excludes the candidate, or the candidate's loss makes the attempted use inadmissible. State the retained weaker use, if any. |
| `unresolved` | A required identity, relation, currentness fact, reliance path, disposition, or receiving result is missing or ambiguous. Name what would reopen the row. |

Selection is use-bounded. It does not make the candidate true, complete, current, published, conforming, relied on, assured, or authorized outside the exact claim and action stated in the row.

#### C.37:4.4 - Use the smallest complete account

Use this readable shape when the result must be retained:

```text
Use-bounded representation-selection account:
  Receiving System and exact action or decision:
  Receiving-result governor and result:
  Candidate rows:
    - Candidate and direct subject result:
      Exact claim used:
      Intended first evidence use, if current:
      A.10 path, direct use relation, and RelianceDisposition, if current:
      Exposed or preserved:
      Withheld, lost, transformed, or uncertain:
      Disposition: select | decline | unresolved
      Return or reconsideration trigger:
  Action supported, declined, or blocked under the combined limits:
```

One row is a valid minimum when C.37 still adds a needed layer separation. If the direct pattern already supplies the same complete one-result/one-use answer, use the direct exit instead.

This is a logical claim group, not a universal record kind, `U.Representation`, `RepresentationOf` relation, taxonomy, manifest, view family, collection, or structure. Do not give it another schema merely because several domains use the same questions.

#### C.37:4.5 - Realize the result once

Use one deterministic realization rule:

1. If an owning domain result already carries this same receiving use, embed the complete row claims and action boundary in that result.
2. Otherwise retain the complete account as one ordinary C.2.1 episteme.
3. Never create both an embedded copy and a standalone duplicate for the same use.

Embedding does not weaken the required separation: direct subject result, optional A.2.4 classification, A.10 reliance when material, receiving result, exposure and loss, disposition, and return trigger all remain recoverable. A cross-use ensemble may later relate several accounts under its own direct pattern; C.37 does not perform that later organization.

#### C.37:4.6 - Keep co-use local to one action

`Co-use` means only that the same receiver relies on two or more completed rows for one exact action or decision. Each row keeps its own direct result, premise, reliance boundary, loss, and return trigger. One positive row cannot repair another row's missing subject result or reliance path.

Co-use does not establish:

- one collection or selected structure;
- one multi-view family or mutual conformance;
- one integrated model or coherent world account;
- one constructional whole or composition relation;
- one shared representation scheme, graph, or correspondence;
- one assurance result or authorization.

Open `C.13`, `A.22`, `E.17.0`, `C.29`, a domain integration pattern, or another direct governor only when the receiving action depends on that additional claim.

#### C.37:4.7 - Recognition, reliance, assurance, and action remain separate

Recognition asks what the candidate is and which direct result or relation obtains. A.2.4 may add only its first evidence-use or status-use classification. A.10 adds one bounded evidence-provenance and reliance result only when the exact use relies on evidence. `B.3` enters only when an actual named assurance claim is current; consequence or reuse alone does not require an assurance package. The receiving pattern then owns the action result.

This split lets ordinary reversible work stop cheaply. A practitioner may inspect or compare a candidate under its direct result and visible limit without opening A.10 or B.3 when no evidence reliance or assurance claim is being made. When reliance is material, the exact path and disposition become mandatory for that use.

#### C.37:4.8 - Direct exits and boundary cases

| Case | C.37 disposition |
| --- | --- |
| One direct domain Method already selects one representation–operation configuration for the same one use and returns its limits, as RHY.5 does for rhythmic-representation choice. | Use that Method and result; do not invoke C.37 for a duplicate account. |
| A candidate is called a view but `EpistemeViewpointConformanceRelation(E,P)` fails or cannot be evaluated. | Decline it for the view-dependent use or mark that row unresolved. C.37 cannot grant `U.View` membership. Another independently positive direct basis may support a different row and claim. |
| A candidate is a mathematical graph or other mathematical object. | First identify the object and obtaining subject relations under their direct patterns; then use `C.29` for the explicit lens, mapping, preserved and lost structure, admitted use, and stop. C.37 neither admits the object nor makes the mapping obtain. |
| A candidate is an ordinary non-graph diagram. | Identify its episteme and subject. Require an exact positive conformance, representation, correspondence, or domain result for the selected claim. Add A.10 when evidence is relied on. Publication, carrier, provenance, or C.2.P.DR repair cannot supply the missing basis or receiving result. |
| Several project, process, or case viewpoints concern one Work. | Co-record them only when each can change the same exact action about that independently identified Work. A viewpoint for another action starts another account. |

