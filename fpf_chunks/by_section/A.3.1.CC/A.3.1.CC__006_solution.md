---
chunk_kind: "child"
pattern_id: "A.3.1.CC"
pattern_title: "Check the Coherence of a Method Claim"
section_id: "A.3.1.CC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1.CC/A.3.1.CC__006_solution.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "A.3.1.CC — Check the Coherence of a Method Claim"
  - "A.3.1.CC:4 — Solution"
line_start: 10527
line_end: 10593
dependencies:
  - "A.10"
  - "A.15.8.MS"
  - "A.3.1"
  - "A.3.2"
  - "C.37"
keywords:
---

### A.3.1.CC:4 - Solution

This is a claim-to-basis comparison for Methods, descriptions, representations and support. Use A.10 for the relied-on evidence and each subject pattern for its positive claim. The local construction below identifies the consequential contradiction or missing basis and returns it to the maintained explanation that can be corrected.

Check one claim relied on for the named use against its declared basis, classify the result, and return any correction only to the maintained result that owns the defeated claim. Recheck the repaired claim while preserving every unaffected status and open question.

When the parts appear locally consistent but the required whole result still has no adequate explanation, use `B.1.5.EW:4.3–4.5` to work back from that result to the constituent contributions and their connections. That supplier covers actual work and proposals for future work; it can expose a required operation or connection whose account is missing. Bring the particular contribution, dependency and supporting basis into step 1 below. Then distinguish a missing construction, an omitted description and an unsupported claim before choosing a correction owner. Agreement among the available parts alone does not settle the whole-result question.

#### A.3.1.CC:4.1 - Pattern-Use Unfolding

Use steps 4–8 only for the claims and evidence that the named coherence question depends on.

1. **Name the blocked use and possible contradiction.** Identify the reader or decision, the claim needed, its qualification window, and what would count as agreement, contradiction, missing information, or a stop. Do not begin with “verify the Method”.
2. **Preserve the subject and status branch.** Identify the admitted Method under `A.3.1`, or keep the proposed whole as a candidate account. Keep Work, WorkPlan, description, representation, support, evidence, publication, and structure claims at their current statuses.
3. **Recover the maintained claim and owner.** Record the claim text or predicate, owning result, edition or occurrence, source or construction basis, intended use, and currentness condition. If ownership cannot be recovered, return `owner-not-recoverable` before editing several carriers.
4. **Check construction claims at B.1.5.CM.** Test construction requirements, component decisions, operation declarations, and obtaining-relation claims separately. Cite the governing FPF predicate where needed rather than recreating its admission test. A failed construction claim returns to that exact B.1.5.CM result.
5. **Check MethodDescription claims at A.3.2.DE.** Test coverage, internal consistency, correspondence with admitted Method claims, navigation for the named use, stated evidence limits, omissions, stops, and any declared description-side conformance. Do not make section count or scheme passage a proxy for useful coverage.
6. **Check representation-use results at the right owner.** For one action, recover its complete representation-use result under C.37 and stop without C.37.MP. For several unlike Method-related actions, recover the [complete C.37.MP profile](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c37mp42---record-the-result), including its shared source and separate cross-use result. Test the contradicted action's claim group and whether the profile relation still holds. The direct FPF governor owns view, mathematical-lens, publication, and structure conformance; if a governed result fails, return that lower result and reopen only the affected use result and cross-use relations that actually depended on it.
7. **Check support results at A.15.8.MS.** Use A.15.8.MS's result distinctions to locate the specific support claim contradicted by the evidence and the result that owns it. Return the repair there; one defeated claim is not a verdict on the whole support configuration.
8. **Use trial evidence to check the maintained claim.** From A.3.1.WT, recover the actual Work occurrence, performer, enacted admitted Method, situation, capability and support conditions, direct relations, result, burden, observation source, and evidence reach. Ask which named claim the observation bears on. A success or failure does not by itself identify the owner.
9. **Classify the finding.** Distinguish: `agreement-within-window`; `contradicted-claim`; `missing-information`; `failed-declared-conformance`; `stale-source-or-edition`; and `owner-not-recoverable`. Do not turn uncertainty into contradiction or a local defect into a whole-Method verdict.
10. **Select one correction owner.** Return the smallest correction to B.1.5.CM construction, A.3.2.DE description, one direct C.37 use row, one complete C.37.MP Method representation profile, one exact A.15.8.MS result, or the direct governor of a lower representation result. If one observation defeats several independent claims, create separate findings with separate owners; do not copy one vague correction into every upstream result.
11. **Repair and repeat the same check.** Preserve unaffected claims, statuses, evidence, and windows. Recheck the repaired claim against the same basis. If the use, subject, source, edition, or criteria changed, start a new coherence use instead of calling the old check passed.
12. **Return the bounded result.** State the verified claim, correction or gap, owner, affected downstream uses, preserved claims, material use limits, and reopen condition.

#### A.3.1.CC:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| coherence use | Blocked decision, reader, relied-on claim, qualification window, agreement and stop conditions. |
| subject status | Admitted Method or candidate account, plus separately identified Work, WorkPlan, description, representation, support, and evidence results in scope. |
| maintained claim | Claim or predicate, owner, edition or occurrence, source or construction basis, intended use, and currentness. |
| comparison basis | Construction requirement, description claim, selected representation rule, support premise, trial evidence, or declared conformance criterion actually used. |
| finding | Agreement, contradiction, missing information, failed declared conformance, stale source or edition, or missing owner; include the evidence reach. |
| repair routing | One maintained result to reconsider, smallest correction, unaffected claims and statuses, and downstream uses that must be rechecked. |
| rerun | Same-check result after repair, or the changed use or basis that requires a new check. |
| return | Verified bounded claim, corrected claim, or named gap; material use limits and reopen condition. |

Use the existing claim and finding records or a concise account that preserves these distinctions; the positions do not require a separate form.

#### A.3.1.CC:4.3 - What Changes in Practice

Teams stop repairing the nearest document or declaring the whole Method inconsistent. They can identify the defeated claim, distinguish construction from description, representation, support, and evidence, and send one correction to its maintained owner.

The correction becomes cheaper to review and safer to reuse. Unaffected claims keep their status, and later fit and worth judgments receive a precise repaired input rather than a package-wide confidence label.

#### A.3.1.CC:4.4 - Minimal Constructed Coherence Replay

Continue the constructed A.3.1.WT trial of admitted `M-Unit-Review-1`. Construction result `CCR-UR-1` states that unit identification and normalization precede tolerance comparison. MethodDescription edition 4 says the same and exposes the unresolved-mismatch stop.

Only one current action is at issue: `Reviewer-17` must use the flow representation to guide pre-release unit review. Direct use result `C37-UR-Flow-4` therefore takes the C.37 exit rather than opening C.37.MP. It returns to that Method and description edition, requires unit identification, normalization before tolerance comparison, the comparison branch, and the unresolved-mismatch stop, and uses governed representation result `REP-UR-Flow-4`.

Exact claim: that representation exposes those operations in order for the named review action. A.2.4 classifies the intended preparation use; A.10 path `P-UR-Flow-4` carries the current-edition premise with `RelianceDisposition=pass` for the review window. Receiving task criterion `UR-PreRelease-Guide-4` permits use only while those claims remain exposed. The row omits unrelated support-edition detail, preserves Method, description, representation, and Work status, is `select` for that action, and returns a missing exposure to the direct representation governor and this use row.

A.15.8.MS supplies the current conversion table used in `W-Disc-1`.

The trial evidence records that `Reviewer-17` normalized the Celsius/Kelvin values before comparison and stopped the release decision. Inspection of `REP-UR-Flow-4`, however, shows identification followed directly by tolerance comparison; the normalization operation is absent. The finding is not “the Method is incoherent”. The construction claim, description claim, support edition, and observed Work agree within this slice. The contradicted claim is the `C37-UR-Flow-4` exposure claim for its exact action; no C.37.MP profile exists or is needed for this one-use case.

Return `CORR-C37-UR-1`: revise governed representation result `REP-UR-Flow-4` and its direct use row to expose normalization and the unresolved-mismatch branch, or narrow the row's action, required claim, and omission account. Preserve `M-Unit-Review-1`, MethodDescription edition 4, `W-Disc-1`, its task result, and the conversion-table support result. Recheck the same exposure claim after repair. Do not infer fit or worth from the successful Work occurrence.

| If the observed defect were instead... | Owner to reconsider | Result not to change automatically |
| --- | --- | --- |
| The admitted construction omitted any normalization requirement while the named problem required one. | The exact B.1.5.CM construction or requirement result. | A.3.2.DE and every affected direct C.37 use row or complete C.37.MP profile until their own action claims and dependent cross-use relations are checked against the changed construction. |
| MethodDescription edition 4 reversed the declared operation order while construction and Work supported the original order. | The exact A.3.2.DE description claim and edition. | Method identity and the Work occurrence. |
| The retrieved conversion table used a stale scale while construction, description, and representation were correct. | The exact A.15.8.MS edition, retrieval, or named-user task result. | B.1.5.CM construction and every unaffected direct C.37 use row or complete C.37.MP profile. |
| The source cannot show which of those positions is wrong. | `owner-not-recoverable` with the missing comparison basis. | All maintained results until evidence distinguishes them. |

