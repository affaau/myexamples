from timeit import timeit

code1='''
items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)
'''
code2='''
items = [1,2,3,4,5]
squared = list(map(lambda x:x**2, items))
'''

print(timeit(stmt=code1, number=10000))

print(timeit(stmt=code2, number=10000))

