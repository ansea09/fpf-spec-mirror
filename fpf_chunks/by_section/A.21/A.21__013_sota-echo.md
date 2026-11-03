---
chunk_kind: "child"
pattern_id: "A.21"
pattern_title: "Gate Decisions from Independent Check Results"
section_id: "A.21:11"
section_title: "SoTA echo"
source_path: "FPF-Spec.md"
output_path: "by_section/A.21/A.21__013_sota-echo.md"
commit_sha: "d5df418106507cff0972788834c0bf8825597de0"
heading_path:
  - "A.21 — Gate Decisions from Independent Check Results"
  - "A.21:11 — SoTA echo"
line_start: 40098
line_end: 40106
dependencies:
  - "A.10"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.20"
  - "B.3"
  - "C.3.2"
  - "E.17"
  - "E.18"
  - "F.17"
  - "F.19"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.6"
keywords:
---

### A.21:11 - SoTA echo

| Basis or practice comparison | Move used in A.21 | Limit |
| --- | --- | --- |
| The join-semilattice defined in §4.5 | Use the associative, commutative, idempotent worst-result join after explicit profile mapping. | Algebra does not make unknown or unrun input neutral. |
| [Open Policy Agent: Rego policy evaluation](https://www.openpolicyagent.org/docs/policy-language), including undefined results and explicitly declared defaults | Keep the applicable policy, its inputs and evaluated result recoverable; A.21 separately specifies the mapping to a bounded action. | Rego values and undefined results do not themselves define A.21 decision values or authority. |
| [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) and [SLSA v1.2 provenance](https://slsa.dev/spec/v1.2/provenance) bind typed attestations and production information to identified artifacts | Retain the subject and claim references needed by the declared audit, transfer or reuse. Publication follows the receiving use. | Attestation or provenance information supplies neither the gate decision nor the truth of every source claim; A.21 keeps those judgements separate. |
| Structural-crossing rules supplied by `E.18` | Apply crossing equations to the identified crossing when its rule requires them. | A structural crossing does not imply a semantic Bridge; each applies only when its own relation and use are current. |

