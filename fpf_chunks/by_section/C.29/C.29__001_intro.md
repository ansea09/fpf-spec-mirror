---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__001_intro.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:intro — Intro"
line_start: 49984
line_end: 49997
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
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
  - "C.28"
  - "C.29"
  - "C.31.ASAP"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
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

**Primary EntityOfConcern.** C.29 concerns a declared mathematical-lens use for a stated phenomenon, EntityOfConcern, relation, claim, or structure-bearing situation. The use names the mathematical object, formalism, learned representation, simulation substrate, or mathematical family; the mapping mode; the preserved structure; the lost structure; the visible payoff or obstruction; the admissible use; the non-admissible use; and the stop condition. FPF-governed wording, pattern examples, method notes, review records, `PublicationUnit`s, decision-facing text, comparison-facing text, bridge-facing text, and assurance-input text can contain or cite that use, but they are not the primary EntityOfConcern of C.29.

**Output boundary.** C.29 outputs are lens-use notes, one-line entries, mini-cards, full cards, and neighboring-locus notes. They are not actors, approvals, gates, work records, evidence records, assurance results, decisions, or release records. They state which declared mathematical-lens use is admissible, what remains blocked, and which neighboring FPF locus carries any live non-lens claim.

**No new `U.*` from C.29 local lens-use outputs.** `MathLensUse.OneLine`, `MathLensUse.MiniCard`, `MathLensUse.FullCard`, `MathLensUse.Card@Context`, `MathLensUseOutputRef`, and `CC-C29-*` are C.29-local instruments. They do not mint `U.MathLens`, `U.MathLensUseRecord`, `LensKind`, `MathLensUseCompliance`, or a durable record family. Durable names, kinds, or records require explicit FPF admission through `F.18`, `C.3`, `F.8`, and `E.9`.

