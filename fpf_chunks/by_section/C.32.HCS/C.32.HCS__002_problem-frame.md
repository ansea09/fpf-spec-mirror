---
chunk_kind: "child"
pattern_id: "C.32.HCS"
pattern_title: "Architecture-Bearing Family Characteristic Starter Packs"
section_id: "C.32.HCS:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.HCS/C.32.HCS__002_problem-frame.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "C.32.HCS — Architecture-Bearing Family Characteristic Starter Packs"
  - "C.32.HCS:1 — Problem frame"
line_start: 64167
line_end: 64226
dependencies:
  - "A.19"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.PAD"
  - "E.10.ROLE"
  - "E.13"
  - "G.5"
keywords:
  - "architecture characteristic heads"
  - "architecture-bearing family characteristic starter pack"
  - "characteristic transfer"
  - "first criteria questions"
  - "source catalogue narrowing"
---

### C.32.HCS:1 - Problem frame

Use this pattern when a practitioner must choose a few architecture-characteristic starter heads for a described holon or for method, system-role-assignment, work, evidence, or cultural-evolution structures recovered from a source label, and the available catalogues are too broad to choose the first project criteria rows.

Primary working reader: an architect or architecture-responsible practitioner choosing a small first set of architecture-characteristic heads for an admitted holon family or another recovered architecture-bearing family, after naming the described holon or source-bearing episteme or publication context and any recovery patterns actually used.

Typical entry phrases:

```text
"The source catalogue has hundreds of quality names; which few heads should we inspect first?"
"The source calls this a review practice or method; what described holon, method-side structure, work family, and system-role side are actually under pressure?"
"A system-role assignment, organization, built asset, or evidence workflow has reliability-like pressure, but the bearer and scale are unclear."
```

**First-minute use slice.** A review lead sees a long quality catalogue and a software-oriented checklist, while the source wording calls the object a reusable review practice. Using C.32.HCS, the practitioner first resolves that label: the live holon is the review organization-as-system; exact review Work occurrences and any presentation carrier remain separate. The relevant structures include a method relation structure, method descriptions, local system-role kinds, separately obtaining assignments, work-product structures, and evidence records. Only then does the practitioner inspect repeatability, transferability, evidence reuse, and exception growth. A.2.7 tests kind substitutability. Assignment continuity, holder replacement, staffing, and Work coverage remain separate candidate characteristics; use the pattern that defines or tests each claim, or return `missing-governor`. Teachability is recorded as a likely C.25 Q-Bundle. The project carries only those starter heads and first project questions to `C.32.ACS` instead of copying hundreds of names or admitting "practice" as a holon kind.

The primary `EntityOfConcern` is one architecture-bearing family starter pack for beginning to turn broad architecture-characteristic names into project criteria rows. A starter head is only a possible characteristic head before project bearer, scale, use class, proxy risk, and protected counter-characteristics are bound. Carry admitted starter heads to ACS. Keep Q-Bundles, measurements, eval programs, candidate palettes, comparison rules, G.5 result declarations, actual publications, and architecture decisions as separate objects handled by their applicable patterns.

Ordinary working move: choose the starter pack for the admitted holon family or recovered architecture-bearing family, keep only the heads that plausibly fit the project, ask the first project question for each head, then hand those heads to `C.32.ACS` for bearer, scale, and use-class binding.

The first useful output is an `ArchitectureBearingFamilyCharacteristicStarterPack@FPF`. It is a working starter record under C.32.HCS: it suggests heads and first questions for one admitted holon family or one recovered architecture-bearing family. It does not introduce a new `U.*` kind and does not by itself create project criteria, scale rows, Q-Bundles, measurement methods, eval programs, or a universal holon ontology:

```text
ArchitectureBearingFamilyCharacteristicStarterPack@FPF:
  architectureBearingFamilyRef:
  describedHolonRef?:
  presentationCarrierRef?:
  starterPackUse:
  recoveryPatternRefs?:
  typicalSelectedStructureRefs:
  starterCharacteristicHeads:
    - architectureCharacteristicHead:
      usualBearerOrSelectedStructureRefs:
      likelyQBundleBoundary?:
      firstProjectQuestion:
      usualNextQuestionPatternRef:
  nonUniversalCaution:
  criteriaRowPatternRef: C.32.ACS
```

Use `describedHolonRef` when the starter heads concern an exact holon. Use `presentationCarrierRef` only when the carrier itself changes how the starter pack is presented or used; do not fill it as a substitute for the described holon.

What goes wrong if C.32.HCS is missed: the team faces hundreds of `-ility` or quality names, copies a catalogue, or starts from a software-module list even when a source label such as method, role, culture, practice, built asset, or evidence workflow still hides what actually bears the characteristic.

What C.32.HCS buys in practice: the practitioner has a short architecture-bearing starting point before `C.32.ACS` turns starter heads into project criteria rows, three to five optimization indicators, and monitored guardrails.

Adoption test: after using C.32.HCS, the project has a short starter set and first project questions; it has not copied a catalogue and has not yet claimed bearer, scale, use class, or optimization status.

Not this pattern when the project already has admitted architecture-characteristic rows with bearers, scales, and use classes. Also not this pattern when the current work is composite-quality modeling, measurement, eval design, candidate synthesis, comparison, selected-set result declaration, actual publication, local choice, or project architecture decision.

Common exits by claim kind:

- `C.32.ACS` for project criteria rows.
- `C.25` for Q-Bundles and composite quality families.
- `C.16` for measurement and `C.32.ACE` for eval programs or eval results.
- `E.13` when a source-looking cue, score, benchmark, or dashboard starts replacing the architecture concern.
- `C.32` for candidate synthesis after project criteria rows exist.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set result declaration, `C.11` for local choice, and `C.32.PAD` for a project decision. For publication, use `E.17` for a source-backed face and source return and `E.24.PUB` for the publication occurrence and audience availability.

