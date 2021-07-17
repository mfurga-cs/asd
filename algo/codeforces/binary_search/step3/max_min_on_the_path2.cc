#include <bits/stdc++.h>

typedef int int64;
typedef std::vector<std::vector<std::pair<int64, int64>>> graph_t;

int64 n, m, d;
graph_t G;

void bfs(int64 max)
{
  std::queue<std::pair<int64, int64>> q;

  std::vector<std::vector<int64>> distance(n);
  std::vector<std::vector<std::pair<int64, int64>>> parent(n);

  for (int64 i = 0; i < n; i++) {
    distance[i].assign(max + 1, std::numeric_limits<int64>::max());
    parent[i].assign(max + 1, std::make_pair(-1, -1));
  }

  q.push(std::make_pair(0, 0));
  distance[0][0] = 0;

  std::pair<int64, int64> p;
  int64 u, v, w, m;

  int64 min = std::numeric_limits<int64>::max();

  while (!q.empty()) {
    p = q.front(); q.pop();
    u = p.first;
    m = p.second;

    for (auto p: G[u]) {
      v = p.first;
      w = p.second;

      if (distance[v][std::max(m, w)] == std::numeric_limits<int64>::max()) {
        distance[v][std::max(m, w)] = distance[u][m] + 1;
        parent[v][std::max(m, w)] = std::make_pair(u, m);
        q.push(std::make_pair(v, std::max(m, w)));

        if (v == n - 1) {
          if (distance[v][std::max(m, w)] <= d) {
            min = std::min(min, std::max(m, w));
          }
          //printf("dist: %d, max: %d\n", distance[v][std::max(m, w)], std::max(m, w));
        }
      }
    }
  }

  if (min == std::numeric_limits<int64>::max()) {
    printf("-1\n");
    return;
  }

  printf("%d\n", distance[n - 1][min]);

  std::stack<int64> s;

  v = n - 1;
  m = min;
  std::pair<int64, int64> t;
  while (v != -1) {
    s.push(v + 1);
    t = parent[v][m];
    v = t.first;
    m = t.second;
  }

  while (!s.empty()) {
    printf("%d ", s.top());
    s.pop();
  }

  printf("\n");
}

int main(void)
{
  scanf("%d %d %d", &n, &m, &d);
  G.resize(n);

  int64 max = std::numeric_limits<int64>::min();

  int64 u, v, w;
  for (int64 i = 0; i < m; i++) {
    scanf("%d %d %d", &u, &v, &w);
    u--;
    v--;
    G[u].push_back(std::make_pair(v, w));

    max = std::max(max, w);
  }

  bfs(max);

  return 0;
}

