#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, r;
  scanf("%lld %lld", &n, &r);

  std::vector<int64> a(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  int64 i = 0;
  int64 result = 0;
  int64 best_i = -1;

  for (int64 j = 0; j < n; j++) {
    while (a[j] - a[i] > r) {
      best_i = i;
      i++;
    }
    result += best_i + 1;
  }

  printf("%lld\n", result);

  return 0;
}

