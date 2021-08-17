#include <bits/stdc++.h>
//using namespace std;

std::vector<int> parent;
std::vector<int> rank;
std::vector<int> expp;

void make_set(int x)
{
  parent[x] = x;
  rank[x] = 0;
  expp[x] = 0;
}

int find_set(int x)
{
  if (x != parent[x]) {
    int p = find_set(parent[x]);
    if (parent[x] != parent[parent[x]]) {
      expp[x] += expp[parent[x]];
    }
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

  if (rank[x] > rank[y]) {
    parent[y] = x;
    expp[y] -= expp[x];
  } else {
    parent[x] = y;
    expp[x] -= expp[y];
    if (rank[x] == rank[y]) {
      rank[y]++;
    }
  }
}

void add_exp(int x, int v)
{
  x = find_set(x);
  expp[x] += v;
}

int get_exp(int x)
{
  int p = find_set(x);
  return x != p ? expp[x] + expp[p] : expp[x];
}

/*
int main(void)
{
  int n = 5;

  parent.resize(n + 1);
  rank.resize(n + 1);
  expp.resize(n + 1);

  for (int i = 1; i <= n; i++) {
    make_set(i);
  }

  add_exp(1, 10);

  assert(get_exp(1) == 10);
  assert(get_exp(2) == 0);
  assert(get_exp(3) == 0);
  assert(get_exp(4) == 0);

  add_exp(2, 20);
  assert(get_exp(1) == 10);
  assert(get_exp(2) == 20);
  assert(get_exp(3) == 0);
  assert(get_exp(4) == 0);

  union_sets(1, 2);
  assert(get_exp(1) == 10);
  assert(get_exp(2) == 20);
  assert(get_exp(3) == 0);
  assert(get_exp(4) == 0);

  add_exp(1, 30);
  assert(get_exp(1) == 40);
  assert(get_exp(2) == 50);
  assert(get_exp(3) == 0);
  assert(get_exp(4) == 0);

  add_exp(3, 10);
  assert(get_exp(1) == 40);
  assert(get_exp(2) == 50);
  assert(get_exp(3) == 10);
  assert(get_exp(4) == 0);

  add_exp(4, 20);
  assert(get_exp(1) == 40);
  assert(get_exp(2) == 50);
  assert(get_exp(3) == 10);
  assert(get_exp(4) == 20);

  union_sets(3, 4);
  assert(get_exp(1) == 40);
  assert(get_exp(2) == 50);
  assert(get_exp(3) == 10);
  assert(get_exp(4) == 20);

  //printf("x=%d p=%d\n", 3, parent[3]);
  //printf("x=%d p=%d\n", 4, parent[4]);

  union_sets(1, 3);
  assert(get_exp(1) == 40);
  assert(get_exp(2) == 50);
  assert(get_exp(3) == 10);
  assert(get_exp(4) == 20);

  union_sets(1, 5);

  printf("x=%d exp=%d\n", 1, expp[1]);
  printf("x=%d exp=%d\n", 2, expp[2]);
  printf("x=%d exp=%d\n", 3, expp[3]);
  printf("x=%d exp=%d\n", 4, expp[4]);

  assert(get_exp(1) == 40);
  assert(get_exp(2) == 50);
  assert(get_exp(3) == 10);
  assert(get_exp(4) == 20);


  return 0;
}
*/

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  parent.resize(n + 1);
  rank.resize(n + 1);
  expp.resize(n + 1);

  for (int i = 1; i <= n; i++) {
    make_set(i);
  }

  std::string op;
  int arg1, arg2;
  char ops[30];

  for (int i = 0; i < m; i++) {
    scanf("%s", ops);
    op = ops;

    if (op == "join") {
      scanf("%d %d", &arg1, &arg2);
      union_sets(arg1, arg2);
    } else if (op == "add") {
      scanf("%d %d", &arg1, &arg2);
      add_exp(arg1, arg2);
    } else {
      scanf("%d", &arg1);
      printf("%d\n", get_exp(arg1));
    }
  }

  return 0;
}
