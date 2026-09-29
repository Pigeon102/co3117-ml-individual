# AI_USE — disclosure log (spec §12, §12.5)

Rules I follow:
- No AI for first-attempt drills, first derivations, or first Depth-A implementations.
- AI only after the pre-AI commit, in Socratic / verifier / quiz mode (spec §12.2).
- Every episode below lists what I independently verified and whether I can reproduce it closed-book.

| Week / date | Learning question | Pre-AI evidence | AI tool | Prompt purpose | Hint / question received (summary) | Verification source | What changed | Closed-book reproduction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W05 / 2026-09-29 | (Not a learning episode) Repository scaffolding from the assignment spec | n/a — infrastructure only | Claude Code (Claude Opus 5.5) | Generate repo skeleton: directory layout, Markdown templates, `src/data.py` (download/load/subject-aware split), `src/metrics.py`, majority/logistic baseline script, split-leakage test | Scaffolding only; **no** Depth-A algorithm, drill, weekly post, or reflection content was generated | Spec §5, §9; UCI HAR README; scikit-learn docs | Protocol draft to be reviewed and frozen by me at R0 | I must read and be able to explain `src/data.py` and `src/metrics.py` before R0 |
