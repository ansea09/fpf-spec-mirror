---
chunk_kind: "child"
pattern_id: "A.3.4"
pattern_title: "U.Transformation: Bounded Change Under Conditions"
section_id: "A.3.4:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.4/A.3.4__003_problem-frame.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "A.3.4 — U.Transformation: Bounded Change Under Conditions"
  - "A.3.4:1 — Problem Frame"
line_start: 7753
line_end: 7778
dependencies:
  - "A.1"
  - "A.10"
  - "A.11"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.22"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "A.3.3"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "C.32.P2S"
  - "E.18"
  - "E.18.1"
  - "E.24"
  - "E.24.UK"
  - "F.18"
  - "G.11"
keywords:
  - "actual bounded change"
  - "actual subject facts"
  - "changed referent"
  - "continuity and reidentification"
  - "occurrence boundary"
  - "transformation composition"
---

### A.3.4:1 - Problem Frame

FPF often needs to talk about change in physical systems, engineered artifacts, organizations, epistemes, documents, architectures, programs, regulatory situations, and research objects. The same source phrase may say "algorithm", "process", "workflow", "procedure", "mechanism", "run", "trajectory", "transition", "stabilization", "editing", "migration", "optimization", "morphism", "construction", or another field-specific name for a change, transformer, or change structure.

Those phrases are not enough to recover the object under concern. A CRISPR editing protocol, a nuclear-plant operating change, a platform refactoring, a model update, a document repair, an architecture move, a proof construction, and a method-result carry-through can all involve transformation, but the FPF values under use differ.

FPF already has strong neighboring patterns:

- `A.3` for transformer constitution: acting system bearing `TransformerRole`, method description, method, and actual work;
- `A.3.1` for `U.Method`;

- `A.3.2` for `U.MethodDescription`;
- `A.3.3` for `U.Dynamics`;
- `A.6.0` and `A.6.5` for signatures and slot discipline;
- `A.6.1` and `E.20` for mechanisms;
- `A.15.2` and `A.15.1` for work plans and dated work;
- `E.18` for transformation-flow structures;
- `E.18.2` for mathematical descriptions of transformation-flow structures;
- `E.18.1` for problem-to-work carry-through;
- `C.27.TA` for positive temporal aspects;
- `C.27` for temporal-claim adequacy;
- `C.29` for mathematical-lens use;
- evidence, gate, assurance, source, result, decision, and publication patterns for their own claims.

What is missing is a positive way to identify the actual bounded change first and then recover each neighboring object through its own direct relation, without turning a checklist or description into the transformation ontology.

