---
chunk_kind: "child"
pattern_id: "F.8"
pattern_title: "Mint-or-Reuse Decision"
section_id: "F.8:12"
section_title: "SoTA-Echoing - Source-Use"
source_path: "FPF-Spec.md"
output_path: "by_section/F.8/F.8__015_sota-echoing-source-use.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "F.8 — Mint-or-Reuse Decision"
  - "F.8:12 — SoTA-Echoing - Source-Use"
line_start: 83499
line_end: 83510
dependencies:
  - "A.11"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.7"
  - "A.8"
  - "C.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9"
  - "F.1"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "decision lattice"
  - "minting new U-kinds"
  - "parsimony"
  - "reuse"
  - "type explosion"
---

### F.8:12 - SoTA-Echoing - Source-Use

| Practice line | What FPF adopts | Practical implication |
| --- | --- | --- |
| Controlled-vocabulary and terminology practice | Preferred labels, aliases, definitions, scope notes, and deprecated labels are separate fields. | F.8 decides admission; F.5 and F.18 then name without confusing alias with meaning change. |
| Ontology engineering and conceptual modeling | New classes or kinds are expensive and should be tested against existing relations, contexts, and constraints. | New U-kind candidates require `E.24.UK` admission, irreducibility, and decision basis, not comfort. |
| Domain-driven bounded-context practice | Meaning is local before it is shared. | Reuse local sense labels first; cross-context reuse needs bridge and row discipline. |
| Authorization and policy-reference practice | Policy identifiers must resolve to definitions and governance decisions. | Policy ids use `PolicyIdRef`; the id is not itself permission, gate passage, or evidence. |
| FPF role and episteme ontology | Work-facing roles, role descriptions, assignments, work, evidence use, and status use are distinct. | Role-like source expressions are split by kind before durable naming. |

Source-use boundary: a source tradition may supply candidate words and current practice pressure. It does not select the FPF decision kind. The decision kind follows the recovered value or relation and the direct governing pattern.

