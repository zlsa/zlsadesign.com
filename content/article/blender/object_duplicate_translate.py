
###
# Duplicate and Translate
###

# This addon is very simple. It duplicates every selected object, then
# translates them.
#
# This addon was created as an example addon for a tutorial.
#
# For more information, see:
# https://zlsadesign.com/article/blender/building-a-simple-blender-addon/
#
# -----
#
# This file is released into the public domain or CC0, whichever you prefer.
#
# https://creativecommons.org/publicdomain/zero/1.0/

import bpy

bl_info = {
    'name': 'Duplicate and Translate',
    'description': 'Duplicates and translates selected object(s)',
    'author': 'ZLSA Design',
    'version': (0, 1, 0),
    'blender': (2, 80, 0),
    'location': 'View3D > Object > Transform > Duplicate and Translate',
    'support': 'COMMUNITY',
    'category': '3D View',
    'wiki_url': 'https://zlsadesign.com/article/blender/building-a-simple-blender-addon/',
}

# Here's where we define the operator class itself. It extends from
# `bpy.types.Operator`, and overrides some important variables.
class DuplicateAndTranslate(bpy.types.Operator):

    # The name of this operator within Blender. In our case, we can
    # call `bpy.ops.transform.duplicate_and_translate()` to execute
    # this operator.
    bl_idname = 'transform.duplicate_and_translate'

    # The user-friendly name for this operator. This is shown in
    # buttons, menus, and in the Operator Search popup.
    bl_label = 'Duplicate and Translate'

    # The user-friendly description for what this operator does. This
    # is shown in tooltips.
    bl_description = 'Duplicate and translate selected object(s)'
    
    bl_options = {'REGISTER', 'UNDO'}

    transform_vertical_distance: bpy.props.FloatProperty(
        name='Vertical Distance',
        description='Move duplicated objects up by this amount.',
        default=3
    )
    
    # Here, we have a poll function. Blender calls this function, and
    # if it returns `True`, it will allow this operator to be
    # executed. If the poll function returns `False`, Blender won't
    # let anybody run this operator.

    # Since this operator only works in Object mode (and needs
    # something to duplicate and translate), we return `True` only if
    # both conditions are met.
    @classmethod
    def poll(cls, context):
        '''Returns `True` only if Blender is in Object mode, and there is more than one object selected.'''
        return context.mode == 'OBJECT' and len(context.selected_objects)

    # This function performs the actual work.
    def execute(self, context):
        '''Runs the operator itself. Duplicates all objects, then transforms them.'''
        
        # Call Blender's "Duplicate Objects" operator.
        bpy.ops.object.duplicate()

        # Now, create a transform vector, using the distance requested by the user.
        transform_vector = [0, 0, self.transform_vertical_distance]
        
        # And then transform the objects. (The `duplicate` operator
        # automatically selects the newly duplicated objects, so we
        # don't need to do anything special to select them.)
        bpy.ops.transform.translate(value=transform_vector)

        # Yay, we're done here!
        return {'FINISHED'}

    
def register():
    bpy.utils.register_class(DuplicateAndTranslate)


def unregister():
    bpy.utils.unregister_class(DuplicateAndTranslate)
