'''Image Tutorial Basics
ref: https://matplotlib.org/users/image_tutorial.html
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

print(matplotlib.get_backend())
# To show what kind of backend is used

# Matplotlib natively only supports PNG
# If fails, support falls on pillow library
img = mpimg.imread('stinkbug.png')
print(img.shape)
# height (y), width (x), channels = (375, 500, 3)

print(img[0:5, 0:3, 0])
# [[0.40784314 0.40784314 0.40784314]
#  [0.4117647  0.4117647  0.4117647 ]
#  [0.41960785 0.41568628 0.41568628]
#  [0.42352942 0.42352942 0.42352942]
#  [0.41960785 0.41960785 0.42352942]]
# Matplotlib rescaled 8-bit data from [0, 255] to [0.0, 1.0]
#   - uint8 for other image formats
# However, pillow only render uint8 data

print(type(img), img.dtype)
# <class 'numpy.ndarray'> float32

# plot (render) any kind of numpy array
imgplot = plt.imshow(img)

# No need for this line if within Ipython
plt.show()
