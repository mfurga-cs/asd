# Znajdowanie punktów artykulacji w grafie.
#
# low[v] - indeks najwyżeszego wierzchołka w drzewie dfs, do którgo możemy skoczyć
#          z podrzewa zakorzenionego w v.
#
# Złożoność: O(V + E)

from utils import g_convert

def dfs(G):
  n = len(G)

  preorder = 0
  visited = [False] * n
  parent = [-1] * n
  pre = [-1] * n
  low = [-1] * n

  vertices = []

  def dfs_visit(u):
    nonlocal preorder

    visited[u] = True

    pre[u] = low[u] = preorder
    preorder += 1
    ok = False

    for v, _ in G[u]:
      if not visited[v]:
        # Jeżeli wierzchołek nie został odwiedzony tzn. musi towrzyć osobne
        # podrzewo, które nie jest połączone krawędzą do innych podrzew dzieci u.
        # Gdyby tak było to wierzchołek v byłby odwiedzony wcześniej w jednym z tych
        # podrzew.
        parent[v] = u
        dfs_visit(v)

        # Aktualizujemy low[u] z dzieci wierzchołka u.
        low[u] = min(low[u], low[v])

        # Jeżeli chociaż dla jednego dziecka v wierzchołka u podrzewo zakorzenione w
        # v nie ma krawędzi wyżej nad u to będzie ono odłączone od grafu a wierzchołek
        # u będzie punktem artykulacji.
        if low[v] >= pre[u] and u != 0:
          ok = True

      elif v != parent[u]:
        # Jeżeli wierzchołek v był już odwiedzony i nie przyszliśmy z niego do obecnego
        # to krawędz u-v jest to krawędź wsteczna (skok) do wcześniejszego wierzchołka v
        # w drzewie dfs. Aktualizujemy low[u].
        low[u] = min(low[u], pre[v])

    if ok:
      vertices.append(u)

  dfs_visit(0)

  # Dla korzenia drzewa dfs (0) sprawdzamy osobno czy ma wiecej niż 1 dziecko w drzewie.
  # Jeśli tak oznaczać to będzie że po usunięciu go graf się rozpójni.
  count = 0

  for u in range(n):
    if parent[u] == 0:
      count += 1

  if count > 1:
    vertices.append(0)

  print(vertices)


G = """
0
1
2
3
4
5
#
0 3
1 0
1 4
3 2
4 5
"""

dfs(g_convert(G))


