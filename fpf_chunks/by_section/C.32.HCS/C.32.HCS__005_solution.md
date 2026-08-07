---
chunk_kind: "child"
pattern_id: "C.32.HCS"
pattern_title: "Architecture-Bearing Family Characteristic Starter Packs"
section_id: "C.32.HCS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.HCS/C.32.HCS__005_solution.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.32.HCS — Architecture-Bearing Family Characteristic Starter Packs"
  - "C.32.HCS:4 — Solution"
line_start: 65021
line_end: 65071
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
  - "E.13"
  - "G.5"
keywords:
  - "architecture characteristic heads"
  - "architecture-bearing family characteristic starter pack"
  - "characteristic transfer"
  - "first criteria questions"
  - "source catalogue narrowing"
---

### C.32.HCS:4 - Solution

Choose a starter pack by the described holon's declared family. Use the pack only to start narrowing starter heads into project criteria rows; then hand the result to `C.32.ACS` for the project criteria set.

#### C.32.HCS:4.1 - Starter pack construction

Build or use a starter pack in this order:

1. Name the admitted holon family. If the source label is method, role, practice, culture, tradition, style, or evidence practice, first name the described holon, or name the source-bearing episteme or publication context when the label is only a description-side family, and record only the recovery-pattern references actually used.
2. List a small set of starter characteristic heads that often matter for that family.
3. For each head, name likely bearers or selected structures, not only a quality word.
4. Record likely C.25 Q-Bundle boundaries when a head is usually composite.
5. State a first project question that helps the practitioner decide whether the head belongs as a draft row in the project criteria set.
6. Hand the resulting starter heads to `C.32.ACS`; do not optimize or measure inside HCS.

#### C.32.HCS:4.2 - Built-in starter packs

| Architecture-bearing family or recovered source label | Typical selected structures | Starter heads to inspect first | Likely C.25 boundary |
|---|---|---|---|
| Engineered system, product family, or built asset | module, component, placement, deployment, maintenance access, control, information, evidence, manufacture, operation | reliability, availability, maintainability, safety, latency, locality, access, substitutability, evidence reuse, source-return cost, scale amenability | availability, safety, maintainability, resilience, security |
| Method-side family or source "practice" after A.3.1/A.15 recovery | method relation structure, method descriptions, work-product structures, role-assignment requirements, evidence records, teaching or work-instruction sequence, review structure, exception-handling structure | repeatability of enactment, teachability, transferability, reviewability, exception growth, evidence reuse, change reach, work burden, role-assignment substitutability | teachability, review quality, reliability of method enactment |
| Role-side, team, organization, or changing-holon context after A.2.7/A.14 recovery | role assignments, role relation structures, systems holding roles, communication relations, work-responsibility allocation, toolchain, deployment responsibility, evidence custody | coordination load, accountability clarity for role-holding systems, independent change, testability, deployability, control separation, decision latency, evidence custody, role-assignment substitutability | team performance, organizational effectiveness, reliability of service delivery |
| Discipline or cultural-evolution case after C.20/C.36 recovery | discipline holon, collective systems, method and work families, role assignments, canon or memory epistemes, publication structures, review records, evidence relations, role succession, recognition and selection regimes | norm transfer, correction latency, coherence of enacted methods and work, evidence reuse, learning reach, variant containment, source-return cost, role continuity | cultural quality, discipline health, trustworthiness |
| AI-agent setup, model-supported workflow, or information system | model boundary, tool boundary, retrieval service, supervisor relation, evidence refresh relation, deployment placement, action interface | function-bearer fit, observability, evidence refresh, policy controllability, latency, resource load, interface grammar burden, rollback, benchmark transfer risk | safety, trustworthiness, robustness, usefulness |
| Evidence-bearing assurance or certification work arrangement after A.10/A.15 recovery | evidence packages, claim scopes, audit trails, inspection work, certification mechanisms, evidence-provenance entries, source-currentness relation records, method descriptions, responsible role assignments | evidence reuse, traceability, source-return cost, inspection latency, certification burden, scope stability, mechanism visibility, change reach | assurance-case quality, certification-work quality, compliance-work quality |

In HCS, `source-return cost` is a starter head only when a holon family repeatedly pays effort, latency, or risk to move from a derivative, coarsened, extracted, rendered, or reused publication or evidence carrier back to the named source expression, selected source `U.Episteme`, `EpistemePublicationRelation` occurrence when availability matters, source-bearing relation, evidence-provenance entry, evidence relation, transform record, or defining ClaimGraph needed for stronger reliance. It is not a generic source-quality name. If the project is only asking whether a catalogue term is useful, keep the wording as source catalogue wording; if recoverability itself is the concern, carry `source-return cost` to `C.32.ACS` and bind its bearer, scale, and use.

#### C.32.HCS:4.3 - Rebinding rule

When a starter head is reused at another admitted holon family, declared holon level, or recovered architecture-bearing family, rebind it. The reusable item is the head, not the row.

Example: `availability` for an engineered service may use time-window and service-scope measures. A method-family analogue may concern whether a method step and evidence relation are available to a role in the work situation. A role-family analogue may concern substitutable responsibility coverage. These are different bearers and scales.

Refresh the starter pack when its starting assumptions no longer hold: the admitted holon family changes, source-label recovery changes the recovered family or bearer, a B.2 whole reidentification changes the bearer or scale, a source catalogue changes the available vocabulary, repeated ACS project-row uses show that a head never survives project binding, or repeated ACS project-row uses reveal a missing head for that family. Refresh only starter-pack fields and blocked overreads. Existing project criteria rows remain with `C.32.ACS`; measurements remain with `C.16`; eval programs remain with `C.32.ACE`.

#### C.32.HCS:4.4 - ACS Criteria-Row Use

HCS stops with starter heads and first project questions. The next `C.32.ACS` use governs:

- whether C.32.ACS admits the head as a draft project criteria row;
- whether it is one characteristic or a C.25 Q-Bundle;
- whether the project uses it as an optimization indicator, monitored guardrail, or context-only row;
- which scale, reading, and pattern for the next question apply.

Before ACS criteria-row use, ask one proxy-resistance question for each carried starter head: what architecture concern would worsen or disappear if the visible catalogue entry, domain term, benchmark row, or dashboard value looked better? Such visible material is not yet an architecture-characteristic starter head. Carry it forward only when the holon family, likely bearer, likely scale, Q-Bundle boundary, first project question, source catalogue entry, benchmark row, dashboard row, or publication row, source-to-use path, and reopen condition remain recoverable. Also name the selected source `U.Episteme` and an `EpistemePublicationRelation` occurrence when availability matters. If no worsening or lost concern can be named, keep the wording as source catalogue wording or remove it from the starter pack.

**Stop condition.** Stop C.32.HCS when the starter pack names the described holon family, starter heads, likely bearers or selected structures, likely composite-quality boundaries, first ACS questions, and any blocked overread. The next project criteria-row work belongs to `C.32.ACS`.

**Lowering condition.** Lower a starter head to source catalogue wording or remove it from the starter pack when the holon family is not declared, the likely bearer or likely scale is missing, the composite-quality boundary is still unresolved, the first ACS question is absent, repeated ACS uses reject the head for that holon family, or the item is being used to smuggle measurement, eval, comparison, publication, local choice, or decision work into HCS. Use `C.25` when the head is composite, `C.32.ACS` when the project criteria-row question is ready, and the named pattern for the next question when the stronger claim is current.

