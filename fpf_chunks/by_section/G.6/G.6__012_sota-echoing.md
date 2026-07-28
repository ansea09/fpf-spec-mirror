---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__012_sota-echoing.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:11 — SoTA-Echoing"
line_start: 98687
line_end: 98699
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.21"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.17.EFP"
  - "E.18"
  - "E.18.2"
  - "E.24"
  - "E.5.2"
  - "F.10"
  - "F.15"
  - "F.17"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
  - "G.Core"
keywords:
  - "CrossingBundle"
  - "EvidenceGraph"
  - "GateCrossing"
  - "PathId"
  - "PathSliceId"
  - "SCR/RSCR"
  - "TriggerAliasMap"
  - "UTS PathCard"
  - "lane tags (TA/VA/LA)"
  - "provenance"
  - "Γ-fold pinning"
---

### G.6:11 - SoTA-Echoing

| Source family | G.6 adoption | Practitioner implication |
| --- | --- | --- |
| Verifiable-credential, content-provenance, and supply-chain attestation practice | Keep subject, issuer or producer, verifier or relying context, proof or signature check, status/currentness relation, policy, time, and input evidence or attestation refs separate. A summary attestation may be useful only when the underlying path or input attestations remain recoverable. | A provenance credential, content credential, or verification summary can feed a `PathId`; stronger downstream uses still need their governing patterns. |
| Current provenance, attestation, credential, and content-authenticity practice | Separate subject, issuer or producer, proof check, status check, time window, verifier or relying context, and source-currentness relation. | A provenance mark or credential view may evidence bounded origin or status; stronger downstream uses are not created by display. |
| Reproducible research, data lineage, model-card, datasheet, and benchmark governance practice | Keep dataset, metric, method description, evaluation condition, version, limitation, and run evidence addressable. | A benchmark or model report can be replayed and refreshed by path slice instead of becoming a frozen story. |
| Assurance-case and safety-case practice | Keep evidence-provenance paths citable by assurance claims without letting evidence presence equal assurance. | `B.3` can consume a `PathId`, but still needs its own assurance tuple, limitations, decay, and reopen relation. |
| Temporal and source-currentness practice | Treat windows, expiry, supersession, and source-order changes as path-local reopen events. | Stale or contested evidence lowers or reopens the path; it does not silently continue to carry reliance. |
| Declarative graph and provenance-graph practice | Use graph paths for addressability and replay, while keeping work execution and transformation-flow structures separate. | A path can be checked without telling a worker to follow it as a route. |

Refresh the source use behind this pattern when current provenance, credential, attestation, benchmark, lineage, assurance-case, or source-currentness practice changes the separation between provenance presence, evidence use, assurance, status use, and role assignment.

