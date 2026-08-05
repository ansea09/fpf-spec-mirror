---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:0.3"
section_title: "Pattern Kind In Plain Terms"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__005_pattern-kind-in-plain-terms.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:0.3 — Pattern Kind In Plain Terms"
line_start: 71988
line_end: 72011
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

An FPF pattern supplies action- or judgement-guiding content for a recurring working situation. “Use this pattern” and “apply this pattern” are valid shorthand for a person or another capable system using that content to choose an action or judgement. The pattern episteme itself does not act, decide, perform `U.Work`, or cause a `U.Transformation`. State that its content is a `U.MethodDescription` only when the A.3.2 membership conditions are established and that membership matters to the current claim; then name the admitted `U.Method`, capable system, role assignment, dated `U.Work`, result, or `U.Transformation` only when those further identities or relations also change the claim.

When a method-bearing `Solution` prescribes actual work or world-side change, it must also distinguish the intended reader from the admitted `U.System` that can perform that work and from the current role assignment under which that system performs the work, and distinguish the method episteme, dated `U.Work`, and problem-facing result. The intended reader and performer may coincide in one person-system, but the positions remain different. A pattern episteme, checklist, reader role, plan, or prose cannot perform the prescribed work. Do not invent a fictive performer or work occurrence when the pattern only guides a judgment or another episteme-side use.

`Pattern application` is metonymic shorthand for this user-side use: the user or another capable system recognizes the working situation and uses the pattern content and its `Solution` to shape the next admissible action or judgement. If that claim depends on method-bearing content, establish `U.MethodDescription` membership under A.3.2 and identify the admitted `U.Method`; when actual work is claimed, name the acting system, admitted Method, role assignment, dated `U.Work`, problem-facing result, and independent `U.Transformation` when one obtains. `Problem frame`, `Problem`, `Forces`, `Solution`, `Consequences`, worked slices, and anti-patterns provide the description-side guidance. A `Conformance Checklist` checks the authored description and the separately evidenced use; it must not replace the `Solution`, manufacture Work, or turn the pattern into a control form.

The primary content-bearing job is constructive action or judgement guidance: the pattern description must say what the user should do or decide so the recurring error does not arise. Error prevention, auditability, and conformance checks are evidence that the guidance is usable; they are not the pattern's center. The first substantive content in the opening `Problem frame` and `Solution` must be positive subject and action guidance: the primary `EntityOfConcern` kind, the first admissible action-guiding move, the practical delta, and the few boundaries needed for that first move. The text must not replace subject content with repeated guards, distinctions, related-pattern mappings, references, mini-rules, definitions, caveats, architecture rationale, or quality or projection evidence unless the repetition adds a new local action, case, evidence value for the user, or first-reading recognition need. Copying distinctions from another pattern's defining or constraining content into this pattern as repeated "do not confuse our EoC with their EoC" prose is the same repetition problem. Boundary doctrine is pattern content like any other doctrine: if an exact distinction, non-use condition, ToC navigation cue, or cited pattern already states it, do not repeat it locally. Cite the short pattern id; identify an exact claim-bearing episteme or `ClaimGraph` only when that identity matters to the receiving use. Add local boundary prose only when it states a documented local confusion and exact stop condition that the existing content does not already state. The repair is to say clearly what this pattern's own `EntityOfConcern` is, not to enumerate the unbounded set of other things it is not.

The same rule blocks pattern-use drift for any FPF object. Name the object by its FPF kind when the kind is known, and do not let “acts”, “routes”, “receives”, “decides”, or an ownership word hide a different relation. For an ordinary neighboring-pattern reference, state what the cited content contributes here—for example, defines a kind, constrains a relation, supplies a test or method, or provides a locator—and cite the pattern id. Identify an exact claim-bearing episteme, `ClaimGraph`, edition, or relation assertion only when that identity changes interpretation, migration, conflict, publication, or reuse. A genuine stop needs no receiver; a reconsideration states its condition and the candidate guidance to consult. Relations are positive claims, not catalogs of absent relations. Detailed discoverability belongs in README, ToC query cues, `E.11`, `I.2`, or retrieval or projection carriers; compact related-pattern statements belong late in `Relations` after the positive subject and action guidance. Ordinary references use ordinary reference forms: a pattern id in prose, a citation, `Builds on`, `Coordinates with`, `Relations`, ToC, README, `E.11`, `I.2`, or a retrieval or projection carrier. Do not repeat them as many conditional sentences or small variants when one compact definition, boundary, table, `Relations`, ToC, README, `E.11`, `I.2`, or retrieval or projection locus already carries the same content family.

Treat precision-restoration problems in pattern prose as one profile with five layers: word, head, and use precision; phrase apparatus; repetition and distribution; role and carrier separation; and pattern application. Do not add a local row for each new symptom. `E.8` requires the author to keep positive subject and action guidance first; `F.19` repairs phrase-level apparatus; `E.10`, `E.10.ARCH`, `F.18`, or the pattern that defines or constrains the relevant kind, relation, or use repairs remaining word, head, and use precision; `E.21` measures the collapsed effect on pattern quality.

A wording cleanup is kind-preserving by default. Before an author accepts a changed FPF-governed phrase as a repair, the pre-repair and post-repair `EntityOfConcern`, kind, relation or claim kind, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope must be recoverable when those items are live. This is a bounded complete preservation check, not an order to formalize ordinary prose or unchanged text and not permission to choose "no edit" as the easy minimum. Leaving text unchanged closes only when the phrase is `not triggered`, ordinary prose, or already satisfied by value with loci; otherwise the finding remains open. Removing a trigger word or replacing a generic head is not a repair when it changes the ontology: for example, a graph-shaped method cue must not be narrowed into a work sequence unless an accepted decision explicitly changes the kind and consequences. If a relation, signature, mathematical-lens, role, method, work, or evidence position is live, cite the pattern that defines or constrains that position instead of restating its ontology in `E.8`. If the phrase hides several kinds, split them or assign the decision to that exact pattern or `DRR`; do not flatten them into one cleaner-looking word.

Authoring repairs also have an MG-DA cold-reader closure. A phrase is not mature merely because it avoids a trigger word or uses an FPF-looking abstraction. A reader who has not read the `DRR`, campaign notes, or author memory must still be able to recover the object being named, its FPF kind or ordinary status, the relation or claim kind, the admissible use, and what any cited pattern contributes to the claim. Identify an exact claim-bearing episteme or `ClaimGraph` only when its identity changes interpretation, migration, conflict, publication, or reuse. If authoring uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or another broad head, name the specific object and position or keep the phrase ordinary. If authoring uses `specialization`, state what object is specialized, what relation makes it a specialization, what inherited or changed slots or uses matter, and which pattern defines or constrains it; require an exact `ClaimGraph` only when the receiving use depends on that exact claim-bearing content. Otherwise the edit is bureaucratic abstraction, not an improvement.

For boilerplate overwrap, use the Method described at `F.19`. `E.8` adds only the pattern-authoring placement rule: after boilerplate is removed or moved and remaining content is precision-restored using the Methods described at `E.10`, `E.10.ARCH`, `F.18`, or the relevant pattern that defines or constrains the kind, relation, or use, pattern prose keeps only the intended user's admissible move and boundary. Process, architecture, review, quality, projection, and release evidence stay in their own carriers unless they are rewritten as that user-facing move.

When an action-adjacent pattern classifies wording, a name, a publication face, an explanation class, a comparison unit, or another semio-facing object, that classification is only useful if it connects back to action guidance. The pattern must say what use or action is admissible now, what related use or action is not admissible under the current pattern, and which FPF pattern defines or constrains the case when the claim is a work, evidence, gate, decision, assurance, engineering-justification, release, or reliance claim.

`Semio-Echoing` is admissible only as a trigger-controlled auxiliary placement. Use it when `E.10`, `C.2.P`, or `E.10.ARCH` has exposed a wording-use overread whose EntityOfConcern, episteme/publication stack, alignment basis, and remaining admissible reader use are recoverable by value. Do not add it as a generic warning block. In non-semio patterns the primary content remains the pattern's own `EntityOfConcern` and admissible use; semio material stays as a thin cue, related-pattern relation named by value, local recovery line, or named description and publication-use boundary section unless it changes that use or blocks a documented overread. If the material mainly says that a description, view, publication, record, card, diagram, source, or file is not a permission, promise, prescription, evidence item, assurance verdict, decision, gate passage, release, work occurrence, or authority source, keep it out of the subject Solution and put it in that boundary section or in the exact description-publication pattern.

