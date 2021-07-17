#include <bits/stdc++.h>

typedef long long int64;

int64 n, k;
std::vector<int64> nums;

bool is_ok(int64 s)
{
  int64 local = 0;
  int64 count = 0;

  for (int64 i = 0; i < n; i++) {
    if (nums[i] > s) {
      return false;
    }

    local += nums[i];
    if (i + 1 < n && local + nums[i + 1] > s) {
      count++;
      local = 0;
    }
  }

  return count + 1 <= k;
}

int main(void)
{
  scanf("%lld %lld", &n, &k);
  nums.resize(n);

  int64 s = 0;
  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &nums[i]);
    s += nums[i];
  }

  int64 l = 0, r = s;
  int64 m, res = 0;

  while (l <= r) {
    m = (l + r) / 2;
    if (is_ok(m)) {
      res = m;
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  printf("%lld\n", res);

  return 0;
}
