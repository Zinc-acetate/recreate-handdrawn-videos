---
name: recreate-handdrawn-videos
description: Recreate or adapt reference-based hand-drawn music videos by breaking down shots, preserving beats and held frames, replacing characters and selectively redrawing, choosing vector, After Effects, or layered raster workflows, and checking contact motion and full-video replacement coverage. Use for reference-driven video production and revisions, not ordinary editing without a reference or standalone illustrations.
---

# Recreate Hand-Drawn Videos

Turn “looks like the reference” into shot and motion constraints that can be produced and reviewed. Do not treat any one work's characters, parameters, or project structure as a default template.

## Establish What to Preserve

Use the request and reference video to establish whether the task is a faithful recreation or an adaptation; which composition, beats, held frames, motion, text, and audio must remain; which characters or props to replace; and the delivery scope and format. Do not ask again for information already provided. Identify specific missing references or essential assets rather than presenting guesses as observed content.

Inspect the existing project and available tools first. Follow a production approach specified by the user; otherwise choose based on the visuals and motion. Do not turn a hand-drawn look into vector icons, a static slideshow, or uniformly smooth animation merely because those are easier to batch-generate.

## Workflow and Reference Routing

1. **Break down shots and locate risks.** Record shot intervals, beat and motion landmarks, original visibility intervals, and assets. Map source drawings to replacement drawings and exposure intervals. Separate camera, character, text, and particle changes; preserve reference holds and absolute timing. For timing recreation, fleeting edge visibility, or local replacement coverage, read [Timing and Coverage](references/timing-and-coverage.md).
2. **Prove the hardest shot first.** Choose a short section that exposes the main risk, such as character–prop contact, a side-lying pose, text deformation, tear trails, or occlusion. Produce a viewable sample to validate design, texture, contact, and beats before expanding to the full video. Local success does not mean the full video is complete.
3. **Choose a method based on the motion.** Determine whether the motion is whole-object movement, local deformation, or a pose/perspective change before choosing translation, a layered rig, small-state variants, or redrawn key poses. Read [Visual and Motion Workflows](references/visual-and-motion.md), using only the sections relevant to the shot.
4. **Produce in sections; validate the whole video.** For each change, check the local result, start and end boundaries, adjacent shots, and complete output. Record technical checks separately from human visual review; a passing script does not prove visual quality. Read [Quality and Delivery](references/quality-and-delivery.md).
5. **Deliver work that can be continued.** Deliver the final video and necessary project/asset notes as agreed with the user. Describe only actually verified or successfully delivered work as complete. Exporting, uploading, and publishing are distinct states and do not imply additional authorization.

For full-video production or work resumed across sessions, read [Production Workflow and Handoffs](references/production-workflow.md). For a reusable task brief, fill in [Production Prompt Template](references/production-prompt.md); the template grants no additional permissions.

## Judgments That Shortcuts Cannot Replace

- Visual style includes linework, negative space, paper/background color, brushwork, and motion quality, not merely character colors.
- Whole-image movement is valid when the reference uses rigid translation. When shoulders, hips, limbs, or occlusion relationships change, moving one image cannot stand in for a new action.
- Strict low-frame-rate recreation preserves distinct drawings and exposure boundaries. Meshes, morphs, and dissolves cannot stand in for a newly drawn source state. Record authorized deformation or added transitions as adaptation, including their timing differences.
- Increasing output frame rate does not increase meaningful poses. Do not default to frame interpolation, tweening, or a fixed frame rate.
- Repair scope depends on the original object's actual visibility throughout the shot, not only known problem frames or the current patch length.
- Numerical thresholds can locate anomalies but cannot replace aesthetic and semantic judgments about resemblance, natural motion, or complete text.

## Runnable Helper

`python scripts/check_coverage.py <manifest.json>` checks manually annotated frame intervals for gaps and undeclared overlaps, and whether replacement intervals cover visible frames plus specified guards. It requires only the Python standard library. See [Timing and Coverage](references/timing-and-coverage.md) for the input schema, exit codes, and limitations. It does not recognize visual content or prove that all visibility intervals have been annotated.

For the rationale behind particular methods, consult [Case Lessons](references/case-lessons.md) as needed. These are sources of reusable lessons, not templates for new projects.

For external method provenance and applicability limits, consult [Public Methods and Boundaries](references/public-methods.md).
