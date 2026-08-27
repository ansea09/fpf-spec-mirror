---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:14"
section_title: "Reasoning primitives"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__016_reasoning-primitives.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:14 — Reasoning primitives"
line_start: 93768
line_end: 93859
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.6.3.CSC"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "B.3"
  - "C.2.1"
  - "C.26.1"
  - "C.26.2"
  - "C.29"
  - "C.3"
  - "E.10.ROLE"
  - "E.17.ID.CR"
  - "E.24.PUB"
  - "F.0.1"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9.1"
keywords:
  - "A.10/B.3 reliance"
  - "LocalSenseClaim> projections"
  - "different <ReferenceScheme"
  - "exact F.17 SchemeSenseCell endpoints"
  - "inverse/composition checks"
  - "obtaining Bridge"
  - "optional CL evidence-strength shorthand"
  - "optional card"
  - "quantum/coarsening exit"
  - "relation-semantic profile"
  - "separate C.2.1 bounded-use claim"
---

### F.9:14 - Reasoning primitives

These are conceptual judgements, not work-enactment, card-completion, registry, publication, permission, or authorization rules.

#### F.9:14.1 - Direct Bridge occurrence

```text
P = <kind, symmetry-or-orientation, endpoint-readings,
     relation-condition, applicability-and-as-of,
     Boolean-truth-condition, stop-dependencies>

Bridge(A, B; P) obtains
iff
  A and B resolve to exact F.17 SchemeSenseCell values,
  semanticContext(A) != semanticContext(B),
  applicable(P, A, B, asOfBasis),
  bridgePredicate(P, A, B) = true,
  and requiredDependencies(P) are present.
```

No proposed use, direction, use-specific rule, loss tolerance, claim polarity, reliance result, or card is a component of `P`.

#### F.9:14.2 - Bounded-use proposition

```text
Bridge(A,B;P) obtains as b
and C is a C.2.1 claim with
  EntityOfConcern = b,
  ClaimGraph designating <u,d,r,t,polarity>,
  and an effective ReferenceScheme interpreting those designations
=> C says whether b is suitable for exactly <u,d,r,t>.
```

Changing `u`, `d`, `r`, or `t` changes `C`; it does not change `b`. Affirmative polarity is not evidence reliance, assurance, authorization, or occurrence.

#### F.9:14.3 - Ordinary A.10 reliance

```text
C is current and affirmative for <u,d,r,t>
and EP is the exact A.10 evidence-provenance graph relation for C and u
and RelianceDisposition(EP,u,d,r,t) = pass
=> the reader may rely on C only for that bounded evidence use.
```

A non-passing or narrower disposition supplies no support for the attempted use. The disposition is a local A.10 classification statement, not a new result kind.

#### F.9:14.4 - B.3 assurance branch

```text
C is current and affirmative for <u,d,r,t>
and an actual named assurance claim about this use is current
and its B.3 AssuranceResult carries the same bounded assurance use
and disposition = supported-for-use
=> assurance supports only that bounded use.
```

A `narrowed` disposition supports only its stated narrower use. `abstain`, `evidence-needed`, `reopen`, or `blocked` stops the attempted use. If no assurance claim is current, do not open B.3. A consequence, display, or local threshold creates no assurance claim.

#### F.9:14.5 - Receiving occurrence stays separate

```text
Bridge b obtains
and C is affirmative for proposed use u
and current reliance supports C for u
=> no Work, assertion, publication, relation, or operation application follows.
```

An actual receiving object exists only when its subject pattern supplies its participants or arguments, obtaining or performance facts, and identity.

#### F.9:14.6 - Direction guard

Relation symmetry or orientation does not select `d`. Each proposed direction receives its own bounded-use claim. For an inclusion relation, a broader-to-narrower proposal normally requires refined endpoint senses and a separately tested Bridge; it cannot borrow safety from the inverse reading.

#### F.9:14.7 - Chained-use guard

```text
Bridge(A,B;P1) obtains
and Bridge(B,C;P2) obtains
=> no Bridge(A,C;P3) follows.
```

A composite proposed use must cite each obtaining Bridge, state one exact composite rule and accumulated tolerance in its own claim, and recover current reliance for that claim. If a direct A-to-C correspondence is needed, test it independently.

#### F.9:14.8 - Candidate-card guard

```text
candidate or negative Bridge Card exists
=> no positive Bridge occurrence follows.
```

The card concerns the admitted direct Bridge relation kind and places proposed endpoints, profile, ClaimMode, and polarity in its ClaimGraph. It creates neither relation nor receiving occurrence.

