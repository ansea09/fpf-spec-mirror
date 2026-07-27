---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__002_problem-frame.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:1 — Problem frame"
line_start: 13723
line_end: 13740
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.3.3"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.NAR"
  - "A.6.4"
  - "A.7"
  - "B.3"
  - "B.5.2"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.RT:1 - Problem frame

Use this pattern when the same EntityOfConcern needs to move across representation schemes or reasoning media: prose to table, table to diagram, diagram to structured notation, or another declared representation regime. The real job is still entityOfConcernRef-preserving representation shift, not explanation, retargeting, bridge work, evidence, gate authority, work authorization, carrier export, or decode-mediated reconstruction.

**Primary EntityOfConcern.** The `EntityOfConcern` is the representation-scheme transition case: an `entityOfConcernRef`-preserving relation between a source representation or publication and a receiving representation or rendering. The preserved object is named inside that relation as `preservedEntityOfConcernRef`; source and receiving representations are relation slots of the transition, not the governed object by themselves.

**First useful move.** Keep these entries recoverable before relying on the shifted representation: source representation or publication, receiving representation or rendering, preserved `entityOfConcernRef`, preserved claim or commitment, representation-scheme or reasoning-medium delta, loss or recoverability note, admissible use, non-admissible downstream use, and reopen or governing-pattern trigger.

**What goes wrong if missed.** A table, diagram, notation, or decoded rendering is treated as harmless formatting after it has started hiding recoverability loss, silent EntityOfConcern shift, hidden bridge work, decode work, or a narrower-use card.

**What this buys.** One honest entityOfConcernRef-preserving representation shift with visible source-relation chain, visible factor and reasoning-medium change, and a named governing pattern when the case stops being ordinary representation-scheme transition.

**Ordinary use.** If the publication-facing rendering is admissible only for inspection, source-finding, comparison, technical review, or reversible planning preparation, keep the positive field spine visible in the rendering or surrounding publication.

**Reliance-facing use.** Open the fuller continuity-review field set only when the shifted representation will be externally relied on, disputed, cited as an admissibility reason, used across context, treated as release, gate, work-preparation justification, carried through a decode-mediated or latent access relation, used in abductive return to source hypotheses, or used for temporal currentness, dynamics currentness, or transformation-flow currentness.

**Not this pattern when.** Not this pattern when only wording changes (`ConservativeRetextualization`), explanation becomes primary (`ExplanationFaithfulnessProfile`), the EntityOfConcern changes (`A.6.4`), carrier work such as rendering, export, or OCR-style extraction is the current claim, or the receiving representation stays honest only by carrying its own narrower admissible use, non-admissible downstream use, declared source-loss mode, and a card that names return to the exact source representation or source relations. In that last case, use `A.6.3.CSC Controlled Semantic Coarsening`.

