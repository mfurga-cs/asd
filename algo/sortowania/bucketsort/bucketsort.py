#!/usr/bin/env python3

def insertionsort(a):
  n = len(a)
  for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key
  return a

def bucketsort(arr):
  n = len(arr)
  mn, mx = min(arr), max(arr)

  print("Max: ", mx)
  print("Min: ", mn)

  buckets = [[] for _ in range(n)]

  for i in range(n):
    idx = int(((arr[i] - mn) / (mx - mn)) * n)
    idx = min(idx, n - 1)

    print("item=%i idx=%i" % (arr[i], idx))
    buckets[idx].append(arr[i])

  for i in range(n):
    insertionsort(buckets[i])

  for b in buckets:
    print(b)

#  k = 0
#  for i in range(n):
#    for j in range(len(b[i])):
#      a[k] = b[i][j]
#      k += 1

  #return a

from random import randint

