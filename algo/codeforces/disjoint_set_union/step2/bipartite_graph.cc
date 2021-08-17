/*
  Dla każdego wierzchołka w DSU trzymamy parzystość ścieżki do parenta.
  Gdy łączymy dwa wierzchołki krawędzią x i y to liczymy parzystość x do reprezentata x
  oraz parzystość y do reprezentata y. Łączymy dwa zbiory tzn łączymy reprezentatów 2 zbiorów
  i ustawiamy parzystość równa: parzystość x do rep. + parzystość y do rep. + 1 bo taka jest
  faktyczna parzystkość scieżki pomiędzy reprezentami połączonymi przy użyciu x i y.
*/

#include <bits/stdc++.h>

std::vector<int> parent;
std::vector<int> rank;
std::vector<int> dist;

void init_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
  dist[x] = 0;
}

int find_set(int x)
{
  if (parent[x] == x) {
    dist[x] = 0;
    return parent[x];
  }
  int p = find_set(parent[x]);
  dist[x] = (dist[x] + dist[parent[x]]) % 2;
  parent[x] = p;
  return parent[x];
}

void union_sets(int x, int y)
{
  int px = find_set(x);
  int py = find_set(y);

  if (px == py) {
    return;
  }

  if (rank[px] > rank[py]) {
    parent[py] = px;
    dist[py] = (dist[x] + dist[y] + 1) % 2;
  } else {
    parent[px] = py;
    dist[px] = (dist[x] + dist[y] + 1) % 2;
    if (rank[px] == rank[py]) {
      rank[py]++;
    }
  }
}

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  parent.resize(n);
  rank.resize(n);
  dist.resize(n);

  for (int i = 0; i < n; i++) {
    init_set(i);
  }

  int shift = 0;
  int op, a, b;
  int x, y;

  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", &op, &a, &b);
    x = (a + shift) % n;
    y = (b + shift) % n;

    if (op == 0) {
      union_sets(x, y);
    } else {
      volatile int px = find_set(x);
      volatile int py = find_set(y);

      if (dist[x] == dist[y]) {
        printf("YES\n");
        shift = (shift + 1) % n;
      } else {
        printf("NO\n");
      }
    }
  }

  return 0;
}


