---
chunk_kind: "child"
pattern_id: "A.6.3.CR"
pattern_title: "ConservativeRetextualization: EntityOfConcern-Preserving Textual Re-Expression"
section_id: "A.6.3.CR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CR/A.6.3.CR__006_archetypal-grounding.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "A.6.3.CR — ConservativeRetextualization: EntityOfConcern-Preserving Textual Re-Expression"
  - "A.6.3.CR:5 — Archetypal Grounding"
line_start: 19301
line_end: 19392
dependencies:
  - "A.15"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.7"
  - "B.5.2"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
keywords:
---

### A.6.3.CR:5 - Archetypal Grounding

#### A.6.3.CR:5.1 - Same-EntityOfConcern report rewrite
**Source note slice.** `Service S exceeded the latency threshold in the evening batch window. Trace T-44 and dashboard pin D-17 show the spike. Two low-confidence hypotheses remain open.`

**Published report slice.** `Evening-batch latency for Service S exceeded the threshold. Source pins: Trace T-44, Dashboard D-17. Low-confidence hypotheses are omitted here and remain in the pinned source note.`

For a reader reporting whether Service S exceeded the evening threshold, the rewrite preserves the occurrence, subject, time window and access to its grounds. If the reader must choose an investigation, the two competing hypotheses and their low confidence may change that choice. Include them or make them recoverable in time for the reader’s decision. Acknowledging the omission alone would leave that reader without the needed comparison.

#### A.6.3.CR:5.1.a - Ordinary inherited-pin summary
**Pinned source cluster.** `In this example, N-14 is the source note in §5.1; N-14, trace T-44, and dashboard card D-17 are already published together under one incident review bundle.`

**Published stand-up slice.** `Evening-batch latency exceeded the threshold for Service S. See N-14 / T-44 / D-17 for the pinned source cluster.`

For reporting the threshold exceedance, this short slice may inherit the published pins and omit the separate hypotheses because it asserts no cause. A causal decision would need the hypotheses and their qualifications from N-14. The source remains reachable to the reader.

#### A.6.3.CR:5.1.b - Benign omission that stays ordinary
**Source note slice.** `Service S exceeded the latency threshold in the evening batch window. Trace T-44 and dashboard pin D-17 show the spike. The note also lists two low-confidence hypotheses for separate investigation.`

**Published stand-up slice.** `Evening-batch latency for Service S exceeded the threshold. Source pins: T-44, D-17. Low-confidence hypotheses are omitted from this stand-up note and remain in the pinned source.`

This stays ordinary `ConservativeRetextualization` because the omission is declared, the same EntityOfConcern remains visible, and no separate narrower admissible use, non-admissible downstream use, or source-bearing return is needed to justify the omission. Ordinary omission alone is not controlled semantic coarsening.

#### A.6.3.CR:5.1.c - Functional-description textual summary

**Source note slice.** `The principle scheme says: choose method family MF-2 for small-batch mixing when material X remains below threshold T; selected method M-2 still requires work plan WP-17 and result measurement RM-4.`

**Published summary slice.** `For small-batch mixing, choose method family MF-2 when material X remains below T. Selected method M-2 still requires work plan WP-17 and result measurement RM-4.`

This remains `ConservativeRetextualization` because it restates the source's selection rule and preserves its planning and measurement requirements. The summary supports interpretation and source-finding. Keep WP-17 and RM-4 recoverable whenever they affect the stated interpretation, decision or performance; actual use must satisfy the applicable requirements.

A shorter summary used only to select a method family may omit requirements for performing the selected method when that omission does not mislead the reader about the summary's scope or make M-2 appear ready for execution.

If material loss is admissible only with a narrower use and return to the source, use `A.6.3.CSC Controlled Semantic Coarsening` with that narrower admissible use, forbidden stronger use, and source-bearing return. For stronger use, apply the governing requirement to the current facts; the CSC label or a reference alone does not satisfy it.

#### A.6.3.CR:5.1.d - Generated-summary source-relation variant

A generated summary follows the same source, EntityOfConcern and conservativity conditions as any other rewrite. A model-produced paragraph over an inspection or method-selection note is not an explanation merely because it was generated. Restated claims, material omissions and use conditions must be recoverable. Use the distinctions below when a source-use or support question affects reuse, citation or reliance.

| Source-relation question | CR-local meaning |
| --- | --- |
| source pointer present | The summary points to the source slice or source bundle it claims to restate. |
| source actually used | The inspectable source relation shows that the generation or rewrite actually used the named source, not merely a similar topic or remembered background. If that historical relation is unavailable, leave it unresolved and block only claims or uses that require it. Retain independently established claim support and uses whose own requirements are satisfied. |
| claim recoverable from source | Each summary assertion can be recovered from the source claims or admitted correspondence witness under the declared rule. |
| claim merely plausible | A sentence sounds likely but is not recoverable from the source. Do not present it as source-backed: retain only a justified source-finding or orientation pointer, or explicitly separate the unsupported proposition and repair it or handle it under the pattern for the new claim. |
| omission or loss | Relevant omitted qualifiers, alternatives, caveats, uncertainty, or conditions are visible enough for the admissible use. |
| claim widening | The summary does not turn possibility, hypothesis, bounded scope, or low-confidence wording into a wider commitment. |
| added linkage | New causal, bridge, comparison, work, gate, evidence, or explanation links are not introduced as if they were in the source. |

When the generated-summary case needs shared vocabulary, use only the `E.17:5.1b` source-relation or bounded-use distinction that changes the present use. Keep claim recoverability from the source separate from admissibility for that use, and an unknown relation separate from one known absent. The same source governs independent-verification claims and reopen conditions.

The summary may expose or cite the source slice it restates. It does not become that source slice by fluency, brevity, translation, layout, generated form, or reuse. If the needed source content, governing requirement, or case relation is missing, a repair request or source-gap note is only prospective: it neither establishes earlier source use nor supplies the missing claim support or use condition.

If the generated summary is source-pointer-only, merely plausible, claim-widened, or carrying added linkage, do not treat it as a conservative source-equivalent summary. For source-finding or orientation, retain only the justified pointer and separate any unsupported or new proposition from the source-backed account. Repair the claim against the source, or apply A.6.3.CSC, ExplanationFaithfulnessProfile, RepresentationTransition, E.17.ID.CR, A.15, A.10, or another pattern that defines, constrains, or tests the claim. An orientation or coarsening label alone does not make an unsupported claim source-faithful.

#### A.6.3.CR:5.2 - Same-EntityOfConcern rewrite via declared correspondence

**Source design slice.** `For configuration K at standard operating demand, CL-2 keeps the temperature at its return sensor in design band D-7.`

**Source safety slice.** `For configuration K at standard operating demand, HC-7 requires the temperature at monitoring point H to stay in safety band S-3.`

**Correspondence used.** CM-12 identifies H as the return sensor for configuration K and gives D-7 and S-3 the same limits, units and averaging interval for standard demand.

**Published joint-review slice.** `For configuration K at standard demand, the design claims to maintain the temperature required by HC-7 at the return sensor. CM-12 identifies the monitoring point and the temperature band used by the two accounts.`

The correspondence supports the stated overlap between a design claim and a safety requirement. An observation of actual operation would need its own basis. If CM-12 identifies only the sensor, report separately the band required by HC-7 and the band the design claims to maintain. Their relation remains to be established if the reader needs a conclusion about compliance.

#### A.6.3.CR:5.2.b - Cross-language re-expression without hidden bridge work
**Source slice.** `The backup controller stays in passive watch mode until the primary loop fails two consecutive heartbeat checks.`

**Published slice.** `Резервный контроллер остаётся в режиме пассивного наблюдения, пока основной контур не провалит две последовательные проверки heartbeat.`

**English reader gloss (comprehension aid only).** `The backup controller remains in passive observation mode until the primary loop fails two consecutive heartbeat checks.`

Russian *пока … не* uses a negative particle where English *until the primary loop fails* has none. In both versions the backup continues to watch until the primary has failed two checks in a row. Omitting the second failure or reversing the condition changes the event up to which passive watching is required. The gloss helps an English-only reader follow this difference. It is a comprehension aid, not a second source or verification of the Russian translation. A conservativity claim still requires suitable language competence or other evidence for the same-claim, same-EntityOfConcern, and hidden-bridge tests.

This remains in `ConservativeRetextualization` only if the translation is tethered to the same source claim, preserves the same EntityOfConcern, and adds no claim beyond the source. Apply F.9 only when a semantic Bridge between local senses or a proposed bounded use of that Bridge is claimed.

#### A.6.3.CR:5.2.c - Boundary to controlled coarsening
**Source slice.** `Vendor bulletin VB-7 requires rollback when pressure drift exceeds 2.5%, and it keeps two equipment-specific exceptions in the pinned annex.`

**Published coarsened slice.** `Pressure drift above 2.5% is a warning condition in the bulletin. Check the pinned bulletin and annex before treating the note as rollback guidance.`

This does **not** remain ordinary `ConservativeRetextualization`. The coarsened slice drops equipment-specific exceptions and remains only an orientation warning: it is not an executable rollback command. It is admissible only through narrower admissible use, non-admissible downstream use, and source-bearing return to the bulletin. Once that narrower-use boundary becomes primary, the case leaves ordinary same-entity rewrite and must use `A.6.3.CSC Controlled Semantic Coarsening`.

#### A.6.3.CR:5.3 - Boundary to explanation-facing renderings

A text is rewritten not mainly to restate the same source, but to explain why it matters, simplify reasoning for a learner, or narrate a mechanism. That move should leave `ConservativeRetextualization` and be reviewed under `ExplanationFaithfulnessProfile`.

#### A.6.3.CR:5.4 - Boundary to representation transition
A reader can need the same events aligned by component to compare recurrences. The event descriptions can stay in the same language while their arrangement makes that comparison practical. A change of representation language can also make an operation possible. Use `RepresentationTransition` when that change is the point of the work.

