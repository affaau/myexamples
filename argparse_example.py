'''argparse example
ref: https://docs.python.org/2/howto/argparse.html
'''

import sys
import argparse

parser = argparse.ArgumentParser()
# positional arguments

# optional arguments
group = parser.add_mutually_exclusive_group()  # only work for optional arguments
group.add_argument('-b', "--buy", help="BUY mode", action="store_true")
group.add_argument('-s', "--sell", help="SELL mode", action="store_true")

parser.add_argument('-code', '--code', help="a reference HK stock code", default="Anonymous")
# test arguments
# it works for [-p  | -q | -pq | -qp] or no entry
parser.add_argument('-p', help="test1", action="store_true")
parser.add_argument('-q', help="test2", action="store_true")
#

args = parser.parse_args()

# actions
if args.buy:
    print("BUY mode")
elif args.sell:
    print("SELL mode")
else:
    print("default BUY mode")

print("Stock: {}".format(args.code))

if args.p:
    print("test1")

if args.q:
    print("test2")
