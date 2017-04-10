
# Demonstration addon; see https://zlsadesign.com/article/blender/building-a-simple-blender-addon/

import bpy

bl_info = {
    'name': 'Duplicate and Translate',
    'description': 'Duplicates and translates selected object(s)',
    'author': 'Jon Ross',
    'version': (0, 1, 0),
    'blender': (2, 78, 0),
    'location': 'View3D > Object > Transform > Duplicate and Transform',
    'support': 'TESTING',
    'category': '3D View',
    'wiki_url': 'https://zlsadesign.com/article/blender/building-a-simple-blender-addon/',
}
    
class DuplicateAndTranslate(bpy.types.Operator):
    bl_idname = 'transform.duplicate_and_translate'
    bl_label = 'Duplicate and Translate'
    bl_description = 'Duplicate and translate selected object(s)'
 
    def execute(self, context):
 
        # Call Blender's "Duplicate Objects" operator.
        bpy.ops.object.duplicate()
        bpy.ops.transform.translate(value=[0, 0, 3])
        
        return {'FINISHED'}

    
def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

