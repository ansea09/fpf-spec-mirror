---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:4"
section_title: "Solution - Keep meaning portable while choosing a useful expression"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__005_solution-keep-meaning-portable-while-choosing-a-useful-expression.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:4 — Solution - Keep meaning portable while choosing a useful expression"
line_start: 102622
line_end: 102656
dependencies:
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
  - "C.2.8"
  - "C.37"
  - "E.5"
keywords:
---

### E.5.2:4 - Solution - Keep meaning portable while choosing a useful expression

1. **Explain the meaning and operative use.**
   Normative content **SHALL** state the concepts, claims and conditions needed for its use, using prose and mathematics as appropriate. Explain the interpretation of meaning-bearing signs and relations.

   A diagram, calculus or learned vocal-gestural expression may carry a reasoning or construction step. When it does, explain the operation and its prerequisites locally or cite the guidance for that subject. The pattern about that subject or the applicable Method governs the reasoning or construction. The reader obtains the subject result by applying that Method.

   When the intended operation depends on a change of representation language or reasoning medium, use A.6.3.RT to construct and compare the expressions. A faithful translation whose purpose is textual restatement can use A.6.3.CR.

2. **State the semantic mapping.**
   When expressions are compared or one is translated, substituted or relied on as carrying the other's content, their semantic mapping **SHALL** be stated.

   Name the source expression and the expression being compared with it. Name their representation languages when the rules matter to interpretation. State the correspondences for the claims and conditions needed by the intended use. If a relevant distinction is lost, state the loss and limit the equivalence claim accordingly.

   First check that the display, its conventions and the other information available to the recipient fit at least one possible situation. If they conflict, resolve the conflict before relying on the display. For a value or a yes-or-no decision, start with the answer the recipient needs. Could two situations consistent with everything the recipient gets yield the same display and different answers to that question? If so, locate the missing information or limit the use. A display can determine whether a limit was exceeded even when it gives only a range for the value. To rely on it, show that every value still possible gives the same decision. Count any independent information used in that argument among the prerequisites.

   The recipient may instead need any one acceptable choice. A choice that works in every situation still consistent with the display can be made now, even when the complete lists of acceptable choices differ. If every situation has a solution but they share none, another observation may show which one to choose.

   Show how the intended reader obtains the determined answer or makes the supported choice with the preparation and resources available. Use A.6.3.RT.OE when the expression needs to support a calculation, comparison or edit. Use B.5.MR to compare models when the substitution also changes what they say is possible about the same subject.

3. **Reference the conceptual role.**
   If the Core cites a diagram, refer to its conceptual role, such as a boundary schematic, rather than making a file or syntax name part of the concept.

4. **Keep conceptual prefixes neutral.**
   Use E.10.P for the prefix registry and required anchors. A conceptual label's meaning **MUST NOT** depend on its expansion into a serialized name or URI. If a tool supplies such an expansion, describe the relation between the conceptual label and the tool's name or URI in Tooling or Pedagogy, and mark it informative.

5. **Identify what the form governs.**
   A Core card or table can identify what the reader needs to record and how the entries relate. Another expression can carry those same claims. When the work calls for a file, publication or message in a specified form, check the submitted expression against the convention for that form. E.5.1:4 permits the exact syntax needed for this judgement. A correctly formed submission can still contain an incorrect claim. An independently specified tool or delivery procedure has its own conditions. When proposing a new syntax rule, explain what the users of the governed form need it for. A restriction needed solely by one validator belongs in Tooling with that validator. Put the implementation of the automated check there as well.

The first result is an expression whose meaning can be recovered, with an explanation of any reasoning or construction step it supports. Include a semantic mapping when the use compares it with another expression or depends on the content it carries from that expression.

If a claim changes, compare again with the named source expression. Then repair the correspondence or narrow the claimed equivalence and permitted use.

Use A.6.3.RT to compare content carried between expressions and A.6.3.RT.OE to construct an expression with which the intended operation can be performed. If the representation language cannot express a needed distinction, select another language or extend its conventions before claiming that the distinction is preserved.

