---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "System-Role–Method–Work Alignment"
section_id: "A.15:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__001_intro.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.15 — System-Role–Method–Work Alignment"
  - "A.15:intro — Intro"
line_start: 28576
line_end: 28626
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
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.3.4"
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

**Use this when.** Use A.15 when a receiving decision needs to connect classification or assignment, Method, capability, planning and performed Work while keeping the particular claims distinct. Recover only the values and relations that decision consumes.

**Start here when.** The team is mixing system classification or assignment with recipe, schedule, capability, or performed Work, often under an ambiguous source word such as *role*, *process*, *workflow*, or *activity*.

**First output.** For planning, identify the intended WorkPlan, performer, local system-role kind and Method only as the next decision requires them. For precise actual performance, recover the A.13 core and independently admit dated Work under A.15.1 from its history, Method, extent and containing-System relation. Add F.6 `performedUnderAssignment` only for precise assignment-bound attribution, using that same obtaining assignment. State that the System performed the Work under the assignment and that the Work enacted the Method only when both relations obtain. Keep descriptions, plans, capability claims, records and results distinct.



**Minimum sufficient use.** Recover only the values and relations needed by the receiving use. Ordinary orientation can stop at one clear sentence. A reliance-bearing claim may also need exact occurrence identity and extent, the selected source and its currentness, a capability-fit claim, and the evidence or assurance claim actually relied on.

**Recovered-reference sufficiency condition.** Proceed when every value and relation consumed by the claim is recoverable with the meaning, identity and conditions that use needs. Otherwise narrow the claim or recover the missing basis. A bounded reversible probe is one option when its attainable contribution justifies its burden under C.11.DUA. Record a repair or decision request, prospective plan entry or source gap only when the continuation needs it.

**Ordinary use.** “Robot-7 performed InspectionWork-17 under InspectionAssignment-17, and the Work enacted TurbineInspectionMethod” can be enough when the A.13 core, same obtaining assignment, F.6 link, and `enactsMethod` relation remain recoverable and the receiving use needs no additional identifiers. A Grade or autonomy profile is not implied.

**Reliance-bearing use.** Use the fuller frame when assignment identity, assignment state, Method edition, capability fit, plan baseline, approval, evidence, release, or disputed responsibility changes the decision. Responsibility and authority remain separate direct relations; neither follows from a system-role kind or assignment.

**Stop condition.** Stop when the needed values and relations are clear enough for the supported next use and further separation would not change that use.

**Admissible-use examples.**

| Admissible project use | Source-finding or reversible probe | Non-admissible use |
| --- | --- | --- |
| A maintenance team identifies the local inspection kind, assignment species and occurrence, Method, and any description or WorkPlan needed by its decision. After inspection, it identifies dated Work independently of the inspection record. | A briefing lacks a source or relation required for its attempted use; use it to locate or recover that basis before making the unsupported claim. | The presence or form of a dashboard, copied approval, generated explanation, label or briefing is treated as proof of assignment, Method, WorkPlan or performed Work. Its content may supply evidence when A.10 supports that use. |

**Alignment frame in plain terms.** The system-role kind says what contribution kind is in question. The assignment relates this System to that kind while its predicate obtains. The Method is the way the Work is done. A MethodDescription describes the admitted Method; a WorkPlan states possible future Work. Dated Work is what happened. A log reports it and remains distinct from that occurrence.

**What goes wrong if missed.** A team collapses classification, assignment, recipe, plan, capability, and performed Work into one fuzzy “process” or “role” label, then mistakes documentation for execution, capability for performance, a schedule for an occurrence, or an assignment for responsibility.

**What this buys.** A compact trace answers who performed the Work, under which assignment, which Method it enacted, and which separate plan and evidence applied, while leaving each additional claim to its direct pattern.

**Not this pattern when.** Use `A.15.1` for one dated Work occurrence, `A.15.2` for planning or schedule baselines, `A.15.5` for work-entry readiness, `A.16` or `A.16.1` for a cue that has not become an alignment question, `A.6` or `A.6.B` for boundary or policy wording, `E.10.ROLE` when *role* is still unresolved, and `A.15.4` when a visible item is being relied on by appearance.

**Related pattern contributions.** Use `A.2` and C.3 to identify exact local system-role kinds, `A.2.1` for direct `U.SystemRoleAssignment` species, A.13 for the precise local agency core and any conditionally consumed profile, `F.6` for performed-Work attribution through that same assignment, `A.15.1` for dated Work, `A.15.2` for WorkPlan epistemes, `A.15.3` for declaration-local planned-filling content inside a WorkPlan, `A.15.4` for work-relevant reliance by appearance, `A.15.5` for work-entry readiness, `F.11` to align Method and Work vocabulary across contexts, and `F.17` for the human-facing term sheet.

**Causal-use work boundary.** Causal inquiry can use the Method, plan, performer and Work distinctions when those claims are needed. `C.28` separately governs the causal-use question, rung, estimand, identification, estimate, sampling and simulation contributions, and supported or unsupported uses. Alignment alone does not establish causal admissibility.

**Related-record mistakes.** A cue, publication, plan, record, result, evidence item, or approval can help locate a value without becoming that value. Recover the dated Work under `A.15.1`. State a subject-specific production or result relation only under its direct pattern; for a production-work, entity-inception, or production-completion question, A.15.PROD may instead return one local claim or exact blocker. Use `A.15.4` only when reliance on an encountered appearance is the problem.

**Boundary to coarsened renderings.** A briefing, summary, redacted note, or coarsened rendering may orient work. Rely on it for an execution, approval, gate, or evidence question only when the exact sources and relations required by that use remain explicit and reopenable. Use `A.6.3.CSC` when coarsening itself changes what may be relied on.


**Outside-practice result boundary.** When one receiving decision or piece of Work needs a bounded result governed by another practice, use `A.15.9` to inspect an already-available result before requesting anything new, ask only for the remaining gap, and preserve supplier Method and authority separately from the receiving decision. A.15 keeps the underlying Method, Work, performer, assignment, communication, result, and record distinctions unchanged.

