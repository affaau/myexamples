'''
https://towardsdatascience.com/5-python-features-i-wish-i-had-known-earlier-bc16e4a13bf4
'''
from timeit import timeit

add_func = lambda z: z ** 2
is_odd = lambda z: z%2 == 1
multiply = lambda x,y: x*y

aList = list(range(10))
print(aList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


## map
print(list(map(add_func, aList)))
print([x ** 2 for x in aList])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## filter
print(list(filter(is_odd, aList)))
print([x for x in aList if x%2 == 1])
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9]


print(timeit('list(map(add_func, aList))', globals=globals(), number=10000))
# 0.0345206
print(timeit('[x ** 2 for x in aList]', globals=globals(), number=10000))
# 0.0309882

print(timeit('list(filter(is_odd, aList))', globals=globals(), number=10000))
# 0.0120342
print(timeit('[x for x in aList if x%2 == 1]', globals=globals(), number=10000))
# 0.0062472

## unpack into seperare elements
a, *b, c, d = aList
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# a = 0, b = [1, 2, 3, 4, 5, 6, 7], c = 8, d = 9


## zip
numList = [0, 1, 2]
engList = ['zero', 'one', 'two', 'three']  # three is neglected!
espList = ['cero', 'uno', 'dos']
print(list(zip(numList, engList, espList)))
# [(0, 'zero', 'cero'), (1, 'one', 'uno'), (2, 'two', 'dos')]

for num, eng, esp in zip(numList, engList, espList):
    print(f'{num} is {eng} in English and {esp} in Spanish.')
# 0 is zero in English and cero in Spanish.
# 1 is one in English and uno in Spanish.
# 2 is two in English and dos in Spanish.


## enumerate
upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']
for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):
    print(f'{i}: {upper} and {lower}.')
# 1: A and a.
# 2: B and b.
# 3: C and c.
# 4: D and d.
# 5: E and e.
# 6: F and f.


## generator
def gen(n):    # an infinite sequence generator that generates integers >= n
    while True:
        yield n
        n += 1
        
G = gen(3)     # starts at 3
print(next(G)) # 3
print(next(G)) # 4
print(next(G)) # 5
print(next(G)) # 6

