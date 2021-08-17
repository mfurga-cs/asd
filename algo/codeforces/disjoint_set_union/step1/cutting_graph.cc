#include <bits/stdc++.h>
//using namespace std;

std::vector<int> parent;
std::vector<int> rank;
std::vector<std::vector<int>> G;

void make_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
}

int find_set(int x)
{
  if (x != parent[x]) {
    parent[x] = find_set(parent[x]);
  }
  return parent[x];
}

void union_sets(int x, int y)
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

void remove_edge(int u, int v)
{
  G[u].erase(std::remove(G[u].begin(), G[u].end(), v), G[u].end());
  G[v].erase(std::remove(G[v].begin(), G[v].end(), u), G[v].end());
}

struct input_row {
  int op;
  int u;
  int v;
};

int main(void)
{
  int n, m, k;
  scanf("%d %d %d", &n, &m, &k);

  G.resize(n);
  parent.resize(n);
  rank.resize(n);

  for (int i = 0; i < n; i++) {
    make_set(i);
  }

  int u, v;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &u, &v);
    u--; v--;
    G[u].push_back(v);
    G[v].push_back(u);
  }

  std::vector<input_row> in(k);
  char op[30];

  std::string asdf;

  for (int i = 0; i < k; i++) {
    scanf("%3s", op);
    scanf("%d %d", &u, &v);
    op[3] = '\0';
    asdf =op;
    u--; v--;

    if (asdf == "cut") {
      remove_edge(u, v);
      in[i].op = 0;
    } else {
      in[i].op = 1;
    }
    in[i].u = u;
    in[i].v = v;
  }

  for (int u = 0; u < n; u++) {
    for (auto v: G[u]) {
      union_sets(u, v);
    }
  }

  std::stack<std::string> resp;

  for (int i = k - 1; i >= 0; i--) {
    if (in[i].op == 0) {
      // cut
      union_sets(in[i].u, in[i].v);
    } else {
      if (find_set(in[i].u) == find_set(in[i].v)) {
        resp.push(std::string("YES"));
      } else {
        resp.push(std::string("NO"));
      }
    }
  }

  while (!resp.empty()) {
    printf("%s\n", resp.top().c_str());
    resp.pop();
  }

  return 0;

}
