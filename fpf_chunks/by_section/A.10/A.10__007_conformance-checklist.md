---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring (C‑4)"
section_id: "A.10:6"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__007_conformance-checklist.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.10 — Evidence Graph Referring (C‑4)"
  - "A.10:6 — Conformance Checklist"
line_start: 18714
line_end: 18735
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.2.8"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.4"
  - "C.16"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "E.17.EFP"
  - "F.9"
keywords:
  - "SCR/RSCR"
  - "authority-reliance evidence path"
  - "claim support"
  - "evidence"
  - "evidence carrier"
  - "exact authority reference"
  - "generated-explanation source support"
  - "probe/distributed/export/causal evidence"
  - "provenance"
  - "register excerpt"
  - "status register"
  - "traceability"
---

### A.10:6 - Conformance Checklist

| ID                                      | Requirement                                                                                                                                                                                                                             | Purpose (what it prevents)                                 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **CC‑A10.1 (EPV‑DAG Presence)**         | Every published claim MUST have a path in the Evidence–Provenance DAG (EPV‑DAG) to concrete **SymbolCarrier** nodes and to the **external** `TransformerRole` that produced or interpreted the evidence.                                | Stops “weightless claims” and self‑justifying text.        |
| **CC‑A10.2 (SCR)**                      | Any `Γ_epist^synth` operation SHALL output an **SCR** listing all symbol carriers substantively used in the aggregate `s.Episteme`.                                                                                                        | Prevents source loss during aggregation.                   |
| **CC‑A10.3 (RSCR)**                     | Any `Γ_epist^compile` operation SHALL output an **RSCR** adapted to the target bounded context (vocabularies, units) with publication‑grade identifiers/hashes; SCR→RSCR MUST preserve carrier identity/integrity.                      | Keeps releases auditable and context‑consistent.           |
| **CC‑A10.4 (Resolution)**               | Every provenance/evidence node in the dependency graph MUST be resolvable to an SCR/RSCR entry. Unresolved links invalidate the claim.                                                                                                  | Eliminates dangling references and unverifiable citations. |
| **CC‑A10.5 (Scope Separation)**         | A single EPV‑DAG instance SHALL NOT mix design‑time MethodDescription nodes with run‑time Work traces. Bridges (“this run trace instantiates that spec”) MUST be explicit.                                                                     | Avoids conflating intent and execution.                    |
| **CC‑A10.6 (Externality)**              | The evidencing `TransformerRole` MUST be **external** to the holon under evaluation (A.12). Reflexive cases require modelling a meta‑holon and an external mirror.                                                                      | Prevents self‑creation/self‑evidence paradoxes.            |
| **CC‑A10.7 (Temporal Coverage)**        | For `Γ\_time` claims, interval coverage MUST be monotone and fully specified; gaps/overlaps require explicit justification or rejection.                                                                                                 | Stops invalid time‑series aggregation.                     |
| **CC‑A10.8 (Integrity & Immutability)** | SCR/RSCR entries MUST include version/date and checksums; published SCR/RSCR are immutable—updates create a new revision id with a pointer to the prior one.                                                                            | Guards against silent drift and tampering.                 |
| **CC‑A10.9 (Holarchy Firewall)**        | EPV‑DAG MUST use provenance edges only; mereological edges (`ComponentOf`, `MemberOf`, `PortionOf`, `PhaseOf`, etc.) MUST NOT appear in EPV‑DAG; conversely, provenance edges MUST NOT be used to build holarchies.                     | Keeps part‑whole and evidence semantics disjoint.          |
| **CC‑A10.10 (Γ\_sys Anchors)**          | Physical claims aggregated by `Γ_sys` MUST reference measurement models (quantity, unit, uncertainty), boundary conditions, and calibration carriers.                                                                                   | Ensures physical plausibility and comparability.           |
| **CC‑A10.11 (Γ\_method Anchors)**       | For order‑sensitive composition, design‑time MUST include a **Method Instantiation Card (MIC)** (Precedes/Choice/Join, guards, exceptions); run‑time traces MUST record `happenedBefore` and reference the MethodDescription they instantiate. | Preserves order semantics and reproducibility.             |
| **CC‑A10.12 (Γ\_work Anchors)**         | Resource spending/yield claims MUST be evidenced by instrumented carriers (meters, logs) and their MethodDescriptions; resource **rosters** MUST NOT be conflated with SCR/RSCR.                                                               | Distinguishes cost accounting from knowledge carriers.     |
| **CC-A10.13 (Causal support-basis path)** | If an evidence path supports a causal-use claim, it **MUST** carry `CausalEvidenceSupportBasis` from `C.28` and any relevant `CausalIdentificationProfile`, `CounterfactualSamplingRealizabilityProfile`, or `CausalUseEvidenceDesignRecord` refs; A.10 **MUST NOT** identify causal effects or mint a second support-basis value set. | Keeps evidence graph support recoverable without moving causal authority out of `C.28`. |
| **CC-A10.14 (Authority-reliance use of ordinary evidence paths)** | When a carrier is used to support approval, permission, gate passage, role or status currentness, work occurrence, provenance, authenticity, copied source support, generated source support, assurance input, or another authority-reliance claim or effect, the evidence path SHALL name the supported claim or effect, carrier, issuer, performer, source-maintenance role assignment or trust anchor, affected work target or claim target and relying context, time window, freshness or revocation stance, evidence-producing work event or method trace, evidence relation, and most relevant rival explanation. Expanded fields SHALL be named only when they decide the live reliance question: method trace or work trace, carrier integrity, identity or holder binding, verifier context, relying-party context, acceptance rule, proof result, cryptographic-signature result, status verification result, policy or gate version, decision source, source-chain transform notes, source order, supersession rule, and minimum disclosure posture. | Prevents badges, dashboards, copied text, generated explanations, credentials, provenance labels, and composed chains from supplying false evidence support, without turning source-finding into a full dossier. |
| **CC-A10.15 (Evidence-kind and reliance disposition)** | When a support-looking source is used for reliance, A.10 SHALL recover the evidence kind before stating support posture, then state the local `RelianceDisposition`, supported use, unsupported use, currentness/window, contest or redress path when live, and reopen trigger. `RelianceDisposition` SHALL NOT be read as `CV.Status`, `GateDecision`, selector outcome, problem-card state, assurance approval, or release permission. | Keeps evidence support action-guiding while preventing confidence, conformance, provenance, score, dashboard, generated explanation, or redress wording from becoming hidden authority. |

**Practitioner’s audit (non‑normative, quick):** For any claim, ask **What carriers? Which system? Which method? When?** If any answer is missing, A.10 is not satisfied.

