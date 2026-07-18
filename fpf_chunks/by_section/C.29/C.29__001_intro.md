---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__001_intro.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:intro — Intro"
line_start: 54661
line_end: 54684
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18.1"
  - "C.19.1"
  - "C.2.P"
  - "C.26"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.31.ASAP"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
  - "LensUseAdmissibilityValue"
  - "coarse-graining"
  - "invariants"
  - "learned lens"
  - "lens mapping mode"
  - "lost structure"
  - "mathematical lens"
  - "ontology smuggling"
  - "preserved structure"
  - "rival lens"
  - "scale window"
  - "stop condition"
  - "structure-preserving representation"
  - "validation boundary"
---

## C.29 - Mathematical Lens Use

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Mathematical lens use.

**Primary EntityOfConcern.** C.29 concerns a declared mathematical-lens use for a stated phenomenon, EntityOfConcern, relation, claim, or structure-bearing situation. The use names the mathematical object, formalism, learned representation, simulation object, local formal role, or mathematical family; the mapping mode; the preserved structure; the lost structure; the visible payoff or obstruction; the declared lens use; the blocked overread; and the stop condition. FPF-governed wording, pattern examples, method notes, review records, `PublicationUnit`s, decision-facing text, comparison-facing text, bridge-facing text, and assurance-input text can contain or cite that use, but they are not the primary EntityOfConcern of C.29.

**Slot discipline.** C.29 uses `CandidateMathObject` for the mathematical object, formalism, learned representation, simulation object, local formal role, or family in a declared mathematical-lens-use relation. `U.Signature(profile=FormalSubstrate)` in `A.6.0` is a different relation position: it declares vocabulary, laws, imports, and applicability for a formal-deductive profile. `A.6.1` governs mechanism import or realization when that `U.Signature(profile=FormalSubstrate)` declaration is used in a mechanism; `E.18.1` governs P2W carry-through when accepted problem-side material needs that formal declaration for later work. The same mathematical object may appear in several of these positions, but the governing pattern is selected by relation position and claim being made, not by a source-local head word.

**Output boundary.** C.29 outputs are lens-use notes, one-line entries, mini-cards, full cards, and neighboring-pattern notes. They state which declared mathematical-lens use is bounded as usable, what remains blocked, and which neighboring FPF pattern governs any non-lens claim being made. Project approval, work, evidence, assurance, decision, or release use must be recorded through the governing pattern for that use.

**Use this when.** Use this pattern when a mathematical object, formalism, simulation object, learned representation, or mathematical family is being used to make a project claim more inspectable, or when the lack of such a lens hides preserved structure, lost structure, invariants, obstruction, approximation, or stop condition.

**What goes wrong if missed.** Mathematical prestige starts acting as evidence, mechanism, architecture, causal proof, assurance, benchmark result, or release confidence; or a useful lens is avoided because no one states what it preserves and what it loses.

**What this buys.** The practitioner can use mathematics as a bounded lens: name the object, mapping, preserved structure, lost structure, visible payoff, blocked overread, and neighboring governing pattern before relying on the result.

**Not this pattern when.** If the current claim is evidence, assurance, causal use, measurement construction, architecture adequacy, work, gate passage, decision, formal signature, mechanism import, or publication use, use the direct governing pattern and keep C.29 only to the mathematical-lens use portion.

**No new `U.*` from C.29 local lens-use outputs.** `MathLensUse.OneLine`, `MathLensUse.MiniCard`, `MathLensUse.FullCard`, `MathLensUse.Card@Context`, `MathLensUseOutputRef`, and `CC-C29-*` are C.29-local instruments. They do not mint `U.MathLens`, `U.MathLensUseRecord`, `LensKind`, `MathLensUseCompliance`, or a durable record family. Durable names, kinds, or records require an accepted FPF naming and kind decision through `F.18`, `C.3`, `F.8`, and `E.9`.

