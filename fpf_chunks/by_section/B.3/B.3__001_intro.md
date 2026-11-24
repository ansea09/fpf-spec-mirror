---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Is This Claim Supported for This Use? — Trust and Assurance Calculus"
section_id: "B.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__001_intro.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "B.3 — Is This Claim Supported for This Use? — Trust and Assurance Calculus"
  - "B.3:intro — Intro"
line_start: 46860
line_end: 46880
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2.4"
  - "A.2.6"
  - "A.21"
  - "A.22"
  - "A.6.1"
  - "B.1.5"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "E.17"
  - "E.24.PUB"
  - "F.10"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
---

## B.3 - Is This Claim Supported for This Use? — Trust and Assurance Calculus

> **Type:** Foundational (B)
> **Status:** Stable
> **Normativity:** Normative when an FPF use makes an assurance claim about one target claim.

> **Plain-English headline.**
> B.3 helps a practitioner state what an assurance claim is about, which argument and results support it, what use they support, what remains unsupported, and what would reopen the conclusion. A visible label or artifact contributes only through the claim and basis the argument uses.

**Use this when.** Use B.3 when a named assurance claim is current: for example, a claim that a model claim is credible for one decision, or that a safety claim is adequately supported for one release use.

**First useful move.** Identify the conclusion its recipient must assess, how it will be used and the work entrusted to the assessor. A sufficient existing argument can settle a question about one claim. To design an assessment, work back from the recipient’s decision to the distinctions the assessment must make (§4.1). To establish how someone actually used a result, identify the decision and the evidence about its use (§4.6). The domain rule governs the resulting action.

**What goes wrong if missed.** A visible label or a score starts raising trust without a target, argument, basis, limitation, and use. At the other extreme, a modest assurance question is forced through a universal score and a large record whose fields do not affect the decision.

**What this buys.** The user gets the smallest assurance result sufficient for the named use, with enough basis and limits to inspect or reopen it. Domain-specific characteristics and calculations remain usable without pretending that unlike measures share one scale.

**Not this pattern when.** Stay with `A.2.4` for the classification of an episteme as evidence, `A.10` and `G.6` for source recovery and bounded reliance, `G.11` for currentness, `F.10` for a status value and its use, `A.21` for a gate decision, and the domain pattern for safety, permission, access, responsibility, release, compliance, or controlled action. Consequence alone does not create an assurance claim. A domain rule may require one, but the claim must be stated before B.3 is applied.

**First output.** For each assurance question, state the bounded `AssuranceResult` or the limits of the available support. If the commission concerns several claims together, carry these judgements through to the conclusion the recipient needs. For a commission to design the assessment, supply the way to reach that conclusion under the permitted conditions.

