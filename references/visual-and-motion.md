# Visual Consistency, Motion Workflows, and Precise Compositing

## Character Sheets Serve the Animation

Source frames constrain pose and visual style; character references constrain identity. Neither replaces the other. Use an accepted replacement drawing as a third reference for project consistency. Label all three roles explicitly; an old generated image must not replace source-pose evidence. Before production-shot drawing, complete the required target-PV-style baseline: front, side, and back views plus face and eye close-ups. Reuse an existing complete set only after visually verifying that it matches; do not regenerate it unnecessarily. Derive the style from actual representative source shots, not directly from detailed official portraits or 3D renders; use the same outfit and character version across all views. Unify silhouette, body and facial proportions, line weight/simplification, palette, garment structure, and anatomical laterality of asymmetric accessories. Close-ups explain identity details; do not impose their detail density on wide shots. Inspect the actual rendered images and record the adopted version and review status; a file or successful generation response does not prove it was viewed or accepted. Keep referencing the adopted sheet in subsequent shots, while source frames still govern pose, action, gaze/expression, crop, and occlusion. The sheet does not guarantee consistency: check every drawing. Identify characters by narrative identity, not left/right screen position. Record anatomical left/right separately from screen left/right. Hands, costume changes, and rear views must preserve the same identity.

When correcting a model sheet's skirt color, accessory placement, or similar feature, propagate the correction through all derived poses. Keep a few accurate identifying features for simple supporting characters; do not automatically upgrade them to detailed lead-character portraits. Treat materials, holes, and occlusion separately: transparent openings must not be painted black, and removing the outer background does not prove internal alpha is correct. Check transparent regions against different backgrounds while preserving legitimate hair or clothing crossing in front of them.

Match the shot's hair volume, clump size, line density, and shadow/highlight count and area. Neither embellish by default nor simplify into geometric icons. Derive color and shading budgets from the reference, not a universal fixed color count.

Validate new poses at final display size for line width, antialiasing, alpha edges, and recognizable details. Recompose high-resolution artwork at the target size rather than enlarging a low-resolution preview. Recheck thin lines lost during downsampling and semitransparent white fringes.

## Choose the Workflow; Do Not Let the Tool Choose the Look

- **Vector paths:** Suitable for simple silhouettes, flat colors, and continuously deformable paths. Preserve line width, sharp corners, local irregularities, and the reference's exaggerated proportions. For substantially different poses, replace paths/key poses rather than forcing point-to-point interpolation that creates knots. Not all hand-drawn brushwork can be replaced losslessly with vectors.
- **After Effects or other layered compositing:** Suitable for existing layered projects, fixed shot transforms, masks, and prop attachments. Make source phase, keyframes, parent/child relationships, anchors, and occlusion order explicit. Do not assume After Effects is installed or change environments without authorization. If unavailable, explain the limitation and choose an available equivalent compositing approach.
- **Layered raster rigs/meshes:** Suitable for local continuous motion that must preserve texture and linework. Allow internal overlap at shoulder/sleeve, forearm, hair/face, and clothing/body connections; do not cut precisely along outer contours and rotate pieces independently. Use front/back layers to conceal seams. Leave drawing margin below offscreen edges too, so vertical movement does not reveal a flat cut-off base.
- **Redrawn key poses and small-state variants:** Prefer redrawing for major joint or viewpoint changes, finger configurations, or complex contact. For only blinking, mouth, or hair-tip changes, edit locally from the same master and lock stable regions. If the base pose is wrong, return to the source keyframe and redraw rather than accumulating patches.

These approaches can be combined, but establish fidelity first: distinct source contours in low-frame-rate cel recreation require corresponding replacement drawings. Local mesh or flexible-hair deformation may be a suitable adaptation, not evidence that every cel was redrawn. Separate output frame rate from animation update rate. Do not add motion when strictly preserving reference holds; when continuous in-between motion is required, evaluate real deformation at output timestamps and inspect phases between keyframes. Before adding an intermediate state, validate both adjacent endpoint poses, then draw a structurally credible transition with correct contact and occlusion rather than duplicating an endpoint. Crossfaded double silhouettes, repeated frames, and random shaking are not meaningful in-between actions. Do not blindly apply optical-flow interpolation to captions, backgrounds, HUDs, and characters together.

## Motion Classes and Stable Regions

When the reference only translates/scales the whole character or moves the camera, rigid transformation is correct and avoids meaningless stretching of faces, sleeves, and skirt edges. When the reference bends an arm, twists the torso, or turns a wrist, internal relative motion is necessary. Tracking only the head center misses sleeve, hair, and torso deformation. Check position, rotation, squash, local relative displacement, and lag. Use measurements to locate issues, not to claim a “recreation percentage.”

Preserve abrupt acceleration, recoil, and accents; smoothing must not erase springy motion. Still poses should stay still, and small-state variants must not widen hems or make the body jump. Check stable-region differences, centroid, silhouette width, and fixed accessories with shot-specific tolerances. Keep fixed canvases and registration anchors; do not independently resize or center each drawing by its bounding box. Record inverse transforms for local crops. Use independent coordinates for characters and paper frames/stages so paper-edge jitter does not move the whole face.

Do not freeze internal poses early during a transition and merely carry the whole image away. Mouth shapes should follow actual source events, not automatically cycle open/closed with the music. A local mouth repair must not change the whole face. Representative-image indices are not motion onsets. A few master drawings may correspond to multiple unequal holds; do not assume an AB loop.

## Same-Pose Whole-Character Micro-Redraws

First identify the changing layer: camera/whole-object trajectory, real main action, same-pose linework variation, or an independent background or prop. If the character holds while the background changes, retain that character hold rather than adding motion to make it “more alive.” Real blinks and head turns need their own key drawings, not an invented idle loop.

When the source genuinely has whole-character redraw variation, derive a small set of near-identical complete drawings from one approved master (for example, two or three). Source evidence determines count, reuse order, and exposures; neither three drawings nor a fixed period is mandatory. Distribute small changes across hair strands, clothing folds, cuffs, and other parts. “Whole-character” means a coordinated complete drawing, not that every pixel must move. Stabilize eyes/face placement, head–neck–shoulder relationships, hand–prop contact, identifying clothing marks, and overall volume. Local identity-pattern locks are valid, but do not paste the entire garment back as a static master.

Reject or redraw variants that become a new pose or noticeably shift the head, shoulders, hair volume, or held container. Do not force them into place with large warps. Neither a mesh moving only one hair tip nor whole-body bobbing substitutes for this redraw effect. Show one coherent drawing at each exposure; crossfaded double lines are not micro-redraws.

For excessive amplitude, distinguish registration error from internal drawing differences: A/B drawings with identical scale and translation can still jump because their internal shapes differ. Reduce the deviating drawing's structural differences while retaining distributed subtle line changes. Do not weaken correct camera trajectories, independent background entrances/exits, or wipes to conceal character instability. Check a short original-speed A/B comparison before updating every reused exposure.

## Spatial-Difference Briefs and Repair Decisions

For an adjacent drawing, assemble a reference board with explicit roles: the accepted replacement drawing anchors persistent structure; source A/B establish real changes; RGB differences and two-color contour overlays locate them; necessary close-ups explain details without defining a new style. Inspect these actual images first. Describe changes separately for eyes/brows/mouth, hair roots/middles/tips, each shoulder/sleeve, and hems/folds: where, in which direction, and relative to which local scale. List stable anchors too. A single percentage is not a spatial instruction; coordinates must match the current canvas. Analysis marks stay out of the result, which remains one clean complete drawing without double images. Reuse existing difference checks and exposure ledgers; no particular external script is required.

Before repairing, distinguish:
- **Placement/uniform-scale error with correct internal structure:** Transform the separated character layer around real contact anchors, checking cleanup and masks. Do not scale backgrounds/captions together or regenerate identity merely to reposition it.
- **Incorrect proportions, shoulder/pelvis perspective, limbs, or contact structure:** Redraw using the source pose and adopted character sheet; nonuniform squeezing or large mesh warps do not repair anatomy. For seated/lying poses, establish torso axes, support surface, gravity, and occlusion first.
- **Implausible garment contours/bulges:** Separate body, sleeve, hair, and fabric silhouettes. Rebuild folds from the replacement garment's panels, length, material, and forces rather than importing bulges from a different source costume. Preserve real pose, contact, and coverage; repeatedly widening/narrowing the waist is not diagnosis.
- **Discontinuity between drawings:** Review the connected group and source differences, repairing hair, accessory, and fabric continuity. Register adjacent shots only when source framing and placement should remain continuous; do not erase genuine cuts or actions.

## Register Around Contact Points

Record frame boundaries, head/shoulders, elbows/wrists/palms, contact points, and occlusion order. Face alignment does not prove that hands, cups, flowers, or two-character relationships are correct. If one translation cannot align two contact points simultaneously, relayer or redraw instead of moving a source prop to accommodate an incorrect hand.

- A side-lying pose requires contact with the pillow, appropriate head/neck tilt, bedding occlusion, and the bed's motion. It is not a frontal face moved onto a bed.
- For an embrace, check hip height, torso tilt, leg overlap, and the two characters' depth order. For standing poses, check heel support and foot placement, not just the face.
- When retaining source prop geometry and the design is compatible, preserve accurate finger/contact geometry and connect the new cuff to the real wrist point. Otherwise redraw, while still locking the prop trajectory and contact relationship.
- Hanging props share suspension points, string curvature, blur, and fades. A prop must not remain sharply floating after its character fades out.
- Compare tear-trail origin, direction, differing lengths, contour, and light/dark contrast to the source, then fit them to the new eye corners. Check at actual viewing scale rather than merely enlarging existing tears.

## Occluded and Flexible Structures Stay Connected

Occlusion hides structure rather than deleting it. Preserve credible limb connections and motion margins behind the torso; check cuff, wrist, and palm continuity. Do not change source occlusion merely to reveal a hand, or let a hidden limb become disconnected in the next drawing.

Track major long-hair clumps through roots, middle sections, tips, and depth order; check length, width, and reappearance after occlusion. Follow the scene's wind and beats with appropriate middle-section follow-through, tip lag, and direction changes instead of copying a short-haired source's tip trajectory. Ribbons and hems respond to the same environment, though their amplitudes can differ. Check adjacent states, reversals, and last-to-first transitions, distinguishing intentional hand-drawn variation from unexplained volume drift.

## Diagnose Mask Errors by Causal Layer

Inspect source frame → artwork → individual masks/alpha → intermediate layers → final encode. Fix the smallest responsible layer. Color thresholds supply candidate selections, not semantics; also constrain local ROIs, connectivity, actual semantic regions, and stage boundaries. Flower colors may select skin, pale hands may select paper edges, and caption restoration may bring back an old cuff. Do not delete all black pixels when a black block appears or redraw the whole image to repair a local problem.

Remove both old character fills and outlines completely: deleting a red fill can leave black hair strands. Restrict animated layers to the real stage region. Smoke or closed curtains do not imply complete occlusion; check corners and curtain gaps, placing the new character beneath the effect first when necessary. When changing resolution, account for affine/perspective pixel-center relationships rather than merely multiplying translation values.


