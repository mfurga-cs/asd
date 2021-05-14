#!/usr/bin/env python3

# def partition(t, l, h):
#   p = t[h]
#   i = l - 1

#   for j in range(l, h):
#     if t[j] < p:
#       i += 1
#       t[i], t[j] = t[j], t[i]

#   t[i + 1], t[h] = t[h], t[i + 1]
#   return i + 1


def partition(arr, lo, hi):
  pivot = arr[lo]
  i, j = lo + 1, hi

  while True:
    while arr[i] < pivot:
      if i == hi:
        break
      i += 1
    while arr[j] > pivot:
      j -= 1

    if j <= i:
      break
    arr[i], arr[j] = arr[j], arr[i]

  arr[lo], arr[j] = arr[j], arr[lo]
  return j


def _quicksort(t, l, h):
  if l < h:
    p = partition(t, l, h)
    _quicksort(t, l, p - 1)
    _quicksort(t, p + 1, h)

def quicksort(t):
    return _quicksort(t, 0, len(t) - 1)

# def _quicksort_tail(t, l, h, i = 0):
#   print(i)

#   while l < h:
#     p = partition(t, l, h)
#     if p - l < h - p:
#       _quicksort_tail(t, l, p - 1, i + 1)
#       l = p + 1
#     else:
#       _quicksort_tail(t, p + 1, h, i + 1)
#       h = p - 1

# def quicksort_tail(t):
#   _quicksort_tail(t, 0, len(t) - 1)

# def quicksort(t):
#   n = len(t)
#   s = [(0, n - 1)]

#   while len(s) > 0:
#     l, h = s.pop()
#     if l >= h:
#       continue
#     p = partition(t, l, h)
#     s.append((l, p - 1))
#     s.append((p + 1, h))


