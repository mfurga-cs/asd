#include <bits/stdc++.h>
//using namespace std;

std::vector<int> parent;
std::vector<int> rank;

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

  if (rank[x] > rank[y]) {
    parent[y] = x;
  } else {
    parent[x] = y;
    if (rank[x] == rank[y]) {
      rank[y]++;
    }
  }
}

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  parent.resize(n);
  rank.resize(n);

  for (int i = 0; i < n; i++) {
    make_set(i);
  }

  std::string op;
  int x, y;

  for (int i = 0; i < m; i++) {
    std::cin >> op >> x >> y;
    if (op == "union") {
      union_sets(x - 1, y - 1);
    } else {
      printf("%s\n", find_set(x - 1) == find_set(y - 1) ? "YES" : "NO");
    }
  }


  return 0;
}

