#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, s;
  scanf("%lld %lld", &n, &s);

  std::vector<int64> a(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  int64 i = 0, j = 0;
  int64 cs = 0;
  int64 result = std::numeric_limits<int64>::max();

  while (j < n) {
    cs += a[j];
    while (cs >= s) {
      result = std::min(result, j - i + 1);
      cs -= a[i];
      i++;
    }
    j++;
  }

  if (result == std::numeric_limits<int64>::max()) {
    printf("-1\n");
  } else {
    printf("%lld\n", result);
  }

  return 0;
}

