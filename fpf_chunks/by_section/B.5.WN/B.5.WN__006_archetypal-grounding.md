---
chunk_kind: "child"
pattern_id: "B.5.WN"
pattern_title: "Develop Lines of Thought with Working Notes"
section_id: "B.5.WN:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.WN/B.5.WN__006_archetypal-grounding.md"
commit_sha: "0c6ade275e9360f0c5ab9715d8f05c0dbaa13cf8"
heading_path:
  - "B.5.WN — Develop Lines of Thought with Working Notes"
  - "B.5.WN:5 — Archetypal Grounding"
line_start: 44296
line_end: 44363
dependencies:
  - "A.15.10"
  - "A.6.3.RT.OE"
  - "B.5.EA"
  - "B.5.QD"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.2.8"
keywords:
---

### B.5.WN:5 - Archetypal Grounding

#### B.5.WN:5.1 - From a duration note to a new cross-case question

A practitioner is investigating reports that a bench is slow. Job Q41 is received at 09:05 and has a usable result at 10:00; the bench is occupied from 09:30 to 10:00. Q42 is received at 11:00, occupies the bench immediately and has a usable result at 11:30. The comparison developed in A.6.3.RT.OE distinguishes 55 versus 30 minutes until a result from equal 30-minute occupation.

A rough cue says “same bench time, different speed”. Before its context disappears, the practitioner writes a usable thought:

> **Compare the same beginning and result events.** Q41 and Q42 both occupy the bench for 30 minutes. Their receipt-to-result durations differ because Q41 begins occupation 25 minutes after receipt. These observations distinguish waiting from occupation; they do not explain why the wait occurred.

The note returns to the two jobs' observed times. An entry for “apparent speed differences” makes it available beyond a folder devoted to this bench.

Q43 later occupies the bench from 13:00 to 13:30 unsuccessfully, then from 13:50 to 14:20 successfully; its receipt is at 13:00. Time to the usable result is 80 minutes, occupation is 60 and the interval between attempts is 20. The practitioner adds:

> **One job can require several attempts.** Relating one job directly to one occupation interval would lose Q43's history. Keep the attempt and its outcome available when comparing time to a usable result.

The connection to the earlier note states the changed assumption. Q41/Q42's observations and calculation remain valid. The new distinction changes the construction needed for Q43. The practitioner places this note under an entry for time to a usable result, with a return from the earlier speed-comparison entry.

In another project, all reviews are reported as completed, but the receiving comparison still lacks a common basis: the reviews evaluated different configurations. While asking whether completed activities supplied the usable result now needed, the practitioner follows the usable-result entry and retrieves the duration notes. Juxtaposition produces a new question:

> **Which event makes a result available for its next use?** Ending the producing activity and obtaining a usable receiving result can differ. Investigate the required relation in each case; equal words such as “completed” do not establish it.

This note is an own cross-case conjecture and question. Its links name the bench and review contributions and preserve their different grounds. It proposes an inquiry; it does not establish a common cause.

Now change the review facts: all reviewers used a common valid basis, but the recipient has not opened their results. The missing-basis explanation fails in that case. The practitioner narrows the connection to the distinction between a result's availability and its actual use, retaining the original bench observations. If no current project needs this question, the semantic entry is a sufficient continuation. If a delivery decision needs it today, the project must establish which result is actually available before acting.

#### B.5.WN:5.2 - Develop an assigned explanation from mathematical notes

A writer must explain what can be inferred about sums of irrational real numbers. The writer already understands rational numbers and the usual proof that `sqrt(2)` is irrational. One note contains a proved statement: adding a rational number to an irrational number yields an irrational number. If the sum were rational, subtracting the rational addend would make the other addend rational.

A rough second note asks whether adding two positive irrational numbers must also yield an irrational number. Keeping the quantifiers in the formulation makes a counterexample searchable. The writer tries `sqrt(2)` and `2 - sqrt(2)`. Both are positive. The second is irrational, since making it rational would make `sqrt(2)` rational by subtraction. Their sum is exactly 2.

The new note retains the two values and that short justification. Its link to the first says: “The first proof requires a rational addend; replacing that condition by an irrational addend permits a rational sum.” Separating the counterexample from its positivity and irrationality grounds would make later use require reconstruction. A small connected note is sufficient.

The assigned explanation also needs a case where two positive irrational addends have an irrational sum. Using `sqrt(2) + sqrt(2) = 2sqrt(2)` supplies it: if that sum were rational, division by the nonzero rational 2 would make `sqrt(2)` rational. The two cases now support the bounded answer that the sum can be rational or irrational. They do not classify products, limits or other operations.

The writer's outline becomes: distinguish the rational-addend theorem; present the rational-sum counterexample; present the irrational-sum case; state the resulting limit of inference. Rewriting the notes into that order produces an explanation for the assigned question. The earlier theorem remains in the collection, with its actual condition.

A later question about squares can enter through the same concern with what an operation preserves. The present note does not answer it. The writer either develops that question through the relevant mathematics or retains the possible connection for another occasion.

#### B.5.WN:5.3 - Carry a developing question into operational case work

An engineer has the notes in :5.1, including their corrected question about availability and actual use. They do not establish that every delay has the bench's cause. The engineer keeps an entry for “completed activity, receiving result still unavailable”.

At an already authorized support handover, a case note says: “Nightly exports finish on time; the senior analyst removes duplicates every morning. The customer proposes buying faster workers.” Private row contents remain in the customer's system. The engineer's permitted work is to examine the support question, not to change that system.

The engineer follows the entry and brings the earlier question to this episode: which result must “finished” supply to the analyst, and what work remains after that event? The comparison produces a new working note:

> **A recorded completion can leave a receiving contribution to be performed.** Here the export has ended, but producing a usable report still includes duplicate reconciliation. Faster export has not yet been shown to remove that contribution. The bench and review cases helped pose this question; they do not identify the export's cause.

The connection states its limited transfer. The support case remains the source of this observation. A return to that case lets the engineer distinguish the customer's proposal from the proposed explanation. The note also leaves a question: under which receiving protocol is reconciliation needed, and what contribution could replace the manual work?

Now use the subject information available in this constructed case. The current manual distinguishes protocol v1, which requires manual receipt reconciliation, from v2, which permits idempotent resend after absence of a receipt has been confirmed. The installed protocol is unknown. The engineer's useful support result is a conditional explanation and a request for that configuration fact through the authorized local service. Neither the resemblance to the earlier cases nor the finished note selects automatic resend.

A later signed configuration report says v2. The retained case question makes its contribution recognizable: it supplies the missing protocol fact. At the next permitted handover, the engineer reads the governing manual and the current case basis. Under the stipulated v2 rule, absence of the relevant receipt must still be confirmed before the proposed resend. The configuration result has answered one question; it has not performed that check or the action. The recipient receives the case-specific explanation and needed next contribution, not the engineer's entire note collection.

Compare the full construction with the smaller incumbent. The ordinary case record already retains the duplicate episode, the protocol question and the eventual report. It is sufficient to resume this same support case; copying those facts into a second case ledger adds no needed capability. The longer-lived note contributes a separately developed question, its grounds and its limits across the bench, review and export occasions. Making that thought available costs the formulation and maintenance of the note and entry. When a practitioner can obtain the same question directly from the present record, no advantage of the additional network is established for that use. Keep the network contribution only for continuations that actually use it.

Finally change the governing source. A new manual still describes v2 but additionally requires destination certification. The available report identifies v2 and says nothing about certification. Preserve that observation, the original duplicate episode and the question that connected them. Revise the conditional advice: the former basis is insufficient for this proposed resend. Obtain the certification contribution through an authorized route or withhold the action; the current protocol fact need not be collected again merely because another premise is missing.

The note has helped construct and carry a question into work. The allowed encounter, configuration read, interpretation of the manual and controlled operational action remain actual contributions with their own conditions. A saved connection performs none of them by itself.

#### B.5.WN:5.4 - Keep the simpler project record when it suffices

An operator records a replacement part, installation time and required follow-up in an existing maintenance case. The next technician can find the current state and perform the scheduled check through that case. Copying those facts into a separate personal note network supplies no identified continuation.

Use the case directly. If several cases later expose a recurring unexplained relation, formulate that question with returns to the relevant observations. The later inquiry can justify a connected note without replacing the operational record.

