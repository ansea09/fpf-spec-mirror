---
chunk_kind: "child"
pattern_id: "A.2.4"
pattern_title: "Episteme Evidence-Use and Status-Use Relations"
section_id: "A.2.4:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.4/A.2.4__012_sota-echoing.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.2.4 — Episteme Evidence-Use and Status-Use Relations"
  - "A.2.4:10.1 — SoTA-Echoing"
line_start: 3677
line_end: 3687
dependencies:
  - "A.10"
  - "A.2"
  - "A.2.1"
  - "A.2.4"
  - "A.6.5"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "F.10"
  - "G.6"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "claim"
  - "episteme"
  - "evidence-use"
  - "provenance"
  - "source-use"
  - "status-use"
---

### A.2.4:10.1 - SoTA-Echoing

| SoTA line | Adopted or adapted move | FPF consequence |
| --- | --- | --- |
| Current digital provenance, content-credential, verifiable-credential, and attestation practice, including C2PA 2.4, W3C Verifiable Credentials 2.0, SLSA Provenance 1.2, and in-toto Statement v1. | Adopt the separation of subject, issuer or producing work, proof or status check, time, verifier or relying context, and claim. Adapt it to FPF `U.Episteme`, `U.Work`, role-assignment, source-currentness, and publication-use distinctions. | A.2.4 uses evidence-use and status-use relation slots instead of an episteme role assignment; credential or provenance display does not become truth, permission, gate passage, or assurance by itself. |
| Assurance-case and trust-calculus practice separates evidence presence from assurance, safety, readiness, compliance, and release confidence. | Adopt the separation between evidence-use and assurance-use. | A.2.4 supplies relation positions; `B.3` computes or states assurance and names limits, scope, decay, and reopen conditions. |
| Current causal-inference, target-trial, counterfactual, and simulation-evaluation practice separates observational, interventional, realized-counterfactual, identified-estimate, and simulation-only evidence classes. | Adopt the separation of causal evidence classes; use exact value names from `C.28`. | Causal evidence-use wording cannot relabel simulation-only output as realized or interventional evidence. |
| Foundational-ontology and relation-slot practice, including gUFO, UFO, and OntoUML role, relator, situation, and high-order type work, separates role-assignment holders, relation positions, status assertions, and object use. | Adopt the anti-collapse principle: a value may fill a relation position without becoming a new kind or role-assignment holder. | `U.RoleAssignment` stays work-facing, while episteme evidence, status, source, publication, requirement, definition, explanation, and assurance uses stay in direct relations. |

Refresh this pattern's source use when those provenance, credential, attestation, assurance, causal-use, or foundational-ontology practices change the separation between evidence presence, status display, assurance, provenance, causal class, and role assignment.

