#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, m;
  char sbuff[100005];
  scanf("%lld %lld", &n, &m);
  scanf("%s", sbuff);
  sbuff[n] = '\0';

  std::string s(sbuff);
  int alphabet[0xff] = {0};

  char c;
  for (int64 i = 0; i < m; i++) {
    scanf(" %c", &c);
    alphabet[c] += 1;
  }

  int curr[0xff] = {0};
  int64 result = 0;

  int64 i = 0;
  for (int64 j = 0; j < n; j++) {
    curr[s[j]]++;
    while (curr[s[j]] > alphabet[s[j]]) {
      curr[s[i]]--;
      i++;
    }
    result += j - i + 1;
  }

  printf("%lld\n", result);
  return 0;
}

