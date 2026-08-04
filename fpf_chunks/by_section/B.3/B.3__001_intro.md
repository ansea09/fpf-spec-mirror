---
chunk_kind: "child"
pattern_id: "B.3"
pattern_title: "Trust and Assurance Calculus (F-G-R with Congruence)"
section_id: "B.3:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3/B.3__001_intro.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "B.3 — Trust and Assurance Calculus (F-G-R with Congruence)"
  - "B.3:intro — Intro"
line_start: 38475
line_end: 38497
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.4"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.3"
  - "B.3.5"
  - "B.4"
  - "C.13"
  - "C.16"
  - "C.16.Q"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "C.26.3"
  - "C.28"
  - "C.29"
  - "D.4"
  - "E.14"
  - "E.17"
  - "E.17.EFP"
  - "E.24.PUB"
  - "F.10"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
  - "F-G-R"
  - "assurance"
  - "authority-looking labels"
  - "claim-support posture"
  - "congruence"
  - "dashboard tiles"
  - "evidence"
  - "formality"
  - "probe/distributed/export/causal assurance"
  - "reliability"
  - "scope"
  - "trust"
---

## B.3 - Trust and Assurance Calculus (F-G-R with Congruence)

> **Type:** Foundational (B)
> **Status:** Stable
> **Normativity:** Normative for FPF use that claims assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for a named claim.

> **Plain-English headline.**
> B.3 governs an assurance-result claim about one exact claim episteme for one named assurance use. It conservatively combines formality `F`, claim scope `G`, reliability `R`, and edge-scoped congruence `CL` without turning evidence, provenance, a dashboard, a status value, an assessment record, or a later decision into assurance by presence. The target fact, its direct result, the claim episteme, assessment work, evidence-use relations, assurance-result claim, witness, record, publication, and later reliance remain separately recoverable.

**Use this when.** Use `B.3` when a receiving work or reliance decision depends on assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for one exact claim episteme.

**What goes wrong if missed.** A label, dashboard, model card, credential, provenance mark, gate decision, status value, or evidence bundle starts raising trust or readiness without an exact target claim, assessment, evidence-use basis, scope, limitations, decay condition, and named assurance use.

**What this buys.** The user gets a conservative, contestable assurance-result claim whose inputs and limits can be replayed without changing the target fact or confusing assurance with status, approval, permission, gate passage, currentness, or actual reliance.

**First output.** Write one typed `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim for exact target-claim episteme `E_C` and named assurance use `U_A`, or write an explicit no-assurance disposition. A publication face, rendering, cue, evidence pointer, wording issue, gate decision, role assertion, status-value assertion, commitment, or work occurrence is not itself an assurance result.

**Not this pattern when.** Stay with `A.2.4` when the question is how an episteme is used as evidence or status support, with `A.10`/`G.6` for source recovery and bounded reliance, with `G.11` when currentness changes admissible use, and with `F.10` for the status value and its use. When no assurance claim or material-reliance threshold is current, use the exact gate, permission, commitment, work, decision, or domain-result rule that defines or tests the claim actually being made; do not create a B.3 result merely to name its pattern.

**Assurance result selection.** Use the lightest result that decides the named assurance use. A cue or source pointer gets no B.3 tuple. A local, reversible, non-release, non-compliance, non-safety use may need only a compact bounded assurance-result claim naming `E_C`, `U_A`, the evidence-use/provenance refs, limit, and reopen condition. Reserve the full typed result for readiness, compliance, safety, release confidence, trust, explicit `F/G/R/CL`, material reliance, or reuse as an assurance input.

**Assurance claim over time.** An assurance-result claim is time-bounded and updateable: it can decay, reopen, narrow, or be withdrawn. Name the drift, monitoring, incident, evidence refresh, version change, policy change, gate change, or residual unsupported-use condition that reopens it. Such a change can alter warrant or admissible reliance while leaving the target fact and target claim identity unchanged.

