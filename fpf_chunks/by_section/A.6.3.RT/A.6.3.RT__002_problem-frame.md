---
chunk_kind: "child"
pattern_id: "A.6.3.RT"
pattern_title: "Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
section_id: "A.6.3.RT:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.RT/A.6.3.RT__002_problem-frame.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "A.6.3.RT — Representation-Scheme Transition: EntityOfConcern-Preserving Representation-Scheme Transition"
  - "A.6.3.RT:1 — Problem frame"
line_start: 14846
line_end: 14879
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
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
  - "B.5.2.0"
  - "C.2.1"
  - "C.2.7"
  - "C.26"
  - "C.27"
  - "C.29"
  - "E.10.D2"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18"
  - "E.24.PUB"
  - "F.9"
keywords:
---

### A.6.3.RT:1 - Problem frame

Use this pattern when practical content must survive a change of representation scheme or reasoning medium: prose to table, table to diagram, diagram to structured notation, a model to a different inspectable rendering, or another declared representation change. In plain language: **change the representation while preserving what matters for this use**.

Start with the content that must survive and the target representation that will make it more usable. Produce the target, compare it with the source, and state what was preserved, foregrounded, rearranged, lost, or newly suggested. Exact episteme identities are not prerequisites for this ordinary first result.

Plain starting vocabulary:

| Term | Plain meaning |
| --- | --- |
| `source material` | The source claims, table, prose, diagram, model, record, publication, or other material being re-represented. In an exact case, distinguish the source episteme from its form, carrier, world-side concern, and additional inputs. |
| `content to survive` | The claims, relations, commitments, uncertainty, source pins, or distinctions the target representation must still support for the declared use. |
| `target representation` | The table, diagram, notation, structured record, or other representation chosen for the receiving task. Its visible form or carrier does not by itself identify a receiving episteme. |
| `representation scheme` | The declared regime under which claim content is represented and interpreted for this use. |
| `reasoning medium` | What the representation lets a user inspect, compare, infer, traverse, or replay more or less easily. |
| `representation delta` | What changed in shape, notation, salience, topology, ordering, interaction, or another representation factor. |
| `loss and recoverability` | What becomes harder to see or is omitted, and how the user can recover it when it matters. |
| `use and return` | What the target supports, what it does not support, and when and where to return to source material. |
| `representation worker` | The person, team, or system doing the conversion. Recover the exact system-role assignment, method, and dated Work only when production history matters; doing the work grants no authority over the represented claims. |

**First useful move.** Name the content that must survive and the target representation; make the target; then attach a compact representation note: source material, intended user action, target representation and why, preserved content, representation/reasoning-medium delta, loss or unsupported additions, admissible and non-admissible use, and return trigger.

**What goes wrong if missed.** A cleaner table, diagram, notation, or decoded rendering is treated as harmless formatting after it has hidden uncertainty, changed the concern, imported a new relation, weakened recoverability, or invited a stronger action than the source supports.

**What this buys.** Users gain a representation suited to their task while preservation, reasoning affordances, loss, unsupported strengthening, and source return stay visible. The rendering does not thereby become knowledge, ontology, Work, `U.View`, publication authority, evidence, or assurance.

**Ordinary use.** For inspection, comparison, source-finding, technical discussion, or reversible planning preparation, the target representation and compact note are normally enough.

**Reliance-facing use.** Open the exact episteme-construction branch when the target must travel independently, be cited or disputed, cross a scheme boundary for consequential use, enter generated or decode-mediated admission, or satisfy a named public, evidence, or assurance receiver. Then recover exact source episteme `X`, receiving episteme `Y`, and viewing construction `v : X -> Y`, together with the source chain, scheme relation, loss/recoverability, evidence, or assurance actually needed for that use.

**Later-specific occurrence.** Open `RepresentationSchemeTransitionRelation@Context` only when actual representation-transformation Work and the exact six participants defined in §4.1.b are themselves material. An exact `v : X -> Y` does not imply that occurrence.

**Not this pattern when.** Use A.6.3.CR for same-regime wording, A.6.3.NAR when reader-useful narrative ordering is primary, E.17.EFP when explanation adequacy is primary, A.6.4 when the EntityOfConcern changes, A.7 for carrier or extraction work before a receiving episteme exists, and A.6.3.CSC when a narrower-use coarsened receiving episteme is primary.

