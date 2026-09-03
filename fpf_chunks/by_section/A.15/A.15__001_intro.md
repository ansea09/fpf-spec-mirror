---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "System-Role–Method–Work Alignment"
section_id: "A.15:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__001_intro.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.15 — System-Role–Method–Work Alignment"
  - "A.15:intro — Intro"
line_start: 24557
line_end: 24618
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.20"
  - "A.21"
  - "A.3"
  - "A.6"
  - "A.6.5"
  - "A.7"
  - "B.3"
  - "C.28"
  - "C.29"
  - "C.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17.EFP"
  - "E.18.1"
  - "F.6"
  - "U.SystemRoleAssignment"
keywords:
  - "A.13 core"
  - "Method"
  - "MethodDescription"
  - "WorkPlan"
  - "conditional agency profile"
  - "dated Work"
  - "independent A.15.1 Work admission"
  - "performedUnderAssignment"
  - "readiness"
  - "result boundary"
  - "same obtaining assignment"
  - "separate later F.6 attribution"
  - "system-role kind"
---

## A.15 - System-Role–Method–Work Alignment

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use this pattern when a team must say which System performed which Work, under which assignment, which Method the Work enacted, and which plan applied without confusing any of those values with a description, capability, record, or result. A precise actual-performer branch first reuses A.13's core, then A.15.1 independently admits the dated Work, and only afterward F.6 uses the same obtaining assignment when precise assignment-bound attribution is current; an agency characteristic profile remains conditional on its receiving use.

**Use this when.** Separate a local system-role kind, an assignment occurrence that obtains, its holder system, a `U.Method`, any `U.MethodDescription`, a `U.WorkPlan`, a holder `U.Capability` instance, the capability-fit and evidence claims actually relied on, and dated Work before a schedule, display, document, or familiar label is treated as if it established the whole chain.

**Start here when.** The team is mixing system classification or assignment with recipe, schedule, capability, or performed Work, often under an ambiguous source word such as *role*, *process*, *workflow*, or *activity*.

**First output.** If the team is planning, name the intended `U.WorkPlan`, intended performer System, local system-role kind, and Method needed by the next decision; do not invent Work or an obtaining assignment. If performance has occurred, first recover the A.13 core and independently admit the dated Work under A.15.1 from its actual history, Method, extent, and containing-System relation. Then, only when precise assignment-bound attribution is current, establish F.6 `performedUnderAssignment` through the same obtaining assignment. Name only the assignment occurrence, declared species, holder System, and Method needed by this decision. Say plainly that the A.13-qualified holder System performed the Work under that same assignment and that the Work enacted the Method only when both relations obtain. Keep the local system-role kind, MethodDescription, WorkPlan, capability, assertions, records, and results separate in either branch.

**Working enactment-alignment sequence.** For precise actual performance, recover the A.13 core for the holder System and local agential kind -> recover the same obtaining assignment occurrence and its declared species -> separate Method from MethodDescription, WorkPlan from Work, and capability from performance -> independently admit the dated Work through A.15.1 -> apply F.6 only when precise assignment-bound attribution is current -> state only the relations needed by the next use -> proceed, plan, probe, narrow, use the pattern for another claim, or stop.

**Working alignment applications.**

1. For a precise actual-performer claim, recover the exact holder System, the local agential system-role kind and criterion, classification, same obtaining assignment, scope, working situation, window, and adequate A.13 core evidence. Add a characteristic profile only when a Grade, autonomy or profile result, criterion-dependent characteristic, or assurance use consumes it.
2. Name the declared assignment species and the occurrence that actually obtains. The species defines the holder and assigned-kind positions; the occurrence supplies their actual values. Add another participant only when it changes the assignment.
3. Name the Method and keep any MethodDescription separate. Name either the intended `U.WorkPlan` or the actual dated Work occurrence, never one as proof of the other.
4. State `performedUnderAssignment` and `enactsMethod` only when their predicates obtain. The holder system performs the Work; neither the kind, assignment, Method, description, plan, nor capability acts.
5. If a visible item is being relied on for a Work, approval, evidence, gate, or release claim before the relation required by that claim is known, use `A.15.4`; keep only the alignment part here.

**Action-pattern protection.** This pattern does not classify encountered publications, displays, or cues. It keeps system-role kind, assignment, Method, MethodDescription, plan, capability, performed Work, and records distinct so an engineer-manager can choose the next admissible action. Use `A.15.4` for work-relevant appearance-based reliance repair.

**Minimum sufficient use.** Recover only the values and relations needed by the receiving use. Ordinary orientation can stop at one clear sentence. A reliance-bearing claim may also need exact occurrence identity and extent, the selected source and its currentness, a capability-fit claim, and the evidence or assurance claim actually relied on.

**Recovered-reference sufficiency condition.** Proceed when every project-side value on which the claim relies is identified by its admitted kind, exact referent, scope, and current window. Otherwise narrow the claim, run a bounded reversible probe, recover the missing relation, or create only the smallest repair request, decision request, prospective WorkPlan entry, or missing-source note needed for the next use.

**Ordinary use.** “Robot-7 performed InspectionWork-17 under InspectionAssignment-17, and the Work enacted TurbineInspectionMethod” can be enough when the A.13 core, same obtaining assignment, F.6 link, and `enactsMethod` relation remain recoverable and the receiving use needs no identifiers. A Grade or autonomy profile is not implied.

**Reliance-bearing use.** Use the fuller frame when assignment identity, assignment state, Method edition, capability fit, plan baseline, approval, evidence, release, or disputed responsibility changes the decision. Responsibility and authority remain separate direct relations; neither follows from a system-role kind or assignment.

**Stop condition.** Stop once the separation changes no next admissible use and blocks no concrete overclaim about classification, assignment, assignment state, Method, plan, Work, result, approval, evidence, or release.

**Admissible-use examples.**

| Admissible project use | Source-finding or reversible probe | Non-admissible use |
| --- | --- | --- |
| A maintenance team identifies `PumpInspectorSystemRole`, the direct `MaintenanceInspectionAssignment` species and current occurrence, the inspection MethodDescription, and the current `U.WorkPlan`. After inspection, it identifies the dated Work occurrence and a separate inspection record. | A briefing says inspection is ready, but the MethodDescription, plan, or assignment occurrence is missing; use the briefing only to locate or repair that source before reliance. | A dashboard tile, copied approval, generated explanation, role label, or briefing is treated as the assignment, Method, WorkPlan, performed Work, or execution evidence. |

**Alignment frame in plain terms.** The system-role kind says what contribution kind is in question. The assignment says that this system holds that kind in one actual episode. The Method says how the Work is done. The WorkPlan says what is intended. The dated Work occurrence says what happened. Descriptions and records state claims about those values; they are not those values.

**What goes wrong if missed.** A team collapses classification, assignment, recipe, plan, capability, and performed Work into one fuzzy “process” or “role” label, then mistakes documentation for execution, capability for performance, a schedule for an occurrence, or an assignment for responsibility.

**What this buys.** A compact trace that answers who performed the Work, under which assignment, which Method the Work enacted, and which separate plan and evidence applied, while leaving every stronger neighboring claim to its direct pattern.

**Not this pattern when.** Use `A.15.1` for one dated Work occurrence, `A.15.2` for planning or schedule baselines, `A.15.5` for work-entry readiness, `A.16` or `A.16.1` for a cue that has not become an alignment question, `A.6` or `A.6.B` for boundary or policy wording, `E.10.ROLE` when *role* is still unresolved, and `A.15.4` when a visible item is being relied on by appearance.

**Related pattern contributions.** Use `A.2` and C.3 to identify exact local system-role kinds, `A.2.1` for direct `U.SystemRoleAssignment` species, A.13 for the precise local agency core and any conditionally consumed profile, `F.6` for performed-Work attribution through that same assignment, `A.15.1` for dated Work, `A.15.2` for WorkPlan epistemes, `A.15.3` for declaration-local planned-filling content inside a WorkPlan, `A.15.4` for work-relevant reliance by appearance, `A.15.5` for work-entry readiness, `F.11` to align Method and Work vocabulary across contexts, and `F.17` for the human-facing work sheet.

**Causal-use work boundary.** Counterfactual sampling, randomization, intervention assignment, target-trial emulation, and causal evidence collection can be represented here as Methods, MethodDescriptions, WorkPlans, dated Work occurrences, and their exact assignment and Method relations. A.15 does not make the resulting causal use admissible. Use `C.28` for the causal-use question, rung, estimand, separate evidence/identification/estimate/sampling/simulation components, counterfactual-sampling result, support result, and supported and unsupported uses.

**Related-record mistakes.** A cue, publication, plan, record, result, evidence item, or approval can help locate a value without becoming that value. Recover the dated Work under `A.15.1`. State a subject-specific production or result relation only under its direct pattern; for a production-work, entity-inception, or production-completion question, A.15.PROD may instead return one local claim or exact blocker. Use `A.15.4` only when reliance on an encountered appearance is the problem.

**Boundary to coarsened renderings.** A briefing, summary, redacted note, or coarsened rendering may orient work. Rely on it for an execution, approval, gate, or evidence question only when the exact sources and relations required by that use remain explicit and reopenable. Use `A.6.3.CSC` when coarsening itself changes what may be relied on.

**Use boundary.** A.15 supplies only the system-role–Method–Work alignment needed by the current project question. Send a single occurrence, wording, assurance, evidence, result, or reliance question to the pattern that defines or tests that claim.

**Outside-practice result boundary.** When one receiving decision or piece of Work needs a bounded result governed by another practice, use `A.15.9` to inspect an already-available result before requesting anything new, ask only for the remaining gap, and preserve supplier Method and authority separately from the receiving decision. A.15 keeps the underlying Method, Work, performer, assignment, communication, result, and record distinctions unchanged.

