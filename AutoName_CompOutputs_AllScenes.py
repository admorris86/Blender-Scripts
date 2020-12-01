"""
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

### About This Script ###

This script will automatically set the filepath of all output nodes
in the compositor (for all scenes) based on their label. The preset 
output path is:
    
//_Exports/[filename]/[scene name]/[node label]/[scene name]_[node label].exr

example:

//_Exports/MyBlendFile/Scene.001/Z-Depth/Scene.001_Shot.002_Z-Depth_0001.exr

"""

import bpy
import os

# Get file name:
filename = bpy.path.basename(bpy.context.blend_data.filepath)

# Remove .blend extension:
filename = os.path.splitext(filename)[0]

for i in range (len(bpy.data.scenes)):
    
    thisScene = bpy.data.scenes[i]
    
    if thisScene.node_tree == None:
        None
    
    else:

        for node in thisScene.node_tree.nodes:
            if node.type == 'OUTPUT_FILE':
                # Configure your desired output path here
                node.base_path = "//" + "_Exports" + "/" + filename + "/" + thisScene.name + "/" + node.label
                node.file_slots[0].path = "/" + thisScene.name + "_" + node.label + "_"
                node.name = node.label

		# Set output node file format options: optional 
                node.format.file_format = 'OPEN_EXR'
                node.format.color_mode = 'RGBA'
                node.format.color_depth = '16'

    # Set scene output file format options: optional
    thisScene.render.filepath = "//" + "_Exports" + "/" + filename + "/" + thisScene.name + "/"
    thisScene.render.image_settings.file_format = 'OPEN_EXR'
    thisScene.render.image_settings.color_mode = 'RGBA'
    thisScene.render.image_settings.color_depth = '16'
    thisScene.render.film_transparent = True

