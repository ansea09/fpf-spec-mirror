---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:11"
section_title: "SoTA-Echoing (normative; typed comparison to contemporary best-known practice)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__016_sota-echoing-normative-typed-comparison-to-contemporary-best-known-practice.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:11 — SoTA-Echoing (normative; typed comparison to contemporary best-known practice)"
line_start: 73767
line_end: 73807
dependencies:
  - "E.10"
  - "E.10.MOVE"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
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

### E.8:11 - SoTA-Echoing *(normative; typed comparison to contemporary best-known practice)*

**Canonical definition and contract.** This is the FPF definition of `SoTA`: the best-known currently defensible answer to one named practice question. `F.1` may prepare the question-relative source cut and `E.21` may evaluate the resulting pattern, but neither redefines SoTA. A `SoTA-Echoing` section earns its place by changing the pattern's Solution, boundary, case, check, relation, evidence requirement, stop, or reopen condition. It is not a bibliography, source-currentness register, or lineage shelf.

**Source roles in plain wording.** Classify each retained source by what it can do for the question:

- a **best-known-line candidate** supplies or critically synthesizes the strongest current answer being considered;
- a **serious current rival** supplies another answer that could change the selection;
- **failure or counterexample evidence** shows where an answer breaks or does not transfer;
- an **official or popular comparator** exposes a default worth comparing but gains no rank from authority or adoption;
- **lineage only** explains history without supporting the current selection; and
- **identity/currentness only** identifies a source, edition, date, or maintenance state without supporting its truth, adequacy, or rank.

Only the best-known line, serious rivals, failure evidence, and a necessary explicit comparator belong in `SoTA-Echoing`. These are comparison roles, not publisher or institution classes. An official standard, widely used practice, or university-endorsed line can be the best-known-line candidate when its substantive answer wins the comparison, but authority, freshness, prevalence, or praise contributes nothing to that win. Lineage-only and identity/currentness-only material stays in source records, notes, or evidence carriers outside the pattern body. An official or popular default stays as comparator only when its precise defect is needed to explain the selected answer and changes a governed pattern locus.

**Positive comparison contract.** Every positive SoTA use states, in readable prose or one compact table:

1. `practiceQuestion` — the exact working question;
2. `bestKnownLine` — the selected answer, not merely its newest source;
3. `seriousAlternativeOrDefault` — the rival or default that could have changed the answer;
4. `defectOvercome` — the action-changing defect, limit, or trade-off that selection repairs;
5. `patternMutation` — the exact Solution, boundary, case, check, relation, evidence, stop, or reopen locus changed;
6. `sourceRolesAndLimits` — the exact source edition or stable locator, why it has this comparison role, and what it does not establish; source identity supports replay, not rank; and
7. `reopenCondition` — the smallest new evidence, rival, failure, or use change that would require comparison again.

Mark material moves `adopt`, `adapt`, or `reject`. Explain which defect of the incumbent, popular, or official answer is repaired and why the selected line is no worse at comparable application effort on the values that matter and better on at least one, or state the trade-off deliberately accepted. More sources, a later date, a wider deployment, institutional praise, or a longer review cannot replace that comparison.

**Honest gap and lightest sufficient evidence.** If an adequate best-known comparison cannot be established, say which rival, counterexample, or source role is missing and return that source gap. Do not fill the section with a current standard or recent paper. Use `F.1` for the smallest question-relative cut and its SoTA-specific role branch. Use `F.0.2` only when the conclusion actually needs cross-source synthesis. Use a broader `G.2` pack only when repeated refresh or a wider claim justifies that cost.

**Evidence and relation discipline.** Reuse an existing `G.2` pack's exact ClaimSheet, corpus-ledger, Bridge rows, and source roles instead of forking a second narrative. Inherit non-conflicting comparison content from an accepted `DRR` and its source materials while keeping the `DRR` as the decision and placement record. For an obtaining semantic Bridge, identify the two exact `F.17` local senses, the `F.9` relation, and a separate bounded-use claim; otherwise leave that relation unasserted. Keep numeric comparison under its applicable ComparatorSet or CG-Spec without hidden scalarization.

**Writing guidance.** Lead each row with the practice question and practical choice. Name the selected line and serious alternative, state the defect and pattern change, then give source roles, limits, and reopen condition. Complete sentences are preferred to tag lists. External terminology or tooling stays out unless the comparison itself needs it.

#### E.8:11.1 - SoTA alignment for this pattern (E.8 self-echo)

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a pattern text remain teachable while retaining a stable reusable shape? | Iba's practitioner pattern-writing line is the best-known candidate here: start from a recurring problem, forces, a usable solution, illustration, and consequences, then make the sequence readable as a whole. | A form-only template that rewards headings and compressed bullets is the serious default. | The default can be structurally complete yet unusable. **Adapt:** `E.8:4.1`, Archetypal Grounding, recognition text, and `CC-SG.2/13/17` require a first action, worked material, and readable continuity rather than heading presence alone. | Takashi Iba, *How to Write Patterns: A Practical Guide for Creating a Pattern Language on Human Actions* (PLoP 2021), supplies practitioner writing guidance, not FPF ontology or evidence that one skeleton fits every pattern. E.8's extra checks and typed boundaries are FPF-local adaptations. | Reopen if a stronger current pattern-writing comparison shows a lower-effort form that preserves the same recognition, action, grounding, and consequence value. |
| What evidence should distinguish pattern validation from a favorable review or folklore count? | Riehle, Harutyunyan, and Barcomb's 2025 handbook method is the best-known candidate for the bounded pattern-discovery and validation question because it makes claims, research methods, cases, and evidence limits explicit. | Ad hoc expert approval and the rule of three are the serious defaults. | The defaults hide what was tested and overstate a small positive history. **Adapt:** E.8 separates a canonical seed from maturity, requires worked grounding and explicit evidence use, and routes quality claims to independent `E.21` results; **reject** a universal research programme for every small pattern. | Riehle, Harutyunyan, and Barcomb, [*Pattern Discovery and Validation Using Scientific Research Methods*](https://doi.org/10.1007/978-3-662-70810-1_6) (2025), supplies a rigorous validation branch but does not validate E.8. It is neither an admission decision nor a universal minimum case count. | Reopen if stronger current validation practice changes the evidence needed for a maturity claim or demonstrates a cheaper method with equivalent limits and replayability. |
| When does a narrower or domain-specific contribution deserve a separate pattern or framework boundary? | The best-known line for this decision combines action-changing pattern evidence with the 2022 systematic comparison of product-line scoping approaches: compare same-situation use, reusable contribution, family promise, organizational conditions, evidence, and maintenance rather than relying on a label. | Label-only specificity and a full software-product-line process are the serious alternatives. | A label can mint empty specialization, while the full process adds software-specific machinery before value is known. **Adapt:** `E.8:4.1.3` tests the same situation at comparable effort and routes a material family change to `E.4.DPF.DA`; **reject** feature ontology and action change as sufficient proof of worth. | Marchezan de Paula et al., [*Software product line scoping: A systematic literature review*](https://doi.org/10.1016/j.jss.2021.111189) (2022), is the scoping synthesis; Riehle et al. (2025) supplies actual-use pressure; Chuprina et al., [*Towards an Approach to Pattern-based Domain-Specific Requirements Engineering*](https://arxiv.org/abs/2404.17338) (2024), is bounded proof-of-concept evidence, not a universal grammar. | Reopen if current scoping or pattern-validation evidence changes the action test, the family-boundary variables, or the evidence needed for warranted retention. |

