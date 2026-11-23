---
chunk_kind: "child"
pattern_id: "C.35"
pattern_title: "Assess Generated or Discovered Results for Architecture Use"
section_id: "C.35:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.35/C.35__005_solution.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "C.35 — Assess Generated or Discovered Results for Architecture Use"
  - "C.35:4 — Solution"
line_start: 85550
line_end: 85590
dependencies:
  - "A.22"
  - "A.6.M"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "E.18"
  - "G.5"
keywords:
  - "DSM"
  - "LLM"
  - "NAS"
  - "candidate input"
  - "discovered result"
  - "generated result"
  - "modal architecture proposal"
  - "structural discovery"
  - "structural synthesis"
---

### C.35:4 - Solution

Ask what decision the result can settle. One candidate checked against every applicable constraint can establish feasibility within the model. It may complete a commission to find any suitable design. A claim that no design qualifies requires grounds that cover every admissible alternative, such as an exhaustive search or a proof of incompatible constraints. A search that stops without a candidate can still tell the next designer which alternatives were examined. When one design uses less energy and another takes less time, both can be nondominated. To call a design nondominated, exclude alternatives that do at least as well on every stated criterion and better on one. State the set over which this was established. A claim that a design is best needs a ranking or trade-off rule for the commission and grounds that the design ranks at least as high as every admissible alternative. A verified bound may settle that comparison. If the leading alternatives remain incomparable, the requirement for a greatest design can have the answer that none exists. A commission to select one can leave the choice to the authorized recipient or require a further preference. A request for the nondominated set can be settled under the given criteria. A unique optimum also excludes ties for the best value. A unique feasible design excludes every other feasible design regardless of preference.

Judge the result and its production separately. A verified design can serve the commission whoever suggested it. To credit an agent with designing the organization, identify the decisions left open by the input, the method or generator, and the evidence that the agent made them. A fixed input that already specifies the organization can support an assessment of how the agent checked it. Claims about the installed organization depend on evidence about the installation. State any material limit or next check in the existing account when possible.

Use the smallest sufficient path:

1. Give or reuse the sufficient account. If it lets the receiver make the intended next move, stop.
2. When organization status affects use, distinguish an obtaining structure, a refuted or unestablished claim about existing organization, and a proposal. Apply A.22's four discriminators to a positive structure claim. Add C.30 claim identity when the receiving use needs independent reidentification. Distinguish the representation when correspondence or representation operations matter; use C.29 for a remaining mathematical-representation choice, transfer, or reliance question.
3. When the receiving use relies on how the result arose, select the branch for that claim. A complex result may need separate accounts for claims arising through different operations; do not infer one branch's basis from another.

   - A transformation adds source and result objects, trace, preservation, and loss.
   - A discovery adds observation or extraction basis, what is observed, what is inferred, what remains unknown, the covered and unexplored region, uncertainty, and validation.
   - A generative proposal adds constraints, proposed organization content, known omissions, and validation needs; state the origin of any input on which the commissioning decision depends. For preservation, also identify the baseline and the relation to what is proposed.
4. When reliance depends on how the result arose, establish the operation and the history facts material to that use. Add the Method, independently admitted dated `U.Work`, and production, discovery-use or Work-to-change relation only when those claims are being made; retain the premises and evidence each requires.
5. Add bearer feasibility, realized structure, publication, archive or front policy, evaluation, measurement, decision, reusable-generator, or next-claim references only when the intended use relies on that claim. Use the pattern for that claim rather than copying its dossier into C.35.
6. Stop when the receiver knows the supported next move and any unresolved condition, material limit or return. Materialize the optional full note only when those facts or their relied-on branch details need an independently reidentifiable result.

Use these patterns when their questions arise:

| Pattern | Question or use |
| --- | --- |
| `C.32` | Candidate-palette use. |
| `C.32.ACE` | Eval programs and results. |
| `C.16` | Measurement. |
| `C.29` | An unresolved mathematical-representation choice, transfer, or reliance question. |
| `C.30.AD` or `C.30.ASV` | Descriptions and views. |
| `G.5`, `C.18`, and `C.19` | Selected-set, archive, front, and pool claims. |
| `E.24.PUB` | Publication occurrence, form, and carrier. |
| `E.17` | A publication that is an episteme projection. |
| `C.32.PAD` and `C.32.ADR` | Project architecture decisions and their ADR-like publication, respectively. |
| `E.20`, `G.1`, `G.10`, or `G.11` | Only when the current question concerns a reusable generator or mechanism suite. |

**Use concerning CGUS.** When a result is useful because it describes, compresses, or demonstrates a constraint-governed unfolding organization, C.35 admits only that result for the declared architecture use. Cite an A.22.CGUS structure only when its positive A.22 and A.22.CGUS basis already obtains; retain an unestablished claim about an existing organization as unresolved, and a proposal as modal claim content.

The structure itself, when it exists, remains with `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `E.23`, or another pattern defining the structure. If the encountered item is only a route card, narrative sequence, demonstrative slice, generated publication form, or presentation carrier, recover its claim-bearing result and represented object before making any positive structure claim.

When the encountered item is a narrative sequence, `A.6.3.NAR` governs only the selected-source carry-through, ordering and connective account, loss, reader use, and return.


