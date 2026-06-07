---
chunk_kind: "child"
pattern_id: "A.6.9"
pattern_title: "U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)"
section_id: "A.6.9:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.9/A.6.9__010_consequences.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "A.6.9 — U.CrossContextSamenessDisambiguation - Repairing cross-context “same / equivalent / align” via explicit Bridges (RPR‑XCTX)"
  - "A.6.9:9 — Consequences"
line_start: 16724
line_end: 16742
dependencies:
  - "A.6.6"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.3.3"
  - "E.10"
  - "E.10.D1"
  - "E.10.U9"
  - "E.17"
  - "E.19"
  - "F.0.1"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "CL"
  - "SenseCells"
  - "alignment"
  - "bridge"
  - "cross-context sameness"
  - "direction"
  - "loss notes"
  - "mapping"
  - "substitution licence"
  - "weakest-link"
---

### A.6.9:9 - Consequences

* **Pros**

  * Removes ambiguity between explanation, naming compatibility, and substitution.
  * Makes directionality explicit; prevents accidental inverse reasoning.
  * Forces Loss disclosure early; reduces later integration surprises.
  * Provides a disciplined evolution path (change classes) when evidence changes.

* **Cons**

  * Adds visible structure to prose; authors must choose `kind/dir/CL/scope` explicitly.
  * Requires reviewers to engage with counter‑examples and loss notes.
  * Can surface uncomfortable truth: many “same” claims are only Naming‑only.

**Adoption test (PRAG).** Take any cross‑Context sentence that uses an umbrella predicate (“same/equivalent/align/map/…”). If the team cannot (a) name the two SenseCell endpoints, (b) state `dir`, (c) write at least one Loss bullet, and (d) give a crisp counter‑example (for CL≤2), then the claim is not ready to be treated as Naming‑only or substitution‑eligible. Keep it as Explanation‑only (or explicit non‑licensing prose) until evidence exists.

If the endpoints’ canons are versioned and the team cannot state `Γ_time` (edition/as‑of basis), treat that as the same kind of “evidence missing”: keep the claim Explanation‑only.

