import os
import shutil
from distutils.dir_util import copy_tree

def getSubDirs(dir):
    return [os.path.join(dir,name) for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]

def changeFolder(modpack_dir, mods_dir):
    
    deleteFolder(mods_dir)
    copy_tree(modpack_dir, mods_dir)

def deleteFolder(folder):

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))