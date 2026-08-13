---
chunk_kind: "child"
pattern_id: "C.2.P"
pattern_title: "Epistemic Precision Restoration"
section_id: "C.2.P:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.P/C.2.P__002_use-this-when.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "C.2.P — Epistemic Precision Restoration"
  - "C.2.P:0 — Use this when"
line_start: 41894
line_end: 41939
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.20"
  - "A.21"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.A"
  - "A.6.F"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.16.Q"
  - "C.2.1"
  - "C.30.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.12"
  - "E.17"
  - "E.17.0"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.2"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.9"
  - "F.18"
keywords:
---

### C.2.P:0 - Use this when
**First useful move.** Decide whether the wording is source-expression clarification or FPF-governed use. Then write the smallest sufficient output: repaired sentence, candidate-set note, compact epistemic precision-restoration row, full epistemic precision-restoration check, or explicit non-use disposition.

**Source-expression clarification.** Use this mode when ordinary non-FPF prose needs precise interpretation. The aim is source-local clarification: recover what the sentence may mean, identify candidate kinds and relations, preserve important wording when needed, and produce one clarified phrase, candidate-set note, epistemic precision-restoration note, or use disposition. This mode may use `E.10`, `A.6.P`, `A.6.6`, `F.18`, `A.7`, `E.17`, or another relevant FPF pattern as a repair lens, but it does not require the source expression itself to use FPF vocabulary.

**FPF-governed use.** Use this mode when wording has FPF-governed use and hides one of this pattern's recovery fields. The field may be an episteme or episteme-side view field; a publication, publication form, generic publication face, MVPK face under E.17 constraints, or bounded publication unit field; a carrier or rendering relation; a relation or declared-use-boundary field; or a pattern-application wording field. The wording states the recovered FPF kind named by value, relation record, relation phrase, tuple-like record, project-side FPF kind and reference named by value, or explicit non-use disposition.

Use `C.2.P` as epistemic precision restoration for wording whose hidden field belongs to one of these field families, not to one new umbrella kind:
- source-expression fields: source wording and source-local meaning;
- episteme fields: claim-bearing episteme, episteme-side view, EntityOfConcern, and grounding relation;
- publication fields: publication, face, publication unit, publication-form relation, carrier relation, and rendering relation;
- project-side-use fields: pattern-application wording, project-side reliance wording, and the disposition by which source expression has or lacks FPF-governed use.

Use `E.10` for lexical and wording-use precision and `C.2.P` for epistemic precision restoration across episteme, publication, carrier-relation, and view distinctions. The C.2.P recovery fields are source expression, source-local meaning, recovered FPF kind and relation set, publication construction, carrier relation construction, view construction, EntityOfConcern or grounding relation, reader use, and use or non-use disposition. These are fields of one recovery pass, not sibling kinds.

The practical partition is episteme-slot or publication-construction use, but it is not limited to named `C.2.1` slots. It also handles source expressions selected for FPF-governed use and pattern-application wording when those phrases carry a claim or use boundary. Apply this pattern from `E.10` only when the applicable pattern cannot yet be selected because one recovery field is unresolved: source wording, claim-bearing episteme, publication construction, carrier-relation construction, project-side reliance, pattern-application wording, or use or non-use disposition. The local decision selects source-expression clarification or FPF-governed use, recovers the episteme-publication relation set, chooses a recovery disposition, and preserves remaining reader use before a neighboring pattern supplies its own definition, constraint, or test.

For source-wording restoration, `C.2.P` stops at recovery. It names the recovered FPF kind, relation, `projectSideFPFRef`, `declaredUseBoundary`, `relationClaimSlice`, remaining reader use, or explicit non-use disposition. When another FPF pattern defines, constrains, or tests a recovered field, name that pattern and leave the field in its ontology. Do not turn source wording into a standalone kind or keep authority, evidence, gate, work, assurance, or readiness inside source wording.

**Source-use wording guard.** Do not read `source-use` as ordinary work with primary sources or citations. In this pattern, the compact phrase only flags that source wording, a source-bearing relation, a source-ref marker with its referenced object kind or relation slot named, or a source-finding cue is being asked to support FPF-governed use. The actual recovered field must be named through this pattern's fields: source expression, publication relation, carrier relation, relation slice, declared-use boundary, project-side FPF reference, or explicit non-use disposition. If that field is not recoverable, write the more specific phrase - source wording, source-bearing relation, unresolved source-finding cue, quote-only wording, or no FPF-governed use - instead of closing on `source-use`.

**Source-to-use continuity rule.** A source-wording repair is not closed merely because the broad word `source` was replaced by a more precise object name. Preserve the relation that made the wording useful. Name the source expression or source-bearing position that matters: selected source `U.Episteme`; an `EpistemePublicationRelation` occurrence or reference when availability matters; publication form or face; carrier, source-currentness, or source-bearing relation; source-ref marker with its referenced kind or relation slot; relation-claim slice; project-side FPF kind and reference; declared-use boundary; or explicit non-use disposition. Then state which input is used, what transformation, rendering, or use path carries it forward, what use is admissible, and what reopen condition or next pattern applies if the use escalates. Do not close on `value` unless the applicable pattern has a value slot. If these answers cannot be stated, lower the wording to source-finding only, reduced-use cue, blocked use, or incomplete rewrite.

**Epistemic source-material and work-boundary sequence.** When `source data` or epistemic `source material` is current, first recover the source expression, selected source `U.Episteme`, any publication occurrence needed to establish availability, and the source-to-use relation. Then treat any separate relation to a method, plan, work occurrence, transformation, evaluation, delivery, transfer, or receiving use—and the posture claimed for that relation—with the applicable pattern. Stop if that work-side relation and posture are already readable; apply `A.6.P.WMR` only while either remains hidden. Keep physical raw material in its constituent, affected-referent, resource-use, supply, transfer, or transformation relation; the adjective `source` does not move it into `C.2.P`. The source-side settlement and the work-side relation claim are distinct and must not be merged.

**Source-return boundary.** Do not use `source-return` as the generic name for source-wording repair. In the current FPF corpus, `source-return condition` is admissible only for the reverse or escalation edge in a derivative, coarsened, extracted, compressed, rendered, or reused carrier. The reader has already moved away from a named source expression, selected source `U.Episteme`, publication occurrence when availability matters, source-bearing relation, transform record, or evidence relation; a stronger use, dispute, freshness change, hidden loss, or missing distinction now requires return to that source or relation. Name a rule-bearing `ClaimGraph` only when later comparison or reuse depends on rule identity. For ordinary movement from source into current use, say source-to-use path, source relation, source-bearing relation, source expression, or name the applicable relation.

**Work-reliance boundary.** `C.2.P` does not decide whether work may proceed. Use `A.15.4` only after the wording repair shows that an appearance is being used as a reason for intended work or reliance and the relevant slot, relation, or project-side reference is still unnamed. If the applicable pattern is already known, use it without an `A.15.4` intermediate step.

**Precision-restoration pattern note.** A precision-restoration pattern is an architectural pattern for a recurring complex precision problem whose wording routinely hides several current distinctions. `A.6.P` is relation precision restoration; `C.2.P` is epistemic precision restoration. `C.30.P` is the selected architecture and structure precision-restoration pattern when architecture or structure wording hides the architecture claim being made, structure kind, structure relation, view, publication relation, or source relation selected for the current architecture claim. `C.16.P` is the selected characteristic and scale precision-restoration pattern when characteristic, scale, metric, score, indicator, coordinate, threshold, or comparison construction is hidden. `C.16.Q` is the selected quality-term precision-restoration pattern when quality-term or evaluative characterization is current and the found problem is not relation construction. `E.10` detects the wording problem and selects the applicable recovery pattern; `E.10.ARCH` carries the shared recovery algorithm and applicability-row architecture; neither replaces this pattern's episteme, publication, and source-relation ontology.

| Problem in the wording | Use this pattern for | Applicable neighboring FPF pattern |
| --- | --- | --- |
| Ordinary source text needs more precise language | Source-expression clarification: clarify the source-local meaning and, when needed, produce a candidate-set note, epistemic precision-restoration note, or use disposition. These are output forms for one clarification pass, not object kinds. | `E.10`, `A.6.P`, `A.6.6`, `F.18`, `A.7`, `E.17`, or another relevant pattern as a lens for the claim or declared-use-boundary question. |
| Wording has FPF-governed use | FPF-governed use: fill the smallest needed recovery field: recovered FPF kind named by value, relation record, relation phrase, tuple-like record, project-side FPF kind and reference named by value, or explicit non-use disposition. | `E.10` plus the pattern that defines, constrains, or tests each recovered claim or declared-use boundary. |
| An episteme or publication field is current | Recover the field family before accepting the sentence: claim-bearing episteme and its EntityOfConcern or grounding relation; publication, view, face, or bounded publication unit; carrier relation; or source relation named by value. | `C.2.1`, `A.7`, `E.17.0`, `E.17`, MVPK, and local episteme and publication patterns. |
| A relation or use-boundary field is current | Recover the relation, claim being made, declared-use boundary, or project-side reliance field before treating the wording as FPF-governed. | `A.6.P`, retained A.6.P specializations, `A.6.B`, and the applicable evidence, work, decision, assurance, causal-use, mathematical-lens, or quality pattern. |
| A reusable term or stable local head is being chosen | Prevent a broad replacement from becoming a new FPF term by taste. | `F.18`, with `E.10:0.2` replacement-candidate anti-umbrella rule. |
| The repair would leave correct typing but no useful reader action | Treat the rewrite as incomplete. | `E.2`, `E.8`, `E.10:6.2`, `E.12`, and the FPF pattern named by value that carries the claim being made. |

**Ordinary-language survival.** Ordinary words can stay ordinary until the sentence gives them FPF-kind, relation, authority, evidence, use-boundary, work, gate, decision, bridge, or reliance claim. `Source` may stay ordinary when it only means where a quote came from; `view` may stay ordinary when it means what the reader sees and not `U.View`; `route` may stay ordinary navigation prose; `support` may stay ordinary help. Repair by FPF-governed sentence function, not by trigger word alone.

**Not this pattern when.** `C.2.P` is not the pattern for every recovered construct. Use `E.10` for general lexical conformance, `F.18` for stable reusable naming, `A.6.P` for relation precision, `A.6.B` for law-, use-boundary-, deontic-, and effect-claim splitting, `A.7` for EntityOfConcern, Description episteme, and carrier separation, and `E.17` or `E.17.0` for view and publication discipline. Use `C.30`, `C.30.ASV`, `A.22`, `C.31`, or the relevant architecture or structure pattern for those claims; use the relevant FPF pattern for project work, evidence, gate, decision, method, action-invitation, assurance, or engineering-justification claims. When one of these claims is current, `C.2.P` supplies source-expression unpacking and rewrite disposition; the named pattern supplies its invariant.

**Do not punish clarity.** Prefer the clearest ordinary head that preserves kind, relation, and declared use boundary. Do not replace a clear plain phrase with a technical phrase unless the technical phrase blocks a currently plausible false interpretation or is needed for accepted stable FPF naming. In an ordinary case, `reader help`, `source-pointer-only`, or `comparison only` may be better than a more technical phrase.

