---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReviewUnit - bounded comparison over comparative review units"
section_id: "E.17.ID.CR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__008_conformance-checklist.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "E.17.ID.CR — ComparativeReviewUnit - bounded comparison over comparative review units"
  - "E.17.ID.CR:7 — Conformance Checklist"
line_start: 84515
line_end: 84557
dependencies:
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.9"
  - "A.6.P"
  - "B.5.2"
  - "B.5.2.0"
  - "C.11"
  - "C.2.2a"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "F.9"
  - "F.9.1"
keywords:
---

### E.17.ID.CR:7 - Conformance Checklist

A conformance check is retained only if it changes the next bounded use of the comparative review unit, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared bounded use.

Use ID.CR-Core for ordinary comparison notes. Conditional rows apply only when the note touches neighboring-pattern relation, bridge declaration, or reader-fit fields. For fuller mixed-case read, read this checklist together with the neighboring pattern discipline and the boundary conditions gathered in this section.

**Assurance recovery note.** Use this checklist as a heavier check of the already-declared ComparativeReviewUnit governing rule, not as a second rule list. If a row cannot be recovered through the ordinary seven-row card, the nearest worked slices, or the practical safeguards already named in the pattern, the case is not yet stable enough to rely on checklist prose alone.

#### E.17.ID.CR:7.1 - ID.CR-Core ordinary checks

1. **CC-ID-1 - Bounded comparative review unit is explicit.**
   The pattern makes clear that the comparison unit is a bounded comparative review unit rather than the whole review or decision work or a hidden mental act.
2. **CC-ID-2 - Source references and comparison criterion are explicit.**
   A reviewer can see what already-fixed source episteme or source publication is being interpreted and what declared comparison criterion or contrast is carrying the lift.
3. **CC-ID-3 - The lift stays bounded.**
   The ordinary card keeps bounded lift, blocked downstream claim or effect, world-contact limit, and boundary trigger visible before any neighboring claim can be read from the unit.
4. **CC-ID-6 - Neighboring-pattern boundaries stay visible.**
   When the boundary trigger fires, the neighboring FPF pattern carries that prompt, ontology, action, gate, authority, or downstream claim instead of leaving it hidden inside comparative prose.
5. **CC-ID-8 - The review unit does not over-claim authority.**
   The unit remains review-only and non-executive; stronger authority use is carried only by the named governing pattern and project-side FPF kind and reference.

#### E.17.ID.CR:7.2 - ID.CR-Conditional checks

1. **CC-ID-4 - Base-case governing-pattern relation is explicit.**
   A reviewer can tell why the case does not really belong to `A.6.3.*`, an F.9 Bridge or bounded-use branch, an F.9.1 stance-note branch, `E.17.EFP`, `B.5.2(.0)`, `OntologicalReframing`, or `A.6.4`.
2. **CC-ID-5 - Bridge declaration does not hide.**
   If the case depends on bridge-mediated comparison, `bridgeOccurrenceRef` and `boundedUseClaimRef` are required. The latter resolves a claim whose `EntityOfConcern` is that Bridge and whose use/direction/rule/loss/polarity tuple matches the comparative unit. Positive use requires affirmative polarity and, when A.10 or B.3 is triggered, current reliance for that exact use; degraded reliance narrows it, while a negative, abstaining, reopened, evidence-needed, blocked, or mismatched result stops it. Authorization and actual comparative-review Work remain separate. Optional `bridgeCardRef` remains packaging; optional `bridgeStanceRef` resolves a separate F.9.1 episteme whose `EntityOfConcern` is that claim.
3. **CC-ID-7 - Reader-fit stays bounded.**
   `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `boundedComparativeUse`, and `overreadRisk` are visible when needed, but they do not create an authority claim that the unit does not carry.

**Checklist recovery map.** If an assurance-side reader wants to recover one checklist row by value, use the nearest ordinary card row and worked recovery below before treating the checklist as self-sufficient:

| Checklist row | Recover through first | Nearest worked or practical recovery |
| --- | --- | --- |
| `CC-ID-1` | `E.17.ID.CR:4.3.b.a` rows **Reviewed source** and **Shared review frame and alternative identities** | `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` |
| `CC-ID-2` | `E.17.ID.CR:4.3.b.a` rows **Reviewed source**, **Source references**, and **Bounded lift** | `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` |
| `CC-ID-3` | `E.17.ID.CR:4.3.b.a` rows **Bounded lift**, **Blocked downstream claim or effect**, and **World-contact limit** | `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` |
| `CC-ID-4` | near-top **Neighboring-work boundary**, **Quick working-fit check**, and `E.17.ID.CR:4.5 - Neighboring-work boundary glance` | `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` |
| `CC-ID-5` | `E.17.ID.CR:4.3.d` bridge-declaration fields plus `E.17.ID.CR:4.2` neighboring patterns | `E.17.ID.CR:5.4.1`, `E.17.ID.CR:5.4.2`, `E.17.ID.CR:5.4.3` |
| `CC-ID-6` | `E.17.ID.CR:4.3.b.a` row **Boundary trigger** plus the near-top boundary corridor | `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` |
| `CC-ID-7` | `E.17.ID.CR:4.3.d` interpretant-side fields, kept subordinate to the ordinary card and blocked downstream claim or effect | `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.b` |
| `CC-ID-8` | `E.17.ID.CR:4.3.b.a` rows **Blocked downstream claim or effect** and **World-contact limit** | `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` |

