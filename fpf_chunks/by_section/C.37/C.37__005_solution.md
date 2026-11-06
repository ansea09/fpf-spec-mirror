---
chunk_kind: "child"
pattern_id: "C.37"
pattern_title: "Select and Use Representations for One Action"
section_id: "C.37:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.37/C.37__005_solution.md"
commit_sha: "4e277189a17b8f9bd3dcdda5df58623d9085ede9"
heading_path:
  - "C.37 — Select and Use Representations for One Action"
  - "C.37:4 — Solution"
line_start: 81768
line_end: 81897
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
  - "co-use"
  - "diagram"
  - "exposure"
  - "loss"
  - "model"
  - "plan"
  - "receiving action"
  - "record"
  - "representation selection"
---

### C.37:4 - Solution

Use one action spine:

1. name the receiving System and exact action or decision;
2. recover each candidate and its direct subject result;
3. separate the direct subject result, optional first-use classification, bounded reliance, receiving conditions and result when needed, and auxiliary facts;
4. state what the candidate exposes or preserves and what it withholds, loses, transforms, or leaves uncertain;
5. mark the row `select`, `decline`, or `unresolved` for the named use and give its return trigger;
6. co-record only rows that support the same receiver and exact action or decision.

**Local mantra.** *One receiver, one action. Recover each candidate under its direct pattern. Name the claim, reliance, loss, receiving conditions, disposition, and return. Put rows together only for that action.*

The mantra is a recall aid, not a decision rule. The receiving pattern still emits the choice, gate, permission, authorization, or domain result.

#### C.37:4.1 - Fix the receiving use before inspecting candidates

Write one sentence:

```text
<receiving System> must <take this exact action or make this exact decision>.
```

Every row in the account uses that same receiver and action. A diagram used to select a proposed Method edition and the same diagram used later to tailor that Method have different use accounts. Reuse unaffected candidate and source results; reconsider the claims, losses and conditions that change with the action. Adjacent actions, one project, one carrier or one meeting do not merge their use boundaries.

If one direct pattern already returns the complete representation–operation choice and limits for this use, take that direct exit. Do not add C.37 merely to rename its result.

#### C.37:4.2 - Recover each row through five separate layers

Open only the layers required by the attempted use.

| Layer | What must be recoverable | What it does not establish |
| --- | --- | --- |
| Direct subject result | The candidate's independently governed kind or result, its subject, and any exact representation, conformance, correspondence, transition, structure, collection, mathematical, plan, Work, or domain relation on which the selected claim depends. | Intended evidence use, reliance, receiving decision, permission, gate passage, or authorization. |
| Optional A.2.4 first-use classification | When the candidate episteme is being used as evidence or as a status carrier, the exact episteme, target claim or status, polarity or value, intended use, and any scope or window that changes that use. | Provenance, sufficiency, `RelianceDisposition`, assurance, permission, or receiving action. |
| Bounded reliance and a needed A.10 account | The relied-on claim, source, actual use relation and support needed for that use. When the source-to-use account remains implicit or must be replayable, use A.10's path and `RelianceDisposition`. Retain currentness, a live challenge, a locally plausible unsupported use, and a reopen or stop condition when they affect this reliance. | Claim truth, selector outcome, gate result, approval, permission, assurance, or Work authorization. |
| Receiving conditions and result | The entry conditions imposed by the rule governing this contribution, including any required gate, permission or authorization. Obtain the choice, acceptance, task or domain result when that result is itself required by the receiving work. Qualified inputs may be used to construct it. | Candidate identity or evidence merely by mentioning the row. |
| Auxiliary facts | Lens, publication, form, carrier, repair, provenance, source, or rendering facts needed to interpret or recover the row. | Any missing positive subject result, reliance, or receiving result. |

If a condition required for the candidate's stated use is negative, missing or unresolved, decline that use or mark it unresolved and name the missing fact or direct result. Preserve independently supported premises. Use ready qualified inputs in the receiving comparison or construction; an unfinished choice or task result does not by itself create a missing input-admission result. Any action that depends on that later result still waits for its grounds.

#### C.37:4.3 - State exposure, loss, and the row disposition

For each candidate, state only distinctions that change the receiving action:

- what it exposes, foregrounds, or preserves;
- what it withholds, omits, loses, transforms, or leaves uncertain;
- the exact claim for which it is selected or declined;
- the direct result and reliance basis that bound that claim, including an A.10 disposition when that account is needed;
- the condition that sends the reader back to the source or reopens selection.

Use exactly these ordinary row dispositions:

| Disposition | Use |
| --- | --- |
| `select` | The required subject identity and relations are established, the reliance basis supports the bounded claim, and the conditions imposed on its use by the receiving rule hold. Use the claim in the receiving operation; obtain its eventual result there. An A.10 `degrade` disposition narrows the selected claim. |
| `decline` | A required direct result is negative, the applicable receiving rule excludes the stated contribution, or the candidate's loss makes the attempted use inadmissible. State the retained weaker use, if any. |
| `unresolved` | A required identity, relation, currentness fact, reliance path, disposition, or receiving result is missing or ambiguous. Name what would reopen the row. |

Selection is use-bounded. It does not make the candidate true, complete, current, published, conforming, relied on, assured, or authorized outside the exact claim and action stated in the row.

#### C.37:4.4 - Use the smallest complete account

Use this readable shape when the result must be retained:

```text
Use-bounded representation-selection account:
  Receiving System and exact action or decision:
  Receiving rule, required entry conditions, and result when needed:
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

First determine whether a later receiving use needs the selection basis retained. An immediate sufficient selection can finish with its grounds, material loss and applicable receiving conditions, without a new record.

When retention is needed:

1. If an owning domain result already carries the same receiving use, embed the complete needed claim group and action boundary there.
2. Otherwise retain that basis as one ordinary C.2.1 episteme.
3. Create no embedded and standalone duplicate for the same use.

A later reader who must reconstruct the selection receives its logically complete basis; a bare verdict or locator is insufficient for that use.

Retention preserves the needed separation: direct subject result, optional A.2.4 classification, reliance basis and any required A.10 account, receiving conditions and result when needed, exposure and loss, disposition and return. An immediate answer preserves the same substantive limits without instantiating every form field. A cross-use ensemble may later relate accounts under its own direct pattern; C.37 does not perform that organization.

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

Recognition asks what the candidate is and which direct result or relation obtains. A.2.4 may add its first evidence-use or status-use classification. Relied-on claims need the source, support and use conditions that warrant them; A.10 develops the source-to-use account when it remains implicit or must be replayable. `B.3` enters only when an actual named assurance claim is current; consequence or reuse alone does not require an assurance package. The receiving pattern owns the action result.

Use an already adequate source-to-use account directly. A new A.10 path or disposition is unnecessary when the claim and its warranted use are already explicit and no further replayable account is needed. A source gap, stale consumed premise or unsupported use still blocks the conclusion that depends on it; narrow the use, obtain the required support, or stop. Reuse an applicable A.10 disposition when one already supplies this boundary.

#### C.37:4.8 - Direct exits and boundary cases

| Case | C.37 disposition |
| --- | --- |
| One direct domain Method already selects one representation–operation configuration for the same one use and returns its limits, as in rhythmic-representation choice. | Use that Method and result; do not invoke C.37 for a duplicate account. |
| A candidate is called a view but `EpistemeViewpointConformanceRelation(E,P)` fails or cannot be evaluated. | Decline it for the view-dependent use or mark that row unresolved. C.37 cannot grant `U.View` membership. Another independently positive direct basis may support a different row and claim. |
| A candidate is a mathematical graph or other mathematical object. | Identify the object and the subject relations on which the claim depends. Use an adequate domain result directly; use `C.29` when a separate mathematical representation, transfer, or reliance question remains. C.37 neither admits the object nor makes the mapping obtain. |
| A candidate is an ordinary non-graph diagram. | Identify its episteme and subject. Require the conformance, representation, correspondence or domain grounds needed for the selected claim. Preserve its evidence and reliance basis; use A.10 for a still-implicit or required replayable source-to-use account. Publication, carrier, provenance or C.2.P.DR repair supplies no missing subject or action ground. |
| Several project, process, or case viewpoints concern one Work. | Co-record them only when each can change the same exact action about that independently identified Work. A viewpoint for another action starts another account. |

