---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__005_solution.md"
commit_sha: "646b0b9b164f7c13258633a33b92d2d0a569da28"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:4 — Solution"
line_start: 11384
line_end: 11513
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "C.26"
  - "C.26.1"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "coarsened rendering"
  - "controlled semantic coarsening"
  - "dashboard tile"
  - "lookup handle"
  - "narrower admissible use"
  - "non-admissible downstream use"
  - "redaction"
  - "reopen trigger"
  - "source-bearing episteme or source publication"
  - "state-representation shortcut"
---

### A.6.3.CSC:4 - Solution

`Controlled Semantic Coarsening` governs one source-to-rendering relation.

- **Source-bearing side** means the governed `U.Episteme`, governed `U.EpistemePublication`, or declared source set that still carries the fuller claim, distinction, evidence relation, trace relation, or authority-reference relation. A declared source set must have a stable source-set identifier, bounded membership, and a reopen condition; an open corpus, folder, topic area, search-result cluster, or vague document neighborhood is not a source-bearing side.
- **Coarsened rendering** means the readable form that carries a declared `source-loss mode`, reduced recoverability, reduced reliability transport, or narrower admissible use than the source-bearing side.
- **Narrower admissible use** means the practical use the coarsened rendering makes admissible, such as orientation, retrieval, bounded disclosure, workshop framing, or preliminary triage.
- **Non-admissible downstream use** means the use the coarsened rendering does not make admissible alone, such as approval, audit closure, release gate, work plan, equivalence, bridge or substitution use, accountability finding, or canonical technical claim.
- **Reopen trigger** means the condition that requires return to the source-bearing side, re-expansion in the current rendering or publication, or handoff to another governing FPF pattern or `authoritySourceRef` destination.
- **Claim-bearing case** means a coarsening case that will be cited, disputed, externally relied on, policy-bearing, bridge-adjacent, gate-adjacent, work-adjacent, privacy-sensitive, or assurance-facing.

#### A.6.3.CSC:4.1 - Ordinary mini-card

For ordinary use, publish only the smallest card that keeps the coarsened rendering honest.

| Row | Question |
| --- | --- |
| Source-bearing side | What source episteme, source publication, or declared source set remains governing and reopenable? |
| Coarsened rendering | What coarsened readable form is being offered to the reader? |
| Narrower admissible use | What use does this coarsened rendering make admissible? |
| Source-loss mode | Which declared source-loss mode is live: omitted-detail, qualifier-loss, redaction, aggregation, scope-narrowing, recoverability-loss, representation-factor-loss, or coarsening-loss? |
| Non-admissible downstream use | What downstream claim, effect, work, or reliance use is not admissible from this coarsened rendering alone? |
| Reopen trigger | What demand forces source-bearing return, re-expansion, or governing-pattern handoff? |

A CSC card makes only the narrower admissible use named on the card admissible for the coarsened rendering. It never makes the non-admissible downstream use admissible; it only tells the reader when and where to reopen the source-bearing side or hand off to the governing pattern that carries that downstream use.

The card may live inline. Inherited source pins count when the surrounding publication already makes the source-bearing side visible.

If the coarsened rendering is used only for local orientation and the source-bearing side remains adjacent, the six-row card may be inline or implicit by immediate context; do not create a durable `Controlled Semantic Coarsening` object unless reuse, reliance, citation, or dispute appears.

#### A.6.3.CSC:4.2 - First check

Before using this pattern, ask five questions:

1. Is there exactly one source-bearing side: one source episteme that remains governing, source publication, or declared source set with stable identifier, bounded membership, and reopen condition?
2. Does the coarsened rendering declare a source-loss mode against that source-bearing side, or has review shown that it can be retained only as a coarsened rendering?
3. Does the coarsened rendering make only narrower use admissible?
4. Is downstream use explicitly non-admissible from the coarsened rendering alone?
5. Is the source-bearing reopen or governing-pattern handoff trigger visible?

If any answer is no, do not polish a coarsening story. Use the ordinary governing pattern or recover the project-side FPF kind and reference named by value or authority-reference relation that actually makes the requested use admissible. If the required admissibility path is missing, create only a prospective repair request, future decision request, prospective work-plan entry, or explicit source-gap note; do not treat that request or note as retroactive admissibility for the coarsened rendering, earlier claim or effect, work occurrence, evidence, approval, gate passage, release permission, or engineering justification.

#### A.6.3.CSC:4.3 - Ordinary vs claim-bearing

Ordinary cases should remain light. A short orientation summary, redacted partner note, workshop simplification, or lookup handle does not need the full assurance record if the six-row card is recoverable.

Claim-bearing cases add only the fields that matter for the use under repair, dispute, reliance, citation, policy, bridge, work, gate, privacy, or assurance case. This list is not a daily gate for ordinary summaries, briefings, redactions, or lookup handles:

The fields below inherit the `E.17:5.1e` local-field rule. They are review aids for one coarsened-rendering case, not `U.Kind`, `publication-face kind`, `RelationKind`, `KindBridge`, `EvidenceKind`, `GateDecision`, `SpeechAct`, `Commitment`, `U.Work`, `authoritySourceRef` destination, or project-side FPF kind and reference named by value unless another governing FPF pattern explicitly instantiates that object.

- `sourceBearingSideRef` and `coarsenedRenderingRef` when the source-bearing side, coarsened rendering, `PublicationUnit`, publication face, E.17 publication-face kind value `publication face/form`, E.17 publication-face kind value `interop publication form`, or carrier could be confused;
- `coarsenedRenderingPublicationUnitIfAny` when the coarsened rendering is carried by one `PublicationUnit` that is distinct from the publication, disclosure note, dashboard tile, or `interop publication form` on which it appears;
- `governingPatternRef`, `projectSourceRecordRef`, or one privileged reopen path, so a coarsened rendering cannot reset its own provenance;
- `coarseningBranch`, `sourceLossMode`, and `admissibleUseValue` as separate fields;
- `recoverabilityAfterCoarsening` when the source-loss mode affects claim admissibility, accountability, admissible-use value, or later citation;
- at least one kept claim bundle or distinction bundle, one coarsened or dropped bundle, and one reopen-only bundle when the case is disputed or later-cited;
- `sourceRelationClass` when the `E.17:5.1b` classes could diverge: source pointer, source availability, source retrieval, source use, source faithfulness, claim admissibility, contradiction, plausibility-only, omission, declared source-loss mode, added commitment, added linkage, independent verification, admissible use, non-admissible downstream use, or reopen trigger;
- uncertainty or abstention state when branch interpretation, preserved distinctions, source pin, or admissible use cannot yet be stated stably;
- independent-verification question when downstream testing, assurance, gate, or external reliance appears;
- `audienceOverReadRisk`, plus a light reader-reliance or user-evidence check when readers may mistake the coarsened rendering for authority it does not carry;
- whether local re-expansion is enough to repair the current rendering or whether downstream use still needs return to the source-bearing side or named `authoritySourceRef` destination.

#### A.6.3.CSC:4.4 - Branch and admissible-use discipline

`coarseningBranch` answers what sort of coarsening case this is. `sourceLossMode` names what was lost from the source-bearing side. `admissibleUseValue` answers which use of the coarsened rendering remains admissible. Do not infer any one of the three from the others.

| Field | Values this pattern uses | Rule |
| --- | --- | --- |
| `coarseningBranch` | aggregation or quotient-like orientation; source-pinned surrogate, index, or handle; privacy or redaction case; exceptional interop-facing simplification | The branch names the kind of coarsening case, not the source-loss mode and not the authority granted by the coarsened rendering. |
| `admissibleUseValue` | ordinary-admissible; source-pinned-only; authoritySourceRef-reopen-only; non-admissible-by-default | The admissible-use value names which use the coarsened rendering makes admissible. |

Ordinary admissible use covers aggregation, quotient-like orientation, didactic or report summaries, and briefings only for the named narrower use. Source-pinned-only use covers surrogate, index, retrieval-hint, lookup, and handle forms; these may help find or orient to the source but do not provide claim admissibility themselves. `authoritySourceRef-reopen-only` covers the exceptional case where the coarsened rendering names the source whose named authority relation must be reopened; the coarsened rendering itself does not become the `authoritySourceRef` destination, evidence source, gate source, or work source.

Privacy or redaction cases are admissible here only when the card names the sharing boundary, the source-loss mode, what was withheld or coarsened, the main re-identification or accountability risk being reduced, the source-bearing review path, and the accountability or gate uses that remain non-admissible.

Exceptional interop-facing simplification is not ordinary coarsening. It is admissible here only when it stays source-tethered and names the operative relation kind, such as bounded contrast, broader or narrower, partial overlap, proxy, lossy normalization, or context-bounded match. If the coarsened rendering makes bounded contrast across contexts or source epistemes or source publications is the primary question, use `E.17.ID.CR`. If it implies equivalence, substitution, projection, or bridge or substitution use, use `F.9` or `F.9.1`.

#### A.6.3.CSC:4.5 - Source-loss mode, recoverability, and anti-overread

The card must name the live `sourceLossMode` before a coarsened rendering is treated as admissible for its stated use. A source-loss mode is not a strength scale. It names which source-bearing distinction failed to travel into the coarsened rendering.

| Source-loss mode | Declared loss |
| --- | --- |
| `omitted-detail` | A detail present on the source-bearing side is absent from the coarsened rendering. |
| `qualifier-loss` | A condition, caveat, uncertainty marker, scope qualifier, temporal qualifier, modality marker, recommendation status, evidence status, possibility status, obligation status, or decision status is absent, collapsed, or less explicit. |
| `redaction` | Detail is withheld for a sharing boundary, privacy, safety, legal, partner-disclosure, accountability, or release reason. |
| `aggregation` | Several source distinctions, alternatives, entities, states, records, or slices are combined into one aggregate or quotient-like readable form. |
| `scope-narrowing` | The coarsened rendering carries only a narrower claim scope, audience scope, time window, source slice, context, population, or use scope. |
| `recoverability-loss` | The reader cannot recover source distinctions, pins, trace, provenance, confidence, relation structure, source relation, or decode path from the coarsened rendering at the level needed for the proposed use. |
| `representation-factor-loss` | A representation shift drops inspection possibilities, comparability, ordering, topology, relation structure, viewpoint relation, publication-face admissibility, or reasoning-medium factors that mattered on the source-bearing side. |
| `coarsening-loss` | The full CSC relation is live: source-bearing side, coarsened rendering, narrower admissible use, declared source-loss mode, non-admissible downstream use, and source-bearing reopen. |

Recoverability and admissible use are separate. A recoverable coarsened rendering is not automatically admissible for downstream use, and a non-admissible use is not repaired merely by saying the source could be found.

| Recoverability class | Reading |
| --- | --- |
| directly recoverable | the coarsened rendering itself still carries enough detail to recover the source-side distinction |
| source-pinned recoverable | the distinction is recoverable only by returning to the named source-bearing side |
| reconstruction or validation required | recovery needs a new reconstruction, test, or validation, so downstream use remains blocked until that work is done |
| not recoverable from admissible source epistemes or source publications | the available source epistemes or source publications, traces, or cited `authoritySourceRef` destinations cannot restore the distinction; do not treat the coarsened rendering as admissibility for downstream reliance |

A coarsening chain may not silently reset provenance. If one coarsened rendering is reused to make another, the same source-bearing side must stay explicit, the earlier source-loss mode and uncertainty state must remain visible, and the new rendering must declare only the added source-loss delta. If that cannot be stated cleanly, reopen the source-bearing side rather than extending the chain.

Aggregation or quotient-like coarsening remains inside this pattern only while the coarsened rendering keeps one bounded selected set, slice, case bundle, or alternative bundle explicit as the EntityOfConcern or selected set. If several entities, alternatives, or slices become one new class-level EntityOfConcern or proxy EntityOfConcern, apply `A.6.4`.

#### A.6.3.CSC:4.6 - Neighbor exits

| If the primary question is now... | Use this governing FPF pattern or `authoritySourceRef` destination |
| --- | --- |
| Same-entity textual rewording without a separate narrower-use card | `A.6.3.CR` |
| Representation scheme or reasoning-medium shift | `A.6.3.RT` |
| Explanation-facing class over existing source `U.Episteme` or `U.EpistemePublication` | `E.17.EFP` |
| Bounded comparison over already pinned source epistemes or source publications | `E.17.ID.CR` |
| Equivalence, substitution, interop row, or bridge or substitution use | `F.9` |
| Stance over an already published bridge card | `F.9.1` |
| Changed EntityOfConcern or proxy EntityOfConcern | `A.6.4` |
| Carrier, export, OCR or parsing, or front-end behavior is primary | `A.7` first; then `A.6.3.RT`, `A.6.3.CSC`, `A.6.4`, or interpretation sources only if meaning-bearing structure, loss, retargeting, or interpretive lift is live |
| Briefing treated as work plan, work authority, or execution cue | `A.15` |
| Gate, approval, assurance, or adjudication authority | `A.20` or `A.21` |

Neighboring governing patterns may point here when a coarsened rendering relation becomes primary. They do not govern the shared coarsening relation by local repetition.

#### A.6.3.CSC:4.7 - Well-formedness constraints

**Well-formedness constraint CSC-WF-1 (source-to-rendering relation).** A controlled-coarsening case is well formed only when it contains exactly one source-bearing side, at least one coarsened-rendering side, one declared narrower admissible use, one non-admissible downstream use, and one visible source-bearing reopen or governing-pattern handoff condition. The source-bearing side may be one source episteme that remains governing, source publication, or declared source set with stable source-set identifier and bounded membership; it must not be an open, vague corpus.

**Well-formedness constraint CSC-WF-2 (no authority upgrade).** A coarsened rendering does not gain evidence, bridge, work, approval, gate, or adjudication authority by repetition, fluency, audience convenience, citation, or publication on a more visible publication face or channel.

**Well-formedness constraint CSC-WF-3 (source path continuity).** A coarsening chain remains well formed only while the same source-bearing side, prior source-loss mode, uncertainty state, and added source-loss delta remain recoverable.

