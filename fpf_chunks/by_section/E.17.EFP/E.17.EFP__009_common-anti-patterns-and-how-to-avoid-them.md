---
chunk_kind: "child"
pattern_id: "E.17.EFP"
pattern_title: "ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
section_id: "E.17.EFP:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.EFP/E.17.EFP__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.17.EFP — ExplanationFaithfulnessProfile — explanation-use discipline over existing MVPK faces"
  - "E.17.EFP:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 78881
line_end: 78893
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2.8"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.6.3.CSC"
  - "A.6.4"
  - "A.6.B"
  - "A.7"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.ID.CR"
  - "F.18"
  - "F.9"
  - "U.MultiViewDescribing"
keywords:
---

### E.17.EFP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it is wrong | How to avoid it |
|---|---|---|
| Treating every explanatory prose block as equally faithful | rendering, reconstruction, didactic work, and speculation have different review loads | publish the explanation-class set and bounded-use matrix |
| Letting reader-fit stay implicit when explanation is clearly tailored | a didactic or contrastive rendering can be overinterpreted as general or policy-bearing guidance | publish the interpretant-side block whenever user model, bounded use, or misuse boundaries are load-bearing |
| Using explanation faces as a second rule track | new semantic commitments hide behind reader-friendly prose | keep explanation faces tied to existing claim IDs, pins, and provenance |
| Calling connective reconstruction "bounded" without naming the added link | source-linked explanation quietly imports unsupported relation theory or bridge-comparison load | require `addedLinkPolicy` with source references, boundedness reason, and forbidden link class |
| Letting speculative prose enter technical or assurance use | speculative retelling starts to look canonical | restrict speculative retelling to clearly marked exploratory or didactic use on existing faces |
| Collapsing MVPK face and `publication face/form` or `interop publication form` discipline | explanation appears to create a new publication family | stay on existing MVPK faces and keep named `publication face/form` or `interop publication form` and carrier policy explicit |
| Derivative rendering as source replacement | a fork, adaptation, generated explanation, tutorial, or access-format conversion is treated as the original source because it is easier to read or access | keep it as a derivative rendering, publish source links for operative claims, and use `A.10` or `A.6.3.CSC` when reliance or narrowed-use discipline is present |
| Explanation as evidence or assurance | a fluent or source-linked explanation is cited as proof, approval, gate passage, release reliance, work authority, or assurance | classify the rendering, keep ordinary reader help inside E.17.EFP, and open `A.10`, `B.3`, `A.21`, `A.15`, or another source relation that carries, supports, or exposes the source basis for the operative claim only for the operative claim being relied on |

