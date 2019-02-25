import os
import shutil
# another standard package
# - using send2trash is much safer than Python’s regular delete functions,
#   because it will send folders and files to your computer’s trash or
#   recycle bin instead of permanently deleting them
import send2trash

'''
    Calling os.unlink(path) will delete the file at path.

    Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.

    Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

'''

# example
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.') # return number of words written
baconFile.close()
send2trash.send2trash('bacon.txt')
# check trash!