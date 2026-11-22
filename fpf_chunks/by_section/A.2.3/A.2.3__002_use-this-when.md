---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent — Promised Outcomes and Acceptance Criteria"
section_id: "A.2.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__002_use-this-when.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "A.2.3 — U.PromiseContent — Promised Outcomes and Acceptance Criteria"
  - "A.2.3:0 — Use This When"
line_start: 5797
line_end: 5816
dependencies:
  - "A.2.2"
  - "A.2.8"
  - "A.6.C"
  - "A.6.P"
  - "E.10"
  - "F.12"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptance specification"
  - "access specification"
  - "claim scope"
  - "promise content"
  - "promised outcome"
  - "provider and consumer system-role kinds"
---

### A.2.3:0 - Use This When

Use this pattern when a project needs to state what is promised to a consumer before asking who is obligated, what work occurred, which system exposes access, or which evaluation method and A.10 evidence relations support a fulfilment assertion.

Typical moments:

- an SLA publication, service catalog, product offer, public API promise, utility offer, or government-service description contains a statement about what a consumer may rely on;
- a team says "the service" but might mean promise content, provider organization, API, access point, delivery system, method, ticket, or performed work;
- to judge fulfilment, apply the declared acceptance criteria to what the promise covers. For one delivery, examine its Work, outcome and any required delivery or acceptance relation. For a population or period, use records covering that population or state over the declared interval (§8.2). Establish a particular evaluation Work when the criterion requires that performance or the claim concerns it. Its operation result, any verdict episteme and A.10 evidence relations each have their own grounds;

**Primary EntityOfConcern.** The EntityOfConcern of this pattern is `U.PromiseContent`: a consumer-facing promise-content episteme. For each PromiseContent episteme, the exact C.2.1 EntityOfConcern is the A.2.3:4.1.1 `OutcomeSpec` episteme designated by `promisedOutcomeSpecRef`. Its claim graph states the promised outcome, any eligibility predicate, and acceptance claims; `accessSpec` separately describes the access method when that description is current.

**First useful move.** Write the promise content as a clause: what outcome is promised, under which effective `ReferenceScheme` and `U.ClaimScope`, who or what is eligible, how access is described when relevant, and what would count as satisfying the promise. For a service measure, derive the unit, eligible population and period from the promise before selecting delivery records. For a fulfilment assertion, name the evaluation Method and the supporting evidence epistemes and A.10 relations separately. Use `U.Commitment` only for an actual duty bearer after the applicable constitutive rule and its required instituting basis obtain.

**What goes wrong if missed.** The word "service" starts naming provider, API, method, ticket, work, department, and promise at once. Teams then judge work against an implicit promise, treat access systems as obligations, or count performed work without knowing which promised outcome it was meant to satisfy.

**What this buys.** One consumer-facing promise-content episteme with explicit outcome and acceptance claims. Each neighboring claim keeps its named `EntityOfConcern` and direct relation, defined or tested by its own pattern.

**Not this pattern when.** If the current `EntityOfConcern` is an individual deontic relation, use `A.2.8`; if it is performed delivery Work, use `A.15.1`; if service or access wording hides its concrete subject or direct relation, start with A.6.P:4.11a. A bearer or access-providing arrangement is only one possible recovered reading; code or another episteme, Method, Work occurrence, participation, promise, permission, status, and direct relations keep their own readings. Use A.1 or A.1.SCR only when a separate repaired claim depends on that entity being a system. If source agreement or SLA wording combines several objects, use `A.6.C` to unpack them.

