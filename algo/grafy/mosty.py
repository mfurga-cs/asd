# Znajdowanie mostów w grafie.
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

  def dfs_visit(u):
    nonlocal preorder

    visited[u] = True

    pre[u] = low[u] = preorder
    preorder += 1

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
      elif v != parent[u]:
        # Jeżeli wierzchołek v był już odwiedzony i nie przyszliśmy z niego do obecnego
        # to krawędz u-v jest to krawędź wsteczna (skok) do wcześniejszego wierzchołka v
        # w drzewie dfs. Aktualizujemy low[u].
        low[u] = min(low[u], pre[v])

  for u in range(n):
    if not visited[u]:
      dfs_visit(u)

  # Mosty to krawędzie, dla których dla jednego z wierzchoów zachodzi pre[u] = low[u].
  # Tzn. nie istnije żadna krawędz wychodząca z podrzewa u, która idzie wyżej nad u.
  # Most to u i parent[u].
  for u in range(n):
    if low[u] == pre[u] and u != 0:
      print("%d - %d" % (parent[u], u))

G = """
0
1
2
3
4
5
#
0 2
0 3
1 0
1 4
3 2
1 5
4 5
"""

dfs(g_convert(G, False))

