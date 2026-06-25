---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:14"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__016_rationale-informative.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:14 — Rationale (informative)"
line_start: 34819
line_end: 34838
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:14 - Rationale (informative)

**13.1 Why canonical‑first?**
CT2R-LOG treats the **human-readable, task-appropriate relation** (e.g., `ut:ComponentOf`) as the **canonical publication form** because that is what engineers and managers actually use to reason, decide, and communicate. The formal layers **ground** that form; they do not replace it. This is consistent with the authoring Standard in Part E (pattern template and style guide), which privileges **clarity, purpose and didactics** over premature formalism in the body text. Authors write *for people first*, then point to the kind of assurance they are invoking.

**13.2 Why two `tv:` links—and why concept‑only?**
`tv:AliasOf` and `tv:groundedBy` name **conceptual bridges** between a Working‑Model relation and its assurance. They are *not* mandates for any particular notational scheme; they are **mental handles** that keep authors honest about *what* grounds their claims (constructive, logical, mapping) and *when* that grounding is expected to be present. This honours the **Notational Independence** guard‑rail in Part E: we adopt **concepts and obligations**, not file formats or tool Standards, in the normative text.

**13.3 Why a triad of `validationMode`?**
The triad **{postulate, inferential, axiomatic}** expresses staged formality compatible with the FPF stance on staged assurance: start with what the team can responsibly claim now, then move to stricter justification where risk or context demands it. That gives reviewers a shared vocabulary for the declared assurance posture of a claim without changing the canonical relation itself.

**13.4 Why keep order/time out of mereology?**
CT2R‑LOG aligns with A.14’s **firewall**: structure (parthood) is distinct from **order** and **temporal coverage**. The former is published as `ut:StructPartOf` sub‑relations; the latter live in `Γ_method` / `Γ_time` and must **not** be smuggled into part‑trees. This separation avoids classic modelling failures (temporal smearing, pseudo‑components for quantities) and keeps reasoning crisp across the Γ‑family.

**13.5 Why point to `Γ_m.sum | set | slice` (Compose‑CAL) for constructive grounding?**
Three constructive moves—**sum, set, slice**—are sufficient to narrative‑rebuild all structural trees while preserving **extensional identity**. When an author selects the *axiomatic* stance, a brief `grounding narrative` can always be told in those terms, without expanding the kernel or inventing bespoke constructors. This satisfies **parsimony (C‑5)** and keeps formal power **outside** the kernel, in a calculus.

**13.6 Why mental obligations rather than process mandates?**
Part E requires that patterns govern **thinking** and **authoring**; enforcement and automation, if any, are external concerns. CT2R‑LOG therefore states obligations as **self‑contained cognitive checks**: declare your mode; tell the constructive story only when you claim *axiomatic* strength; keep order/time in their places. This keeps the core specification **evergreen and tool‑agnostic**, as required.

