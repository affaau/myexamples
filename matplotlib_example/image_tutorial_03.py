'''Image Tutorial Histogram & range
ref: https://matplotlib.org/users/image_tutorial.html
'''
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('stinkbug.png')
lum_img = img[:,:,0]

plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.show()

plt.subplot(1,2,1)
# to the cmap maps between (0.0, 0.7), discard the rest
imgplot = plt.imshow(lum_img)
plt.title('BEFORE')
plt.colorbar(orientation='horizontal')

plt.subplot(1,2,2)
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))
plt.title('AFTER')
plt.colorbar(orientation='horizontal')

plt.show()
