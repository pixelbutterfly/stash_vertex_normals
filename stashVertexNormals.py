
bl_info = {
    # required
    'name': 'Stash Vertex Normals',
    'blender': (3, 6, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 0),
    'author': 'pixelbutterfly.com',
    'description': 'Save your normals and restore them later.',
    'doc_url': '',
}

import bpy
from mathutils import Vector

# == GLOBAL VARIABLES
PROPS = [
    ('stashed_normals_name', bpy.props.StringProperty(name='stashed normals name', default='stashedNormals')),
]
# == OPERATORS
class StashVertexNormals(bpy.types.Operator):
    
    bl_idname = 'opr.stash_vertex_normals'
    bl_label = 'Stash Vertex Normals'
    bl_options = {'REGISTER', "UNDO"}
    
    @classmethod
    def description(cls, context, properties):
        return "Stash Vertex Normals"
    
    def execute(self, context):
        
        stashedNormals = context.scene.stashed_normals_name
        
        for object in bpy.context.selected_objects:
        
            #create a var to store if object is in edit mode
            edit_mode = False;
            #test to see if we're in edit mode
            if context.mode == 'EDIT_MESH':
                    bpy.ops.object.mode_set(mode='OBJECT')
                    edit_mode = True;
                    
            current_obj = bpy.context.active_object 
            mesh = current_obj.data
            
            #check if attribute already exists
            if mesh.attributes.get(stashedNormals) is None:
                mesh.attributes.new(name=stashedNormals, type='BYTE_COLOR', domain='CORNER')
            elif mesh.attributes[stashedNormals].domain != 'CORNER':
                mesh.attributes.remove(mesh.attributes[stashedNormals])
                mesh.attributes.new(name=stashedNormals, type='BYTE_COLOR', domain='CORNER')
            elif mesh.attributes[stashedNormals].data_type != 'BYTE_COLOR':
                mesh.attributes.remove(mesh.attributes[stashedNormals])
                mesh.attributes.new(name=stashedNormals, type='BYTE_COLOR', domain='CORNER')
            
            #make an array to store the normals in
            split_normals = []
            
            for poly in mesh.polygons:
                    for loop_index in poly.loop_indices:
                        normal = mesh.loops[loop_index].normal.copy()
                        normal.normalize()
                        color = (normal * 0.5) + Vector((0.5,) * 3)
                        color.resize_4d()
                        mesh.attributes[stashedNormals].data[loop_index].color = color
                
            #return to edit mode if you were in it before
            if edit_mode == True:
                bpy.ops.object.mode_set(mode='EDIT')
                
        return {'FINISHED'}
        
 # == OPERATORS
class RetrieveVertexNormals(bpy.types.Operator):
    
    bl_idname = 'opr.retrieve_vertex_normals'
    bl_label = 'Restore Vertex Normals'
    bl_options = {'REGISTER', "UNDO"}
    
    @classmethod
    def description(cls, context, properties):
        return "Retrieve Vertex Normals"
    
    def execute(self, context):
        stashedNormals = context.scene.stashed_normals_name
        for object in bpy.context.selected_objects:
        
            #create a var to store if object is in edit mode
            edit_mode = False;
            #test to see if we're in edit mode
            if context.mode == 'EDIT_MESH':
                    bpy.ops.object.mode_set(mode='OBJECT')
                    edit_mode = True;
                    
            mesh = object.data
            
            #check if attribute already exists
            if mesh.attributes.get(stashedNormals) is None:
                self.report({"ERROR"}, stashedNormals +" were not stored on "+object.name+"!")
            elif mesh.attributes[stashedNormals].domain != 'CORNER':
                self.report({"ERROR"}, "Stored attribute is not the domin! Expects a corner attribute.")
            elif mesh.attributes[stashedNormals].data_type != 'BYTE_COLOR':
                self.report({"ERROR"}, "Stored attribute is not the right type! Expects a byte color.")
            else:
                normals = []
                for poly in mesh.polygons:
                        for loop_index in poly.loop_indices:
                            color =  mesh.attributes[stashedNormals].data[loop_index].color
                            myVector = Vector([color[0],color[1],color[2]])
                            myVector = (myVector * 2) - Vector((1,) * 3)
                            myVector.normalize()
                            normals.append(myVector)
                mesh.normals_split_custom_set(normals)
                
            #return to edit mode if you were in it before
            if edit_mode == True:
                bpy.ops.object.mode_set(mode='EDIT')
                
        return {'FINISHED'}
 
class DeleteStoredNormals(bpy.types.Operator):
    
    bl_idname = 'opr.delete_stored_normals'
    bl_label = 'Delete Stored Normals'
    bl_options = {'REGISTER', "UNDO"}
    
    @classmethod
    def description(cls, context, properties):
        return "Delete Stored Normals"
    
    def execute(self, context):
        stashedNormals = context.scene.stashed_normals_name
        for object in bpy.context.selected_objects:
            bpy.context.view_layer.objects.active = object
            mesh = object.data
            
            #check if attribute already exists
            if mesh.attributes.get(stashedNormals) is None:
                self.report({"ERROR"}, stashedNormals + " were not found on "+object.name+"!")
            else:
                mesh.attributes.remove(mesh.attributes[stashedNormals])
            
        return {'FINISHED'} 

# == PANELS
class StashVertexNormalsPanel(bpy.types.Panel):
    
    bl_idname = 'VIEW3D_PT_stash_vertex_normals'
    bl_label = 'Stash Vertex Normals'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Stash Vertex Normals"

    def draw(self, context):
        layout = self.layout
        scene = context.scene      
        vis_box = layout.box()
        
        vis_box.operator('opr.stash_vertex_normals', text='Stash Vertex Normals')
        vis_box.operator('opr.retrieve_vertex_normals', text='Retrieve Vertex Normals')
        vis_box.operator('opr.delete_stored_normals', text='Delete Stored Normals')
        vis_box.prop(context.scene, 'stashed_normals_name')
        ## dislay the user input properties

        layout.label(text='Pixelbutterfly Tools')

class PanelPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    # Addon Preferences https://docs.blender.org/api/blender_python_api_2_67_release/bpy.types.AddonPreferences.html

    def draw(self, context):
        layout = self.layout

        box = layout.box()

        box.label(text="Additional Links")
        col = box.column(align=True)
        col.operator("wm.url_open", text="Developer Website", icon='WORDWRAP_ON').url = "https://www.pixelbutterfly.com"
        
def register():

    bpy.utils.register_class(StashVertexNormals)
    bpy.utils.register_class(RetrieveVertexNormals)
    bpy.utils.register_class(DeleteStoredNormals)
    bpy.utils.register_class(StashVertexNormalsPanel)
    bpy.utils.register_class(PanelPreferences)
    
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)
        
def unregister():

    bpy.utils.unregister_class(StashVertexNormals)
    bpy.utils.unregister_class(RetrieveVertexNormals)
    bpy.utils.unregister_class(DeleteStoredNormals)
    bpy.utils.unregister_class(StashVertexNormalsPanel)
    bpy.utils.unregister_class(PanelPreferences)
    
    for (prop_name, _) in PROPS:
        delattr(bpy.types.Scene, prop_name)
        
if __name__ == '__main__':
    register()
