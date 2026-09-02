---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Gamma_method - Order-Sensitive Method Composition and Work Enactment"
section_id: "B.1.5:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "B.1.5 — Gamma_method - Order-Sensitive Method Composition and Work Enactment"
  - "B.1.5:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 37816
line_end: 37831
dependencies:
  - "A.1"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.1"
  - "A.3.2"
  - "A.6.0"
  - "A.6.1"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.1"
  - "B.1.4"
  - "B.1.5"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.20"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.6"
  - "G.5"
  - "U.MethodDescription"
  - "U.PresentationCarrier"
  - "U.Signature"
  - "U.Structure"
  - "U.Work"
keywords:
  - "A.6.RCD claim disposition"
  - "assurance hooks"
  - "capability continuity"
  - "composite-Method boundary account"
  - "method composition"
  - "method relation structure"
  - "method/work granularity"
  - "methodPartOf"
  - "order-sensitive method"
  - "submethod"
  - "typed join"
  - "work enactment"
---

### B.1.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The workflow diagram is the composite Method." | First govern the diagram as `U.MethodDescription` or another representation; identify the exact candidate and part Methods under A.3.1, then test `methodPartOf`, whole-forming claims at their A.6.RCD dispositions, whole semantics, boundary, and reidentification. |
| "Step A is part of the Method because it is a box." | Recover whether the box denotes an exact `U.Method`, description node, plan item, Work occurrence, claim, or lens expression; test `methodPartOf` only for an independently identified Method. |
| "Parallel branches can join because the picture rejoins." | State the independence, downstream precondition, exact join, any adapter or correspondence, and failure route in ordinary language; use A.6.RCD's lightest sufficient disposition and open a relation kind only for an independently accepted occurrence-semantics need. |
| "The production plan lists five Methods, so the practice has five stages." | Preserve any real setup, handoff, or continuation order. Then test the representative Work: Methods may contribute together in one Work whole or in overlapping Work occurrences. The plan's row order establishes neither a total sequence nor a subject level. |
| "The selector table is the Method." | Use `G.5` for the selector. Use A.22 only when an actual selection basis and all four structure discriminators are present; otherwise keep a one-off comparison without asserting a selected `U.Structure`. A composite Method still needs its own exact construction and whole-level commitments. |
| "The run proved the method structure." | Record the run as `U.Work`; relate it to the method through `enactsMethod` and use evidence only through its governing relation. A successful run neither creates method parts nor settles reidentification. |
| "The phase is a method step." | Recover the subject: use the carrier's direct identity rule plus proper A.14 `PhaseOf` for one unchanged non-Work individual, C.2.1 for distinct MethodDescription epistemes and any obtaining edition relation, or A.15.1 for Work temporal parts and occurrences. None is a Method part unless an exact `U.Method` and `methodPartOf` independently obtain; use B.2 only for a separately current whole-reidentification, supervision, or closure claim. |
| "The join improves throughput, so the method has emergence." | Name the measured characteristic, critical path, cutsets, typed joins, and assurance relation; open B.2 only when a separate whole-level reidentification claim remains. |
| "The boundary-account prompts define the Method." | Identify the exact claim-bearing `U.MethodDescription` edition first. A boundary-account form is a reusable form only when `PublicationFormExpressionRelation` obtains; its prompts create neither the Method nor the form, carrier, declaration epistemes, publication Work, five-participant publication occurrence, or composition facts. |
| "The boundary account is a nice diagram." | For a load-bearing publication, identify the MethodDescription edition, bounded-use- and audience-declaration epistemes, boundary-account form, and carrier independently; then distinguish the system's publication Work from the five-participant occurrence that makes the edition available. Keep designation content separate. Otherwise state the few boundary decisions directly. |
| "The same Work and referent make the transformations one composite." | Identify each transformation under A.3.4. Without a direct transformation-composition governor, return `missing-governor[transformation-composition]` for the proposed whole and independently identified changes; infer neither composition nor atomism. |

