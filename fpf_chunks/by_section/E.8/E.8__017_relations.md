---
chunk_kind: "child"
pattern_id: "E.8"
pattern_title: "FPF Authoring Conventions & Style Guide"
section_id: "E.8:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8/E.8__017_relations.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "E.8 — FPF Authoring Conventions & Style Guide"
  - "E.8:12 — Relations"
line_start: 73802
line_end: 73815
dependencies:
  - "E.10"
  - "E.10.MOVE"
  - "E.11.PFP"
  - "E.11.PUR"
  - "E.13"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4.DPF"
  - "E.5.1"
  - "E.5.4"
  - "E.6"
  - "E.7"
  - "E.8"
  - "E.8.ECSPF"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "). The key words MUST"
  - "MAY"
  - "MUST NOT"
  - "MUST NOT appear inside Definition:/Invariant:/Well-formedness constraint: blocks. When enforceable"
  - "Prevents ambiguity between obligation language and model validity"
  - "RECOMMENDED"
  - "REQUIRED"
  - "SHALL"
  - "SHALL NOT"
  - "SHOULD"
  - "SHOULD NOT"
  - "and OPTIONAL are to be interpreted as described in RFC 2119"
  - "improves auditability"
  - "inside the predicate block"
  - "or other admissibility conditions of the modeled world"
  - "structural invariants"
  - "to state definitions"
  - "typing rules"
  - "“is required to”) in normative clauses"
---

### E.8:12 - Relations
* **Coordinates with:** `E.9.DA` when an authored pattern body is drafted from a concrete `DRR` and the blocker is whether the `DRR` selected, distributed, carried source use, carried accepted decisions, or supplied a first drafting action sufficiently for that authoring use. `E.8` still governs the pattern body; `E.9.DA` is not a mandatory authoring section, review card, or substitute for writing the Solution.

* **Builds on:** E.6, E.7
* **Constrained by:** Guard‑Rails E.5.1–E.5.4 (lexical firewall, notation independence, etc.)
* **Coordinates with:** `E.21` when one authored FPF pattern version is evaluated as a scoped pattern-quality claim. `E.8` governs authoring shape, recognition text, action guidance, worked cases, SoTA grounding, and conformance material; `E.21` governs the pattern-quality evaluation, required coordinate values, `PatternQualityStatus`, and stop condition. Do not import `E.21` as a mandatory authoring section or full review card.
* **Coordinates with:** `E.23` when an authored FPF pattern body is being improved through repeated passes. `E.8` still governs the authored pattern body; `E.23` governs the repeated quality-improvement method; the object-under-improvement evaluation such as `E.21` or `E.9.DA` supplies value meanings and stop meanings.
* **Coordinates with:** `E.13` when an authored pattern claims practical payoff or uses a visible quality value, metric, checklist result, review result, or release posture as if it were the intended value. `E.8` keeps the payoff in user-facing prose; `E.13` repairs proxy-to-value substitution.
* **Coordinates with:** `E.4.DPF` for choosing a DPF reference code, PatternID plan, continuity across editions, and reader return after split, merge, replacement, or retirement; and `E.11.PFP` for current Part, position, public order, and citation display. `E.8` owns only the common identifier grammar and reference wording; identifier form and checker success decide none of those authoring or publication questions.
* **Coordinates with:** `E.11.PUR`, which supplies the recommended-pattern-use decision for a current concern, and `E.10.MOVE`, which disambiguates whether move-like wording names pattern-use recommendation, direct work, plan, gate, transformation, publication, source, architecture, call-planning, or language-state material. These references state concrete contributions; an exact assertion, claim-bearing episteme, or `ClaimGraph` is added only when the named receiving use depends on that identity.


* **Constrains:** All patterns; the DRR template references the same section order.

