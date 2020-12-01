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
This script will convert any relative path in Blender (on a Windows
system) to and absolute path. Modify and run it in the console to return
the output.

'''
import bpy
from pathlib import Path

directoryPath = bpy.path.abspath("//")

relativePath = r"" # insert relative path here, keep the r!

# count parent directories above relative path
parentDirs = relativePath.count("..\\")

# assign this blend file's full directory path to a new variable
# named parentPath
parentPath = Path(directoryPath)

# for the number of parent directories above this blend,
# re-assign the value of parentPath to the path of the
# directory above i.e step up x levels
for k in range(parentDirs):
    parentPath = parentPath.parent

# trim relative path from the first char after the relative path symbols
# i.e keep anything after this stuff //..\..\
i = 0
for char in relativePath:
    if char in ['\\', '/', '.']:
        i += 1
    else:
        relativePath = "\\" + relativePath[i:]
        # combined parentPath and trimmed relative path for the full path
        fullPath = str(parentPath) + relativePath
        break

print(fullPath)
