'''
Copyright (C) 2017 Loïc Dautry aka -L0Lock-

Created by Loïc Dautry aka -L0Lock-

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Quadrify",
    "description": "In Object Mode, converts selected object's triangles to quads.",
    "author": "Loïc Dautry aka -L0Lock-",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "View3D > Toolbar and View3D > Specials (W-key)",
    "warning": "This addon is still in developpement",
    "category": "Mesh"
    }

import bpy

class Quadrify_operator(bpy.types.Operator) :
    bl_idname = "object.quadrify"
    bl_label = "Quadrify Selected"
    bl_description = "Converts selected object's triangles to quads"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context) :
        
        # quadrify script
        
        for obj in context.selected_objects :
            context.scene.objects.active = obj
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.tris_convert_to_quads()
            bpy.ops.mesh.select_all()
            bpy.ops.mesh.tris_convert_to_quads()
            bpy.ops.object.editmode_toggle()
            
        return {'FINISHED'}


# Register to UI
def add_object_button(self, context):
    self.layout.operator (Quadrify_operator.bl_idname)

def register() :
    bpy.utils.register_class(Quadrify_operator)
    bpy.types.VIEW3D_MT_object_specials.append(add_object_button)

def unregister() :
    bpy.utils.register_class(Quadrify_operator)


if __name__ == "__main__":
    register()