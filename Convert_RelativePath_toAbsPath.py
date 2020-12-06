def absolutePath(relativePath):
    '''
    input a relative path from THIS blend file to return 
    it as an absolute path. Note to use the raw string tag on Windows 
    i.e. absolutePath(r"mystring") to ensure the \ characters are 
    escaped properly
    '''
       
    import bpy
    from pathlib import Path

    directoryPath = bpy.path.abspath("//")
    
    # count parent directories above relative path
    parentDirs = relativePath.count("..\\")
    
    if parentDirs > 0:
    
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
        
    else: 
        fullPath = relativePath

    return fullPath
