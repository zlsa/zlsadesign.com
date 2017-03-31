+++
title = "Why is everybody building reusable rockets?"
description = "Since their inception, rockets have been thrown away after every launch. Why is this changing now?"

draft = true

date = "2017-03-31"

categories = ["writing"]

tags = [
     "spacex",
     "spacex-falcon9",
     "spacex-falcon9-stage-one",
     
     "blue-origin",
     "blue-origin-new-shepard",
     "blue-origin-new-shepard-propulsion-module",
     "blue-origin-new-glenn",
     "blue-origin-new-glenn-stage-one",
     ]
     
+++

# Since their inception, rockets have been thrown away after every launch. Why is this changing now?

{{< img
class="right"
src="/article/why-is-everybody-building-reusable-rockets/media/space-shuttle-launch.jpg"
caption="The Space Shuttle lifts off."
attr="NASA"
attrlink="https://spaceflight.nasa.gov/gallery/images/shuttle/sts-120/html/sts120-s-028.html"
>}}

In the decades since the first experimental rockets flew, the only
launch vehicle that was capable of any kind of reuse was the Space
Shuttle. For various reasons, the Space Shuttle cost far more to fly
than an equivalent non-reusable rocket; it did its job well, but in
the end, it was too expensive to refurbish and rebuild the orbiter
after every launch. In 2011, the Space Shuttle program came to an end.

<!--more-->

Reusable rockets aren't new. Although SpaceX was the first company to
successfully recover the first stage of an orbital-class rocket in
December of 2015, reusable rockets have been considered since the
1960s. Even the Saturn V, the rocket that launched humans to the Moon,
was the subject of many proposals that would enable partial recovery
of the launch vehicle. In the end, none of these proposals were ever
implemented.

In the 1990s, McDonnell Douglas began testing the
[DC-X](https://en.wikipedia.org/wiki/McDonnell_Douglas_DC-X), an
experimental testbed for building rockets capable of vertical landing
and takeoff, or VTOL. The DC-X vehicle first flew in 1993, and over
the next three years it flew eleven more times. These were all small
hops of only one or two kilometers; the final flight reached an
altitude of only 2.5 kilometers. Even though it never demonstrated
high-altitude flights, it proved that building a VTOL rocket was
feasible.

The DC-X program was shelved when a landing leg failed to deploy and
the rocket tipped over after landing. NASA did not have the budget to
devote to the DC-X program, and it was cancelled in 1996. Several of
the remaining DC-X engineers are
[now involved](http://www.airspacemag.com/space/black-day-at-white-sands-1381694/)
with [Blue Origin](/tags/blue-origin), who is working on its own
reusable rockets today.

---

Now, for an explanation of why it's so easy to reuse airplanes and
cars and why it's so difficult to reuse rockets.

Rockets that reach orbit need to fly very, very fast. There is a huge
difference between reaching _space_, which is only 100km away from sea
level; and _orbit_, which requires a velocity of at least 7.8
kilometers per second. That's 22 times the speed of sound. The only
way to get that fast is to bring a lot of fuel with you, and to bring
fuel you need a place to store it.

At liftoff, modern rockets are about 90% fuel by mass. Of the
remaining 10% mass, the actual payload, the part that actually reaches
orbit, is usually less than 3%. The lighter the rocket, the heavier
the payload it can launch into orbit. Everything you add that helps
make a rocket reusable also reduces the maximum payload of that
rocket.

This has made reusable rockets a difficult pill to swallow. The
payload capacity would need to be cut nearly in half to make even the
first stage reusable, and then you would need to prove that the stage
could reliably land and fly again with minimal maintenance. It's a
huge gamble that might not even work out.

# SpaceX's Recovery Proving Grounds

In 2001, Elon Musk wanted to get the public excited in Mars, to push
Congress to increase funding for NASA. He decided to send a greenhouse
to Mars, called Mars Oasis; in his words, it would "show great images
of green plants on a red background" and "get the public excited
[about Mars.]" The greenhouse itself would be simple; but the rocket
launch would not. Musk visited Russia three times, attempting to buy
used ICBMs; however, they were far more expensive than he thought they
would be. On the plane back to the United States after his last trip
to Russia, he turned to aerospace consultant and friend Jim Cantrell
and said, "I think we can build a rocket ourselves."

In 2002, Elon Musk founded SpaceX with the goal of making life
multiplanetary. As he saw it, the issue was that expendable rockets
have a fixed cost: unlike with airplanes, you can't reduce the cost by
flying them multiple times. The price of a launch includes the full
price of the rocket.

But before SpaceX could tackle reusability, they needed to build a
rocket that could reach orbit. Their first rocket, the Falcon 1, was a
21-meter tall two-stage rocket. Its maiden launch, in 2006, ended in
failure when a corroded nut caused an engine fire; the rocket fell
back into the ocean less than a minute after liftoff.

The next two launches got closer, with Flight 3 nearly reaching
orbit. At this point, though, SpaceX was running low on money for a
fourth flight, and Elon had to personally fund the fourth launch.

Thankfully, the fourth launch of the Falcon 1 was a complete success,
as was the fifth. SpaceX had attempted to recover some of the Falcon 1
first stages with parachutes, but they all broke up as they fell
through the atmosphere at supersonic speeds. At this point, SpaceX
decided to switch over to building and launching their new Falcon 9.

## The Falcon 9 v1.0

{{< img
class="right"
src="/article/why-is-everybody-building-reusable-rockets/media/falcon9-v1.0-launch.jpg"
caption="The CRS-2 Falcon 9 lifts off, carrying the Dragon capsule to the ISS."
attr="NASA"
attrlink="https://commons.wikimedia.org/wiki/File:SpX_CRS-2_launch_-_further_-_cropped.jpg"
>}}

The [Falcon 9 v1.0](/tags/spacex-falcon-9) is a two-stage rocket
standing 54 meters tall. It's large enough to launch cargo and crew to
the International Space Station with the
[Dragon capsule](/tags/spacex-dragon), and because it has nine
engines, it can still complete its mission even if an engine fails
during launch.

The Falcon 9 launched for the first time in 2010 and performed
flawlessly, deploying a dummy spacecraft into low-Earth orbit. Like on
the Falcon 1, SpaceX tried to put parachutes into the Falcon 9 first
stage; once again, the stages broke up before the parachutes even had
a chance to deploy.

So, in 2011, SpaceX announced that instead of using parachutes to
recover the first stage, they'd use actively-guided propulsive
landing. This means they'd use the Falcon 9's engines to guide the
booster back to land. This would involve
[several different maneuvers]({{< ref
"infographic/trajectory/spacex-falcon9-booster-rtls.md" >}}); first,
the booster would need to turn back towards land and restart three
engines for the **boostback burn**; then, it would turn to face
engines-first and restart the same three engines to slow it down in
the **entry burn**; finally, as it approached its landing pad, it
would start up the single center engine for the **landing burn**;
then, seconds before landing, it would deploy its four landing legs
and touch down on land only a few kilometers from its launchpad.

{{< img
class="left"
src="/article/why-is-everybody-building-reusable-rockets/media/grasshopper.jpg"
caption="The Grasshopper testbed, in 2012. Note the mechanic standing next to the landing leg."
attr="Steve Jurvetson"
attrlink="https://www.flickr.com/photos/jurvetson/7971310054/in/photostream/"
>}}

However, such a plan would need a lot more fuel since the booster
would need to use its own fuel to fly back and land. It would also
require very accurate control of the booster, or it would land dozens
of kilometers off-target, or worse, hit the ground at Mach 0.8 and
explode.

So SpaceX built an experimental rocket, called the
[Grasshopper](https://en.wikipedia.org/wiki/Grasshopper_(rocket)). It
made eight successful flights in 2012 and 2013, demonstrating accurate
throttle and gimbal control of the engine. These flights were all
small hops, similar to those made by the DC-X. Each flight was a
complete success; in 2013, after the vehicle had demonstrated stable
hovering, horizontal diverts, and reached an altitude of over 700
meters, the vehicle was retired and replaced with the F9R-Dev1.

{{< img
class="left"
src="/article/why-is-everybody-building-reusable-rockets/media/f9r-dev1.jpg"
caption="The F9R-Dev1 testbed in-flight. Note the four landing legs."
attr="SpaceX"
attrlink="https://www.flickr.com/photos/spacex/17127808431/"
>}}

The F9R-Dev1 was a more advanced version of the Grasshopper; where the
Grasshopper featured custom landing legs and other hardware, the
F9R-Dev1 was a mostly standard Falcon 9 v1.1 booster; it even featured
the four prototype carbon-fiber landing legs. The F9R-Dev1 flew five
times, reaching an altitude of one kilometer; on its final flight, a
blocked sensor caused the vehicle to veer off course, and the flight
termination system was triggered, ending the flight.

In 2013, SpaceX flew the first flight of a significantly larger Falcon
9 v1.1, with almost twice the fuel capacity, along with internal
modifications that would allow legs and other hardware to be
attached. Over the next few flights of the upgraded Falcon 9, SpaceX
attempted to perform soft ocean landings to demonstrate the
technology; the first successful landing was with the CRS-3
mission. The booster touched down on the ocean's surface during a
storm, and although it splashed down gently, it broke apart when it
hit the ocean, as expected.

{{< img
class="left"
src="/article/why-is-everybody-building-reusable-rockets/media/jrti.jpg"
caption="'Just Read the Instructions', SpaceX's first droneship."
attr="SpaceX"
attrlink="https://www.flickr.com/photos/spacex/17127808431/"
>}}

{{< img
class="right"
src="/article/why-is-everybody-building-reusable-rockets/media/new-shepard-landed.jpg"
caption="The NS2 booster, the first ever rocket to reach space and land vertically."
attr="Blue Origin"
attrlink="https://www.blueorigin.com/gallery"
>}}

Next, SpaceX needed a place to land. They hadn't yet built a landing
pad, and they also hadn't received permission to bring a rocket back
to land. Ocean landings wouldn't work; the booster was so tall that it
would disintegrate when it fell into the ocean. So they modified a
barge, converting it to a powered droneship, and painted a giant "X"
on it. It was sent out into the ocean for the first time in 2015, for
the CRS-5 mission.

{{< img
class="left"
src="/article/why-is-everybody-building-reusable-rockets/media/crs5-crash.jpg"
caption="The CRS-5 booster smashing into JRTI"
attr="SpaceX"
attrlink="https://vine.co/v/OjqeYWWpVWK"
>}}

The CRS-5 launch went perfectly, and the Falcon 9 booster performed
all the necessary engine burns flawlessly; however, the grid fins used
for maneuvering the booster ran out of hydraulic fluid, and the
booster smashed into the droneship at highway speeds. Needless to say,
the landing was not very smooth, and the only parts that came back
were in a pile on the droneship, covered by a tarp.

The next attempt, with the CRS-6 mission, did far better. The booster
performed perfectly, but when it was less than ten seconds from
landing, the engine throttle setting got stuck, and the booster landed
hard and tipped over seconds later. Just like CRS-5, they brought back
the remains of the booster in a pile.

On the next launch, with the CRS-7 mission, the launch vehicle failed
before there was a chance to attempt a landing. SpaceX was grounded
for several months while they fixed the problems that caused the CRS-7
failure.

***

In the meantime, Blue Origin's experimental test program, shrouded in
secrecy for years, announced that their New Shepard rocket had become
the first ever rocket to reach space and land vertically. The New
Shepard booster, like the Falcon 9, was designed to be reusable;
unlike SpaceX, Blue Origin had been planning to land their rockets
propulsively from the start, and they had been quietly experimenting
with it for over a decade.

The New Shepard vehicle is about 15 meters tall and has many different
types of fins to stabilize and control the vehicle as it returns to
Earth; notably, at the bottom of the vehicle, there are four
maneuvering fins; and at the top of the vehicle, there are drag brakes
(to slow the vehicle) and wedge fins (to keep the vehicle
stable) mounted to the ring fin.

Whereas the Falcon 9's purpose is to launch payloads into orbit, the
New Shepard is both a testbed and a space tourism platform. It's
capable of launching multiple space tourists to 100km and returning
them safely, requiring far less energy than reaching orbit. For this
reason, the New Shepard is fully reusable; both the crew capsule and
the propulsion module can be recovered and reused for future flights.

{{< img
class="right"
src="/article/why-is-everybody-building-reusable-rockets/media/og2m2-landed.jpg"
caption="The Orbcomm OG2-M2 booster after its landing."
attr="SpaceX"
attrlink="https://www.flickr.com/photos/spacex/23273082823/"
>}}

***

SpaceX's next mission was the Orbcomm OG2-M2 launch; the first flight
after the CRS-7 inflight breakup. It was also the first Falcon 9 to be
powered by densified propellant; this, combined with the lightweight
payload, meant that the Falcon 9 booster could return to the launch
site.

The flight was picture-perfect, and less than ten minutes after
liftoff, the booster touched down smoothly and softly at SpaceX's
landing pad at Cape Canaveral, marking the world's first recovery of
an orbital-class booster. Over the next few months, SpaceX continued
to recover every core they could, and so far, they've recovered six
more boosters; two that landed on land, and four that landed on
SpaceX's droneships.

Less than 12 hours ago, on March 30, 2017, SpaceX made history when
they launched a rocket with a reused booster for the SES-10 mission,
cementing SpaceX's place in history as the first company to ever refly
a recovered booster from an orbital-class launch vehicle. 

***

{{< img
class="left"
src="/article/why-is-everybody-building-reusable-rockets/media/new-shepard-abort.jpg"
caption="The NS2 booster, underneath the crew capsule at the moment of abort motor ignition."
attr="Blue Origin"
attrlink="https://www.blueorigin.com/gallery"
>}}

In September of 2016, SpaceX announced their
[Interplanetary Transportation System](/tags/spacex-its), a rocket
SpaceX hopes will begin the colonization of Mars. Both the first and
second stages will be recovered and reused on every launch,
dramatically reducing launch prices and opening up whole new worlds of
human space exploration. SpaceX plans to reuse the booster a
staggering 1,000 times; the propellant tanker and Mars lander are
reused 100 and 12 times, respectively. These prices bring Mars
colonization within reach for the first time ever.

***

The final flight of the Blue Origin NS2 vehicle was in 2016, with the
crew capsule performing an in-flight abort to verify the safety of the
crew in the case of a booster failure. Miraculously, the booster
survived the heat and debris from the solid rocket motor exhaust, then
proceeded to continue its flight to space, performing a smooth landing
only a few minutes later. The booster was retired; Blue Origin plans
to perform more test flights this year, and they're planning to fly
crew this year.

Recently, Blue Origin unveiled their proposed orbital launch vehicle,
the New Glenn. Like the Falcon 9, the first stage is built to be
reusable; it will land itself on a ship in the ocean under its own
engine power, just like SpaceX.

With Blue Origin and SpaceX both demonstrating that booster reuse is
possible, it now falls to the rest of the industry to follow
along. Soon, the price for a launch on a reused rocket will drop, and
the entire rocket industry will need to lower their prices to remain
competitive. I, for one, cannot wait for the low-cost future of
spaceflight, where launches don't cost tens or hundreds of millions of
dollars; where you don't need to be a giant international corporation
to launch your satellites. And just maybe, a future where humanity
lives on both Earth and Mars.
