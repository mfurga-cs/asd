#include <bits/stdc++.h>

std::vector<int> parent;
std::vector<int> rank;
std::vector<int> sum;

void init_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
  sum[x] = 0;
}

int find_set(int x)
{
  if (parent[x] != x) {
    int p = find_set(parent[x]);
    sum[x] += sum[parent[x]];
    parent[x] = p;
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

  parent[x] = y;
  sum[x] = 1;

/*
  if (rank[x] > rank[y]) {
    parent[y] = x;
    sum[y] = 1;
  } else {
    parent[x] = y;
    sum[x] = 1;
    if (rank[x] == rank[y]) {
      rank[y]++;
    }
  }
*/

}


int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  parent.resize(n);
  rank.resize(n);
  sum.resize(n);

  for (int i = 0; i < n; i++) {
    init_set(i);
  }

  int op, x, y;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d", &x, &y);
      union_sets(x - 1, y - 1);
    } else {
      scanf("%d", &x);
      find_set(x - 1);
      printf("%d\n", sum[x - 1]);
    }
  }

  return 0;
}

