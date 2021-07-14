#include <bits/stdc++.h>

double c;

double f(double x) {
  return x * x + std::sqrt(x) - c;
}

int main(void)
{
  scanf("%lf", &c);

  double l = 0, r = c;
  double m, res;

  for (int i = 0; i < 40; i++) {
    m = (l + r) / 2;

    if (f(m) >= 0) {
      res = m;
      r = m;
    } else {
      l = m;
    }
  }

  printf("%f\n", res);

  return 0;
}

