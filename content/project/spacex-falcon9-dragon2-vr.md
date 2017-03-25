+++
title = "SpaceX Falcon 9 and Dragon 2 3D model"

categories = ["3d", "art"]

date = "2017-03-24"

tags = [
    "spacex",
    "spacex-falcon9",

    "spacex-dragon2",
    "virtual-reality",

    "blender",
    "sketchfab",
    
    "3d-model"
]

[project]
url = "https://sketchfab.com/models/f709fc945bb2413faf2878aa613cde3d"

[embed]
type = "sketchfab"
id = "f709fc945bb2413faf2878aa613cde3d"

+++

This is a 3D model of the SpaceX [Falcon 9](/tags/spacex-falcon9)
rocket along with the [Dragon 2](/tags/spacex-dragon2) capsule. The
Falcon 9 is in its landed configuration (but with the soot
mysteriously washed off) and the Dragon 2 is in launch configuration
(except for, you know, the "being on the rocket" part.)

<!--more-->

# Technical details

The scene uses PBR techniques. The Falcon 9 textures were made with
Blender (in a separate model file); I do this to get clean normal maps
(along with albedo, metalness, and roughness maps.) My method is to
use Blender Internal; I enable a few render passes:

* AO (for the AO pass, obviously)
* Color (for albedo)
* Spec (for roughness)
* Normal (for the normal map)
* Material Index (for metalness; yeah, this is really hacky; no, I
  haven't found a better solution yet. Turns out Blender wasn't really
  built for rendering PBR maps...)

However, the normal map still needs a bit of extra processing, since
Blender bakes it with the wrong coordinate system (you can tell from
the black up-facing areas and the red/green edges.) To fix this, I
remap the range from `-1..1` to `0..1` with a color multiply and then
a color mix node; then, I invert it (since the normal is actually
backwards.) Note that your colorspace must be set to linear ("Display
Device: None") or gamma will be applied to the normal map, which will
totally screw it up.

I then manually switch the output around and export all the files. (I
could write a script for this, but manually exporting the textures
isn't that much of a time-waster yet.) Then, all I have to do is
reopen the actual model file and the new textures are all there!

This technique has some downsides, though: notably, I'm rather limited
in how many outputs I can repurpose for my evil means. I'm already
using Material index for metalness; I suppose I _could_ use UV
coordinates instead if I had to, but I'd rather have something I can
set per material instead of per mesh.
