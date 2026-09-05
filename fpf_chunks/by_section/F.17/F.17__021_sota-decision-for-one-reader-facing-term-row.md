---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:16"
section_title: "SoTA Decision for One Reader-Facing Term Row"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__021_sota-decision-for-one-reader-facing-term-row.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:16 — SoTA Decision for One Reader-Facing Term Row"
line_start: 99537
line_end: 99552
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:16 - SoTA Decision for One Reader-Facing Term Row

**Question and selected answer.** At the effort of settling one reusable term, what must a reader recover beyond a familiar label, and what apparatus can be left out? Applying `E.8:11`, the selected answer is one readable row that returns separately to the named value, naming decision, exact local sense, permitted and blocked citation uses, and the condition that reopens the row. Create it only when that reader-facing route is needed.

**The lightweight serious rival.** The [OntoLex Community Report, Overview, Purpose, Core, and Semantics](https://www.w3.org/2016/04/ontolex/), permits the core module alone. A fair one-term comparator is a lexical entry with a form, a sense and a reference to the already defined ontology entity, plus only the usage notes this application needs. It does not require a full lexicon, morphology or syntax graph; it is not intended to define the ontology itself. **Adapt** its expression/sense/reference separation in `5.1` and `7`. Its extensibility also permits notes or a view to expose the same decision content as an F.17 row.

The choice is therefore not between a cheap row and an unnecessarily large graph. Hold the term, target, use conditions, and maintenance obligation fixed. A bare label or bare form/sense/reference chain lets the reader find the expression and target, but leaves the naming choice, blocked use, and reason to revisit it unstated. Adding those statements to the lightweight rival closes that gap; a generated readable view of those same statements is an acceptable way to express the F.17 row. A different vocabulary or file format is not, by itself, an improvement or a second naming result.

For an ordinary reader inspecting one term, select the explicit row because the decision and return are visible together. The deliberate trade-off is maintaining a truthful reader-facing projection instead of asking that reader to reconstruct it from linked lexical statements. When lexical tooling already produces that projection, keep it and avoid a second editable source. Conversely, when morphology, translation, or machine lexicon exchange is the actual use, the core model and only its needed extensions may be the better carrier. No measured speed advantage, blanket cost superiority, or replacement of OntoLex is claimed.

**Exact effect and countercases.** Steps 1–5 of section `4`, together with sections `6` and `14`, stop at ordinary wording, a local card, or a cell when no row is needed; steps 7–8 of section `4`, together with sections `5.1` and `7`, make the row's returns explicit and keep later publication separate. The countercase in `12.2` prevents a state label from becoming a system-role kind, `12.4c` leaves ordinary mantra wording without rows, `12.4h` distinguishes a reusable structure kind from one selected instance, and `12.4i` returns the Reference name to its product-form rule without creating a product or lookup Work. These cases supply the FPF-local reason for the added decision content; the OntoLex report supplies the rival's lexical modeling capability, not validation of FPF ontology. **Reject** mandatory full-lexicon modeling, raw label familiarity as sufficient reader recovery, and the inference that a row makes its referent or publication real.

**Reopen.** Recompare when an equally small lexical entry or other presentation exposes the same decision, blocked uses, and exact returns with less reader and maintenance effort; when a generated view drifts from its source; or when the current use needs linguistic distinctions or machine exchange omitted by the row. If the added reader projection no longer changes use, retain the simpler expression of the same content.

Currentness rule: when `F.2`, `F.3`, `F.5`, `F.7`, `F.8`, `F.9`, `F.10`, `F.14`, `F.15`, `F.18`, `C.2.1`, `E.17.0`, `E.24.UK`, `E.24.PUB`, `A.1.1`, `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.10`, `B.3`, `E.10.D2`, or the pattern that defines or constrains the governed value changes the value, kind, membership or obtaining rule, designation, scheme, cell, basis relation, Bridge, bounded-use claim, reliance, status and system-role boundary, edition relation, reference typing, or publication boundary, recheck only the affected rows and worked examples.

