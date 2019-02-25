# standard libraries
import zipfile
import send2trash
import os

# reading zip file
example_zip = zipfile.ZipFile('sample.zip')
content_list = example_zip.namelist()
print(content_list)
#['cars.jpg', 'color_tracking.py']

file_info = example_zip.getinfo(content_list[1])

print(file_info.file_size)
#814

print(file_info.compress_size)
#432

# # extract single file
# #    returns full path of extracted file
# example_zip.extract(content_list[0])
# #'D:\\Workspace\\Anaconda\\python3x\\Examples\\file_folder_management_example\\cars.jpg'

# # extract single file to an existed folder
# #    returns path of extracted file
# example_zip.extract(content_list[0], '.\\dummy'))
# #'dummy\\cars.jpg'

# # extract ALL files to current folder
# example_zip.extractall()

# # extract ALL files to an existed folder
# folder = '.\\dummy'
# example_zip.extractall(folder)

# example_zip.close()

# to clean up extracted files after test
def cleanup(path, list):
    print("deleting...")
    for file in list:
        file_path = os.path.join(path, file)
        print("\t{}".format(file_path))
        send2trash.send2trash(file_path)
    print("cleanup completed\n")    

#cleanup(folder, content_list)
 
 
# creat & add to zip file
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('text.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close() 
