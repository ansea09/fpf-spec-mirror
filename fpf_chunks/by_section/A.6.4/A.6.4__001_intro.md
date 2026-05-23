---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — describedEntity‑retargeting morphism"
section_id: "A.6.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__001_intro.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — describedEntity‑retargeting morphism"
  - "A.6.4:intro — Intro"
line_start: 11487
line_end: 11510
dependencies:
  - "A.1"
  - "A.6.2"
  - "C.2"
  - "C.2.1"
  - "E.18"
  - "E.TGA"
  - "F.9"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
keywords:
  - "KindBridge"
  - "SquareLaw-retargeting"
  - "StructuralReinterpretation"
  - "describedEntity shift"
  - "retargeting"
  - "subject retargeting"
---

## A.6.4 - `U.EpistemicRetargeting` — describedEntity‑retargeting morphism

**One‑line summary.** `U.EpistemicRetargeting` is the **describedEntity-retargeting** species of `U.EffectFreeEpistemicMorphing`: an effect‑free episteme→episteme morphism that **intentionally changes what the episteme is about** (the occupant of `DescribedEntitySlot` in C.2.1) under a declared `KindBridge` and invariant, while remaining conservative with respect to that invariant.

**Placement.** After **A.6.3 `U.EpistemicViewing`**, before **A.6.5 `U.RelationSlotDiscipline`**.

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.3 `U.EpistemicViewing`; A.6.5 `U.RelationSlotDiscipline`; A.7/E.10.D2 (I/D/S discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot graph`; C.2/C.3 (KD‑CAL/LOG‑CAL, ReferencePlane, Kind‑level reasoning); F.9 (Bridges, `KindBridge`, CL/CL^plane, SquareLaw witnesses).

**Used by.**
E.18 (E.TGA StructuralReinterpretation and other reinterpretation nodes); discipline packs for signal/spectrum transforms, data↔model retargetings, abstraction/refinement under kind‑invariants; KD‑CAL/LOG‑CAL retargeting rules; additional species for architecture and governance reinterpretations.

**Governed object in plain terms.** One effect-free episteme-to-episteme retargeting where the source episteme and receiving episteme intentionally describe different but bridge-related entities.

**Governing move in plain terms.** Change the occupant of `DescribedEntitySlot` under a declared `KindBridge` and invariant, while making preserved commitments, withdrawn commitments, admissible predicate changes, and source-bearing reopen conditions visible.

**Use this when.** Use this pattern when a representation, view, functional description, model, diagram, `StructuralReinterpretation`, or other episteme-facing item no longer describes the same entity, but a declared bridge and invariant make a controlled retargeting admissible.

**What goes wrong if missed.** A changed target is treated as "the same thing in another form", so readers inherit claims, gates, evidence, work authority, or TGA-path currentness that the new described entity does not support.

**What this buys.** One honest retargeting relation: the reader can see the source entity, receiving entity, bridge, invariant, preserved commitments, lost or new commitments, and the exact admissible use that remains.

**Not this pattern when.** Not this pattern when the described entity is preserved and the main change is wording (`A.6.3.CR`), representation scheme or reasoning medium (`A.6.3.RT`), controlled coarsening (`A.6.3.CSC`), explanation mode (`E.17.EFP`), bridge-supported comparison without retargeting (`F.9` or `F.9.1`), work (`A.15`), evidence (`A.10`), assurance (`B.3`), gate decision (`A.21`), temporal adequacy (`C.27`), or dynamics/control law (`A.3.3`).

