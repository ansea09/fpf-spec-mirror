---
chunk_kind: "child"
pattern_id: "C.32.P2S"
pattern_title: "Problem-to-Structure Architecturing Unfolding"
section_id: "C.32.P2S:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.P2S/C.32.P2S__006_archetypal-grounding.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.32.P2S — Problem-to-Structure Architecturing Unfolding"
  - "C.32.P2S:5 — Archetypal Grounding"
line_start: 81374
line_end: 81417
dependencies:
  - "A.1"
  - "A.1.SCR"
  - "A.1.STM"
  - "A.15.6"
  - "A.22"
  - "C.22.2"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.31"
  - "C.32"
  - "C.33"
  - "C.35"
  - "E.17"
  - "E.24.PUB"
keywords:
---

### C.32.P2S:5 - Archetypal Grounding

Carry the outside need through to what the commission requires. An explanation may establish how existing relations produce the relevant property. A design shows how the proposed relations would do so. For installation, establish the work agreed with the recipient, including qualification when it belongs to acceptance. For a capability, establish what the participants can now do under the agreed conditions. When the commission calls for use to start, continue or cease, establish the required start, continuation or cessation in practice. An actual transformation has its own `A.3.4` basis.

**A throughput shortfall after a layout change.** A plant architect finds that a production cell delivered fewer accepted units per shift than the layout design predicted. The count establishes the shortfall for the observed shifts. It leaves open whether a buffer was installed on a different route, the input mix changed or the cell spent longer waiting for release. Identify which of those differences would change the proposed action.

The approved layout requires output from station B to bypass the shared fixture. Inspection shows that B's conveyor actually feeds the fixture. This establishes a discrepancy in the installed connection. The architect can call for conformity to the approved layout where that decision is binding. To claim that rerouting will restore the missing output, trace which operations waited for the fixture and what would still limit accepted output after the change. If inspection instead confirms the bypass, keep the throughput shortfall and investigate the constraint that remains.

A short P2S account can therefore record a production-cell performance question first. Record `actualStructureDivergesFromExpectedStructure` for the inspected conveyor once its actual connection has been compared with the binding layout. Keep the shift data and any still unidentified bottleneck separately recoverable. Use C.32 to develop changes to the connections implicated in the shortfall. The output record alone supplies no particular buffer design.

**Lens-use slice.** If the plant team builds a DSM or epiplexity-style model over stations, buffers and routing events, P2S retains the architecture inference and its grounds: the dependency or learnable structural content preserved, any consequential flow distinction omitted, and the structures the result can inform. Use C.29 when choosing or transferring that representation, or relying on its result, remains unresolved; an adequate domain treatment needs no additional lens account. Establish any architecture-adequacy, eval or decision conclusion separately.

**Built asset and technical system.** A clinic has rising instrument-turnaround delays and infection-control pressure. The first P2S move does not ask for a better diagram. It names the clinic service system as described holon, the turnaround-and-contamination architecture question, intended operating use, applicable scope and window, candidate structure kinds, architecture characteristics, and uncertainty: room layout, sterile and contaminated flows, equipment modules, tray interface, maintenance work, throughput, contamination isolation, maintainability, and surge adaptability.

Candidate synthesis develops these alternatives: a centralized autoclave bay, distributed sterilization modules, and a reusable tray-interface change. Use `C.32.PAD` for the decision selecting one configuration, `C.30.AD` and `C.32.ADR` for its descriptions and publication, and A.15-family patterns for construction and operating work.

During operation, measure turnaround, contamination events, maintenance burden, and actual-structure feedback triggers.

**Method, organization and Work.** Inspection work catches ontological errors late. Recover what the source's "review practice" names before choosing the described holon. When the question concerns how source recovery, judgement and repair connect, the bearer can be the Method itself under A.3.1; candidate alternatives can change that sequence or its feedback.

When staffing or coordination among performers is the problem, recover the review organization-as-system and its relevant structures.

If a performed review is the subject, recover each performer through A.13 and identify the `U.Work` occurrence independently through A.15.1.

Use `C.32.HCS` and `C.32.ACS` to bind characteristics to the bearer recovered for the question and the required result. Use `E.10.ROLE` to separate any local checker kind, classification, current assignment, direct review-relation position, function claim, organization position, and ordinary audience label. Candidate synthesis develops modal alternatives. Establish any claimed actual subject relations independently. For later actual inspection Work, add F.6 only when the flow or receiving use expressly represents precise assignment-bound attribution. Compare the phase at which the same kinds of errors become detectable under each arrangement. Records of detection can establish when particular errors were found. A rise in recorded early findings may also reflect more errors in the incoming material or a change in recording.

**Architecture-influence and transformed-side co-synthesis.** A team wants a modular product architecture but its toolchain, team communication, release method, and evidence workflow only support one tightly coupled build. The team uses `C.32.CONWAY` within the P2S flow: those typed influence sources and their direct relations remain separate from both C.30 architecture sides, the changed referent, any actual transformation, acting Systems, assignments, and Work.

Candidate families include changing the product modules only, changing the influence-source structures only, changing both, or accepting a bounded mismatch while retaining a named correspondence-frame return condition. The decision states which side changes now, what architecture characteristics are protected, what Work and work-to-change relations realize the change, and what operation or delivery feedback can return to the `C.32.CONWAY` correspondence frame or to decision repair.

**PumpSkid 7 realization and return.** Architecture pressure calls for a modular pump-skid with selected module and placement structures; use `C.32.PAD` for the project architecture decision.

Assembly work `W-PS7-ASSEMBLY` and later commissioning work `W-PS7-COMMISSION` are separate Work occurrences admitted under `U.Work` by `A.15.1`. Mounting change `T-PS7-MOUNT`, wiring change `T-PS7-WIRE`, fluid-connection change `T-PS7-CONNECT`, and commissioning-related change `T-PS7-COMMISSION` are each independently identified under `A.3.4`. Where the assembly or commissioning work is asserted to cause a change, cite the work-to-change relation and its declared predicate. Shared work, temporal adjacency, and one selected pump-skid configuration do not establish one composite transformation.

The local `A.15.PROD` entity-identity-inception claim uses the applicable PumpSkid 7 identity-specification edition, its applicability basis, work-to-change and change-to-identity facts, and `inceptionBoundary`; it need not assert a composite transformation. Later commissioning can remain production work until subject-state facts at `completionBoundary` satisfy the applicable production-completion-criterion edition; only then can a separate historically indexed completion claim be written.

A later `C.30.AD` or `C.30.ASV` record describes the actual structure; use `C.32.ACE` to evaluate service-access coupling. When coupling is worse than the selected expectation, the eval result returns to decision repair or new synthesis. Neither the description, evaluation, identity-inception claim, completion claim, nor shared assembly work proves conformance to the selected architecture or transformation composition.

**Workshop capability with finite acceptance.** A workshop-development project must enable the delivery of machined components with an agreed surface finish under the expected order flow. The workshop and receiving organizations have agreed supply and acceptance obligations for those components. The components are the SoIs of their extended enterprise; the workshop is the architectural subject. One candidate adds a machine, another combines that machine with a revised production Method, qualified operators, suitable measurement and secured material access, and a third obtains suitable external machining. The architect compares their actual capacity, handovers, cost and provision conditions.

A machine-only candidate cannot establish the workshop capability while the measurement Method or skilled operator is absent. A bounded acquisition project may still deliver and accept the machine. For the capability project, choose a supported combination or a bounded investigation of the unresolved fit; carry that distinction to PAD.

Acceptance can demonstrate the agreed production capability under representative conditions without waiting for every future component to operate. Later use can reopen the product or capability hypothesis without erasing completed acquisition Work.

