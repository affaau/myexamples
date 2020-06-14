'''Extract the largest signed integer from the beginning of the
given string.
- neglect all initial white spaces
- if alphabets appeards first, consider no match
'''
import re

x = '   +123   '
y = 'abc 123  -456'
z = '-123 apple '

num_regex = re.compile(r'^\s*([-+]?\d+).*')
gp = num_regex.search(x)
print(x)
if gp:
    print(gp.group())
    print(gp.group(1))   # '+123'
else:
    print('No match')

print()
gp = num_regex.search(y)
print(y)
if gp:
    print(gp.group())
    print(gp.group(1))
else:
    print('No match')    # no match

print()
gp = num_regex.search(z)
print(z)
if gp:
    print(gp.group())
    print(gp.group(1))   # '-123'
else:
    print('No match')
