#include <bits/stdc++.h>

#define BREAD 0
#define SAUSAGE 1
#define CHEESE 2

typedef long long int64;

int64 kitchen[3];
int64 need[3];
int64 shop[3];
int64 money;

bool is_ok(int64 n)
{
  int64 money_have = money;

  money_have -= -1 * std::min(kitchen[BREAD] - (need[BREAD] * n), 0LL) * shop[BREAD];
  money_have -= -1 * std::min(kitchen[SAUSAGE] - (need[SAUSAGE] * n), 0LL) * shop[SAUSAGE];
  money_have -= -1 * std::min(kitchen[CHEESE] - (need[CHEESE] * n), 0LL) * shop[CHEESE];

  return money_have >= 0;
}

int main(void)
{
  std::string recipe;
  std::cin >> recipe;
  scanf("%lld %lld %lld", kitchen, kitchen + 1, kitchen + 2);
  scanf("%lld %lld %lld", shop, shop + 1, shop + 2);
  scanf("%lld", &money);

  for (int i = 0; i < recipe.size(); i++) {
    switch (recipe[i]) {
      case 'B':
        need[BREAD] += 1;
        break;
      case 'S':
        need[SAUSAGE] += 1;
        break;
      case 'C':
        need[CHEESE] += 1;
        break;
    }
  }

  int64 r = 1LL;
  while (is_ok(r)) {
    r *= 2LL;
  }

  int64 l = 1, m, res = 0;

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

