---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Adequacy (MLA)"
section_id: "C.29:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__001_intro.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "C.29 — Mathematical Lens Adequacy (MLA)"
  - "C.29:intro — Intro"
line_start: 48016
line_end: 48030
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
  - "C.18.1"
  - "C.19.1"
  - "C.26"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
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
  - "LensSupportPosture"
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
  - "validation posture"
---

## C.29 - Mathematical Lens Adequacy (MLA)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Mathematical lens adequacy.

**Governed object.** C.29 governs only mathematical-lens adequacy claims carried by FPF prose, pattern examples, method notes, review records, `PublicationUnit`s, decision-facing text, comparison-facing text, bridge-facing text, or assurance-input text that use a mathematical object, formalism, learned representation, simulation substrate, or mathematical family as a lens for a stated use. It does not govern those objects themselves: `PublicationUnit`s, decision records, comparative review units, bridges, work records, evidence paths, and assurance inputs remain with their own FPF loci; C.29 contributes only the bounded adequacy of the mathematical lens used inside them.

**Output posture.** C.29 outputs are claim-supporting notes, not actors, approvals, gates, work records, or release decisions. They state what the mathematical lens can support for one declared use and which neighboring FPF locus carries any live claim outside lens adequacy.

**No new `U.*` from MLA.** `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, `MLA.Card@Context`, `MLAOutputRef`, and `CC-MLA-*` are C.29-local instruments. They do not mint `U.MathematicalLens`, `U.MLARecord`, `LensKind`, `MLACompliance`, or a durable record family. Durable names, kinds, or records require explicit FPF support through `F.18`, `C.3`, `F.8`, and `E.9`.


