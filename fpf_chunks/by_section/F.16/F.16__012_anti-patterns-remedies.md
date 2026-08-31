---
chunk_kind: "child"
pattern_id: "F.16"
pattern_title: "Worked-Example Template (Cross-Domain)"
section_id: "F.16:11"
section_title: "Anti-patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.16/F.16__012_anti-patterns-remedies.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "F.16 — Worked-Example Template (Cross-Domain)"
  - "F.16:11 — Anti-patterns & remedies"
line_start: 97961
line_end: 97975
dependencies:
  - "A.10"
  - "A.15"
  - "A.3"
  - "A.6.1"
  - "A.6.RCD"
  - "B.1.5"
  - "B.3"
  - "C.16.P"
  - "E.10.D1"
  - "E.13"
  - "F.0.1"
  - "F.1"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "actual values"
  - "boundary"
  - "direct relations"
  - "evidence"
  - "exact sources"
  - "optional cell"
  - "optional comparison table"
  - "practical gain"
  - "working situation"
---

### F.16:11 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **AP-1** | Architecture before question | The page opens with cells and routes but no recognizable problem. | Reader cannot tell what changes in practice. | Lead with situation, gain, and worked claim. |
| **AP-2** | Mandatory row | Every example must span two sources and contain a Concept-Set row. | Ceremony replaces the simplest adequate explanation. | Make the table optional; use direct prose when enough. |
| **AP-3** | Row-created sameness | Entries are “the same for this claim” because they share a row. | Layout becomes an ontological assertion. | State the actual relation and evidence, or show a contrast. |
| **AP-4** | Cell as subject | A RoleDescription, promise, Work, observation, result, or status is anchored to one cell as though the cell were that value. | Lexical address replaces the subject. | Name the actual value; cite a cell only for local wording. |
| **AP-5** | Generic Bridge | All cross-domain relations are labelled Bridges. | MethodDescription membership, description use, enactment, indicator, evidence, assignment, and fulfilment collapse. | Use each defining or testing pattern; recover unsupported indicator wording through C.16.P and A.6.RCD, and reserve F.9 for local-meaning relations. |
| **AP-6** | Global trigger word | *Role*, *function*, *process*, or *service* appears without recovering its subject. | Polysemy hides objects and relations. | Apply E.10 and F.0.1 and then choose precise plain wording. |
| **AP-7** | Design-time and run-time blur | A design description is narrated as Work. | Plan and occurrence collapse. | Use F.11, A.3, and A.15 and state the actual relation. |
| **AP-8** | Edition haze | Source name lacks the edition that controls meaning. | The example cannot be replayed. | Name the source, edition, and relevant passage. |
| **AP-9** | Evidence silence | The result appears without observations, source claims, or reliance basis. | Confidence cannot be assessed. | Show evidence use, limits, and non-use boundary. |
| **AP-10** | Ontologist’s shorthand | Predicate notation replaces an ordinary explanation. | Precision becomes inaccessible to the cold reader. | Lead with plain language; retain compact notation only when it genuinely shortens a repeated calculation. |

