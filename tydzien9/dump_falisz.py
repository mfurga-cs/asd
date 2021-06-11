# parking tutaj
def calc_transitive_closure(graph): # algorytm Floyda-Warshalla
    n = len(graph)
    graph_H = [[False]*n for _ in range(n)]
    
    # init
    for u in range(n):
        for v in range(n):
            graph_H[u][v] = bool(graph[u][v])


    # Algorithm
    for t in range(n): # korzystam z wierzchołków v0, v1, v2, ..., vt
        for i in range(n): # ścieżka wychodzi z wierzchołka vi
            for j in range(n): # ścieżka dociera do wierzchołka vj
                if i == j:
                    continue
                graph_H[i][j] = graph_H[i][j] or bool(graph_H[i][t]) and bool(graph_H[t][j])
        
    return graph_H



# prosty test
#graph = [ # 0 to brak krawędzi
#    [0, 10, 1, 0, 5],
#    [0, 0, 0, 5, 0],
#    [1, 1, 0, 0, 0],
#    [0, 0, 0, 0, 0],
#    [5, 0, 0, 0, 0]
#    ]
#graph_H = calc_transitive_closure(graph)
#for row in graph_H:
#    row = list(map(int, row))
#    print(row)


# for list of edges
def decreasing_path(graph, start, t):
    # find number of nodes
    m = len(graph)
    n = 0
    for i in range(m):
        n = max(n, graph[i][0], graph[i][1])
    n += 1

    # sort edges by weight (decreasing order)
    graph.sort(key=lambda x: x[2], reverse=True)

    # go through edges
    shortest = [float('inf') for _ in range(n)]
    parent = [[] for _ in range(n)]
    shortest[start] = 0
    for i in range(m):
        u, v, w = graph[i]
        if shortest[u] + w < shortest[v]:
            shortest[v] = shortest[u] + w
            parent[v].append([u, w, shortest[v]])
        elif shortest[v] + w < shortest[u]:
            shortest[u] = shortest[v] + w
            parent[u].append([v, w, shortest[u]])

    # recreate result based on parents
    if not parent[t]:
        return []
    result = [t]
    prev_val = shortest[t]
    prev_edge = parent[t][len(parent[t]) - 1][1]
    t = parent[t][len(parent[t]) - 1][0]
    while parent[t]:
        result.append(t)
        i = len(parent[t]) - 1
        u, w, s = parent[t][i]
        while prev_val - prev_edge != s:
            i -= 1
            u, w, s = parent[t][i]
        prev_val = s
        prev_edge = w
        t = u
    result.append(start)
    return result[::-1]


G = [(0, 1, 4), (1, 2, 10), (0, 4, 8), (1, 4, 11), (4, 5, 7), (4, 6, 4), (5, 6, 6), (2, 3, 2), (2, 5, 9), (3, 6, 3),
     (6, 7, 5), (3, 7, 15), (3, 8, 8), (7, 8, 1)]
print(decreasing_path(G, 0, 8))