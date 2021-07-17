#include <bits/stdc++.h>

typedef int int64;
typedef std::vector<std::vector<std::pair<int64, int64>>> graph_t;

int64 n, m, d;
graph_t G;

bool bfs(int64 max, std::stack<int64> &path)
{
  std::queue<int64> q;
  std::vector<int64> distance(n, std::numeric_limits<int64>::max());
  std::vector<int64> parent(n, -1);

  q.push(0);
  distance[0] = 0;

  int64 u, v, w;
  while (!q.empty()) {
    u = q.front(); q.pop();

    for (auto p: G[u]) {
      v = p.first;
      w = p.second;
      if (w <= max && distance[v] == std::numeric_limits<int64>::max()) {
        distance[v] = distance[u] + 1;
        parent[v] = u;
        q.push(v);

        if (v == n - 1) {
          goto done;
        }
      }
    }
  }

  done:

  u = n - 1;
  while (u != -1) {
    path.push(u + 1);
    u = parent[u];
  }

  return distance[n - 1] <= d;
}

int main(void)
{
  scanf("%d %d %d", &n, &m, &d);
  G.resize(n);

  int64 l = std::numeric_limits<int64>::max();
  int64 r = std::numeric_limits<int64>::min();

  int64 u, v, w;
  for (int64 i = 0; i < m; i++) {
    scanf("%d %d %d", &u, &v, &w);
    u--;
    v--;
    G[u].push_back(std::make_pair(v, w));

    l = std::min(l, w);
    r = std::max(r, w);
  }

  std::stack<int64> path;
  std::stack<int64> res;
  int64 m;

  while (l <= r) {
    m = (l + r) / 2;
    path = std::stack<int64>();
    if (bfs(m, path)) {
      res = path;
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  printf("%ld\n", res.size() - 1);
  while (!res.empty()) {
    printf("%d ", res.top());
    res.pop();
  }
  printf("\n");

  return 0;
}

