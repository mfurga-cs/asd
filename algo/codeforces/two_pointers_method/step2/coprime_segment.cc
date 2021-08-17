#include <bits/stdc++.h>

typedef long long int64;

struct GCDS {
  std::stack<int64> _stack;
  std::stack<int64> _gcd;

  void push(int64 x) {
    if (_stack.empty()) {
      _stack.push(x);
      _gcd.push(x);
      return;
    }
    _stack.push(x);
    _gcd.push(std::gcd(_gcd.top(), x));
  }

  int64 pop() {
    int64 x = _stack.top();
    _stack.pop();
    _gcd.pop();
    return x;
  }

  int64 gcd() {
    return _gcd.top();
  }

  bool empty() {
    return _stack.empty();
  }

  int64 size() {
    return _stack.size();
  }
};

struct GCDQ {
  GCDS sl;
  GCDS sr;

  int64 pop() {
    if (sl.empty()) {
      while (!sr.empty()) {
        sl.push(sr.pop());
      }
    }
    return sl.pop();
  }

  void push(int64 x) {
    sr.push(x);
  }

  int64 gcd() {
    if (sl.empty()) {
      return sr.gcd();
    }

    if (sr.empty()) {
      return sl.gcd();
    }

    return std::gcd(sl.gcd(), sr.gcd());
  }

  bool empty() {
    return sl.empty() && sr.empty();
  }

  int64 size() {
    return sl.size() + sr.size();
  }
};

int main(void)
{
  int64 n;
  scanf("%lld", &n);

  std::vector<int64> a(n);

  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  int64 i = 0, j = 0;
  GCDQ queue;
  int64 result = std::numeric_limits<int64>::max();

  for (j = 0; j < n; j++) {
    if (a[j] == 1) {
      printf("1\n");
      return 0;
    }
    queue.push(a[j]);

    while (queue.gcd() == 1) {
      result = std::min(result, j - i + 1);
      queue.pop();
      i++;
    }
  }

  if (result == std::numeric_limits<int64>::max()) {
    printf("-1\n");
    return 0;
  }

  printf("%lld\n", result);

  return 0;
}
