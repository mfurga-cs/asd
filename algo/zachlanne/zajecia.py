#!/usr/bin/env python3

def s(act):
  return act[0]

def f(act):
  return act[1]

def _select(arr, i, n):
  j = i + 1

  while j < n and f(arr[i]) > s(arr[j]):
    j += 1

  if j >= n:
    return []

  return [arr[j]] + _select(arr, j, n)

def select(arr):
  return [arr[0]] + _select(arr, 0, len(arr))

t = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]

