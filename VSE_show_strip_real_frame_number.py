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

### Known Issues ###

- Deleting the selected scene strip throws up an error: The code needs
conditionals adding to to allow for this.

- Strips modified by the Speed Controller effect don't take the effect
into account: This is potentially something that could be added.

"""
import bpy
import os

class RealFrameNumberDisplay(bpy.types.Panel):
    bl_label = "Strip Frame Number"
    bl_idname = "VSE_Strip_realframe"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Strip'

    def draw(self, context):
        layout = self.layout
        
        # get the active scene
        scn = bpy.context.scene

        # get the scene frame number
        currentFrame = scn.frame_current

        # get the VSE active strip properties
        stripStart = scn.sequence_editor.active_strip.frame_start

        stripOffset = scn.sequence_editor.active_strip.frame_offset_start

        # calculate the number of frames between the play head and the start of the strip
        frameOfStrip = currentFrame - (stripStart + stripOffset)

        # get the strip's parent scene name
        stripScene = scn.sequence_editor.active_strip.scene.name

        # get the in point of the strip's parent scene
        realStripStart = bpy.data.scenes[str(stripScene)].frame_start

        # calculate the real frame number of the strip
        realFrameNum = realStripStart + stripOffset + frameOfStrip

        # Display scene frame number
        row = layout.row()
        row.label(text="Scene Frame: " + str(scn.frame_current), icon='SEQUENCE')
        
        # Display strip internal frame number
        row = layout.row()
        row.label(text="Strip Frame (internal): " + str(realFrameNum), icon='SEQUENCE')
        
        # Display selected strip frame number
        row = layout.row()
        row.label(text="Strip Frame (selected): " + str(frameOfStrip), icon='SEQUENCE')
             
    # Update output on scene frame change    
    bpy.app.handlers.frame_change_pre.append(draw)

def register():
    bpy.utils.register_class(RealFrameNumberDisplay)


def unregister():
    bpy.utils.unregister_class(RealFrameNumberDisplay)


if __name__ == "__main__":
    register()
