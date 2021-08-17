#!/usr/bin/env python3

s = []

def subsets(k):
  if k == 3:
    print(s)
    return
  subsets(k + 1)
  s.append(k)
  subsets(k + 1)
  s.pop()

def subsets2(n):
  for i in range(1 << n):
    s = []
    for j in range(n):
      if i & (1 << j):
        s.append(j)
    print(s)

subsets(0)
print("=========")
subsets2(3)


