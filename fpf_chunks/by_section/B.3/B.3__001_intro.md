---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus"
section_id: "B.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__001_intro.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "B.3 — Trust and Assurance Calculus"
  - "B.3:intro — Intro"
line_start: 38046
line_end: 38066
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.6"
keywords:
---

## B.3 - Trust and Assurance Calculus

> **Type:** Foundational (B)
> **Status:** Stable
> **Normativity:** Normative when an FPF use makes an assurance claim about one exact target claim.

> **Plain-English headline.**
> B.3 helps a practitioner state what an assurance claim is about, which argument and results support it, what use they support, what remains unsupported, and what would reopen the conclusion. It does not turn a badge, evidence item, calculation, record, publication, status, or decision into assurance by appearance.

**Use this when.** Use B.3 when an actual named assurance claim is current: for example, a claim that an exact model claim is credible for one decision, or that an exact safety claim is adequately supported for one release use.

**First useful move.** Write the target claim and the assurance use in one sentence. Then ask which direct results and argument make that use supportable. If there is no assurance claim, stop and use the pattern that defines or tests the actual evidence, status, gate, permission, safety, release, work, or domain-result claim.

**What goes wrong if missed.** A visible label or a convenient score starts raising trust without an exact target, argument, basis, limitation, and use. At the other extreme, a modest assurance question is forced through a universal score and a large record whose fields do not affect the decision.

**What this buys.** The user gets the smallest assurance result that changes the named use, with enough basis and limits to inspect or reopen it. Domain-specific characteristics and calculations remain usable without pretending that unlike measures share one scale.

**Not this pattern when.** Stay with `A.2.4` for the classification of an episteme as evidence, `A.10` and `G.6` for source recovery and bounded reliance, `G.11` for currentness, `F.10` for a status value and its use, `A.21` for a gate decision, and the direct domain pattern for safety, permission, access, responsibility, release, compliance, or controlled action. Consequence alone does not create an assurance claim. A direct domain rule may require one, but the claim must be stated before B.3 is applied.

**First output.** Produce either one bounded `AssuranceResult` claim or a plain statement that the available argument does not support the attempted assurance use. Do not create a B.3 result merely to record that another pattern is relevant.

