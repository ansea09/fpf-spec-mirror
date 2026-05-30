---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__002_use-this-when.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:0 — Use this when"
line_start: 34867
line_end: 34895
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.A"
  - "A.6.P"
  - "A.6.Q"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.2.1"
  - "E.10"
  - "E.12"
  - "E.17"
  - "E.17.0"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.2"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.9"
  - "F.18"
keywords:
  - "PublicationUnit"
  - "carrier"
  - "claim-bearing episteme"
  - "described entity"
  - "epistemic precision restoration"
  - "grounding relation"
  - "publication face"
  - "remaining admissible reader move"
  - "source wording"
  - "source-expression unpacking"
  - "source-to-FPF transfer"
  - "transfer disposition"
---

### C.2.P:0 - Use this when

**Source-expression unpacking mode.** Use this mode when someone asks to make ordinary language more precise, including intake notes, seminar transcripts, external reviews, project documents, source publications, tool outputs, or other non-FPF prose. The aim is source-local clarification: recover what the sentence might mean, identify candidate kinds and relations, preserve important wording when needed, and produce one clarified phrase, candidate-set note, epistemic precision-restoration note, or transfer disposition. This mode may apply `E.10`, `A.6.P`, `A.6.6`, `F.18`, `A.7`, `E.17`, or another exact FPF pattern as a repair method, but it does not require the source text itself to become FPF-conformant.

**FPF-transfer or conformance mode.** Use this mode when episteme-publication-heavy conformant text or text being promoted into FPF current content relies on loose wording around epistemes, publications, views, publication forms, generic publication faces, governed MVPK faces, bounded publication units, carriers, records, relations, admissible uses, or pattern application. Here the output must be FPF-conformant: exact recovered FPF kind, relation record, relation phrase, tuple-like record, exact project-side FPF kind and reference, or explicit non-transfer disposition.

Use `C.2.P` as epistemic precision restoration for wording whose live object is an episteme/publication/source-transfer construction: source wording, source-local meaning, claim-bearing episteme, publication, view, face, carrier, publication unit, described entity, grounding relation, pattern-application wording, project-side reliance wording, or the disposition by which source expression may or may not become FPF-current wording.

`E.10` governs lexical conformance of a wording use. `C.2.P` governs epistemic precision restoration across the epistemic and publication stack: expression, source-local meaning, recovered FPF kind stack, publication/carrier/view construction, described-entity or grounding relation, admissible reader move, and transfer or non-transfer disposition.

The practical partition is episteme/publication-slot-like, but it is not limited to named `C.2.1` slots. It also includes publication constructions, carrier and face constructions, source-expression-to-current-FPF transfer, and pattern-application wording when those are used as claim-bearing or admissibility-bearing signs. Apply this pattern from `E.10` only when the target governing pattern cannot yet be selected directly because source wording, claim-bearing episteme, publication/carrier construction, project-side reliance, pattern-application wording, or transfer/non-transfer disposition is still unresolved. The pattern-local decision is not a procedure path: it selects source-expression unpacking mode or FPF-transfer/conformance mode, recovers the live episteme-publication stack, chooses recovered-by-value, quote-only, reduced-use-cue, extension-candidate, blocked-transfer, rewrite-incomplete, or not-triggered disposition, and preserves the remaining admissible reader move before any neighboring pattern governs its own invariant.

**Precision-restoration pattern note.** A precision-restoration pattern is an architectural pattern for a recurring complex precision problem whose wording routinely hides several live distinctions. `A.6.P` is relation precision restoration; `C.2.P` is epistemic precision restoration. Architecture or structure precision restoration is admissible only through the exact architecture/structure pattern that governs the live architecture/structure problem, such as `C.30`, `C.30.ASV`, `A.22`, `C.31`, or a later accepted architecture/structure precision-restoration pattern with its own worked cases and `F.18 -> A.6.P`-surviving name. `E.10` detects the language problem and creates the obligation to apply the selected precision-restoration pattern; it does not become that pattern's ontology.

| Problem in the wording | Use this pattern for | Applicable neighboring authority |
| --- | --- | --- |
| Ordinary source text needs more precise language | Source-expression unpacking mode: source-local clarification, candidate kinds and relations, exact wording preservation when needed, clarified phrase, candidate-set note, epistemic precision-restoration note, or transfer disposition. | `E.10`, `A.6.P`, `A.6.6`, `F.18`, `A.7`, `E.17`, or another exact pattern as a repair method only for the selected load. |
| Text is being promoted into FPF current content | FPF-transfer/conformance mode: exact recovered FPF kind, relation record, relation phrase, tuple-like record, exact project-side FPF kind and reference, or explicit non-transfer disposition. | `E.10` plus the exact governing pattern for each recovered load. |
| Claim-bearing episteme, described entity, grounding relation, publication, view, face, carrier, publication unit, source relation, target relation, or bounded publication-unit wording is live | Recover the kind stack and relation/publication construction before accepting the sentence. | `C.2.1`, `A.7`, `E.17.0`, `E.17`, MVPK, and local episteme/publication patterns. |
| Relation, comparison, dependency, support, sameness, grounding, mapping, endpoint, admissible-use, or project-side reliance is live | Recover the relation/load before treating the wording as current FPF content. | `A.6.P`, retained A.6.P specializations, `A.6.B`, and the exact evidence, work, decision, assurance, causal-use, mathematical-lens, or quality pattern when live. |
| A reusable term or stable local head is being chosen | Prevent a broad replacement from becoming a new FPF term by taste. | `F.18`, with `E.10:0.2` replacement-candidate anti-umbrella rule. |
| The repair would leave correct typing but no useful reader action | Treat the rewrite as incomplete. | `E.2`, `E.8`, `E.10:6.2`, `E.12`, and the exact named FPF pattern that carries the live claim. |

**Ordinary-language survival.** Ordinary words remain admissible until the sentence gives them FPF-kind, relation, authority, evidence, admissibility, work, gate, decision, bridge, or reliance load. `Source` may stay ordinary when it only means where a quote came from; `view` may stay ordinary when it means what the reader sees and not `U.View`; `route` may stay ordinary navigation prose; `support` may stay ordinary help. Repair by load-bearing sentence function, not by trigger word alone.

**Not this pattern when.** `C.2.P` is not the governing pattern for every recovered construct. General FPF lexical conformance stays under `E.10`; stable reusable naming under `F.18`; relation precision under `A.6.P`; A.6.B law-, admissibility-, deontic-, and effect-claim boundary splitting under `A.6.B`; object-description-carrier separation under `A.7`; view and publication discipline under `E.17` and `E.17.0`; architecture and structural description adequacy under `C.30`, `C.30.ASV`, `A.22`, `C.31`, or the exact architecture/structure pattern; project work, evidence, gate, decision, method, action-invitation, assurance, and engineering-justification claims under their exact FPF patterns. When one of those claims is live, this pattern supplies source-expression unpacking and rewrite disposition; the exact named FPF pattern supplies its invariant.

**Do not punish clarity.** Prefer the clearest ordinary head that preserves kind, relation, and admissible use. Do not replace a clear plain phrase with a technical phrase unless the technical phrase blocks a live false reading or is needed for accepted stable FPF naming. In an ordinary case, `reader help`, `source-pointer-only`, or `comparison only` may be better than a more technical phrase.

