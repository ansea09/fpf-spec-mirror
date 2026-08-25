---
chunk_kind: "child"
pattern_id: "E.11.PFP"
pattern_title: "Framework Publication Form Profile"
section_id: "E.11.PFP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PFP/E.11.PFP__005_solution.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "E.11.PFP — Framework Publication Form Profile"
  - "E.11.PFP:4 — Solution"
line_start: 76835
line_end: 76924
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

Between the title and ToC, retain only the shortest public cues already justified by product use. An exact edition designation or locator belongs there only when its possible values change the reader's next use, reliance, return, language, dependency, or access choice. When such a cue is present, project it from one product-owned edition or relation record; do not maintain a second editable copy. Add authorship, credit, date, lifecycle, dependency, language, or access only under the same next-working-move test. A date is a cue, not edition identity, and a visible lifecycle word is not evidence of acceptance, currentness, maintenance, availability, access, or authorization.

Reader front matter extends from the opening title through the Readme and Preface up to the first pattern-body collection H1. It must not contain campaign keys; candidate, review, or result identifiers; local disk or repository paths; source or candidate digests; Git commits or blobs; generated comments; build commands; machine warnings; or "do not edit" instructions. Detailed edition, provenance, rebuildability, and maintenance records remain adjacent maintainer evidence or product-declared reference-tail material unless a separately selected public use justifies a reader-facing projection.

#### E.11.PFP:4.2 - Put public units into the established Table of Contents

Immediately after the single `# Table of Contents` H1, continue the product's established ToC grammar. Represent the exact Readme and Preface before the logical pattern index using the same kind of labelled segment and rows already used for non-pattern units in that product. When an established ToC already represents Preface and pattern groups, add Readme there; do not invent a generic `Publication route`, a second mini-menu, or a new table shape. A non-pattern publication unit receives no fabricated PatternID. Its product-declared entry remains mechanically recognizable and, when the carrier supports links, resolves to the exact unit.

Place the one authoritative logical pattern index after those public-unit entries. It may be one table or several ordered, uniquely labelled Part or placement segments. Every authoritative segment uses:

```text
| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
```

Across all segments, every pattern body has exactly one row, every row resolves to exactly one body, and no PatternID appears twice. A Part label groups rows for navigation; it is not a pattern row, a semantic parent, or another index.

Reserve `Support index — <lookup job>` for a secondary pattern lookup. Its exact header is:

```text
| PatternID | Pattern title | Lookup use |
```

Ordinary relation, source-return, maintenance, and reference tables may cite PatternIDs under truthful headings and other complete headers. Do not infer that they are indexes from their cell values. Reject a second `# Table of Contents`, a `Pattern Index` heading for the same job, an authoritative header outside the authoritative ToC region, or a support heading and header that do not occur together. Public-unit entries are navigation inside the one ToC, not another pattern catalogue.

#### E.11.PFP:4.3 - Give each practical entry five recognizable fields

Start the Readme body with `## Practical entries`. Each `###` entry uses these fields in order:

1. `Situation`;
2. `Question`;
3. `First useful result or honest blocker`;
4. `Start with`; and
5. `Stop or return`.

`Start with` resolves to one current PatternID or a named small route. `Stop or return` gives the ordinary non-use boundary, the sufficient first-result boundary, or the exact missing input. Keep richer branches, tests, and boundary notes when they help the reader; the five fields are a recognition layer, not a ceiling on useful content.

An independently published Readme starts with its exact product-declared Readme H1. If identifying the edition outside the surrounding carrier changes use or return, follow that H1 with the same shortest public cue and then emit `## Practical entries`; otherwise do not duplicate an edition or maintenance record merely to make the file look complete. The standalone Readme is another carrier of the same edition form, not another edition.

This profile keeps the structural keys in canonical English. A translation may translate surrounding prose and values and may add a human-readable gloss, but it does not silently replace or reorder the keys. A translated structural-key profile needs a separately selected recovery and checking rule. Test the translated and low-tool carrier with actual readers and navigation tools rather than treating English parser success as accessibility evidence.

#### E.11.PFP:4.4 - Keep support units and adjacent products distinct

A Readme, Preface, ToC, pattern-body collection, framework-scale structure or coverage account, relation or edition note, and refresh route may be publication units of one framework product when they share its declared readers and use, edition boundary, access, maintainer, and change cadence. A unit does not become another product merely because it is outside the pattern set or stored in another file.

An adjacent result is a separate maintained product when people need to change, cite, use, or maintain it independently. Look for its own useful identity, version or current state, users and use, rule saying what content belongs, access route, maintenance commitment, refresh or retirement rule, or cross-framework reuse or reliance. Examples include a source registry, MethodDescription collection, decision-support publication, inquiry evidence package, practitioner guide, pedagogical companion, catalogue, tool reference, access service, or inquiry programme. This is an open list; those labels do not decide the boundary by themselves.

When the adjacent result is independently maintained, point from the framework to its exact edition or state. An annex may carry a declared snapshot or projection, but it returns to the authoritative product and does not fork it. When no independent boundary is useful and ordinary framework use needs the material, include it as a named support publication unit of the framework product.

One outer presentation carrier may expose several products. The carrier stays neutral: each product keeps its own identity, edition or state, status, form, access, and maintenance boundary. Apply this profile only to FPF, DPF, or LPF constituents. A catalogue, evidence package, guide, service, programme, or other non-framework product uses the form selected for its own kind and receives no invented framework family, dependency field, or pattern index.

DRRs, build manifests, quality runs, digests, logs, and campaign state are process or maintainer evidence by default. They become reader products only after a separately selected public use gives them their own product boundary.

#### E.11.PFP:4.5 - Check syntax and product truth at the right boundary

The common form check handles only recoverable syntax and projection agreement:

- the product-declared title and Readme H1, the compact opening, and absence of prohibited development or machine material from reader front matter;
- the required H1 sequence plus the product-declared body and reference tail;
- product-declared Readme and Preface entries in the established ToC grammar, before the logical pattern index, with no generic rival mini-menu;
- authoritative index segments, aggregate row/body bijection, duplicates, and reserved support-index grammar;
- the Readme heading and five ordered fields; and
- equality and source agreement of every optional public cue that is actually projected.

For Markdown grouping, one canonical bounded invocation runs the focused source-hazard guard and a parser-backed render together. It returns the rendered heading outline and block, list, table, code, and link structure for inspection while the candidate is already loaded. The agent does not discover a second renderer or reread the same file merely to close that form question. A clean mechanical result supports but does not replace the reader-visible judgement.

The product-specific check compares every visible cue with the exact edition or relation record from which it was projected and checks the product-specific body, reference tail, and any pinned compact-front shape. A syntax-valid but unresolved value fails there. A field absent from the public opening is not a form defect unless a selected reader use and product-specific rule require it.

Neither check decides framework scale from pattern count. Report `pattern_count = 1` as a diagnostic. Use E.4, E.4.PFAD, E.4.DPF.DA, E.11, E.21, and the applicable subject patterns to judge whether the result is a usable pattern language for its declared field and first use.

#### E.11.PFP:4.6 - Return the form result without overclaiming

Return the exact framework edition, edition-record source, carriers checked, form units found, public-cue agreement, logical-index result, practical-entry result, product-specific tail checked, and every mismatch or unresolved ref. Say separately whether the edition, carrier, publication occurrence, availability, currentness, or framework adequacy has an applicable result. Do not infer those claims from form conformance.

