# Mateusz Furga
#
# Wolne pola będą wierzchołkami w grafie. Do każdego pola dodajemy informacje
# z jakiego kierunku do niego trafiliśmy i który z kolei to ruch do przodu.
# Do tak utowrzonego grafu szukamy najktótszej scieżki przy użyciu zmodyfikowanego
# alg. Dijkstry.
#
# Złożoność to złożoność alg. Dijkstry dla powielonych wierzchołków. O(ElogV)
#

from zad2testy import runtests
from queue import PriorityQueue

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
SPEEDS = (60, 40, 30)

def can_move(L, y, x):
  n = len(L)
  m = len(L[0])
  return 0 <= y < n and 0 <= x < m and L[y][x] != "X"

def robot(L, A, B):
  n = len(L)
  m = len(L[0])
  Q = PriorityQueue()

  D = [None] * (n + 1)
  for i in range(n + 1):
    D[i] = [None] * (m + 1)

  for i in range(n + 1):
    for j in range(m + 1):
      D[i][j] = [None] * 4

  for i in range(n + 1):
    for j in range(m + 1):
      for k in range(4):
        D[i][j][k] = [float("+inf")] * 3

  x = A[0]
  y = A[1]

  vertex = (y, x, 0, 0)
  D[y][x][0][0] = 0
  Q.put((0, vertex))

  while Q.qsize() > 0:
    _, u = Q.get()
    curr_y, curr_x, curr_dir, curr_speed = u

    if curr_x == B[0] and curr_y == B[1]:
      return D[curr_y][curr_x][curr_dir][curr_speed]

    next_y = curr_y + DIRECTIONS[curr_dir][0]
    next_x = curr_x + DIRECTIONS[curr_dir][1]

    next_dir = curr_dir
    next_speed = curr_speed + 1 if curr_speed + 1 <= 2 else 2

    if can_move(L, next_y, next_x):
      v = (next_y, next_x, next_dir, next_speed)
      d = D[curr_y][curr_x][curr_dir][curr_speed] + SPEEDS[curr_speed]

      if D[next_y][next_x][next_dir][next_speed] > d:
        D[next_y][next_x][next_dir][next_speed] = d
        Q.put((d, v))

    next_x = curr_x
    next_y = curr_y
    next_dir = (curr_dir + 1) % 4
    next_speed = 0

    v = (next_y, next_x, next_dir, next_speed)
    d = D[curr_y][curr_x][curr_dir][curr_speed] + 45

    if D[next_y][next_x][next_dir][next_speed] > d:
      D[next_y][next_x][next_dir][next_speed] = d
      Q.put((d, v))

    next_dir = (curr_dir - 1) % 4
    v = (next_y, next_x, next_dir, next_speed)

    if D[next_y][next_x][next_dir][next_speed] > d:
      D[next_y][next_x][next_dir][next_speed] = d
      Q.put((d, v))

  return

L = [ "XXXXXXXXXX", # 0
      "X X      X", # 1
      "X XXXXXX X", # 2
      "X        X", # 3
      "XXXXXXXXXX", # 4
]
A = (1, 1)
B = (8, 3)

#print(robot(L, A, B))
runtests(robot)

