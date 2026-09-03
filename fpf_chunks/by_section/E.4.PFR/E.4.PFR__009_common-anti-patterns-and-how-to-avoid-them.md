---
chunk_kind: "child"
pattern_id: "E.4.PFR"
pattern_title: "Pattern-Framework Relation and Edition Discipline"
section_id: "E.4.PFR:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFR/E.4.PFR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "E.4.PFR — Pattern-Framework Relation and Edition Discipline"
  - "E.4.PFR:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 72242
line_end: 72257
dependencies:
  - "A.10"
  - "A.6.0"
  - "A.6.5"
  - "A.6.6"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.2.1"
  - "C.32.PAD"
  - "C.33"
  - "C.33-C.35"
  - "C.34"
  - "C.35"
  - "E.11"
  - "E.11.PUR"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFAD"
  - "E.5.3"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
  - "G.5"
keywords:
---

### E.4.PFR:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Related-pattern flattening | A relation list hides subject, function, predicate, and blocked reading. | Recover the exact subject assertion first; add a relation-specific row only for a named PFR receiver. |
| Mandatory row for every relation | Representation burden becomes an ontology and ordinary authoring becomes record-first. | Keep lane 1; open lane 2 only above its receiver threshold. |
| Pattern owner or governor | A pattern locator becomes a semantic owner, authority, or relation participant. | Cite the exact defining or constraining ClaimGraph and state the subject assertion. |
| Dependency as specialization | Edition reliance is read as child-pattern inheritance. | Use the exact dependency assertion; add a dependency-specific record only when a named dependency-impact or refresh receiver needs it, and state specialization separately if it also obtains. |
| Compatibility folded into dependency | A dependency sentence or record carries `compatibilityBoundary` and makes one relation stand for two claims. | State dependency and pairwise compatibility separately; add only an optional ref from the dependency record when a named maintenance consumer needs the link. |
| Compatibility by version label | An edition number is assumed to settle compatibility. | Inspect the exact pair, overlapping use, difference or interface, impact, and reopen condition; otherwise make no positive compatibility claim. |
| Generated graph as authority | A search or graph artifact decides relation meaning. | Use C.35 for candidate admission, then test the exact subject predicate. |
| Callable route as dependency | A skill, endpoint, or assistant integration is treated as framework dependency, method order, permission, or Work. | State only the exact bounded access relation; keep runtime/tool/work/currentness claims separate. |
| Source prose as basis truth | "supports" is read as formal-premise use, evidence, or sufficiency. | Separate bounded G.2 source use, actual-use predicate, evidence, and candidate evaluation. |
| Silent conflict winner | One sufficient base overwrites another in the same cell. | Preserve both and record pairwise conflict; return `established-conflict` and open bounded E.9. |
| Analysis as permission | A compatible or established family is treated as authorization or reliance. | Use the separate A.10/B.3 and authority/permission claims required by the attempted use. |

