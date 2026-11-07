---
chunk_kind: "child"
pattern_id: "A.1.STM"
pattern_title: "Connect Project Reasoning (System-Thinking Long Mantra)"
section_id: "A.1.STM:5"
section_title: "Worked uses"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.STM/A.1.STM__007_worked-uses.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "A.1.STM — Connect Project Reasoning (System-Thinking Long Mantra)"
  - "A.1.STM:5 — Worked uses"
line_start: 4290
line_end: 4359
dependencies:
  - "A.1"
  - "A.1.CSD"
  - "A.1.SCR"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.5"
  - "A.15.6"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "A.22.CGUS"
  - "A.3"
  - "A.3.1"
  - "A.3.4"
  - "B.3"
  - "B.5.PI"
  - "C.22.2"
  - "C.28"
  - "C.30"
  - "C.30.STRAT"
  - "C.32.P2S"
  - "E.18"
  - "E.18.NET"
keywords:
---

### A.1.STM:5 - Worked uses

#### A.1.STM:5.1 - Common pump SoI, separate organizational contributions

The intended operating situation requires reliable water delivery at the user's outlet. Start there and examine the water-supply installation of which the pump is a part at that time: demand, inlet supply, the downstream path and the conditions under which delivery must continue. The pump must move water and maintain the required flow and pressure within those conditions. "Water-delivery unit" names the sought system by that contribution. The claimed mechanism needs engineering grounds; the desired outlet result alone cannot establish it.

In this modernization project, the operator, controller supplier and maintenance team designate the existing `PumpUnit-3` as the common SoI for the selected use. A supplier offering a usable controller under its own bounded delivery obligations can also have the controller as its product SoI. A separate project to develop the test laboratory has the laboratory as its engineering subject, with pump qualification providing the use basis. The water-supply installation is relevant through composition and operation; the supplier and laboratory are relevant through creation and provision. A.1 recognition, project designation, any local system-role classification and any assignment remain separate questions.

With the use basis available, compare constructions such as variable-speed regulation or a pressure-regulated bypass, with their different energy, operating and maintenance conditions. Then reason backward to how each could be produced and qualified. These are proposals whose suitability must be investigated. The following inquiry concerns a construction with a controller and sensor; its test arrangement must fit that construction.

##### A.1.STM:5.1.1 - Locally plausible answers that do not fit together

Suppose a proposed pump assembly must meet a stated delivery condition after installation. A functioning argument assumes a calibrated sensor in the completed assembly. The construction encloses that sensor, the production Method closes the housing before the proposed calibration, and the available calibration instrument needs physical access that the closed housing does not provide. Each team's answer may have worked in another configuration. Together, these particular answers leave the proposed qualification impossible as described. A common SoI and three signed local documents would not repair that incompatibility.

The team can now compare different whole proposals. It could change the housing to preserve calibration access, provided the changed construction still meets its operating requirements. It could propose calibration before closure, but then must establish why closure and installation would preserve the calibrated condition or how a later check can detect a consequential change. It could obtain another measurement arrangement, provided that arrangement can establish the required claim in the completed assembly and can actually be supplied. None is established merely by being imaginable.

The teaching explanation may run from required delivery through functioning, construction, production and calibration capability. The actual discovery began at a calibration question and returned to construction. A drawing, experiment or qualified measurement may supply the missing answer. If the team changes the housing, it reopens the affected operating and production assumptions; if it changes the instrument, it reopens the measurement and provision assumptions. It retains unaffected knowledge and restores agreement among the contributors whose decisions changed.

This case shows why the mantra must connect whole bodies of subject knowledge. Repeating "function, construction, method, creator" cannot supply the missing measurement argument. Conversely, a complete measurement argument for an inaccessible configuration cannot settle the project question. The connected account identifies what must be explained, which alternatives remain open, and where the answer will matter.

For the next project step, suppose the proposed housing can still be revised, but no alternative calibration instrument with demonstrated fit is available. The team chooses to investigate an access feature in the housing: the designer develops an option, the production specialist checks whether it can be made, and the calibration specialist checks whether it permits the required measurement. Their next result is a jointly supported option or a reason to return to the other repairs, not a claim that the pump is already qualified. If sealing or strength rules out the access feature, that result reopens the pre-closure calibration or alternative-instrument question. The operating requirement remains in force until those entitled to change it agree otherwise.

This also distinguishes a creator contribution from its performer. The chosen option may require housing redesign, manufacture and a calibration argument. Those descriptions guide the search for suitable people and equipment; naming a designer or assigning a laboratory does not establish their fit. If the measurement Method changes, compare its required access, range and conditions with the proposed laboratory and instrument again, then check that design, fabrication and calibration can obtain their shared inputs in time.

##### A.1.STM:5.1.2 - When actual production and use must be established

The design inquiry above can finish at its supported option. Later, an installation decision may ask whether the controller has actually been produced and is ready. Use A.15.PROD for the particular question: production participation, identity inception or completion. `ControllerSubassembly-7` and other pre-existing materials can be continuing subjects of changes; the future controller is not transformed before it exists. Identify the actual controller under its applicable identity rule when it first exists, and assess completion or readiness separately. Recover any claimed dated fabrication Work through A.13 and A.15.1; F.6 is needed only for precise assignment-bound attribution.

For a closure claim about this controller-production case, state its subject, the claims and references needed for that question, and the applicable closure basis. The case closes only when the production, identity, completion or readiness claims required by its question are supported, including the required evidence and decisions, and its closure rule is satisfied. Installation and later operation in `PumpUnit-3` remain the named receiving use outside this local closure. The ordinary positive branch of A.15.PROD:4.7 can return a readable answer or a precise gap; its stronger semantic or assurance branch opens when the receiving claim requires it.

If the project now needs a network of controller-production, pump-modification, qualification and operation flows, identify each member through E.18 and apply E.18.NET. Establish the actual production, installation, participation, use or feedback occurrences and their endpoint bindings; keep applied constraints and the use frame explicit. Until those conditions hold, retain the proposed network and its named missing link. A successful fabrication step does not provide a missing installation or feedback relation.

Follow actual facts from fabrication and changes of existing subjects through controller inception and pump modification to pump operation. For a runtime claim, keep the existing `PumpUnit-3` and its functioning, causal, interaction or participation claim separate from an A.3.4 change of the identified continuing delivery-side environment or input referent. If dated runtime Work is also claimed, use A.13 and A.15.1 for that claim, adding F.6 only for precise assignment-bound attribution. The reliable-delivery hypothesis establishes neither actual claim. A failed relation or missing binding stops the dependent claim while preserving valid local results.

If later operation shows that reliable water delivery depends on an upstream reservoir-control assembly outside the proposed `PumpUnit-3` boundary, the team reopens the outside-use, project designation and boundary hypotheses before revising the architecture and any network selection. Work already spent does not make the old boundary adequate.

##### A.1.STM:5.1.3 - Two products sharing one creator

A shared laboratory supports water-supply pumps that face frequent starts and irrigation pumps that run continuously. These product uses require different test conditions. The laboratory has eight available bench-hours tomorrow, with four promised to each product line. A water-supply failure now needs four additional diagnostic hours. Renaming that work a priority project would not supply twelve hours or settle the irrigation commitment.

The laboratory manager compares the consequences: delaying diagnosis blocks the water-supply commissioning decision; displacing the irrigation test delays its delivery. No qualified extra shift is available. A qualified external laboratory can perform the irrigation Method and return the required result before its deadline, including sample transport. Outsourcing is allowed for that result, and the manager has authority to buy it within a reserve that covers the confirmed price.

The manager obtains that commitment, informs the affected receivers and keeps the eight internal hours for the promised water-supply test and the additional diagnosis. Both product requirements and deadlines remain explicit. The decision is local because the manager's delegated authority covers the changed provision and expenditure. Without a suitable external commitment or that authority, the manager would have to return the unresolved trade-off to those entitled to change the product commitments; calling the laboratory the SoI would not settle it.

This one-off allocation does not establish a case for permanent expansion. If expected demand justifies developing the laboratory, a temporary organizational project can provide a defined capacity for both test classes. Its acceptance can establish compatible Methods, equipment, qualified people, sample access, handovers and capacity limits. The project can then close before future pumps operate. The test report, the laboratory's demonstrated capability and each pump's fitness remain distinct results. An internal budget transfer provides means; it is neither external customer income nor evidence of product usefulness.

#### A.1.STM:5.2 - One-off service: a usable hairstyle

A client and a stylist first describe the intended use: the appearance the client seeks while moving through an event and later ordinary conditions, including possible rain. They examine the hairstyle in that bodily and social use before choosing the arrangement of hair and fasteners, then cutting and styling Methods, a capable stylist and suitable tools. The salon contributes through creation; it is not a containing whole of the worn hairstyle. Merely completing the hair operations would leave the purpose unmet if the result cannot survive the agreed use.

The embodied hairstyle is the proposed SoI; the salon is a provider, the sketch is a description, and the appointment's Work has its own boundary. Before the hairstyle exists, its designator belongs to the agreed description. For an actual system claim, A.1.SCR evaluates that exact proposed hair-and-fastener whole, its identity and physical organization; it does not substitute the client merely because the client is already a recognized System. If the whole is established not to satisfy the System criterion, reject that System interpretation. If necessary facts are missing, leave recognition unresolved and name the missing basis. In either case, preserve the supported service and result claims; do not treat those claims as settling the project's common SoI. The ordinary hairstyle name alone settles no systemhood question.

The sketch can be complete before styling; styling Work can end before the later use has been observed. Each local closure remains available at its own scope. A later failure under the agreed use conditions can reopen the design or service decision without making the earlier sketch an unfinished episteme or erasing the Work that happened.

#### A.1.STM:5.3 - Knowledge development with an epistemic result

A materials-instrument team is developing a diagnostic installation for laboratories. Its intended use is to distinguish two material failure mechanisms, so that installation is the product SoI. A bounded research project investigates an explanatory model and produces an account of experiments; those results are epistemes. The shared systemic account connects model construction, test design and instrument changes to the diagnostic use. The argument and publication can reach their own acceptance before the installation is changed or the improved diagnosis is demonstrated.

This choice depends on the stated research purpose. A project seeking a theorem, historical explanation or openly reusable knowledge must not invent an arbitrary laboratory, reader or computer as its SoI merely to fill a position. Its epistemic result can be legitimate and locally complete. For the diagnostic research, a supported finding that the proposed model cannot distinguish the mechanisms can finish the agreed inquiry and justify another approach; it does not establish improved diagnostic capability. If participants need a systemic account, they must still establish which system's useful use supplies their common purpose and how knowledge development contributes to it. An unknown or contested receiving use leaves that systemic basis open without invalidating the separate epistemic result.

#### A.1.STM:5.4 - The same machine in different project roles

A manufacturer proposes a cutting machine that does not yet exist. First describe its future use at the customer's plant: which component transformations are needed, what the next operation must receive, and under which operating conditions. Look upward to the production cell in which the machine is intended to be installed and explain how its functioning depends on the machine's contribution. These are proposed use and composition relations at the future operating time. The manufacturer's organization is a creator, not that production cell.

The machine is the SoI of the manufacturer's product undertaking because the manufacturer offers it as a usable supply with defined fitness obligations. The customer can supply the design and use requirements. Recover that use basis before comparing construction, manufacture and qualification, needed creator contributions and their provision. The control software, calibration rig and manufacturer organization are distinct local subjects. Work to develop the manufacturer has its own result and acceptance, judged by the agreed creator capability; the machine remains the product SoI.

The customer's component-production work uses the machine as a means of production. Its product SoI is the component supplied for a receiving use, which gives the construction and provision choices their reason. In work maintaining this capability, the machine is the local system-in-hand. Its repair can finish under its own acceptance conditions before another component is produced. Moving that repair to another contractor preserves both its finite completion and the component-use basis for providing it.

If the customer undertakes to supply refurbished machines to other users, recover those recipients and their use before comparing the refurbishment. This undertaking can select the machine as SoI too. Explain the resulting requirements and commitments rather than infer a new purpose from the object currently under inspection. Several products, users or linked projects can constrain one decision; use their actual relations instead of assigning them a single universal boundary.

