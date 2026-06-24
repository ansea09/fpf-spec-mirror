# Required Pattern Contract

This repository validates a small required-pattern contract before publishing
generated FPF chunks. The contract protects downstream skills that rely on
specific FPF entrypoints.

## C.7 Migration

`C.7` (`CHR-CAL - Characterisation Kit`) was previously treated as a required
ToC-or-body entry. Upstream FPF no longer publishes `C.7` as a standalone body
pattern or ToC row.

The mirror therefore treats `C.7` as deprecated/removed and validates the
current replacement basis instead:

- `A.17` - canonical characteristic vocabulary
- `A.18` - characteristic, scale, level, coordinate kernel
- `A.19` - characteristic space and dynamics hook
- `C.16` - measurement and metrics characterization
- `G.3` - CHR authoring kit and publication surface
- `G.4` - CAL authoring kit and publication surface

The validator must not fail only because `C.7` is absent. It should fail if any
replacement-basis pattern above is missing from generated body chunks.
