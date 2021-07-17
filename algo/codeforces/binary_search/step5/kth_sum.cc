#include <bits/stdc++.h>
using namespace std;

typedef long long int64;

int64 n, k;
vector<int64> a;
vector<int64> b;

int64 less_than(int64 x, bool &exists)
{
  int64 l = 0, r = n - 1;
  int64 m, res = -1;
  while (l <= r) {
    m = (l + r) / 2;
    if (b[m] < x) {
      res = m;
      l = m + 1;
    } else {
      if (b[m] == x) {
        exists = true;
      }
      r = m - 1;
    }
  }
  return res + 1;
}

bool is_ok(int64 x, bool &exists)
{
  int64 count = 0;
  for (int64 i = 0; i < n; i++) {
    count += less_than(x - a[i], exists);
  }
  return count + 1 <= k;
}

int main(void)
{
  scanf("%lld %lld", &n, &k);
  a.resize(n);
  b.resize(n);

  int64 min_a = numeric_limits<int64>::max();
  int64 max_a = numeric_limits<int64>::min();
  int64 min_b = numeric_limits<int64>::max();
  int64 max_b = numeric_limits<int64>::min();

  for (int i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
    min_a = min(min_a, a[i]);
    max_a = max(max_a, a[i]);
  }

  for (int i = 0; i < n; i++) {
    scanf("%lld", &b[i]);
    min_b = min(min_b, b[i]);
    max_b = max(max_b, b[i]);
  }

  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  int64 l = min(min_a, min_b);
  int64 r = max_a + max_b;
  int64 m, res;
  bool exists, ok;

  while (l <= r) {
    exists = false;
    m = (l + r) / 2;
    ok = is_ok(m, exists);

    if (!exists) {
      r++;
    }

    if (ok) {
      res = m;
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  printf("%lld\n", res);

  return 0;
}


