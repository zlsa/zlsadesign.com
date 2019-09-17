+++

title = "Building for Oculus Quest on Linux with UE4"

date = "2019-09-08"

categories = ["UE4", "VR"]
tags = [
    "linux",
    "unreal-engine-4",
    "oculus-quest",
    "vr"
]

summary = "A short guide, explaining how to build an Unreal Engine 4 game for the Oculus Quest, on Linux."

+++

First off, a word of warning. Building for the Oculus Quest on Linux
with Unreal Engine 4 is not officially supported. This is also my
first foray into UE4 development, and I'm not familiar with the
terminology or architecture yet.

{{% note title="Versions" %}}

This guide was tested with Arch Linux and Unreal Engine 4.23 (from the latest `git` master, at time of writing.)
The procedure should be largely similar on other distributions as well, but no guarantees.

{{% /note %}}

<!--more-->

# Setting up UE4 on Linux

First things first: let's get UE4 compiled and running on Linux.

## Getting the source code

First, you'll need to get a copy of the Unreal Engine 4 source code.
While the source code is available to UE4 developers, it's not open-source, and you'll need to [sign up for an Epic Games account](https://accounts.epicgames.com/login), then [connect your GitHub account to your Epic Games account](https://www.unrealengine.com/en-US/ue4-on-github)).

Once you've done this, you should have access to the [EpicGames/UnrealEngine](https://github.com/EpicGames/UnrealEngine) repository.
The next step is to clone the repository.
This will take quite a long time, depending on your internet speed.
A normal clone will download several gigabytes.

{{< language "Shell" "~/" >}}

```
$ git clone git@github.com:EpicGames/UnrealEngine.git
...
$ ls
UnrealEngine
$ cd UnrealEngine
```

## Setting up dependencies

You'll need to install your system's packages for software development.
On Arch Linux, this is `base-devel`.
(You'll also need `git`, obviously.
Hopefully you've already completed this before getting to this step.)

Now, you'll need to run some scripts to set up the repository for compilation.
First, there's `Setup.sh`, which downloads, compiles, and installs dependencies.
This will take some time to run, and will download a significant amount of data.

{{< language "Shell" "~/UnrealEngine/" >}}

```
$ ./Setup.sh
...
$
```

Once this is done, you can run `GenerateProjectFiles.sh`.

{{< language "Shell" "~/UnrealEngine/" >}}

```
$ ./GenerateProjectFiles.sh 
...
$
```

## Compiling UE4

All the setup is complete, and you're now ready to compile UE4 itself.
This can take several hours, even on insanely powerful computers.

{{< language "Shell" "~/UnrealEngine/" >}}

```
$ make -j16
...
$
```

Replace `16` in the above command with the appropriate number of threads for your processor.
Remember, this will take several hours, so go and watch a couple thousand fast and lazy Blender 2.80 tutorials from [Ian Hubert](https://www.youtube.com/watch?v=U1f6NDCttUY&list=PL4Dq5VyfewIxxjzS34k2NES_PuDUIjRcY) or [CGMatter](https://www.youtube.com/watch?v=j5GFtJPvQXo&list=UUy1f4m64dwCwk8CBZ_vHfPg) or something.

After compilation is complete, you should be able to run the UE4 binary itself:

{{< language "Shell" "~/UnrealEngine/" >}}

```
$ ./Engine/Binaries/Linux/UE4Editor
```

## One more thing

If you run UE4 and create a project, then click on "Build", UE4 will crash after a few minutes.
This is because UE4 expects a "multicast loopback" interface.
To enable this, run the following commands as root:

{{< language "Shell" "~/UnrealEngine/" >}}

```
# ip route add 230.0.0.0/8 dev lo
# ip link set lo multicast on
```

Once you've done this, you should be able to click "Build" and watch it successfully complete.

# Setting up the Android SDK/NDK

<!--Now that I've relayed the official UE4 on Linux build guide to you, let's get on to the unsupported, magical part: building for the Oculus Quest.-->

The Android SDK (software development kit) and NDK (native development kit) are required to deploy to Android from UE4.

{{% note title="Android NDK version" %}}

UE4 requires Android NDK to be version 14b-18b, whereas the `android-ndk` package in the Arch User Repository is version 20.
They recommend version 14b, so that's what I'm installing here.
If you're using the NDK anywhere else, I recommend you manually install version 14b to a UE4-specific path to avoid issues with your other Android projects.

{{% /note %}}

## Installing dependencies for Android

You'll need to install the Android SDK and NDK packages.
These are in the [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository) as [`android-sdk`](https://aur.archlinux.org/packages/android-sdk/) and [`android-ndk-14b`](https://aur.archlinux.org/packages/android-ndk-14b/), respectively.
Despite what the UE4 guides say, using the AUR Android packages seems to work perfectly without nVidia's CodeWorks for Android.
These will take some time to install as well.
When they're installed, you'll need to log out and log back in to apply the new paths.
The SDK is installed in `/opt/android-sdk`, and the NDK is installed in `/opt/android-ndk`.

## Telling UE4 where the SDK/NDK are

The next step is to tell Unreal Engine where the Android SDK and NDK are.
To do this, open UE4 and open the Project Settings.

# Troubleshooting
