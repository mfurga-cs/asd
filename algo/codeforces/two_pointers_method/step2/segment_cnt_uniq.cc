#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, k;
  scanf("%lld %lld", &n, &k);

  std::vector<int64> a(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  int64 i = 0, j = 0;
  int64 result = 0;

  std::unordered_map<int64, int64> inside;

  while (j < n) {
    if (inside.count(a[j]) == 0) {
      inside[a[j]] = 1;
    } else {
      inside[a[j]] += 1;
    }

    while (inside.size() > k) {
      if (inside.count(a[i]) == 1 && inside[a[i]] == 1) {
        inside.erase(a[i]);
      } else {
        inside[a[i]] -= 1;
      }
      i++;
    }

    result += (j - i + 1);
    j++;
  }

  printf("%lld\n", result);

  return 0;
}

