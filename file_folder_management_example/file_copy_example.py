'''Copy Files
ref: https://automatetheboringstuff.com/chapter9/
'''
# standard library - shell utility
import shutil
import os

# copy a single file to destination folder
# !!destination folder must be available!!
response = shutil.copy('.\\text.txt', '.\\dummy')
print(response)
# .\dummy\text.txt

# copy to destination with new name
response = shutil.copy('.\\text.txt', '.\\dummy\copied.txt')
print(response)
# .\dummy\copied.txt

# copy entire folder, including subfolders and files within it 
# to "newly created" destination folder
# !!!cannot copy to EXISTING folder!!!
response = shutil.copytree('.\\dummy', '.\\backup')
print(response)
#.\backup