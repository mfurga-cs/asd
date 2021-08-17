#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, m, s, aw, bw;
  scanf("%lld %lld %lld %lld %lld", &n, &m, &s, &aw, &bw);

  std::vector<int64> a(n);
  std::vector<int64> b(m);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  for (int64 i = 0; i < m; i++) {
    scanf("%lld", &b[i]);
  }

  std::sort(a.begin(), a.end(), std::greater<int64>());
  std::sort(b.begin(), b.end(), std::greater<int64>());

  std::vector<int64> ap(n + 1);
  std::vector<int64> as(n + 1);

  std::vector<int64> bp(m + 1);
  std::vector<int64> bs(m + 1);

  ap[0] = 0;
  as[0] = 0;
  for (int64 i = 0; i < n; i++) {
    ap[i + 1] = a[i] + ap[i];
    as[i + 1] = aw + as[i];
  }

  bp[0] = 0;
  bs[0] = 0;
  for (int64 i = 0; i < m; i++) {
    bp[i + 1] = b[i] + bp[i];
    bs[i + 1] = bw + bs[i];
  }

  int64 i = n;
  int64 j = 0;
  int64 result = 0;

  while (j < m + 1) {
    while (as[i] + bs[j] > s) {
      if (i == 0) {
        goto done;
      }
      i--;
    }
    result = std::max(result, ap[i] + bp[j]);
    j++;
  }

  done:
  printf("%lld\n", result);

  return 0;
}



