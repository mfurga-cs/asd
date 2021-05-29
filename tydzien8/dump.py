''from queue import PriorityQueue
from math import inf

def Dijkstry2(G,s):
    n=len(G)
    parent=[-1]*n
    value=[inf]*n
    value[s]=0
    q=PriorityQueue()
    q.put((0,s))


    while not q.empty():
        v,p=q.get()
        for i in G[p]:
            if value[i[0]]>v+i[1]:
                value[i[0]]=v+i[1]
                parent[i[0]]=p
                q.put((value[i[0]],i[0]))


    print(value)
    print(parent)



G = [
    [(1, 1), (2, 5)],
    [(0, 1), (2, 2), (3, 7), (4, 8)],
    [(0, 5), (1, 2), (4, 3)],
    [(1, 7), (4, 1)],
    [(1, 8), (2, 3), (3, 1)]
]
Dijkstry2(G,3)






# Reprezentacja wierzchołka grafu
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.visited = False
        self.parent = None


def hamilton_DAG(V, E):
    def DFSVisit(summits, V, E, v):
        nonlocal time, T
        time += 1
        v.visited = True
        for e in E:
            if v.number == e[0] and not summits[e[1]].visited:
                summits[e[1]].parent = e[0]
                DFSVisit(summits, V, E, summits[e[1]])
        T = [V[v.number]] + T

    summits = []
    for v in V:
        summits.append(Summit(v))
    time = 0
    T = []
    for summit in summits:
        if not summit.visited:
            DFSVisit(summits, V, E, summit)
    for i in range(1,len(T)):
        print(T[i-1][0], summits[T[i][0]].parent)
        if T[i-1][0] != summits[T[i][0]].parent:
            return False
    return True


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
E = [(0, 1), (1, 2), (1, 4), (4, 3)]
# V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), '''(4, "e")]
# E = [(0, 1), (1, 2), (2, 


#3), (3, 4)]
#print(hamilton_DAG(V, E))

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


''from queue import PriorityQueue
from math import inf

def Dijkstry2(G,s):
    n=len(G)
    parent=[-1]*n
    value=[inf]*n
    value[s]=0
    q=PriorityQueue()
    q.put((0,s))


    while not q.empty():
        v,p=q.get()
        for i in G[p]:
            if value[i[0]]>v+i[1]:
                value[i[0]]=v+i[1]
                parent[i[0]]=p
                q.put((value[i[0]],i[0]))


    print(value)
    print(parent)



G = [
    [(1, 1), (2, 5)],
    [(0, 1), (2, 2), (3, 7), (4, 8)],
    [(0, 5), (1, 2), (4, 3)],
    [(1, 7), (4, 1)],
    [(1, 8), (2, 3), (3, 1)]
]
Dijkstry2(G,3)






# Reprezentacja wierzchołka grafu
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.visited = False
        self.parent = None


def hamilton_DAG(V, E):
    def DFSVisit(summits, V, E, v):
        nonlocal time, T
        time += 1
        v.visited = True
        for e in E:
            if v.number == e[0] and not summits[e[1]].visited:
                summits[e[1]].parent = e[0]
                DFSVisit(summits, V, E, summits[e[1]])
        T = [V[v.number]] + T

    summits = []
    for v in V:
        summits.append(Summit(v))
    time = 0
    T = []
    for summit in summits:
        if not summit.visited:
            DFSVisit(summits, V, E, summit)
    for i in range(1,len(T)):
        print(T[i-1][0], summits[T[i][0]].parent)
        if T[i-1][0] != summits[T[i][0]].parent:
            return False
    return True


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
E = [(0, 1), (1, 2), (1, 4), (4, 3)]
# V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), '''(4, "e")]
# E = [(0, 1), (1, 2), (2, 