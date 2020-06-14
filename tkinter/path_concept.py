'''Concept of working path

- run this script from a different directory
- test by executing script using absolute or relative path
- lena.jpg in the same directory of script

https://stackoverflow.com/questions/7116889/is-module-file-attribute-absolute-or-relative
'''
import os
import sys

# Current working directory (cwd) is where you execute the python
# Absolute path
current_directory = os.getcwd()
print("Current working directory: {}".format(current_directory))

# The path\file of the script run
# 'Relative or Absolute' follows if script is called by relative or absolute path
print(__file__)
print("It is an absolute path: {}".format(os.path.isabs(__file__)))
print(os.path.abspath(__file__))  # Force to deliver full path

# The directory path of the script run
# 'Relative or Absolute' follows if script is called by relative or absolute path
# Relative from current_directory
path_of_localscript = os.path.dirname(__file__)
print("Path of script: {}".format(path_of_localscript))

# Check if 'lena.jpg' is available
# Relative from current_directory, NOT script directory
print("File location:", os.path.join(current_directory, "lena.jpg"))
print(os.path.isfile("lena.jpg"))
# It should be a FALSE

# Combine to give the path of image relative to script
localpath = os.path.join(path_of_localscript, "lena.jpg")
print("File location: ", localpath)

# Check if 'path\lena.jpg' is available
print(os.path.isfile(localpath))
# It should be a TRUE
