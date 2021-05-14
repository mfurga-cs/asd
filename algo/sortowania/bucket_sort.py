#!/usr/bin/env python3
# Bucketsort dla listy jednokierunkowej.

class Node(object):
  def __init__(self, val, next):
    self.val = val
    self.next = next

def count_min_max(l):
  l = l.next
  c = 0
  mx = -1
  mn = float("+inf")
  while l is not None:
    mn = min(mn, l.val)
    mx = max(mx, l.val)
    c += 1
    l = l.next
  return c, mn, mx

def list_insert(l, node):
  prev = l
  curr = l
  while curr is not None and curr.val < node.val:
    prev = curr
    curr = curr.next
  node.next = curr
  prev.next = node

def bucketsort(l):
  # Zliczanie elementów i szukanie min i max.
  n, mn, mx = count_min_max(l)
  print("min %f, max: %f, n: %i" % (mn, mx, n))

  buckets = [Node(-1, None) for _ in range(n)]

  prev = l.next
  curr = l.next

  while curr is not None:
    curr = curr.next
    idx = int(((prev.val - mn) / mx) * n)
    if idx == n:
      idx -= 1

    list_insert(buckets[idx], prev)
    prev = curr

  for i in range(n):
    print("%i: " % (i + 1), end="")
    print_list(buckets[i])

  nl = l

  for i in range(n):
    curr = buckets[i].next
    while curr != None:
      nl.next = curr
      nl = nl.next
      curr = curr.next

  print("new list:")
  print_list(l)
  return nl

def print_list(l):
  while l is not None:
    print(l.val, end=" -> ")
    l = l.next
  print("None")

def arr_to_list(arr):
  l = Node(-1, None)
  curr = l
  for e in arr:
    curr.next = Node(e, None)
    curr = curr.next
  return l

