#!/usr/bin/env python3
#
# Zcalanie k posortowanych list w jedną.
# Zlożność: O(nlogk)
# n - ilość elementów we wszystkich listach.
# k - ilość list do scalenia

from queue import PriorityQueue

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
    return 1

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

def merge(L):
  n = len(L)
  Q = PriorityQueue()

  for i in range(n):
    if L[i] is not None:
      Q.put((L[i].value, L[i]))

  head = Node("dummy")
  curr = head

  while Q.qsize() > 0:
    _, l = Q.get()
    if l.next is not None:
      Q.put((l.next.value, l.next))
    curr.next = l
    curr = curr.next

  return head.next

A =  [[0,1,2,4,5],[0,3,4,10,20],[1,2,3,4,15,25], [100, 121,130]]
L = [array_to_list(A[i]) for i in range(len(A))]
L = merge(L)
print_list(L)

