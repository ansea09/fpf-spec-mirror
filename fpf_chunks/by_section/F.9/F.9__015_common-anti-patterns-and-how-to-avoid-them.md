---
chunk_kind: "child"
pattern_id: "F.9"
pattern_title: "Alignment and Bridge across Contexts"
section_id: "F.9:13"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.9/F.9__015_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "F.9 — Alignment and Bridge across Contexts"
  - "F.9:13 — Common Anti-Patterns and How to Avoid Them"
line_start: 92582
line_end: 92601
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

### F.9:13 - Common Anti-Patterns and How to Avoid Them

| ID | Anti-pattern | Symptom | Repair |
| --- | --- | --- | --- |
| AP-1 | String-equals becomes sense-equals | Same spelling is used as proof of identity. | Resolve the exact cells and test the least-committing relation profile. |
| AP-2 | Profile as use licence | Direction, use rule, or tolerated loss is placed inside profile identity. | Keep only relation semantics in the profile; state `<u,d,r,t>` in a separate C.2.1 claim. |
| AP-3 | Bridge-alone substitution | “A corresponds to B, therefore use A as B.” | Require both the obtaining Bridge and an affirmative bounded-use claim, then check A.10 or B.3 reliance. |
| AP-4 | Symmetry grants two directions | An `Equivalence` Bridge is treated as two approved substitutions. | State and test each proposed use direction separately. |
| AP-5 | Inclusion grants the reverse use | A broader sense is silently substituted for a narrower one. | Refine the endpoint senses and test the reverse relation and bounded use independently. |
| AP-6 | Assessment score grants use | `CL=3` is cited instead of the exact rule, tolerance, and reliance path. | Treat the score as optional evidence shorthand; write and warrant the bounded-use claim. |
| AP-7 | Loss note becomes tolerance | An observed difference is treated as automatically acceptable. | Put observed loss in evidence and the accepted maximum in the claim's `t`. |
| AP-8 | Card creates relation or permission | An approved or published card is cited as obtaining or authorization. | Test the Bridge independently and recover authorization under its direct governor. |
| AP-9 | Named role becomes actual use | The claim says “publication use” or “comparison use”, so a publication or comparison is presumed. | Recover a publication occurrence under E.24.PUB; recover any comparison or other receiving object under A.15.1, C.2.1, A.6.1, or its direct domain-relation pattern. |
| AP-10 | Evidence failure erases the Bridge | A stale evidence path is said to make the semantic relation disappear. | Reopen reliance or the use claim; change the obtaining claim only when endpoint facts or the profile predicate changed. |
| AP-11 | Bridge as durable U-kind | A local correspondence is used to globalize meaning. | Keep kinds context-local unless the exact admission patterns independently admit a U-kind. |
| AP-12 | Silent relation composition | A-to-B and B-to-C are used as an A-to-C occurrence. | Test and individuate the direct A-to-C Bridge separately. |
| AP-13 | Description identity becomes occurrence identity | A description/Card C.2.1 triple or registry id is used to identify the world-side Bridge. | Apply `BridgeOccurrenceIdentityRule` to exact endpoints and profile; identify the description separately. |
| AP-14 | Same-locality Bridge | Two designations under one exact projection are forced into F.9. | Use ordinary designation and A.2.6 scope operations; no F.9 occurrence is current. |
| AP-15 | Bridge creates another subject fact | Semantic correspondence is said to assign a role, perform Work, authorize evidence, transfer status, admit a U-kind, publish an episteme, or relate model-use structures. | Open the exact direct governor for that subject relation or state the missing-governor stop. |

