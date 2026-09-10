---
chunk_kind: "child"
pattern_id: "E.11.PFP"
pattern_title: "Framework Publication Form Profile"
section_id: "E.11.PFP:section-007"
section_title: "<FrameworkCode>.Preface:<n>.<m> - <Title>"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PFP/E.11.PFP__008_frameworkcode-preface-n-m-title.md"
commit_sha: "a87d0ef4f3712507edd6e5a59f4de5bf7a55905a"
heading_path:
  - "E.11.PFP — Framework Publication Form Profile"
  - "E.11.PFP:section-007 — <FrameworkCode>.Preface:<n>.<m> - <Title>"
line_start: 80658
line_end: 80670
dependencies:
  - "A.3.2"
  - "C.29"
  - "E.11"
  - "E.17"
  - "E.2.DA"
  - "E.21"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.FPF"
  - "E.4.PFR"
  - "E.8"
  - "G.11"
keywords:
  - "& Search Queries"
  - "Dependencies"
---

### <FrameworkCode>.Preface:<n>.<m> - <Title>
```

For example, `## STR.Preface:1 - Problem frame - Direction and commitment under changing conditions` identifies the first section of the Strategy Preface. `### ME.Preface:7.3 - Production MethodDescription` identifies a nested section in the Method Engineering Preface. Use the framework's declared public code; name the framework as well when quoting outside a context that identifies it. The enclosing Preface H1 retains its product-declared title and established ToC entry.

Number sibling sections in reading order, starting at 1, and carry the complete parent path into nested headings. Each nesting level adds one heading level and one ordinal. These ordinals locate sections in this Preface; their titles state the content functions. An account can combine several E.8 functions in one section or explain one function across several sections. Keep that useful arrangement instead of adding twelve empty sections to match numbers. The rule introduces no limit on useful conceptual scales; physical Markdown heading depth remains a carrier constraint.

`STR.Preface` names a publication unit. Its section addresses are `SectionRef` uses under E.8, not declarations of additional patterns: the pattern index continues to contain the individually declared pattern bodies. Apply the same self-identifying construction to a profile account or other support unit when it needs its own section addresses, using its product-declared unit key. A profile explained inside the Preface retains its Preface section path; that text position does not decide the profile's semantic relations.

The prefix lets a reader distinguish a whole-language Problem frame from the Problem frame of one pattern before choosing what to read or cite. Visible names and numbers also survive copying and printing, where a hidden anchor cannot help.

The visible address and title use the ASCII ` - ` separator. Build each clickable fragment from the complete rendered heading according to the target Markdown carrier's rules, including punctuation removal and duplicate handling. When a heading changes, update its direct links in the publication, source templates and public consumers together. Check that the link resolves to the intended heading, then read that target for the answer the link promises. Keep the visible address usable for search and non-clickable copies. HTML anchors are optional carrier facilities, not a substitute for a self-identifying visible heading.

