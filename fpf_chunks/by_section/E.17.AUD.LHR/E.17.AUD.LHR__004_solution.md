---
chunk_kind: "child"
pattern_id: "E.17.AUD.LHR"
pattern_title: "PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
section_id: "E.17.AUD.LHR:3"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.AUD.LHR/E.17.AUD.LHR__004_solution.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "E.17.AUD.LHR — PublicationUnit Stability Discipline and Local Head Restoration - repair the overloaded local lexical head before the publication unit inherits it"
  - "E.17.AUD.LHR:3 — Solution"
line_start: 65584
line_end: 65663
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.14"
  - "E.17.AUD"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "F.18"
keywords:
---

### E.17.AUD.LHR:3 - Solution

> `Local Head Restoration` repairs the overloaded local lexical head before the rest of the publication unit is allowed to inherit it.
>
> It restores lexical-head kind, active local reading, carried move or question under repair, and any family, governing-pattern, and primary-entity/relation stack that the sentence is quietly relying on.

#### E.17.AUD.LHR:3.1 - Pairwise plain glosses

- **Pressured local lexical head** = the word doing more work than the sentence has honestly restored.
- **Lexical-head kind** = what FPF kind or locally declared head that word names here: for example description, carrier, publication unit, EntityOfConcern, relation record, face, or view.
- **Active lane** = where the local work is happening here: for example review, publication, comparison, process, or authority.
- **Active primary entity or relation named by value/claim** = what the local sentence or publication unit is actually about here, when such an object is active.
- **Move or question under repair** = what the sentence is doing with the active primary entity, relation named by value/claim, or local lexical-head repair object, if anything.
- **Family, governing-pattern, and primary-entity/relation stack** = when a broader family or governing pattern is active, name the family, governing pattern, primary entity or relation named by value/claim, carried move or question under repair, and outside work separately rather than letting one familiar local lexical head carry them by implication.

**Local reading lens.** Treat the overloaded local lexical head as one typed local head inside one publication unit. This local lens restores one overloaded local lexical head; it does not settle publication-unit modeling-lens policy, redefine the inherited moving lineage or its publication-form lane, publication-face lane, and carrier lane, or replace neighboring semioarchitecture characteristics. The smallest honest local lens asks five entries: what lexical-head kind is named here, which lane is primary, what active primary entity or relation named by value/claim is in play, what carried move or question under repair is carried, and what still remains outside. If that local lens no longer stabilizes the same publication unit, local repair has already reached its limit; apply its governing FPF pattern or use the project-side FPF kind and reference named by value.

#### E.17.AUD.LHR:3.2 - Ordinary working card

Use this five-row card for ordinary cases:

| Row | Ordinary prompt |
| --- | --- |
| 1 | Which trigger word is carrying unresolved semantic load? |
| 2 | What lexical-head kind is it honestly naming here? |
| 3 | Which local reading is actually primary here? |
| 4 | What active primary entity or relation named by value/claim, carried move or question under repair, and outside work are actually in play here? |
| 5 | After one honest repair, is local restoration enough, or does another governing FPF pattern or project-side FPF kind and reference named by value now govern the case? |

Treat that card as the recognition block. It is a local repair aid, not a universal sequence rail.
Use it while one overloaded local lexical head remains the main defect.

When family or governing-pattern language is load-bearing, add one explicit conditional output line next to the card: `repair disposition = ... | governing pattern = ... | primary entity/relation = ... | move = ... | outside work = ...`.

Read the card as a three-way recovery aid:
- if rows 1-5 stabilize around one repaired local lexical head, one restored lane, one active primary entity or relation named by value/claim, and one honest local question, stay here;
- if rows 1-5 stabilize locally and the remaining question is one bounded comparative review move over already pinned source epistemes or publications, apply `E.17.ID.CR` rather than thickening this local lexical-head repair pattern;
- if rows 2-5 still cannot stay stable because the same publication unit keeps borrowing a different object, move, or outside-work boundary from the same local lexical head, apply `E.17.AUD.OOTD` instead of pretending one more qualifier will rescue the same unit.

The nearest worked slices for those three repair dispositions are:
- ordinary stay-local: `E.17.AUD.LHR:5.2`;
- admissible return to bounded comparison: `E.17.AUD.LHR:5.4`;
- admissible application of whole-unit discipline: `E.17.AUD.LHR:5.5`.

#### E.17.AUD.LHR:3.3 - Load-bearing extension

If the local case is close to a neighbouring-pattern boundary and the ordinary card already stabilizes the unit, add these checks:
- overloaded local lexical head;
- restored lexical-head kind;
- restored active local reading;
- restored primary entity or relation named by value/claim;
- restored carried move or question under repair;
- restored outside-work boundary;
- any family, governing pattern, and primary-entity/relation distinction now made explicit;
- governing-pattern and project-side-reference decision.

Use that extension as the assurance section only when ordinary repair is already holding and the remaining risk is misuse at a neighboring-pattern boundary.
It is for the stay-local repair disposition, not for re-deciding whether the case really belongs in `E.17.ID.CR` or `E.17.AUD.OOTD`.
If the ordinary card now shows one stable local repair plus one bounded comparative review question, apply `E.17.ID.CR` before opening the extension.
If the ordinary card still shows publication-unit reading instability after local repair, apply `E.17.AUD.OOTD` before adding declaration weight here.
Do not use it to rescue a unit whose publication-unit reading still shifts, and do not turn it into a second rule sheet.

#### E.17.AUD.LHR:3.4 - Ordinary repair order

Use this order when one local lexical head is carrying too much:
1. name the overloaded word;
2. restore the lexical-head kind;
3. restore the active local reading;
4. restore the active primary entity or relation named by value/claim when one is active;
5. restore the carried move or question under repair, if any;
6. restore any family, governing pattern, and primary-entity/relation distinction and nearest outside-work boundary the sentence is relying on;
7. decide which of three repair dispositions is honest: stay with local repair, return the case to bounded comparison, or apply publication-unit discipline.

A narrowing qualifier alone does not count as restoration.
Treat this order as one local repair aid, not as a canonical flow.
Steps 1-6 restore the overloaded local lexical head; step 7 classifies what the repaired unit can honestly do next.
If step 6 keeps reopening because the same unit still cannot hold one stable primary entity of concern, one carried move, and one outside-work boundary, stop local repair and apply `E.17.AUD.OOTD`.
If the local lexical head is now honest and the only remaining question is one bounded contrast over already available source epistemes or publications, apply `E.17.ID.CR` instead of escalating the local card into a heavier record by habit.
If the local lexical head is honest and no neighboring reading has become primary, stop here rather than manufacturing extra extension weight.

