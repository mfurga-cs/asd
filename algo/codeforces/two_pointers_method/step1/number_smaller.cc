#include <bits/stdc++.h>

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  std::vector<int> a(n + 1);
  std::vector<int> b(m);

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  a[n] = std::numeric_limits<int>::max();

  for (int i = 0; i < m; i++) {
    scanf("%d", &b[i]);
  }

  int j = 0;
  int count = 0;

  for (int i = 0; i < m; i++) {
    while (a[j] < b[i]) {
      j++;
      count++;
    }
    printf("%d ", count);
  }

  printf("\n");

  return 0;
}

