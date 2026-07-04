---
chunk_kind: "child"
pattern_id: "A.6.H"
pattern_title: "Wholeness Language Unpacking — RPR-WHOLE"
section_id: "A.6.H:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.H/A.6.H__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.6.H — Wholeness Language Unpacking — RPR-WHOLE"
  - "A.6.H:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 19337
line_end: 19349
dependencies:
  - "A.14"
  - "A.15"
  - "A.6.5"
  - "A.6.P"
  - "A.7"
  - "B.1.1"
  - "B.1.4"
  - "F.18"
keywords:
  - "boundary"
  - "completeness"
  - "environment"
  - "integrity"
  - "mereology"
  - "order/time"
  - "part-of"
  - "publication-carrier and EntityOfConcern/Description distinction"
  - "role-method-work"
  - "wholeness"
---

### A.6.H:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                 | Symptom                                                                | Why it fails                                        | How to avoid / repair                                                                             |
| ---------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Holistic-as-evasion**      | “We took a holistic view” replaces boundary/scope detail               | Sacrifices auditability for conversational economy                   | State the boundary, environment, and scope (G); use wholeness facets explicitly                   |
| **Universal part-of**        | Everything is “part of” everything                                     | Breaks portability; different readers infer different relations      | Replace with ComponentOf/ConstituentOf/PortionOf/PhaseOf/MemberOf                                 |
| **Structure-as-sequence**    | Step order encoded as containment                                      | Collapses procedure into structure; causes Γ errors                  | Use SerialStepOf/ParallelFactorOf + Γ_ctx/Γ_method                                                |
| **History-as-structure**     | Versions modeled as parts                                              | Erases temporal coverage and identity discipline                     | Use PhaseOf + Γ_time; if identity changed, model the new holon, episteme, or publication according to the live identity criterion                                   |
| **Collection-as-assembly**   | A team “consists of” people encoded as ComponentOf                     | Confuses membership with assembly                                    | Use MemberOf and, if the group acts, model it as a bounded system with its own work               |
| **Completeness-by-rhetoric** | “Method is complete” without stating what it covers                    | Confuses structural wholeness with capability/spec/evidence coverage | Rewrite using A.15: MethodDescription vs Method vs Work, plus explicit coverage                   |
| **Module vs component blur** | “Module” used sometimes as physical part, sometimes as deployment unit | Breaks cross-team comparability                                      | Use a mini-definition on first mention and route: component, constituent, or deployment unit; if a document or screen is live, name that publication separately |
| **Description-publication and referent drift**   | “The whole X” alternates between a system, its description episteme, and a spec/model/document publication   | Breaks auditability; smuggles relations across A.15 levels            | State the reference level explicitly; use ConstituentOf for publication-unit parts; keep model-of separate |

