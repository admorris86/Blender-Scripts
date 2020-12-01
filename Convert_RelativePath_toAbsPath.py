import bpy
from pathlib import Path

directoryPath = bpy.path.abspath("//")

relativePath = r"" # insert relative path here, keep the r

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
