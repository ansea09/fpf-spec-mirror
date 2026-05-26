---
chunk_kind: "child"
pattern_id: "C.22.2"
pattern_title: "ProblemCard@Context"
section_id: "C.22.2:7"
section_title: "Source Record-Form Receiving Map"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.2/C.22.2__008_source-record-form-receiving-map.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.22.2 — ProblemCard@Context"
  - "C.22.2:7 — Source Record-Form Receiving Map"
line_start: 42862
line_end: 42911
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.21"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "A.6.Q"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "C.25"
  - "C.27"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.SEMIO"
  - "E.16"
  - "E.17"
  - "E.17.ID.CR"
  - "E.18"
  - "E.2"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.6"
  - "G.9"
keywords:
  - "P2W-ready"
  - "Thin problem card"
  - "first-principles cue"
  - "freshness and unknown disposition"
  - "problem card"
  - "problem signal"
  - "problem-side record"
  - "safe-probe-needed"
  - "setContextRef"
  - "support posture"
  - "validation boundary"
---

### C.22.2:7 - Source Record-Form Receiving Map

These are source-form recovery rows, not a taxonomy of FPF forms or `C.22.2` subkinds. This map keeps source wording from becoming local `C.22.2` subobjects. A form may enrich the problem card only when it supplies problem-side source, set, characterization, or comparison material. Authority, evidence, gate, autonomy, work, method, and result forms remain neighboring exits.

Problem-side and set-source forms:

| Source record form | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| Problem card | Carried by this pattern. | Use `C.22.2 - ProblemCard@Context`. |
| Problematization passport | Absorbed as the compact support template inside `C.22.2`. | Do not mint a new FPF object. |
| Problem archive | Assigned to archive, pool, and provenance patterns. | Use `C.18`, `C.19`, `A.10`, and `G.6`; do not create a local portfolio or archive kind in `C.22.2`. |
| Problem portfolio | Assigned to selected-set, pool-policy, parity, and refresh patterns. | Use `G.5`, `C.19`, `G.9`, and `G.11` according to the live relation. |
| Selected set, shortlist, front, archive, pool, or Goldilocks source | Preserved only as source or set-source cue. | Use `setContextRef`, source set kind, source-set form, selection or retention basis, non-scalar next move, and the receiving pattern when live. |
| Solution search | Assigned to archive, pool, or selection patterns according to state. | Use `C.18`, `C.19`, `C.11`, or `G.5`; `C.22.2` names only the search exit. |
| Solution portfolio | Assigned to selected-set, archive, front, and method-family selection patterns. | Use `G.5`, `C.18`, `C.19`, and `G.9`; `C.22.2` only carries the candidate acceptance-basis reference and set-return exits that make downstream solution selection reviewable. |

Comparison and characterization forms:

| Source record form | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| Characterization passport | Assigned to characterization and comparison patterns. | Use `C.16`, `A.19`, and `C.25` where live; `C.22.2` cites the basis. |
| Characteristic card | Assigned to characteristic and scale discipline. | Use `A.19` and `C.16`; problem-card use appears through `indicator selection` and `characteristic or Q-bundle basis`. |
| Parity plan or report | Assigned to parity harness. | Use `G.9`; `C.22.2` names the need for parity only as a neighboring-pattern exit. |
| Rule-of-choice card | Assigned to local choice or selected-set patterns when a chooser and option set are live. | Use `C.11` for local choice records; use `G.5` for selected-set publication and `C.19` for pool policy. |

Neighboring authority, evidence, work, method, and result forms:

| Source record form | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| ADR-like decision record | Assigned by the decision being recorded. | Use `E.9` for FPF content decisions, `C.11` for local choice records, and `A.21` for gate decision logs. |
| Evidence pack | Assigned to evidence, provenance, and assurance patterns. | Use `A.10`, `G.6`, and `B.3`; `C.22.2` names support posture and validation boundary without certifying evidence. |
| Autonomy budget declaration | Assigned to autonomy governance. | Use `E.16`; `C.22.2` carries only risk or autonomy cues that point to this pattern. |
| Autonomy ledger | Assigned to autonomy, work, and gate patterns. | Use `E.16` with `A.15` and `A.21` when work or gates are live. |
| Gate decision log | Assigned to gate decision recording. | Use `A.21`; if the same record also carries evidence or provenance load, that load exits to `A.10`, `G.6`, or `B.3`. |
| Override protocol | Assigned by the live autonomy, gate, work, evidence, or control relation. | Use `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` as applicable. Use `A.2.8` only when an explicit deontic relation is live. |
| Deontic commitment, permission, or obligation | Assigned only when the commitment, permission, or obligation is explicit. | Use `A.2.8`; do not apply it to logs or override-looking wording by appearance. |
| Method selection | Assigned to method-family selection. | Use `G.5` and `A.15`; `C.22.2` carries only method-family cues. |
| Work planning | Assigned to work-planning patterns. | Use `A.15` and `SlotFillingsPlanItem`; not `TaskSignature`. |
| Performed work | Assigned to work, evidence, and provenance patterns. | Use `A.15`, `A.10`, `G.6`, and `B.3` according to use. |
| Result record and result measurement | Assigned to evidence, provenance, assurance, measurement characterization, and refresh patterns. | Use `A.10`, `G.6`, `B.3`, `C.16`, and `G.11`; `C.22.2` does not certify results. |
| Candidate solution or described system | Assigned to selection, method, work, evidence, and system-description patterns according to live use. | Use `G.5`, `A.15`, `E.17`, `E.18`, `A.10`, `G.6`, and `B.3`; do not treat selected solution publication as the problem card. |
| Runbook and rollback plan | Assigned to work-planning, gate, autonomy, evidence, and control patterns. | Use `A.15`, `A.21`, `E.16`, `A.10`, `G.6`, and `B.3`; `C.22.2` may name reversibility or containment as a risk or validation boundary only. |

Source-local exposition terms:

| Source wording | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| Problem factory, solution factory, or factory-of-factories | Source exposition for related work families, not FPF process kinds. | `C.22.2` covers only the problem-side output. Solution and P2W work exits to `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, or `G.11` when those relations are live. |
| Ordinary log | Assigned by the relation the log is used to support. | Use `A.10`, `G.6`, or `B.3` when evidence, provenance, assurance, or support posture is live; use `G.11` when the log supports refresh or update discipline. `C.22.2` may cite the cue, but does not treat a log as problem evidence by appearance. |
| Passport, card, budget, ledger, protocol, plan, and pack wording | Recovered by use, not by label shape. | If the source term carries problem-side material, recover it through the relevant `C.22.2` field. If it carries authority, evidence, gate, autonomy, work, method, result, selection, or assurance load, send that relation to the receiving pattern. |
