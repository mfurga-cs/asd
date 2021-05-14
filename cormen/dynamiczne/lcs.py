#!/usr/bin/env python3

def backtract(s1, s2, mem, i, j):
  if i == -1 or j == -1:
    return ""
  if s1[i] == s2[j]:
    return backtract(s1, s2, mem, i - 1, j - 1) + s1[i]

  if mem[i - 1 + 1][j + 1] > mem[i + 1][j - 1 + 1]:
    return backtract(s1, s2, mem, i - 1, j)

  return backtract(s1, s2, mem, i, j - 1)

def lcs(s1, s2):
  n1 = len(s1)
  n2 = len(s2)

  mem = [[0] * (n2 + 1) for _ in range(n1 + 1)]

  for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
      if s1[i - 1] == s2[j - 1]:
        mem[i][j] = mem[i - 1][j - 1] + 1
      else:
        mem[i][j] = max(mem[i - 1][j], mem[i][j - 1])

  for r in mem:
    print(r)

  print(backtract(s1, s2, mem, n1 - 1, n2 - 1))


