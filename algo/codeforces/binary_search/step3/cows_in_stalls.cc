#include <bits/stdc++.h>

typedef long long int64;

int64 n, k;
std::vector<int64> stalls;

bool is_ok(int64 d)
{
  int64 count = 1;
  int64 curr = 0;

  for (int64 i = 1; i < n; i++) {
    curr += stalls[i] - stalls[i - 1];
    if (curr >= d) {
      count++;
      curr = 0;
    }
  }

  return count >= k;
}

int main(void)
{
  scanf("%lld %lld", &n, &k);
  stalls.resize(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &stalls[i]);
  }

  int64 l = 1, r = stalls[n - 1] - stalls[0];
  int64 m, res;

  while (l <= r) {
    m = (l + r) / 2;
    if (is_ok(m)) {
      res = m;
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  printf("%lld\n", res);

  return 0;
}

