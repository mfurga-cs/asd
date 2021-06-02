# from math import inf
# from queue import PriorityQueue


# def Ob(G, s):
#     V = G[0]
#     E = G[1]

#     n = len(V)

#     d = [inf for _ in range(n)]
#     visited = [False for _ in range(n)]

#     Q = PriorityQueue()
#     E2 = sortE(G)

#     d[s] = 0
#     Q.put((0, inf, s))

#     while not Q.empty():
#         u = Q.get()

#         if not visited[u[2]]:
#             d[u[2]] = u[0]
#         visited[u[2]] = True

#         v = len(E2[u[2]]) - 1
#         while v >= 0 and E2[u[2]][v][0] < u[1]:
#             Q.put((u[0] + E2[u[2]][v][0], E2[u[2]][v][0], E2[u[2]][v][1]))
#             E2[u[2]].pop(v)
#             v -= 1

#     print(d)


# def sortE(G):
#     V = G[0]
#     E = G[1]
#     n = len(V)

#     E2 = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if E[i][j] != -1:
#                 E2[i].append((E[i][j], j))
#         E2[i].sort(reverse=True)
#     return E2


# V = [0, 1, 2, 3, 4]

# E = [[-1, 2, -1, -1, 1],
#      [2, -1, 4, 1, -1],
#      [-1, 4, -1, 5, -1],
#      [-1, 1, 5, -1, 3],
#      [1, -1, -1, 3, -1]]

# Ob((V, E), 0)
'''
G = [[-1, 10, 5, -1, -1, -1],
     [10, -1, 1, 3, 5, -1],
     [5, 1, -1, 6, 4, -1],
     [-1, 3, 6, 3, 3, 2],
     [-1, 5, -1, 3, -1, 1],
     [-1, -1, -1, 2, 1, -1]]
#0 -> 3 [0, 2, 4, 3] 12
'''
from queue import Queue

def BFS(T, s):

    n = len(T)
    Q = Queue()
    visited = [False] * n
    distance = [-1] * n
    parent = [None] * n
    distance[s] = 0
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()


        for v in range(n):
            if T[u][v] != 0 and not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    return distance


def close_pedestrians(G):
    n = len(G)
    H = [[0] * n for i in range(n)]
    for i in range(n):
        distance = BFS(G, i)
        for j in range(n):
            if distance[j] > 0:
                H[i][j] = 1

    return H


G = [[0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0]]
H = close_pedestrians(G)
print(H)