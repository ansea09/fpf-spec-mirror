---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:0.3"
section_title: "Pattern Kind In Plain Terms"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__005_pattern-kind-in-plain-terms.md"
commit_sha: "7f7c592f4d633e54cdb202d622d6e0e05df41517"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:0.3 — Pattern Kind In Plain Terms"
line_start: 70375
line_end: 70400
dependencies:
  - "E.10"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUR"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.8.ECSPF"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "I.2"
keywords:
  - "). The key words MUST"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT appear inside Definition:/Invariant:/Well-formedness constraint: blocks. When enforceable"
  - "Prevents ambiguity between obligation language and model validity"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SHALL"
  - "SHALL NOT"
  - "SHOULD"
  - "SHOULD NOT"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:0.3 - Pattern Kind In Plain Terms

An FPF pattern supplies action- or judgement-guiding content for a recurring working situation. “Use this pattern” and “apply this pattern” are valid shorthand for a person or another capable system using that content to choose an action or judgement. The pattern episteme itself does not act, decide, perform `U.Work`, or cause a `U.Transformation`.

Call the pattern content a `U.MethodDescription` only when it describes one independently admitted `U.Method` under A.3.2 and that distinction matters to the current claim. Keep the Method and its description episteme separate. A `Solution` can guide future action or help choose a Method without establishing that any dated Work has happened. The intended reader, an actual performer System, local system-role classification, assignment, capability, responsibility, authority, result, and Transformation remain separate whenever those claims are current.

When a pattern or worked case does assert dated `U.Work`, establish the complete A.15.1 and F.6 facts. Name the performer `U.System`, enacted Method, time, and containing System. Name the assignment occurrence that covers the Work and its declared `U.SystemRoleAssignment` species. Preserve every participant required by the species, confirm that the performer is the holder throughout the Work interval, and establish the F.6 link between the Work and assignment. These facts are required for admitted Work even when a short practitioner sentence does not expose the assignment identifier. Expose that identifier only when the receiving claim uses it.

`Pattern application` is metonymic shorthand for user-side use: the user or another capable system recognizes the working situation and uses the pattern content and its `Solution` to shape the next admissible action or judgement. Ordinary guidance creates no fictive performer, assignment, Work, result, or Transformation. `Problem frame`, `Problem`, `Forces`, `Solution`, `Consequences`, worked slices, and anti-patterns carry the description-side guidance. A `Conformance Checklist` checks the authored description and separately evidenced use; it must not replace the `Solution`, manufacture Work, or turn the pattern into a control form.

The primary content-bearing job is constructive action or judgement guidance: the pattern description must say what the user should do or decide so the recurring error does not arise. Error prevention, auditability, and conformance checks are evidence that the guidance is usable; they are not the pattern's center. The first substantive content in the opening `Problem frame` and `Solution` must be positive subject and action guidance: the primary `EntityOfConcern` kind, the first admissible action-guiding move, the practical delta, and the few boundaries needed for that first move. The text must not replace subject content with repeated guards, distinctions, related-pattern mappings, references, mini-rules, definitions, caveats, architecture rationale, or quality or projection evidence unless the repetition adds a new local action, case, evidence value for the user, or first-reading recognition need. Copying distinctions from another pattern's defining or constraining content into this pattern as repeated "do not confuse our EoC with their EoC" prose is the same repetition problem. Boundary doctrine is pattern content like any other doctrine: if an exact distinction, non-use condition, ToC navigation cue, or cited pattern already states it, do not repeat it locally. Cite the short pattern id; identify an exact claim-bearing episteme or `ClaimGraph` only when that identity matters to the receiving use. Add local boundary prose only when it states a documented local confusion and exact stop condition that the existing content does not already state. The repair is to say clearly what this pattern's own `EntityOfConcern` is, not to enumerate the unbounded set of other things it is not.

The same rule blocks pattern-use drift for any FPF object. Name the object by its FPF kind when the kind is known, and do not let “acts”, “routes”, “receives”, “decides”, or an ownership word hide a different relation. For an ordinary neighboring-pattern reference, state what the cited content contributes here—for example, defines a kind, constrains a relation, supplies a test or method, or provides a locator—and cite the pattern id. Identify an exact claim-bearing episteme, `ClaimGraph`, edition, or relation assertion only when that identity changes interpretation, migration, conflict, publication, or reuse. A genuine stop needs no receiver; a reconsideration states its condition and the candidate guidance to consult. Relations are positive claims, not catalogs of absent relations. Detailed discoverability belongs in README, ToC query cues, `E.11`, `I.2`, or retrieval or projection carriers; compact related-pattern statements belong late in `Relations` after the positive subject and action guidance. Ordinary references use ordinary reference forms: a pattern id in prose, a citation, `Builds on`, `Coordinates with`, `Relations`, ToC, README, `E.11`, `I.2`, or a retrieval or projection carrier. Do not repeat them as many conditional sentences or small variants when one compact definition, boundary, table, `Relations`, ToC, README, `E.11`, `I.2`, or retrieval or projection locus already carries the same content family.

Treat precision-restoration problems in pattern prose as one profile with five layers: word, head, and use precision; phrase apparatus; repetition and distribution; actor, text, and carrier separation; and pattern application. Do not add a local row for each new symptom. Use `E.8` to keep positive subject and action guidance first, `F.19` for phrase-level apparatus, `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines or constrains the relevant kind, relation, or use for remaining word, head, and use precision, and `E.21` to measure the combined effect on pattern quality.

A wording cleanup is kind-preserving by default. Before an author accepts a changed FPF-governed phrase as a repair, the pre-repair and post-repair `EntityOfConcern`, kind, relation or claim kind, current ontic slot, relation position, use relation, admissible use, and scope must be recoverable when those items are live. This is a bounded complete preservation check, not an order to formalize ordinary prose or unchanged text and not permission to choose "no edit" as the easy minimum. Leaving text unchanged closes only when the phrase is `not triggered`, ordinary prose, or already satisfied by value with loci; otherwise the finding remains open. Removing a trigger word or replacing a generic head is not a repair when it changes the ontology: for example, a graph-shaped Method cue must not be narrowed into a Work sequence unless an accepted decision explicitly changes the kind and consequences. If a relation, signature, mathematical-lens, system-role kind or assignment, Method, Work, or evidence position is live, cite the pattern that defines or constrains that position instead of restating its ontology in `E.8`. If the phrase hides several kinds, split them or assign the decision to that exact pattern or `DRR`; do not flatten them into one cleaner-looking word.

Authoring repairs also have an MG-DA cold-reader closure. A phrase is not mature merely because it avoids a trigger word or uses an FPF-looking abstraction. A reader who has not read the `DRR`, campaign notes, or author memory must still be able to recover the object being named, its FPF kind or ordinary status, the relation or claim kind, the admissible use, and what any cited pattern contributes to the claim. Identify an exact claim-bearing episteme or `ClaimGraph` only when its identity changes interpretation, migration, conflict, publication, or reuse. If authoring uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or another broad head, name the specific object and position or keep the phrase ordinary. If authoring uses `specialization`, state what object is specialized, what relation makes it a specialization, what inherited or changed slots or uses matter, and which pattern defines or constrains it; require an exact `ClaimGraph` only when the receiving use depends on that exact claim-bearing content. Otherwise the edit is bureaucratic abstraction, not an improvement.

For boilerplate overwrap, use `F.19`. After removing or moving the apparatus, repair any remaining word, head, name, relation, or use with `E.10`, `E.10.ARCH`, `F.18`, or the specific pattern that defines, constrains, or tests the claim. Keep the intended user's action and boundary. Do not expand ordinary `use this pattern` or `apply this pattern` wording into `U.MethodDescription`, `U.Method`, performer System, assignment, `U.Work`, `U.Transformation`, or `ClaimGraph` language unless the current claim or a named later use depends on those identities. If dated `U.Work` is asserted, however, A.15.1 and F.6 require its actual performer System, enacted Method, time, containing System, a covering assignment that has that performer as holder and spans the Work, and the Work-to-assignment attribution. Only how many already established identifiers the prose exposes is proportional. Process, architecture, review, quality, projection, and release evidence stay in their own carriers unless rewritten as that user-facing action.

When an action-adjacent pattern classifies wording, a name, a publication face, an explanation class, a comparison unit, or another semio-facing object, that classification is only useful if it connects back to action guidance. The pattern must say what use or action is admissible now, what related use or action is not admissible under the current pattern, and which FPF pattern defines or constrains the case when the claim is a work, evidence, gate, decision, assurance, engineering-justification, release, or reliance claim.

`Semio-Echoing` is admissible only as a trigger-controlled auxiliary placement. Use it when `E.10`, `C.2.P`, or `E.10.ARCH` has exposed a wording-use overread whose EntityOfConcern, episteme/publication stack, alignment basis, and remaining admissible reader use are recoverable by value. Do not add it as a generic warning block. In non-semio patterns the primary content remains the pattern's own `EntityOfConcern` and admissible use; semio material stays as a thin cue, related-pattern relation named by value, local recovery line, or named description and publication-use boundary section unless it changes that use or blocks a documented overread. If the material mainly says that a description, view, publication, record, card, diagram, source, or file is not a permission, promise, prescription, evidence item, assurance verdict, decision, gate passage, release, work occurrence, or authority source, keep it out of the subject Solution and put it in that boundary section or in the exact description-publication pattern.

