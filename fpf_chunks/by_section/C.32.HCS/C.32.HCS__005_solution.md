---
chunk_kind: "child"
pattern_id: "C.32.HCS"
pattern_title: "Holon-Family Architecture Characteristic Starter Packs"
section_id: "C.32.HCS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.HCS/C.32.HCS__005_solution.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.32.HCS — Holon-Family Architecture Characteristic Starter Packs"
  - "C.32.HCS:4 — Solution"
line_start: 59810
line_end: 59858
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
  - "characteristic transfer"
  - "first criteria questions"
  - "holon-family architecture characteristic starter pack"
  - "source catalogue narrowing"
---

### C.32.HCS:4 - Solution

Choose a starter pack by the described holon's declared family. Use the pack only to start narrowing starter heads into project criteria rows; then hand the result to `C.32.ACS` for the project criteria set.

#### C.32.HCS:4.1 - Starter pack construction

Build or use a starter pack in this order:

1. Name the holon family and the selected structures usually involved in architecture synthesis for that family.
2. List a small set of starter characteristic heads that often matter for that family.
3. For each head, name likely bearers or selected structures, not only a quality word.
4. Record likely C.25 Q-Bundle boundaries when a head is usually composite.
5. State a first project question that helps the practitioner decide whether the head belongs as a draft row in the project criteria set.
6. Hand the resulting starter heads to `C.32.ACS`; do not optimize or measure inside HCS.

#### C.32.HCS:4.2 - Built-in starter packs

| Holon family | Typical selected structures | Starter heads to inspect first | Likely C.25 boundary |
|---|---|---|---|
| Engineered system, product family, or built asset | module, component, placement, deployment, maintenance access, control, information, evidence, manufacture, operation | reliability, availability, maintainability, safety, latency, locality, access, substitutability, evidence reuse, source-return cost, scale amenability | availability, safety, maintainability, resilience, security |
| Method family or practice | method steps, work products, roles, evidence records, teaching sequence, review structure, exception-handling structure | repeatability, teachability, transferability, reviewability, exception growth, evidence reuse, change reach, work burden, role substitutability | teachability, review quality, reliability of method enactment |
| Role, team, organization, or changing holon | role boundaries, communication relations, work responsibility, toolchain, deployment responsibility, evidence responsibility | coordination load, accountability clarity, independent change, testability, deployability, control separation, decision latency, evidence custody, substitutability | team performance, organizational effectiveness, reliability of service delivery |
| Culture, discipline, or episteme-bearing holon | norms, exemplars, teaching sequences, publication structures, review practices, evidence relations, role succession | norm transfer, correction latency, practice coherence, evidence reuse, learning reach, variant containment, source-return cost, role continuity | cultural quality, discipline health, trustworthiness |
| AI-agent setup, model-supported workflow, or information system | model boundary, tool boundary, retrieval service, supervisor relation, evidence refresh relation, deployment placement, action interface | function-bearer fit, observability, evidence refresh, policy controllability, latency, resource load, interface grammar burden, rollback, benchmark transfer risk | safety, trustworthiness, robustness, usefulness |
| Evidence-bearing assurance or certification practice | evidence packages, claim scopes, audit trails, inspection work, certification mechanisms, source records | evidence reuse, traceability, source-return cost, inspection latency, certification burden, scope stability, mechanism visibility, change reach | assurance-case quality, certification-practice quality, compliance-practice quality |

#### C.32.HCS:4.3 - Rebinding rule

When a starter head is reused at another declared holon level, rebind it. The reusable item is the head, not the row.

Example: `availability` for an engineered service may use time-window and service-scope measures. A method-family analogue may concern whether a method step and evidence relation are available to a role in the work situation. A role-family analogue may concern substitutable responsibility coverage. These are different bearers and scales.

Refresh the starter pack when its starting assumptions no longer hold: the described holon family changes, a B.2 whole reidentification changes the bearer or scale, a source catalogue changes the available vocabulary, repeated ACS project-row uses show that a head never survives project binding, or repeated ACS project-row uses reveal a missing head for that family. Refresh only starter-pack fields and blocked overreads. Existing project criteria rows remain with `C.32.ACS`; measurements remain with `C.16`; eval programs remain with `C.32.ACE`.

#### C.32.HCS:4.4 - ACS Criteria-Row Use

HCS stops with starter heads and first project questions. The next `C.32.ACS` use governs:

- whether C.32.ACS admits the head as a draft project criteria row;
- whether it is one characteristic or a C.25 Q-Bundle;
- whether the project uses it as an optimization indicator, monitored guardrail, or context-only row;
- which scale, reading, and receiving pattern apply.

Before ACS criteria-row use, ask one proxy-resistance question for each carried starter head: what architecture concern would worsen or disappear if the visible source cue looked better? A richer catalogue, familiar software term, higher benchmark, or cleaner dashboard is only a source signal. Carry it forward only when the holon family, likely bearer, likely scale, Q-Bundle boundary, and first project question are recoverable. If no worsening or lost concern can be named, keep the item as source vocabulary or remove it from the starter pack.

**Stop condition.** Stop C.32.HCS when the starter pack names the described holon family, starter heads, likely bearers or selected structures, likely composite-quality boundaries, first ACS questions, and any blocked overread. The next project criteria-row work belongs to `C.32.ACS`.

**Lowering condition.** Lower a starter head to source vocabulary or remove it from the starter pack when the holon family is not declared, the likely bearer or likely scale is missing, the composite-quality boundary is still unresolved, the first ACS question is absent, repeated ACS uses reject the head for that holon family, or the item is being used to smuggle measurement, eval, comparison, publication, local choice, or decision work into HCS. Use `C.25` when the head is composite, `C.32.ACS` when the project criteria-row question is ready, and the named receiving pattern when the stronger claim is current.

