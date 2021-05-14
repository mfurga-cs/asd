#!/usr/bin/env python3

def left(i):
  return 2 * i + 1

def right(i):
  return 2 * i + 2

def parent(i):
  return (i - 1) // 2

def heapify(t, n, i):
  l = left(i)
  r = right(i)
  m = i

  if l < n and t[l] > t[m]:
    m = l
  if r < n and t[r] > t[m]:
    m = r

  if m != i:
    t[i], t[m] = t[m], t[i]
    heapify(t, n, m)

def heapify_iter(t, n, i):
  while True:
    l = left(i)
    r = right(i)
    m = i
    if l < n and t[l] > t[m]:
      m = l
    if r < n and t[r] > t[m]:
      m = r

    if m == i:
      break

    t[i], t[m] = t[m], t[i]

def buildheap(t):
  n = len(t)
  for i in range(parent(n - 1), -1, -1):
    heapify(t, n, i)

def heapsort(t):
  n = len(t)
  buildheap(t)

  for i in range(n - 1, 0, -1):
    t[i], t[0] = t[0], t[i]
    heapify(t, i, 0)

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

