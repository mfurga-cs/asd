#include <bits/stdc++.h>

typedef long long int64;

int64 n, k;

bool is_ok(int64 x)
{
  int64 count = 0;

  for (int64 i = 1; i <= n; i++) {
    if (i * i < x) {
      count++;
    }

    if (x / i > n || (x % i > 0 && x / i == n)) {
      count += 2 * (n - i);
    } else {
      if (x % i == 0) {
        count += std::max(2 * (x / i - i - 1), 0LL);
      } else {
        count += std::max(2 * (x / i - i), 0LL);
      }
    }

  }
  //return count + 1;
  return (count + 1) <= k;
}

bool is_good(int64 x)
{
  for (int64 i = 1; i <= n; i++) {
    if (x % i == 0) {
      if ((x / i) <= n) {
        return true;
      }
    }
  }
  return false;
}

void tests()
{
  n = 4;
  assert(is_ok(12) == 14);
  assert(is_ok(1) == 1);
  assert(is_ok(2) == 2);
  assert(is_ok(3) == 4);
  assert(is_ok(4) == 6);
  assert(is_ok(16) == 16);
  assert(is_ok(6) == 9);
  assert(is_ok(8) == 11);
  assert(is_ok(9) == 13);

  n = 5;
  assert(is_ok(1) == 1);
  assert(is_ok(2) == 2);
  assert(is_ok(3) == 4);
  assert(is_ok(4) == 6);
  assert(is_ok(9) == 15);

  assert(is_ok(10) == 16);

}

int main(void)
{
  scanf("%lld %lld", &n, &k);

  int64 l = 1, r = n * n;
  int64 m, res;

  //tests();

  while (l <= r) {
    m = (l + r) / 2;

    if (!is_good(m)) {
      r++;
    }

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

