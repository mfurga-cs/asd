#!/usr/bin/env python3
#
### Na każdej stacji możemy kupić tyle ile chcemy.
#
# STRATEGIA: Jeśli musimy kupić to tylko tyle aby dostać się do następnej tańszej stacji.
#            Jeśli takiej stacji nie ma to kupujemy tylko tyle aby dostać się do punkty t.
#
# ZŁOŻONOŚĆ: O(n)       jeśli stacje są posortowane po pozycji.
#            O(nlogn)   wpp
#

class Station(object):
  def __init__(self, pos, cost):
    self.pos = pos
    self.cost = cost

def tank(stations, dest, cap):
  n = len(stations)

  # Dla każdej stacji szukamy następnej, która ma mniejszy koszt. O(n).
  next_station = [-1] * n
  stack = []

  for i in range(n):
    while len(stack) > 0 and stations[stack[-1]].cost > stations[i].cost:
      next_station[stack.pop()] = i
    stack.append(i)

  cost = 0
  fuel = cap - stations[0].pos

  for i in range(n):
    if next_station[i] == -1:
      need = dest
    else:
      need = stations[next_station[i]].pos

    need -= stations[i].pos
    need = min(cap, need)

    if need > fuel:
      cost += (need - fuel) * stations[i].cost
      fuel = need

    if i == n - 1:
      fuel -= dest - stations[i].pos
    else:
      fuel -= stations[i + 1].pos - stations[i].pos

  return cost

stations = [Station(2, 10), Station(3, 1000), Station(6, 5)]
print(tank(stations, 7, 3))

