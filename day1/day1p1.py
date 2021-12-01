#!/usr/bin/env python3

import sys

numbers = [int(n) for n in sys.stdin.readlines()]
print(sum(map(lambda x: int(x[1] > x[0]), zip(numbers, numbers[1:]))))
