#include <bits/stdc++.h>

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  std::vector<int> a(n + 1);
  std::vector<int> b(m + 1);
  std::vector<int> c(n + m);

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  a[n] = std::numeric_limits<int>::max();

  for (int i = 0; i < m; i++) {
    scanf("%d", &b[i]);
  }
  b[m] = std::numeric_limits<int>::max();

  int i = 0, j = 0;

  for (int k = 0; k < n + m; k++) {
    if (a[i] <= b[j]) {
      c[k] = a[i++];
    } else {
      c[k] = b[j++];
    }
  }

  for (int k = 0; k < n + m; k++) {
    printf("%d ", c[k]);
  }
  printf("\n");

  return 0;
}

