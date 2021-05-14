#!/usr/bin/env python3

def remove_duplicates(s):
  d = {}
  for c in s:
    if c in d:
      d[c] += 1
    else:
      d[c] = 1

  stack = []

  for c in s:
    while len(stack) > 0 and stack[-1] >= c and d[stack[-1]] > 0:
      stack.pop()
    if c not in stack:
      stack.append(c)
    d[c] -= 1

  print(d)
  print(stack)

s = "cabaaaddbb"
remove_duplicates(s)


