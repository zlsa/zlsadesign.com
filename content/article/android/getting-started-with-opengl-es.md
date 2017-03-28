+++
title = "Getting started with OpenGL ES 2.0 on Android"
description = "Learn how to use OpenGL ES 2.0 in Android by example."

date = "2017-03-27"

categories = ["android"]

tags = [
     "android",
     "android-app",
     "opengl",
     "opengl-es",
     ]

[hero]
background = "/article/spacex-journey-to-mars-2018/media/mars-approach.jpg"
+++

Google's Android
[developer documentation](https://developer.android.com/guide/topics/graphics/opengl.html)
tends to be pretty bare. Third-party documentation and tutorials are
usually years out of date and accompanied by code that was obviously
hacked together for the tutorial; sometimes, they ask you to clone a
GitHub repository to get started.

I learn by example, and all of the above makes it more difficult than
it should be. I won't provide example apps or copy-pasteable classes;
instead, I'll work through a problem, one step at a time.

I hope to make "Getting started with <whatever> on Android" a regular
series; this article covering OpenGL ES 2.0 is the first.

<!--more-->

# The problem

OpenGL has traditionally been... difficult, to say the least. The API
is unintuitive and often poorly-documented, and each platform behaves
slightly differently.

Diving right in, then. Most apps need a bit more than a "Hello, world"
triangle; but often, importing a full OpenGL library is overkill. This
"getting started" guide will try to bridge the two.

# High-level overview

At the time of writing, Android supports 4 different versions of
OpenGL ES:

* OpenGL ES 1.0 and 1.1. These are supported since Android 1.0 (API 1) and
  should not be used in any new code.
* OpenGL ES 2.0. This version has been supported since Android 2.2
  (API 8) and is available on all hardware running 2.2 or above.
* OpenGL ES 3.0. This version is supported on _some_ hardware starting
  with Android 4.3 (API 18.) Android phones running Android 4.3 or
  above do not _necessarily_ support OpenGL ES 3.0.
* OpenGL ES 3.1. This version is supported starting with Android 5.0
  (API 21.)
  [The official documentation for OpenGL ES on Android](https://developer.android.com/guide/topics/graphics/opengl.html)
  does not mention whether or not it's available on any hardware
  running Android 5.0 or above, but according to the
  [Wikipedia article on OpenGL ES](https://en.wikipedia.org/wiki/OpenGL_ES#OpenGL_ES_3.1_2),
  it's only supported on some chips and is not guaranteed to be
  available.

Realistically, an app that uses OpenGL ES must support OpenGL ES 2.0
at a minimum, and potentially OpenGL ES 3.0 and 3.1 on the right
hardware. OpenGL ES 2.0 is adequate for most applications (the newer
APIs support more advanced features such as more texture options,
compute shaders, and different texture compression algorithms;
however, these aren't strictly necessary in most cases.)

This article will cover only OpenGL ES 2.0 and not 1.0 or 3.0/3.1.

# How OpenGL ES works in Android

Android's
[`GLSurfaceView`](https://developer.android.com/reference/android/opengl/GLSurfaceView.html)
implements the Android `Surface` (the final texture, to be drawn
onscreen); the EGL "display" (the equivalent of an OpenGL context);
and some other minor features (such as OpenGL error-checking and
rendering in another thread.)

The `GLSurfaceView` does _not_ render anything; it merely provides a
surface to which your own render can draw. A renderer must implement
[`GLSurfaceView.Renderer`](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer.html);
more specifically, it must implement the following methods:

* [`abstract void onDrawFrame(GL10 gl)`](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer.html#onDrawFrame(javax.microedition.khronos.opengles.GL10)); called when the
  `GLSurfaceView` needs a new frame.
* [`abstract void onSurfaceChanged(GL10 gl, int width, int height)`](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer.html#onSurfaceChanged(javax.microedition.khronos.opengles.GL10, int, int));
  called when the size of the `GLSurfaceView` has changed.
* [`abstract void onSurfaceCreated(GL10 gl)`](https://developer.android.com/reference/android/opengl/GLSurfaceView.Renderer.html#onSurfaceCreated(javax.microedition.khronos.opengles.GL10, javax.microedition.khronos.egl.EGLConfig)); called before
  `onDrawFrame` and after the class has been instantiated.

You might notice the `GL10 gl` argument in all three of the above
methods; that's from the OpenGL ES 1.0 days, and if you're using 2.0
you won't ever need to touch them.

# Manifest

Be sure to add the relevant manifest `uses-feature` tag! Android
itself does not use or care about this tag, but if your app is
available on the Google Play store, this tag will hide your app on
phones that don't support OpenGL ES 2.0.

```xml
<uses-feature android:glEsVersion="0x00020000" android:required="true" />
```

The `android:glEsVersion` attribute is the important part here; if
your app requires OpenGL ES 3.0, use the value `0x00030000`; if your
app requires OpenGL ES 3.1, use the value `0x00030001`.

# Minimal `GLSurfaceView`

This is the simplest possible implementation of a `GLSurfaceView`. All
it does is set the version of OpenGL ES it's going to use, creates the
`GLSurfaceView.Renderer`, then sets it as the renderer.

```java
class CustomGLSurfaceView extends GLSurfaceView {

  private final CustomGLRenderer this.renderer;

  public CustomGLSurfaceView(Context context){
    super(context);

    // Use OpenGL ES 2.0
    setEGLContextClientVersion(2);

    // Instantiate our class (that extends GLSurfaceView.Renderer)
    this.renderer = new CustomGLRenderer();

    // Use our CustomGLRenderer.
    setRenderer(this.renderer);
  }
}
```

`GLSurfaceView` extends `View`, so you can treat it as a normal view
and do things like the following (in an `Activity`):

```java
@Override
protected void onCreate(Bundle state) {
  super.onCreate(state);

  this.game = new Game();

  this.render_view = new RenderView(this);
  ((RenderView) this.render_view).setGame(this.game);

  setContentView(this.render_view);
}
```

# Minimal implementation of `GLSurfaceView.Renderer`

This is a minimal implementation of a renderer implementing all three
required functions.

```java
public class CustomGLRenderer implements GLSurfaceView.Renderer {

  public void onSurfaceCreated(GL10 unused, EGLConfig config) {
    // Color equivalent to #ff00ff (i.e. magenta; very good for debugging)
    GLES20.glClearColor(1.0f, 0.0f, 1.0f, 1.0f);
  }

  public void onDrawFrame(GL10 unused) {
    GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT);
  }

  public void onSurfaceChanged(GL10 unused, int width, int height) {
    GLES20.glViewport(0, 0, width, height);
  }
}
```

When the surface is first created, it sets the clear color with [`glClearColor`](https://developer.android.com/reference/android/opengl/GLES20.html#glClearColor(float, float, float, float)); when the viewport size changes, it sets the viewport with [`glViewport`](https://developer.android.com/reference/android/opengl/GLES20.html#glViewport(int, int, int, int));
and when it needs to render it simply clears the color buffer bit with [`glClear`](https://developer.android.com/reference/android/opengl/GLES20.html#glClear(int)).
