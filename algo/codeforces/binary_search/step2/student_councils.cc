#include <bits/stdc++.h>

long long k, n;
std::vector<long long> nums;

bool is_ok(long long m)
{
  long long s = m * k;
  for (long long i = 0; i < n; i++) {
    s -= std::min(nums[i], m);
  }
  return s <= 0;
}

int main(void)
{
  scanf("%lld %lld", &k, &n);
  nums.resize(n);

  long long v;
  long long s = 0;
  for (int i = 0; i < n; i++) {
    scanf("%lld", &v);
    nums[i] = v;
    s += v;
  }

  long long l = 1, r = s, m;
  long long res = 0;

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

