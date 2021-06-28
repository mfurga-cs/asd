#!/usr/bin/env python3

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None

def reverse(head):
  prev = None
  curr = head
  next = head.next

  while next is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

  return prev

def print_list(head):
  print("==========")
  while head is not None:
    print(head.val)
    head = head.next

head = Node(1)
curr = head

i = 2
while i < 10:
  curr.next = Node(i)
  curr = curr.next
  i += 1

print_list(head)
head = reverse(head)
print_list(head)


