#include <bits/stdc++.h>

typedef unsigned long long int64;

std::vector<int64> parent;
std::vector<int64> rank;

struct edge {
  int64 u, v, w, idx;
  bool ok;
};

std::vector<edge> G;

void init_set(int64 x)
{
  parent[x] = x;
  rank[x] = 0;
}

int64 find_set(int64 x)
{
  if (parent[x] != x) {
    parent[x] = find_set(parent[x]);
  }
  return parent[x];
}

void union_sets(int64 x, int64 y)
{
  x = find_set(x);
  y = find_set(y);

  if (x == y) {
    return;
  }

  if (rank[x] > rank[y]) {
    parent[y] = x;
  } else {
    parent[x] = y;
    if (rank[x] == rank[y]) {
      rank[y]++;
    }
  }
}

bool cmp(const edge &a, const edge &b)
{
  return a.w > b.w;
}

int main(void)
{
  int64 n, m, s;
  scanf("%llu %llu %llu", &n, &m, &s);

  parent.resize(n);
  rank.resize(n);
  G.resize(m);

  for (int64 i = 0; i < n; i++) {
    init_set(i);
  }

  int64 u, v, w;
  for (int64 i = 0; i < m; i++) {
    scanf("%lld %lld %lld", &u, &v, &w);
    u--; v--;
    G[i] = {u, v, w, i, false};
  }

  std::sort(G.begin(), G.end(), cmp);

  int64 count = 0;

  for (int64 i = 0; i < m; i++) {
    u = G[i].u;
    v = G[i].v;
    w = G[i].w;

    if (find_set(u) != find_set(v)) {
      union_sets(u, v);
    } else {
      G[i].ok = true;
    }
  }

  int64 sum = 0;
  for (int64 i = 0; i < m; i++) {
    if (G[i].ok) {
      sum += G[i].w;
    }
  }

  std::vector<edge> res;

  for (int64 i = 0; i < m; i++) {
    if (G[i].ok == false) {
      continue;
    }

    if (sum > s) {
      sum -= G[i].w;
    } else {
      res.push_back(G[i]);
    }
  }

  printf("%lu\n", res.size());

  for (auto e: res) {
    printf("%lld ", e.idx + 1);
  }
  printf("\n");

  return 0;
}

