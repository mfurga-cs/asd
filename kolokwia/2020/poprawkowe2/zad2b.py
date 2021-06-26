
from zad2testy import runtests
from collections import deque

def let(ch):
  return ord(ch) - ord("a")

def bfs(G, L, W, s):
  queue = deque()

  queue.append((s, 0, 0))
  distances = [float("+inf")]

  while len(queue) > 0:
    u, i, d = queue.popleft()

    if i == len(W) - 1:
      distances.append(d)
      continue

    for v, w in G[u]:
      if L[v] == W[i + 1]:
        queue.append((v, i + 1, d + w))

  return min(distances)

def letters(G, W):
  L, E = G
  n = len(L)
  G = [[] for _ in range(n)]

  for u, v, w in E:
    G[u].append((v, w))
    G[v].append((u, w))

  v = float("+inf")
  for i in range(n):
    if L[i] == W[0]:
      v = min(v, bfs(G, L, W, i))

  return v

runtests(letters)

