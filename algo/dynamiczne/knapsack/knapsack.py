#!/usr/bin/env python3

from random import randint

def _knapsack(arr, i, w):
  if i < 0:
    return 0

  if arr[i][0] > w:
    return _knapsack(arr, i - 1, w)

  return max(_knapsack(arr, i - 1, w - arr[i][0]) + arr[i][1], _knapsack(arr, i - 1, w))

def knapsack(arr, w):
  return _knapsack(arr, len(arr) - 1, w)

def _knapsack2(arr, mem, i, w):
  if i < 0:
    return 0

  if mem[i][w] > float("-inf"):
    return mem[i][w]

  if arr[i][0] > w:
    v = _knapsack2(arr, mem, i - 1, w)
    mem[i][w] = v
    return v

  v1 = _knapsack2(arr, mem, i - 1, w - arr[i][0]) + arr[i][1]
  v2 = _knapsack2(arr, mem, i - 1, w)

  if v1 >= v2:
    mem[i][w] = v1
    return v1

  mem[i][w] = v2
  return v2

def knapsack2(arr, w):
  n = len(arr)
  mem = [[float("-inf") for j in range(w + 1)] for i in range(n + 1)]
  return _knapsack2(arr, mem, len(arr) - 1, w)

# (weight, cost)
#t = [(12, 4), (6, 11), (4, 11), (3, 6)]
t = [(randint(1, 100), randint(1, 100)) for _ in range(100)]

