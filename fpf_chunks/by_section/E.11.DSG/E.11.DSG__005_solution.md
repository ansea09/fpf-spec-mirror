---
chunk_kind: "child"
pattern_id: "E.11.DSG"
pattern_title: "Architectural Reference"
section_id: "E.11.DSG:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.DSG/E.11.DSG__005_solution.md"
commit_sha: "b40c9df9e856c1c8c6a12f93ed8b310265007f68"
heading_path:
  - "E.11.DSG — Architectural Reference"
  - "E.11.DSG:4 — Solution"
line_start: 102775
line_end: 102888
dependencies:
  - "C.2.1"
  - "C.2.P"
  - "C.20"
  - "E.11"
  - "E.11.PFP"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.4"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
---

### E.11.DSG:4 - Solution

Develop the account of the named whole under section 4.1, preserving the explanations needed to understand and adapt it. For a problem-led entry, write the practical answer first. State the recognizable situation and question, then say what each returned item actually is and what it contributes: an available result of its own kind and supplying product, a MethodDescription used to select or perform its Method, direct-source evidence for a named claim or decision, or a named unavailable result with its blocker and retry. State maintenance only when it changes the answer. End the entry with the ordinary stop or return. Add identity, relation, evidence, warning, or reliance detail only when it changes the answer's truth, the reader's choice, or a named later use.

When an account cites a basis or directs readers to another contribution, use E.8:4.2.2.2 to make the purpose clear in ordinary prose. Preserve the difference among an explanation already given, an available result, material to apply, and a contribution still unavailable. This distinction does not make every relation between frameworks an application instruction or require a label beside every address.

#### E.11.DSG:4.1 - Identify the explained whole and the account's boundary

Start from the language assembly selected under E.4 and E.4.PFAD. Identify what the whole enables and which constituents and connections it contains. For a Suite, recover its composite discipline under C.20, constituent DPFs, whole-forming connections and outside suppliers. For FPF Library, recover the relations among Core, Suites and standalone frameworks without inferring disciplinary parthood from their use or co-publication. A useful outside contribution remains outside unless its separate part relation is established.

Identify the architectural-reference episteme under C.2.1 by its claims, subject and effective ReferenceScheme. Its claims include the whole's purpose and architecture, intended readers and questions, answers and gaps, and sources and conditions needed to use them. Its scheme resolves the named whole, constituent and external frameworks, Methods, results and relation words. A title or a folder supplies a locator, not those distinctions.

Keep the architectural reference as a support unit of the explained whole when their readers, content change and publication boundary agree. Give it a separate product boundary only when readers need to use, cite or revise the account independently. If continuity across independently managed editions matters, E.4:4.2.5 supplies the product-series distinction. This publishing choice does not make the account a subdiscipline or a constituent DPF.

Establish publication, availability, currentness and maintenance only to the extent claimed. An author, locator or recent date does not establish a maintaining System or a commitment to future updates. A stale Reference can cease to supply a reliable route while the Suite and its constituent Methods remain directly usable.

##### E.11.DSG:4.1.1 - Explain the architecture and its reasons at this level

Explain the working problems served by the whole, the contributions of its constituents and the connections that make their use coherent. State the shared assumptions, combination conditions and limitations that are not recoverable from one constituent alone. Include the alternatives and tradeoffs that help a reader choose or adapt the arrangement, the source synthesis and SoTA grounds behind it, and representative cases in which a whole condition changes the next action. Use the substantive questions in E.11.PFP:4.7 for a framework account; at another assembly level retain the questions that its promised use actually needs. A short entry and exact constituent returns can spare a familiar reader repetition, but a locator does not supply an unwritten shared explanation.

Choose the receiver from the named whole the account explains, then choose its carrier. In a one-file framework, embed that framework's architectural reference as a named unit. In a multi-file language, provide the account at that language's assembly level and make the constituent accounts reachable. For example, an Engineering Suite Architectural Reference explains the Suite's composition; the FPF Library Architectural Reference explains its relations to other Suites and standalone DPFs. Neither source-file boundaries nor generated website pages create additional explained wholes. Use the full qualified title at the unit's entrance and an unambiguous shorter mention within it; a generic heading `Reference` alone does not identify the subject.

Keep the account's **referential index** recoverable: who speaks, to whom, about which language, and for which reader action. In an Architectural Reference, its author explains the named language to its users. They need to understand how the arrangement works, what it enables, how to use its contributions and why it was chosen. Resolve wording such as 'we', 'you', 'here' and 'this framework' from that position. Identify the reading purpose, not a person's profession: a framework developer selecting a Method is a user in that passage; when the explained framework itself teaches framework development, its developers are its practitioner users.

Distinguish that explanation from instructions for constructing or revising a pattern language. This pattern and the applicable E.9, architecture and authoring patterns address that development work. A Reference can explain a constraint on valid use of its language; state whom it constrains, under which conditions and from which governing pattern it follows. A sentence about what the authors selected does not by itself impose an obligation on users or future authors.

Publish the architectural decisions realized by this language and the reasons needed to understand and use them. The architectural reference can be their public statement, not merely a summary of a private record. Keep chronology, superseded decisions, review correspondence and release logs in the corresponding project's documentation. E.9 develops and records a substantive decision; a decision record is not historical by its kind. The public account retains the operative choice and its useful grounds. An explanation of an already described Method can remain in its pattern or the architectural reference of the whole it explains. A separate course or Guide serves a learning purpose; it is not a substitute for the language's own explanation.

##### E.11.DSG:4.1.2 - Make current decisions understandable and revisable

Organize the account around the architectural questions that matter to users of this language. A reader may need to understand a boundary before choosing a Method. The same explanation can let that reader challenge the boundary and propose a change; it need not teach the work of developing the next framework edition. Give such a decision a recognizable title and section address. Connect related decisions: a choice of field boundary can determine which Methods are constituents, which are suppliers and what a whole-level Method still has to obtain. A list of isolated decisions cannot replace the account of that whole.

For a decision needed to understand, combine or revise the language, make these answers recoverable:

1. **Question and conditions.** What difficulty or requirement does the choice address, and which competing forces shape it?
2. **Selected arrangement.** What is constituted or separated, which relations hold, and where are they realized in the language? Distinguish the selected architecture from a proposed alternative or an illustrative case.
3. **Grounds and alternatives.** Why is this arrangement useful under those conditions? Compare the serious alternatives that could change the choice, with their sources and limits. An unexplained preference or reference to an inaccessible DRR supplies no rationale.
4. **Consequences and revision.** What can readers obtain with this arrangement, what does it cost or leave unresolved, and which Methods or connections depend on it? Explain what changed condition would justify reconsideration and what related claims would then need examination.

These are substantive questions, not four mandatory subheadings or a demand for one ADR file per decision. Use connected prose, a comparison table, a diagram or a developed case as the question requires. Section titles should name the architectural issue or choice; E.11.PFP:4.7 supplies the framework-wide content functions, and section 4.2.1 supplies the addresses. Keep a shared premise once and return to it from the decisions that use it. The reader should not have to assemble the whole from repeated miniature forms.

A decision can define the architecture of this published language without imposing a universal rule on all disciplines or frameworks. State any normative requirement with its actual scope and return to its governing pattern. Conversely, an explanatory form does not make the language's declared composition an optional opinion. Claims about the discipline still need their C.20 grounds; publishing a decision does not create those subject-side relations.

Architectural patterns can contribute to this account or organize its explanation when they belong to the explained language and supply a result its users need. Develop a missing reusable construction as a complete E.8 pattern in Core, the relevant DPF or the Suite according to its subject. An architectural-reference publication may carry that pattern if its full body, identity, reader use, entry and authoritative source remain explicit under E.11.PFP. Otherwise return to its existing full body. Distinguish a domain architectural Method used by the language's practitioners from a Method for developing the language itself. Reusability alone does not place the latter in a user-facing account. Sharing a carrier does not turn ordinary explanatory sections into normative authoring Methods. A record explaining why this language selects one architecture is not automatically a new pattern; E.9 and the applicable architecture and authoring patterns supply the development Methods.

First test the account for its user's work. From the account and its reachable suppliers, can the reader recognize when the language is useful, select and connect its contributions, and explain why a relevant architectural condition changes that use? If the reader can only repeat the arrangement or guess why it was chosen, develop the missing explanation.

An informed change proposal supplies an additional test of that understanding. A user who questions the arrangement should be able to identify the decision, the challenged premise, a meaningful alternative, its expected gain and the connections it could affect. This requires neither private authoring history nor a mandatory issue form. It does not replace the account's user-facing purpose with a Method for changing the framework.

#### E.11.DSG:4.2 - Make the public minimum immediately useful

Make these facts recoverable before the reader chooses an entry. An embedded architectural reference can use the containing publication's edition, date, status and ToC wherever they already identify this unit and its content; do not repeat that front matter or constitute a separate edition solely for the account. A separately carried unit exposes the necessary facts at its own entrance:

- the qualified architectural-reference title and exact edition locator;
- fixed edition date, intended readers, and practical use;
- actionable status or an honest non-current, superseded, or retired warning, together with its as-of basis;
- a direct entry to the account of the explained whole, with constituent and external contributions distinguished; and
- a table of contents that locates the architectural account, useful question-led entries and their supplying explanations without implying a mandatory order.

The edition date says when this edition was constituted. It is not a changing currentness claim or the date of every publication occurrence. Show the author when attribution, trust, contact, reliance, or source return changes what the reader should do. A byline does not identify the Reference maintainer, suite maintainer, publisher, or authority.

Every problem-led entry keeps this small visible core:

```text
recognizable situation and practical question
first useful answer or honest blocker
available result, MethodDescription, direct-source evidence, or named unavailable result needed now, and what each contributes
ordinary stop or return
```

Add a DPF product series' or edition's state, field promise, detailed locator, applicability, evidence, availability, dependency, compatibility, warning, author, or claim-local reopen condition only when it changes the choice, truth, stop, return, or named reliance. Put a genuinely shared boundary once at Reference or section level. Do not repeat empty fields or turn ordinary architectural decisions into pattern-index entries. Use section addresses for the account. If the publication also carries declared E.8 patterns, retain their distinct entries and full bodies under E.11.PFP.

Frame each entry around a real working question and the decision or action the reader needs next. Let the answer branch, overlap, or offer several honest stops when the situation does; do not force a false linear procedure. Keep the action-changing answer in the entry and return to detailed sources and explanations already provided in the account or its constituents instead of repeating them. At Reference level, state whose information need is served, how the publication is presented and made available, how readers return to its sources, and where later review or retirement is decided. Future revision or continued availability requires a separate commitment.

##### E.11.DSG:4.2.1 - Give each answer a stable address and a recoverable extent

Use the architectural-reference unit's declared key and give each substantive heading a stable section address, for example `Engineering.Reference:2` and `Engineering.Reference:2.1`. These are `SectionRef` values for the unit, not PatternIDs or a framework identity. Keep one qualified unit title, a contents entry for every substantive heading, and a final `<ReferenceKey>:End` boundary. In an embedded account, use the containing publication's ToC rather than add another one. A structural Contents heading needs no section address. Use nested contents entries to make the answer hierarchy visible and every substantive heading reachable.

Make the heading levels express the actual containment of the answers. In a Markdown carrier, a complete addressed section includes its own text and child sections up to the next heading of the same or a higher level, or the document's end boundary. The numbers and heading hierarchy must agree; a number alone does not change the returned extent. Place examples and variations under the explanation whose answer they develop. An independently retrieved example returns to any parent or related explanation needed to interpret it.

Keep an established SectionRef when only the heading title changes. When moving a section beneath another parent requires a different hierarchical path, assign its current SectionRef and record the correspondence in the publication or access maintenance material. Update maintained links to the current section. Preserve former returns in each access route that claims that continuity; do not reuse a former address for another answer or place a migration history in practitioner prose. A new answer receives an unused address. Preserve returns to saved heading fragments using facilities permitted by the selected publication form. For Markdown, follow E.8:4.1.1 and update maintained links to the corresponding native heading. Resolution of a carrier fragment does not establish that another access route can resolve the former SectionRef. If a route cannot preserve a return, identify the replacement and the affected reliance before claiming continuity. Check the full contents and complete returned sections, including their children, in each selected presentation or access route. Successful title search establishes findability for that query; stable identity and complete extraction need their own evidence.

#### E.11.DSG:4.3 - Keep lookup Work and the answer separate

A person, team, or assisting System may use one Reference edition while doing lookup Work. Ordinary use alone does not establish a Method, assignment, operation application, evidence, or authority. Identify those objects only when the current claim actually needs their direct rules.

An ordinary answer may remain readable conversation. Persist one only when review, reuse, publication, or later reliance needs an addressable result. First identify the exact practical-question episteme `Q`. Then identify the answer episteme `A` under `C.2.1` as `<claim content = J_a, EntityOfConcern = Q, effective ReferenceScheme = R_a>`. `J_a` states the answer, exact Reference edition used, every returned resource or blocker, and what each does in this answer. `R_a` resolves those values and the use-specific relation words. This is an ordinary episteme, not a new lookup-result kind.

Say directly what each returned item does. For an available result, name the result's actual kind, supplying product and edition or current state, receiving use, and any currentness or availability condition that can change that use. State maintenance only when it changes the answer. For a MethodDescription, name the described Method and how the reader uses the description; do not present its expected result as already obtained. For direct-source evidence, name the supported claim or decision and the source limits. For an unavailable result, name the blocker and retry condition. Recommendation, alternative, dependency, compatibility, and co-listing remain separate claims and create none of these stronger relations.

#### E.11.DSG:4.4 - Test sufficiency and each item's necessity

Call an answer a **sufficient combination with every returned item necessary** only when the Reference entry gives a recoverable candidate boundary, required result, and sufficiency rule, the combination satisfies that rule, and removing any returned item makes the result insufficient. The boundary is the resources actually inspected through the entry and its direct source returns, not every publication that might exist. This item-necessity test does not establish the smallest combination. A “smallest” claim also needs a declared size criterion and a comparison or argument showing that no smaller in-scope combination is sufficient.

When that test cannot be completed, return a bounded plausible combination and name the uncertainty or missing item. Do not disguise a convenient shortlist as a `JointUseSet`. Use `G.5` only when every named returned resource is required for one named use and the current inclusion basis supports that all-items-needed claim.

#### E.11.DSG:4.5 - Return to the full Methods and refresh the affected answers

The architectural reference supplies the current account of the explained whole, with exact returns to inherited explanations. For a Suite it distinguishes constituent DPFs from the external frameworks that a question happens to use. It also identifies the supplying edition, Method or result whenever that difference can change the answer. A reproducible comparison may pin an assembly and constituent-edition selection; ordinary current use needs a reliable current return, not a history of editorial decisions.

When a supplying DPF changes, compare the contribution consumed by the answer. Refresh the answer if the Method, conditions, result, evidence, applicability or availability changed materially. A new layout need not change the answer; a stable URL does not prove stable content. Use E.4.PFIP for preservation across reconstructed publications and E.4.PFR for a genuine edition dependency or compatibility claim.

When a DPF moves or a former pattern is divided, return to the full current Methods that supply the required results. Preserve a distinct result only where its explanation still exists. A list of successor titles, an empty redirect pattern or an old locator cannot stand in for lost content. Update maintained links and test their destinations and complete returned sections in the selected publication form.

If the field boundary or constituent relation changes, return that architecture question to E.4:4.2 and E.4.PFAD. Do not keep a false membership statement because an older Reference printed it. A Reference can show the newly supported arrangement without claiming that a publication edit itself transformed the discipline.

When an answer loses a required contribution, name the missing result and its consequence. Offer a direct known DPF route when sufficient, a bounded qualified alternative when supported, or an honest stop. An unavailable Reference does not prohibit direct DPF use. An unavailable constituent publication does limit the Suite's claimed usable coverage; neither fact erases the discipline.

#### E.11.DSG:4.6 - Distinguish expression, derivative, edition, and product

Another layout, carrier, rendering, or faithful expression of the same exact claims under the same scheme presents the same Reference episteme. A translation or other derivative that changes claims or effective scheme is a distinct episteme with an exact source-to-use path under `C.2.P`; when meanings cross schemes, test the `F.9` Bridge and bounded use separately. Title or provenance alone establishes no `EpistemeEditionRelation`.

A language-specific derivative stays within the same Reference product only while it uses the same intended readers and use, access rule, warning rule, later-review rule, and retirement rule. A separately established maintenance relation changes product identity only when the identity rule says so. If a language community needs a different current state or any of those rules, select another Reference product. A comparison across Suites can belong to the FPF Library Architectural Reference. Give it an independent product identity only when its use and change boundary justify that choice under E.4:4.1.

