#include <bits/stdc++.h>

std::vector<int> parent;
std::vector<int> rank;
std::vector<int> max;

int init_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
  max[x] = x;
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
    max[x] = std::max(max[x], max[y]);
  } else {
    parent[x] = y;
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
  max.resize(n + 1);

  for (int i = 0; i <= n; i++) {
    init_set(i);
  }

  char op;
  int pos, parent;

  for (int i = 0; i < m; i++) {
    scanf(" %c %d", &op, &pos);

    pos--;
    if (op == '-') {
      union_sets(pos, pos + 1);
    } else {
      parent = find_set(pos);

      if (max[parent] == n) {
        printf("-1\n");
      } else {
        printf("%d\n", max[parent] + 1);
      }
    }
  }

  return 0;
}

