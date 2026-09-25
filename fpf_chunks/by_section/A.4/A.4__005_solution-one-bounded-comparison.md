---
chunk_kind: "child"
pattern_id: "A.4"
pattern_title: "Compare a System's Intended Design with Its Operating Conditions"
section_id: "A.4:4"
section_title: "Solution - One Bounded Comparison"
source_path: "FPF-Spec.md"
output_path: "by_section/A.4/A.4__005_solution-one-bounded-comparison.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.4 — Compare a System's Intended Design with Its Operating Conditions"
  - "A.4:4 — Solution - One Bounded Comparison"
line_start: 10965
line_end: 10987
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.3.4"
  - "B.4"
  - "C.2.1"
  - "C.27"
keywords:
  - "comparison criterion"
  - "conformance"
  - "design account"
  - "discrepancy"
  - "missing basis"
  - "operating facts"
---

### A.4:4 - Solution - One Bounded Comparison

1. **Select the subject, account and use.** Identify the System, the design account edition and the decision this comparison must inform. Keep the System's identity under its own rule and the account's identity under C.2.1. Choose the relevant account claim rather than treating the entire design as one test.
2. **Recover the operative criterion.** State the target or expected behavior, relevant conditions, units and tolerances, and the rule for comparing them with actual facts. Identify what force the account claim has:

   | Account claim | What the comparison can establish |
   |---|---|
   | Normative target, such as a required minimum flow | Whether the actual operation meets that target under the rule. A miss does not by itself make the target inapplicable. |
   | Descriptive prediction | Agreement or discrepancy between predicted and actual behavior under the prediction's conditions. Model revision remains a separate decision. |
   | Applicability condition | Whether the named condition is met. Use A.1.1 when the question is the model's applicability to this subject/use; do not substitute target conformance for that judgment. |

3. **Obtain or reuse comparable facts.** Recover the actual operating conditions and results required by the criterion. Check their temporal reference, units, tolerance, relevant configuration and measurement uncertainty when it affects the selected decision rule. If the design and observation concern different conditions, use an already justified translation only within its limits. Otherwise name the missing basis. Use C.27 when temporal adequacy is itself unresolved.
4. **Perform the comparison and return its boundary.** State what meets the criterion, the discrepancy, or the precise missing or incomparable premise. Qualify the result to the named System, account claim, conditions and use. When a rule withholds acceptance because the evidence is too uncertain, distinguish that outcome from an established physical failure. A partial comparison can leave other requirements unexamined.
5. **Separate any response decision.** Keeping the present use, qualifying reliance, changing the System and revising the account are different possible next decisions. Use their own authority and subject methods when needed; B.4 coordinates repeated adaptation. Do not replace the selected target with an easier one and report that as improved conformance. Stop at the comparison when it answers the working question.

No additional record is required when the subject, criterion, actual facts and bounded answer are already recoverable in the working account. Describing this method does not assert that an observation or Work occurrence happened.

#### A.4:4.1 - Observation, change and continuity

An observation may involve dated measurement Work. Recover that Work under A.13 and A.15.1 only when the receiving claim needs the occurrence; identify the result and its relied-on evidence under their own patterns. A new record does not establish a target change. A.3.4 governs any actual before/during/after change claim, and A.12 distinguishes actual acting and changed participants when internal action is asserted.

Changed account claim content identifies a different C.2.1 episteme. An obtaining edition relation is a further claim with its own conditions, including any actual branching. Neither an account edit nor overlapping operation and design work decides the System's continuity. Particular practices may define design and operating regimes where useful; these regimes do not partition every holon's existence.

