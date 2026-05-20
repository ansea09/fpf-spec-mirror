---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 50022
line_end: 50044
dependencies:
  - "E.10"
  - "E.19"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.9"
  - "F.18"
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

| Anti-pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
|-------------|---------|------------------------------|-----------------------|
| **Template cargo-culting** | Headings exist, but each section is a thin bullet list with no narrative. | Satisfies Uniformity but loses Readability and Didactic Primacy. | Use S-0 narrative flow per section; write 2-4 sentence micro-paragraphs before any list/table. |
| **Un-grounded abstractions** | Problem/Solution stay abstract; no concrete System/Episteme Tell-Show-Show. | Breaks teachability and makes misuse likely. | Fill Archetypal Grounding first; then back-propagate concrete nouns into Problem/Forces/Solution. |
| **SoTA name-dropping** | SoTA-Echoing is a list of nouns/buzzwords with no adopt/adapt/reject rationale. | Violates CC-SG.7 and CC-SG.10; readers cannot audit alignment. | For each source, state what is adopted/adapted/rejected and why (complete clauses, 2-4 sentences). |
| **Tool-bound normativity** | A vendor tool, file format, or schema is described as required to apply the pattern. Data governance implied. | Violates Guard-Rails (lexical firewall; notation independence, data governance absence); reduces portability and conceptual clarity. | Keep normative content conceptual; move tooling and data governance into Context-local Profiles. |
| **Hidden trade-offs** | Solution sounds universally good; Consequences lists only benefits. | Removes decision-support value; applicability cannot be judged. | In Consequences, include at least one trade-off and a mitigation; if none exists, explain why. |
| **Skeleton-only pattern** | The template is present, but the pattern gives only one compressed definition block and scenario labels. | Passes form while failing didactic sufficiency. | Add supporting content: local decomposition, concrete slices, reviewer cues, and neighboring-pattern or exact project-side FPF kind and reference guidance. |
| **Project-context leakage** | A reader needs architecture memos or planning notes to understand the pattern. | The monolith stops being self-sufficient. | Move the essential problem framing, worked slices, and rationale into the pattern itself; keep project reviews informative only. |
| **Generic-head underspecification** | A load-bearing phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the text never restores what kind of thing that phrase names. | The reader cannot tell what ontology the sentence is actually governing. | Restore the head kind first in pattern-local or project-local terms before any broader claim or effect or comparison is made. |
| **Qualifier-smuggled load** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the text leaves its load implicit. | The sentence sounds precise without actually stating its comparison basis, relation load, or downstream claim or effect boundary. | Unpack the qualifier into explicit load, criteria, named neighboring FPF pattern, or project-side FPF kind and reference rather than relying on the modifier alone. |
| **Mixed comparison basis** | One sentence compares or ranks publication-form, carrier, process, authority-reference, or project-record values on one basis. | The sentence becomes ontologically incoherent even if each local noun sounds plausible. | First restore head kind, then qualifier load, then rewrite the comparison through a homogeneous load, threshold, or named receiving-pattern/source-relation basis. |
| **Implicit relation shorthand** | Words like “species”, “branch”, or process metaphors do the semantic work without naming the actual governing-pattern relation. | Readers infer the wrong ontology or workflow. | State the governing-pattern relation explicitly and remove shorthand that only makes sense inside project discussions. |
| **Package-form and governing-pattern relation drift** | Words like `bundle`, `cluster`, `profile`, `overlay`, `family`, `suite`, or `kit` are swapped as if they were stylistic variants. | Readers cannot tell whether the text is naming an `authoritySourceRef` target, a navigation grouping, a review role, or a packaged set of defaults. | Pick one role word by ontology, keep the governing-pattern relation explicit, and do not vary the noun unless the ontology really changes. |
| **Reader-role leakage** | Live sections start telling the reader why the pattern was isolated, what landing form is safest, or why freeze/merge is premature. | The pattern stops teaching the user and starts narrating FPF-development decisions. | Move package-development reasoning to companion notes; keep live sections about admissible use, costs, boundaries, and exact neighboring FPF patterns or project-side FPF kinds and references for the intended user. |
| **Editorial/process-plane self-instruction leak** | The live pattern starts saying things like `this draft should ...`, `later authoring will ...`, or `that is the opening this draft must hold`. | The text stops addressing the working reader and starts narrating the current editorial or drafting process. | Move the sentence to the authored-slice carrier or handoff, or rewrite it as one user-facing claim about the governed object, boundary, or practical consequence. |
| **Role-clean but pragmatically foggy** | The pattern addresses the right reader in principle, but a cold practitioner still cannot recognise the working situation, practical payoff, governed object, first useful move, or project-level implication of the `SoTA-Echoing` early enough. | The text passes role hygiene but still fails `E.12`/`E.13`/`E.14` as working guidance. | Bring a manager-first or practitioner-first recognition cue higher, add one minimally viable worked case, state what changes in practice, expose the governed object and any minimal modeling lens in plain user-facing prose, add plain glosses for early load-bearing terms, and keep `SoTA-Echoing` tied to visible practitioner or manager implications plus nearby case linkage rather than lineage alone. |
| **Hybrid audience blob** | One main narrative tries to serve engineers, managers, auditors, architects, and researchers at once with no primary working reader or concern role. | The text becomes globally polite but locally blurry; no reader knows which concern governs the first role. | Make the primary working reader, concern, and viewpoint explicit and assign other audiences to secondary support roles, other faces, or an explicit out-of-scope note. |

