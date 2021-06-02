from collections import deque

def BFS(G, s): #indeksuje grafy od zera
    n = len(G)
    k = 0
    Q = deque()

    G = sorted(G,key = lambda x: x[1])
    G = sorted(G,key = lambda x: x[0])

    for i in range(n):
        if G[i][1] > k:
            k = G[i][1]
    n = k + 1

    visited = [False]*n
    d = [-1]*n #odleglosci, jesli -1 to znaczy ze nie ma polaczenia
    parents = [None]*n

    d[s] = 0
    Q.append(s)
    visited[s] = True

    while Q:
        u = Q.popleft()
        for i in range(n):
            if not visited[G[i][1]] and G[i][0] == u:
                visited[G[i][1]] = True
                d[G[i][1]] = d[u] + 1
                parents[G[i][1]] = u
                Q.append(G[i][1])

    res = []
    k = n-1
    res.append(k)
    while k is not None:
        res.append(parents[k])
        k = parents[k]


    return res

#G = [(0,1),(0,2),(1,2),(1,3),(2,4),(4,3)]
G = [(0,1),(1,2),(2,3),(3,0),(2,4)]
print(BFS(G,0))