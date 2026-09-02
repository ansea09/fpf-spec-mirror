---
chunk_kind: "child"
pattern_id: "E.11.PFP"
pattern_title: "Framework Publication Form Profile"
section_id: "E.11.PFP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PFP/E.11.PFP__005_solution.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "E.11.PFP — Framework Publication Form Profile"
  - "E.11.PFP:4 — Solution"
line_start: 79812
line_end: 79868
dependencies:
  - "E.11"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFR"
  - "G.11"
keywords:
  - "& Search Queries"
  - "Dependencies"
---

### E.11.PFP:4 - Solution

Apply one common reader-facing publication form to one FPF, DPF, or LPF edition. The profile is the reusable rule for that form. It is not the form itself, the presentation carrier that bears the form, the edition expressed by it, or the publication occurrence that makes the edition available.

#### E.11.PFP:4.1 - Preserve the compact product opening

For an all-in-one Markdown publication, preserve the product-declared compact opening and use this H1 route:

1. `# <product-declared publication title>`;
2. `# Table of Contents`;
3. the exact product-declared Readme H1;
4. the exact product-declared Preface H1;
5. the pattern bodies or pattern collection in the order selected by that edition; and
6. reference and maintenance material under headings declared by the product pattern.

The title and Readme H1 are separate product declarations. A checker receives both exact strings; it does not derive the Readme H1 by concatenating `Readme` to a longer carrier title. The common profile does not insert a metadata block, edition record, warning, or other lines into a compact predecessor opening merely to make products look alike. A product-specific builder may pin a compact front shape, including the line at which the ToC begins, when that shape protects an established reader entry.

Between the title and ToC, retain only the shortest public cues already justified by product use. An exact edition designation or locator belongs there only when its possible values change the reader's next use, reliance, return, language, dependency, or access choice. When such a cue is present, project it from one product-owned edition or relation record; do not maintain a second editable copy. Add authorship, credit, date, dependency, language, access, or a product-declared maintenance status, support window, or currentness window only under the same next-working-move test. A date is a cue, not edition identity, and a visible status or window is not evidence of acceptance, currentness, maintenance, availability, access, or authorization.

Reader front matter extends from the opening title through the Readme and Preface up to the first pattern-body collection H1. It must not contain campaign keys; candidate, review, or result identifiers; local disk or repository paths; source or candidate digests; Git commits or blobs; generated comments; build commands; machine warnings; or "do not edit" instructions. Detailed edition, provenance, rebuildability, and maintenance records remain adjacent maintainer evidence or product-declared reference-tail material unless a separately selected public use justifies a reader-facing projection.

#### E.11.PFP:4.2 - Put public units into the established Table of Contents

Immediately after the single `# Table of Contents` H1, continue the product's established ToC grammar. Represent the exact Readme and Preface before the logical pattern index using the same kind of labelled segment and rows already used for non-pattern units in that product. When an established ToC already represents Preface and pattern groups, add Readme there; do not invent a generic `Publication route`, a second mini-menu, or a new table shape. A non-pattern publication unit receives no fabricated PatternID. Its product-declared entry remains mechanically recognizable and, when the carrier supports links, resolves to the exact unit.

Place the one authoritative logical pattern index after those public-unit entries. It may be one table or several ordered, uniquely labelled Part or placement segments. Every authoritative segment uses:

```text
| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
```

Across all segments, every pattern body has exactly one row, every row resolves to exactly one body, and no PatternID appears twice. A Part label groups rows for navigation; it is not a pattern row, a semantic parent, or another index.

PatternID, title, Part, and `§` position remain separate even when one row displays them together. PatternID supplies the stable public address within the named framework; the title explains the pattern; Part and `§` show where the current edition places it. Within each Part, the ToC rows and pattern bodies follow the same order. That order need not ascend by PatternID, and moving or retitling a pattern does not by itself change its PatternID.

When the surrounding text does not already identify the framework, name the framework together with the PatternID. To select the body published in one edition, also name that framework edition. For a DPF, `E.4.DPF` supplies the choice of reference code and local locator, and the continuity decision; this profile only makes the selected distinctions visible in the publication.

Reserve `Support index — <lookup job>` for a secondary pattern lookup. Its exact header is:

```text
| PatternID | Pattern title | Lookup use |
```

Ordinary relation, source-return, maintenance, and reference tables may cite PatternIDs under truthful headings and other complete headers. Do not infer that they are indexes from their cell values. Reject a second `# Table of Contents`, a `Pattern Index` heading for the same job, an authoritative header outside the authoritative ToC region, or a support heading and header that do not occur together. Public-unit entries are navigation inside the one ToC, not another pattern catalogue.

#### E.11.PFP:4.3 - Keep one practical-entry set and two visible forms

Start the Readme body with `## Practical entries`. The product maintains one declaration for every selectable example and assigns each key exactly one public form: ordinary practical entry or Practical-Use Card. Each declared key occurs once, at H3 for an ordinary entry or at H4 for a card. A compact locator may precede or follow these examples, but it is a finding aid rather than another editable entry set.

The Readme says plainly that its entries are selected examples, not a catalogue or coverage boundary. It tells the reader to bring the actual question and to use the product's index, direct patterns, or another finding aid when no example fits. The selected examples should make two uses visible without implying that every question belongs to either displayed case:

- an ordinary entry shows how one direct pattern or one bounded direct route can answer a comparatively simple difficulty without a mantra; and
- a Practical-Use Card shows a recurring complex difficulty whose useful answer spans several direct pattern contributions and whose long dependency is easier to retain with a mantra.

Use this ordinary-entry form:

```text
