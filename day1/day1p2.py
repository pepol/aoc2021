#!/usr/bin/env python3

import sys

numbers = [int(n) for n in sys.stdin.readlines()]
windows = list(map(lambda x: sum(x), zip(numbers, numbers[1:], numbers[2:])))
print(sum(map(lambda x: int(x[1] > x[0]), zip(windows, windows[1:]))))
