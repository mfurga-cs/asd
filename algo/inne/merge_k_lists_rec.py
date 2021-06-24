#!/usr/bin/env python3
#
# Zcalanie k posortowanych list w jedną.
# Zlożność: O(nlogk)
# n - ilość elementów we wszystkich listach.
# k - ilość list do scalenia

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

def print_list(L):
  while L is not None:
    print(L.value, end=" -> ")
    L = L.next
  print("NULL")

def array_to_list(A):
  n = len(A)
  if n == 0:
    return None
  head = Node(A[0])
  prev = head
  for i in range(1, n):
    prev.next = Node(A[i])
    prev = prev.next
  return head

def merge(L1, L2):
  head = Node("dummy")
  curr = head

  while L1 is not None and L2 is not None:
    if L1.value <= L2.value:
      curr.next = L1
      L1 = L1.next
    else:
      curr.next = L2
      L2 = L2.next
    curr = curr.next

  while L1 is not None:
    curr.next = L1
    L1 = L1.next
    curr = curr.next

  while L2 is not None:
    curr.next = L2
    L2 = L2.next
    curr = curr.next

  return head.next

def mergesort(L, i, j):
  if i == j:
    return L[i]
  m = (i + j) // 2
  l = mergesort(L, i, m)
  r = mergesort(L, m + 1, j)
  return merge(l, r)

def merge_lists(L):
  return mergesort(L, 0, len(L) - 1)

#A =  [[0,1,2,4,5],[0,10,20],[5,15,25], [1,2,3,4, 100, 121]]
#L = [array_to_list(A[i]) for i in range(len(A))]
#L = merge_lists(L)

#print_list(L)

