---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection and First-Use Disposition"
section_id: "E.24.CD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__006_solution.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "E.24.CD — Ontic Candidate Detection and First-Use Disposition"
  - "E.24.CD:4 — Solution"
line_start: 88334
line_end: 88404
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.19"
  - "A.19.ECS"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.RSIR"
  - "B.1"
  - "B.2"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.22.2"
  - "C.22.PFR"
  - "C.28"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17.0"
  - "E.18.1"
  - "E.23"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:4 - Solution

Start from the work that is blocked, not from the shape of the source material.

Ask these four questions in order:

1. **What must the next person do or decide?** Name the comparison, classification, publication, repair, decision, or other practical use.
2. **What is that use about?** Name the subject, claim, or source expression without treating its card, row, filename, diagram, or field bundle as the answer.
3. **Which current pattern already governs the needed claim?** Name the predicate or judgment that would let the work proceed.
4. **If that pattern does not close the case, what is actually missing?** State one applicable pattern or one precise unresolved stop below.

#### E.24.CD:4.1 - Apply the first truthful disposition

Plain `situation`, `incident`, `current configuration`, `operating <system>`, and `emergency` are recognition cues, not kind names. Recover only the subjects, claims, and relations that the receiving work actually needs.

| Current need | Next use | Stop that follows |
| --- | --- | --- |
| One current subject pattern already states the needed claim or action. | Apply that subject pattern. If the missing piece is a relation-bearing claim that no current direct predicate closes, apply `A.6.RCD` before proposing a relation kind. | Do not create an ontic, kind, candidate note, or disposition record. A local compound claim or predicate-definition episteme is neither a relation kind nor an occurrence; only a separately justified kind candidate proceeds through `E.24` and `E.24.UK`. |
| One exact ClaimGraph forms one claim-bearing whole about one truthful exact EntityOfConcern under one effective ReferenceScheme. | Use `C.2.1` to identify that episteme. Other independently governed objects may be designated inside its claims without becoming extra EntityOfConcern fields or ontic slots. | If one truthful EntityOfConcern or one identity-bearing ClaimGraph cannot be recovered, keep the epistemes separate. State a collection, publication, representation, or other use relation only when its own predicate obtains; common use or co-publication does not identify one episteme. |
| Wording such as `situation`, `incident`, `current configuration`, `operating <system>`, or `emergency` groups several cues. | Recover the exact systems or holons, characteristic or state claims, actual part relations, and only the temporal or causal relations needed by the current use. Add actual `U.Transformation` or `U.Work` only when independently grounded under `A.3.4` or `A.15.1`. Use a possible-state episteme when possibility is the subject, and a separate C.2.1 description episteme only when claim-bearing orientation is current. | Their conjunction is neither `U.Situation` nor `U.IncidentSituation`. An episteme's EntityOfConcern and any grounding holon in a separately current `EpistemeEmpiricalGroundingRelation` neither identify the world-side subject nor become mandatory fields. Stop decomposition once the action-facing distinction needed by the receiving use is recovered. |
| A proposed subject exists only as an arbitrary fusion, co-presence, connected set, or chosen boundary. | Reject the bundle without forcing it through a construction record. If a constructed object survives as the current subject, apply `B.1`, `A.14`, and `C.13`, and apply `B.2` only when whole reidentification is current; recover its exact construction inputs, whole-forming relations, and identity rule. | Fusion, co-presence, connectedness, and a selected boundary alone form no durable whole. The no-mint result does not block a genuinely irreducible subject later shown to have its own identity and obtaining laws. |
| Repeated typed reasoning needs a local criterion, candidate judgment, or true-candidate set for one context slice. | Use `C.3`, `C.3.1`, and `C.3.2`. | The local kind, `KindSignature`, judgment, and optional extension stay distinct; neither a public `U.*` kind nor a classification-relation occurrence follows. |
| A card, record, table, diagram, file, or schema carries claims, is used as a description, conforms to a viewpoint, expresses an edition, represents something, or bears a form. | Use `C.2.1` to identify an episteme only when its constitution test passes. If it describes a method, structure, relation occurrence, or another subject, apply that subject's description pattern. Use `E.17.0` for actual view membership, `E.24.PUB` for publication, and `C.29` for representation and correspondence. Several patterns can apply because they govern different objects or relations. | Visible shape does not identify the described subject or make any neighboring relation obtain. |
| A path, table, dashboard, schema, or other declarative form seems to authorize, dispatch, prove, prescribe, or perform something by its shape. | Use `C.2.P.DR` to name the visible expression, recover the direct object or relation, state its representation or correspondence use—or `none`—and block the unsupported action claim. | A declarative form does not itself authorize or dispatch work, perform an action, or grant authority. |
| Words such as `relation`, `slot`, `field`, `interface`, bare *role*, `function`, or `endpoint` still leave the object or claim unclear. | Use E.10.ROLE first for bare *role*; continue to A.6.RSIR when it denotes relation participation, a declaration place, an interface place, or a representation position. Use A.6.F for function wording and A.6.P or the pattern for the recovered relation. Then stop at that pattern. | An engineering word creates no subject kind, relation kind, participant, declaration, system-role kind, or assignment. |
| The subject and governing claim are already clear, but a word or phrase compresses them. | Repair the bounded wording through `E.10`, `E.10.ARCH`, or the applicable precision-restoration pattern. | A clearer name does not create a new subject, relation, or kind. |
| An already governed value needs a stable reusable name rather than a repaired sentence. | Use `F.18` after recovering the value, its kind and subject pattern, its effective reference scheme, and the local sense to be named. For relation-facing wording, settle any missing direct relation through `A.6.RCD` first. | A label or `NameCard` neither admits the value or a public kind nor makes a relation obtain. |
| One blocked use concerns an independently recoverable candidate, proposal, or source construct; named consumers show concrete cross-pattern duplication or disagreement pressure; and one obvious direct route does not close it. | Open `E.24` and transfer only those detection facts. Let E.24 test identity, the minimal relation set, dependent reliance, non-duplication, and non-use. | E.24.CD neither requires those settlement results nor admits or rejects the ontic. A still-missing identity or relation rule can reach E.24's unresolved branch. |
| The subject, needed claim, or subject pattern cannot yet be recovered. | Keep the inquiry attached to the source expression or blocked work and name what is missing. | Do not hide non-settlement inside a candidate record, score, provisional `U.*` name, or “future ontology” list. |

When a durable public `U.*` kind is also proposed, `E.24.UK` returns its separate admission result. If the ontic and kind are both new, use the atomic co-decision already defined by E.24 and E.24.UK; neither result proves the other.

#### E.24.CD:4.2 - Recover objects hidden by a visible form

For a project card, row, schema, or diagram, inspect only what the current work consumes:

1. Which filled statements are claims, and what is each claim about?
2. Which entities or non-entity values are independently identified under their direct patterns?
3. Which direct predicates are asserted, what are their actual participants, and which independently established facts satisfy their obtaining conditions?
4. Is the visible arrangement a publication form, a C.29 representation, a carrier, or merely a local layout?
5. Does the work need local classification of a candidate, or only a claim about an already governed feature?
6. What stronger reading must be blocked—for example, record existence creates performed work, a row creates membership, or a field name admits a kind?

A field label is not a `SlotSpec`. `A.6.5` governs the declaration: a reusable `SlotSpec` appears only inside a `RelationSignature` for an already recovered direct relation and only when a named later use needs that declaration. A row value is not an actual relation participant merely because it occupies a column.

#### E.24.CD:4.3 - Open E.24 when cross-pattern pressure is concrete

Open E.24 when these detection facts are recoverable:

- one blocked use or decision;
- one independently recoverable candidate entity, proposal episteme, or source-construct entity that carries the inquiry without presupposing a durable ontic;
- concrete duplication or disagreement pressure in more than one current pattern description;
- the named consumers that make shared coordination plausible; and
- why one obvious direct-pattern route does not already close the blocked use.

Transfer those facts to E.24. E.24—not E.24.CD—tests the complete identity or constitution rule, minimal direct-relation set, dependent reliance, non-duplication, practical gain, and nearest non-use boundary. If one of those facts cannot be established, E.24 may return its unresolved result. Detection therefore does not require the author to settle the candidate before opening the settlement pattern.

A plainly direct case still stops at its subject pattern. Repeated words, several source forms, copied fields, or a useful schema can prompt inspection, but without a blocked use, an independently recoverable inquiry subject, concrete cross-pattern pressure, named consumers, and failure of an obvious direct route, they do not open E.24.

#### E.24.CD:4.4 - State one result and stop

Most cases need only one sentence:

> For `<work or decision>`, apply `<subject pattern>` to `<exact subject or claim>` because `<decisive fact>`; `<blocked stronger reading>` does not follow.

When no pattern can yet apply truthfully, say:

> For `<work or decision>`, leave `<exact subject or claim question>` unresolved because `<missing subject, predicate, or subject pattern>`; `<blocked stronger reading>` does not follow.

Use a longer explanation only when another author must understand a disputed disposition. Do not create an `OnticCandidateCluster`, candidate registry, scorecard, or mandatory disposition form. Once the applicable pattern or unresolved stop is stated, continue there; reopen E.24.CD only if the recovered subject or practical use changes.

