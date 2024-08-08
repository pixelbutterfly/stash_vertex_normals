![stash_vertex_normals](https://github.com/user-attachments/assets/8c7680ac-e742-43ac-8430-195dfe9f291b)

What is this?
Stash Normals is a blender addon for saving and restoring the vertex normals on a mesh. I wrote it to compensate
for Blender's lack of a "lock normals" option similar to Maya's. Lock normals stops the vertex normals from updating while the mesh is edited. Stash Normals provides a workaround by storing the normals as a color attribute, then copying that data back to the normals at a later time.

Why do you need this?
Usually Blender's default behavior of constantly updating the normals is exactly what you want. However, there are some practical uses for normal hacking.

Trim sheets. Trim sheets are normal maps that tile in one direction. Because of how they're made, trim sheets work best on geo that has flat faces and 90 degree corners with hard edges.  However, a common game art trick is to lock the normals and do a wonkify pass on the geo adding tapers, flares, popped edges, and generally creating a more interesting and varied silhouette. Stash Normals allows you to recreate this workflow.

https://github.com/user-attachments/assets/940015f1-41bf-4c7d-b4d7-2697afc6770c

This is not just limited to trims. It can be used to  punch up your models that use tiling textures. Let's say you have a wall like this that had a brick tiling texture applied. It would be great if you could pop out some of those bricks on the silhouette but you don't really want the vert normals to be added on top of the baked normals map. What you can do is stash the normals, cut in some edges on the normals, and restore the normals.

https://github.com/user-attachments/assets/959cd617-fb7b-4564-aebb-1cfedc5fa296

It's also generally useful for editing the geo on a model with a baked normal map. If rebaking is not an option (maybe you don't have access to the highpoly), the edited model should have normals that match the original as closely as possible. Sometimes it's possible to transfer the normals from the original mesh to the edited mesh with a transfer attributes modifier, but this works best when the edited model has a shape close to the original (not to mention faster to set up than a transfer attribute).

https://github.com/user-attachments/assets/abe25f61-f055-417a-8c78-cb77e27df565

Another example is restoring normals on split models.
Say you have a character with a baked normal map that needs to be split up into separate pieces (ie, separating the head from the neck). You can stash the normals, separate the pieces, and restore the normals to restore the seamless shading across the pieces.

https://github.com/user-attachments/assets/c77546de-efea-48bf-af4a-ae158bb30104


Note: after you stash normals, be careful with of how you edit your mesh.  Operations that would result in a split in the UVs, will also create a hard split in the vertex colors that will result a sharp edge when you restore the normals.  For this reason you should merge verts with "mergeUVs" enabled.

If you're planning on doing a lot of editing between stashing your normals and restoring them, working with the stored normal attribute visualized as color is recommended.



