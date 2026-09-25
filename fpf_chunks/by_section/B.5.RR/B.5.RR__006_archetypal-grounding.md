---
chunk_kind: "child"
pattern_id: "B.5.RR"
pattern_title: "Revise Reasoning After a Premise or Question Changes"
section_id: "B.5.RR:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RR/B.5.RR__006_archetypal-grounding.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "B.5.RR — Revise Reasoning After a Premise or Question Changes"
  - "B.5.RR:5 — Archetypal Grounding"
line_start: 44856
line_end: 44889
dependencies:
  - "B.5"
  - "B.5.MPC.R"
  - "B.5.RA"
  - "B.5.RC"
  - "C.11.DUA"
keywords:
---

### B.5.RR:5 - Archetypal Grounding

#### B.5.RR:5.1 - Changing the range of a sum

A reader has established S(n)=n² for the sum of the first n positive odd integers, with S(0)=0 and n a nonnegative integer. The argument uses the shared initial value and increment: S(n+1)−S(n)=2n+1, also the increment from n² to (n+1)².

The new question asks for n terms beginning at 3: 3+5+...+(2n+1). The change is the range of summation. Reuse the established result on the first n+1 terms and remove the initial 1:

T(n)=S(n+1)−1=(n+1)²−1=n²+2n.

For n=4, the new sum is 3+5+7+9=24. The old formula applied unchanged would return 16. The proof of S survives; the application of that proof changes.

This repair also exposes a reusable construction. For n terms starting at a and increasing by 2, term j, counted from j=0, is (2j+1)+(a−1). Summing the established odd-number terms and the n equal additions gives n²+n(a−1). Changing the increment would require another derivation. The worked extension makes the next question precise without assuming that the same correction covers every progression.

For the next use, retain four terms and the increment 2, but require their sum to be 28. The former starting value a=3 becomes the unknown: 16+4(a−1)=28 gives a=4. Checking 4+6+8+10=28 confirms the required sum. If there are zero terms and the required sum is positive, no starting value can supply it: the empty sum is zero for every a. The changed question then requires a different term count or total.

#### B.5.RR:5.2 - Losing one way to recover a report

A team needs to read revision 17 of a report. Its established account has two ways to obtain that revision's bytes: decrypt the local backup using its available key and decryptor, or obtain an unencrypted remote copy. An available viewer then displays the report.

The key becomes unavailable. Following that change removes the local decryption route. The remote copy and viewer still supply the requested reading, so the team can proceed through them. The missing key need not be recovered for this use.

Now consider a different finding: the supposed remote alternative is encrypted with the same key. Both routes need that key, so neither supplied route obtains the bytes. The next contribution is the key, another usable copy or a different way to obtain the report. A second storage location had concealed a shared prerequisite.

If instead the viewer becomes unavailable, either route may still provide the bytes. Reading now needs a suitable viewer or format conversion. This repair preserves the obtained result and locates the different operation that the receiving use requires.

#### B.5.RR:5.3 - A repeated conclusion loses its starting support

An analysis establishes claim A from an observation O, derives B from A and uses B in a further argument for A. A corrected interpretation of O removes its support for A.

The second occurrence of A does not preserve that support: its offered reason B was itself obtained from A. Reopen both uses and look for an argument grounded in retained premises. The conclusion may be true, but this circular route no longer establishes it.

Contrast this with an induction argument whose base case remains established and whose step derives the next case from the preceding one. Its recurrence has a grounded way to obtain each finite case. The relevant inference, rather than the visual presence of a cycle or repeated letter, decides what can be retained.

