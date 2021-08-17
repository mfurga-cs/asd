#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, s;
  scanf("%lld %lld", &n, &s);

  std::vector<int64> w(n);
  std::vector<int64> c(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &w[i]);
  }

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &c[i]);
  }

  int64 result = -1LL;
  int64 i = 0;
  int64 ws = 0, cs = 0;

  for (int64 j = 0; j < n; j++) {
    ws += w[j];
    cs += c[j];

    while (ws > s) {
      ws -= w[i];
      cs -= c[i];
      i++;
    }

    result = std::max(result, cs);
  }

  printf("%lld\n", result);

  return 0;

}
