# Timing, Held Frames, and Replacement Coverage

## Shot Breakdown Is Not Uniform Screenshot Sampling

First establish the source video's time base, duration, frame dimensions, and audio. Anchor the breakdown to cuts, pose changes, caption changes, prop entrances/exits, and beats. Uniform sampling is useful only for initial screening and can miss fleeting visibility at frame edges. Record shot start/end, motion landmarks, characters/props, foreground and background occlusion, text, pauses to preserve, and transitions.

Read the reference's held-frame structure: long pauses, a few replacement poses, and abrupt changes may define its style. Record output container frame rate separately from the effective drawing update rate. When aligning to a reference, sample reference frames or animation states using the final output's absolute time; restarting each section at zero can shift the beats. Handle variable-frame-rate footage by timestamps. Establish an explicit project-time-base mapping before using frame-number manifests.

To preserve holds from a verified constant-frame-rate source exactly, compute source phase from global output index `k` and rational frame rates as `k * source_fps / output_fps`, then select frames by source-state boundaries. Do not convert to an intermediate frame rate and then duplicate frames. For VFR, anomalous PTS, or a nonzero start time, use actual presentation timestamps instead of this simplified formula. Backgrounds may hold according to source presentation timing while characters requiring continuous animation are evaluated separately by phase. Check the actual last frame even for short components; approximate container duration must not cause premature truncation.

## Distinct Drawings and Exposure Ledgers

Within a shot, separate camera, character, text, and particle changes before deciding whether the character drawing changes. Inspect candidate frames side by side, with RGB absolute differences and two-color contour overlays to locate subtle sleeve, eyelid, or hair changes. Do not warp frames into alignment and then use the result to merge drawings. Calibrate compression noise on known holds and retain candidate and manual-merge records; global similarity can hide meaningful local changes.

Record each source drawing, replacement drawing, absolute frame/PTS interval, adopted asset, and reuse relationship. A drawing may recur across several intervals; file creation order is not timeline order. Strict recreation retains drawing distinctions and every exposure boundary. For adaptation, keep a separate output ledger marking new transitions and time allocation: equal duration does not prove unchanged beats. Held character drawings must not freeze moving text or particles.

Map micro-redraws through the source exposure table too, recording character drawings separately from independent background/prop phases; the number of combined assets is not the number of character drawings. When replacing a drawing, find every reused exposure, including its final appearance within a transition. Treat a user's approximate timestamp as a visual locator: identify the complete problematic shot and neighboring transitions rather than examining only that exact instant.

An exposure ledger may explicitly label `strict_source` or `adapted_motion`. Keep source and adopted-output tables separately. Check for gaps, undeclared overlaps, out-of-range intervals, matching overall scope, and real asset references. In strict mode, compare exposure boundaries and stable drawing correspondence without merging distinct source drawings. In adapted mode, record added transitions, redistributed durations, and shifted boundaries, then review beats. Equal duration does not prove equal switch times; existing files do not prove distinct drawing content. These are review criteria: the existing `check_coverage.py` only supplies its documented interval-coverage checks, not exposure-semantic validation.

## Whole-Shot Visibility Comes Before Patch Scope

1. Inspect each object's complete relevant shot and mark every visibility interval, including frame edges, occlusion gaps, motion blur, reflections, and later reappearances. Do not inspect only from the main action's onset onward.
2. Add guards before the first and after the last visible frame appropriate to the motion, occlusion, and sampling uncertainty. Guards are not a fixed frame count. They provide review/processing margin, not a requirement to make a replacement abruptly appear when it should be invisible.
3. Check the replacement's entrance, exit, position, contact points, and occlusion. Extending a patch must not place foreground elements at the wrong depth or damage unrelated pixels.
4. Check before, inside, and after the patch, then review the complete export. If earlier or later remnants appear, update the visibility inventory and revalidate the entire section rather than patching only the newly discovered frame.

## Interval Checker

All intervals use integer frame numbers in the project time base and are half-open: `[start, end)`. `duration_frames` is the total frame count. `shots` must cover the whole video; ordinary cuts share a boundary without overlapping. Declare intentional dissolves explicitly in `allowed_overlaps`. A replacement's `covered` intervals describe the scope included in cleanup, replacement, and review, not frames in which the replacement must be visible. `visible` must come from whole-shot inspection; the script does not observe the original object automatically.

Example (numbers illustrate the format, not recommended parameters):

```json
{
  "duration_frames": 120,
  "shots": [[0, 50], [48, 120]],
  "allowed_overlaps": [[48, 50]],
  "replacements": [
    {
      "id": "prop-a",
      "visible": [[3, 8], [25, 46]],
      "covered": [[1, 10], [23, 48]],
      "guard_before": 2,
      "guard_after": 2
    }
  ]
}
```

Run: `python scripts/check_coverage.py manifest.json`. Exit codes: 0 means the declared intervals pass; 1 indicates gaps or undeclared overlaps; 2 indicates malformed input or a read error. Guards are clipped to video boundaries, but not automatically to shot boundaries, so that adjacent-shot handoffs needing review remain detectable. If an adjacent shot must not be processed, adjust actual boundaries or use separate manifests with explicit scopes rather than blindly extending a visible object.

The script proves only containment relationships among supplied intervals. Missing visibility annotations, incorrect occlusion, stray hair, wrong designs, ineffective animation, or audiovisual desynchronization can remain even when it passes. For multitrack composites, supply final shot intervals, not character or caption layer intervals; their normal concurrency would otherwise be reported as overlap.


