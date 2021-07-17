#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<pair<int, double>>> G;

bool dag_shortest_path(double x, stack<int> &path)
{
  vector<double> dist(n, numeric_limits<double>::max());
  vector<int> parent(n, -1);
  dist[0] = 0L;

  int v;
  double w;
  for (int u = 0; u < n; u++) {
    if (dist[u] == numeric_limits<double>::max()) {
      continue;
    }

    for (auto p: G[u]) {
      v = p.first;
      w = p.second - x;

      if (dist[v] > dist[u] + w) {
        dist[v] = dist[u] + w;
        parent[v] = u;
      }
    }
  }

  v = n - 1;
  while (v != -1) {
    path.push(v + 1);
    v = parent[v];
  }

  return dist[n - 1] <= 0;
}

int main(void)
{
  scanf("%d %d", &n, &m);
  G.resize(n);

  double l = numeric_limits<double>::max();
  double r = numeric_limits<double>::lowest();

  int u, v, w;
  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", &u, &v, &w);
    G[u - 1].push_back(make_pair(v - 1, static_cast<double>(w)));
    l = min(l, static_cast<double>(w));
    r = max(r, static_cast<double>(w));
  }

  //printf("l=%f r=%f\n", l, r);

  stack<int> path_best;
  stack<int> path_local;
  double m;

  l -= 1L;
  r += 1L;

  for (int i = 0; i < 40; i++) {
    path_local = stack<int>();
    m = (l + r) / 2;
    //printf("checking m=%f\n", m);
    if (dag_shortest_path(m, path_local)) {
      path_best = path_local;
      r = m;
    } else {
      l = m;
    }
  }

  printf("%lu\n", path_best.size() - 1);
  while (!path_best.empty()) {
    printf("%d ", path_best.top());
    path_best.pop();
  }
  printf("\n");

  return 0;
}

