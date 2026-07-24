---
chunk_kind: "child"
pattern_id: "G.6"
pattern_title: "Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
section_id: "G.6:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/G.6/G.6__008_conformance-checklist.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "G.6 — Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths"
  - "G.6:7 — Conformance Checklist"
line_start: 97384
line_end: 97398
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

### G.6:7 - Conformance Checklist

| ID | Check | Repair if missing |
| --- | --- | --- |
| `CC-G6-01` Primary EoC | Is the current evidence-provenance concern an `EvidenceGraph`, `PathId`, `PathSliceId`, or provenance ledger entry, with any role, work, or assurance claim kept under its own governing pattern? | Return to `A.2.4`, `A.10`, `B.3`, `C.28`, `F.10`, `A.15.1`, or `E.17` as appropriate. |
| `CC-G6-02` Graph path identity | Does each `PathId` resolve to a graph path in a named `EvidenceGraph`? | Mint or repair `EvidenceGraphRef`, node refs, edge refs, and path addressing rule. |
| `CC-G6-03` Node typing | Are node kinds explicit and governed by neighboring patterns? | Replace role-shaped or label-shaped nodes with evidence-use, status-use, source, work, method-description, carrier, or causal-use refs. |
| `CC-G6-04` Edge typing | Are provenance edges typed and minimal? | Replace narrative "because" text with verified, validated, produced-by-work, uses-method-description, source, bridge, time, status, or causal-use edges. |
| `CC-G6-05` Context and time | Are bounded context, reference plane, time window, freshness, currentness, edition, or policy refs stated when they decide use? | Add the missing refs or lower the path to source-finding or local evidence orientation. |
| `CC-G6-06` Bridge visibility | Are cross-context, cross-plane, cross-edition, or source-order crossings explicit? | Add bridge, loss, currentness, or source-order refs; otherwise block downstream reuse. |
| `CC-G6-07` Not carried | Does the path say what stronger downstream use it does not carry? | Add `NotCarried` for the stronger use and cite the governing pattern. |
| `CC-G6-08` Downstream use | Is the downstream citation use named? | Name selector, assurance, benchmark, release, maturity, refresh, audit, or local claim use, or stay in `A.10`. |
| `CC-G6-09` Refresh locality | Does a changed source, bridge, policy, edition, status, causal-use, or time relation reopen the smallest path slice? | Add `PathSliceId` and reopen trigger; avoid broad rerun language. |
| `CC-G6-10` No process leakage | Is the provenance ledger free of work-progress notes, review comments, release proof, or quality proof? | Move process evidence to the current process carrier; keep G.6 to evidence-provenance facts. |

