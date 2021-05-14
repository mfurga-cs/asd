#!/usr/bin/env python3

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def print_list(l):
  arr = []
  while l is not None:
    arr.append(l.val)
    l = l.next
  print(arr)

def merge(l1, l2):
  l = Node()
  f = l

  while l1 != None and l2 != None:
    if l1.val < l2.val:
      l.next = Node(l1.val)
      l = l.next
      l1 = l1.next
    else:
      l.next = Node(l2.val)
      l = l.next
      l2 = l2.next

  while l1 != None:
    l.next = Node(l1.val)
    l1 = l1.next

  while l2 != None:
    l.next = Node(l2.val)
    l2 = l2.next

  return f.next

def midNode(head, tail):
  f = head
  s = head

  while f != tail and f.next != tail:
    f = f.next.next
    s = s.next

  return s

def mergesort(head, tail):
  if head == tail:
    Node n = Node(head.val)
    return n
  



