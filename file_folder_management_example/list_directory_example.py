import os

# list all FILES within the currect directory
# including DIRECTORIES!!
for filename in os.listdir():
    print(filename)
    
# list all .py files
for filename in os.listdir():
    if filename.endswith('.py'):
        print(filename)

# returns FULL PATH of current directory
local_path = os.getcwd()

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(os.path.join(local_path, filename))   
        
print('')

#
# list full tree of the directory, including its subfolders & files
#
# os.walk() returns list of fodlers and files information
for folderName, subfolders, filenames in os.walk('.\\'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
