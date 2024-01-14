# working with arguments
# how to run python3 15-arguments.py -c red

import sys
print(sys.argv)

print("Hello ", sys.argv[0])
print("Color: ", sys.argv[2])


import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-c', '--color', help='Color of the car', required=True)

args = parser.parse_args()
print(args.color)