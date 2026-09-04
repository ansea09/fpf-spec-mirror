---
chunk_kind: "child"
pattern_id: "E.18.1"
pattern_title: "P2W Problem-to-Work Carry-Through"
section_id: "E.18.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.1/E.18.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.18.1 — P2W Problem-to-Work Carry-Through"
  - "E.18.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 86623
line_end: 86638
dependencies:
  - "A.15"
  - "A.15.PROD"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22.2"
  - "C.29"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.18"
  - "E.18.3"
  - "F.17"
  - "F.18"
  - "F.8"
  - "F.9"
  - "G.11"
  - "G.2"
  - "G.5"
  - "G.9"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Signature"
keywords:
---

### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats neighboring algorithms or builds a second relation-selection catalogue. | Keep `4.6` as the plain one/several/no-claim branch, Relations as the only question-to-pattern map, and include neighboring-pattern details elsewhere only when a local discriminator or worked case changes the reader's action. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a prescribed project sequence. | Treat it as a way to keep one accepted claim visible across separately answered relation questions. `Stop`, `split`, and `return` guide use of E.18.1; they are not P2W relation kinds or a project-work order. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, Work, evidence, or result. | State the carried distinction and next question in conversation; add a compact note only when another person or later action needs replay, then apply the pattern that answers the question. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Apply `C.29` to the preserved structure, lost structure, payoff, declared use, and stop condition. Continue only through the resulting relation; add a P2W note only when another person or later action needs replay. |
| **Generic result token.** The word *result* is treated as one kind, or P2W repeats the whole recovery method. | Ask what can actually be asserted. Apply `A.6.P.WMR`, then carry only the direct subject claim, `A.6.1` application binding, local `A.15.PROD` or `A.6.RCD` claim, or bounded non-assertability result it returns. Keep `factually unsupported`, `missing-information`, and `missing-governor` distinct; only `missing-governor` says that no current predicate definition or occurrence rule can state the claim for the named participants and use. |
| **Choice-as-commitment.** A `C.11` choice result is treated as an individual duty, recommendation-as-duty, prohibition, or obtaining commitment. | Keep the option set, comparison basis, choice rule, and choice result under `C.11`, and apply `A.2.8` separately. A generic prescription remains an episteme without an individual commitment. Carry a `U.Commitment` only when the applicable institution rule and current facts establish its bearer, modality, referents, scope, validity interval, prescription, and instituting basis. Carry the rule's non-obtaining result when the available facts make its test fail. Return `unknown` or the pattern's missing-information result when a required fact is unavailable, and `missing-governor[individual commitment institution]` only when no current rule can state the commitment. |
| **Plan, path, or proximity as actual change.** A desired state, model, method, plan, flow arrow, adjacent work occurrence, or common affected referent is treated as an actual or composite transformation. | Apply `A.3.4` to the change and the direct work-to-change or `A.15.PROD` pattern to its separate claim. Carry only the results or blockers they return; shared timing or proximity opens no composition or production claim. |
| **Intended realization as MethodDescription.** A selected continuation, recommendation, plan seed, imperative sentence or pattern ref is said to describe the Method it may realize. | First identify one C.2.1 episteme and one admitted `U.Method`; apply A.3.2 only when that Method is the episteme's exact EntityOfConcern and the ClaimContent contains a substantive way-of-doing claim. |
| **One giant transformation flow.** Independently selected development, production, use or evaluation flows are flattened because a diagram or common product connects them. | Keep same-TFS valuations and internal `SubflowRef` cases in E.18; select E.18.NET only from independently identified members and exact cross-boundary occurrences. |
| **Displayed mantra as execution.** The five-row display, repeated formula or word *move* is treated as a method, plan or performed step. | Keep the formula as Plain recall wording for one decision, the table as display content, and apply the pattern for each current action or object. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the module-interface, signature-slot, function, architecture, work, evidence, or gate relation before continuing. |

