#!/usr/bin/env python3

def enqueue(q, e):
  q.append(e)

def dequeue(q):
  if len(q) < 0:
    return

  s = []

  while len(q) > 1:
    s.append(q.pop())

  res = q.pop()
  while len(s) > 0:
    q.append(s.pop())

  return res

