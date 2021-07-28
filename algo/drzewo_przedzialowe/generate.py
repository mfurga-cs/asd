#!/usr/bin/env python3

import random
import sys

POINTS = 100
TESTS = 200

random.seed(int(sys.argv[1]))

points = []

while len(points) != POINTS:
  p = random.randint(-1 * POINTS * 10, POINTS * 10)
  points.append(p)

points = sorted(set(points))
print(" ".join(str(p) for p in points))

for i in range(TESTS):
  op = random.randint(1, 2)

  if op == 1:
    value = random.randint(-1000, 1000)
    a, b = sorted(random.sample(points, 2))
    print(op, a, b, value)
  else:
    a, b = sorted(random.sample(points, 2))
    print(op, a, b)

print()

