#!/usr/bin/env python3

from functools import reduce
import sys

def mcb(l, pos):
    ln = len(l)
    count = reduce(lambda a,b: a+b, map(lambda x: x[pos], l))
    if count >= ln/2:
        return 1
    else:
        return 0

def oxygen(readings):
    acum_list = readings
    for i in range(len(readings[0])):
        if len(acum_list) == 1:
            break
        v = mcb(acum_list, i)
        acum_list = list(filter(lambda x: x[i] == v, acum_list))
    return int(''.join([str(x) for x in acum_list[0]]), 2)

def co2(readings):
    acum_list = readings
    for i in range(len(readings[0])):
        if len(acum_list) == 1:
            break
        v = int(not mcb(acum_list, i))
        acum_list = list(filter(lambda x: x[i] == v, acum_list))
    return int(''.join([str(x) for x in acum_list[0]]), 2)

readings = [[int(y) for y in list(x.strip())] for x in sys.stdin.readlines()]
print(oxygen(readings) * co2(readings))
