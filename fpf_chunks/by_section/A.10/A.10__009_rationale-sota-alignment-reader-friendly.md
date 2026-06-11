---
chunk_kind: "child"
pattern_id: "A.10"
pattern_title: "Evidence Graph Referring (C‑4)"
section_id: "A.10:8"
section_title: "Rationale (SoTA alignment, reader‑friendly)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10/A.10__009_rationale-sota-alignment-reader-friendly.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.10 — Evidence Graph Referring (C‑4)"
  - "A.10:8 — Rationale (SoTA alignment, reader‑friendly)"
line_start: 18832
line_end: 18842
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

### A.10:8 - Rationale (SoTA alignment, reader‑friendly)

* **Metrology & assurance.** The requirement to name quantities, units, uncertainty, calibration carriers reflects long‑standing metrology practice and modern assurance cases: numbers are only comparable when their **measurement models** are stated.
* **Knowledge provenance.** The EPV‑DAG and SCR/RSCR embody post‑2015 best practices in provenance for epistemes and their carriers: keep a complete, machine‑checkable trail from claims to carriers; separate provenance from part‑whole.
* **Temporal reasoning.** Monotone coverage (no unexplained gaps/overlaps) aligns with temporal knowledge graph practice and avoids “impossible histories.”
* **Holonic parsimony.** By drawing a firewall between **mereology** (A.14) and **provenance**, A.10 prevents semantic leakage and keeps the holarchy well‑typed.
* **Role–Method–Work clarity.** Evidence relationing explicitly rides on A.15: **roles** act via **methods** specified at design‑time and produce **work** observed at run‑time. This keeps agency, policy, and execution disentangled yet connected.
* **Credential, provenance, attestation, status-register, and generated-source currentness.** Verifiable-credential and digital-identity practice separates issuer or trust root, holder binding, proof result, status result, revocation, validity window, audience, and relying context. Some bounded contexts also treat a register entry or status-source entry as the source that creates or changes role assignment, status assertion, permission, duty, or gate state; a credential view, pass, badge, dashboard cell, API response, screenshot, or certificate excerpt is then a publication of that source, not automatically the source itself. C2PA content provenance plus SLSA and in-toto attestations separate bounded origin, history, build, and process claims from truth, approval, release, safety, gate passage, permission, or assurance; their consumer-side verifier or policy acceptance rule is part of the relying context, not implied by source-carrier presence. LLM citation and generated-explanation practice requires claim-bound attribution alignment before operative claims are relied on. A.10 adopts issuer, holder, verifier, status, and currentness recoverability, status-source recoverability, and claim-bound attribution as evidence-path invariants, adapts credential practice, provenance practice, attestation practice, model documentation, data documentation, register-backed status display, and generated-explanation practice as FPF source-role and carrier-relation inputs, and rejects visual display, copied text, generated text, provenance mark, credential display, register excerpt, or attestation form as evidence of an operative action invitation, gate, role assignment, status assertion, work-occurrence, assurance, or admissible-work effect without source relation named by value.

Action result from that cited practice basis: provenance, attestation, credential, status-register, and generated-source practice rejects the shortcut that provenance means truth, safety, release, permission, or assurance. The local A.10 result is bounded origin, history, build, holder or status currentness, generated-claim source mapping, admissible use, non-admissible use, and reopen when the verifier, trust model, status or currentness rule, source mapping, or source-order relation changes.

