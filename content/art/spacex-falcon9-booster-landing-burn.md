+++
title = "SpaceX Falcon 9 landing burn"

date = "2019-12-22"

categories = ["3d", "art"]

tags = [
     "spacex",
     "spacex-falcon9",
     "spacex-falcon9-stage-one",

     "ocean-landing",
     
     "blender",
     "blender-eevee",
     "blender-cycles",
     ]

[art]
image = "spacex-falcon9-booster-landing-burn"
#redbubble = "https://www.redbubble.com/people/zlsa/works/"

+++

This piece depicts a Falcon 9 booster in the final stages of its landing burn.
The landing legs have been unlatched and are beginning to deploy, the pistons pushing the legs out against the airstream.
At the top of the booster, the interstage-mounted grid fins continue to pivot to keep the booster pointed towards the landing pad.
Now that the single Merlin 1D engine in the center of the octaweb has slowed the booster down to a near-standstill, the turbopump exhaust flame mostly burns down instead of wrapping around the octaweb and up the side.

Looking closely at the clean white impression of the landing legs on the body, there are seven individual latches on the body to hold the landing leg in-place during ascent and descent.
These latches open up at the last minute, just a few seconds before touchdown, and a small starter piston pushes the legs out, giving the primary pneumatic pistons enough mechanical advantage to finish the job.
On the right side of the booster, beneath the "U" of the bottom leg, is a small white flap.
The flap protects one of two octaweb-mounted quick-disconnects from the chaos of launch and reentry.
Before launch, the propellants in the first stage booster are loaded through these quick disconnects.

<!--This 3D model the end result of hundreds of hours of research, modeling, texturing, and rigging.-->

# Technical Details

Everything you see in this piece was created with [Blender](/tags/blender) 2.80, [Eevee](/tags/blender-eevee), and [Cycles](/tags/blender-cycles).

There are two sets of PBR textures for the first stage; each of them is 2048x2048, and are produced with a custom Blender scene and rendered with Cycles.
There is an additional "cover" texture, used to mask out the sooty parts of the vehicle.
The Falcon 9 here is actually [pretty low-poly](https://host.zlsadesign.com/r1JD1yC0B.png), at ~40k vertices.
The normal maps really bring out the fine details in the legs and the body.

The lens dirt, vignette, and film grain are all pre-rendered in, you guessed it, Eevee.
The lens dirt image was created with a particle system, the particles being camera-facing planes with a custom simulated bokeh (to avoid the high render times of real bokeh, which isn't needed anyway in this case.)
The vignette and film grain are both pure shader solutions, rendered to images for compositing.

The Falcon 9 model is [fully rigged](https://host.zlsadesign.com/rJLEkiAAH.png).
The leg pistons slide in and out automatically as the leg bone is rotated.
The grid fins are fully rigged as well, and can open, close, and pivot.

# Links

The HDRI I used was found at [HDRIHaven](https://hdrihaven.com/). Their HDRIs are awesome; go check them out!

Let me know what you think about this piece on [Twitter](https://twitter.com/zlsadesign/) and [ArtStation](https://www.artstation.com/artwork/9enkmy).
And if you'd like this as a poster, check it out on [RedBubble](https://www.redbubble.com/people/zlsa/works/).
I highly appreciate all comments and critiques.
Thank you for checking this out!

---

This is a fan-made render, and no copyright infringement is intended.
I believe this work is sufficiently transformative for its use of copyrighted material to qualify as fair use.
