---
chunk_kind: "child"
pattern_id: "C.25"
pattern_title: "Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
section_id: "C.25:17"
section_title: "Repair and Boundary Notes"
source_path: "FPF-Spec.md"
output_path: "by_section/C.25/C.25__018_repair-and-boundary-notes.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "C.25 — Q-Bundle: Authoring \"-ilities\" as Structured Quality Bundles"
  - "C.25:17 — Repair and Boundary Notes"
line_start: 52553
line_end: 52591
dependencies:
  - "A.10"
  - "A.15"
  - "A.16.0"
  - "A.18"
  - "A.2.6"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.16.P"
  - "C.16.Q"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.2.2a"
  - "C.26.3"
  - "C.33"
  - "C.34"
  - "C.35"
  - "F.9"
  - "F.9.1"
keywords:
  - "admissible quality-family use"
  - "characteristic plus scope"
  - "endpoint classification"
  - "failure mode"
  - "ility"
  - "mechanism/status slots"
  - "proxy metric"
  - "quality bundle"
  - "quality family"
  - "viability envelope"
---

### C.25:17 - Repair and Boundary Notes

#### C.25:17.1 - Repair from bare quality requirement prose

Bare phrases such as *quality requirement*, *security requirement*, or *availability requirement* should not survive as bare heads when the underlying endpoint is actually a characteristic or bundle. The repair rule is:

- choose the endpoint shape first,
- then bind the requirement or commitment to that explicit head.

`C.16.Q` may still be the entry repair for overloaded quality wording, and `C.16.P` may repair characteristic, scale, score, metric, or proxy wording inside the same statement; `C.25` is the resting place only after the engineering quality family has been made explicit.

#### C.25:17.2 - Boundary to cross-context use and reliance

Cross-context comparison does not change whether the endpoint is one characteristic or one bundle and does not modify any bundle slot. Align the exact bundle heads or slots, resolve their exact `F.17` local senses, and test the direct `F.9` predicate. If a Bridge obtains, state the proposed direction, correspondence rule, tolerated loss, and polarity in a separate bounded-use claim. Observed loss remains evidence; permitted loss remains that claim's tolerance. Use `A.10` for ordinary bounded reliance and open `B.3` only when an actual named assurance claim is current.

#### C.25:17.3 - Boundary to publication convenience

A report, summary publication, or executive summary may express only one slice of the selected quality-claim episteme. Keep the selected episteme and any exact `ClaimAddress` distinct from its publication occurrence, form, and carrier under `E.24.PUB`. A coarser form does not collapse the source claim content, while changed Q-Bundle claim content identifies another episteme even when the file or layout stays the same.

#### C.25:17.4 - Serviceability and supportability

Serviceability, supportability, and adjacent family labels often look simple in prose but become composite as soon as operational use is declared. An admissible bundle for this family may need:

- support-scope slices,
- measured restoration or service intervals,
- mechanism slots for support mechanisms, access discipline, or replacement procedures,
- and evidence from service traces or support records.

The lesson is the same as elsewhere in `C.25`: once the truth of the family claim depends on several typed contributors, the bundle should stay explicit.

#### C.25:17.5 - Boundary to description-side and selector-side evaluation

`C.25` is for engineering quality families whose bearer is a system-side, promise-side, or explicit quality-bearing artifact. It does **not** automatically cover:

- viewpoint-fit or grounded architecture adequacy claims, which may belong in viewpoint or evaluative-ascription patterns,
- or selector/objective heads where *quality* means use-value under a search or portfolio frame.

This boundary matters because the same word *quality* appears across those zones. `C.16.Q` repairs overloaded quality wording, `C.16.P` repairs characteristic, scale, score, metric, or proxy wording when that is the hidden object, and the resting endpoint depends on what is actually being evaluated.

