---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__008_conformance-checklist.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:7 — Conformance Checklist"
line_start: 84427
line_end: 84441
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:7 - Conformance Checklist

| Requirement | Required result |
|---|---|
| `CC-ADA-1` | Declared use and stop condition are written before evaluation. |
| `CC-ADA-2` | The evaluated decision relation and optional ADR projection are cited. |
| `CC-ADA-3` | Every coordinate has a supported `0`–`5` value, a grounded `notTriggered` disposition, or an explicitly unestablished dependent value with its missing basis. Keep the complete evaluation draft while a required judgement is unestablished, retaining supported results. |
| `CC-ADA-4` | Every value has adjacent-value rationale, not only a number. |
| `CC-ADA-5` | No coordinate values are averaged or converted into one global score. |
| `CC-ADA-6` | Weak coordinates name repair pattern refs and repair instructions. |
| `CC-ADA-7` | Evidence, assurance, gate, measurement, eval, publication, Method, Work and pattern-quality claims retain their distinct meanings and applicable definitions or tests; exact ClaimGraph identity is cited when the claim or reliance needs it. |
| `CC-ADA-8` | A project-local ADA record names both `projectWorkOccurrenceRef` and `architectureDecisionEvaluationProjectUseRelationRef`; the evaluated decision's relation, the suffix, or either field alone asserts no locality. |
| `CC-ADA-9` | A local evaluator kind and a System-classification judgment use separate optional refs and neither requires an assignment. A claim about a particular dated evaluation Work occurrence first recovers the evaluator through A.13 and names independently admitted A.15.1 Work. Ordinary evaluation retains the operation, material conditions and support needed for its result. Assignment species, occurrence, and F.6 refs are optional and appear only when the ADA record or receiving use represents precise assignment-bound attribution; a missing or failed F.6 relation alone leaves independently admitted Work intact, with any questioned admission premise rechecked as above. An operation application and result episteme remain separate. Keep those objects and relations distinct, preserving the admission dependencies stated above; a label or record does not establish the other facts. |
| `CC-ADA-10` | Each evaluation binds its exact claim scope, relevant context slices and reference scheme, preserving every declared selector and any plane, time qualification or input projection required by the judgement or receiving use. The declared-use label and coordinate table do not replace those conditions. |

