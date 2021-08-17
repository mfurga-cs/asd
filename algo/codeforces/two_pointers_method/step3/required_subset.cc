#include <bits/stdc++.h>

typedef long long int64;

bool subset(const std::vector<int64> &a, int64 lo, int64 hi, int64 sum)
{
  int64 n = hi - lo + 1;
  std::vector<std::vector<bool>> dp(n);
  for (int64 i = 0; i < n; i++) {
    dp[i].assign(sum + 1, false);
  }

  for (int64 i = 0; i < n; i++) {
    dp[i][0] = true;
  }

  dp[0][a[lo]] = true;

  for (int64 i = 1; i < n; i++) {
    for (int64 s = 1; s < sum + 1; s++) {
      if (a[i + lo] > s) {
        dp[i][s] = dp[i - 1][s];
      } else {
        dp[i][s] = dp[i - 1][s] || dp[i - 1][s - a[i + lo]];
      }
    }
  }

  return dp[n - 1][sum];
}

int main(void)
{
  int64 n, s;
  scanf("%lld %lld", &n, &s);

  std::vector<int64> a(n);
  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  int64 result = std::numeric_limits<int64>::max();

  int64 good_i = -1;
  int64 i = 0;
  for (int j = 0; j < n; j++) {

    good_i = -1;
    while (subset(a, i, j, s)) {
      good_i = i;
      i++;
    }

    if (good_i != -1) {
      result = std::min(result, j - good_i + 1);
    }
  }

  if (result == std::numeric_limits<int64>::max()) {
    printf("-1\n");
    return 0;
  }
  printf("%lld\n", result);

}

