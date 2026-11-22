---
chunk_kind: "child"
pattern_id: "C.32"
pattern_title: "Architecture Candidate Synthesis"
section_id: "C.32:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32/C.32__006_archetypal-grounding.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "C.32 — Architecture Candidate Synthesis"
  - "C.32:5 — Archetypal Grounding"
line_start: 80448
line_end: 80469
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.25"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.HCS"
  - "C.32.LCA"
  - "C.32.MLAO"
  - "C.32.MWA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.18"
  - "E.22"
  - "E.23"
  - "G.5"
  - "U.Structure"
keywords:
  - "CandidateArchitecturePalette@Project"
  - "architecture candidate synthesis"
  - "architecture characteristics"
  - "candidate configurations"
  - "retained alternatives"
  - "selected structures"
  - "selected-structure contribution rows"
  - "trade-off front"
---

### C.32:5 - Archetypal Grounding



| Grounded working case | Synthesis question | C.32 candidate work | Stop condition |
|---|---|---|---|
| Regulated product family with growing field exceptions | How should functions, module interfaces, placement, and evidence scope be configured so substitutability and certification burden stay acceptable? | Prepare candidates that narrow interface grammar, split the family by evidence scope, change placement responsibility, or keep a bounded exception with source return. | Stop at palette unless G.5 selected-set result declaration, publication availability, assurance, or architecture decision is current. |
| Built-asset digital-twin handover where a view omits part of its source | What structure can the maintainer recover from the current view? If a new handover is commissioned, what information must reach the maintainer in time? | For the first question, use C.30.ASV and C.33 to recover the source structures, omissions and warranted use. For the second, develop proposals for the view, access to its source or the responsibility for maintaining it and trace each proposal to the receiving work. | Use C.30.AD.BA for the built-asset description, E.17 and E.24.PUB for the view and its publication, and A.10 for a claim of reliance. |
| Emergency-department triage arrangement whose local desk is fast but hospital-wide escalation is brittle | How should admitted Systems, local system-role kinds or classifications, future assignment conditions, procedure and Method structure, control, direct responsibility, evidence, and any actual Work and separately needed F.6 attribution be configured so speed does not erase escalation adequacy? | Prepare candidates that retarget responsibility only through an admitted direct predicate, state a possible mediator assignment as plan or candidate content rather than an occurrence, split triage scope by patient class, or adjust evidence capture; use the missing governor when needed. | Stop before ethical mediation, evidence, staffing decision, assignment occurrence, or performed Work unless those claims are current. |
| AI-agent review setup where local autonomy conflicts with policy scope | How should control, module-interface, evidence-refresh, and work-method structures be configured so autonomy and policy conformance stay jointly acceptable? | Prepare candidates that add supervisor relation, narrow model interface behavior, change evidence refresh cadence, or alter work-method responsibility. | Stop before safety, release, gate, or causal claims unless their subject patterns are current. |
| Method family whose shared template shortens drafting and lengthens review | Which arrangement gets an acceptable document to its reader earlier? | Compare drafting and review of each document with use of the template. Another candidate separates reusable checks on the common material from checks that need the completed document. Establish which checks can travel with the template. | Use the qualifying conditions and the reviewer’s availability to decide what can already be recommended. See §5.1. |

#### C.32:5.1 - Choose an arrangement for an accepted document

A team must deliver a document after an independent review. Under one design the author drafts for 50 minutes and the reviewer needs 20 minutes. A shared template changes those times to 35 and 30 minutes. Both designs preserve the same review of the finished document. For this comparison assume those durations, a common start, an immediately available author, review after drafting and no rework. The reviewer has time to finish once available, is authorized to accept the document and accepts it when the review ends. In this agreement, delivery occurs when the accepted document becomes available to the reader. Acceptance gives the reader immediate access.

If the reviewer is ready for either handover, the template delivers at minute 65 and the existing arrangement at minute 70. If the reviewer first becomes available at minute 60, both drafts wait. The existing arrangement delivers at minute 80 and the template at minute 90. The template saves five minutes of combined effort in both comparisons. The earliest acceptable delivery changes with the appointment. Even an inexact appointment can settle the choice. Availability by minute 39 puts the template ahead throughout that range.

A third design could qualify common material once and review its use in each finished document. To compare it, identify the common checks, the authority that accepts their reuse and the local checks each document still needs. A new heading in the template leaves this work in place unless a check or its input actually changes.

These times are consequences of the stated designs. Suppose instead that accepted documents are delivered together at minute 100. Both designs then meet the same delivery time under either appointment. If the recipient chooses the lower effort at equal delivery, the template can be selected without first resolving the appointment. To establish how long a particular release took, use its actual start and the event promised to the recipient. Use the delivery terms to identify the event and its evidence. A portal access record can establish when the document became available under this agreement. If delivery is complete when a named recipient receives the document, establish when it reached them. If the agreement also requires their acknowledgement to complete delivery, use the time of that act. A receipt at minute 100 followed by a required acknowledgement at minute 120 completes delivery at minute 120. To establish what passed review, use the applicable criterion and the review result for that document. A comparison across releases also depends on what they had to deliver, reviewer availability and any rework. A shorter observed release can raise a question about the design without identifying what caused the difference.

