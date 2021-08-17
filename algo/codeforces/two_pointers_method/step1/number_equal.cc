#include <bits/stdc++.h>

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  std::vector<int> a(n);
  std::vector<int> b(m);

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }

  for (int i = 0; i < m; i++) {
    scanf("%d", &b[i]);
  }

  int i = 0, j = 0;
  long long result = 0;
  long long ac = 1, bc = 1;

  while (1) {

    if (a[i] == b[j]) {
      ac = 1;
      while (i + 1 < n && a[i] == a[i + 1]) {
        i++;
        ac++;
      }
      if (i + 1 < n) {
        i++;
      }

      bc = 1;
      while (j + 1 < m && b[j] == b[j + 1]) {
        j++;
        bc++;
      }
      if (j + 1 < m) {
        j++;
      }
      result += ac * bc;

      if (i + 1 == n && j + 1 == m) {
        break;
      }

      continue;
    }

    if (i + 1 == n && j + 1 == m) {
      break;
    }

    if (i + 1 == n || (j + 1 < m && a[i] > b[j])) {
      j++;
      continue;
    }

    if (j + 1 == m || (i + 1 < n && a[i] < b[j])) {
      i++;
      continue;
    }
  }

  printf("%lld\n", result);

  return 0;
}

