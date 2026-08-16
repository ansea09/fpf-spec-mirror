---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "System-Role–Method–Work Alignment"
section_id: "A.15:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__001_intro.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "A.15 — System-Role–Method–Work Alignment"
  - "A.15:intro — Intro"
line_start: 23900
line_end: 23959
dependencies:
  - "A.10"
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
  - "Method"
  - "MethodDescription"
  - "WorkPlan"
  - "assignment"
  - "attribution"
  - "dated Work"
  - "readiness"
  - "result boundary"
  - "system-role kind"
---

## A.15 - System-Role–Method–Work Alignment

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use this pattern when a team must say which system performed which Work, under which system-role assignment, which Method the Work enacted, and which plan applied without confusing any of those values with a description, capability, record, or result.

**Use this when.** Separate a local system-role kind, an assignment occurrence that obtains, its holder system, a `U.Method`, any `U.MethodDescription`, a `U.WorkPlan`, a holder `U.Capability` instance and its support, and dated Work before a schedule, display, document, or familiar label is treated as if it established the whole chain.

**Start here when.** The team is mixing system classification or assignment with recipe, schedule, capability, or performed Work, often under an ambiguous source word such as *role*, *process*, *workflow*, or *activity*.

**First output.** The smallest inspectable alignment needed by the receiving use: one exact Work occurrence `W`, one exact assignment occurrence `RA` belonging to a direct species under `U.SystemRoleAssignment`, the holder system `RA.HolderSystemSlot`, and one Method `M`, with `performedUnderAssignment(W, RA)` and `enactsMethod(W, M)` stated only when they obtain. Keep the local system-role kind, MethodDescription, WorkPlan, capability, assertions, records, and results separate.

**Working enactment-alignment sequence.** Recover the holder system and local system-role kind -> recover the assignment occurrence and its declared species -> separate Method from MethodDescription, WorkPlan from Work, and capability from performance -> state only the relations needed by the next use -> proceed, plan, probe, narrow, use the pattern for another claim, or stop.

**Working alignment applications.**

1. Name the holder system and the local system-role kind relevant to the work.
2. Name the declared assignment species and the occurrence that actually obtains. The species defines the holder and assigned-kind positions; the occurrence supplies their actual values. Add another participant only when it changes the assignment.
3. Name the Method and keep any MethodDescription separate. Name either the intended `U.WorkPlan` or the actual dated Work occurrence, never one as proof of the other.
4. State `performedUnderAssignment` and `enactsMethod` only when their predicates obtain. The holder system performs the Work; neither the kind, assignment, Method, description, plan, nor capability acts.
5. If a visible item is being relied on for a Work, approval, evidence, gate, or release claim before its supporting relation is known, use `A.15.4`; keep only the alignment part here.

**Action-pattern protection.** This pattern does not classify encountered publications, displays, or cues. It keeps system-role kind, assignment, Method, MethodDescription, plan, capability, performed Work, and records distinct so an engineer-manager can choose the next admissible action. Use `A.15.4` for work-relevant appearance-based reliance repair.

**Minimum sufficient use.** Recover only the values and relations needed by the receiving use. Ordinary orientation can stop at one clear sentence. A reliance-bearing claim may need exact occurrence identity, source, extent, and support.

**Recovered-reference sufficiency condition.** Proceed when every project-side value on which the claim relies is identified by its admitted kind, exact referent, scope, and current window. Otherwise narrow the claim, run a bounded reversible probe, recover the missing relation, or create only the smallest repair request, decision request, prospective WorkPlan entry, or missing-source note needed for the next use.

**Ordinary use.** “Robot-7 performed InspectionWork-17 under InspectionAssignment-17 using TurbineInspectionMethod” can be enough when those three relations and identities are already current.

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

**Related pattern contributions.** Use `A.2` and C.3 to identify exact local system-role kinds, `A.2.1` for direct `U.SystemRoleAssignment` species, `F.6` for performed-Work attribution, `A.15.1` for dated Work, `A.15.2` for WorkPlan epistemes, `A.15.3` for slot-filling plan items, `A.15.4` for work-relevant reliance by appearance, `A.15.5` for work-entry readiness, `F.11` to align Method and Work vocabulary across contexts, and `F.17` for the human-facing work sheet.

**Causal-use work boundary.** Counterfactual sampling, randomization, intervention assignment, target-trial emulation, and causal evidence collection can be represented here as Methods, MethodDescriptions, WorkPlans, dated Work occurrences, and their exact assignment and Method relations. A.15 does not make the resulting causal use admissible. Use `C.28` for the causal-use question, `CausalityLadderRung`, causal estimand, `CausalEvidenceSupportBasis`, counterfactual-sampling realizability, `CausalUseSupportVerdict`, and its supported and unsupported uses.

**Related-record mistakes.** A cue, publication, plan, record, result, evidence item, or approval can help locate a value without becoming that value. Recover the dated Work under `A.15.1`; state production or result relations under their direct patterns; and use `A.15.4` only when reliance on an encountered appearance is the problem.

**Boundary to coarsened renderings.** A briefing, summary, redacted note, or coarsened rendering may orient work. It supports execution, approval, gate, or evidence use only when the required sources and relations remain explicit and reopenable. Use `A.6.3.CSC` when coarsening itself changes what may be relied on.

**Use boundary.** A.15 supplies only the system-role–Method–Work alignment needed by the current project question. Send a single occurrence, wording, assurance, evidence, result, or reliance question to the pattern that defines or tests that claim.

