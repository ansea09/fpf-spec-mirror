---
chunk_kind: "child"
pattern_id: "A.6.RSIG"
pattern_title: "Recognition Signatures for Descriptions"
section_id: "A.6.RSIG:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIG/A.6.RSIG__005_solution.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "A.6.RSIG — Recognition Signatures for Descriptions"
  - "A.6.RSIG:4 — Solution"
line_start: 10746
line_end: 10890
dependencies:
  - "A.6"
  - "A.6.P"
  - "E.10"
  - "F.18"
keywords:
---

### A.6.RSIG:4 - Solution

#### A.6.RSIG:4.1 - Relation-signature object and non-goals

`A.6.RSIG` governs description-recognition signatures in general: the
first-contact cue structure by which one reader can recover what encountered
description is live, what carrier or projection exposed it, what it applies to,
what excludes it, which `definitionEpistemeRef` identifies its defining `U.Episteme`, and which nearby false
description or wrong defining `U.Episteme` must be rejected.

Here "description-recognition signature" is lower-case authoring and reading
discipline. It is not `U.Signature`, not a Signature Stack object, not a new
Description object by default, not a `U.*` kind, and not a specialization of
`A.6.0` unless another pattern explicitly promotes a particular declaration.

The encountered carrier or projection may help recognition; it does not become
authoritative merely by being encountered. When this pattern talks about an
encountered publication or projection, that wording does not mint a new surface
kind; use an existing publication face, publication form, interop publication form,
`U.View`, card, or lane kind only when that kind is actually being made.

Use `definitionEpistemeRef` for the defining `U.Episteme`. If the definition is available only through one publication, cite the `U.EpistemePublication` that publishes it separately; the publication, projection, or carrier does not become the defining episteme merely because it exposed the definition to the reader.

`A.6.RSIG` does not govern:

- general information architecture or search UX;
- documentation layout or publication-face selection;
- pattern-entry discoverability across a pattern language;
- the full semantics of the description itself;
- lexical repair, alias acceptance, or naming governance as such;
- graph ontology, workflow sequencing, or runtime route semantics.

#### A.6.RSIG:4.2 - Two-level description-recognition shape

**Reader-visible minimum.** For ordinary reader-facing use, the minimum is not a card. One or two good
sentences may be enough if they make recoverable:

1. what this description is for;
2. when it applies;
3. when it does not apply;
4. which definitionEpistemeRef applies;
5. what nearby false reading or wrong defining `U.Episteme` to reject.

**Review-expanded shape, only when needed.** When the recognition entry load is
load-bearing or under review, use the expanded recoverability shape:

```text
description_seen
encountered_carrier_or_projection
reader_viewpoint
case_signal_or_access_condition
applies_to
excludes
expected_first_recognition_gain
first_admissible_entry_stop_or_reroute
definitionEpistemeRef
projection_role_if_any
nearby_false_description_or_wrong_definition_episteme
```

This shape is a review aid, not a mandatory form for every encountered
description. It exists to keep description, carrier, projection, and definitionEpistemeRef from
collapsing into one overloaded publication label or projection label.

#### A.6.RSIG:4.2.1 - Minimal local repair and review sequence

Use this sequence when authoring or reviewing one recognition-signature repair:

1. Name the `description_seen` and the reader viewpoint in one concrete first
   sentence.
2. Name the encountered carrier or projection if confusing it with authority is
   a live risk.
3. State what the description applies to and what excludes it.
4. Name the defining `U.Episteme` to inspect first.
5. Name one nearby false description or wrong defining `U.Episteme` that looks
   plausible in the same situation.
6. State the first admissible entry stop or neighboring-pattern application.
7. If that stop cannot be stated without A.6.B claim routing, publication-face law,
   lexical repair, or cross-pattern comparison, apply the appropriate neighboring pattern instead of
   stretching `A.6.RSIG`.

Minimal admissible output:

- one first-contact recognition statement the reader can use immediately;
- one explicit defining `U.Episteme`;
- one explicit false-neighbor rejection;
- one admissible entry stop or reroute.

#### A.6.RSIG:4.3 - Parent cases

`A.6.RSIG` keeps the main parent cases explicit:

- **boundary-description recognition**: can one reader recover what one
  boundary-presented description is for before L/A/D/E-classified claim structure becomes
  the dominant entry load;
- **method-description applicability recognition**: can one reader recover
  whether one method description is the right description to inspect, reject, or
  compare under the live entry load;
- **interface/access-description recognition**: can one reader recover the
  right access or interface description without confusing it with promise,
  execution, or downstream effect semantics;
- **pattern-local recognition-signature case**: can one reader recover one
  pattern opening as the right first description to inspect before broader
  pattern-language comparison begins.

#### A.6.RSIG:4.4 - Neighbor boundaries

Neighbor boundaries remain explicit:

- `A.6.B` governs routed `L/A/D/E` claim structure when the boundary
  description is already in routed-claim territory;
- `E.17.0 / E.17` govern admissible view and publication-face projection when the
  same recognition entry load is carried through published views;
- `E.10.D2` and the `E.10 / F.18 / A.6.P` lane govern lexical repair,
  collision checks, and naming survival;
- `C.25 / C.16.Q` govern formal quality treatment when the discoverability or
  recognition claim becomes explicitly evaluative;
- the relevant authoritative pattern body governs pattern semantics when the
  encountered description is one pattern-local opening.

The four-part split for pattern-local recognition is:

| Recognition concern | Governing FPF pattern or source-maintenance role assignment | What it governs |
| --- | --- | --- |
| Generic first-contact description recognition | `A.6.RSIG` | The neutral cue shape: description, carrier or projection, definitionEpistemeRef, exclusions, false neighbor. |
| Local placement and form | `E.8` | How the pattern's `Problem frame` carries the first-reading role. |
| Actual local semantics | The pattern itself | The pattern's relation-signature object, solution, consequences, and conformance law. |
| Cross-pattern comparison | `E.11` and `I.2` | Candidate patterns, tempting wrong patterns, entry-load reclassification, and expanded entry-disambiguation cases. |

#### A.6.RSIG:4.5 - No-minting rule

This pattern does not mint:

- one standalone `U.Discoverability`;
- one new `U.Signature`, Signature Stack object, `U.Characteristic`, `CHR`, or
  local `Q-Bundle`;
- one publication face kind, publication form kind, interop publication form kind, carrier kind, `DescriptionKind`, relation kind, graph ontology, pattern-reference publication
  graph, or process-family claim;
- one universal reader-orientation role.

If a recognition-signature entry load is promoted into a quality claim with a higher evidence requirement,
typed signature object, reusable description object, or publication-face law,
that promotion is explicit and handled by the existing neighboring
patterns.

