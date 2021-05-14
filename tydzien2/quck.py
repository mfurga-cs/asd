#!/usr/bin/env python3


def partition(head, tail):
  tailnext = tail.next
  pivot = tail
  curr = head

  prev = None
  head = None

  while curr != pivot:
    if curr.value < pivot.value:
      if head is None:
        head = curr
      else:
        prev.next = curr
      prev = curr
    else:
      tail.next = curr
      tail = tail.next
curr = curr.next

  tail.next = tailnext

  if head is not None:
    prev.next = pivot
  else:
    head = pivot

  return head, prev, pivot, tail

def partition(head, tail):
  tailnext = tail.next
  pivot = head

  left_first = None
  right_first = None

  left = None
  mid = pivot
  right = None

  curr = head.next

  while curr is not tail:
    if curr.value > pivot.value:
      if right is None:
        right = curr
        right_first = curr
      else:
        right.next = curr
        right = curr

    if curr.value == pivot.value:
      mid.next = curr
      mid = curr

    if curr.value < pivot.value:
      if left is None:
        left = curr
        left_first = curr
      else:
        left.next = curr
        left = curr

    curr = curr.next

  nhead = None
  ntail = None

  if left is not None:
    left.next = pivot
    nhead = left_first
  else:
    nhead = pivot

  mid.next = right_first
  ntail = right

  return nhead, left, mid, ntail

