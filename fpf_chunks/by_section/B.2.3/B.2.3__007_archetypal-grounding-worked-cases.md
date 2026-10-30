---
chunk_kind: "child"
pattern_id: "B.2.3"
pattern_title: "Meta-Holon Transition With Episteme Result"
section_id: "B.2.3:5"
section_title: "Archetypal Grounding (Worked Cases)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.3/B.2.3__007_archetypal-grounding-worked-cases.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "B.2.3 — Meta-Holon Transition With Episteme Result"
  - "B.2.3:5 — Archetypal Grounding (Worked Cases)"
line_start: 44219
line_end: 44280
dependencies:
  - "A.1"
  - "A.10"
  - "A.6.2"
  - "A.6.3"
  - "A.6.3.CSC"
  - "A.6.4"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "B.3.5"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "E.17"
  - "E.24.UK"
  - "F.18"
  - "F.19"
keywords:
---

### B.2.3:5 - Archetypal Grounding (Worked Cases)

#### B.2.3:5.1 - Reliability Doctrine

Reliability work may begin with local runbooks, incident reports, dashboards, and definitions that remain a collection. A first doctrine constitution requires A.1 and C.2.1; the collection supplies no prior holon merely by being named. The following constructed case instead starts with an already recognized episteme and asks whether it can support a stronger deployment claim.

**Supplied setting and receiving need.** The example stipulates a modeled deployment `S = Relay-S/D17`, independently identified by its deployment configuration, and a fixed nonempty set of requests. Use classical two-valued logic. `Ack(r)` means that D17 emits an acknowledgement for request `r`; `PrimaryStored(r)` means its primary store holds that request's payload when the acknowledgement is emitted. The already recognized episteme `E0 = <G0, S, R0>` has a ClaimGraph containing the sole premise:

```text
P: for every request r, Ack(r) implies PrimaryStored(r).
```

`R0` is the complete scheme interpreting this graph, with those request, acknowledgement, and primary-storage designations. The receiving work now needs one episteme whose own stated premises support a derivation of:

```text
Q: for every request r, Ack(r) implies
   (PrimaryStored(r) and ReplicaStored(r)).
```

Here `ReplicaStored(r)` means the replica holds the same payload at acknowledgement time. Q concerns the deployment S. The required new object, if established, is an episteme carrying and supporting Q.

**Compare with E0.** In the comparison vocabulary, retain all R0 meanings and add `ReplicaStored`. Set `Ack(r*) = true`, `PrimaryStored(r*) = true`, and `ReplicaStored(r*) = false` for one request, with `Ack = false` for every other request. This valuation satisfies P and falsifies Q, so G0's stated premise does not entail Q. To obtain the required derivation, supply the additional premise:

```text
T: for every request r, Ack(r) implies ReplicaStored(r).
```

T is a stipulated premise of this example, not a reliability fact proved about an operating service. Let G1 contain P, T, Q, and the inference deriving Q from P and T by conjunction introduction under the common antecedent. Let R1 retain R0's meanings and add the replica-storage designation. The candidate is `E1 = <G1, S, R1>`.

Nonentailment alone would not establish a new identity. Here C.2.1's declared identity discriminators are the exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme. Keeping E0 requires retaining G0 and R0. Adding the premise, inference, and effective designation needed for this use changes both G and R, so the result cannot be E0 under that identity rule. This establishes `insufficient` for E0 and this receiving use. E0 still exists and supports P; a different layout or publication of its unchanged triple would leave it E0.

**Recognize the candidate.** The construction supplies each A.1 ground:

| Ground | Supplied fact or demonstrated result |
| --- | --- |
| Individuated candidate | E1 is the particular candidate `<G1, S, R1>`. |
| Constituents | G1 and R1 are its epistemic constituents under C.2.1; S remains the independently identified EntityOfConcern. |
| Construction | R1 interprets every claim and inference in G1 about S, and G1 organizes P and T as premises for Q. This satisfies the C.2.1 constitution predicate for one interpretable claim-bearing whole. |
| Identity | C.2.1 reidentifies this episteme by that exact G1/S/R1 triple. A change in one of those values identifies another episteme. |
| Composition-grounded characteristic | G1 supplies the inference organization and R1 its interpretation about S; together they yield an interpretable derivation of Q. P alone and T alone each leave one of Q's conjuncts unestablished. |
| Compatibility with a larger assembly | The argument construction below incorporates E1 unchanged and uses Q in a further derivation. |

For the last ground, supply a local argument-assembly rule: retain an interpreted argument as an unchanged constituent, preserve its graph and interpretation, and join its conclusion to an additional compatible premise by a named inference. Construct `E2 = <G2, S, R2>`. G2 contains G1 as an unchanged subargument and adds the supplied lemma `L: (PrimaryStored(r) and ReplicaStored(r)) implies Recoverable(r)` for each request. R2 retains R1 as the fixed local scheme for that subargument and adds the meaning of `Recoverable(r)`: the modeled recovery method can read back r's payload at the stated time. Under the assumption Ack(r), Q gives both storage conditions and L gives Recoverable(r) by modus ponens; discharging the assumption yields `Ack(r) implies Recoverable(r)`. Under this construction rule, E1 is a constituent of E2 with its graph, local scheme, subject, and identity preserved.

E1 therefore satisfies the displayed A.1 grounds and C.2.1 constitution and meets the receiving need. If later work needs a reidentification record, `resultHolonRef` names E1 and `resultHolonKindRef` names `U.Episteme`. The record and any classification assertion concern E1; Q still concerns S. The logical construction establishes the conditional derivation, not the truth of P, T, or L for a real deployment. A use that must rely on those service claims needs their actual grounds and any assurance required under B.3.

**Change the interpretation condition.** Suppose the supplied candidate uses G1 with the complete R0, whose declared vocabulary has no interpretation of `ReplicaStored`. The proposed `<G1, S, R0>` fails constitution: its scheme cannot interpret the whole graph. Supply a scheme that does interpret it and identify the resulting episteme. By contrast, if R1 exists but is unavailable to the evaluator, evaluation is `unknown`; recover the scheme or withhold the classification. Neither result erases E0 or changes the identity of an already constituted E1. A failed or unresolved judgment is not a typed positive result in the optional record.

For a larger reliability doctrine, the same comparison uses its actual claims about user-visible service harm and reliability, its independently identified subject, and its effective designations. Add empirical grounding to operating services, handbook publication, and source use for standards or training materials only when the receiving use needs them. Systems use and cite the doctrine, use it in training, and let its claims guide their work; any relevant local system-role kind and assignment remain separate claims.

#### B.2.3:5.2 - Model Family Becomes Theory

A model family can remain a toolbox. It becomes an episteme-result MHT only if B.2's candidate passes A.1 and one exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme stand in an obtaining C.2.1 constitution relation. Empirical grounding and explanatory or predictive use are checked through neighboring direct relations when the receiving use needs them; they are not extra identity constituents.

If the change is only a new model publication or benchmark score, use publication, source-use, measurement, evidence-use, and mathematical-lens patterns instead.

#### B.2.3:5.3 - Standard Body

A set of clauses, examples, and annexes can become a standard episteme only when the candidate passes A.1 and its exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme satisfy C.2.1 constitution. Recover its terms, references, scope, and conformance claims under that constitution; identify publication forms separately.

The standard is not the committee, the PDF, or the Work of enforcement. The committee may be an acting System. If committee or enforcement Work is claimed, recover each exact performer through A.13 and admit the Work independently under A.15.1. Add F.6 only if the account expressly consumes precise assignment-bound attribution; a missing or failed relation leaves the Work intact. The PDF file is a presentation carrier; its layout may supply a publication form.

