---
chunk_kind: "child"
pattern_id: "A.10.1"
pattern_title: "Revalidate Affected Uses When a Relied-on Source Changes"
section_id: "A.10.1:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10.1/A.10.1__005_solution.md"
commit_sha: "886e84cadcc302e1c622aec02a0a0ba1e1c3955d"
heading_path:
  - "A.10.1 — Revalidate Affected Uses When a Relied-on Source Changes"
  - "A.10.1:4 — Solution"
line_start: 23136
line_end: 23275
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.11"
  - "B.3"
  - "C.2.1"
  - "E.15"
  - "G.11"
  - "G.6"
keywords:
---

### A.10.1:4 - Solution

Use the outline in 4.1 to locate the current move; sections 4.2–4.7 give its comparison criteria, fields, and stop conditions.

#### A.10.1:4.1 - Perform the Nine-Step Move

1. **Start from the changed source, not a presumed receiver.** Name the predecessor and later or replacement source epistemes, the claim set whose change may matter, and the present question that bounds the search. Leave source identity, edition continuity, access, or applicability unresolved when the required fact is missing.
2. **Compare claims rather than files.** Separate changes in proposition, subject, scope, applicability, assumptions, limits, evidence status, and effective conditions from wording, layout, publication, carrier, and revision-label changes. If comparison establishes compatible meaning, applicability and access, finish with any needed reference repair. If comparison cannot establish them, return the material gap; neither branch requires a multi-use search merely to record its stop.
3. **Select a receiving-use search frame.** Use the search-frame fields in 4.3 to state where a receiving use would count for the present question.
4. **State reproducible discovery coverage.** Name the exact source identifiers, claim addresses and aliases used; the included search surfaces; the source-outward and receiver-oriented routes; and every unsearched, inaccessible, stale, unindexed, or identity-ambiguous surface.
5. **Discover and then name candidate receiving uses.** Use search, citations, lineage, traces, indexes, owner knowledge, or tools to find candidates. Inspect the receiving content and recover the exact premise, evidence-use, operation-argument, specification, decision-basis, or other direct relation. Discovery alone establishes no reliance.
6. **Classify and bound reach.** Distinguish actual dependence, irrelevant mentions and unresolved uses within the searched frame. Group equivalent irrelevant mentions when one inspected reason covers them. Retain the direct-use basis and gaps that can change the receiving conclusion, without a separate exclusion record for each mention. Follow a `depends` branch only through another exact use relation while a receiving action can change. Supply the discovery-and-reach content needed by each subject judgment.
7. **Apply the direct subject pattern's guidance.** Use the discovery-and-reach statement to apply that guidance to the changed claim, exact direct use, current conditions, affected reach, coverage limits, and material subject facts. The practitioner or admitted System carrying out that application may find that the proposed dependence must be narrowed or rejected or that stronger evidence is required. Use adequate existing evidence and return the supported subject result or its scoped blocker directly to its existing consumers. Further inquiry is selected for the receiving question; a discovery gap alone does not commission Work.
8. **Supply a common account when a receiver needs it.** A sufficient direct subject result can finish the use. If another receiving question needs an overview, cite the independently governed results and summarize only the consequences it needs. That summary neither replaces those results nor changes `A.10 RelianceDisposition`.
9. **Stop at the completed receiving answer.** Apply the branch conditions in 4.7. Preserve the coverage and direct-use basis needed for the conclusion actually returned, including material gaps. Name a next actor or reopen observation when the receiving use needs that continuation. An unresolved independent branch need not delay a completed one.

This numbered presentation is an `A.22.CGUS` learning unfolding, not a lifecycle and not a mandatory sequence of `U.Work`. Discovery, source recovery, subject inquiry, and communication may overlap. Only the information dependencies in the move impose order.

#### A.10.1:4.2 - Compare the Source at Claim Size

Recover each source as a `C.2.1` episteme: a claim-bearing informational object, not its file or display. Name the predecessor and later or replacement episteme, their relevant claim addresses, subjects, interpretation bases, effective conditions, and edition relation when that relation is established.

Treat a difference as material here only when it can alter a receiving action or result. Useful comparison dimensions are:

| Comparison dimension | Question |
| --- | --- |
| Proposition or result | Does the later source state a different fact, value, rule, or result? |
| Subject and scope | Does the claim now concern a different entity, population, configuration, jurisdiction, interval, or use? |
| Applicability and assumptions | Did an entry condition, premise, model assumption, or interpretation basis change? |
| Limits and uncertainty | Did a supported range, exclusion, uncertainty, evidence status, or unsupported use change? |
| Effective conditions | Did an effective date, validity window, revocation, supersession, or conditional branch change? |

Wording can change without meaning changing; one word can also reverse an obligation. A text diff is a locator, not the semantic verdict.

If the same source episteme is merely republished on a new carrier, update the governed identity, publication, representation, availability, or one-use reliance facts through `C.2.1`, `E.17`, `E.24.PUB`, and `A.10` as applicable. Do not open the several-use search unless availability itself changes the bounded reliance question.

#### A.10.1:4.3 - Bound the Search Frame and Make Coverage Reproducible

These fields apply when affected-use discovery is selected. Set the frame before treating found candidates as the universe. Keep it in the existing result or working source at the detail needed to interpret the search. A harmless reference repair opens none of these fields. A claim of no impact across a frame does require adequate coverage and support for that frame.

| Search-frame field | Minimum useful content |
| --- | --- |
| Present question | The decision, result, release, account, or other use for which impact matters now. |
| Organizational and product boundary | Named project, product, portfolio, organization, or other working boundary. |
| Receiving families | Decision, result, model, specification, plan, account, procedure, or other families in which a use would count. |
| Conditions | Configurations, jurisdictions, populations, situations, intervals, horizons, or editions that bound applicability. |
| Discovery surfaces | Repositories, registers, model stores, data catalogues, decision records, account stores, owner-held sources, and other included locations. |
| Owners and access | Responsible contacts, access limits, and any surface whose owner or identity is unresolved. |
| Explicit exclusions | The boundary and exclusion reasons needed to delimit this question. Group equivalent exclusions; do not enumerate every non-receiving product, period or mention. |

Coverage is adequate only relative to that frame. Use complementary routes:

- **Source-outward discovery** starts from exact source identifiers, claim addresses, aliases, citations, backlinks, provenance, data or model lineage, declared traces, and transformations.
- **Receiver-oriented discovery** inspects the included receiving families for the same or an equivalent premise, limit, parameter, assumption, evidence use, or decision basis, even when the source identifier is absent.

One justified complete index may cover both directions. Otherwise state both routes and their limits. For every surface, record the query or inspection basis, the source identifiers and aliases used, the date or source value inspected when it matters, and the result or gap. An unsearched, inaccessible, stale, unindexed, or identity-ambiguous surface is a discovery-coverage gap. Outside the covered surface, a use is `not found`, not established unaffected.

#### A.10.1:4.4 - Confirm Direct Reliance Before Following Reach

Search output supplies candidates. The receiving content supplies the reliance test.

| Discovery disposition | Use it when | What follows |
| --- | --- | --- |
| `depends` | The receiving action, interpretation, condition, result, check, specification, or public reference uses the changed claim through an exact direct relation and could change if that claim changes. | Include the use in affected reach and prepare a discovery-and-reach statement for application of its direct subject-pattern guidance. |
| `mentions only` | The content cites, lists, stores, describes, or sits near the source, but its current action or result does not use the changed claim. | Exclude it from affected reach. Group equivalent irrelevant mentions and retain a short reason in the existing result when its receiver needs it; no separate certificate is required. |
| `unresolved` | The premise, equivalent claim, applicability, direct relation, receiving content, or necessary access cannot yet be recovered or contested dependence remains. | Name the missing fact or owner. Continue independent resolved branches, but do not classify this candidate as unaffected. |

These discovery dispositions answer whether a found candidate belongs in the affected branch. They are not `A.10 RelianceDisposition` values. Use `A.10` to judge whether one bounded evidence use passes, degrades, abstains, reopens, needs evidence or assurance, or is blocked for current use.

A citation, a present or missing trace, storage, indexing, carrier co-location, succession, ownership, declared dependency, graph reachability, or a shared keyword does not establish `depends`. A missing trace may be a discovery or coverage gap; it is not impact and it does not prove no impact. Conversely, an undeclared use can `depend` when the receiving content actually uses an equivalent premise.

Follow a `depends` branch only through another exact direct use relation. Stop before a downstream item whose action, condition, result, or required check cannot change. The affected reach is the smallest dependency-closed structure that contains every in-frame use that can change an action; it is not every transitively reachable node.

For a branch that needs subject judgment, supply the following discovery-and-reach content at the detail required by its receiver. It may already be present in the direct result; no second statement is needed:

| Position | Required content |
| --- | --- |
| Source change | Predecessor and later or replacement epistemes; exact material claim difference; unresolved identity, edition, or applicability facts. |
| Search and coverage | Present question, bounded frame, included surfaces, source-outward and receiver-oriented routes, explicit exclusions, and known gaps. |
| Direct use | Named receiving result or action, exact premise or other direct use relation, current conditions, and the evidence for `depends`. |
| Reach and stop | Further exact receiving uses followed, last action that can change, `mentions only` and `unresolved` candidates relevant to the branch, and the stop reason. |
| Subject application and result | The direct subject pattern to apply, its needed current inputs, the independently governed subject result to obtain, and the existing consumer that should receive that result. |

The statement is usable claim content for that subject judgment, not a new mandatory carrier or universal record. A table, list, matrix, or optional `G.6` path slice may present it; the representation establishes none of its relations.

#### A.10.1:4.5 - Apply Direct Subject Guidance and Keep the Result Independent

Discovery and reach classification prepare the branch for subject judgment. A practitioner or admitted System applies the direct subject pattern's concrete rule or test to each `depends` branch. Recover or recheck facts about current conditions, evidence, authority, cost, and Work only where those facts can change the independently governed result.

| Live question | Governing contribution to apply |
| --- | --- |
| Source and claim identity | `C.2.1` |
| One bounded evidence or source reliance use | `A.10` |
| Truth claim or measurement, formal, causal, diagnostic, conformance, comparison, or acceptance result | The direct definition or test: `C.16` for measurement, `C.28` for causal support, `A.19.CPM` for comparison of admitted CHR profiles under an explicit comparator, `A.19.SelectorMechanism` for selection from admitted candidates under explicit criteria after comparison, `G.4` for an acceptance-clause application, and the applicable truth, formal, diagnostic, or conformance pattern. |
| Choice or decision | `C.11` or the applicable subject decision pattern |
| Assurance | `B.3`, only when an actual named assurance claim is current |
| Authority, responsibility, commitment, permission, gate, or release | The direct authority, commitment, permission, gate, or release pattern |
| Currentness and refresh planning | `G.11` |
| Planned or performed Work and actual bindings | `A.15.2` for the applicable `U.WorkPlan` and `PlanItem` structure; `A.13` and `A.15.1` for precise performers and independently admitted dated Work; `A.6.1` for actual bindings |
| FPF pattern-edition continuity | `E.15` |

A practitioner or admitted System may, by applying the direct subject rule or test, narrow or reject the proposed affected reach. Keep the independently obtained result on its existing direct route: the engineering source-change result governed by `SYSE.19` goes to `SYSE.14`; revision feedback governed by `FIN.17` goes to `FIN.4`; and the assumption-impact result governed by `STR.2` goes to `STR.3` and `STR.4`.

When a common account is needed, it cites independently governed subject results and is never their own input. The information dependency is:

> material source change → needed discovery and reach → application of direct subject guidance → independently governed subject result → common account, if a further receiving use needs it

#### A.10.1:4.6 - Complete the Affected-Use Revalidation Account

Prepare a common account only when a receiving question needs an overview beyond the sufficient direct results. Cite each independently governed result used by that overview. A repaired reference or a direct subject result can close its own question without this account. When durability or reliance requires an episteme, ordinary `C.2.1` content is sufficient.

| Account position | Content when needed for this receiving question |
| --- | --- |
| Source comparison | Source epistemes, relevant claim addresses and material change or gap. Include publication, carrier and access distinctions when they affect the conclusion. |
| Search frame and coverage | The question, boundary, discovery basis and material limits of a search actually performed. Preserve enough to judge any no-impact claim at its stated scope. |
| Candidate uses | Direct-use bases for affected branches and unresolved candidates that limit the conclusion. Equivalent irrelevant mentions may share one short exclusion reason. |
| Action-changing reach | The dependent branch, last action that can change and why reach stops there. |
| Subject applications and results | The subject result and its governing contribution, with the conditions and existing receiver material to this overview. |
| Local summaries | The supported use consequences that the receiver needs, with the cited subject basis. |
| Reuse and continuation | Earlier values and inspected independent results needed for reuse; material gaps and any continuation or reopen condition the receiving use needs. |

`Preserved`, `narrowed`, `reopened`, `superseded`, `reliance withdrawn`, and `blocked` are local prose summaries, not a universal status vocabulary. When they summarize subject judgments, they require those judgments' basis. They replace neither `RelianceDisposition` nor assurance, permission, authority, release or decision.

Keep earlier source editions and prior results recoverable for their original uses and conditions. A later source does not rewrite what an earlier source meant. Reuse a prior result only when its conclusion and conditions remain current and the changed claim lies outside its actual dependency.

#### A.10.1:4.7 - Stop, Return Gaps, and Reopen Locally

Close the branch that answers the present question:

| Branch taken | Sufficient completion |
| --- | --- |
| Compatible meaning, applicability and access; only a reference or carrier changed | Complete the needed reference repair. No affected-use search, separate subject-result record or common account follows merely to certify that stop. |
| A claim of no impact within a receiving-use frame | Supply a bounded frame, adequate discovery coverage and the actual-use basis supporting that claim. Equivalent irrelevant mentions may be grouped. Missing coverage limits the claim; absence of a search hit alone does not establish no impact. |
| Affected uses need subject judgment | Return their independently governed supported results or scoped blockers with the direct dependence, action-changing reach and material coverage limits. Finish independent resolved branches. A common summary follows only when its receiver needs it. |
| Comparison, dependence, access or subject qualification remains unresolved | Return the exact gap and its effect on current use. Preserve independently supported results. Name further Work only when it is needed and selected for the receiving question. |

Retain the history and reasoning needed to reuse the result. State who must receive an unresolved action question or what would reopen a continuing use when that information changes practice; a completed small repair need not create a monitoring arrangement.

An inaccessible or unsearched surface is not established unaffected. Reopen locally when a source, claim, direct relation, included surface, subject result or applicability condition changes enough to affect the current conclusion. Use `A.15.9` and `C.11.DUA` when further acquisition is considered; attainable contribution and whole burden govern its selection without weakening support or authority conditions.

