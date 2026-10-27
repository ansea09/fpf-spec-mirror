---
chunk_kind: "child"
pattern_id: "C.32.HCS"
pattern_title: "Architecture-Bearing Family Characteristic Starter Packs"
section_id: "C.32.HCS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.HCS/C.32.HCS__005_solution.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.32.HCS — Architecture-Bearing Family Characteristic Starter Packs"
  - "C.32.HCS:4 — Solution"
line_start: 76594
line_end: 76647
dependencies:
  - "A.19"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.PAD"
  - "E.10.ROLE"
  - "E.13"
  - "G.5"
keywords:
  - "Method"
  - "System"
  - "Work"
  - "architecture-bearing family"
  - "domain transfer"
  - "starter characteristics"
---

### C.32.HCS:4 - Solution

Choose a starter pack by the admitted holon family or recovered architecture-bearing family. Use the pack only to start narrowing starter heads into project criteria rows; then hand the result to `C.32.ACS` for the project criteria set.

#### C.32.HCS:4.1 - Starter pack construction

Build or use a starter pack in this order:

1. Name the admitted holon family or recovered architecture-bearing family. If the source label is method, role, practice, culture, tradition, style, or evidence practice, recover the bearer before choosing heads. A Method admitted by A.3.1 is itself a non-agentive holon; its description, a Work occurrence under A.15.1, and the performing System remain separate. When the label is only a description-side family, name the source-bearing episteme or publication context. Record only the recovery patterns actually used.
2. List a small set of starter characteristic heads that often matter for that family.
3. For each head, name likely bearers or selected structures, not only a quality word.
4. Record likely C.25 Q-Bundle boundaries when a head is usually composite.
5. State a first project question that helps the practitioner decide whether the head belongs as a draft row in the project criteria set.
6. Hand the resulting starter heads to `C.32.ACS`; do not optimize or measure inside HCS.

Choose with four distinct considerations: the common characterization method, the bearer kind, the domain or practice, and the concrete use and interests. These considerations intersect. A software-development Method and an instructional Method share a bearer kind but serve different work; a biological system and Work performed in the same project share a domain but have different bearers. Neither domain membership nor a shared quality name supplies the missing structure, value meaning or observation.

#### C.32.HCS:4.2 - Built-in starter packs

| Architecture-bearing family or recovered source label | Structures and related values to inspect | Starter heads to inspect first | Likely C.25 boundary |
|---|---|---|---|
| Engineered system, product family, or built asset | module, component, placement, deployment, maintenance access, control, information, evidence, manufacture, operation | reliability, availability, maintainability, safety, latency, locality, access, substitutability, evidence reuse, source-return cost, scale amenability | availability, safety, maintainability, resilience, security |
| Method admitted by A.3.1, including a source "practice" when recovery establishes that bearer | Method parts and their input/result, ordering, guard, feedback, refinement and substitution relations; C.30.ASV:4.5a distinguishes these from description, performer and Work structures | repeatability under stated conditions, transferability, exception growth, evidence reuse, change reach and enactment burden; first ask which relation changes the attainable work result | teachability, review quality, reliability of enactment |
| Work occurrence admitted by A.15.1, or a family of such occurrences | actual constituent performances, their obtaining connections, time and resource conditions, required contributions and observed results; keep a WorkPlan and the reusable Method separate | completion of needed contributions, coordination delay, recovery or rework, resource burden and result adequacy; first ask what happened in the occurrence and which structural difference could matter for a later one | delivery reliability, cost of useful completion, robustness of coordinated performance |
| Role-word, team, organization, or changing-holon case after the applicable recovery | Use `E.10.ROLE` only for unresolved claim-bearing *role* wording; A.2/C.3 and A.2.7 only for a local system-role kind, a separate System-classification judgment, or a relation among kinds; A.2.1 only for an assignment species or occurrence; A.14 only when a changing-holon question is current. Otherwise use the direct relation, architecture, organization, representation, function, responsibility, availability, staffing, Work-coverage, or ordinary non-use route actually recovered. | Carry only the exact or explicitly provisional head into ACS: for example coordination load, independent change, testability, deployability, control separation, decision latency, evidence custody, kind substitutability, assignment continuity, holder replacement, staffing, Work coverage, availability, or responsibility. Infer no branch from another. | team performance, organizational effectiveness, reliability of service delivery |
| Discipline or cultural-evolution case after C.20/C.36 recovery | discipline holon, collective systems, method and work families, local system-role kinds and assignments, canon or memory epistemes, publication structures, review records, evidence relations, succession of systems in assignments, recognition and selection regimes | norm transfer, correction latency, coherence of enacted methods and work, evidence reuse, learning reach, variant containment, source-return cost, continuity of needed contributions | cultural quality, discipline health, trustworthiness |
| AI-agent setup, model-supported workflow, or information system | model boundary, tool boundary, retrieval service, supervisor relation, evidence refresh relation, deployment placement, action interface | function-bearer fit, observability, evidence refresh, policy controllability, latency, resource load, interface grammar burden, rollback, benchmark transfer risk | safety, trustworthiness, robustness, usefulness |
| Evidence-bearing assurance or certification work arrangement after A.10/A.15 recovery | evidence packages, claim scopes, audit trails, inspection work, certification mechanisms, evidence-provenance entries, source-currentness relation records, method descriptions, system-role assignments, direct responsibility relations | evidence reuse, traceability, source-return cost, inspection latency, certification burden, scope stability, mechanism visibility, change reach | assurance-case quality, certification-work quality, compliance-work quality |

In HCS, `source-return cost` is a starter head for a holon family only when repeated source return incurs effort, latency, or risk. The return is from a derivative, coarsened, extracted, rendered, or reused publication or evidence carrier back to the named source expression, selected source `U.Episteme`, `EpistemePublicationRelation` occurrence when availability matters, source-bearing relation, evidence-provenance entry, evidence relation, transform record, or defining ClaimGraph needed for stronger reliance. It is not a generic source-quality name. If the project is only asking whether a catalogue term is useful, keep the wording as source catalogue wording; if recoverability itself is the concern, carry `source-return cost` to `C.32.ACS` and bind its bearer, scale, and use.

#### C.32.HCS:4.3 - Rebinding rule

When a starter head is reused at another bearer kind, holon level, domain, or concrete use, rebind it. Identify the target bearer, relevant relations and receiving result. State what is known about the conditions, quality meaning and attainable observation; carry unanswered binding questions to ACS. State which part of the source construction survives and which part needs replacement. The reusable item is a candidate head, not an already valid project row.

Example: `availability` for an engineered service may use time-window and service-scope measures. A method-side case may ask whether an exact System can access a Method description and evidence relation in the working situation. A kind case may ask whether A.2.7 admits substitution; an assignment case may ask whether holder replacement or assignment continuity obtains; a responsibility case needs its own direct relation. These are different bearers, predicates, and scales.

Refresh the starter pack when its starting assumptions no longer hold: the admitted holon family changes, source-label recovery changes the recovered family or bearer, a B.2 whole reidentification changes the bearer or scale, a source catalogue changes the available vocabulary, repeated ACS project-row uses show that a head never survives project binding, or repeated ACS project-row uses reveal a missing head for that family. Revise the affected guidance and any action-changing caution. Existing project criteria rows remain with `C.32.ACS`; measurements remain with `C.16`; eval programs remain with `C.32.ACE`.

#### C.32.HCS:4.4 - ACS Criteria-Row Use

HCS stops with starter heads and first project questions. The next `C.32.ACS` use governs:

- whether C.32.ACS admits the head as a draft project criteria row;
- whether it is one characteristic or a C.25 Q-Bundle;
- whether the project uses it as an optimization indicator, monitored guardrail, or context-only row;
- which scale, reading, and pattern for the next question apply.

Before ACS criteria-row use, ask whether improving a visible catalogue, benchmark or dashboard value could hide a loss in the actual architecture concern. Retain a plausible action-changing risk; do not invent one to qualify the head. Carry a head when the architecture-bearing family, likely bearer, concern and first project question are recoverable. A likely scale or composite-quality boundary can remain an explicit question for ACS or C.25. Preserve the source item and relevant source-to-use connection for a borrowed head, or the inspection basis for a directly recovered one. Name formal source identity or publication availability when the receiving use depends on it. If no architecture concern can be recovered, keep the term as source vocabulary or remove it from the starter set.

**Stop condition.** Stop C.32.HCS when the family, plausible starter heads, likely bearers or selected structures, and first ACS questions are recoverable. Carry a suspected composite boundary or unresolved scale as a question for C.25 or ACS, and retain a caution only when it changes use. The next project criteria-row work belongs to `C.32.ACS`.

**Lowering condition.** Keep a term as source vocabulary, or remove it from this starter set, when its architecture-bearing family, likely bearer, concern or first project question cannot be recovered. Repeated rejection during ACS binding can justify narrowing or revising the family guidance; inspect why the head failed before excluding another use. An unresolved scale or composite boundary is a question to resolve before stronger reliance, not evidence that the head is irrelevant. Use C.25 for composite quality and ACS for project binding; measurement, evaluation, comparison and decisions retain their own conditions.

