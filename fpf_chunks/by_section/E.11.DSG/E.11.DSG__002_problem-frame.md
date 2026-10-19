---
chunk_kind: "child"
pattern_id: "E.11.DSG"
pattern_title: "Architectural Reference"
section_id: "E.11.DSG:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.DSG/E.11.DSG__002_problem-frame.md"
commit_sha: "9a8471b145233a83524724caa5d7eb50ee151185"
heading_path:
  - "E.11.DSG — Architectural Reference"
  - "E.11.DSG:1 — Problem frame"
line_start: 102778
line_end: 102791
dependencies:
  - "C.2.1"
  - "C.2.P"
  - "C.20"
  - "E.11"
  - "E.11.PFP"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.4"
  - "E.4.PFAD"
  - "E.4.PFR"
  - "E.9"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
---

### E.11.DSG:1 - Problem frame

#### E.11.DSG:1.1 - Use this when

Use this pattern when writing an architectural account for the users of a named method language: how it is assembled, why its parts and connections are selected, what they make possible and how to use them. The account can explain one framework, a DPF Suite or FPF Library. Understanding its choices also lets a user question a premise or propose an improvement. Call it `<name of the explained whole> Architectural Reference`. It carries the public architecture, shared explanation and useful question-led entries, with returns to the full Methods and evidence. It is a support unit of the explained language unless independent use or change justifies a separate product boundary; this function does not by itself make the account another framework or the discipline being described.

**First useful result.** Give the reader a usable account of the whole's purpose, constituents, connections and limits, then a direct way into the needed explanation or Method. For a working question, give an answer or honest blocker. Distinguish an available result, a MethodDescription to use, direct-source evidence and a result still missing. Explain each necessary contribution and end that entry with an ordinary stop or return. Do not fill a missing result with another title.

**Primary EntityOfConcern.** One architectural-reference episteme: the public account of one named language assembly under C.2.1. Its content belongs to the explained whole and can be embedded in that whole's publication or separately carried. It can share the whole's publication and change boundary or have an independently useful product boundary under E.4:4.1. Separate files alone settle neither choice.

**What this buys.** The reader can understand the whole without its internal development records, select a useful route, recognize constituent and external contributions, and reach the full Methods, cases, limits and evidence needed to act or adapt the language.

**Not this pattern when.** Use E.4:4.2 and E.4.PFAD to decide which discipline a Suite describes and how its subdisciplines compose it. Use E.8 and the applicable Core or DPF authoring pattern to develop an unwritten Method, including a composite Method. Use a known pattern directly when its contribution is already clear; the architectural reference is not a prerequisite for that use. A separate curriculum or instructional Guide is a pedagogical companion. E.11.PFP governs framework publication form; it does not turn a supporting architectural reference into another framework. Describing FPF Library's connections does not claim a discipline above all its DPFs.

