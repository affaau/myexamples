'''ref: https://docs.python.org/3.6/library/string.html#formatstrings
'''
from datetime import datetime
import sys


print("[1234567890123456]")
print("[{:<16}]".format(-45.346))  # default filling is ' '
print("[{:>16}]".format(-45.346))
print("[{:=16}]".format(-45.346))
print("[{:^16}]".format(-45.346))
# [1234567890123456]
# [-45.346         ]
# [         -45.346]
# [-         45.346]
# [    -45.346     ]

print("[{:<16.2f}]".format(-45.346))
print("[{:>16.2f}]".format(-45.346))
print("[{:=16.2f}]".format(-45.346))
print("[{:^16.2f}]".format(-45.346))
# [-45.35          ]
# [          -45.35]
# [-          45.35]
# [     -45.35     ]

print("[{:016b}]".format(15))  # 16-bit, fills with 0
# [0000000000001111]

print("[{:>16b}]".format(15))  # no filling
print("[{:^16b}]".format(15))
# [            1111]
# [      1111      ]

num_fmt = "{:05b}".format(15)
print("[{:^16s}]".format(num_fmt))
# [     01111      ]

ver = sys.version_info
# f-string style examples, support since v3.6
# ref: http://zetcode.com/python/fstring/
if ver.major >= 3 and ver.minor >= 6:
    print()

    val = -45.346
    print(f'[{val: <16}]')

    now = datetime.now()
    d_fmt = f'{now:%Y-%m-%d}'
    print(f'[{d_fmt:<16}]')

    print(f'[{-45.346:^16.2f}]')

    for x in range(1, 11):
        print(f'{x:02} {x*x:3} {x*x*x:4}')

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
