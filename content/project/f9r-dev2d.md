+++
title = "F9R-Dev2D"

categories = ["web", "game", "programming"]

date = "2014-07-17"

tags = [
     "spacex-falcon9",
     "spacex-falcon9-stage-one",
     
     "vtvl",
     "f9r-dev2d"
     ]

[project]
url = "http://zlsa.github.io/f9r-dev2d/"
code = "https://github.com/zlsa/f9r-dev2d"
+++

F9R-Dev2D is a simplistic Falcon 9 landing game. It was originally
created as a programming-exercise-slash-fun-toy, and as a result, the
code could be far cleaner than it currently is.

To fly, use the arrow keys (or `A`/`D` for pitch and `Shift`/`Ctrl`
for throttle); `X` and `Z` throttle to zero and full throttle,
respectively. If the pitch direction feels backwards, toggle "flip
left-right".

<!--more-->

# Autopilot

The autopilot is designed only to land the Falcon 9 in either the `f9r
rtls` or `f9r rtls extreme` scenarios and with "hard mode" enabled. 

# Hard mode

The "hard mode" option simply reduces your gimbal range to realistic
levels and remaps the thrust from `0..1` to approximately `0.4..1`,
preventing unrealistically low throttle levels. It also tightens up
what's a "failed landing", so hard landings at twenty degrees of tilt
will count as a failure.
