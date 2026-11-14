---
chunk_kind: "child"
pattern_id: "C.32.MWA"
pattern_title: "Synthesize an Architecture Account of Methods and Their Use"
section_id: "C.32.MWA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.MWA/C.32.MWA__005_solution.md"
commit_sha: "2aea46c8a8ad57c56a81423184fd0d2e19d19cca"
heading_path:
  - "C.32.MWA — Synthesize an Architecture Account of Methods and Their Use"
  - "C.32.MWA:4 — Solution"
line_start: 82592
line_end: 82650
dependencies:
  - "A.13"
  - "A.15.1"
  - "A.22"
  - "A.3.1"
  - "B.1.5"
  - "B.2"
  - "C.17"
  - "C.18"
  - "C.30"
  - "C.30.AD"
  - "C.30.ILC"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.MLAO"
  - "C.36"
  - "E.23.CDI"
  - "E.4.DPF"
  - "E.4.PFAD"
  - "F.6"
keywords:
---

### C.32.MWA:4 - Solution

For an architecture decision, examine how methods, performers and means of provision fit together. The eight actions in §4.1 help organize that inquiry. The mantra below can also be used on its own to locate one missing contribution in familiar arrangements.

**A mantra for following a method from a need to its use.** *What work is needed, and what is missing? Is there a way to do it? If several ways are available, how do we choose? Where can we find or develop a missing way? How will the way reach whoever needs it? What must the performer learn, what can the performer discover through inquiry or practice, and what help will be available? Which method fits this case, and what must be set or changed? Are the means and authority in place? Who did what? What did the work produce, what reached the recipient, how was it used, and what effect was observed?*

Use as much of the mantra as the job requires. If a cook already knows the recipe and has been denied access to the kitchen, the immediate task is to obtain entry from the agent authorized to grant it or find another available kitchen. Check readiness when the decision is whether the whole job can start. Develop an architecture account when the arrangement itself needs examination, for instance when changing who provides a step also changes who can learn or perform it. A methodologist can reconstruct a way of working from observations and examine the grounds for its applicability. A practitioner can find the same way in a discipline's literature, learn it from a demonstration or commission the work. Discovery by this practitioner establishes novelty for that practitioner. A claim of novelty for a discipline needs comparison with what its practice and sources already supply.

A discipline can describe one reusable method. If the decision calls for comparing several, recover what makes each one applicable. Call them a family when the grouping matters and its basis can be stated. A family catalogue may compare many methods. A.3.2 identifies a MethodDescription by the one Method it describes and what it says about doing it. To put a way into use, identify the method that fits the present requirements and the settings its applicability permits (A.3.1:4.7–4.8). Develop the missing way through C.39 if none fits. A description or demonstration may give the performer what is needed to try it. E.23.CDI:4.2.1 addresses acquiring the capability or obtaining continuing support. A.15.5 tests readiness for the particular job, and A.15.1 identifies its actual performance. Establish what the work produced, whether it reached the recipient, what the recipient did with it and what changed. A catalogue may exist before anyone receives it. A.6.P.WMR helps recover the particular relation when “result” leaves it open. If an accepted problem formulation is the starting point, E.18.1 carries its relevant claim to the particular decision that needs it. In teaching, follow the dependencies aloud. In practice, begin with the gap that matters. An observed failure can take the practitioner back to the choice of a method, the help required or an unmet condition of the job.

#### C.32.MWA:4.1 - Eight actions

1. **Choose an entry.** For an obtaining organization of Method use, anchor one independently admitted representative performed Work occurrence and the useful result at stake, with A.13 bases before A.15.1 admission; establish the other relied-on relations separately. For a possible-future organization, anchor an intended-use case, `WorkPlan`, or another correctly typed prospective account; state what would put that proposal into use and how later representative Work would test it. Keep actual development or support Work separate from the proposed use. Actual and prospective claims can coexist in the same account.
2. **Name the subject and participants.** State the subject under discussion (`EntityOfConcern`) and the kinds of the participants before classifying rows or positions. A source word such as *practice*, *layer*, *role*, *model*, or *provider* does not settle those kinds.
3. **Build alternatives for the question.** State whether the alternatives are competing architecture accounts of the same arrangement, proposed changes to that arrangement, or both. Competing accounts can reveal a relation that a sequence-only description misses; proposed changes alter how the Methods would be used or supported. Keep those comparisons distinct. Develop or reuse alternatives that can change the decision or fail on different cases. When NQD is the current generation test, retain NQD-distinct candidates: their novelty is not a relabeling, their use-value preserves the declared constraints, and their diversity exposes different failure modes. A first layout needs examination against the question; retain it when it supplies an adequate answer. Do not turn NQD into one scalar score.
4. **Recover each relation used.** In ordinary words first, state whether the source claim concerns Method composition or order, Work parthood or overlap, a subject relation, description or model use, a capability or provider dependency, cultural dynamics, or another admitted relation. Use the pattern that defines or constrains that relation when the claim matters to the answer. For structures of a Method and its uses, C.30.ASV:4.5a helps select the question before drawing its representation.
5. **Separate the described objects from their descriptions.** Keep identified Methods, Work, Systems and their relations distinct from the descriptions, models, views and coarse-grained accounts about them. A description can itself be used in Work; name that use separately from what it describes. State the correspondence and the distinctions each description preserves or loses.
6. **Resolve a whole-identity question when needed.** Use `B.2` when the current claim raises a consequential question about retaining the identified Method, Work, System or Discipline whole or identifying a new one. Keep the existing whole when a supported explanation is sufficient, and retain uncertainty when the needed basis is missing. Reidentify a selected structure under `A.22`'s four identity discriminators when the claim requires a different selected structure.
7. **Compare conflict and moved burden.** Expose conflicts between candidate structures. For every apparent local repair, ask what residual, constraint, cost, evidence burden, delay, or loss moved to another structure or scope. Compare the alternatives against the named architecture question, not against visual tidiness.
8. **Keep deliberate and distributed change distinct.** Separate a project's architecture choice or intervention from cultural generation, transmission, recognition, selection, rejection, retention, and loss. A project can influence those processes without controlling or proving them.

#### C.32.MWA:4.2 - Short working result

Write the first result as a short account that another practitioner can use without decoding a private ontology. This outline is a writing aid, not a mandatory schema:

```text
Current architecture question:
Entry: obtaining / possible-future organization of Method use; status of each relied-on claim
Representative occurrence or prospective anchor:
Useful result at stake:
Selected structures and the relations used:
Correspondences between described objects and descriptions, with losses:
Alternatives: competing accounts / proposed arrangements / both
Main conflict and any moved residual or burden:
Alternative that changes the current decision:
Source-return or later-test condition:
```

A compact table can support this account. Symbolic predicates are optional assurance and belong after the readable explanation. The result stops at architecture evidence; comparison, selection, decision, publication, evidence, assurance, or gate claims use their own patterns when those claims become current.

#### C.32.MWA:4.3 - Conditional product-boundary comparison

Only when product identity is the current architecture question, compare these four different arrangements:

1. one domain DPF;
2. independently maintained sibling DPFs;
3. direct use of FPF plus exact domain sources; and
4. a proposed common applied DPF.

For each arrangement, state the recurring practitioner problem, first useful result, independently useful boundary, sources and maintenance burden, and what another arrangement would leave hidden or duplicate. These four are comparison forms, not a selected product roster. When product identity is not the question, do not force this comparison into the Method.

#### C.32.MWA:4.4 - Stop, lower, and reopen

Stop when the short synthesis identifies the entry, selected structures and relations, consequential correspondences and losses, any conflict or moved burden, and the next useful action. Include different alternatives when the receiving question needs a comparison; an adequate account or retained arrangement can finish without inventing another option. Add a view only when it can change the answer.

Lower only the dependent claim when its subject, representative occurrence or prospective anchor, relation, evidence boundary, or required alternative is not recoverable. Preserve independently useful content and obtain the named missing basis from its direct source or pattern.

Reopen when representative Work contradicts the synthesis, a proposed organization of Method use is put into practice, a new structure changes the decision, a moved burden becomes material, a direct source changes a relied-on premise, or the product-boundary question enters or leaves scope.

