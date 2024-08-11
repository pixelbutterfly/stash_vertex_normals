![stash_vertex_normals](https://github.com/user-attachments/assets/f6db1f99-f763-4eb8-9136-ae6239ddc823)

# What is this?

Stash Normals is a Blender addon for saving and restoring the vertex normals on a mesh. I wrote it to compensate
for Blender's lack of a "lock normals" option similar to Maya's. Lock normals stops the vertex normals from updating while the mesh is edited. Stash Normals doesn't do this, but rather provides a workaround by storing the normals as a color attribute and copying that data back to the normals at a later time.


# Why do you need this?

Usually Blender's default behavior of constantly updating the normals is exactly what you want. However, there are some practical uses for normal hacking.

Trim sheets are textures that tile in one direction, often used in games for building architecture. Because of how they're made, trim sheets work best on geo that has flat faces and 90 degree corners with hard edges. However, a common game art trick is to lock the normals and do a wonkify pass on the geo adding tapers, flares, popped edges, and generally creating a more interesting and varied silhouette to make the tiling texture less obvious. Stash Vertex Normals allows you to recreate this workflow in Blender.

https://github.com/user-attachments/assets/940015f1-41bf-4c7d-b4d7-2697afc6770c

It can also be used to punch up your models that use tiling textures. Let's say you have a wall with a tiling brick texture applied. It would be great if you could pop out some of the bricks on the corners to improve the silhouette, but you don't really want the extra vert normals to be added on top of your normals map. Stash Normals allows you to store the normals, model in some bricks, and retrieve the normals so the original shading is preserved.

https://github.com/user-attachments/assets/959cd617-fb7b-4564-aebb-1cfedc5fa296

It's also generally useful for editing the geo on a model with a baked normal map. If rebaking is not an option (maybe you don't have access to the highpoly), the edited model should have normals that match the original normals as closely as possible. Sometimes it's possible to transfer the normals from the original mesh to the edited mesh with a transfer attributes modifier, but Stash Vertex Normals requires less setup and works even when the edited model has a very different shape from the original.

https://github.com/user-attachments/assets/abe25f61-f055-417a-8c78-cb77e27df565

It can also work for preserving normals on models that have been split up into pieces.
A common example is a character model where the head needs to be separated from the body for customization. You can stash the normals, separate the pieces, and retrieve the normals to get the original shading back.

https://github.com/user-attachments/assets/d63229b3-d3f2-4b64-912c-ad74ca03745a

## Warning
After you stash normals, be careful with of how you edit your mesh.  Operations that would result in a split in the UVs will also create a hard split in the vertex colors that will result a sharp edge when converted back to normals. For this reason, you should merge verts with "mergeUVs" enabled. If you're planning on doing a lot of editing between stashing your normals and restoring them, working with the stored normal attribute visualized as color is suggested.

## Special Thanks
Thank you to Philipp Seifried whose [convert normals to vertex color](https://github.com/Philipp-Seifried/Blender-Normals-To-Vertex-Color) addon was an inspiration for this tool.






