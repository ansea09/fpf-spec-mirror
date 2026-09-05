---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:14"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__016_rationale-informative.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:14 — Rationale (informative)"
line_start: 40354
line_end: 40373
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:14 - Rationale (informative)

**14.1 Why canonical‑first?**
CT2R-LOG treats the **human-readable, task-appropriate relation** (e.g., `ut:ComponentOf`) as the **canonical publication form** because that is what engineers and managers actually use to reason, decide, and communicate. The formal layers **ground** that form; they do not replace it. This is consistent with the authoring Standard in Part E (pattern template and style guide), which privileges **clarity, purpose and didactics** over premature formalism in the body text. Authors write *for people first*, then point to the kind of assurance they are invoking.

**14.2 Why two `tv:` links—and why concept‑only?**
`tv:AliasOf` and `tv:groundedBy` name **conceptual bridges** from a public Working-Model relation to its direct principle and assurance account. They mandate no notation. They keep authors explicit about the relation reading, the support being invoked, and when that support must be current, without letting an alias, trace, or mode define the world-side occurrence.

**14.3 Why a triad of `validationMode`?**
The triad **{postulate, inferential, axiomatic}** expresses staged formality compatible with the FPF stance on staged assurance: start with what the team can responsibly claim now, then move to stricter justification where risk or context demands it. That gives reviewers a shared vocabulary for the declared assurance posture of a claim without changing the canonical relation itself.

**14.4 Why keep order/time out of mereology?**
CT2R‑LOG aligns with A.14’s **firewall**: structure (parthood) is distinct from **order** and **temporal coverage**. The former is published as `ut:StructPartOf` sub‑relations; the latter live in `Γ_method` / `Γ_time` and must **not** be smuggled into part‑trees. This separation avoids classic modelling failures (temporal smearing, pseudo‑components for quantities) and keeps reasoning crisp across the Γ‑family.

**14.5 Why point to `Γ_m.sum | set | slice` (Compose‑CAL) for constructive grounding?**
The three C.13 forms—**sum, set, slice**—are sufficient to report the recurring construction accounts for integrated assemblies, collections, and aspects without expanding the kernel. They are not identity functions. A truthful account carries exact participants, direct relation occurrences, the applicable rule, and identity or reidentification conditions: the same inputs under another assembly can form another whole, while a permitted replacement can preserve one whole.

**14.6 Why mental obligations rather than process mandates?**
Part E requires that patterns define or constrain **thinking** and **authoring**; enforcement and automation, if any, are external concerns. CT2R‑LOG therefore states obligations as **self‑contained cognitive checks**: declare your mode; tell the constructive story only when you claim *axiomatic* strength; keep order/time in their places. This keeps the core specification **evergreen and tool‑agnostic**, as required.

