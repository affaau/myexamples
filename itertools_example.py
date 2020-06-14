'''https://docs.python.org/3/library/itertools.html'''
from itertools import combinations


names = 'ABC'

for combination in combinations(names, 2):
    print(combination)

# ('A', 'B')
# ('A', 'C')
# ('B', 'C')
