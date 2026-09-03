---
chunk_kind: "child"
pattern_id: "E.4.PFIP"
pattern_title: "Principle-Framework Publication Integration and Preservation"
section_id: "E.4.PFIP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFIP/E.4.PFIP__005_solution.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "E.4.PFIP — Principle-Framework Publication Integration and Preservation"
  - "E.4.PFIP:4 — Solution"
line_start: 72348
line_end: 72447
dependencies:
  - "C.2.1"
  - "C.33"
  - "C.34"
  - "E.11"
  - "E.17"
  - "E.24.PUB"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFIP"
  - "E.8"
keywords:
---

### E.4.PFIP:4 - Solution

Run two independent comparisons over one candidate framework publication:

- **accepted source to candidate:** whether each accepted source contribution was incorporated into the named part of a candidate publication-form expression without changing its accepted meaning or use; and
- **predecessor to candidate:** whether the candidate preserves the complete predecessor publication outside accepted content changes.

The predecessor-to-candidate question has two branches. Use a one-to-one expression comparison for an eligible predecessor/candidate pair. Use an allocation comparison for a non-one-to-one publication-form change, including every split or merge even when a narrower one-to-one pair also survives.

These two comparisons and the two predecessor branches are parts of the method, not new FPF kinds. When a later use needs the conclusion as a reusable episteme, identify it under `C.2.1` and state the later reliance separately.

#### E.4.PFIP:4.1 - Bound the candidate and accepted inputs

Identify:

- the candidate FPF, DPF, or LPF edition and declared publication use;
- every accepted source contribution included in this candidate edition;
- every candidate `PublicationFormExpressionRelation` occurrence and its selected edition, publication form, and bounded-use declaration;
- the corresponding carriers and publication occurrences only when their identities affect the comparison; and
- every predecessor expression whose continuity, replacement, retirement, split, merge, or use change is claimed.

Complete the accepted input set before assembly. If one source contribution changes a public entry, required input, result, field meaning, action order, stop, return, or another consumed interface, either include the affected public entries and direct consumers in this candidate or leave that contribution out until they can be updated with it.

For each accepted source contribution, record the candidate publication-form expression and the passage, field, relation, cue, or selected structure intended to incorporate it. A source contribution with no corresponding predecessor content is an accepted addition. Changing or retiring predecessor content needs an accepted content decision; changing or retiring a publication form is not such a decision.

Use `E.24.PUB` to keep the framework edition, publication form, expression relation, carrier, bearing relation, audience, bounded use, and publication occurrence distinct. Use the smallest explicit statement that supports the comparison.

#### E.4.PFIP:4.2 - Compare accepted sources with candidate expressions

After assembly, inspect every accepted source contribution in the named part of its candidate publication-form expression.

For each contribution, ask whether the candidate preserves the selected claim, action, result, boundary, relation, structure, or other content that made the contribution acceptable. Classification by filename, heading, or copied wording is insufficient when the receiving use changed.

Classify each accepted source contribution with one of these outcomes:

- incorporated as accepted;
- incorporated with an accepted content change;
- missing or only partly incorporated;
- placed where the intended reader or consumer cannot use it; or
- blocked because the accepted source contribution or intended candidate expression part cannot be recovered.

The checkable traversal can retain an ordinary positive classification without adding a prose row. This comparison establishes source carry-through only. It says nothing yet about unrelated predecessor content.

#### E.4.PFIP:4.3 - Compare one eligible expression pair

One preservation comparison follows one eligible pair: one predecessor `PublicationFormExpressionRelation` occurrence and one candidate occurrence.

A pair is eligible only when both expressions have the same declared bounded use and either:

- retain publication-form identity under the FPF pattern that defines or constrains that form; or
- are identified by an accepted one-to-one replacement or continuity decision.

The same broad use alone does not pair two forms when several forms serve that use.

Before concluding preservation, select one complete, form-appropriate comparison inventory. The inventory names every predecessor claim, instruction, boundary, field, relation, cue, or selected structure required for the declared use. Beside each entry, record why it matters—the FPF pattern that defines or constrains the form, or another accepted comparison basis—and any candidate correspondence. The inventory is a comparison aid; it does not make the named kinds members of one new kind.

For comparable text expressions, deletion and replacement spans expose independently actionable predecessor claims, instructions, and boundaries. Treat this as one comparison technique, not the definition of completeness. For a card, diagram, retrieval form, or another expression without shared span coordinates, inventory the claims or selected structures required for the declared use. Use the FPF pattern that defines or constrains that form and, when applicable, `C.33` to state captured and lost structure or `C.34` to state a bounded structural correspondence.

Traverse the entire predecessor inventory. For each named content or selected structure, record one outcome:

- matched by content or selected structure in one or more named candidate expression parts;
- intentionally changed or retired by an accepted content decision;
- accidentally lost; or
- blocked because the correspondence or decision cannot be established.

Classify candidate content or selected structure without a predecessor correspondence as an accepted or unexpected addition. If no applicable FPF pattern or accepted comparison basis makes a complete inventory selectable for the declared use, stop at `missing form-comparison basis`. Carrier identity, visual similarity, or a green build cannot complete the comparison.

#### E.4.PFIP:4.4 - Allocate a non-one-to-one form change

An accepted publication-form addition, retirement, split, merge, or use-change decision names the affected predecessor and candidate expression occurrences and any narrower one-to-one continuity that survives. It authorizes the change in publication forms. It does not dispose of predecessor content.

Run a separate allocation comparison for every accepted form change that leaves an affected predecessor expression outside an eligible one-to-one pair, and for every split or merge even when narrower pairs survive.

1. Select a complete inventory for every predecessor expression named by the form-change decision.
2. For every named predecessor content or selected structure, record one or more corresponding candidate expression parts, an accepted content-change or content-retirement decision, an accidental-loss result, or a blocker.
3. Allow predecessor content to appear in several candidate expressions and several predecessor inventory entries to correspond to one candidate expression part.
4. Inspect the complete inventories of the named candidate expressions and classify candidate content or selected structure without a predecessor allocation as accepted or unexpected additions.
5. Reuse an eligible-pair result as correspondence evidence when applicable, but do not let it replace the allocation traversal.

Keep every named expression, carrier, edition, and publication occurrence separate throughout the allocation. The allocation comparison is the method for reasoning across them; it does not need a new collective publication kind.

Without the form-change decision, stop at `missing publication-expression continuity decision`. Without a complete selectable predecessor inventory, stop at `missing form-comparison basis`. Without an outcome for any named predecessor content or selected structure, return accidental loss or a blocker. Retiring a form never retires its content by implication.

#### E.4.PFIP:4.5 - Complete the affected-publication comparison and return

Identify every affected publication-form expression relation occurrence and, when carrier or publication identity affects the comparison, its bearing and publication relations. Run every applicable eligible-pair comparison and allocation comparison. Check each shared public entry or direct consumer once across the comparisons, while preserving the separate expression results that depend on it.

Return a bounded preservation conclusion with:

- accidental losses and the expression parts that need repair;
- accepted content changes or retirements that account for a predecessor difference;
- unexpected additions;
- unresolved candidate correspondences or content-change questions;
- blockers and the comparisons they prevent; and
- the declared use for which the conclusion holds.

The complete traversal remains checkable even though unchanged predecessor content and selected structure receive no prose rows. A build result, successful accepted-source comparison, pattern-quality result, or package-adequacy result cannot substitute for it.

When the framework publication has no predecessor, perform the accepted-source comparison, inspect the complete candidate inventory, check changed public entries and direct consumers, and use the applicable package evaluation. When an unchanged edition is merely republished through a different form or carrier, use `E.24.PUB`, `E.17`, `C.33`, and `C.34` for the changed publication claims. Use this pattern only when accepted-source integration or complete framework-publication continuity is the live problem.

