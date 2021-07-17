#include <bits/stdc++.h>

typedef std::pair<double, double> interval_t;

int n;
double POS_MIN;
double POS_MAX;
std::vector<double> pos;
std::vector<double> speed;

bool intersection(interval_t &a, interval_t &b)
{
  if (a.second < b.first || b.second < a.first) {
    return false;
  }
  a.first = static_cast<double>(std::max(a.first, b.first));
  a.second = static_cast<double>(std::min(a.second, b.second));
  return true;
}

bool is_ok(double time)
{
  interval_t a;
  a.first = POS_MIN;
  a.second = POS_MAX;
  interval_t b;

  for (int i = 0; i < n; i++) {
    b.first = pos[i] - speed[i] * time;
    b.second = pos[i] + speed[i] * time;
    if (!intersection(a, b)) {
      return false;
    }
  }

  return true;
}

int main(void)
{
  scanf("%d", &n);
  pos.resize(n);
  speed.resize(n);

  double s, p;
  for (int i = 0; i < n; i++) {
    scanf("%lf %lf", &p, &s);
    pos[i] = p;
    speed[i] = s;

    if (i == 0) {
      POS_MIN = pos[0];
      POS_MAX = pos[0];
    }

    POS_MIN = std::min(POS_MIN, p);
    POS_MAX = std::max(POS_MAX, p);
  }

  double l = 0, r = 1;
  double m, res;

  while (!is_ok(r)) {
    r *= 2;
  }

  for (int i = 0; i < 20; i++) {
    m = (l + r) / 2;
    if (is_ok(m)) {
      res = m;
      r = m;
    } else {
      l = m;
    }
  }

  printf("%f\n", res);

  return 0;
}

