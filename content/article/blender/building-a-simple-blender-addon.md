+++
title = "Building a simple Blender Addon"
description = "Learn how to create a simple Blender addon by example."

draft = true

date = "2017-04-07"

categories = ["blender", "tutorial"]

tags = [
     "blender",
     "blender-addon"
     ]
     
+++

Blender's addon API may be documented, but the documentation is not
all in one place, and lots of the intricacies (such as UI layout)
aren't documented very well. Here, I'll show you how all the different
Blender APIs go together to create an addon.

<!--more-->

# Some useful tips

* Pressing `Shift+Enter` within Blender reloads all the active
  addons. This is equivalent to closing and reopening Blender.

* You may want to run Blender from a terminal. This way, you can see
  anything printed to the console with Python's `print()` function.

* Enable "Tooltips" and "Python Tooltips" in the "Interface" tab of
  Blender's User Preferences (`Ctrl-Alt-U`.) This makes it easy to see
  the names of operators and properties.

# Addon Location

A Blender addon is just a Python module or package, located in
Blender's addon folder. The location of Blender's addon folder depends
on your OS.

{{< language "" "Windows" >}}

```
C:\Users\<username>\AppData\Roaming\Blender Foundation\Blender\<blender-version>\scripts\addons\
```

{{< language "" "Mac" >}}

```
/Users/<user>/Library/Application Support/Blender/<blender-version>/scripts/addons/
```
{{< language "" "Linux" >}}

```
/home/<user>/.blender/<blender-version>/scripts/addons/
```

For example, if your addon is a Python file named `object_duplicate_translate.py`, it
would be located in `[...]/scripts/addons/object_duplicate_translate.py`.

> ## A quick note on packages vs modules

> A Python `package` is a directory containing at least
> `__init__.py`. A Python `module` is just a single file. For our
> addon, `object_duplicate_translate`, we don't need multiple files so
> we're using a single module named `object_duplicate_translate.py`.
> However, if you are building a complex addon that uses multiple
> files, you would put `bl_info` in
> `object_duplicate_translate/__init__.py`.

# Metadata

Before you can do much of anything, you need to tell Blender about
your addon. To do this, you set the global variable `bl_info` in the
main Python file of your addon:

{{< language "Python" "object_duplicate_translate.py" >}}


```py
# ...

bl_info = {

    # The name of your addon. This is shown in the addon tab in
    # Blender's user preferences.

    'name': 'Duplicate and Translate',
    
    # A short, one-line description; this is also displayed in the
    # user preferences.
    'description': 'Duplicates and translates selected object(s)',

    # The author of this addon.
    'author': 'Jon Ross',

    # A tuple, containing the addon version.
    'version': (0, 1, 0),
    
    # The earliest Blender version this addon will work with. If
    # you're not sure what versions of Blender your addon is
    # compatible with, use the version of Blender you're developing
    # the addon with.
    'blender': (2, 78, 0),

    # This is where users should look for your addon.
    'location': 'View3D > Object > Transform > Duplicate and Transform',

    # This is shown to users in the addon tab of Blender's user preferences.
    'warning': 'This is my first Blender addon. Make of that what you will.',

    # This can be either 'OFFICIAL', 'COMMUNITY', or
    # 'TESTING'. 'OFFICIAL' should only be used if your addon is
    # included with Blender. (If you're not sure, don't use
    # 'OFFICIAL'.) 'COMMUNITY' and 'TESTING' are both fine to
    # use. Note that 'TESTING' addons aren't shown by default in
    # Blender's addon list.
    'support': 'TESTING',

    # Addon category; shown on the left side of Blender's addon list
    # to make filtering simpler. This must be one of the categories as
    # listed in Blender's addon tab; if it's not, it will create a new
    # category for your addon (which may be good or bad.) Don't create
    # new categories to make your addon stand out.
    'category': '3D View',

    # Optional; specifies the wiki URL for an addon. This will appear
    # in your addon listing as "Documentation".
    'wiki_url': '<documentation URL>',

    # Optional; specifies the bugtracker URL for an addon. This will
    # appear in your addon listing as "Report a Bug".
    'tracker_url': '<bugtracker URL>'
}
    
# ...
```

Obviously, you don't need to keep the comments I've included; here's
the same metadata block, just without comments.

{{< language "Python" "object_duplicate_translate.py" >}}

```py
# ...

bl_info = {
    'name': 'Duplicate and Translate',
    'description': 'Duplicates and translates selected object(s)',
    'author': 'Jon Ross',
    'version': (0, 1, 0),
    
    'blender': (2, 78, 0),

    'location': 'View3D > Object > Transform > Duplicate and Transform',
    'warning': 'This is my first Blender addon. Make of that what you will.',
    'support': 'TESTING',
    'category': '3D View',

    'wiki_url': '<documentation URL>',
    'tracker_url': '<bugtracker URL>'
}
    
# ...
```

# Creating an `Operator`

"Operator" is Blender's name for a single operation; for example,
adding a cube with `bpy.ops.mesh.primitive_cube_add()`, translating an
object with `bpy.ops.transform.translate()`, and even rendering the
scene `bpy.ops.render.render()`. In short, every button that performs
an _action_ extends the base `bpy.types.Operator` class.

(Side note: you can search through a list of available `Operator`s at
any time by pressing the spacebar.)

An `Operator` is simply a class that extends `bpy.types.Operator`
(note that you'll need to `import bpy` or that won't work.) A basic
`Operator` class must set the static variables `bl_idname` to a valid
Python identifier, and `bl_label` to the user-facing name of the
operator. For inspiration, hover over buttons in Blender to see what
the built-in operators are called. You can also set `bl_description`
to provide a description of the operator. More information available at [Blender's official documentation.](https://docs.blender.org/api/blender_python_api_current/bpy.types.Operator.html#bpy.types.Operator)

{{< language "Python" "object_duplicate_translate.py" >}}

```py
# ...

class DuplicateAndTranslate(bpy.types.Operator):
    bl_idname = 'transform.duplicate_and_translate'
    bl_label = 'Duplicate and Translate'
    bl_description = 'Duplicate and translate selected object(s)'
 
   def execute(self, context):
       return {'FINISHED'}
# ...
```

The `execute()` method is called whenever the user executes the
operator; it's given the current context (containing `context.object`
for the active object, `context.scene` for the active scene,
etc. Learn more about contexts at
[Blender's official documentation.](https://docs.blender.org/api/blender_python_api_current/bpy.context.html))

Note that the operator itself doesn't do anything yet; it just returns a
[Python set](https://docs.python.org/3/tutorial/datastructures.html#sets)
containing the string value `FINISHED`.
([Here's a list](https://docs.blender.org/api/blender_python_api_current/bpy.types.Operator.html#bpy.types.Operator.execute)
of other values you can return from `execute()`.)

Since other operators can be called from Python, it's quite simple to
duplicate the active object by just using Blender's built-in
"Duplicate" operator. But first, we need to find out what it's
called.

## Using Blender

First, you'll need to make sure "Python Tooltips" is enabled in the
"Interface" tab of Blender's user preferences. With this option
enabled, tooltips will show you the operator or property path when you
hover over operator buttons or input fields. Just find a place within
the UI to run the "Duplicate" operator; a good place is in the
"Object" menu in the 3D View. From this, you can see that "Duplicate
Objects" is called `object.duplicate_move` (the `bpy.ops` in front
part just specifies that this is an operator.)

But wait! By default, Blender duplicates the object and immediately
switches to the translate operator; how do we cancel that from within
code? It turns out that we don't have to, since we'll call the direct
Python function while Blender calls the modal function. This is a
complicated discussion for another time, but suffice it to say that
operations will not perform modal actions (such as mouse-guided
extrude, translate, rotate, etc.) when called from Python.

## Using the documentation

Visit
[the operators page](https://docs.blender.org/api/blender_python_api_current/bpy.ops.html)
of the documentation; the operators themselves are split into many
different categories. We're looking for the "Duplicate" operator,
which should be in the
["Object Operators" section.](https://docs.blender.org/api/blender_python_api_current/bpy.ops.object.html)

A quick search for "duplicate" leads us to
[`object.duplicate`](https://docs.blender.org/api/blender_python_api_current/bpy.ops.object.html#bpy.ops.object.duplicate),
which does exactly what we want to do!

But wait! If we used Blender to find the operator, we got
`object.duplicate_move`; what's with the `_move_` part? That's just a
shortcut to the `object.duplicate` operator with the `mode` set to
`TRANSLATION`; this is something that's trivial to do from Python, but
might get a little cumbersome if Blender needs to set the parameter
everywhere. For the purposes of this addon, `object.duplicate` and
`object.duplicate_move` are identical.

---

I'll use the `object.duplicate` operator here as it's simpler and
easier to understand than `object.duplicate_move`.

So now that we've determined that the "Duplicate Objects" operator is
called `object.duplicate`, we just need to call it.

{{< language "Python" "object_duplicate_translate.py" >}}

```py
# ...

class DuplicateAndTranslate(bpy.types.Operator):
    bl_idname = 'transform.duplicate_and_translate'
    bl_label = 'Duplicate and Translate'
    bl_description = 'Duplicate and translate selected object(s)'
 
    def execute(self, context):
 
        # Call Blender's "Duplicate Objects" operator.
        bpy.ops.object.duplicate()
        
        return {'FINISHED'}
# ...
```

And that's it! If you reload your addon, press `Space` to bring up the
searchbox, and search for "Duplicate and Translate," you'll see your
new operator in the list. When you press `Enter` to run the operator,
the `execute()` method is called and the object is duplicated! It's
hard to tell, though, since the duplicated object is in the exact same
location as the original. You can make sure it's a duplicate by
looking at the name or moving it (and confirming that the original is
still there.)

From here, it's easy to find out what the translate operator is
called: `transform.translate`. Easy-peasy! All we have to do is add it
to our `execute` function after `object.duplicate`. And we zip over to
Blender... and it doesn't do anything.

# Adding a `Property`

Operators perform actions, and Properties save data. Practically
everything in Blender is a `Property`; they store material colors, the
position of an object, the influence of a constraint, and virtually
everything else.

Properties all have a context; for example, a material color is tied
to the material. There are a
[few different types](https://docs.blender.org/api/blender_python_api_current/bpy.types.Property.html)
of `Property`, all used to store different kinds of value:

| Name | Purpose | Example
|:---|:---|:---
|[`BoolProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.BoolProperty.html)|A single boolean value; `True` or `False`.|`scene.render.use_overwrite`
|[`EnumProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.EnumProperty.html)|Contains multiple hardcoded options.|`scene.render.engine`
|[`FloatProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.FloatProperty.html)|A single floating-point property.|`scene.render.resolution_percentage`
|[`IntProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.IntProperty.html)|A single integer property.|`scene.render.resolution_x`
|[`StringProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.StringProperty.html)|A single string.|`scene.render.filepath`
|[`CollectionProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.CollectionProperty.html)|List of values.|`scene.objects`
|[`PointerProperty`](https://docs.blender.org/api/blender_python_api_current/bpy.types.PointerProperty.html)|A "dictionary" of other properties.|N/A

Properties don't exist in a vacuum, though. They need to be tied to
something; for example, the scene, an object, or a material.

# Registering and unregistering your addon

Addons can be enabled and disabled by the user at any time. This means
that every addon must be able to handle being registered (enabled) and
unregistered (disabled) at runtime. Blender does this with two global
functions, appropriately named `register` and `unregister`. They're
called when the user enables or disables your addon, respectively;
`register` is also called when Blender starts up and your addon is
enabled.

Within the `register()` and `unregister()` functions, you must tell
Blender exactly what to use (and remove) for your addon with the
`bpy.utils.register_class()` and `bpy.utils.unregister_class()`
functions, respectively.

{{< language "Python" "object_duplicate_translate.py" >}}

```py
# ...

class DuplicateAndTranslate(bpy.types.Operator):
    # ...

# ...

def register():
    bpy.utils.register_class(DuplicateAndTranslate)


def unregister():
    bpy.utils.unregister_class(DuplicateAndTranslate)

# ...
```

Alternatively, you can use `bpy.utils.register_module()` and
`bpy.utils.unregister_module()` to register and unregister your whole
module (i.e. everything within in that file.) I personally prefer to
use the `[...]_class()` functions, but using `[...]_module()` works
just as well and is far simpler, so that's what I've gone with here.

{{< language "Python" "object_duplicate_translate.py" >}}

```py
# ...

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

# ...
```

