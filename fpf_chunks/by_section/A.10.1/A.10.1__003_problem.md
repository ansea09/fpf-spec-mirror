---
chunk_kind: "child"
pattern_id: "A.10.1"
pattern_title: "Revalidate Affected Uses When a Relied-on Source Changes"
section_id: "A.10.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.10.1/A.10.1__003_problem.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.10.1 — Revalidate Affected Uses When a Relied-on Source Changes"
  - "A.10.1:2 — Problem"
line_start: 23038
line_end: 23051
dependencies:
  - "A.10"
  - "A.10.1"
  - "A.11"
  - "B.3"
  - "C.2.1"
  - "E.15"
  - "G.11"
  - "G.6"
keywords:
---

### A.10.1:2 - Problem

Source-change impact is difficult precisely when the receiving uses are partly unknown. A source register may know the source but not every later premise. A receiving decision may use an equivalent claim without retaining the same citation. A dependency graph may include declared edges that do no current work and omit an informal premise that does.

The cheapest apparent boundaries are therefore unreliable:

1. a file or edition label says too little about changed meaning;
2. a citation, mention, link, carrier, adjacency, or graph path says too little about actual reliance;
3. a repository search says too little about surfaces it could not inspect;
4. transitive reach says too much when no downstream action can change; and
5. a local revalidation summary says too little about the subject result that justified it.

Without a bounded search frame, “no affected use found” can silently mean “we searched one convenient repository.” Without application of direct subject guidance and an independently obtained subject result, “preserved” or “reopened” becomes an ungoverned universal status. The method must make both errors visible without turning every source change into a corpus-wide programme.

