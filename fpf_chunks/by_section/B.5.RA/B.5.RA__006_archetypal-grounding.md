---
chunk_kind: "child"
pattern_id: "B.5.RA"
pattern_title: "Recover an Argument for Its Next Use"
section_id: "B.5.RA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RA/B.5.RA__006_archetypal-grounding.md"
commit_sha: "60744ae65f5fd6af60ea1e887878e20abe6be429"
heading_path:
  - "B.5.RA — Recover an Argument for Its Next Use"
  - "B.5.RA:5 — Archetypal Grounding"
line_start: 45123
line_end: 45251
dependencies:
  - "B.5"
  - "B.5.MPC"
  - "B.5.RC"
  - "B.5.RR"
  - "C.2.8"
  - "C.37"
keywords:
  - "distinguishes ordinary access to knowledge from expertise"
---

### B.5.RA:5 - Archetypal Grounding

#### B.5.RA:5.1 - Understanding why the sum of odd numbers is a square

Consider this compressed argument: “The sum of the first n positive odd numbers is n²: the sum and the square start at zero, and both increase by 2n+1 when n increases by one.” The statement concerns every nonnegative integer n. A reader recognizes the formula but needs to explain the steps compressed in that reason.

Write S(0)=0 and S(n+1)=S(n)+(2n+1). The main reason is that both the sum and the square start at zero and grow by the same amount when n increases by one. The algebraic identity (n+1)²−n²=2n+1 supplies that connection.

Recover the general transition. Assuming S(n)=n² for an arbitrary nonnegative integer n gives:

S(n+1)=S(n)+2n+1=n²+2n+1=(n+1)².

The temporary assumption is the induction hypothesis. It supports the successor step. Together with S(0)=0, that step establishes the statement for every nonnegative integer by induction.

For n=3, the sum is 1+3+5=9. Adding the next odd number, 7, gives 16. This instance makes the equal-increment operation visible. The argument's reach comes from the arbitrary n, the base value and the induction rule.

A square drawing gives another way to follow the increment: grow an n-by-n square with a row of n cells and a column of n+1 cells. That adds 2n+1 cells. The drawing and algebra expose the same increment under the counting interpretation.

The reader can now explain the role of the initial value and successor step. If the next task instead asks for the sum of n odd terms beginning at 3, the changed range opens a revision: use the established sum through the (n+1)th odd number and remove the first term, giving S(n+1)−1=n²+2n. For four terms, 3+5+7+9=24. The reusable contribution is the recovered relation between range, initial value and increment.

If the original question asked only for 1+3+5, direct addition would already supply the result. Recovering the general argument earns its effort when explanation, general use or revision needs it.

#### B.5.RA:5.2 - Understanding a drawing-recovery argument

A team needs to open an archived engineering drawing for reuse. Someone argues that the drawing is recoverable because three backup copies exist.

Recover the method behind that conclusion. For the encrypted-backup route, the needed contributions are readable stored data, an available way to decrypt it and a decoder for the drawing format. Their joint use produces a readable drawing. Having more copies addresses loss of stored data, while all three may still share one decryption key.

Suppose the key is unavailable. The backup count leaves the decoding route incomplete. The next useful question is whether the key can be recovered or another usable copy obtained. The recovered argument identifies that missing prerequisite.

Now suppose a separate plaintext copy in a readable format is available. That gives a different route to the drawing and permits the team to continue without recovering the encryption key for this use. The original encrypted route remains conditional.

The result is a usable recovery choice or a focused request for a missing contribution. A later claim that the opened drawing describes the present equipment requires its own comparison; the file-opening argument answers the immediate recovery question.

#### B.5.RA:5.3 - A projection argument with two grounds and one shared condition

A seminar organizer receives the message: ‘The slides should display correctly. Dana says the projector is compatible, and yesterday's rehearsal worked.’ The organizer needs to decide whether another display test is needed before using projector P with laptop L and adapter D. The relevant technical claim C is: **the current PDF can be displayed at 1080p by this setup**. It says nothing yet about sound, remote attendance or uninterrupted operation for an entire seminar.

**Construct the offered argument.** Ask what ‘compatible’ and ‘worked’ mean here. Suppose Dana maintains these projectors, has relevant technical expertise, and explicitly confirms her claim: ‘The current PDF can be displayed at 1080p using P, L and D at the current settings.’ Separately, the organizer personally inspected all pages of the current PDF during the rehearsal and found them displayed correctly at 1080p. Recover the condition S: the equipment, PDF and settings relevant to this result have not changed.

The expertise and the assertion work together in the first reason. Neither ‘Dana is an expert’ alone nor an unattributed compatibility sentence supplies that reason. The rehearsal is a different ground: it is an observed instance under the required setup. Its use for another showing depends on S and on the ordinary technical judgement that the successful test remains applicable. It is not a deductive guarantee of future operation.

The following outline is an argument map. Braces group premises used together; arrows mean support for C, not physical causation or event order.

```text
R1: {Dana has relevant expertise; Dana asserts C for P/L/D; S}
    --expert-opinion inference--> C
R2: {the organizer observed the current PDF displayed correctly on P/L/D; S}
    --applicable rehearsal result--> C
```

R1 and R2 are separate grounds, but they share S. R2 is not merely another report of Dana's judgement. There is no numeric independence or probability claim.

**Question the ground.** A colleague asks, ‘Did Dana assess this adapter, or just the projector's ordinary input?’ Dana replies that her message was shorthand: she knows P and L but had assumed that D was compatible. This answer removes the claimed coverage of her assessment. Mark the objection at R1's asserted scope and its use for C. The resulting conclusion is not ‘the slides cannot display’. R2 still supplies the observed result for P/L/D. If that rehearsal is an adequate technical basis for this modest use and S holds, the organizer can use C on R2 alone. The map records why losing one reason need not lose the conclusion.

**Revise after a common condition changes.** Before the seminar, D is replaced by D2. B.5.RR now follows the changed configuration through both uses of S. The rehearsal remains evidence about D, and Dana's statement supplies no assessment of D2. C for the new setup is unresolved. Testing the new setup, restoring D, or obtaining an applicable technical account can close that gap. Repeating the old positive reports cannot.

Suppose a test with D2 then shows that the current PDF is not displayed under the intended settings, after the operator checks the connections and follows the equipment's setup instructions. This is a new opposing observation for that tested setup. The organizer can report that the attempted display failed and return to technical diagnosis; the observation alone does not identify which component caused the failure.

**Separate the technical result from the practical proposal.** ‘Therefore use P’ introduces another inference. It needs the seminar's display requirement, an available way to keep the tested setup, and comparison with relevant alternatives and costs. If using P prevents another booked session from running, that consequence can defeat the proposal while C remains supported. PSD.8/.9/.11 supply the option, value and consequence work. The receiving decision uses the qualified technical result instead of silently expanding it into a recommendation.

The useful return is a conclusion with its surviving reason and its next change condition: use the rehearsal for the unchanged setup; reopen compatibility after replacing the adapter; treat the later failed display as a result to diagnose. Another person can challenge a specific connection and see what needs to be redone.

#### B.5.RA:5.4 - From an ambiguous message to a conditional venue argument

An amateur theatre group is choosing a room for a complete three-hour rehearsal on Friday evening. It receives this message:

> Use the school hall on Friday. If it is free, we can rehearse there together. Noor says it is; she manages the bookings. We missed last week because the band had the hall. Paying for the studio would be a waste.

**Begin with possible readings.** “Free” could mean unbooked or without a hire charge. “It is” could refer to either meaning, and “we can rehearse” might concern some rehearsal rather than the complete three-hour session. The opening recommends a venue; it does not itself justify that choice. The conditional in the second sentence supplies a proposed relation between availability and rehearsal feasibility. It does not establish availability.

A first sketch that puts “the hall is free” and “we can rehearse” into two boxes as asserted facts has strengthened the text. A sketch that puts every remaining sentence directly under “use the hall” hides how the recommendation is supposed to follow. Two more faithful readings remain: the message could argue from available space or from avoiding a hire charge. The booking role makes the first reading plausible, but does not prove which meaning the speaker intended.

Ask the organizer what was meant. Suppose the reply is: “I meant unbooked for our Friday rehearsal. Noor told me there was a free slot. I was explaining last week's cancellation, which we all already know about.” This supports the availability reading and identifies the “because” sentence as an explanation of the accepted cancellation. Keep that explanation as context; it supplies no evidence that the hall is available this Friday. The reply still does not establish the slot's duration or the relative cost.

**Extract the claims without filling the gaps.** The organizer's proposed conditional is now: if the school hall is available for the required Friday session, the group can complete that rehearsal there. Noor is reported to have said there is a free slot. Managing the bookings gives a reason to treat her as able to know the booking entries, not as an expert on every condition of a rehearsal. Recovering her statement's actual scope is necessary before using it for the three-hour claim.

The sentence about waste suggests a practical choice: avoid paying for an alternative when an adequate option already exists and the payment buys no relevant advantage. It does not mention past investment or abandoning an earlier undertaking. A sunk-costs scheme therefore adds the wrong premise. The useful question is which present and future differences make the studio expense unnecessary.

A provisional structure makes the missing intermediate result and grounds visible. Braces below group co-premises. “Reported” retains attribution; “proposed implicit” identifies a reading supported by the waste remark but not yet confirmed. Arrows mean the indicated support.

```text
{Noor manages the bookings; Noor is reported to say a slot is free}
    --ordinary knowledgeable-source inference-->
    A: a Friday slot is available (its hours remain unconfirmed)

{A with the hours required by the group;
 the organizer's conditional about completing the rehearsal}
    --conditional application-->
    F: the group can complete the required rehearsal in the hall

{F;
 D: using the hall has lower relevant burden and the studio adds
    no compensating benefit [needed comparison, not supplied];
 V: choose the adequate option without that unnecessary burden
    [proposed implicit choice rationale]}
    --practical inference--> C: use the hall for this rehearsal
```

A is not yet the premise about the required hours, and F is not simply another independent reason alongside Noor's report. F depends on the availability claim and the organizer's conditional. D is an exposed need for evidence, not a fact extracted from “waste”. The practical argument remains conditional on it and on the other requirements in F. The map therefore recovers both the plausible offered reasoning and what it has not supplied.

**Use the structure to ask the next question.** The availability claim affects every later step, so ask Noor for the actual interval before making a booking. She replies: “The hall is unbooked from 18:00 to 20:00; another group has it after that.” The actors need 18:00 to 21:00 for the complete run. Preserve Noor's narrower claim; do not revise it into a false claim that the hall is occupied all evening. Replace A's uncertain scope with the two-hour interval. That interval does not supply the required three-hour premise, so the route to F and C fails for the intended session. It is unnecessary to settle the cost comparison to reach this result.

B.5.RR follows that affected route while retaining the usable booking information and last week's explanation. A shorter rehearsal, a different time or the studio can become alternatives, but each changes a condition or opens another argument. The source has not justified any of them merely by losing its first recommendation. If the group changes the task to a two-hour scene rehearsal, reassess the conditional's remaining requirements and the practical comparison for that new use.

**Separate reconstruction from a repair.** Suppose the reader now checks room capacity, access for every actor and both venues' charges. Those findings may help construct a better choice argument. They are new grounds obtained by the reader. They do not make the original message complete or turn its ambiguous “free” into a statement about price.

#### B.5.RA:5.5 - An expert's title cannot turn a clue into an observation

A workshop colleague writes: “The parcel has arrived. Noah, our electronics expert, says so: the goods trolley is back by the door.” The recipient wants to tell an assembler that the replacement parts are ready to collect.

Trying expert opinion first exposes a mismatch: electronics expertise does not establish knowledge of this delivery. Ordinary access could matter instead. A person who checked the parcel could report its arrival without being an expert. Before replacing the first scheme with knowledgeable testimony, recover what Noah actually knows.

Ask, “Did Noah receive or see this parcel, or infer its arrival from the trolley?” Suppose Noah replies, “I saw the trolley. I haven't looked for the parcel; deliveries usually bring it back.” Now the distinction changes the structure:

```text
{Noah saw the trolley by the door; his report is usable for that observation}
    --ordinary observation report--> T: the trolley is by the door

{T; a proposed connection between this trolley's return and this parcel}
    --inference from a clue--> P: this parcel has arrived
```

Noah's claim about the trolley can remain credible while his conclusion about the parcel is unsupported. The observation and inferred arrival were compressed into one attributed statement. The repair separates them and locates the missing connection. It does not establish that Noah was dishonest, that the parcel is absent, or that a witness's every claim needs specialist credentials.

Ask what other work moves the trolley and whether this delivery was due to use it. Suppose the workshop uses the same trolley for outgoing parcels, and today's dispatch account explains its current position. That removes the offered clue's claimed discrimination for this arrival. The recipient can check the receiving record or inspect the parcel location. Either would be a new ground; repeating Noah's title supplies none.

This differs from a disagreement over the trustworthiness of a witness who actually saw the parcel. In that case the disputed ground would be the report. Here the observation is accepted and the disputed transition is from trolley position to this parcel's arrival. The first scheme has been abandoned for a substantive reason, the map has changed, and the next inquiry follows the remaining gap.

