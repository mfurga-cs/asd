#include <bits/stdc++.h>

std::string t;
std::string p;
std::vector<int> perm;

bool is_ok(int k) {
  std::string c = t;
  for (int i = 0; i < k; i++) {
    c[perm[i]] = '\0';
  }
  int j = 0;
  for (int i = 0; i < t.size(); i++) {
    if (c[i] == p[j]) {
      j++;
      if (j == p.size()) {
        return true;
      }
    }
  }
  return false;
}

int main(void)
{
  std::cin >> t;
  std::cin >> p;
  perm.resize(t.size());

  int v;
  for (size_t i = 0; i < t.size(); i++) {
    scanf("%d", &v);
    perm[i] = v - 1;
  }

  int l = 0, r = t.size(), m;
  int res = 0;

  while (l <= r) {
    m = (l + r) / 2;
    if (is_ok(m)) {
      res = m;
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  printf("%d\n", res);

  return 0;
}

