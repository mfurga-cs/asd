#!/usr/bin/env python3
# Minimalna liczba tankowań.
#
# STRATEGIA: Jeśli możesz nie tankować to nie tankuj.
# ZŁOŻONOŚĆ: O(n)

def tank(stations, cap, dest):
  n = len(stations)
  count = 0

  fuel = cap - stations[0]
  for i in range(n):
    if i + 1 < n:
      if stations[i + 1] - stations[i] > fuel:
        fuel = cap
        count += 1
      fuel -= stations[i + 1] - stations[i]
    else:
      if dest - stations[i] > fuel:
        fuel = cap
        count += 1
      fuel -= dest - stations[i]

  return count

stations = [2, 3, 5]
capacity = 2
dest = 6

print(tank(stations, capacity, dest))

