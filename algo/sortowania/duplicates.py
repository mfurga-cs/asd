#!/usr/bin/env python3

def duplicates(arr):
  n = len(arr)
  i = 0
  j = 1
  while j < n:
    if arr[i] != arr[j]:
      i += 1
      arr[i] = arr[j]
    j += 1
  print(i)

