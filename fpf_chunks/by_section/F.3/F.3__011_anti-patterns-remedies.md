---
chunk_kind: "child"
pattern_id: "F.3"
pattern_title: "Source-Local Sense Clustering"
section_id: "F.3:10"
section_title: "Anti-patterns & remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/F.3/F.3__011_anti-patterns-remedies.md"
commit_sha: "0c3ef3d3921bb3176096e3e6102dd819c42f6446"
heading_path:
  - "F.3 — Source-Local Sense Clustering"
  - "F.3:10 — Anti-patterns & remedies"
line_start: 93378
line_end: 93392
dependencies:
  - "A.11"
  - "A.7"
  - "E.10.D1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "LocalSenseClaim"
  - "alias consolidation"
  - "counterexample"
  - "effective ReferenceScheme"
  - "optional SchemeSenseCell"
  - "source expression"
---

### F.3:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | String = sense | Surface identity decides the cluster. | Different propositions collapse. | Compare argument patterns and entailments. |
| **A2** | Cross-source creep | A BPMN use is folded with a PROV use inside F.3. | The interpretation basis changes unnoticed. | Finish each local claim first; test any relation in F.9. |
| **A3** | Over-granulation | *SLO* and its full form become separate claims without a difference in use. | Friction rises without gain. | Consolidate source-blessed aliases. |
| **A4** | Under-granulation | Diagram node and real occurrence share one claim. | Later inferences contradict each other. | Split on argument or entailment conflict and add a counterexample. |
| **A5** | Imported definition | A dictionary replaces the selected source passages. | The result is no longer source-local. | Ground the claim in the actual passages. |
| **A6** | Label drift | Plain adds scope not present in Tech or the claim. | The cold reader learns the wrong concept. | Keep both labels within the same claim. |
| **A7** | Substantive leakage | A sense line contains policies, equations, or kind criteria. | The lexical note is asked to establish a substantive fact about another value. | Route the claim to its direct pattern. |
| **A8** | Edition blend | Two editions with changed usage share one unqualified claim. | Replay and comparison become unreliable. | State each basis; merge only if evidence supports the same claim. |
| **A9** | Cue worship | Similar collocations are treated as proof. | Correlation replaces source meaning. | Use cues to locate passages, then test propositions. |
| **A10** | Time blur | A design-time use and a run-time occurrence are clustered together. | MethodDescription and Work collapse. | Split and use F.11, A.3, and A.15 for the substantive distinction. |

