---
chunk_kind: "child"
pattern_id: "E.5.2.L"
pattern_title: "Languages, Expressions and Interpretation"
section_id: "E.5.2.L:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2.L/E.5.2.L__005_solution.md"
commit_sha: "169e3e09c04a4174ce4c26682cf181a0d255b6f7"
heading_path:
  - "E.5.2.L — Languages, Expressions and Interpretation"
  - "E.5.2.L:4 — Solution"
line_start: 102233
line_end: 102280
dependencies:
  - "A.6.3.RT"
  - "C.2.1"
  - "E.5.2"
  - "F.18"
keywords:
---

### E.5.2.L:4 - Solution

A **language** (`Language`) is an identifiable repertoire of expressions with conventions that determine which expressions belong and, for composite expressions, which constructions are admissible. A grammar may specify the conventions. They may also be evident in established use. A formal language of strings can be defined by membership alone.

A **representation language** (`RepresentationLanguage`) is a language whose conventions also give its expressions permissible readings under specified conditions. A **language of designations** (`ReferenceLanguage`) is a representation language whose complete entries serve to identify entities under its resolution conventions and any context or bindings they call for. A prefix, separator or other part of an entry can help form a designation without identifying any entity on its own. Each more specific kind classifies the very same language. English contains personal names. An equipment-code language embedded in an English manual can be specified and selected independently.

#### E.5.2.L:4.1 - Recover what the conventions establish

| Question | What establishes an answer |
| --- | --- |
| Can this expression be formed? | Use the identified language, the candidate structure and the applicable formation convention. For a composite, establish that the parts are admissible in the positions they occupy. |
| Which reading does it admit here? | Use the expression or construction, its representation language and the conditions on which interpretation depends. More than one reading can be admissible. A rule restricted to one document belongs with that document's effective interpretation under C.2.1. |
| Which entity does this expression pick out here? | Use the expression with its surrounding words, a gesture or the other available indication. When two entities still fit, keep both candidates open. If the choice affects the work, obtain a further indication or ask the speaker. For an issued code, use the language of designations and the binding that applies to this issuer, domain and interval. |

For a rule about admissibility or interpretation, fix the convention, participants and conditions. When an expression refers to an individual, establish what selects it in this use. A pointing gesture or a previous mention can identify it in ordinary conversation. An issued code requires the applicable assignment. A reader's act of interpretation, the act of issuing a code, and a physical change in the object each have their own evidence. Express the needed rule or fact in a claim. A separate relation occurrence needs its own identity and a practical use that depends on referring to it (A.6.RCD, E.24).

A malformed entry fails the formation test. A complete authoritative register can establish that a valid code had no assignment in a given interval. Several candidate assignments may leave the referent ambiguous. An unavailable or incomplete register can leave the assignment unknown. These conclusions support different actions, from correcting the expression to obtaining the missing register.

#### E.5.2.L:4.2 - Choose what a reference to the language identifies

Identify the conventional system. Specify its community, period or edition where the distinction changes the answer. A specification can document that system, an expression can belong to it, and an expression can refer to something else. Two specifications can define the same language. An edition label or the name of a family alone cannot establish that two editions admit the same expressions and readings.

For languages defined solely as sets of strings over a fixed alphabet, compare membership. For a language with parsing or interpretation conventions, compare those conventions as well. When only selected readings matter, state the construction, inquiry and conditions on which the readings agree. This bounded result can be sufficient for the intended use.

A *sublanguage* has an identifiable repertoire within a language and inherits its formation conventions and any interpretations for the selected constructions. A *profile* selects provisions for a use. If those provisions define such a repertoire and preserve the conventions, the profile also specifies a sublanguage. A *register* concerns customary choices of expression for an audience and activity. A language serves as a *metalanguage* when its expressions specify or examine the expressions or conventions of another.

One language can express a repeatable method, its local adoption and a particular performance. An equipment code can designate a pump while a work instruction says what to do with it. A writer can also change register and retain the same commitment. To claim that a second model refines the first, establish that at least one design, performance or other completion satisfies the second model, and that every such completion satisfies the first under the chosen interpretation. Strict refinement also excludes a formerly admissible answer to the same inquiry. B.5.MR:4.2 gives the test.

Use `representationLanguageRef` when the receiver must identify the language. A notation designer choosing a system in which a reader can build and interpret new expressions and an integration engineer comparing languages of asset designations can reuse these same kind criteria. When a single record already supplies its one relevant interpretation by value, that record needs no separately identified language edition. Name the binding authority or give the necessary rule by value when that is what the receiver needs. C.2.1 determines the effective interpretation of a particular episteme, which may also fix modality, permissible inferences and qualifications. E.8.ML addresses a pattern language that organizes methods and their dependencies. A learned representation with a successful readout supplies evidence for that readout under the tested conditions. A claim about a language in the representation also needs an identifiable repertoire and formation conventions.

#### E.5.2.L:4.3 - Use a language classification in a typed reference

When an interface needs to constrain what a language reference denotes, use the C.3 declarations below. Each row declares one `U.Kind` individual. Its `KindSignature` is a C.2.1 episteme whose EntityOfConcern is that kind; a table carrying the three declarations does not combine their subjects. The member language, its specification and its classification declaration remain independently identifiable.

| Declaration | Candidate domain and membership criterion | Boundary |
| --- | --- | --- |
| `LanguageKindDeclaration` — Language | Independently identified `U.Entity` candidates. The entity has the repertoire and formation conventions defined in §4. For a proposed conventional system, recover its identity through §4.2 before classifying it. | Formal string languages, parsed languages and interpreted systems can qualify, including conventions learned through use. A performance, specification document or expression token does not thereby become the conventional system. A sign list qualifies only when it defines the admitted expression repertoire under the stated interpretation. |
| `RepresentationLanguageKindDeclaration` — RepresentationLanguage | Candidates satisfying Language. Their conventions additionally license readings of expressions under specified conditions, as defined in §4. | Multiple readings and contextual dependence are permitted. Membership in a purely formal string language supplies no interpretation by itself. |
| `ReferenceLanguageKindDeclaration` — ReferenceLanguage | Candidates satisfying RepresentationLanguage. Their complete entries serve as designations under the resolution conventions defined in §4. | A language's inclusion of names does not establish that its complete entries serve as designations. An independently identified equipment-code sublanguage can satisfy this criterion. |

For each declaration, the application slice selects the conventional system under examination, including its community, period or edition when needed. A formal string language also fixes its alphabet. Use the selected conventions rather than an implicit latest edition. The effective interpretation of the declaration combines the criterion in its row with §4.1's formation, reading and reference rules and §4.2's member-identity rule. The declaration's formality is a characteristic of that episteme.

Recover the candidate's identity and conventions from the governing source or established practice. Test admissibility before membership under C.3.2: a known candidate outside the declared domain gives `not-applicable`; insufficient support for a criterion on an admissible candidate leaves membership `unknown`. Unknown does not mean false. Classification establishes neither the truth of an expression nor a successful lookup or performance.

Each kind continues while its candidate domain and operative membership distinction continue under C.3.1. Rewording a declaration or applying it in another discipline creates no new kind. Changing a member language's conventions can identify another edition while leaving the classification criterion unchanged. No `ExtentRule` is needed for the reference uses here; supply one when a later operation consumes an extension.

The added criteria entail the preceding criteria for the same individual: ReferenceLanguage is a subkind of RepresentationLanguage, which is a subkind of Language. A reference to a member is a `U.EntityRef` whose referent satisfies the corresponding criterion. Its binding selects the language; classification does not create or reidentify it. Here C.3's local-kind classification supplies a reusable distinction for the stated uses. It does not restrict a language to a particular enterprise or locality.

