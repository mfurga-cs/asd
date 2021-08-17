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

  if (x == y) {
    return;
  }

  if (x == 0 || y == 0) {
    if (x == 0) {
      parent[y] = x;
      rank[x]++;
    } else {
      parent[x] = y;
      rank[y]++;
    }
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

void falling(std::vector<int> &times, int p, int t)
{
  for (int i = 0; i < parent.size(); i++) {
    if (parent[i] == p && times[i] == -1) {
      times[i] = t;
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

  std::vector<std::pair<int, int>> monkeys(n);
  std::vector<std::pair<int, int>> releases(m);

  int monkey1, monkey2;
  for (int i = 0; i < n; i++) {
    scanf("%d %d", &monkey1, &monkey2);
    monkeys[i].first = monkey1 - 1;
    monkeys[i].second = monkey2 - 1;
  }

  int hand;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &monkey1, &hand);
    releases[i].first = monkey1 - 1;
    releases[i].second = hand;
  }

  std::vector<std::pair<int, int>> end = monkeys;
  for (int i = 0; i < m; i++) {
    monkey1 = releases[i].first;
    hand = releases[i].second;

    if (hand == 1) {
      end[monkey1].first = -2;
    } else {
      end[monkey1].second = -2;
    }
  }

  for (int i = 0; i < n; i++) {
    //printf("%d: l=%d r=%d\n", i, end[i].first, end[i].second);
    if (end[i].first != -2) {
      union_sets(i, end[i].first);
    }
    if (end[i].second != -2) {
      union_sets(i, end[i].second);
    }
  }

  std::vector<int> times(n, -1);

  int parent1, parent2;
  for (int i = m - 1; i >= 0; i--) {
    monkey1 = releases[i].first;
    hand = releases[i].second;

    if (hand == 1) {
      monkey2 = monkeys[monkey1].first;
    } else {
      monkey2 = monkeys[monkey1].second;
    }

    parent1 = find_set(monkey1);
    parent2 = find_set(monkey2);

    if ((parent1 == 0 || parent2 == 0) && parent1 != parent2) {
      if (parent1 == 0) {
        falling(times, parent2, i);
      }

      if (parent2 == 0) {
        falling(times, parent1, i);
      }
    }

    union_sets(parent1, parent2);
  }

  for (int i = 0; i < n; i++) {
    printf("%d\n", times[i]);
  }

  return 0;

}


