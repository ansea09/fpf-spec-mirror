---
chunk_kind: "child"
pattern_id: "C.3.2"
pattern_title: "Kind Intent, Membership Judgment, and Extension"
section_id: "C.3.2:5"
section_title: "KindSignature Declaration"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.2/C.3.2__007_kindsignature-declaration.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "C.3.2 — Kind Intent, Membership Judgment, and Extension"
  - "C.3.2:5 — KindSignature Declaration"
line_start: 44590
line_end: 44608
dependencies:
  - "A.14"
  - "A.2.6"
  - "A.6.0"
  - "C.2.1"
  - "C.2.3"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.3"
  - "C.3.4"
  - "C.3.5"
  - "C.3.A"
  - "E.24.UK"
keywords:
  - "KindExtension representation"
  - "KindSignature declaration episteme"
  - "candidate classification"
  - "local kind"
  - "true/false/unknown"
---

### C.3.2:5 - KindSignature Declaration

Author a reusable `KindSignature` only when a named receiving use needs the criterion and assumptions to persist across more than one classification.

Its claim content declares:

- the exact local kind that is its `EntityOfConcern`;
- the candidate `ValueKind`: the direct kind or value interpretation admitted as candidate input;
- the membership criterion in terms of direct governed candidate qualities, relations, constructive grounding, or other features;
- the exact `U.ContextSlice` conditions under which the criterion can be evaluated;
- the effective `U.ReferenceScheme`;
- named assumptions, dependencies, standards, versions, units, and temporal policy;
- its `U.Formality`;
- an optional `ExtentRule` stating how repeated candidate evaluations feed an extension when a varying extension is current.

In A.6.0 terms, `SubjectKind` is the broad candidate kind and `RangedValueKind` is the finite judgment value kind `{true, false, unknown}`. `ExtentRule` is declaration content, not a new ontic relation. Formality characterizes the declaration episteme—not the local kind, candidate, candidate value, judgment truth, or extension. A claim that relies on the signature content evaluates that dependency on its own F–G–R support path; raising signature formality does not upgrade an unrelated claim.

A changed membership criterion, evaluation-domain declaration, `EntityOfConcern` referent, or effective reference scheme identifies another `U.Signature` episteme edition. C.3.1 separately decides whether the same local kind continues across that declaration change.

