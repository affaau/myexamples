'''ref: http://zetcode.com/python/fstring/
'''
from datetime import datetime
import sys


ver = sys.version_info
# f-string style examples, support since v3.6
if ver.major < 3 or ver.minor < 6:
    print('f-string format supports from v3.6 onwards')
    sys.exit()

print(f'[1234567890123456]')
val = -45.346
print(f'[{val: <16}]')

now = datetime.now()
d_fmt = f'{now:%Y-%m-%d}'
print(f'[{d_fmt:<16}]')

print(f'[{-45.346:^16.2f}]')

for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}')

print()
s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'

print(f'1234567890')
print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')

a = 300
# hexadecimal
print(f'{a:x}')  # 12c
# octal
print(f'{a:o}')  # 454
# scientific
print(f'{a:e}')  # 3.000000e+02

# special case for curly bracket, cannot use \ back slash!
print(f'Python uses {{}} to evaludate variables in f-strings')
# Python uses {} to evaludate variables in f-strings
print(f'This was a \'great\' film')
# This was a 'great' film
