---
chunk_kind: "child"
pattern_id: "C.2.8"
pattern_title: "U.ExtractableStructuralInformation"
section_id: "C.2.8:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.8/C.2.8__006_archetypal-grounding.md"
commit_sha: "aa10af7e8221518114822d00bb9cf11e6c41f6b2"
heading_path:
  - "C.2.8 — U.ExtractableStructuralInformation"
  - "C.2.8:5 — Archetypal Grounding"
line_start: 45094
line_end: 45134
dependencies:
  - "A.17"
  - "A.18"
  - "A.6.3.NAR"
  - "C.16"
  - "C.2.1"
  - "C.2.4"
  - "C.29"
  - "C.33"
  - "E.17.EFP"
keywords:
  - "bounded observer"
  - "description comparison"
  - "epiplexity"
  - "extractable structure"
  - "reader preparation"
  - "reading budget"
  - "structural information"
---

### C.2.8:5 - Archetypal Grounding

#### C.2.8:5.1 - Architecture account in prose and a diagram

A service account states:

> The API returns “stored” only after the Store confirms a durable write. Reports read a Replica updated from Store and may lag by five minutes. A synchronous report query to Store was rejected because report bursts must not delay request writes. If required report freshness becomes one second, reconsider the replica update design.

A second expression adds this diagram while retaining those four sentences:

```text
API --write--> Store --update--> Replica --read by--> Reports
API <--durable-write confirmation-- Store
```

The reader is an engineer familiar with durable writes and replicas. Select the acknowledgment dependency, report-source/lag relation, rejected alternative with its reason, and reconsideration condition. Both forms expose the same claims; the described architecture is unchanged. Compare recovery with the same three-minute budget and source access. The diagram's presence alone establishes no advantage.

Suppose a reading trial recovers three selected relations from the prose and all four from the combined expression. Report that bounded observed difference and identify the additional relation. If a source paragraph was supplied only before the second reading, the comparison also changed assistance. If the same reader encountered both forms, previous reading may contribute. These conditions prevent attributing the whole difference to form alone.

A reader unfamiliar with replication may need a prerequisite explanation. Adding its substantive claims changes the account as well as its expression. If the design requirement changes to one-second freshness, the account supplies reconsideration of the replica update design. It does not supply a replacement architecture. C.33 can record this captured structure and the source return needed for the next design question.

#### C.2.8:5.2 - A technical pattern's explicit plan

The plan in C.2.4:13.2 names Maintenance Team 2, Pump P-17, isolation, seal replacement and restoration only after LT-9 passes. For its planning use, the actor, action order and condition are explicit enough for AE4. A maintainer can recover the restore-after-pass dependency even when the note does not explain the LT-9 procedure.

If the selected use is carrying out that test, the applicable procedure must be available as a prerequisite or source return. The plan's articulation result does not teach the missing procedure. The useful ESI comparison names which required test relations the reader can recover with the available source access; it does not replace the planning judgment with a larger or smaller AE number.

#### C.2.8:5.3 - An observer with a two-statement budget

Let E describe edges A→B, B→C, A→D and D→C. Form P1 lists them in that order. Form P2 lists A→B, A→D, B→C, D→C. Observer O reads the first two edge statements and returns every two-edge path supported by those edges. Select the paths A→B→C and A→D→C as the structural denominator.

P1 gives O the edges needed for A→B→C; P2 gives two edges leaving A and no complete selected path. Under the declared count, the results are 1 and 0 out of two selected paths. With four statement reads, the same procedure recovers both paths from both forms.

This result follows from the stated algorithm and budget. It is neither a human-comprehension observation nor a Finzi estimate. It shows one characteristic applied to the same expressed claims under a precisely bounded computational observation.

#### C.2.8:5.4 - A whole-framework architectural rationale

A framework maintainer has several individual pattern-quality results and needs to decide what they establish about the framework as a whole. E.4.FPF:3–4 explains the different questions: E.21 evaluates a pattern; E.2.DA evaluates whole-FPF Pillar adequacy. The selected structure is this relation between the two scopes and the corresponding return.

For a reader who can already use those evaluation questions, the existing rationale and direct links may be sufficient. A less prepared reader may need the questions explained before the links are useful. An ESI comparison checks recovery of that scope distinction and next return under stated preparation and access. Counting the account's headings would not answer it.

