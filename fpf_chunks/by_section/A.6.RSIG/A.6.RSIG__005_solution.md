---
chunk_kind: "child"
pattern_id: "A.6.RSIG"
pattern_title: "Recognition Signatures: Find the Defining Episteme for a Description"
section_id: "A.6.RSIG:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIG/A.6.RSIG__005_solution.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.6.RSIG — Recognition Signatures: Find the Defining Episteme for a Description"
  - "A.6.RSIG:4 — Solution"
line_start: 14183
line_end: 14307
dependencies:
  - "A.6"
  - "A.6.P"
  - "E.10"
  - "F.18"
keywords:
---

### A.6.RSIG:4 - Solution

#### A.6.RSIG:4.1 - Recognition-cue discipline

A recognition cue makes the description, its purpose and relevant applicability conditions recoverable, with a reference to its defining account. Identify the encountered carrier or projection when that distinction affects recognition.
Reject a nearby reading or wrong defining `U.Episteme` only when it passes F.19's
grounded-guard test: the rejected reading has an independent local ground, is
plausible for the intended reader, and changes truth, understanding, selection,
safety, stop, reliance, or action. Use the
smallest clear correction; do not invent an alternative to fill the cue shape.

Here "description-recognition signature" is a lower-case authoring and reading
discipline, not by itself a typed `U.Signature` or a new formal kind. A typed
declaration requires the applicable neighboring pattern's explicit conditions.

The encountered carrier or projection may help recognition; it does not become
authoritative merely by being encountered.

Point to the defining `U.Episteme` through the available publication. Identify the E.24.PUB publication occurrence separately when its identity changes which definition or use is available. The publication and its carrier keep their own identities.

`A.6.RSIG` does not govern:

- general information architecture or search UX;
- documentation layout or publication-face selection;
- pattern-entry discoverability across a pattern language;
- the full semantics of the description itself;
- lexical repair, alias acceptance, or naming governance as such;
- graph ontology, workflow sequencing, or runtime route semantics.

#### A.6.RSIG:4.2 - Two-level description-recognition shape

**Reader-visible minimum.** Ordinary prose is sufficient when it makes these values recoverable:

1. what this description is for;
2. when it applies;
3. any exclusion that changes recognition or use;
4. which definitionEpistemeRef applies;
5. what nearby false reading or wrong defining `U.Episteme` to reject, when
   the grounded-guard condition in §4.1 holds.

**Expanded questions when needed.** Use the following questions when the shorter cue leaves a consequential recognition ambiguity unresolved. Existing prose can carry the answers; a separate form is optional.

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

Use the exclusion and false-neighbor fields only when the grounded-guard condition in §4.1 holds. The viewpoint field names the reader’s perspective; identify a formal U.Viewpoint episteme only when that separate relation matters.

The questions help distinguish the encountered description and its defining account from their publication or carrier when those differences affect the choice.

##### A.6.RSIG:4.2.1 - Minimal local repair and review sequence

Use this sequence when authoring or reviewing one recognition-signature repair:

1. Name the encountered description and the reader’s question.
2. Name the encountered carrier or projection if confusing it with authority is
   a live risk.
3. State the applicability and any exclusion needed to choose the description.
4. Name the defining `U.Episteme` to inspect first.
5. When the grounded-guard condition in §4.1 holds, name the nearby false
   description or wrong defining `U.Episteme` to reject.
6. State the useful next inspection or the missing basis that prevents it.
7. If that stop cannot be stated without A.6.B claim routing, publication-face law,
   lexical repair, or cross-pattern comparison, apply the appropriate neighboring pattern instead of
   stretching `A.6.RSIG`.

The result is the recognition statement, its defining source reference and the useful next inspection or limitation. Include a false-neighbor correction only under §4.1.

#### A.6.RSIG:4.3 - Common uses

The same recognition question occurs in several settings:

- **boundary-description recognition**: can one reader recover what one
  boundary-presented description is for before the reader needs to classify its
  claims as L/A/D/E;
- **method-description applicability recognition**: can one reader recover
  whether one method description is the right description to inspect, reject, or
  compare for the reader's question;
- **interface/access-description recognition**: can one reader recover the
  right access or interface description without confusing it with promise,
  execution, or downstream effect semantics;
- **pattern-local recognition-signature case**: can one reader recover one
  pattern opening as the right first description to inspect before broader
  pattern-language comparison begins.

#### A.6.RSIG:4.4 - Neighbor boundaries

Neighbor boundaries remain explicit:

- use `A.6.B` when the reader needs to classify the boundary claims as `L/A/D/E`;
- `E.17.0` tests viewpoint/view membership; `E.17` publishes reader-facing forms of an already accepted engineering account;
  use `E.24.PUB` when publication occurrence, form, or carrier identity affects the recognition use;
- `E.10.D2` recovers description-episteme and specification-use distinctions;
  use `E.10` cues within `F.19` for wording, `A.6.P` for under-specified direct relations, and `F.18` for durable naming and its collision checks;
- `C.16.Q` repairs overloaded recognition or discoverability quality wording;
  `C.25` applies when the quality-family claim depends on several differently typed contributors; a single-Characteristic claim stays with its direct Characteristic pattern;
- the relevant authoritative pattern body governs pattern semantics when the
  encountered description is one pattern-local opening.

The four-part split for pattern-local recognition is:

| Recognition concern | Governing FPF pattern or source | What it governs |
| --- | --- | --- |
| Generic first-contact description recognition | `A.6.RSIG` | The neutral cue shape: description, carrier or projection, definitionEpistemeRef, exclusions, and a false neighbor when §4.1's grounded-guard condition holds. |
| Local placement and form | `E.8` | How the pattern's `Problem frame` carries the first-reading role. |
| Actual local semantics | The pattern itself | The pattern's governed object, solution, consequences, and conformance law. |
| Cross-pattern comparison | `E.11` | Candidate patterns, tempting wrong patterns, reclassification of the reader's question, and expanded entry-disambiguation cases. |

#### A.6.RSIG:4.5 - When a neighboring pattern is needed

If the task requires a quality claim, typed signature declaration, reusable
description, or publication-face rule, use the neighboring pattern that governs
that object or claim, including its evidence requirements. The recognition cue
alone does not establish that result.

