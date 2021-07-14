#include <bits/stdc++.h>

int main(void)
{
  int n, x, y;
  scanf("%d %d %d", &n, &x, &y);

  int time = 0;
  time += std::min(x, y);
  n -= 1;

  int l = 0, r = n, m;
  int time_loc = std::numeric_limits<int>::max();

  while (l <= r) {
    m = (l + r) / 2;
    time_loc = std::min(time_loc, std::max(x * m, y * (n - m)));
    if (x * m > y * (n - m)) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }

  printf("%d\n", time + time_loc);

  return 0;
}

