---
chunk_kind: "child"
pattern_id: "E.20"
pattern_title: "Mechanism Introduction Protocol"
section_id: "E.20:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.20/E.20__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.20 — Mechanism Introduction Protocol"
  - "E.20:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 64082
line_end: 64094
dependencies:
  - "A.15.3"
  - "A.6.1"
  - "A.6.7"
  - "E.10"
  - "E.15"
  - "E.18"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.18"
  - "G.2"
  - "G.Core"
  - "G.x"
keywords:
  - "MIP-run manifest"
  - "P2W seam"
  - "PQG profiles"
  - "SlotKind lexicon discipline"
  - "alias docking"
  - "authoring protocol"
  - "canonical card-first"
  - "governing-definition assignment"
  - "mechanism introduction"
  - "no dangling …IntensionRef"
  - "regression envelope"
  - "suite boundary hygiene"
  - "typed RSCR triggers"
---

### E.20:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
|---|---|---|---|
| **Wiring carries semantics** | Part G extensions start redefining what a mechanism “means”. | Meaning becomes edition-fragile and non-local. | Move semantics back to the mechanism-governing pattern; keep extensions as binding only. |
| **Suite becomes a meta-mechanism** | Suite text defines ops/laws or embeds thresholds/decisions. | Collapses suite, mechanism, and gate kinds; creates hidden gate behavior. | Restore suite as description-only; push thresholds to acceptance/gate kind. |
| **Plan becomes enactment** | Plan items contain launch values, witnesses, or decisions. | Destroys P2W seam; breaks audit semantics. | Strip enactment content; pin only refs/policies/time selectors. |
| **Kernel churn by convenience** | New required stage is added directly to kernel suite membership. | Expands the E.15 impact radius; destabilizes citations. | Prefer suite variant; if not possible, pair with alias docking and explicit deltas. |

| **Token drift by silent rename** | “Just rename UNM to ...” without aliasing. | Breaks citations and downstream reasoning. | Use F.18 alias docking; update registers explicitly. |
| **MIP as gate surrogate** | A MIP-run manifest is treated as a runtime pass/fail result or gate passage. | Governing-definition assignment is being mistaken for project execution or gate decision. | Keep MIP as authoring-side governing-definition assignment; use `A.21` for gate decisions and `A.15` for work or enactment claims. |
| **Governing-definition ambiguity** | “We’ll put it somewhere later.” | Leaves incompleteness and drift invisible. | Name the governing definition up front; otherwise treat as non-normative. |

