'''Common collections tool to use'''
from collections import namedtuple, deque, Counter, OrderedDict
import math


# namedtuple is an easy way to represent a small
# simple class with no methods
Dot = namedtuple('Dot', 'x y')
p1, p2 = Dot(0, 0), Dot(3, 4)

print(p1, p2)
# Dot(x=0, y=3), Dot(x=0, y=4)


def distance(p1, p2):
    x_distance = math.pow(p1.x - p2.x, 2)
    y_distance = math.pow(p1.y - p2.y, 2)
    return math.sqrt(x_distance + y_distance)


print(distance(p1, p2))
# 5.0

# lists are great for LIFO (last in first out) but really bad
# for FIFO (first in first out)
# deque comes in handy, you can pop and insert from both sides in O(1)

# creating a deque
improved_list = deque([1, 2, 3, 4])
print(improved_list)
# deque([1, 2, 3, 4])

# inserting at O(1)
improved_list.appendleft(0)  # append() adds to right
print(improved_list)
# deque([0, 1, 2, 3, 4])

# poping at O(1)
print(improved_list.popleft())
# 0
print(improved_list)
# deque([1, 2, 3, 4])

# changing starting point, keeping the order
# positve to shift to the right, negative to shift left!
improved_list.rotate(1)
print(improved_list)
# deque([4, 1, 2, 3])

# Counter is a simple and effective object, that counts!
c1 = Counter([2, 3, 1, 2, 3, 5, 3, 6, 7, 9, 5, 3, 4, 5, 6, 4, 3, 4, 6])
c2 = Counter("gjfjadlfggfkgd;fkgd,fgfsfdjsfj")

print(c1)
# Counter({3: 5, 5: 3, 6: 3, 4: 3, 2: 2, 1: 1, 7: 1, 9: 1})
print(c2.most_common(3))  # top 3
# [('f', 8), ('g', 6), ('j', 4)]

print(c2['m'])
# 0

text = """how many times each word is written in this sentence? I can easily
count, but what is this was a document? will I still count?"""
org_text = text

# this could be done much better with re module
text.replace('?', '')
text.replace(',', '')

words_counter = Counter(text.split(' '))

print(words_counter.most_common(3))
# [('is', 2), ('this', 2), ('I', 2)]

# OrderedDict is a dictionary subclass that remembers the order in 
# which its contents are added
print('Regular dictionary:')
# Regular dictionary:
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

# no gurantee of order when looping thru
for k, v in d.items():
    print(k, v)
# a A
# c C
# b B
# e E
# d D
print('\nOrderedDict:')
# OrderedDict:
d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

# display in the order they are added
for k, v in d.items():
    print(k, v)
# a A
# b B
# c C
# d D
# e E
