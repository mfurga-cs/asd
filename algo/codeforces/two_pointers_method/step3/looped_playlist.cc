#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, s;
  scanf("%lld %lld", &n, &s);

  std::vector<int64> a(2 * n);

  int64 sum = 0;
  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
    sum += a[i];
  }

  for (int64 i = n; i < 2 * n; i++) {
    a[i] = a[i - n];
  }

  if (s % sum == 0) {
    printf("1 %lld\n", (s / sum) * n);
    return 0;
  }

  int64 result_len = std::numeric_limits<int64>::max();
  int64 result_idx = -1;
  int64 i = 0;
  int64 cs;

  if (s >  sum) {
    int64 times = (s / sum);
    cs = sum * times;

    int64 j = 0;
    while (i < n) {
      cs += a[j % n];

      while (i < n && cs >= s) {
        if (j + times * n - i + 1 < result_len) {
          result_len = j + times * n - i + 1;
          result_idx = i;
        }
        cs -= a[i];
        i++;
      }
      j++;
    }
  } else {
    cs = 0;

    int64 j = 0;
    while (i < n) {
      cs += a[j % n];

      while (i < n && cs >= s) {
        if (j - i + 1 < result_len) {
          result_len = j - i + 1;
          result_idx = i;
        }
        cs -= a[i];
        i++;
      }
      j++;
    }
  }

  printf("%lld %lld\n", result_idx + 1, result_len);

  return 0;

}
