---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
section_id: "C.2.1:9"
section_title: "Archetypal Grounding — Worked Cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__010_archetypal-grounding-worked-cases.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "C.2.1 — U.Episteme: Constitution, Empirical Grounding, and Edition Relations"
  - "C.2.1:9 — Archetypal Grounding — Worked Cases"
line_start: 43711
line_end: 43775
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.14"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.0"
  - "A.6.1"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.5"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "C.3.2"
  - "E.10.D2"
  - "E.13"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.9"
  - "G.11"
  - "U.Episteme"
  - "U.MethodDescription"
  - "U.Signature"
  - "U.View"
keywords:
---

### C.2.1:9 - Archetypal Grounding — Worked Cases

These cases ground the pattern in practice; only a case that names an obtaining `EpistemeEmpiricalGroundingRelation` asserts empirical grounding.

#### C.2.1:9.1 - Physical engineering

A pump-maintenance specification has a claim graph about exact pump `P` under a reference scheme that resolves part names, states, units, and measurement procedures. Those three participants identify the episteme. For test bench `B`, exact covered claim subgraph `C_B` contains the discharge-pressure-tolerance and leakage claims. Its claim-to-world mapping names the direct pressure-measurement and leakage-inspection relations involving `B`; a maintenance-interval claim outside `C_B` is not grounded by those measurements. The grounding relation over `(E,B)`, with `covered=C_B`, continues for the maximal interval during which every required mapping obtains. If that coverage continues while an evidence archive or inspection-work log becomes unavailable, only a separately governed support, warrant, confidence, or evidence-use assertion may change. A publication occurrence makes the episteme available through a rendered checklist form borne by an exact carrier. When checklist marks assert particular maintenance or inspection Work, use :4.0's Work branch; assignment attribution is added only when the checklist account requires it. A separately current assertion that `P` satisfies the constructive `U.System` criterion is another episteme about `P`; renaming or republishing the governing FPF pattern does not change `P` or create its systemhood.

The classification assertion changes only when its own claim content or reference scheme changes. Pump continuity is judged instead under the `A.1` reidentification rule; a changed or unchanged assertion does not establish that continuity.

#### C.2.1:9.2 - Medicine

A diagnostic model concerns one patient-state entity or one admitted patient cohort under a scheme that defines observations, measurements, and diagnostic interpretations. Each `EpistemeEmpiricalGroundingRelation` identifies the exact covered diagnostic-claim subgraph, grounding holon, mapping to the required current observation, measurement, or test relations, and maximal continuous interval of complete coverage; it grounds no unlisted claim. If a threshold revision changes claim content or the effective reference scheme, that changed discriminator identifies another episteme; moving the unchanged model to another screen changes only the exact publication or representation object that actually changed.

#### C.2.1:9.3 - Competence claims, teaching Work, and learner-facing views

A curriculum model concerns an exact competence structure under a scheme that relates assessment or performance evidence to competence claims. If *taught* or *learned* wording leaves the changed subject or result unclear, use `E.10.LRN` to recover the claim first: receiving an intervention and acquiring a capability call for different evidence.

A learner-facing episteme is a `U.View` when it conforms to an exact learner-facing viewpoint under `E.17.0`. If its construction from the source curriculum model matters to the account, `A.6.3` supplies that viewing relation. Changing the selected competence claims changes the receiving episteme; changing only its display preserves it.

If empirical grounding is needed, name the covered competence claims and their mappings to the relevant assessment or performance relations involving an exact admitted course-cohort or learning-environment holon, as required by :4.3. A later capability, transfer or retention claim uses `A.10` for its bounded reliance on the relevant result. If particular teaching, assessment or construction Work must be asserted, open :4.0's Work branch. The identity-only use finishes with the model's claims, exact subject and effective scheme.

#### C.2.1:9.4 - Episteme about an episteme

Simulation model `M` is one episteme. Review `R` concerns `M`, so the EntityOfConcern in `R` is the episteme `M`, not the physical system modeled by `M`. Claims in either episteme may cite separately governed evidence-use relations concerning the simulated or physical system. Publishing `R` does not revise `M`.

A theory episteme is recognized through its claim-bearing constitution and whole-level inferential characteristics. A textbook publication can make one edition of that theory available, but the publication occurrence, form, and carrier are not constituents of the theory and do not establish its holonhood.

#### C.2.1:9.5 - Edition succession

Episteme `E1` is the exact source used to produce candidate edition `E2`. The applicable continuity policy says that the EntityOfConcern remains the same, specified core claims must remain traceable, listed claims may be corrected, and a translation into another reference scheme counts as a derivative rather than an edition. The current case identifies the preserved core claims, deliberately corrected claims, unchanged EntityOfConcern, and source-to-revision use. Those facts satisfy the policy, so the positive `EpistemeEditionRelation(E1,E2)` assertion is available.

If the same Work instead retargets the claims to another EntityOfConcern, translates them under a rule that the policy classifies as a derivative, or reconstructs similar content without using E1 as source, the edition predicate fails even when the Method is named “revision.” Work, Method, provenance, change facts, evaluation, and evidence remain outside the two-participant relation. Later repackaging or publication establishes neither another episteme nor edition continuity.

#### C.2.1:9.6 - Grounded identity across two observations
A morning-observation episteme concerns an object designated `M`; an evening-observation episteme concerns an object designated `E` under another reference scheme. To decide whether the observations concern the same continuing object, recover the domain's criterion for that continuation and use its motion and observation account to construct and test the connection. State the identification with the premises and evidence that support it. When the observations leave competing connections possible, retain that ambiguity; when they fit none of the proposed connections, reconsider the observations or model. The finite case below supplies its continuation, motion and observation premises explicitly.

The two observation epistemes can retain different identities after the object is identified: they can make different time-indexed claims or use different reference schemes. C.2.1:4.2.3 permits the identifying claim in ordinary language. If a later use needs a separately designated relation occurrence, apply A.6.REL with the direct relation pattern's obtaining predicate and occurrence-identity rule. A missing relation definition then blocks that occurrence-dependent use. It does not erase a conditional identification already established under stated premises; an unspecified object-continuation criterion, by contrast, leaves the identification itself unresolved.

**Construct a bounded identifying result.** Consider two persistent point objects whose motion is modeled independently on one axis; paths may cross. Each object is observed exactly once at each end of a one-second interval, with exact positions expressed in one common coordinate frame. Initially object A is at 0 cm and B at 10 cm. The later observations R and S are at 1 cm and 9 cm. The motion account bounds speed by 2 cm/s, so each object's displacement is at most 2 cm.

There are two complete associations. A–R with B–S requires displacements of 1 cm each and is admissible; straight paths supply a joint realization. A–S with B–R requires 9 cm each and fails the bound. Under these premises, R is the later observation of A, and S of B. The earlier and later observation claims concern the same respective objects while retaining their different time-indexed content.

Change the speed bound to 10 cm/s. Both associations now have admissible straight-path realizations. The observations leave the correspondence unresolved; a further discriminating observation or motion constraint is needed.

In [Rodin's astronomical reconstruction](https://philsci-archive.pitt.edu/12116/1/vh.pdf), the connecting trajectory is supplied through theory and observations. In the HoTT reconstruction, MS and ES are represented as terms of a point-object type Pt; `p : MS =_Pt ES` expresses the identifying construction as a term of their identity type.

#### C.2.1:9.7 - Readable wiring diagram as a proxy

Wiring-model episteme `E1` concerns exact harness `H` under reference scheme `S1`, which resolves connector designators, pin identities, and connection predicates. If only layout changes in a wiring-diagram representation, identify the exact representation transition and preserved connector, pin, and connection correspondence; `E1` remains the same. If instead only an exact publication form, carrier, or rendering changes, identify that E.17/E.24.PUB object and relation; `E1` again remains the same. If a connection claim is removed from `E1`'s ClaimGraph or the legend changes the effective reference scheme, the changed claim content or scheme identifies episteme `E2`.

The wiring-diagram representation under its stated diagram scheme represents the connectivity of `H`; its mapping resolves connector marks and pin marks to the independently identified connectors and pins. A layout-only transition preserves connector identity, pin identity, and connection predicates. If the diagram omits a connection that remains in `E1`'s ClaimGraph, that representation loses one connection predicate. If a revised legend no longer resolves an earlier mark to its connector, that mark-to-connector reference is lost. The diagram remains admissible for maintenance diagnosis only while the connections on which that diagnosis depends are preserved and recoverable; stop that use or return to the source relation structure when they are not.

A readability score can improve while the diagram makes the connections needed for diagnosis harder to recover. When that score is used as the practical value, apply `E.13`: name the intended diagnostic value, the readability proxy, and what became worse. Use the representation branch in :4.0 for the transition and its preserved or lost structure.

#### C.2.1:9.8 - Trained or probe-derived representation and tool-using inference

A distributed activation pattern observed during inference is a system-side phenomenon. A trained probe or decoded rendering can represent it for a declared use under `C.29` and `A.6.3.RT`. To identify a probe report as an episteme, recover what it claims about that exact phenomenon and the interpretation scheme that gives those claims meaning. Decodability or a readable label alone leaves that identity question unanswered. Use `E.10.LRN` when *learned representation* still leaves the subject or result unclear.

For a claim about particular inference or tool-call Work, open :4.0's Work branch. If a trace participates at an exact `A.6.1` result position, state that binding. When the trace carries claims about the call, identify its episteme through those claims, that Work as subject, and the effective scheme. A question about when the trace first existed separately opens :4.9.

An answer may carry a proposed solution, while an evaluation report states whether it passes a named test. To rely on the solution, inspect the support relevant to its claim; to assert empirical grounding, test :4.3's exact covered-claim mappings. A successful call or score does not supply those mappings.

When a changed tool regime changes inference behavior, locate the changed method, Work or representation and the evidence used to assess it. Update the grounding occurrence if its coverage predicate changes. Reidentify an episteme only when claim content, EntityOfConcern or effective reference scheme changes.

