
# importing the shutil module
import shutil
 
# importing the os module
import os
 
# defining the function to ignore the files
# if present in any folder
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
 
# calling the shutil.copytree() method and
# passing the src,dst,and ignore parameter
shutil.copytree('D:\Python_Program\Project\Structure_1','D:\Python_Program\Project\Copied_Structure',ignore=ignore_files)