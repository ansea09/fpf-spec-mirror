---
chunk_kind: "child"
pattern_id: "E.3"
pattern_title: "Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
section_id: "E.3:6"
section_title: "Illustrative Conflict Resolution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.3/E.3__007_illustrative-conflict-resolution.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "E.3 — Principle Taxonomy, Precedence and Agent Autonomy Profiles (ABL)"
  - "E.3:6 — Illustrative Conflict Resolution"
line_start: 79026
line_end: 79087
dependencies:
  - "E.1"
  - "E.2"
keywords:
  - "ABL"
  - "Arch"
  - "BLP waiver"
  - "Did"
  - "Epist"
  - "Gov"
  - "Prag"
  - "autonomy budget"
  - "conflict resolution"
  - "oversight"
  - "precedence"
  - "principle taxonomy"
  - "profile change"
---

### E.3:6 - Illustrative Conflict Resolution

**Same-kind wording.** First recover the intended kind under A.1. For an already identified U.System, compare the plain name System with its technical expression U.System; both name the same kind. P-1 supports a precise, economical expression, while P-2 expressly gives human comprehension priority over theoretical or tooling purity. Use the familiar wording where it preserves the required meaning and make the technical designation recoverable where needed. The default Arch-over-Did order does not reverse that explicit P-2 priority. U.System is a proper subtype of U.Holon: replacing a non-System Holon with System would change the subject’s extension before any legitimate wording comparison.

**Two Gov rules with no priority.** Suppose two rules at the same source level apply to publishing report R to audience A at noon: rule G1 requires that action and G2 forbids it. Both are Gov and neither has priority over the other. Return G1/G2, R, A and the noon window as the unresolved conflict; hold publication. Merely listing the class and an acyclic graph does not settle it. The rule-governing authority can authorize an applicable priority or scope amendment with the §4.2 rationale. A proposed G1-over-G2 edge that completes an existing G2-to-G1 path is rejected; the hold remains until a permitted resolution exists. An authorized amendment outside this action's scope leaves this conflict unresolved.

**BLP and a guard.** If an applicable E.5 guard excludes a proposed implementation dependency, BLP-6 already gives that guard priority over BLP. Compare those particular rules in their current scope, not the E.2 and E.5 files as whole nodes. B.3 enters the policy ordering for an assurance requirement actually consumed by the use.

**Local product policy and a pillar.** A product preference cannot override an applicable pillar merely because a local policy says it wins. A disclosed local tie-break can settle only a preference left open by the applicable higher rules. Classify the compared principles; a compound policy such as BLP need not receive one class for all its provisions.

**BLP-policy precedence (high → low, for applicable rules).** Law & Regulation → **E.5 Guard-Rails** → **B.3 assurance requirements consumed by the use** → **E.3 governance decisions** → **E/E-LOG policies** (editioned) → **BLP derived policy (E.2 §6)** → Product Policies → Implementation Tactics. This scope-specific ordering implements the stated BLP safeguards; it does not place a derived policy above a pillar or create unconditional file-to-file edges.

**Notes.**
* BLP is a constitutional policy (see E.2 / “BLP”), but **does not supersede** E.5 Guard‑Rails nor B.3 assurance floors; it governs an activated scale comparison; a non-dominant result leaves any generality tie-break to a separately declared local policy.
* Wherever **NQD/E/E‑LOG** promotes illumination telemetry to dominance (via an explicit **CAL** policy; **policy‑id recorded in SCR**), **BLP adopts that lens** rather than overriding it (see E.2 BLP‑6).
* Any exception to policy **MUST** include a DRR with rationale and expiry.
* **BLP Override (Waiver).** A waiver is needed only when an applicable declared generality policy would otherwise decide the use and its exception rule is invoked. Name that policy, the rationale, responsible review System and direct responsibility basis, expiry/review, and the evidence required by the actual exception. Apply C.19.1's waiver and debt conditions. Ordinary bounded specialization is not an override. Add an AutonomyProfileId and GateDecision authority only when an independently applicable agentic profile governs the action.
**Set-returning parity.** Activated scale comparisons preserve parity and admissible operations under A.18; use G.5/G.9 where their selector/parity contracts apply. Independently applicable stronger profiles retain those requirements. Mixed-scale scalarization without an admissible operation remains prohibited.

**BLP — Bitter-Lesson Hooks into Precedence**
1) **Comparison and tie-breaking.** Under E.2 BLP-2, compare usable responses over the declared range and receiving conditions, with uncertainty and applicable α/δ tolerances. Slope dominance alone supplies no usable-performance preference. On non-dominance, a generality preference must be a separately declared local policy allowed by higher rules.
2) **Procedure and search.** Select a positive procedure or general search under the task/control requirements and applicable policy. A mandated safety procedure keeps its force. BLP adds no universal prohibition-first rule or waiver for a fixed procedure.
3) **Publication.** A BLP precedence result retains the actual policy/edition and comparison basis. A performed full audit publishes its material resource and assurance accounts under E.2 BLP-1d and G.11. A bounded use with no scale claim creates no audit package.

**ABL — Autonomy‑Budget & Oversight Profiles (GateProfile)**
This section defines an **extensible family of autonomy oversight profiles** for agentic tool use: each profile specifies (i) a budget envelope, (ii) a Freedom‑of‑Action (FoA) descriptor, and (iii) the required **publication of a gate decision authorizing execution** under that envelope. The familiar labels **L0…L4** are treated here as **profile identifiers** (not a fixed managerial ladder): projects MAY introduce additional profiles or sub‑profiles by minting new profile ids, provided they publish the same fields (budgets, FoA, decision roles, telemetry requirements) and keep profile changes explicit and auditable.

| ProfileId | Name                         | Freedom‑of‑Action (FoA)                  | Explore‑Share (default) | Typical Use                                     | GateDecision authority |
|---------:|------------------------------|------------------------------------------|-------------------------|-------------------------------------------------|------------------------|
| **L0** | Scripted Execution           | **Whitelist only**; fixed scripts        | 0                       | Compliance‑critical, deterministic procedures   | Engineer‑of‑Record (EoR) |
| **L1** | Constrained Sequencing       | Negative constraints; **single‑tool**    | ≤ 0.10                  | Low‑risk automation with bounded novelty        | EoR + Peer Review |
| **L2** | Supervised Autonomy          | Multi‑tool plans; bounded replanning     | 0.20 (±0.10)            | Ambiguous tasks; moderate budget                | Team Lead + Safety |
| **L3** | Auditable Autonomy           | Multi‑step, self‑replanning; adaptive    | 0.30 (±0.10)            | Production agents with learning under guard‑rails | Product + Safety + Legal |
| **L4** | Open‑Ended / Research Mode   | Broad FoA within sandbox & rails         | 0.40–0.50               | Illumination‑first exploration, sandboxes only  | Governance Board (Gov‑CAL) |

**Normative requirements by profile.**
* **Budgets.** Each profile **MUST** declare ceilings for **time / compute / cost / risk** and a FoA descriptor; units must be explicit under **C.16**, planned ceilings remain **A.15.2** WorkPlan content, and run‑time consumption is tied to dated Work, aggregation, and provenance under **A.15.1**, **B.1.6**, and **A.10**. Budgets are **hard gates** at run‑time (**A.21**; C.Agent‑Tools‑CAL **ATC‑3** for stopping or replanning when a ceiling is breached).
* **Profile binding & change visibility.** Every CallPlan **MUST** declare the active profile id. A profile change **MUST** retain its from/to profiles, policy editions, effective window and A.21 permission result in the DecisionLog. Recompute the decision when its subject, action, rule, checks, scope or window changes. Cite an E.18 GateCrossing only when an independently selected TFS, exact source/receiving positions and changed CtxState bindings establish that structural transition. Add an F.9 Bridge only for its independently obtaining relation between the two F.17 local senses.
* **Assurance floors.** Apply B.3 to the named assurance claim and receiving use. A required F floor uses C.2.3's ordinal meaning; any R threshold, composition, or CL loss needs its justified quantity, scale, and model under B.3/C.2.2. No universal F/R weakest-link minimum is imposed by an autonomy-profile label, and F does not substitute for R. Any justified profile-specific tightening for broader FoA **MUST** be declared on the profile and pinned by policy-id; the actual protection and decision-authority conditions remain binding. Pre-deployment **assurance deltas** MUST be recorded for L2+.
* **Exploration discipline.** When a still-live C.19 pool constrains the `CallPlan`, cite its `PoolPolicyResult`. Include the exact `EmitterPolicy` and `explore_share` only when the plan uses that profile, including `0` when it explicitly plans no exploration. Apply the declared profile's exception rule to a deviation; do not invent live-pool refs after the action is fixed and pool treatment is irrelevant.
* **Provenance.** L1+ MUST emit a **CallGraph** with Service/Method editions, any actually used EmitterPolicyRef, budget deltas, and observation hooks (C.Agent‑Tools‑CAL **ATC‑5**).
* **BLP conformance.** Apply E.2 BLP when selection makes a scale claim or invokes a declared generality policy, retaining its actual α/δ tolerances and conditional debt requirements. L2+ alone does not manufacture a scale claim. A profile that independently requires a fuller comparison or audit must state that trigger and basis; its other budget, oversight and assurance duties remain binding.
* **Learning/Adaptation.** L3–L4 MAY enable adaptation only under product permission, change authority, E.5 and privacy controls. L0–L2 retain their profile default off unless their authorized policy change documents mitigation. Remaining fixed needs no BLP waiver; changing an applicable product requirement follows that requirement's exception rule.
* **Human‑in‑the‑Loop (HITL).** HITL obligations are expressed as **gate decisions and pause/resume hooks**, not an implicit “approval ladder”:
  * **L0–L1:** execution MAY start only after an explicit **GateDecision** authorizing the CallPlan is present in the declared window.
  * **L2:** sentinels MUST be able to pause execution; resumption requires a new **GateDecision** recorded in the DecisionLog.
  * **L3:** the profile MUST declare periodic review windows; continued execution across a review boundary requires an explicit **GateDecision**.
  * **L4:** continuous telemetry review; the default execution context is **sandboxed**. Leaving the sandbox requires an explicit A.21 GateDecision for that bounded action, with the applicable signers, budget, scope/window and stop conditions. Publish the decision and profile/policy change. When the case also satisfies E.18’s structural crossing conditions, cite its CrossingRef and required per-binding accounts. Unchanged local meanings need no invented F.9 Bridge.

**Gate‑decision authority map (default signers; who may author GateDecisions).**
* **L0:** EoR or appointed maintainer.
* **L1:** EoR **and** peer reviewer (two‑person rule).
* **L2:** Team Lead **and** Safety representative.
* **L3:** Product Owner **and** Safety **and** Legal/Privacy.
* **L4:** **Gov‑CAL Board** (multi‑disciplinary) with documented scope, time‑boxed **trial budget**, and rollback criteria.

**Profile promotion / demotion triggers.**
* **Promote** a profile when the active profile's required performance and assurance evidence shows stability within its declared tolerances and budget adherence for ≥ **N_policy** runs. Promotion requires its A.21 GateDecision. If a scale claim supports promotion, cite the usable-response comparison under E.2 BLP-1c; slope evidence alone is insufficient. Keep every independently required profile check.
* **Demote** a profile when: (i) the profile's declared risk or budget ceiling is breached, (ii) assurance drops below floors, (iii) policy changes, or (iv) a significant **heuristic‑debt** item expires without replacement. Demotion **MUST** be published as a profile-change and permission result with updated budgets and policies pinned. Any structural crossing is established separately under E.18.

**Profile-change cases.** A local budget revision from twenty to thirty minutes with unchanged meanings requires the authorized profile/policy change and its permission result; absent a selected TFS transition, it has no GateCrossing. If the profile label remains L2, the original twenty-minute permission still cannot authorize execution at minute twenty-five. Apply the authorized new ceiling, required checks and effective window before continuing; otherwise stop at the old ceiling. A case that changes a CtxState binding between two positions in an independently selected TFS also satisfies E.18’s crossing obligations. Leaving a sandbox with unchanged F.17 senses still needs the declared authorization and oversight, but supplies no semantic Bridge. Stop/resume, signer and budget duties remain applicable in each case under its profile.

