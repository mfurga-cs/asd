#include <bits/stdc++.h>
//using namespace std;

std::vector<int> parent;
std::vector<int> rank;
std::vector<int> min;
std::vector<int> max;
std::vector<int> cnt;

void make_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
  max[x] = x;
  min[x] = x;
  cnt[x] = 1;
}

int find_set(int x)
{ if (x != parent[x]) {
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
    cnt[x] += cnt[y];
    min[x] = std::min(min[x], min[y]);
    max[x] = std::max(max[x], max[y]);
  } else {
    parent[x] = y;
    cnt[y] += cnt[x];
    min[y] = std::min(min[y], min[x]);
    max[y] = std::max(max[y], max[x]);
    if (rank[x] == rank[y]) {
      rank[y]++;
    }
  }
}

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  parent.resize(n + 1);
  rank.resize(n + 1);
  min.resize(n + 1);
  max.resize(n + 1);
  cnt.resize(n + 1);

  for (int i = 0; i <= n; i++) {
    make_set(i);
  }

  std::string op;
  int x, y;
  char ops[30];

  for (int i = 0; i < m; i++) {
    scanf("%s", ops);
    op = ops;

    if (op == "union") {
      scanf("%d %d", &x, &y);
      union_sets(x, y);
    } else {
      scanf("%d", &x);
      x = find_set(x);
      printf("%d %d %d\n", min[x], max[x], cnt[x]);
    }
  }


  return 0;
}

