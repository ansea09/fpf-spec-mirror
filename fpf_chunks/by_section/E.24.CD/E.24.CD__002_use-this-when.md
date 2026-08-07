---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection and First-Use Disposition"
section_id: "E.24.CD:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__002_use-this-when.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "E.24.CD — Ontic Candidate Detection and First-Use Disposition"
  - "E.24.CD:0 — Use This When"
line_start: 88495
line_end: 88523
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

### E.24.CD:0 - Use This When

Use this pattern when a recurring word, card, table, schema, diagram, record, draft pattern row, or field bundle looks like a new FPF subject and the author must decide what to do next.

Typical moments:

- one word such as "process", "source", "quality", "architecture", "problem", "view", "role", "function", "mechanism", or "method" points to several FPF objects or claims at once;
- several patterns repeat a similar declaration, participant list, or relation rule;
- a project data structure looks concept-shaped, although it may be only a claim-bearing episteme, publication form, representation, or local record;
- a draft ToC row names a family that no current pattern yet governs;
- a proposed `U.*` kind feels useful, but it may duplicate a current kind or direct relation.

**Primary EntityOfConcern.** When the author records this choice in a C.2.1 episteme, its EntityOfConcern is the subject already identified under a direct pattern. If that subject cannot yet be identified, use the source episteme or expression entity whose inquiry remains open. The visible form and the note recording the disposition are not substitutes.

**First useful move.** Write one plain sentence: “For this work or decision, we need to know or do `<action>` about `<subject>`.” Then ignore the wrapper long enough to recover the subject, the needed claim, and the current pattern that governs it. Apply the first truthful disposition in section 4.

**What goes wrong if missed.** FPF grows shadow ontology. A table becomes a kind; a field label is mistaken for a relation-participant meaning; a filled field is treated as an actual relation participant merely because it occupies a column; a card becomes the subject; or a convenient word creates a second ontology over values and relations that already have governing patterns.

**What this buys.** The author identifies one usable governing pattern without filling a candidate record or maintaining a registry. A genuine durable ontic must still pass E.24's full identity and relation test; simpler cases stop with their direct governing pattern, local classification, description or publication handling, wording repair, or a precise unresolved question.

**Not this pattern when.**

- If one existing governing pattern already states the needed claim, use it directly.
- If a local kind, criterion, candidate judgment, or extension is already the question, use `C.3`, `C.3.1`, and `C.3.2`.
- If the current question is a description episteme, use `C.2.1` for its identity and the subject-specific description pattern when one applies. For view membership, publication form or occurrence, representation, or carrier, use `E.17.0`, `E.24.PUB`, or `C.29`.
- If the subject and governing claim are clear and only the wording hides them, use `E.10`, `E.10.ARCH`, or the applicable precision-restoration pattern.
- If a durable ontic has already been selected, use `E.24`; if a durable public `U.*` kind is separately at issue, use `E.24.UK`.
- If the work is comparing architecture alternatives, construct the evaluation through `A.19.ECS`.

