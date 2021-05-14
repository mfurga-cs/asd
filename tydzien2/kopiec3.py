#!/usr/bin/env python3

def left(i):
  return 3 * i + 1

def mid(i):
  return 3 * i + 2

def right(i):
  return 3 * i + 3

def parent(i):
  return (i - 1) // 3

def heapify(t, n, i):
  l = left(i)
  m = mid(i)
  r = right(i)
  max = i

  if l < n and t[l] > t[max]:
    max = l
  if m < n and t[m] > t[max]:
    max = m
  if r < n and t[r] > t[max]:
    max = r

  if max != i:
    t[i], t[max] = t[max], t[i]
    heapify(t, n, max)

def buildheap(t):
  n = len(t)
  for i in range(parent(n - 1), -1, -1):
    heapify(t, n, i)

def increase_key(t, i, key):
  if key < t[i]:
    return
  t[i] = key
  while i > 0 and t[parent(i)] < t[i]:
    t[i], t[parent(i)] = t[parent(i)], t[i]
    i = parent(i)

def insert(t, e):
  t.append(float("-inf"))
  increase_key(t, len(t) - 1, e)

def extract_max(t):
  n = len(t)
  if n < 0:
    return
  t[0], t[n - 1] = t[n - 1], t[0]
  res = t.pop()
  heapify(t, len(t), 0)
  return res


