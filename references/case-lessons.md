# Generalized Production Lessons

Use these cases to understand why a method exists, not to copy project parameters. The examples are grouped by production problem and omit project titles and conversation provenance. They summarize prior production and review experience, not a claim that every earlier project has been restored or revalidated. Transfer only techniques that match the new shot's conditions.

## Case Group A: Pose, Identity, and Fine Detail

- **Faces, sleeves, and skirt edges stretched during a translation shot.** Local deformation was applied even though the original action was whole-object movement. Use rigid transforms. Do not turn “translation cannot substitute for joint motion” into “all translation is wrong.”
- **Side-lying poses failed to meet pillows; embrace leg positions or foot placements were wrong.** Ordinary standing/frontal poses were reused without rebuilding contact. Redraw from source key poses, checking head/neck tilt, pillow/bedding occlusion, hip height, leg overlap, and heel support. Stop accumulating patches when the base pose is wrong.
- **Restored text still lacked strokes, and emotional details were weak.** Color selection and representative-frame review missed antialiasing and late appearances. Tear trails were not compared with the source at actual viewing scale. Protect the entire text line throughout its full interval; check tear origins, directions, and contrast rather than merely enlarging them.
- **Incorrect model-sheet colors propagated, and transparent structures became black.** Identity colors, materials, and alpha were conflated. After correcting the model sheet, update all derived poses. Test internal openings against different backgrounds while preserving legitimate foreground occlusion.

## Case Group B: Held Timing, Registration, and Occlusion

- **Actions happened late or held-frame beats changed.** Representative-image numbers were mistaken for real onsets, and master-image counts for state-interval counts. Build half-open intervals from source change points and sample by global time instead of converting to an intermediate frame rate and duplicating.
- **Small-state variants made bodies drift; paper-frame jitter moved faces.** Stable regions were independently redrawn or coordinate systems mixed. Derive variants through local edits to one master, lock stable regions, and register characters separately from the stage.
- **Faces aligned, but hands missed balls, flowers, or cups.** Registration anchors ignored real contact. Lock prop trajectories and contact geometry; revise wrists/cuffs or redraw if necessary instead of moving props to accommodate incorrect hands.
- **Old skin or paper edges became black blocks, and old characters remained in curtain gaps.** Color masks crossed semantic boundaries, and transitions were incorrectly assumed to provide full occlusion. Add ROI, connectivity, stage-boundary, and layer-order constraints; inspect intermediate masks and check smoke corners/curtain gaps frame by frame.

## Case Group C: Internal Motion, Coverage, and Reproducibility

- **Overall trajectories were close, but motion still looked like a paper cutout.** Head displacement concealed insufficient internal limb deformation, and excess smoothing weakened accents. Inspect local relative motion, recoil, intermediate phases, and poses during transitions separately. High frame rate or center-point trajectories cannot stand in for completed action.
- **A local prop patch passed, but whole-video review found an earlier edge appearance.** The initial visibility interval began at the most obvious main action and omitted a fleeting entrance. Rescan the complete shot's first/last visibility, extend coverage earlier, and add guards. Check low-alpha remnants and black fringes after encoding. A local PASS must not replace whole-video review.
- **Nominal frame rate/duration caused last-frame or alignment problems.** Source PTS anomalies, actual component frame counts, and approximate container durations did not fully agree. Decode sequentially to establish mappings, distinguish background holds from continuous character phase, and align comparison images precisely.
- **Local repairs threatened the reproducibility of approved sections.** Shared scripts and dependencies kept changing, so the current directory no longer matched the versions actually used for earlier components. Freeze approved components and exact dependencies, record patch impact, and verify restoration entry points in an independent directory. Successful extraction does not mean complete reproduction is possible.

## Same-Pose Micro-Redraw Revision Lessons

- **A hair tip moves, but the character still feels like a pasted cutout.** The reference uses coordinated complete-character redraws rather than one local deformation. Derive near-identical drawings from one master, distributing line changes while stabilizing face, contact, and volume. This does not mean every held shot needs redraw variation.
- **Identically registered A/B drawings still jump too much.** Internal head/shoulder, hair-volume, and sleeve differences—not whole-object placement—cause the jump. Reduce the deviating drawing's structural differences and review at original speed. Preserve genuine background motion and entrance/exit transitions rather than reducing everything together.
- **Background changes are mistaken for character changes.** Separate background/prop and character exposures. Do not invent character micro-states from the count of combined assets; preserve real key drawings for main action, blinks, and head turns.
- **An approved local test changes character when expanded or rendered at higher resolution.** Integrate through all reused exposures and check adjacent drawings, loop boundaries, and transitions. Compose high-resolution masters directly on the final canvas; higher resolution is not permission to increase approved motion amplitude.

