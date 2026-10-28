# Quality Review, Compositing, and Reproducible Delivery

## Establish Different Kinds of Quality Separately

Play complete motion cycles and transitions at original speed, including adjacent drawings, reversals, and last-to-first boundaries. Slow motion and stills are supplementary diagnostics, not substitutes for playback.

- **Semantics and design:** Compare corresponding reference timestamps side by side for identifying character features, expressions, poses, object identity, text content, and complete strokes. Use thumbnails for full-video consistency and native-size/local enlarged views for hair, cuffs, contact points, low-alpha remnants, and two- or three-pixel edge leaks. Neither view replaces the other.
- **Motion:** Play key actions and transitions, comparing local relative movement, entrances/exits, accents, recoil, and holds. Check that intermediate phases have a genuine single silhouette. Output frame rate or overall trajectory is not sufficient evidence of motion quality. State accurately when frames were sampled but playback was not reviewed.
- **Technical:** Decode the complete final encode and verify actual frame count, PTS, frame dimensions, color interpretation, audio mapping, and the ending. Both sides of comparison images must show the same corresponding moment; automatic synchronization by a concatenation tool can pair the wrong frames. When container duration/nominal frame rate disagrees with decoding, investigate actual timestamps and a verified mapping rather than guessing from integer frame-count multiples.
- **Regression:** Check that the problem is fixed inside the modified region, that no changes were introduced outside it, then check guards and the complete output. Before encoding, lossless composites can be compared outside the mask. Explain lossy-encoding differences separately from content changes. PSNR, pixel differences, and motion residuals do not measure semantic fidelity.

Review micro-redraws both as individual drawings and as switches: forward A→B, reverse B→A, last-to-first, and original-speed comparisons including adjacent transitions. Watch for jumps in eyes/face, head/shoulders, contact points, and volume. Smaller numerical differences or a successful decode help diagnosis but do not replace aesthetic review at actual viewing size.

Create a full-video appearance inventory for captions, props, clothing, and identifying features needing consistent correction. Check every appearance and its complete interval rather than repairing only the most conspicuous shot.

Bind approval to a specific version and review evidence. Do not conflate draft, locally approved, full-video approved, and delivered states. Batch completion still requires whole-video review. A local PASS does not prove other sections or earlier edge appearances were addressed.

## When Applicable: Preserve the Reference Plate and Replace Locally

When background, text, layout, and music must remain unchanged, prefer the original video as the base plate. A purported clean-background version or third-party recreation may already have changed fonts/colors; use it as a local donor only after checking. Before cleanup, list fingers, lines, rods, frames, captions, and speech bubbles to protect. Do not restore foreground elements using only white/gray/black thresholds; that can restore old characters, objects, watermarks, or white blocks.

Preserve the full shapes and correct alpha of semitransparent text/bubbles. Hard thresholds must not truncate fading strokes. Crop moving picture frames/black borders using stable geometric boundaries, not whether compressed pixels are pure black. For screen replacement, mask the real screen outline and rounded corners. Distinguish scan light, borders, foreground occlusion, and exit blur rather than treating everything as a rectangular overlay.

If source material is too short, first locate whether the missing section affects visible action. Consider a very brief hold only in an explicitly acceptable, verified occluded or strongly blurred tail. Do not automatically freeze, loop, or retime clear action to fill the duration. Record such a compromise as a local choice.

## When Applicable: Consistent Encoding and Audio Preservation

- Proxy previews support iteration, but final production needs assets/rendering capable of the real target dimensions. Enlarging a low-resolution preview is not native high quality. Recompose directly from high-resolution masters onto the final canvas rather than upscaling a low-resolution cache and calling it native output. Preserve approved motion amplitude, phase, and registration when changing resolution, then recheck linework and contact points.
- Verify pixel format, matrix, primaries, transfer, and range against source and delivery requirements. Adding output tags cannot correct misinterpreted input; check raw YUV input parameters especially. Do not apply one video's SDR color strategy to HDR or unrelated sources.
- Do not concatenate compressed streams unless component encoding parameters, time bases, and stream configurations are verified compatible. Decode to a common representation and encode the complete video if needed. If using stream copy, verify compatibility and decode the entire result for review.
- When original music must remain unchanged, prefer a single mux/composite using the original continuous audio track. Do not concatenate short preview tracks that may have been zero-padded, faded, or re-encoded. For strict preservation, compare packet payloads/PTS/durations or decoded PCM. Similar sound is not proof of byte identity.
- If the task permits music or edit changes, use sample-accurate joins, listening, and synchronization review instead of demanding original-track byte identity. Frame/sample quantization can create tiny end differences; explain them using time bases before stretching audio merely to match container numbers.
- If native-resolution rendering resources are limited, use streaming decode, bounded caches, small keyframe batches, and controlled concurrency. Choose parameters for the current machine rather than hard-coding a concurrency count.

## Freeze Results and Deliver

For approved components, record input/asset checksums, the exact scripts and dependency versions used, anchors, masks, trajectories, frame mappings, output checksums, and review scope. If shared scripts change later, do not claim their current versions can reproduce old components pixel for pixel. Small repairs may reuse an approved encoded plate for local patches, but check re-encoding losses. Do not rerender the whole video with changed global scripts without a reason.

Save final masters, viewing copies, layered assets/projects, source mappings, and runnable entry points according to user needs. Version outputs and distinguish earlier deliveries from later full-video versions; a filename containing “final” does not establish status. For a reproducible project delivery, check dependency paths and asset loading in an independent directory, rerun representative difficult frames, and verify encoded components decode. An archive that opens with correct CRCs does not prove the whole project can be rebuilt. State what has not been rerun.

A download link is a delivery copy, not long-term archival storage. Verify results and authorization separately for generation, attachment sending, uploading, and public publishing. A failed upload does not automatically authorize another service. A production summary must not reopen completed projects or imply authorization to clean up historical working files.

