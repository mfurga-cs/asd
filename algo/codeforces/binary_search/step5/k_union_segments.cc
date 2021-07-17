#include <bits/stdc++.h>
using namespace std;

typedef long long int64;

int64 n, k;
vector<pair<int64, int64>> segs;

bool is_ok(int64 x)
{
  int64 pos = 0;
  for (int64 i = 0; i < n; i++) {
    if (segs[i].first < x) {
      pos += min(segs[i].second + 1, x) - segs[i].first;
    }
  }
  return (pos + 1) <= k;
}

int main(void)
{
  scanf("%lld %lld", &n, &k);
  segs.resize(n);
  k++;

  int64 l = numeric_limits<int64>::max();
  int64 r = numeric_limits<int64>::min();

  int64 b, e;
  for (int64 i = 0; i < n; i++) {
    scanf("%lld %lld", &b, &e);
    segs[i] = make_pair(b, e);
    l = min(l, b);
    r = max(r, e);
  }

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


