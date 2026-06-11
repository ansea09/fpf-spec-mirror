---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReading — bounded comparative reading over comparative review units"
section_id: "E.17.ID.CR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__008_conformance-checklist.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "E.17.ID.CR — ComparativeReading — bounded comparative reading over comparative review units"
  - "E.17.ID.CR:7 — Conformance Checklist"
line_start: 65201
line_end: 65243
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

A conformance check is retained only if it changes the next admissible use of the comparative review unit, blocks a concrete overclaim, or preserves a source reference or reopen condition needed for the declared admissible use.

Use ID.CR-Core for ordinary comparison notes. Conditional rows open only when the note touches neighboring-pattern relation, bridge declaration, or reader-fit fields. For fuller mixed-case read, read this checklist together with the neighboring pattern discipline and the boundary conditions gathered in this section.

**Assurance recovery note.** Read this checklist as a heavier read-back of the already-declared ComparativeReading governing rule, not as a second rule list. If a row cannot be recovered through the ordinary seven-row card, the nearest worked slices, or the practical safeguards already named in the pattern, the case is not yet stable enough to rely on checklist prose alone.

#### E.17.ID.CR:7.1 - ID.CR-Core ordinary checks

1. **CC-ID-1 - Bounded comparative review unit is explicit.**
   The pattern makes clear that the comparison unit is a bounded comparative review unit rather than the whole review or decision work or a hidden mental act.
2. **CC-ID-2 - Source references and comparison basis are explicit.**
   A reviewer can see what already-fixed source episteme or source publication is being read and what declared comparison basis or contrast is carrying the lift.
3. **CC-ID-3 - The lift stays bounded.**
   The pattern keeps the comparative claim visibly narrower than bridge licence, explanation governance, prompt opening, ontology shift, or guidance carrying approval, gate, release, policy, assurance, adjudication, or authority-reference claim.
4. **CC-ID-6 - Neighboring-pattern boundaries stay visible.**
   Prompt-worthiness, ontology-shift claim, or action, gate, approval, rollout, release, policy, assurance, or adjudication use leads to an explicit neighboring FPF pattern rather than staying hidden inside comparative prose.
5. **CC-ID-8 - The review unit does not over-claim authority.**
   The unit is still review-only and non-executive and does not present itself as substitution licence, gate guidance, or action authority.

#### E.17.ID.CR:7.2 - ID.CR-Conditional checks

1. **CC-ID-4 - Base-case governing-pattern relation is explicit.**
   A reviewer can tell why the case does not really belong to `A.6.3.*`, `F.9.1`, `E.17.EFP`, `B.5.2(.0)`, `OntologicalReframing`, or `A.6.4`.
2. **CC-ID-5 - Bridge declaration does not hide.**
   If bridge-mediated comparative relation is live, `bridgeCardRef` is required; optional `bridgeStanceRef` remains visible and subordinate to that existing bridge card.
3. **CC-ID-7 - Reader-fit stays bounded.**
   `targetUserModel`, `interactionMode`, `contrastiveQuestion`, `allowedUse`, and `misuseRisk` are visible when needed, but they do not open an authority claim that the unit does not carry.

**Checklist recovery map.** If an assurance-side reader needs to cash one checklist row out by value, use the nearest ordinary card row and worked recovery below before treating the checklist as self-sufficient:

| Checklist row | Recover through first | Nearest worked or practical recovery |
| --- | --- | --- |
| `CC-ID-1` | `E.17.ID.CR:4.3.b.a` rows **Reviewed source** and **Shared review frame and alternative identities** | `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` |
| `CC-ID-2` | `E.17.ID.CR:4.3.b.a` rows **Reviewed source**, **Source references**, and **Bounded lift** | `E.17.ID.CR:5.4.5`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.a` |
| `CC-ID-3` | `E.17.ID.CR:4.3.b.a` rows **Bounded lift**, **Unsupported downstream claim or effect**, and **World-contact limit** | `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` |
| `CC-ID-4` | near-top **Neighboring-work boundary**, **Quick working-fit check**, and `E.17.ID.CR:4.5 - Neighboring-work boundary glance` | `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` |
| `CC-ID-5` | `E.17.ID.CR:4.3.d` bridge-declaration fields plus `E.17.ID.CR:4.2` neighboring patterns | `E.17.ID.CR:5.4.1`, `E.17.ID.CR:5.4.2`, `E.17.ID.CR:5.4.3` |
| `CC-ID-6` | `E.17.ID.CR:4.3.b.a` row **Boundary trigger** plus the near-top boundary corridor | `E.17.ID.CR:5.4.7` through `E.17.ID.CR:5.4.10` |
| `CC-ID-7` | `E.17.ID.CR:4.3.d` interpretant-side fields, kept subordinate to the ordinary card and unsupported downstream claim or effect | `E.17.ID.CR:5.4.4`, `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.6.b` |
| `CC-ID-8` | `E.17.ID.CR:4.3.b.a` rows **Unsupported downstream claim or effect** and **World-contact limit** | `E.17.ID.CR:5.4.6`, `E.17.ID.CR:5.4.10`, `E.17.ID.CR:5.4.11` |

