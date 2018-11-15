import bpy

for b in bpy.context.selected_pose_bones:
    for c in b.constraints: 
        if c.name == "Stretch To":
            c.rest_length = 0