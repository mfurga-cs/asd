#include <bits/stdc++.h>

std::vector<int> parent;
std::vector<int> rank;

void init_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
}

int find_set(int x)
{
  if (parent[x] != x) {
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

void union_merge_sets(std::set<int> &nojoined, int x, int y)
{
  int i = x;
  while (*nojoined.lower_bound(i) < y) {
    i = *nojoined.lower_bound(i);
    nojoined.erase(i);
    union_sets(i, i + 1);
  }
}

int main(void)
{
  int n, q;
  scanf("%d %d", &n, &q);

  parent.resize(n);
  rank.resize(n);

  std::set<int> nojoined;

  for (int i = 0; i < n; i++) {
    init_set(i);
    nojoined.insert(i);
  }

  int op, x, y;
  for (int i = 0; i < q; i++) {
    scanf("%d %d %d", &op, &x, &y);
    x--; y--;

    if (op == 1) {
      union_sets(x, y);
    } else if (op == 2) {
      union_merge_sets(nojoined, x, y);
    } else {
      printf("%s\n", find_set(x) == find_set(y) ? "YES" : "NO");
    }
  }

  return 0;
}

