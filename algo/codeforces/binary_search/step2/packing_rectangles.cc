#include <bits/stdc++.h>

typedef long long int64;

int64 n, h, w;

bool can_pack(int64 x) {
  return (x / w) * (x / h) >= n;
}

int64 binsearch(int64 l, int64 r)
{
  int64 m, res = -1;
  while (l <= r) {
    m = l + (r - l) / 2;
    if (can_pack(m)) {
      res = m;
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return res;
}

int main(void)
{
  scanf("%lld %lld %lld", &w, &h, &n);
  int64 l = 0LL, r = 1LL;
  while (!can_pack(r)) {
    r *= 2LL;
  }
  printf("%lld\n", binsearch(l, r));
  return 0;
}

