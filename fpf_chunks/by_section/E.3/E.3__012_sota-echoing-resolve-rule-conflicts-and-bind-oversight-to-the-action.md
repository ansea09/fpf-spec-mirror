---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
section_id: "E.3:11"
section_title: "SoTA-Echoing — resolve rule conflicts and bind oversight to the action"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__012_sota-echoing-resolve-rule-conflicts-and-bind-oversight-to-the-action.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.3 — Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
  - "E.3:11 — SoTA-Echoing — resolve rule conflicts and bind oversight to the action"
line_start: 79112
line_end: 79128
dependencies:
  - "E.1"
  - "E.2"
keywords:
  - "ABL"
  - "Arch"
  - "BLP waiver"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "autonomy budget"
  - "conflict resolution"
  - "oversight"
  - "precedence"
  - "principle taxonomy"
  - "profile change"
---

### E.3:11 - SoTA-Echoing — resolve rule conflicts and bind oversight to the action

**Practice question and choice.** How can an agentic action use applicable governance rules and a budget profile without acquiring an undeclared priority or extra authority? The selected answer combines §4.2's partial order and unresolved-action hold with §6's editioned profile, concrete ceilings, checks and permission window. The serious simpler default uses one fixed conflict-combining rule and a stable table of profiles. That default is cheaper where every relevant rule fits its declared semantics and the table fully specifies the action; the added governance work is justified when obligations conflict or a profile's actual conditions change.

[Cedar's authorization algorithm](https://docs.cedarpolicy.com/auth/authorization.html) is a substantive comparator: an applicable forbid overrides permits, otherwise an applicable permit allows the request, and the default is denial. **Adopt** explicit request scope and a declared combination rule where that permission policy is intended. **Reject** treating it as a universal ordering of obligations: a requirement to publish and a prohibition of publication can remain normatively inconsistent even when access is denied. Cedar does not claim to repair that inconsistency. Its policy-error handling also does not replace A.21's treatment of required check results. The source defines an authorization language, not FPF rule-change authority.

[NIST AI RMF 1.0 §6, pp.33–34](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) supplies the candidate line for oversight: profiles depend on the particular use, requirements, risk tolerance and resources; they can distinguish current and target conditions. **Adapt** that contextual treatment to §6's budgets, signers, checks and effective window. The source does not prescribe ABL's L0–L4 labels, numeric defaults or FPF permission semantics. A project's defaults still need a basis appropriate to its use; an ordinal-looking label alone supplies none. This is a comparison with the published 1.0 method, not a claim about an unreleased revision.

At the same action and input scope, the two cases expose the chosen trade-off:

| Case | Simpler default | Selected move and cost |
| --- | --- | --- |
| G1 requires noon publication and G2 forbids it; same source level and class, no priority. | A forbid-overrides permission rule denies publication. It is a complete access decision if that combination is already authorized, but leaves the competing obligation to be resolved. | §4.2 returns the unresolved obligation pair and holds its action. The extra cost is obtaining an authorized priority or scope amendment; the gain is a visible unresolved duty instead of an invented governance winner. |
| A plan keeps the label L2 while its requested ceiling changes from twenty to thirty minutes. | A stable profile table works if it already resolves the correct edition, checks and window. Looking only at an unchanged label cannot decide the new request. | §6 binds the new ceiling and permission before minute twenty-five. Maintaining those conditions costs more than checking a label; an existing table or policy system can carry them without another store. No E.18 or F.9 event is inferred from the budget change. |

The taxonomy groups principles for the declared fallback order; its five classes are not a claim that all governing duties reduce to permission predicates. Use the simpler default when its scope and maintained inputs suffice. Reopen only the affected priority or profile comparison when a new incompatible rule, changed permission condition, or equally adequate cheaper policy changes the action. BLP comparisons remain conditional on an actual scale claim or declared generality policy.

