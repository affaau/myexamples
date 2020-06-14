'''
Example to show how to use argparse module
'''
import argparse

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="name of the user")
ap.add_argument("-i", "--integer", type=int, default=1, help="An optional special integer")
ap.add_argument("-s", "--secret", type=str, help="A secret message")

# Get arguments as dictionary
args = vars(ap.parse_args())

print("Hi there {}, it's nice to meet you!".format(args['name']))
print("Integer is {}.".format(args['integer']))
if args['secret']:
    print("Secret message is \"{}\".".format(args['secret']))
