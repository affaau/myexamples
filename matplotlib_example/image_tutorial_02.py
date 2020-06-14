'''Image Tutorial Color Scheme
ref: https://matplotlib.org/users/image_tutorial.html
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('stinkbug.png')

# Extract one channel
lum_img = img[:,:,0]

# Pseudocolor can be a useful tool for enhancing contrast and visualizing your
# data more easily. It applies to single-channel, grayscale, luminosity images.
plt.imshow(lum_img)  # default color - viridis
plt.show()

# Plenty of other options,
# ref: https://matplotlib.org/examples/color/colormaps_reference.html
# e.g.
plt.imshow(lum_img, cmap="hot")
plt.show()

# Alternative way to change colormap
imgplot = plt.imshow(lum_img)       # Render immediately in IPython,
imgplot.set_cmap('nipy_spectral')   # this line doesn't work
plt.colorbar()                      # show colorbar of cmap
plt.show()
