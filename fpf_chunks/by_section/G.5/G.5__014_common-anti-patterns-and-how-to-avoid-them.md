---
chunk_kind: "child"
pattern_id: "G.5"
pattern_title: "Multi‑Method Dispatcher & MethodFamily Registry"
section_id: "G.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.5/G.5__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "G.5 — Multi‑Method Dispatcher & MethodFamily Registry"
  - "G.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 79271
line_end: 79300
dependencies:
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.23"
  - "C.24"
  - "G.0"
  - "G.2"
  - "G.2-G.4"
  - "G.5"
  - "G.6"
  - "G.9-G.11"
  - "G.Core"
keywords:
  - "RankedShortlist"
  - "SelectorOutcomeKind"
  - "Shortlist"
  - "ShortlistId"
  - "SpecialistHandoff"
  - "abstain/escalation result"
  - "are forbidden in registry"
  - "assurance"
  - "basis pins"
  - "dispatcher"
  - "eligibility"
  - "generator-family registry"
  - "in core registry/eligibility fields"
  - "method-family registry"
  - "no hidden scalar winner"
  - "or selector‑kernel obligations (E.5.*)"
  - "selected-set publication"
  - "set-result outcome"
  - "tool choices are outside the core"
---

### G.5:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern: “Selector as a shadow spec.”**
  *Symptom:* local acceptance/legality rules appear in selector prose/code, diverging from CN/CG/CAL.
  *Avoid:* route all constraint semantics via `CNSpecRef/CGSpecRef` and pinned CAL records; keep G.5 core as a facade.

* **Anti‑pattern: “Implicit crossings.”**
  *Symptom:* cross‑Context reuse is claimed without Bridge/CL pins, or without cited `CrossingBundle`.
  *Avoid:* require explicit crossing pins; block consumption without publication.

* **Anti‑pattern: “Hidden scalarisation.”**
  *Symptom:* partial orders are flattened into single winners “for convenience”.
  *Avoid:* return declared sets; make dominance regimes explicit; keep telemetry report‑only unless promoted by explicit policy.

* **Anti‑pattern: “Method specifics in the selector head.”**
  *Symptom:* QD/OEE/preference models become mandatory for basic dispatch.
  *Avoid:* keep them in `G.5:Ext.*` blocks with explicit pins and `Uses`.

* **Anti‑pattern: “Churn by meaning.”**
  *Symptom:* registry entries are “renamed” to reflect updated interpretation, breaking continuity.
  *Avoid:* version/deprecate; keep stable ids; use explicit edition pins and deprecation notices.

* **Anti‑pattern: “Publication hidden in upstream reasoning.”**
  *Symptom:* the retained set exists only as one implication inside `C.11`, `C.19`, or `C.24`, while `G.5` never names the published selected-set label.
  *Avoid:* publish the selected-set result directly, with explicit label, members, and basis pins, instead of leaving the shortlist implicit in neighboring doctrine.

* **Anti‑pattern: “Published result without closure record.”**
  *Symptom:* a `Shortlist`, narrowed handoff, or abstain result is named, but the emitted result still does not state its members, ordering status, or basis pins.
  *Avoid:* publish the head, retained members, ordering status, abstain or escalation condition, and basis pins directly in `G.5`.

