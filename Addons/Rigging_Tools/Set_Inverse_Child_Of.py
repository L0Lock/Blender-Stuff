import bpy

ob = bpy.context.active_object

# Take a copy of current layers 
org_layers = ob.data.layers[:]

# Show all layers
for i in range(len(org_layers)):
    ob.data.layers[i] = True

for b in ob.pose.bones:
    for c in b.constraints: 
        if c.type == "CHILD_OF":
            context_py = bpy.context.copy()
            context_py["constraint"] = c
            ob.data.bones.active = b.bone
            bpy.ops.constraint.childof_set_inverse(context_py, constraint="Child Of", owner='BONE')
            
# Reset back to orginal layer state    
for i in range(len(org_layers)):
    ob.data.layers[i] = org_layers[i]