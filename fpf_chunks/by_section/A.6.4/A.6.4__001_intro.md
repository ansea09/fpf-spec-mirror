---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__001_intro.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:intro — Intro"
line_start: 15162
line_end: 15190
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

## A.6.4 - `U.EpistemicRetargeting` — EntityOfConcern retargeting morphism
> **Status:** Stable
> **Type:** Definitional ontic pattern

**One‑line summary.** `U.EpistemicRetargeting` is the **EntityOfConcern retargeting** species of `U.EffectFreeEpistemicMorphing`: an effect‑free episteme→episteme morphism that **intentionally changes what the episteme is about** (the value filling `EntityOfConcernSlot` in C.2.1) under a declared `KindBridge` and invariant, while remaining conservative with respect to that invariant.
**EntityOfConcern retargeting discipline.** A.6.4 names the retarget branch of the C.2.1 EntityOfConcern retargeting law: `entityOfConcernRef(Y) != entityOfConcernRef(X)` only under a declared `KindBridge`, invariant, loss boundary, and admissible use. Source-side spellings are source wording only; conformant text normalizes them to `EntityOfConcern*` before use.

**Placement.** After **A.6.3 `U.EpistemicViewing`**, before **A.6.5 `U.RelationSlotDiscipline`**.

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.3 `U.EpistemicViewing`; A.6.5 `U.RelationSlotDiscipline`; A.7 and E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use/refinement discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot relation`; C.2/C.3 (KD‑CAL/LOG‑CAL, ReferencePlane, Kind‑level reasoning); F.9 (Bridges, `KindBridge`, CL/CL^plane, SquareLaw witnesses).

**Used by.**
E.18 (`StructuralReinterpretation` loci and other transformation-flow reinterpretation loci); discipline packs for signal/spectrum transforms, data↔model retargetings, abstraction/refinement under kind‑invariants; KD‑CAL/LOG‑CAL retargeting rules; additional species for architecture and governance reinterpretations.

**Body-level U-kind settlement.** `U.EpistemicRetargeting` is the governed durable value in this pattern. It reuses `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, and `U.Episteme`; episteme card, view, and publication names are dependent C.2.1/E.17 values when those patterns govern them. `ClaimGraph`, `Viewpoint`, `ReferenceScheme`, and `RepresentationScheme` are C.2.1/A.6.5 slot fillers or ValueKinds. `SubjectRef` is source wiring through `DescriptionContext`. `EpMorphism` is the local mathematical-lens arrow value for retargeting, not a root U-kind.

**Retargeting in plain terms.** One effect-free episteme-to-episteme retargeting where the source episteme and receiving episteme intentionally describe different but bridge-related values of `EntityOfConcernSlot`.

**First retargeting move in plain terms.** Change the value filling `EntityOfConcernSlot` under a declared `KindBridge` and invariant, while making preserved commitments, withdrawn commitments, admissible predicate changes, and source-bearing reopen conditions visible.

**Use this when.** Use this pattern when a representation, view, functional description, model, diagram, `StructuralReinterpretation`, or other episteme-facing item no longer preserves `entityOfConcernRef`, but a declared bridge and invariant make a controlled retargeting admissible.

**What goes wrong if missed.** A changed EntityOfConcern is treated as "the same thing in another form", so users inherit claims, gates, evidence, work authority, or transformation-flow path currentness that the receiving EntityOfConcern does not make admissible.

**What this buys.** One honest retargeting relation: the reader can see the source entity, receiving entity, bridge, invariant, preserved commitments, lost or new commitments, and the specific admissible use that remains.

**Not this pattern when.** Not this pattern when the EntityOfConcern is preserved and the main change is wording (`A.6.3.CR`), representation scheme or reasoning medium (`A.6.3.RT`), controlled coarsening (`A.6.3.CSC`), explanation mode (`E.17.EFP`), bridge-only comparison without retargeting (`F.9` or `F.9.1`), work (`A.15`), evidence (`A.10`), assurance (`B.3`), gate decision (`A.21`), temporal adequacy (`C.27`), or dynamics/control law (`A.3.3`).

