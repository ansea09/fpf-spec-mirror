---
chunk_kind: "child"
pattern_id: "C.39.WA"
pattern_title: "Develop an Account of the Whole Subject"
section_id: "C.39.WA:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.39.WA/C.39.WA__006_archetypal-grounding.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.39.WA — Develop an Account of the Whole Subject"
  - "C.39.WA:5 — Archetypal Grounding"
line_start: 82901
line_end: 82958
dependencies:
  - "C.20"
  - "C.39.QR"
  - "C.41"
  - "E.8"
keywords:
---

### C.39.WA:5 - Archetypal Grounding

The following constructed cases expose different transitions in the Method. Their purpose is to make the common operation and its returns inspectable.

#### C.39.WA:5.1 - Mathematics replaced by a multiplication

The request is to explain mathematics and judge the completeness of the account. The submitted text is “2 × 2 = 4.” The reviewer establishes that the equality is true and concerns mathematics, then accepts the request as completed.

Recovering the subject immediately changes the judgement. The submitted text explains at most a particular calculation. An account of the field needs a chosen depth and reader, but it must develop mathematical objects and questions, ways of constructing and proving, and relevant relations among its branches. The precise breadth of a future overview remains a design question; the absence of that account in the submitted equality is already apparent.

The wrong inference joins two different relations: the statement's membership in the field and the account's adequacy for the requested subject. Retain the valid calculation as a possible illustration. Return the missing field explanation to authorship.

Suppose the author next provides ten correct calculations. This supplies more instances of calculation. Their contribution to the field account depends on an explained organization: what questions the operations answer, which structures and rules support them, how proof and construction differ, and how the selected branches connect. Diversity of examples can support that explanation while its organizing claims still require their own grounds.

The approving coordinator repeats the comparison with the original question. The previous reviewer has supplied a local truth judgement. Acceptance of the requested account remains unsupported until its substantive construction is provided and assessed.

#### C.39.WA:5.2 - Rebuild an explanation around the conditions of recovery

A technical author is asked to explain how a specified service design can resume within 60 seconds of a primary-server interruption while preserving acknowledged updates. The reader must be able to assess the proposed recovery and revise that assessment when the time requirement changes. The available draft describes the primary and backup servers and reports a successful backup start-up test.

The author first tries to order the account by those components. Returning to the reader's question reveals what that order leaves unexplained: how the acknowledged state reaches the new writer, and when clients may safely use it. The design supplies three relevant facts: acknowledgement follows replication of the log entry; the old writer's authority is removed before the backup receives authority; the client route opens after restoration of the required state. The author connects these facts through the conditions that each transition needs and produces. This gives the account its organization: preservation of acknowledged state, transfer of authority, and restoration of usable service.

That organization changes the text. The replication rule moves next to the claim about preserved updates, where it supplies the claim's premise. Authority transfer is explained between detection and recovery by the new writer. The start-up test stays with the narrower claim it supports. The new connecting explanation tells the reader why an available process, correct state and permission to write must coincide before the service can resume. A list of servers could not explain that coincidence.

The author then develops the timing paragraph from the same dependencies. In this constructed design, supported upper bounds are 8 seconds for detection, 12 for authority transfer, 15 for restoration and 5 for opening the route. The specified sequential order warrants a 40-second upper bound. The text attaches the conclusion to that order and to the replication, authority and timing premises. A reviewer can now follow both questions in the commission: what preserves the acknowledged updates, and what supports the recovery bound. A missing deployment test remains identifiable as a missing premise rather than disappearing behind the successful start-up test.

A new requirement of 30 seconds changes the author's comparison. Forty seconds no longer supports it, while the upper bound alone leaves the original design's actual feasibility unresolved. The author obtains the designers' alternative: maintained warm state reduces the restoration bound to 4 seconds, with continuous compute and state-maintenance provision. The account is revised at the affected join: 29 seconds is supported under the new provision, and the state and authority explanation now includes that provision's role. Detection's established bound is retained. If the provision is unavailable, the explanation exposes the unresolved timing or support question for the designers; it does not invent a completed service.

The revision follows the account's organizing grounds. It changes the premises, connection and qualified claim that depend on restoration, while preserving the still-supported contributions. This is the author's construction the reader can reuse when another whole-subject account consists of accurate component descriptions with its decisive relations missing.

#### C.39.WA:5.3 - Build a disciplinary account through knowledge and practice

An author is preparing the common entry to an operations-management guide. Its reader needs to choose and revise ways of obtaining continuing production or service under competing demands and changing conditions. The supplied chapters explain admission of work, capacity allocation, development of operating methods and review of results. The initial entry groups them by department. That arrangement helps locate a chapter but leaves the reader to discover why a finding in one chapter changes work in another.

The author recovers the field question and reads the knowledge–practice connections in OPS.Reference:1.1–1.6. Two different grounds in the source are particularly consequential. With a consistently identified work population, opening unfinished work plus entries minus exits gives closing unfinished work. A completion forecast additionally depends on premises about capacity, work mix, variability and dependencies. The author uses this difference to construct the entry's organizing explanation: operating knowledge both constrains the arrangement and supplies revisable grounds for anticipating its results; performed work can reveal errors in the account, failed premises or a need for a different Method.

This explanation reorganizes the connections among the four chapters. Admission and allocation now return a jointly supportable arrangement. Review compares its predicted and observed consequences, identifies which ground is affected, and returns that question either to the operating account, to provision or to development of the Method. The author writes the reasons for those different returns alongside the connection. An arithmetic discrepancy requires recovering the event account; a defeated forecast premise requires revising the forecast or arrangement. The shared field question holds these contributions together while their different grounds explain why they remain distinct Methods.

To check whether this connection is actually available in the guide, the reviewer follows a supplied report of growing unfinished work. The report counts only items awaiting technicians and explains delay by technician capacity. Completion also requires specialist approval. The author recovers that omitted transition and revises the account's work population and exit condition. The guide's diagnosis paragraph now explains how more technician output can increase the approval queue, and directs the reader to establish the approval contribution or revise admission. These details are needed to show the author's repair: changing the represented operating unit changes the explanation and the Method choice together.

A second supplied situation concerns readiness for an unknown future incident. The initial entry treats every operating result as an item that can be completed and stored. The author discovers that this common assumption cannot organize the readiness chapters: the required capability must remain available during the covered interval. The entry is revised to explain the relation between receiving result, operating unit and commitment. Its production branch follows completed items; its readiness branch follows maintained availability. Their shared principles concern obtaining usable results under joint conditions, while their different objects select different operating Methods.

The completed entry contains that field explanation and the connections at the four chapter entrances. The reviewer reads those actual connections against the original commission, including how a changed knowledge claim returns to practice and how a practice finding revises knowledge. The guide now supplies the joins that its departmental outline had left to the reader. Further chapters receive their own place through the same field question and their actual knowledge–practice relations.

#### C.39.WA:5.4 - Organize a theoretical account by the questions its structures answer

A mathematics author is commissioned to explain finite-dimensional linear maps to readers who can solve elementary linear equations. The account must connect maps, equations and matrix calculations so that readers can reason about existence and uniqueness of solutions. This scope is part of the commission. The available notes define a map, introduce a matrix, and then present successful calculations in that order.

The author recovers what must be explained before choosing a more elaborate calculation. Two questions organize the subject: which outputs can a map attain, and which inputs it treats alike? In the standard theory, the image answers the first question. Linearity gives the second a common construction: \(T(x)=T(y)\) exactly when \(x-y\) lies in the kernel. Consequently, \(T(x)=b\) is solvable when \(b\) is in the image; after one solution \(x_0\) is found, all solutions have the form \(x_0+k\) with \(k\) in the kernel. The [UCL account of linear maps](https://www.homepages.ucl.ac.uk/~ucahmto/0007_2021/3-3-linear-maps.html) supplies the definitions and structural grounds.

These relations give the author a reason to change the exposition. The new opening states the two questions and derives their connection through linearity. The kernel and image definitions now perform identifiable explanatory work. A solved equation is placed after the solution-set construction, so the reader can see which features of that calculation arise from the common relation. The matrix section explains how selected bases represent the map and make calculation possible. A change of basis can change the matrix while retaining the map and the two structural questions.

The reviewer then examines a transition the draft had left implicit: the claim that a map reaches every output. Two maps can have the formula \(T(x,y)=(x,0)\) and different codomains. With codomain \(\mathbb{R}^2\), some outputs are unattainable; with the first coordinate axis as codomain, every allowed output is attained. The formula alone leaves this judgement underdetermined. The author repairs the general explanation by including the declared codomain in the attainable-output question, and updates the affected statements and examples. The kernel argument remains valid. This local finding has changed the common account and selected its dependent revisions.

The reviewer returns to the commissioned use. Existence is explained through image membership; freedom among solutions through the kernel; matrix computation through the chosen representation. The text now gives their connecting grounds before asking the reader to interpret particular calculations. These grounds also let the author select useful contrasts: a different codomain tests the scope of the attainable-output claim, whereas changing only a matrix entry may exercise the same calculation again.

Here the whole account is organized by mathematical structures and justified implications. The author obtained that organization from the questions and theory, used it to choose and arrange the parts, then revised it when a particular judgement exposed a missing participant.

