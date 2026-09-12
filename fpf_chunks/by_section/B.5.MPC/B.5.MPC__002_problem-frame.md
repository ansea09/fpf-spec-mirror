---
chunk_kind: "child"
pattern_id: "B.5.MPC"
pattern_title: "Connect Physical, Mathematical and Computational Reasoning"
section_id: "B.5.MPC:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.MPC/B.5.MPC__002_problem-frame.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "B.5.MPC — Connect Physical, Mathematical and Computational Reasoning"
  - "B.5.MPC:1 — Problem frame"
line_start: 41381
line_end: 41392
dependencies:
  - "A.15.9"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.3"
  - "B.3.3"
  - "B.5"
  - "B.5.4"
  - "C.11.DUA"
  - "C.16"
  - "C.29"
  - "C.29.1"
  - "C.29.2"
  - "C.29.3"
  - "C.39"
  - "C.40"
  - "U.Dynamics"
keywords:
---

### B.5.MPC:1 - Problem frame

**Use this when** a physical question needs contributions from mathematics and computation, and their results do not yet form an interpretable answer together. You may be choosing a robot command, determining whether a gear arrangement can turn, or organizing entry to a room with a finite stock of cards. The difficulty is to connect what the physical arrangement does, what the mathematical result establishes, and what the procedure and its execution actually produce.

Begin with the difference the answer should help you understand or make possible. Take one available contribution and explain what it would have to mean, and what else would have to hold, for that contribution to answer the question. Work the first missing connection far enough to obtain a consequence or locate the next missing contribution. For a motion command, this might already reveal that the supplied count concerns motor revolutions while the distance model concerns wheel revolutions.

The result is a connected solution, a useful conditional consequence or bound, or a particular missing connection that directs the next inquiry. This pattern specializes B.5's choice and connection of inquiry contributions for this joint physical, mathematical and computational difficulty. It governs the reasoning that connects those contributions. Physical laws, mathematical constructions, algorithm design and the engineering of an executing arrangement supply their respective subject content.

A practitioner needs enough preparation to recover the question, follow the meanings of the important quantities and operations, and recognize where specialist help is needed. The worked cases explain their elementary algebra, graph and counting constructions. A more demanding application can require additional physical theory, mathematics, computation or measurement expertise; obtain that contribution with its explanation when it is missing.

Use an already adequate calculation, implementation or operating procedure directly when its connection to the intended physical use is settled. A proof or bound can answer a physical design question before implementation is worthwhile. For an actual performance claim, add the observations, measurement relation and evidence needed for that claim; a conditional construction alone answers only what follows under its assumptions.

