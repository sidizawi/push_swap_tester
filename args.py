#!/usr/bin/env python3

from random import randint
import sys

"""
./args.py count min_val max_val

    - count     : number of args
    - min_val   : minimum value
    - max

"""

def main():
    count = 5
    max_val = 5
    min_val = -5

    if len(sys.argv) == 4:
        count = int(sys.argv[1])
        min_val = int(sys.argv[2])
        max_val = int(sys.argv[-1])

    args = []

    for _ in range(count):
        new_arg = randint(min_val, max_val)
        while new_arg in args:
            new_arg = randint(min_val, max_val)
        args += [new_arg]

    print(*args)

if __name__ == '__main__':
    main()
