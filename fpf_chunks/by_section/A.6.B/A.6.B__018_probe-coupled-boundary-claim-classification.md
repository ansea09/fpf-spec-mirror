---
chunk_kind: "child"
pattern_id: "A.6.B"
pattern_title: "Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
section_id: "A.6.B:15a"
section_title: "Probe-coupled boundary claim classification"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.B/A.6.B__018_probe-coupled-boundary-claim-classification.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.6.B — Boundary Norm Square (Laws / Admissibility / Deontics / Work‑Effects)"
  - "A.6.B:15a — Probe-coupled boundary claim classification"
line_start: 9627
line_end: 9658
dependencies:
  - "A.10"
  - "A.2.3"
  - "A.2.8"
  - "A.2.9"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26.1"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.8"
  - "F.18"
  - "U.Commitment"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.Signature"
  - "U.SpeechAct"
keywords:
  - "(MUST"
  - "(ii) claim that evidence carriers exist (that is E-)"
  - "(ii) encode runtime entry predicates (those are A-)"
  - "(they are not obligations"
  - "Keeps modalities separated and audit‑ready"
  - "L/A/D/E claim classification"
  - "MAY"
  - "MUST"
  - "MUST NOT"
  - "MUST NOT hide a gate predicate (that is A-)"
  - "SHALL"
  - "SHOULD"
  - "SHOULD NOT"
  - "The key words MUST"
  - "admissible use"
  - "and MAY"
  - "and MUST NOT cite D-*"
  - "and SHALL are to be interpreted as in RFC 2119/8174. Lower-case must"
  - "and should in explanatory prose is descriptive"
  - "as if it were an agent obligation"
  - "as if it were an agent obligation. (It is a gate predicate"
  - "as operators"
  - "atomic claims"
  - "belong here"
  - "boundary norm square"
  - "claim IDs"
  - "laws vs gates vs commitments vs evidence"
  - "may"
  - "non-admissible use"
  - "not a duty.)"
  - "not normative"
  - "or (iii) assert evidence existence or measurement outcomes (those are E-*)"
  - "or (iii) assign responsibility or enforcement (that is D-*)"
  - "or MAY) as operators inside the law or definition itself"
  - "they describe adjudicable effects and evidence)"
  - "triangle decomposition"
  - "“commits to”)"
  - "“is admissible”"
  - "“is blocked”"
  - "“the interface or system promises” does not)"
  - "”) used as operators inside L- or A- predicates (should be D- that references L-/A-)"
---

### A.6.B:15a - Probe-coupled boundary claim classification

Probe-coupled boundary language does not create a fifth quadrant. A boundary sentence that says a question, metric, dashboard, workshop, bridge, or API read changes the represented state must still be atomized through the same L/A/D/E square.

Action classification:

1. Copy the boundary sentence being used for a decision.
2. Split it into atomic claims before judging it: definition or law claim, admissibility or use-condition claim, role commitment, and work-and-evidence effect claim.
3. Give each atomic claim its quadrant and identifier.
4. Put the state, probe, update, or export part in the quadrant where it belongs rather than treating "quantum-like boundary" as one claim.
5. Apply `A.6.P` to reusable relation words; use `F.18` only when recovered terms need durable names; apply `A.10` to evidence; apply `B.3` to assurance; apply `C.16` to measurement; apply `C.26.1` to any remaining probe-coupled state-reading claim.
6. Emit a Claim Register row set or equivalent L/A/D/E-classified claim set only when the sentence is decision-bearing, reusable, contested, assurance-facing, or likely to be cited across faces.

For a local working note, the lighter action is enough: atomize the sentence mentally, write one clean L/A/D/E-classified sentence, and avoid the phrase "quantum-like boundary" as a single claim. Use the Claim Register when the L/A/D/E-classified claim set must survive reuse or dispute.

| Quantum-like boundary phrase hides | Claim class | What the user writes |
| --- | --- | --- |
| The term, variable, state, frame, or relation being defined | `L-*` law or definition claim | Definition or invariant, without agent obligation language |
| When a probe, metric, question, or bridge use is usable for the intended decision | `A-*` admissibility or use claim | Use condition, admissible use, non-admissible use, and neighboring-pattern continuation |
| Who is responsible for applying, retaining, exposing, or not overusing the probe result | `D-*` role or commitment claim | Accountable role and referenced L/A/E claim IDs |
| What work effect, carrier, trace, report, metric, or observed before-state or after-state supports the claim | `E-*` work-effect and evidence claim | Carrier, observation condition, time window, and evidence reference |

Useful outputs:

- a Claim Register row set when the boundary sentence mixes claim kinds;
- one rewritten L/A/D/E-classified sentence when the case is only a local working note;
- an ordinary A.6.B L/A/D/E-classified claim set when no quantum-like probe-coupled state-reading claim remains;
- a C.26.1 classify only for the remaining probe-coupled state-reading part;
- an A.10/B.3/C.16/F.9 classification when evidence, assurance, measurement, or bridge work is the actual claim being made.

Do not write "the boundary is quantum-like" as one unL/A/D/E-classified claim. The action is: split the claim, classify the pieces, then decide whether `C.26.1` still has a remaining job.

