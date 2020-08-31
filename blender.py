import bpy
import os
import sys
import bmesh
from mathutils import Vector
from bmesh.types import BMVert

# Usage
# /Applications/Blender.app/Contents/MacOS/Blender -b --python /PATH/blender.py -- /PATH_TO/svg/ /PATH_TO/models/

argv = sys.argv
argv = argv[argv.index("--") + 1:] 

svgfiles=argv[0]
modelfiles=argv[1]

dir = os.listdir(svgfiles)

for file in dir:
    if file.endswith('.svg'):
        context = bpy.context
        scene = context.scene

        for c in scene.collection.children:
            scene.collection.children.unlink(c)
        bpy.ops.object.select_all()
        bpy.ops.object.delete()

        print(svgfiles + file)

        bpy.ops.import_curve.svg(filepath=svgfiles + file)

        curves = []
        for ob in bpy.data.objects:
            if "Curve" in ob.name:
                curves.append(ob)
        curves.sort(key=lambda curve: curve.name, reverse=False)
        symbol = curves[-1]

        bpy.ops.object.select_all()
        symbol.select_set(False)
        bpy.ops.object.delete()
        symbol.select_set(True)

        m = symbol.modifiers.new("Solidify", type='SOLIDIFY')
        m.use_even_offset = True
        m.thickness = 0.001

        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        symbol.location = (0.0, 0.0, 0.0)

        bpy.ops.export_scene.obj(filepath=modelfiles + file.replace('.svg', '.obj'), use_materials=False)
