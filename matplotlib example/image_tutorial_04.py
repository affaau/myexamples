'''Image Tutorial PIL & Resize
ref: https://matplotlib.org/users/image_tutorial.html
'''
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('stinkbug.png')
img.thumbnail((64,64), Image.ANTIALIAS)  # resize image in-place
imgplot = plt.imshow(img)                # default interpolation - bilinear
plt.show()

imgplot = plt.imshow(img, interpolation='nearest')
plt.show()

imgplot = plt.imshow(img, interpolation='bicubic')
plt.show()
