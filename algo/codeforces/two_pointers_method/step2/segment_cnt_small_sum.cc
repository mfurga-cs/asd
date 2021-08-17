#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, s;
  scanf("%lld %lld", &n, &s);

  std::vector<int64> a(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  int64 i = 0, j = 0;
  int64 cs = 0;
  int64 result = 0;

  while (j < n) {
    cs += a[j];
    while (cs > s) {
      cs -= a[i];
      i++;
    }
    // Dodajemy segmenty kończące się na j-tym wyrazie. Możemy dodać tylko do i bo i - 1 > s.
    result += (j - i + 1);
    j++;
  }

  printf("%lld\n", result);

  return 0;
}

