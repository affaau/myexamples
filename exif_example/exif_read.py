#! /usr/bin/python3
'''
Get and display exif data of image

<script>
execute by command line:
  $> py exif_read.py

  python3 will be selected automatically
'''
from PIL import Image
from PIL.ExifTags import TAGS
import sys
 
def get_exif(fn):
    '''
    Get exif data within image file
    '''
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def print_keys(exif):
    '''
    Print properties (keys) of all exif data pairs
    '''
    print(data.keys())
    print()
    max = 0
    key = ""
    for item in data:
        l = len(str(data[item]))
        print(l)
        if l > max:
            key = item
            max = l
    print("\nLargest data pair is [%s] : %s bytes\n"%(key, max))

def print_exif(exif):
    '''
    Print all data pairs in exif, except
    ["MakerNote"] which consists of a lot of (unknown) hex data
    '''
    for item in exif:
        
        if item != "MakerNote":
            print("%s : %s"%(item, exif[item]))
    
if __name__ == "__main__":
    #fn = raw_input("Enter file name: ")  # python2
    fn = input("Enter file name: ")      # python3
    try:
        if len(fn) < 1:
            data = get_exif("photo.jpg")
        else:
            data = get_exif(fn)
    except:
        print("Error: File not available!")
        sys.exit(0)
    #print_keys(data)   # not necessary
    print_exif(data)
