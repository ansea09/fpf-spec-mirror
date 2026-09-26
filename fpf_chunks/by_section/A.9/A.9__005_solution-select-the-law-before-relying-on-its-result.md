---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:4"
section_title: "Solution — Select the Law Before Relying on Its Result"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__005_solution-select-the-law-before-relying-on-its-result.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:4 — Solution — Select the Law Before Relying on Its Result"
line_start: 24013
line_end: 24038
dependencies:
  - "A.19.CN"
  - "A.19.ULSAM"
  - "B.1"
  - "B.2"
  - "C.29"
keywords:
  - "aggregation law"
  - "bounds"
  - "cross-scale consistency"
  - "dependency model"
  - "intended result"
  - "ordered composition"
  - "singleton identity"
---

### A.9:4 - Solution — Select the Law Before Relying on Its Result

1. **Name the intended result and operands.** State what the combination must mean, which inputs contribute and what operation is proposed. For reliability, distinguish joint success from alternative success. For a composed Method or function, retain the intended order and participant meanings.
2. **Recover the subject model and conditions.** Identify dependence, overlap, interaction, grouping and numerical interpretation where they change the result. For quantities, also recover the Characteristic, Scale, units and measurement conditions. Use C.29 when the representation or its correspondence to the subject is unresolved; mathematical notation alone is not that correspondence.
3. **Select a justified law.** Use the direct domain source or Method that supports this operation for this result. Reuse its current applicability judgment when adequate. If no available law is justified, name the missing model or condition; do not pick a convenient average or a generic weakest-part rule.
4. **Check the property needed by the current action.** A requested reorder needs an order-invariance claim; a repartition needs valid decomposition and recombination; a bound needs the model that warrants it. For a numerical reproducibility claim, state whether the use requires the same exact value, the same bits, or an error bound before accepting a regrouping. Use the applicable argument or warranted test under those conditions. The table below supplies possible questions, not a compulsory set of five checks.
5. **Return the warranted answer and limit.** Apply the justified law, or return a supported bound, separate inputs or the exact missing/defeated premise. If a condition changes, withdraw only the conclusion that depended on it and recover the needed model. Pass an actual CHR measure fold to ULSAM when that mechanism use is current. Use B.3 only for a receiving claim that requires assurance.

Describing the choice does not perform the fold, establish parthood or authorize reliance. No additional record is needed when the law, inputs, conditions and answer are already recoverable in the working account.

#### A.9:4.1 - Select Only the Relevant Property

| Property or legacy code | Question and applicability |
|---|---|
| Singleton base case — **IDEM** | If the construction has this requirement, does a one-element input return the corresponding element? This differs from algebraic idempotence `x ⊕ x = x`. Repeated sources need their own dependence treatment. |
| Reordering — **COMM** | Does exchanging the operands preserve the intended result under the actual operation and model? Keep order when it is consequential. Commutativity alone does not establish independence of the observations. |
| Repartitioning or moving computation — **LOC** | Do the declared decomposition, recombination and numerical conditions preserve the required result? Exact arithmetic and floating-point implementations may answer differently. |
| Weakest-part bound — **WLNK** | Does the specified result and dependency model justify this bound? A bound need not be the exact result, and it is not a cap on every aggregate. |
| Monotonicity — **MONO** | Under which input/output order and side conditions can improving an input not worsen the result? Interactions can defeat the proposed claim. |

A layered-control contract may state a reference signal, guaranteed tracking error and cycle time. Check the needed composition property under its control model. Possessing that contract alone proves neither reordering nor repartitioning valid.

#### A.9:4.2 - Keep Whole Reidentification Separate

If observations defeat a law's premise, reopen the model, applicability conditions and resulting claim. B.2 is needed only when the current question also concerns whether the existing whole still satisfies its identity rule. A failed aggregation model alone neither identifies a new whole nor establishes a Meta-Holon Transition.

