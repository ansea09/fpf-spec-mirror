---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__003_use-this-when.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:0 — Use This When"
line_start: 3015
line_end: 3034
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.3.1"
  - "A.3.2"
  - "A.6.8"
  - "A.6.C"
  - "E.10"
  - "F.12"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Scope"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
---

### A.2.3:0 - Use This When

Use this pattern when a project needs to state what is promised to a consumer before asking who is obligated, what work was done, which system exposes access, or how evidence will judge fulfilment.

Typical moments:

- an SLA, service catalog, product offer, public API promise, utility offer, or government service description says what a consumer may rely on;
- a team says "the service" but might mean promise content, provider organization, API, access point, delivery system, method, ticket, or performed work;
- a promise must be judged by acceptance criteria against work evidence, without turning the promise clause into the work or the system.

**Primary EntityOfConcern.** The EntityOfConcern is `U.PromiseContent`: a consumer-facing promise-content episteme that states promised outcome, access or eligibility, and acceptance criteria inside one bounded context.

**First useful move.** Write the promise content as a clause: what outcome is promised, who may use it, how access is described when relevant, and how fulfilment will be judged from work evidence. Then use `U.Commitment` only when an accountable subject is assigned to that content.

**What goes wrong if missed.** The word "service" starts naming provider, API, method, ticket, work, department, and promise at once. Teams then judge work against an implicit promise, treat access systems as obligations, or count performed work without knowing which promised outcome it was meant to satisfy.

**What this buys.** One consumer-facing promise-content episteme that can be linked to commitments, role assignments, access descriptions, work evidence, acceptance criteria, and outcome specs without collapsing those neighboring objects into one "service" bundle.

**Not this pattern when.** If the current EntityOfConcern is the accountable deontic relation, use `A.2.8`; if it is the performed delivery work, use `A.15.1`; if it is the access point or delivery system, use system and architecture patterns plus A.6.8 service wording repair; if it is contract-bundle unpacking, use `A.6.C`.

