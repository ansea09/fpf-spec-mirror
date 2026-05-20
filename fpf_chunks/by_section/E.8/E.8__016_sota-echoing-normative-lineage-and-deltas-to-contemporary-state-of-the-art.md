---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:11"
section_title: "SoTA-Echoing  (normative; lineage and deltas to contemporary State-of-the-Art)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__016_sota-echoing-normative-lineage-and-deltas-to-contemporary-state-of-the-art.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:11 — SoTA-Echoing  (normative; lineage and deltas to contemporary State-of-the-Art)"
line_start: 50066
line_end: 50097
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

### E.8:11 - SoTA-Echoing  *(normative; lineage and deltas to contemporary State-of-the-Art)*

**Purpose.** Make each pattern's relationship to contemporary best-known practice explicit and comparable without importing tooling or data governance. This section is prose-first and notation-independent. It does not mint an independent second rule source, but it is a load-bearing alignment section: the Solution, Conformance Checklist, Relations, worked cases, and other load-bearing sections must reflect the stance stated here or explicitly justify divergence.

**Action-guidance test.** A SoTA row is accepted only when it changes what the pattern lets a working user do, what the pattern forbids them to over-read, which neighboring FPF pattern must apply, which evidence or validation obligation remains live, or how the Solution is written. A citation that only decorates the pattern or proves that the author has read a tradition does not carry E.8.

**Minimum contents (obligations).**
1) **Evidence binding (no duplicate SoTA).** If a **SoTA Synthesis Pack** exists (G.2), this section **SHALL cite** its **ClaimSheet IDs, CorpusLedger entries, and BridgeMatrix rows** as the governing evidence source for claims and report `adopt`, `adapt`, or `reject` **consistent with those IDs**. Avoid forking an untracked SoTA narrative.
1a) **Accepted basis set, not DRR-only narrowing.** When a pattern is drafted under an accepted `DRR` and other accepted basis materials also exist by value, the `DRR` remains the decision and placement anchor, but `SoTA-Echoing`, neighboring-pattern relations, and any minimal modeling or mathematical lens **MAY** and **SHOULD** inherit non-conflicting material from that accepted basis set.
2) **Sources (post-2015, or current-practice anchor).** For **Architectural patterns**, cite at least 3 primary SoTA sources such as standards, papers, or books, with at least **two independent Traditions**. For **Definitional patterns**, cite at least 1 current source or practice anchor for the reduced issue being governed: terminology work, ambiguity or sense recovery, separation between constraint and ontology, controlled-vocabulary caution, or a comparable definitional problem. If the best source is older but still current, mark it as current practice rather than treating SoTA as not applicable.
3) **Best-known, not merely popular.** Authors **SHALL** distinguish best-known currently defensible practice from merely widespread or fashionable defaults. If the pattern adopts, adapts, or rejects a popular but less defensible practice, that divergence **MUST** be stated explicitly.
3a) **Currentness and lineage status.** Older standards, early papers, and historically important examples may be cited as lineage only when later practice has materially changed the answer. They may carry a live SoTA row only when the pattern states why the anchor is still current for the governed problem or pairs it with a current source that supplies the live practice.
3b) **Problem-domain and practice answerability.** The selected SoTA source family **MUST** answer the governed working problem and the relevant domain or practice tradition. It **MUST NOT** be selected only because it makes package placement, naming neatness, or pattern clustering easier to justify.
4) **Practice alignment.** For each cited item, state **what is adopted, adapted, or rejected** and **why** in 2 to 4 sentences.
5) **Scale admissibility.** If numeric operations are implied, bind to ComparatorSet or CG-Spec and declare partial-order stance with no hidden scalarization.
6) **Cross-Context reuse.** Any reuse across `U.BoundedContext` must expose Bridge id plus CL and, if planes differ, Phi policy ids; penalties affect only `R_eff`.
7) **Lexical hygiene.** Avoid “mapping” unless you mean an explicit Bridge, translation relation, or other named relation with loss notes.

**Writing guidance (readability).**
*Write short paragraphs, not tag lists.* For each Tradition, provide one sentence naming the practice, one sentence comparing it to the pattern's Solution, and one sentence giving adoption status with reason. Where helpful, add one **System** and one **Episteme** micro-example (Tell-Show-Show).

**Format: human-first.** A small table is allowed, but each row **MUST** be accompanied by 1 to 2 sentences as above. Vendor tokens, tool tokens, file formats, or data schemas are out of scope unless the governed problem itself makes them load-bearing.

#### E.8:11.1 - SoTA alignment for this pattern (E.8 self-echo)

| Claim (E.8 need) | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with E.8 | Adoption status |
|---|---|---|---|---|
| Pattern texts must be teachable, not just correct. | Use a stable skeleton with context, problem, forces, solution, actions, and consequences, plus illustration and checks, to keep patterns readable and actionable. | Iba (2021), “How to Write Patterns …” (PLoP 2021 PLoPourri). | Canonical Template mirrors the skeleton and adds Archetypal Grounding plus Conformance Checklist as first-class sections. | **Adopt and adapt.** Adopt the skeleton; adapt by making bias and conformance explicit sections. |
| Pattern quality needs explicit validation beyond folklore. | Critique of ad hoc validation, including the rule of three, and push toward more rigorous discovery and validation methods. | Riehle et al. (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | E.8 encodes validation as Conformance Checklist plus SoTA-Echoing with adoption status and evidence binding. | **Adopt.** Adopt auditability goals; keep the mechanism lightweight through checks and evidence binding. |
| Governance should constrain structure, not mandate tools. | Specify conformance and structure; do not prescribe processes, notations, tools, or recording media. | Joint ISO, IEC, and IEEE 42010:2022 on architecture description. | E.8 is template-centric and conformance-centric, with guardrails against tool and notation lock-in in core narrative. | **Adopt.** Direct alignment. |
| Pattern languages are networks; visuals often mislead. | Systematic surveys report low consensus on what to visualise and ambiguous or inexpressive visuals; relations need clear definition in text. | Quirino, Barcellos, Falbo (2018), survey of visual notations for software pattern languages. | E.8 requires a Relations section and keeps diagrams optional, placing primacy on textual structure and explicit links. | **Adapt.** Use the finding as rationale for text-first, relation-explicit authoring. |

