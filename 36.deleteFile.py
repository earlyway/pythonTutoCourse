import os
import shutil

path = "emptyfolder"


try:
    #os.remove(path)    #delete a file
    #os.rmdir(path)     #delte an empty directory
    shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You can't delete that using that function")
else:
    print(path+" was deleted")