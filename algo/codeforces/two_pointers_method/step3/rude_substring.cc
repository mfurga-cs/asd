#include <bits/stdc++.h>

typedef long long int64;

int main(void)
{
  int64 n, c;
  char sbuff[(int)1e6 + 5];
  scanf("%lld %lld", &n, &c);

  scanf("%s", sbuff);
  sbuff[n] = '\0';

  std::string s(sbuff);

  int64 ac = 0;
  int64 bc = 0;
  int64 i = 0;
  int64 rc = 0;
  int64 result = 0;

  for (int64 j = 0; j < n; j++) {
    if (s[j] == 'a') {
      ac++;
    }

    if (s[j] == 'b' ) {
      bc++;
      rc += ac;
    }

    while (rc > c) {
      if (s[i] == 'a') {
        ac--;
        rc -= bc;
      }
      if (s[i] == 'b') {
        bc--;
      }
      i++;
    }

    result = std::max(result, j - i + 1);
  }

  printf("%lld\n", result);

  return 0;
}

