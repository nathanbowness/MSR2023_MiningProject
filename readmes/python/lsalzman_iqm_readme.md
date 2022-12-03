IQM Developer Kit 2021-06-13

*** Format information ***

"iqm.txt" contains a description of the Inter-Quake Model (IQM) format.
"iqe.txt" contains a description of the Inter-Quake Export (IQE) format.


*** Blender export ***

blender-*/iqm_export.py are exporter scripts for their respective versions of Blender, where the highest version script should work with the later versions of Blender. They can either directly export an IQM file (if the output filename has an ".iqm" suffix), or they can export an IQE file (if the output filename has an ".iqe" suffx) for use with the IQM compiler.

The "Meshes" toggle controls whether to export meshes in the IQM.
The "Skeleton" toggle controls whether to export joints and their associated blend weights in the IQM. This should only be disabled for models that are not animated and intended to be static.
The "Bounding boxes" toggle controls whether to generate per-frame bounding boxes for each animation frame. This only works if the IQM contains meshes. This option can take a while, so turning it off while doing test exports of a model and re-enabling it on the final export may be a good idea.
The "Vertex colors" toggle controls whether vertex colors will be exported. At least one mesh must have vertex colors defined to use this option. Starting with the Blender 2.59 exporter, if this vertex color layer is named "alpha" or any name starting with the word "alpha", the colors will be treated as grayscale and source for the alpha channel of the exported vertex colors. Any other vertex color layers with names other than "alpha" will be treated as the RGB channels of the exported vertex colors.
The "Animations" field contains a comma (",") separated list of action names to export. The names can also have parameters of the form "name:X:Y:Z:L", where X is the start frame number, Y is the end frame number, Z is the frames per second (floating-point), and L is 0 or 1 to indicate looping. Earlier parameters can be left empty as in "idle::::1" to specify only a later parameter, and later parameters can be omitted if unnecessary as in "run:1:25".
The "Materials" option controls how material names are generated. "material+image-ext" combines the name of the material and the name of the UV-map image (without its extension or directory) to generate the material name, "material" uses only the name of the material, and "image" just uses the name of the UV-map image (without its directory). 
The "De-rigify" toggle can be used to optimize certain skeletons generated by the rigify script to export only deformation bones.
The "Bone order" option specifies the name of an optional text file (relative to the export path) containing an ordering of bones for export, one bone name per line. 

*** IQM compiler ***

The IQM compiler can be used to compile MD5, SMD, IQE, FBX (7.x/ascii only), and OBJ files into IQM files.

It is run as follows:

./iqm [options] output.iqm mesh.iqe anim1.iqe ... animN.iqe

./iqm [options] output.iqm mesh.md5mesh anim1.md5anim ... animN.md5anim

./iqm [options] output.iqm mesh.smd anim1.smd ... animN.smd

./iqm [options] output.iqm mesh.fbx anim1.fbx ... animN.fbx

./iqm [options] output.iqm mesh.obj

For certain formats, IQE, OBJ, and FBX, it is possible to combine multiple mesh files of the exact same vertex layout and skeleton by supplying them as "mesh1.iqe,mesh2.iqe,mesh3.iqe", that is, a comma-separated list of the mesh files (with no spaces) in place of the usual mesh filename.

Options can be any of the following command-line switches:

-s N
--scale N
  Sets the output scale to N (float).

--meshtrans Z
--meshtrans X,Y,Z
  Translates a mesh by X,Y,Z (floats). This does not affect the skeleton.

-j
--forcejoints
  Forces the exporting of joint information in animation files without meshes.

Each animation file can be preceded by any combination of the following command-line switches:

--name A
  Sets the name of the animation to A. 
--fps N
  Sets the FPS of the animation to N (float).
--loop
  Sets the loop flag for the animation.
--start N
  Sets the first frame of the animation to N (integer).
--end N
  Sets the last frame of the animation to N (integer).

You can supply either a mesh file, animation files, or both.
Note that if an input mesh file is supplied, it must come before the animation files in the file list.
The output IQM file will contain the supplied mesh and any supplied animations.
If no mesh is provided, the IQM file will simply contain the supplied animations.

The included Makefile can be used to build the IQM compiler.


*** IQM upgrader ***

The IQM upgrader is a program to convert older versions of IQM files to the most recent version. Ideally you should regenerate the IQM files using the exporters or the compiler, but if necessary, the upgrader will try to generate a new version while manipulating as little of the data as possible.

It is run as follows:

./upgrade output.iqm input.iqm

The included Makefile can be used to build the IQM upgrader.


*** Code examples ***

Please see the included "demo" directory for examples of loading and using IQM models.

The "demo" program shows a simple rendering example using OpenGL fixed-function rendering and GLUT.
The "gpu-demo" program shows GPU-accelerated skinning using OpenGL GLSL rendering and GLUT.


*** LICENSE INFO ***

The IQM compiler and upgrader source code as well as the IQM blender exporters (blender-*/iqm_export.py) are licensed as specified by the LICENSE file included with this distribution.
