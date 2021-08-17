#include <bits/stdc++.h>

std::vector<int> parent;
std::vector<int> rank;

int init_set(int x)
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

  parent[x] = y;
}

int main(void)
{
  int n;
  scanf("%d", &n);

  parent.resize(n);
  rank.resize(n);

  for (int i = 0; i < n; i++) {
    init_set(i);
  }

  int pos, parent;
  for (int i = 0; i < n; i++) {
    scanf("%d", &pos);
    pos--;
    parent = find_set(pos);
    printf("%d ", parent + 1);
    union_sets(parent, (parent + 1) % n);
  }
  printf("\n");

  return 0;
}

