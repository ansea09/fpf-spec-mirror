---
chunk_kind: "child"
pattern_id: "E.10"
pattern_title: "Unified Lexical Rules for FPF"
section_id: "E.10:5"
section_title: "Vertical Stratification (four strata; no cross-bleed)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10/E.10__007_vertical-stratification-four-strata-no-cross-bleed.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "E.10 — Unified Lexical Rules for FPF"
  - "E.10:5 — Vertical Stratification (four strata; no cross-bleed)"
line_start: 75249
line_end: 75265
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.2"
  - "A.15.PROD"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.3.2"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.7"
  - "B.1"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.D1"
  - "E.10.DEV"
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.10.ROLE"
  - "E.17"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.5"
  - "F.17"
  - "F.18"
  - "F.19"
  - "F.5"
  - "F.6"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
---

### E.10:5 - Vertical Stratification (four strata; no cross-bleed)

> **Rule V‑0 (Strata).** Every lexical item in a conformant text belongs to exactly one **stratum**:

1. **Kernel** — admitted `U.*` names, core relation kinds, and invariants (for example `U.Holon`, `U.SystemRoleAssignment`, `U.Method`, `U.Work`, and `U.PromiseContent`).
2. **Extension patterns** — CAL, LOG, and CHR exports (e.g., **Sys‑CAL**, **KD‑CAL**, **Agency‑CHR**) that **extend** but do not override Kernel.
3. **Local use** — the exact source or practice boundary, effective scheme, local meaning statements, aliases, local kind distinctions and classification rules that the use actually needs; cite an F.9 Bridge only when an exact relation between distinct local senses obtains.
4. **Instance** — concrete identifiers for admitted holder Systems, exact `U.SystemRoleAssignment` occurrences, Work occurrences, and carriers.

**V‑1 (Unidirectional meaning).** Meaning is constrained from Kernel to extension patterns to local use to Instance. A local source, practice, or scheme may add a narrower designation or distinction, but it does not silently redefine a higher stratum's term; any actual relation between distinct local senses is stated separately.

**V‑2 (Strata and authoring stances).** The four lexical strata above constrain **tokens**. They are independent of a claim-bearing unit's **stance** (its `CtxState` pins such as `DesignRunTag`, `ReferencePlane`, and `Locus`). Strata answer “what words mean here”; stance answers “where this claim is situated” and which evidence-lane expectations apply.

**V-3 (Citation style).** When a local Tech designation changes interpretation or action, its first use names the source or practice provenance and effective scheme needed to read that use—for example, `ReviewerSystemRole` under the JournalReview-2026 definition. Reuse under another local meaning first compares the exact governed values; use F.9 only if a direct Bridge between distinct exact cells actually obtains. A suffix may serve as a locator, but it establishes neither kind identity, admission, nor assignment.

**V-4 (Firewall).** Tooling and Pedagogy idioms remain outside Kernel prose (DevOps Lexical Firewall). CI/CD jargon, file formats, and API names are not admitted in Core definitions. Pedagogy may use them only as Plain-register examples with Tech anchors present.

