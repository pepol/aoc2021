#!/usr/bin/env python3

import sys

instructions_str = [x.split() for x in sys.stdin.readlines()]
instructions = [(x[0], int(x[1])) for x in instructions_str]

h = 0
v = 0
aim = 0

for inst in instructions:
    if inst[0] == 'forward':
        h += inst[1]
        v += inst[1] * aim
    if inst[0] == 'up':
        aim -= inst[1]
    if inst[0] == 'down':
        aim += inst[1]

print(v * h)
