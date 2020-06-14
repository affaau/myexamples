from timeit import timeit
from pprint import pprint

N = 4  # number of binary digit
binary_format_lst = ['{:04b}'.format(e) for e in range(2**4)]
pprint(binary_format_lst, width=2)

scores=[54,67,48,99,27]

# more pythonic & neater
def enu_way():
    l =[]
    for i, score in enumerate(scores):
        l.append((i, score))
   
def standard():
    l=[]
    for i in range(len(scores)):
       l.append((i, scores[i]))
       


## result almost the same, enumurate slightly faster
print(timeit('enu_way()', globals=globals(), number=10000))
print(timeit('standard()', globals=globals(), number=10000))
