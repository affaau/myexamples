import cv2
import numpy as np

img = cv2.imread("widow-grayscale-320x480.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.jpg', gray)
r, c = gray.shape
print(gray.shape)
print('total size: ', gray.size)
gray_flat = gray.flatten()

hist = gray_flat.copy()
ttl_size = hist.size
hist.sort()
top_percentage = 0.1       # precentage of highest values to keep
cut_off = hist[int(ttl_size*(1-top_percentage))]  
print('k_sparse: ', int(ttl_size*top_percentage))
print('cut-off value: ', cut_off)

for i in range(ttl_size):
    if gray_flat[i] <= cut_off:
        gray_flat[i] = 0

compressed = gray_flat.reshape((r,c))

cv2.imshow('Gray', gray)
cv2.imshow('Lossy', compressed)

cv2.imwrite('lossy.jpg', compressed)

cv2.waitKey(0)          # Press ESC to exit
cv2.destroyAllWindows()
