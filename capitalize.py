#!/bin/python3

import os


def solve(s):
    words = s.split(' ')
    return " ".join((word.capitalize() for word in words))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
