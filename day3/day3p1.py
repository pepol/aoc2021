#!/usr/bin/env python3

import sys

readings = [[int(y) for y in list(x.strip())] for x in sys.stdin.readlines()]
ln = len(readings)

mcb = ''.join(list(map(lambda x: str(int(ln/2 < x)), (map(sum, map(list, zip(*readings)))))))
lcb = ''.join(list(map(lambda x: str(int(x != 1)), [int(x) for x in mcb])))

gamma = int(mcb, base=2)
epsilon = int(lcb, base=2)

print(gamma * epsilon)
