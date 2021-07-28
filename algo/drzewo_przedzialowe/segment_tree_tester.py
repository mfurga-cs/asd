#!/usr/bin/env python3

def build_intervals(points):
  n = len(points)
  intervals = []
  for i in range(n - 1):
    intervals.append((points[i], points[i + 1], 0))
  return intervals

def update_interval(intervals, a, b, value):
  n = len(intervals)
  for i in range(n):
    if intervals[i][0] >= a and intervals[i][1] <= b:
      intervals[i] = (intervals[i][0], intervals[i][1], value)
    if intervals[i][0] >= b:
      break

def query_interval(intervals, a, b):
  n = len(intervals)
  m = float("-inf")
  for i in range(n):
    if intervals[i][0] >= a and intervals[i][1] <= b:
      m = max(m, intervals[i][2])
    if intervals[i][0] >= b:
      break
  return m

if __name__ == "__main__":
  points = list(map(int, input().split()))
  intervals = build_intervals(points)

  while line := input():
    op, a, b, value = (list(map(int, line.split())) + [None])[:4]
    if op == 1:
      update_interval(intervals, a, b, value)
    else:
      v = query_interval(intervals, a, b)
      print(v)



