---
chunk_kind: "child"
pattern_id: "C.11.MV"
pattern_title: "Compare the Worth of a Method Option"
section_id: "C.11.MV:5"
section_title: "Archetypal Grounding - Field Evidence and Alternatives"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.MV/C.11.MV__007_archetypal-grounding-field-evidence-and-alternatives.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.11.MV — Compare the Worth of a Method Option"
  - "C.11.MV:5 — Archetypal Grounding - Field Evidence and Alternatives"
line_start: 60923
line_end: 60973
dependencies:
  - "A.3.1.FT"
  - "A.3.1.QM"
  - "C.11"
  - "C.11.DUA"
  - "C.32.MWA.PP"
  - "C.39.RQ"
keywords:
---

### C.11.MV:5 - Archetypal Grounding - Field Evidence and Alternatives

The SSFD study identified 95 instances of benefits in 41 project reports. Its investigators examined how use of the functional models connected with those benefits, directly or through subsequent work. This gives a decision maker reported outcomes, conditions of use and candidate explanations. To choose between two current arrangements, establish what each can deliver and at what burden. To estimate the effect of changing one element, establish what else would change with it and what supports that estimate.

Project 11 supplies substantial reported outputs from one by-wire steering application; Project 32 supplies a representation difficulty. Preserve both. A practical-worth result may retain SSFD for one situation, revise its representation or support for another, or return missing alternative evidence. Do not average the difficulty and benefit counts into a score.

The sustainable-design study supplies three families of separate workshop observations: The Natural Step, Whole System Mapping, and Biomimicry across 23 workshops, more than 172 qualified respondents, 27 companies, and three industries. Companies chose which workshops they took; most received two or more, order varied, and participants could differ.

The source reports immediate participant-perceived value of activities and mindsets and warns against theoretical-only recommendations. It does not itself supply one named receiver's feasible current-alternative set, a common decision, matched alternative Work, or a counterfactual basis.

Use those observations for the participant experiences they document. For a present choice, identify the feasible options, recipient and decision rule. A binding constraint or an already established difference can settle that choice. If it depends on a comparative effect on later work, account for voluntary participation, unmatched timing and participants, immediate self-report and any missing basis for transfer, causation or combining workshops. Return what can be decided with those limits.

The Halogen case can supply evidence about project demands, practitioner skill sets, organization, and cyclic adaptation. It can justify a `branch` or variant question when conditions differ, but one firm's history does not make its repertoire universally preferable.

#### C.11.MV:5.1 - EC-417 Early Stop

The [full EC-417 application](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#fpfreference169---choose-the-method-development-result-needed-for-release-ec-417) supplies the receiving problem, alternatives, calculations and the distinct limits used below.

In the constructed EC-417 case, the team must release a controller firmware and harness change on `D0`. Its software-integration slot is `D-21`, but signed supplier pinout evidence is expected at `D-8`. The present question is which proposed way to coordinate that release is worth pursuing under the current constraints.

[C.32.MWA.PP §5.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp53---possible-future-alternatives-a-b-and-b2) supplies the timing and capacity comparison:

| Alternative | Proposed way of working | Consequence for this decision |
| --- | --- | --- |
| A | Wait for signed supplier evidence before integrating the software; hold one final board. | With evidence arriving at `D-8`, the team misses the `D-21` slot. Arrival by `D-21` removes that timing disadvantage. |
| B | Integrate at `D-21` from a versioned provisional edition and reconcile it with signed evidence at `D-8`. Keep the provisional edition, its uncertainty and its earlier use traceable. The safety engineer performs all `2.00 h` of preparation of the changes between editions. | Estimated peak safety demand is `4.40 h`, above the `3.20 h` limit in an eight-hour day. |
| B2 | Use B's integration and reconciliation order and retain the same evidence history, but allocate `1.60 h` of that preparation to the supplier-configuration role and `0.40 h` to the safety engineer. | Estimated peak safety demand is `2.80 h`, within the same limit; the supplier's preparation remains part of the total burden. |
| Stop or next slot | Stop the proposed change or defer the release to an authorized later slot when the required conditions cannot be met. | State the delay or foregone result and the condition needed to reconsider. |

B2 moves preparation work to another role. Verify that its holder can absorb the 1.60 hours in the required window, is qualified to prepare the difference, and can access the relevant evidence under the supplier's confidentiality conditions. Include the work that allocation displaces and how project, user and provider Systems exchange, check and recover the records through the repository, PLM and CI systems. Three A.15.8.MS support tasks establish only the results observed on those tasks. A three-release WorkPlan describes intended work.

Keep `C-EC-Release-v2` as a candidate. Preserve the missing A.22 selection basis, untested AI-provider and feedback branches, and unsupported `CUR-EC417-CadenceEffect-1`.

With evidence at D−8, A misses the original slot. B exceeds the safety engineer's limit. B2 reduces the estimated demand on that engineer from 4.40 to 2.80 hours, within 3.20 hours. Recommend at most three trials if B2 also meets the supplier and trial-entry conditions. The responsible holder can select a trial on those grounds. If it cannot proceed, defer or stop, or seek a decision to change the slot for A. Arrival of signed evidence by D−21 would reopen A for the original slot.

An actual release or trial entry still needs every applicable capability, assignment, permission and authority condition. If the question is demonstrated release worth, return the missing performed-release and alternative evidence. The observed support-task results, with the tailoring operation still undefined and its permission/authority stop untested, do not establish that stronger result.

#### C.11.MV:5.2 - Use situated evidence in another Method-repertoire decision

Supply evidence to another Method-repertoire decision only when that receiving use is compatible and the following content is recoverable:

| Evidence contribution | Required boundary |
| --- | --- |
| source decision | C.11.MV subject and status, receiving practice, domain result, situation family, alternative set, qualification window, and action considered. |
| evidence | Observations and credible estimates distinguished per alternative, with their sources, domain consequences, burdens, capability and System demands, side effects, opportunity costs, reversibility, reach and gaps. Actual Work, performers and direct relations retain their independently supported basis wherever claimed. |
| supported statement | The smallest situated worth statement that bears on the receiving Method-repertoire decision. |
| non-transfer | No transfer of the C.11.MV `keep`/`revise`/`replace`/`branch`/`stop` action, implementation authority, universal Method rank, causal claim, or evidence outside the stated source-use conditions. |
| reopen | Changed Method or candidate status, situation in the receiving practice, alternatives, evidence, capability or platform conditions, direct relations, or receiving repertoire use. |

The receiving practice remains responsible for its Method repertoire and compatibility claims. The contribution supplies evidence for that decision; it does not direct the recipient to take the C.11.MV action.

