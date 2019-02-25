import shutil

# move file from source to destination folder
# destination folder must already exist!!
#   othersise, FileNotFoundError
#
# if 'text.txt' already exists in destination folder,
# it will be over-written!!!
response = shutil.move('.\\text.txt', '..\\')
print(response)
#..\text.txt

response = shutil.move('..\\text.txt', '.\\')
print(response)
#.\text.txt

# move and rename!!
response = shutil.move('.\\text.txt', '..\\new_name.txt')
print(response)
#..\new_name.txt

response = shutil.move('..\\new_name.txt', '.\\text.txt')
print(response)
#.\text.txt
