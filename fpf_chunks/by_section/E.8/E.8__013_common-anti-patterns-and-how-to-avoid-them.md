---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 73698
line_end: 73722
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

### E.8:8 - Common Anti-Patterns and How to Avoid Them

These failure modes recur in drafts and in downstream application. They are predictable ways the Forces in this pattern get violated.

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
|-------------|---------|------------------------------|-----------------------|
| **Template cargo-culting** | Headings exist, but the section is fragments, decorative bullets, or a table with no governing claim. | Satisfies Uniformity but loses Readability and Didactic Primacy. | State the governing claim and its practical consequence in ordinary prose; introduce a list or table only when that structure improves the reader's work, and apply `F.19` to its contribution and load. |
| **Un-grounded abstractions** | Problem/Solution stay abstract; no concrete System/Episteme Tell-Show-Show. | Breaks teachability and makes misuse likely. | Fill Archetypal Grounding first; then back-propagate concrete nouns into Problem/Forces/Solution. |
| **SoTA name-dropping** | SoTA-Echoing lists sources or adopt/adapt/reject labels but never names the practice question, serious alternative, defect overcome, or changed pattern locus. | The reader cannot recover why the selected line is best for this question or what changed in practice. | Supply the complete compact comparison from CC-SG.7, or state an honest source gap. |
| **Currentness laundering** | An official registry entry, publication date, maintained status, latest release, citation count, or widespread default is verified and then reported as evidence that the source is SoTA. | The check establishes source identity, availability, or currentness, not the best-known answer or its advantage over a serious alternative. | Classify the source as official/popular comparator or identity/currentness only. It contributes to SoTA only through an explicit comparison whose defect and pattern mutation are independently shown. |
| **Tool-bound normativity** | A vendor tool, file format, or schema is described as required to apply the pattern. Data governance implied. | Violates Guard-Rails (lexical firewall; notation independence, data governance absence); reduces portability and conceptual clarity. | Keep normative content conceptual; move tooling and data governance into subject-specific project profiles. |
| **Hidden trade-offs** | A material cost or limitation is omitted from Consequences. | Hides information needed to judge adoption or applicability. | State the decision-relevant cost or limitation and a mitigation when available. Consequences may state only gains when no such cost or limitation is known. |
| **Skeleton-only pattern** | The template is present, but the pattern gives only one compressed definition block and scenario labels. | Passes form while failing didactic sufficiency. | Add didactic content: local decomposition, concrete slices, reviewer cues, and neighboring-pattern or project-side FPF kind and reference named by value guidance. |
| **PatternID read as definition or order** | A numeric or mnemonic segment is treated as the pattern's meaning, title, current position, dependency, Method relation, or semantic parent. | The address becomes a hidden claim and ordinary reordering threatens reference continuity. | Use the PatternID only as an address together with surrounding text that identifies the framework. Show title and current position separately, state relations directly, and use the applicable product-authoring rule to decide continuity across editions. |
| **Project-context leakage** | A reader needs architecture memos or planning notes to understand the pattern. | The monolith stops being self-sufficient. | Move the essential problem framing, worked slices, and rationale into the pattern itself; keep project reviews informative only. |
| **Repeated content, reference, and architecture boilerplate leakage** | The body repeats a guard, definition, reference, or placement rationale without adding a local action, case, evidence value, or recognition need. | Repetition hides the positive `Solution` and turns the pattern into an architecture note. | Cite the existing source or use the proper discovery or architecture carrier; keep one local boundary only when it changes use. |
| **Quality-carrier leakage** | The pattern body reports development, review, projection, assembly, or landing evidence as if it were practitioner guidance. | The reader sees why the text was processed rather than what to do. | Keep the evidence in its own carrier and retain only the user action or boundary that it supports. |
| **Apparatus overwrap** | Process, status, role, carrier, or quality language displaces the pattern's object and move, or a polished caveat introduces an unsupported relation. | The prose can be true and still force the reader to solve the wrong problem. | Apply the connected `F.19` reading, return the positive practitioner path, and route only a genuinely unresolved FPF value to its exact pattern. |
| **Unresolved wording kept as local style doctrine** | `E.8` locally restates generic-head, qualifier, comparison, or implicit-relation rules instead of resolving the actual sentence. | The authoring pattern grows a rival precision-restoration algorithm and encourages checklist prose. | Apply the connected `F.19` reading; use `E.10` only as a cue or route, and take an unresolved FPF kind, relation, comparison, or admissible-use question to its exact governing pattern. |
| **Package-form and neighboring-relation drift** | Package-form words are varied for style or used without their declared relation. | The reader cannot recover membership, projection, navigation, or another actual relation. | Use the matching term from `E.8:4.2.2`, state the relation, and name any cited content's concrete contribution. |
| **Intended-reader leakage** | Pattern sections narrate the current draft's promotion, freeze, review, or safest landing form. | The reader must reconstruct development history to find the Method and its reasons. | Keep that history in companion records; explain the user's Methods, costs, alternatives, boundaries, and use-changing architectural reasons in the public account. |
| **Editorial/development self-instruction leak** | The pattern starts saying things like `this draft should ...`, `later authoring will ...`, or `that is the opening this draft must hold`. | The text stops addressing the working reader and starts narrating the current editorial or drafting process. | Move the sentence to the authored-slice carrier or handoff, or rewrite it as one user-facing claim about the primary `EntityOfConcern`, boundary, or practical consequence. |
| **Intended-reader-clean but pragmatically foggy** | The pattern addresses the right reader, but the first reading still hides the working situation, payoff, governed object, or first move. | Correct audience alone does not make the guidance usable. | Put the recognition cue and one minimal worked case earlier, gloss necessary technical terms, and tie explanatory `SoTA-Echoing` back to the case it changes. |
| **Hybrid audience blob** | One main narrative tries to serve engineers, managers, auditors, architects, and researchers at once with no primary working reader or concern. | The text becomes globally polite but locally blurry; no reader knows which concern governs the first passage. | Make the primary working reader, concern, and viewpoint explicit and assign other audiences to secondary companion uses, other faces, or an explicit out-of-scope note. |

