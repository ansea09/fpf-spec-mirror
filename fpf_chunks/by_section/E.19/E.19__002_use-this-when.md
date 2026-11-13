---
chunk_kind: "child"
pattern_id: "E.19"
pattern_title: "Pattern Quality Gates: Review and Refresh Profiles"
section_id: "E.19:0"
section_title: "Use this when"
source_path: "FPF-Spec.md"
output_path: "by_section/E.19/E.19__002_use-this-when.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.19 — Pattern Quality Gates: Review and Refresh Profiles"
  - "E.19:0 — Use this when"
line_start: 119715
line_end: 119750
dependencies:
  - "A.15.1"
  - "A.6.P"
  - "E.10"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
  - "(see H-8)"
  - "inside the predicate)"
  - "under E.8 H-8 and CC-SG.4"
  - "where a non-deontic Invariant: predicate is required)"
---

### E.19:0 - Use this when

Use `E.19` when one new, substantially revised, or aging FPF pattern edition or bounded subset needs a repeatable admission, refresh, or return-for-repair review. Its profiles specify the questions to ask and what each conclusion means. A reviewer applies the selected questions and returns either repaired text with focused verification or actionable findings.

Use it especially when a draft looks structurally compliant but may fail on first-minute usability, primary `EntityOfConcern` stability, terminology, SoTA grounding, related-pattern boundaries, examples, anti-patterns, or shipping-facing authority claims.

**Not this pattern when.** Use `E.8` to write the pattern body. Use `E.9` to record the content decision that explains why FPF should change. Use `E.9.DA` when the question is whether one exact DRR is adequate for a declared downstream authoring use before drafting or host amendment. Its ordinary result may be precise findings or repaired text, while exact C.2.1 and coordinate-result apparatus is conditional on a requested reusable result or named reliance.

Use `E.21` for ordinal pattern-quality evaluation of one pattern version. Use `E.23` when the aim is repeated quality improvement against an object-under-improvement evaluation rather than one admission or refresh review profile.

Use local patterns for the domain rule or constraint being reviewed. Use project gate or release patterns when the question is whether a project publication, work-result record, or release candidate passes a delivery gate. E.19 reviews admission or refresh of FPF patterns. Its profiles and results do not certify a state of the world, project, publication, or release.

#### E.19:0.1 - What goes wrong if missed

Review collapses into heading compliance or personal taste. A draft can pass because it has the right headings while being hard for a practitioner to recognise, too thin against current practice, unclear about its primary `EntityOfConcern`, relation record, or claim record, or misleading about related patterns and the authority each pattern's content carries.

#### E.19:0.2 - What this buys

`E.19` gives authors, reviewers, and stewards a shared review profile: what must be checked, how deep the check should go, which defects block admission or refresh, and what evidence is needed before a pattern-quality claim is made. It also makes the recognition text visible before the more detailed assurance checks.

**First useful move.** Name the reviewed pattern edition or subset and the admission or refresh question. Select `PCP-BASE` plus only the risk profiles the question needs. Inspect the affected loci, then repair and verify each defect or return the actionable findings.

**Local-repair boundary.** If baseline triage shows that the review question has no ontology, usability, SoTA, boundary, naming, or authority risk beyond a small mechanical repair, close with that repair direction. Apply further profiles only for risks the question raises. Claim an `E.21` quality value only if `E.21` has evaluated the pattern version over its required coordinate set.

**Three situations for recognizing which questions to select**

| What the reviewer sees | Risk-selected move | First useful result |
| --- | --- | --- |
| A safety-critical subsystem-deployment pattern adds a condition in prose but not in its Solution or Conformance Checklist, introduces scope-hiding terms, and treats matching cross-team labels as identity. | Apply `PCP-BASE`, `PCP-NORM`, and `PCP-TERM`; add `PCP-BRIDGE` only if the text claims a relation across contexts. | Repair and recheck the requirement, terms, and identity claim, or return one actionable findings set. Solution and checklist constrain the same system claim; project deployment permission remains under its own governing rule. |
| An episteme or publication pattern still reads smoothly, but its sources are stale, its Relations use superseded names, or a carrier is treated as the claim it carries. | Apply `PCP-BASE` and `PCP-REFRESH`; add `PCP-TERM` for the claim, publication, or carrier confusion. | Update and verify the affected Solution, source use/currentness, publication/carrier distinctions, and Relations, or return complete findings. Handle historical-only evidence as lineage under E.8. |
| A Method pattern says that the Method or checklist performed dated work, leaving the acting system, Work, and result hidden. | Apply `PCP-BASE` and `PCP-TERM`; add `PCP-MOD` only if the text mixes guidance with an actual occurrence. | Restore plain Method guidance and state the acting system, Work, and result separately only when an actual occurrence is claimed. |

**Primary EntityOfConcern in plain terms.** One FPF pattern edition or bounded subset under an admission or refresh review question. The selected checks, reviewer, any repair, findings, optional aggregate result and evidence use, and any authority-bearing decision remain distinct when the review involves them.

**Primary working reader.** The first reader is an FPF reviewer, with the pattern author close behind. The review must be answerable to the eventual practitioner or manager who will rely on the admitted pattern.

