import numpy as np
#from matplotlib.pyplot import imshow, show, colorbar
import matplotlib.pyplot as plt

image = np.random.rand(4,4)
print(image)
plt.imshow(image)
plt.colorbar()
plt.show()