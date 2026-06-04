---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition"
section_id: "A.6.3.RT:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__001_intro.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "A.6.3.RT — RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition"
  - "A.6.3.RT:intro — Intro"
line_start: 10863
line_end: 10912
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
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicRetargeting"
  - "U.EpistemicViewing"
keywords:
---

## A.6.3.RT - RepresentationTransduction — entityOfConcernRef-preserving representation-scheme transition
> **Status:** Stable

**Placement.** Specialization under `A.6.3 U.EpistemicViewing` for entityOfConcernRef-preserving representation-scheme transition.
**Builds on.** `A.6.3 U.EpistemicViewing`; `A.6.2 U.EffectFreeEpistemicMorphing`; `A.7`; `E.10.D2`; `C.2.7`; `E.17.0`; `E.17`; `F.9`; `F.18`.
**Coordinates with.** `ConservativeRetextualization`; `A.6.3.CSC Controlled Semantic Coarsening`; `ExplanationFaithfulnessProfile`; `E.17.ID.CR ComparativeReading`; `A.6.4 U.EpistemicRetargeting`; `F.9`; `F.9.1`; `E.18`; `A.15`; `A.10`; `B.3`; `B.5.2`; `A.20`; `A.21`; `C.27`; `A.3.3`; explicit decoding-access review.
**Name boundary.** In this pattern, `RepresentationTransduction` names an `A.6.3 U.EpistemicViewing` specialization for an entityOfConcernRef-preserving transition across declared representation schemes or reasoning media. It is not an `E.18` Transduction Graph Architecture node, not a TGA graph edge, not an `A.15` method description, work-plan, or work-occurrence claim, and not a changed-function or control-architecture claim.

**One-line summary.** `RepresentationTransduction` is an entityOfConcernRef-preserving shift in representation scheme that stays inside `A.6.3 U.EpistemicViewing`: it may move between prose, table, diagram, structured notation, or another declared representation regime, but it does **not** silently change `entityOfConcernRef`, promote geometry or notation into ontology-by-default, or hide decode-mediated recoverability behind rendering fluency.
**EntityOfConcern preservation discipline.** In this specialization, entityOfConcernRef-preserving representation change means the C.2.1 `entityOfConcernRef` stays stable while representation scheme, reasoning medium, recoverability, and loss are made explicit.

**Primary EntityOfConcern in plain terms.** One published rendering of the same EntityOfConcern in a different representation scheme or reasoning medium; not the whole source corpus, not a new ontology, and not carrier-operation work.
**Admissible move in plain terms.** Change representation scheme while keeping entityOfConcernRef-preserving continuity witness reviewable, factor deltas visible, and handoff explicit when the case has become explanation, retargeting, bridge work, or a narrower-use card.

**Use this when.** Use this pattern when the same EntityOfConcern needs to move across representation schemes or reasoning media such as prose, table, diagram, or structured notation, and the real job is still the representation shift rather than explanation, retargeting, or downstream action.

**Start here when.** Your first honest publication unit already changes representation scheme or reasoning medium, and the main review question is whether the receiving representation keeps a visible source-relation path and entityOfConcernRef-preserving continuity rather than becoming a new ontology, a hidden bridge, or a coarsened proxy.

**What goes wrong if missed.** A table, diagram, or notation shift gets treated as harmless formatting even after it has started hiding recoverability loss, silent EntityOfConcern or ontology shift, decode work, or a separate narrower-use card.

**What this buys.** One honest entityOfConcernRef-preserving representation shift with visible source-relation path, visible factor and reasoning-medium change, and an explicit handoff when the case stops being ordinary representation transduction.

**Working action spine.** The same `entityOfConcernRef` appears in a new representation scheme -> separate source representation or publication, receiving representation or rendering, preserved claim, representation scheme, reasoning medium, and admissible use -> use the rendering for inspection, source-finding, comparison, technical review, or reversible planning preparation -> output the ordinary use path or the fuller continuity-witness decision block when ambiguity, dispute, citation, reliance, bridge, work, gate, assurance, decode-mediated access, abductive reopen, temporal/dynamics, release, or TGA-path use is live -> hand off if work, evidence, gate, explanation, retargeting, bridge, carrier, coarsened-rendering, abductive, temporal, dynamics, or TGA claim appears.

**Ordinary use.** If the publication-facing item is admissible only for inspection, source-finding, comparison, or planning preparation, keep the explicit interpretation of the source representation or publication, the receiving representation or rendering, the one preserved `entityOfConcernRef`, preserved claim, representation-scheme change, and admissible and non-admissible use.

**Ordinary use path.**
1. Which source representation or publication and receiving representation or rendering are being compared, and is preservation of the same `entityOfConcernRef` explicit?
2. Which source claim or commitment remains preserved for the intended use?
3. What representation scheme, reasoning medium, or expression form changed?
4. What reader action remains admissible, and what downstream use is not admissible from this representation shift alone?

**Action/work boundary.** A representation shift may be admissible for method inspection or work-planning preparation, but the source for intended or actual work remains `A.15` plus the source `U.Episteme`, source `U.EpistemePublication`, or exact project-side FPF kind and reference that governs that work claim.

**Reliance-facing use.** Open the fuller continuity-witness decision block only when the shifted representation will be externally relied on, disputed, cited as an admissibility reason, used across context, treated as gate/release/work preparation justification, carried through a decode-mediated or latent access path, used in abductive reopen, or used for temporal/dynamics or TGA-path currentness.

**Representation-validity grounding.** Recoverability is recoverability for one declared admissible use, not a general property of the receiving representation. A diagram, table, notation, decoded output, or model-state rendering may be recoverable enough for inspection or technical review when receiving-side relations trace back to source-relation records and loss notes, while still being insufficient for work-planning reliance, gate reliance, release reliance, evidence reliance, assurance reliance, or engineering justification. For any such reliance use, this pattern supplies only same-EntityOfConcern correspondence witness; the operative admissibility must come from the governing FPF pattern and exact project-side FPF kind and reference named by `A.15`, `A.10`, `A.20`, `A.21`, `B.3`, `E.17.EFP`, `E.17.ID.CR`, `F.9`, or `F.9.1` as applicable. When the shifted representation will carry claim-bearing use, state the admissibility path that makes that exact use admissible: source-relation path, recoverability scope, decode path where needed, evidence class, any probe evidence, intervention evidence, or causal-abstraction claim, and the `E.17:5.1b` source-relation class when source pointer, source availability, source retrieval, source use, source faithfulness, claim admissibility, contradiction, omission, claim widening, or reopen trigger could diverge. Use `E.17:5.1c` for the shared use-boundary meanings of `orientation use`, `reliance use`, `operative claim`, `non-admissible downstream use`, and `reopen trigger`; use `E.17:5.1d` when the primary live question may belong to ordinary textual restatement, coarsening, explanation, comparison, bridge work, substitution, work, reliance, gate, evidence, assurance, retargeting, or carrier and front-end work.

A table, diagram, notation, decoded output, or model-state rendering may expose or cite its source relation. It does not become that source relation, architecture, ontology, evidence, gate, or work source by visual clarity, geometry, notation, proximity, or reuse. If the needed admissibility path is missing, a repair request, source-gap note, or evidence-work plan is prospective only; it does not retroactively make the earlier representation shift admissible.

**Stop condition.** Stop once the representation shift changes no next inspection, comparison, source-finding, or planning-preparation move and blocks no concrete overclaim about the represented entity, source relation, work, gate, or evidence.

**Admissible-use examples.**

| Admissible project-side use | Source-finding or reversible probe | Non-admissible downstream use |
| --- | --- | --- |
| A table or diagram makes the same EntityOfConcern easier to inspect while the source-relation path and representation-scheme change stay visible. | A diagram helps reversible planning or source inspection while the team checks recoverability, source-relation records, or decode path before gate, work, evidence, or justification use. | A diagram, geometry, table, or notation is treated as architecture, ontology, evidence, gate passage, work authority, or engineering justification by visual form alone. |

**Not this pattern when.** Not this pattern when only wording changes (`ConservativeRetextualization`), explanation becomes primary (`ExplanationFaithfulnessProfile`), the EntityOfConcern changes (`A.6.4`), or the receiving representation stays honest only by carrying its own narrower admissible use, non-admissible downstream use, declared source-loss mode, and source-bearing reopen card. In that last case, use `A.6.3.CSC Controlled Semantic Coarsening` instead of resolving it as ordinary `RepresentationTransduction`.

