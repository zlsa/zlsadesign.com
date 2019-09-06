+++
title = "Xon Wasp departing Venalis Station"

date = "2019-09-03"

categories = ["3d", "art"]

tags = [
     "xon-wasp",
     "reports-from-the-orion-arm",
     "venalis-station",
     "blender",
     "blender-eevee",
     ]

[hero]
background = "/background/reports-from-the-orion-arm/spaceship-pattern.jpg"
compressed = true

[art]
image = "xon-wasp-venalis-station-departure"
redbubble = "https://www.redbubble.com/people/zlsa/works/41013640-xon-wasp-departing-venalis-station"

+++

This piece shows the [Xon Wasp](/tags/xon-wasp) general-purpose atmosphere-capable jump ship as it travels from Venalis Station to a nearby mining outpost.
To conserve fuel, the jump drive isn't engaged for short moon-to-moon hops like this one.
Instead, the trip is performed entirely in normal space, where efficient maneuvers make a real difference.

<!--[trans-Mars injection burn]({{< ref
"term/tmi.md" >}}) that marks the beginning of its coast to Mars.-->

<!--more-->

<!--
{{% note %}}
This science-fiction excerpt is one of the [Reports from the Orion Arm](/tags/reports-from-the-orion-arm).
{{% /note %}}
-->

# Background

The Xon Wasp is a marvel of engineering.
Design work began in 3242, and after only 9 years --- a remarkably short span of time --- it was certified for general sale by the International Astronautical Union.
As an atmosphere-capable jump ship, it's a rare breed of spacecraft; able to take off from the surface of an atmospheric planet, travel up to 150 light-years, then rendezvous and dock with a space station.
Most ships can do either one or the other, requiring surface-to-orbit shuttles to carry payload to and from the surface of atmospheric planets.
This flexibility comes at a cost, though: its size is limited by existing launch infrastructure, and despite its small size, it's staggeringly expensive.
For these reasons, the Wasp is very popular with high-flying executives, heads of state, and other people who need its flexibility and can stomach the price.

In this promotional photo, the Wasp is traveling from Venalis Station to a small mining outpost in the rings of the gas giant.
It's performing its correction burn at its perigee around the asteroid to its left to maximize performace and efficiency.
Its primary engines are burning hydrogen, and the reactor is at near-maximum capacity, as evidenced by the glowing radiator panels (only the right-side radiator panel is visible in this photo.)

Inquiries about the Xon Wasp can be made at your system's Xon shipyard.
We look forward to doing business with you.

# Technical Details

Everything you see in this piece was created 100% with [Blender](/tags/blender) 2.80 and [Eevee](/tags/blender-eevee) (we don't need Cycles here!)
The environment a cubemap, pre-rendered in Eevee; it's imported directly into the primary scene with a custom cubemap world shader to avoid the distortion from equirectangular projections.
The ship itself is rather detailed, with panels being built into the geometry, not delineated with a normal map.
(The panels are shrinkwrapped to a hidden "body shape" object to keep their normals consistent even when their shapes are tweaked.)
The radiator texture is pre-rendered in Eevee as a grayscale heatmap; the glowing colors are added in the primary scene with a custom shader.
The engine volumetric effects are created with judicious use of fresnel and add blending; there are dozens if not hundreds of overlapping meshes at any point in the image.

The lens flares, lens dirt, vignette, and film grain are all pre-rendered in, you guessed it, Eevee.
The lens dirt image was created with a particle system, the particles being camera-facing planes with a custom simulated bokeh (to avoid the high render times of real bokeh, which isn't needed anyway in this case.)
The vignette and film grain are both pure shader solutions.
The lens flares are created with many layers of custom shaders and exported as high-dynamic-range EXR files to prevent banding or clipping.

Compositing and post-processing are also done in Blender, in a separate file to allow for screen-space effects like lens flare to be created in the 3D Editor.
The pre-composite render is not included in this scene; instead, it's added in the compositor to prevent Eevee's antialiasing from reducing its quality.
The lens flares are 3D elements, positioned on top of the pre-composite render with the help of a reference image.
Finally, the composite scene can be rendered, and the final image you see here can be saved.

# Links

Let me know what you think about this piece on [Twitter](https://twitter.com/zlsadesign/status/1170117948947587072) and [ArtStation](https://www.artstation.com/artwork/4b2VoY).
And if you'd like this as a poster, check it out on [RedBubble](https://www.redbubble.com/people/zlsa/works/41013640-xon-wasp-departing-venalis-station).
I highly appreciate all comments and critiques.
Thank you for checking this out!
