#include <bits/stdc++.h>

typedef long long int64;

int n, k;
std::vector<int> nums;

bool can_pack(double x) {
  int s = 0;
  for (int i = 0; i < nums.size(); i++) {
    s += int(((double)nums[i] / x));
    if (s >= k) {
      return true;
    }
  }
  return false;
}

int main(void)
{
  scanf("%d %d", &n, &k);
  nums.resize(n);

  double l = 0, r = 0, m, res = -1;
  int v;
  for (int i = 0; i < n; i++) {
    scanf("%d", &v);
    nums[i] = v;
    r = std::max(r, (double)v);
  }

  for (int i = 0; i < 100; i++ ) {
    m = (l + r) / 2;
    if (can_pack(m)) {
      res = m;
      l = m;
    } else {
      r = m;
    }
  }

  printf("%f\n", res);
  return 0;
}

