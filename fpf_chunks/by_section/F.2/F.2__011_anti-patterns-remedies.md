---
chunk_kind: "child"
pattern_id: "F.2"
pattern_title: "Term Harvesting & Normalisation"
section_id: "F.2:10"
section_title: "Anti-patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.2/F.2__011_anti-patterns-remedies.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "F.2 — Term Harvesting & Normalisation"
  - "F.2:10 — Anti-patterns & remedies"
line_start: 93557
line_end: 93575
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.3"
  - "F.4"
  - "F.9"
keywords:
  - "LNF"
  - "LocalExpression"
  - "LocalSenseClaim"
  - "effective ReferenceScheme"
  - "exact source and edition"
  - "optional SchemeSenseCell"
---

### F.2:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | Global normal form | One canonical label is reused across sources. | It erases source-local meaning. | Keep an LNF per recovered source use; relate meanings only in F.9. |
| **A2** | String = meaning | Identical spelling is treated as one concept. | Homonyms such as *role* and *process* collapse. | State source, scheme, and LocalSenseClaim before comparison. |
| **A3** | Over-normalisation | Case, hyphens, or modifiers are removed for consistency. | Source cues and citations become unreliable. | Make only minimal edits. |
| **A4** | Headless multiword | *Service-level objective* becomes *objective*. | Scope disappears. | Preserve the meaningful compound. |
| **A5** | Premature structure | A gloss contains equations, duties, or kind axioms. | A lexical note is asked to establish a substantive fact about another value. | Route the substantive claim to its direct pattern. |
| **A6** | Cross-source folding | “BPMN process ≈ PROV activity” appears in F.2. | A relation and its losses are hidden. | Leave the comparison to F.9. |
| **A7** | Edition blur | A source name has no edition although usage changed. | The claim cannot be replayed. | Name the exact edition and recover the changed meaning afresh. |
| **A8** | Dialect elevation | A tool keyword list is treated as the whole domain. | One source use displaces other evidence. | Keep it as one exact source basis. |
| **A9** | Tail chasing | Hundreds of unused terms are harvested. | Signal and working memory are diluted. | Keep terms that change the receiving answer. |
| **A10** | Fake Plain label | Tech and Plain repeat the same jargon. | The cold reader gains nothing. | Explain the use without widening it. |
| **A11** | Design-time and run-time blur | A design expression is glossed as an occurrence, or conversely. | MethodDescription and Work collapse. | State the actual source-local claim and route the distinction through F.11, A.3, and A.15. |
| **A12** | Cross-language collapse | Bilingual expressions are merged because a dictionary aligns them. | Normative and idiomatic differences vanish. | Recover each source use; assert a relation only when one obtains. |
| **A13** | Alias inflation | A new technical term is invented “for clarity”. | It competes with the source and hides provenance. | Keep inventions, if needed, only as bounded Plain labels. |
| **A14** | Role–status conflation | RBAC *role* is glossed as an acting system role. | Permission and agency claims mix. | Say **access role (RBAC)** and use E.10.ROLE and F.4 for any system-role claim. |

