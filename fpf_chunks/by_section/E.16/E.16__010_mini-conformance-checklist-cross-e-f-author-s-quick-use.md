---
chunk_kind: "child"
pattern_id: "E.16"
pattern_title: "RoC‑Autonomy Budget & Enforcement"
section_id: "E.16:9"
section_title: "Mini conformance checklist (cross-E-F; author's quick use)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.16/E.16__010_mini-conformance-checklist-cross-e-f-author-s-quick-use.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "E.16 — RoC‑Autonomy Budget & Enforcement"
  - "E.16:9 — Mini conformance checklist (cross-E-F; author's quick use)"
line_start: 90890
line_end: 90900
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.24"
  - "C.9"
  - "E.10"
  - "E.18"
  - "E.8"
  - "F.15"
  - "F.17"
  - "F.4"
  - "F.6"
  - "F.8"
  - "G.10"
  - "G.4"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "autonomy budget"
  - "autonomy ledger"
  - "guarded enactment"
  - "override speech act"
  - "scout/probe/commit checkpoint"
---

### E.16:9 - Mini conformance checklist (cross-E-F; author's quick use)

1. **Declare the boundary:** name the autonomy claim, consumer local kind, working situation, policy, ClaimScope, window, budget, override-authority kind, and exact A.2.7 incompatibility relation.
2. **Identify the proposed action:** keep an unscheduled budget prospective; use action-bound for a scheduled action, its work-entry claim, real assignments/holders and independent authority. Apply the declared action identity and continuation rule.
3. **Gate permission to start:** apply the appropriate prospective allocation test, budget and guards to the bounded action. Recheck permission-relevant changes. A pass is not performed Work.
4. **Record actual Work:** after independent A.15.1 admission, emit the Work-anchored ledger entry, attribution and actual delta; relate it to prior permission through the exact policy-supported action match.
5. **Check override separately:** distinguish the existing target Work from the proposed override; apply the selected actual-Work or prospective-action species to the real assignments and applicable window, and independently test authority before performance.
6. **Publish what users need:** expose the budget edition, binding state, policy, override protocol, scope, and window in the UTS row.

These steps are the smallest complete route for a working Part F test harness; optional telemetry and selection lenses remain optional.

