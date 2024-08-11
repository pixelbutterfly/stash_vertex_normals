![stash_vertex_normals](https://github.com/user-attachments/assets/8c7680ac-e742-43ac-8430-195dfe9f291b)

#What is this?

Stash Normals is a Blender addon for saving and restoring the vertex normals on a mesh. I wrote it to compensate
for Blender's lack of a "lock normals" option similar to Maya's. Lock normals stops the vertex normals from updating while the mesh is edited. Stash Normals doesn't do this, but rather provides a workaround by storing the normals as a color attribute and copying that data back to the normals at a later time.
![image](https://github.com/user-attachments/assets/8914c78f-b089-4f88-899e-df75f3a17c95)


#Why do you need this?

Usually Blender's default behavior of constantly updating the normals is exactly what you want. However, there are some practical uses for normal hacking.

Trim sheets. Trim sheets are textures that tile in one direction. Because of how they're made, trim sheets work best on geo that has flat faces and 90 degree corners with hard edges. However, a common game art trick is to lock the normals and do a wonkify pass on the geo adding tapers, flares, popped edges, and generally creating a more interesting and varied silhouette to make the tiling texture less obvious. Stash Normals allows you to recreate this workflow in Blender.![image](https://github.com/user-attachments/assets/2f1ddabe-b750-40e0-8a1f-2a781fe08877)

https://github.com/user-attachments/assets/940015f1-41bf-4c7d-b4d7-2697afc6770c

It can also be used to punch up your models that use tiling textures. Let's say you have a wall with a tiling brick texture applied. It would be great if you could pop out some of those bricks on the corners to improve the silhouette of the wall, but you don't really want the extra mesh normals to be added on top of your baked normals map. Stash Normals allows you to store the normals, model in some bricks, and restore the normals so the original shading is preserved.![image](https://github.com/user-attachments/assets/3272e603-9952-4d36-8b37-cff44e867949)

https://github.com/user-attachments/assets/959cd617-fb7b-4564-aebb-1cfedc5fa296

It's also generally useful for editing the geo on a model with a baked normal map. If rebaking is not an option (maybe you don't have access to the highpoly), the edited model should have normals that match the original normals as closely as possible. Sometimes it's possible to transfer the normals from the original mesh to the edited mesh with a transfer attributes modifier, but Stash Normals requires less setup and works even when the edited model has a very different shape from the original. ![image](https://github.com/user-attachments/assets/45e6c975-8e96-42e8-b2eb-6847a5bce1da)

https://github.com/user-attachments/assets/abe25f61-f055-417a-8c78-cb77e27df565

It can also work from preserving normals on models that have been split up into pieces.
A common example is a character model where the head needs to be separated from the body for customization. You can stash the normals, separate the pieces, and restore the normals to get the original shading back.![image](https://github.com/user-attachments/assets/fc190b4f-e88e-444c-bc74-b6495f78a7b2)


https://github.com/user-attachments/assets/c77546de-efea-48bf-af4a-ae158bb30104


Note: After you stash normals, be careful with of how you edit your mesh.  Operations that would result in a split in the UVs will also create a hard split in the vertex colors that will result a sharp edge when converted back to normals.  For this reason, you should merge verts with "mergeUVs" enabled. If you're planning on doing a lot of editing between stashing your normals and restoring them, working with the stored normal attribute visualized as color is recommended.

Special thanks to Philipp Seifried who's convert normals to vertex color was an inspiration for this tool.![image](https://github.com/user-attachments/assets/c619658a-b0ae-4194-a242-5b7b7f73887f)

##Installation
##(3.0 to 4.1)
	• Get the latest vertexColorStylizer.py release in:  https://github.com/pixelbutterfly/stash_vertex_normals/releases
	• start Blender and open the user preferences
	• switch to the Add-ons tab and click the Install Add-on from file... button at the bottom
	• locate the downloaded stashVertexNormals.py file and double-click it
	• search for the addon "Stash Vertex Normals"
	• activate the addon by ticking the checkbox
	
 ##(4.2+)
	• Get the latest vertexColorStylizer.py release in:  https://github.com/pixelbutterfly/stash_vertex_normals/releases
	• start Blender and open the user preferences
	• switch to the Add-ons tab and click the arrow in the upper right. Choose "install from disk…"
locate the downloaded stashVertexNormals.py file and double-click it![image](https://github.com/user-attachments/assets/d9adad51-980f-432f-a218-9881c323d610)


