---
chunk_kind: "child"
pattern_id: "C.40.CD"
pattern_title: "Develop Problems and Ways of Solving Them Together"
section_id: "C.40.CD:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.40.CD/C.40.CD__006_archetypal-grounding.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "C.40.CD — Develop Problems and Ways of Solving Them Together"
  - "C.40.CD:5 — Archetypal Grounding"
line_start: 76990
line_end: 77040
dependencies:
  - "B.5.MPC"
  - "B.5.QD"
  - "B.5.RC"
  - "B.5.TU"
  - "C.11.DUA"
  - "C.18"
  - "C.19"
  - "C.39.RO"
  - "C.40"
keywords:
---

### C.40.CD:5 - Archetypal Grounding

The following constructed cases supply their task conditions and ordinary subject operations. They demonstrate the reasoning and its limits.

#### C.40.CD:5.1 - A mixed transfer leaves a narrower comparison available

An investigation requires each error/non-error comparison to share both setup and temperature regime. An existing grouping operation uses setup alone. The permitted target records are:

| Record | Outcome | Setup | Temperature |
| --- | --- | --- | --- |
| T1 | Error | S1 | Warm |
| T2 | Acceptable | S1 | Cool |
| T3 | Error | S2 | Warm |
| T4 | Acceptable | S2 | Warm |

The source operation returns T1–T2 and T3–T4. Comparing those outputs with the target rule exposes the first pair's temperature mismatch.

The changed local problem is to return eligible pairs and expose where no comparison is supported. An available filtering operation adds temperature to the grouping key. It returns T3–T4 and no eligible S1 pair. This operation constructs the target comparison; repeating the old setup-only grouping would preserve the mismatch.

The result permits the S2/warm comparison if it serves the investigation. The S1 question remains open. A next inquiry can seek a comparable S1 record when obtaining it could change the needed explanation; alternatively, receiving work can use the narrower result or stop. The original source operation retains its uses where setup alone was the applicable rule.

The grouping has established eligibility for comparison. A causal explanation would need the separate reasoning and observations for that claim.

#### C.40.CD:5.2 - An obstruction changes the mathematical question

A scheduling model represents pairwise conflicts by the finite undirected path A-B-C-D. There are no capacity or precedence conditions in this model. Assigning A and C to session 1, B and D to session 2 satisfies its conflicts.

A new conflict A-C creates the triangle A-B-C. Applying two-coloring now exposes an odd cycle. Two sessions are impossible under the retained pairwise-conflict model.

That result supports the next mathematical question: what is the least number of sessions? The triangle requires at least three. The assignment A=1, B=2, C=3, D=1 satisfies every edge, so three suffice and are minimal. The obstruction and construction together answer the new question.

If the receiving project actually has only two sessions, the new mathematical answer identifies a resource mismatch. Receiving work must change a real conflict condition, obtain another session or accept that the stated assignment cannot be supplied. Merely asking the easier resource question has not removed that requirement.

The successful three-session construction opens a further question when more conflicts are expected: which additions remain compatible with three sessions? Adding A-D invalidates the old assignment because A and D both use session 1. Retain A=1, B=2 and C=3, and move D to session 2. This changed construction satisfies all five conflicts.

If B-D is then added as well, every pair among the four vertices conflicts. Four sessions are now necessary, and assigning one vertex to each session attains that bound. The successful construction has led to a new question, a local repair and then a limit on that repair. These results distinguish which anticipated conflicts can be accommodated with three sessions and which require changing the allocation conditions.

#### C.40.CD:5.3 - A physical invariant replaces a timed operation

A device should dispense 40 cm³ from a reservoir. An earlier constant-flow model used `V = q t`; with `q = 20 cm³/s`, it prescribed two seconds. The receiving situation has unknown time-varying outflow, so that duration no longer determines the volume.

The reservoir has constant cross-sectional area `A = 10 cm²`, starts at height `h₀ = 15 cm` and has no inflow or leakage. The supplied model treats the level reading and shutoff as ideal. Conservation and geometry give the dispensed volume:

`V = A(h₀ − h)`.

The changed construction asks which level corresponds to the required volume. It gives `h = 15 − 40/10 = 11 cm`. The new operating rule is to stop outflow when that level is reached. At that event the model gives 40 cm³, independently of the outflow's variation before it. If outflow stops earlier, the desired level is never reached; the volume relation alone supplies no completion guarantee.

This result connects physical conservation, a mathematical invariant and an event-based operating rule. Realizing it requires usable level observation and shutoff through C.16 and C.29.3. This supplies a design result under the model's premises.

Suppose receiving work also requires completion within eight seconds. The level rule has left that condition open. A supplied bound `q(t) ≥ 5 cm³/s` until the target level makes the accumulated outflow at least `5t`, so 40 cm³ is reached within eight seconds under the same ideal model. If no such flow support is available, keep the deadline unresolved or change the physical arrangement.

