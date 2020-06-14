import numpy as np

D2 = np.array([ [1, 2, 3],
                [4, 5, 6] ])
print(D2.shape)  # (2, 3)
print(D2)
print(D2[1,2])   # 6

print()
D3 = np.array([ [[1,2,3,4], [2,3,4,5], [3,4,5,6]],
                [[4,5,6,7], [5,6,7,8], [6,7,8,9]] ])

print(D3.shape)   # (2, 3, 4)
print(D3)
print(D3[0,1,2])  # 4
