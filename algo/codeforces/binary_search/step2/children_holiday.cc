/*
  Liczymy ile balonów można napomować dana osoba w czasie t.

*/
#include <bits/stdc++.h>

typedef long long int64;

struct assist_t {
  int64 time;
  int64 strength;
  int64 rest;
};

std::vector<assist_t> assists;
int m, n;

int64 balloons_one_assist(assist_t assist, int64 time) {
  int64 balloons = 0;
  int64 times = 0;
  while (time - assist.time >= 0) {
    if (assist.strength > 0 && times == assist.strength) {
      time -= assist.rest;
      times = 0;
      continue;
    }
    time -= assist.time;
    balloons++;
    times++;
  }
  return balloons;
}

int64 f(int64 time) {
  int64 s = 0;
  for (int i = 0; i < assists.size(); i++) {
    s += balloons_one_assist(assists[i], time);
  }
  return s;
}

int main(void)
{
  scanf("%d %d", &m, &n);
  assists.resize(n);

  int64 time, strength, rest;
  for (int i = 0; i < n; i++) {
    scanf("%lld %lld %lld", &time, &strength, &rest);
    assists[i].time = time;
    assists[i].strength = strength;
    assists[i].rest = rest;
  }

  int64 r = 1;
  while (f(r) <= m) {
    r *= 2;
  }
  int64 l = 0, res = LONG_LONG_MAX;

  while (l <= r) {
    time = (l + r) / 2;
    if (f(time) >= m) {
      res = time;
      r = time - 1;
    } else {
      l = time + 1;
    }
  }

  printf("%lld\n", res);
  int64 count = 0;
  int64 one;
  for (int i = 0; i < assists.size(); i++) {
    one = balloons_one_assist(assists[i], res);
    if (one + count >= m) {
      printf("%lld ", m - count);
      count = m;
    } else {
      printf("%lld ", one);
      count += one;
    }
  }
  printf("\n");

  return 0;
}

