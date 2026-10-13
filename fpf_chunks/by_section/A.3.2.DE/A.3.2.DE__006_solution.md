---
chunk_kind: "child"
pattern_id: "A.3.2.DE"
pattern_title: "Describe a Method for Its Intended Use"
section_id: "A.3.2.DE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.2.DE/A.3.2.DE__006_solution.md"
commit_sha: "7d0a78002c04f2337283b97d707991c888013a73"
heading_path:
  - "A.3.2.DE — Describe a Method for Its Intended Use"
  - "A.3.2.DE:4 — Solution"
line_start: 11639
line_end: 11670
dependencies:
  - "A.3.2"
  - "C.37"
  - "C.39"
  - "E.8"
keywords:
---

### A.3.2.DE:4 - Solution

A.3.2 distinguishes description membership from adequacy for use. C.39:4.3–4.5 supplies construction of a missing action or join. Here the author develops the explanation for the declared reader: recover the actual operations, reasons, conditions and changed case that the reader must be able to follow, retaining an unresolved candidate as such.

Author claims for named uses while preserving the described Method's identity or the account's candidate status. Return gaps instead of filling them with neighboring objects.

#### A.3.2.DE:4.1 - Pattern-Use Unfolding

1. **Name the receiving use.** State the reader or consuming system, the action or decision, the situation and qualification window, and the stop. Replace “complete documentation” with the smallest question that changes work.
2. **Establish the subject branch.** Name the admitted `U.Method` and effective `U.ReferenceScheme`. If admission is absent, keep the subject as a candidate account and author only improved candidate content.
3. **Select the needed Method claims.** For the named use, consider the transformation or enactment concern, generic participant meanings, applicability, preconditions, intended effects or preserved conditions, bounds, parameters, variation, internal composition, evaluation conditions, and stops. Include only positions that change the use. For enactment or learning, recover the operations the performer must carry out and where their inputs come from.
4. **Separate neighboring claims.** Keep planned assignments and dates in a `U.WorkPlan`; actual performers, temporal extent, participation, and results with dated `U.Work`; operation declarations with `A.6.1`; evidence reliance with `A.10`; capability with `A.2.2`; approval, permission, and authority with the patterns that define those claims. Cite them when the use depends on them without absorbing them into Method semantics.
5. **Write the explanation or instruction.** For enactment or learning, connect each needed action to its inputs, the operation performed, the result and the condition for continuing or stopping. Explain why a connection or ordering matters when the reader needs that reason to apply or adapt it. For a Method that depends on professional judgment, explain which observations bear on the decision, how they change the proposed action, and which unresolved conflict needs another contribution or a stop. Naming a mindset without showing that effect leaves the explanation incomplete. Unfold a constituent operation until the intended performer can carry it out, or identify the missing know-how or contribution; do not invent an operation to fill a heading. Retain alternatives and genuine dependencies without imposing one order on independent actions. In the admitted-Method branch, identify the episteme by its claim content, Method as `EntityOfConcern`, and effective scheme. In the candidate branch, retain the account's proposed content and unresolved Method-identification conditions. State which claims were added, retained, narrowed, or removed when another edition is being revised.
6. **Record use coverage and omissions.** For each named use, list the claims exposed, claims deliberately omitted, unresolved claims, and the return condition. An omission is acceptable when the receiver does not rely on it; otherwise it is a gap.
7. **Choose expression and publication separately.** Select text, code, diagrams, a mathematical lens, publication form, and carrier only after the claims are stable enough for the use. When different named Method-related actions require complementary governed representations of the current MethodDescription or candidate account, C.37.MP returns a complete Method representation profile: one complete C.37 claim group per action, together with cross-use correspondences, conflicting omissions, edition relations, decisions to keep representations separate, and conditions that require reconsidering several selections. Use the FPF pattern governing any other represented entity.
8. **Try the receiving use from the description.** Recover the claims, conditions and omissions needed by the receiving use. For enactment or learning, work through a small case: recover the first action and its inputs, follow its result to the next needed action or stop, and expose any instruction supplied only from the author's memory. Return a description or candidate-account correction, or identify the missing input, know-how or other result needed by the use. This checks the description at that use; it does not establish the Method's effectiveness or a learner's acquired capability.

#### A.3.2.DE:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| subject | Admitted Method and identity basis, or candidate account and unresolved admission condition. |
| named use | Receiver, action or decision, situation, qualification window, and stop. |
| claim set | Method-side claims included in this edition and their effective scheme; the connected operations, inputs, results and conditions when the use requires an actionable instruction. |
| use coverage | Needed claims, exposed claims, deliberate omissions, gaps, and return condition for each use. |
| neighboring objects | Any WorkPlan, Work, representation, operation declaration, evidence path, capability, permission, authority, publication, or carrier relied on, each kept under its own kind. |
| edition disposition | MethodDescription edition, improved candidate-account content, or lower stop with the decisive missing condition. |

#### A.3.2.DE:4.3 - What Changes in Practice

Authors stop treating “the method document” as one undifferentiated object. They can issue a small edition for one use, explain why it is enough, and name the exact gap when it is not. Readers can distinguish a claim about a reusable way of doing from a plan, an observed occurrence, a tool presentation, or an approval fact.

