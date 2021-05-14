#!/usr/bin/env python3

# f(i) - max zysk z cięć i pierwszych drzew
#
# f(i) = 0                                   , i < 0
# f(i) = max{ f(i - 2) + z(i), f(i - 1) }    , wpp
#
def trees(arr, i):
  if i < 0:
    return 0
  return max(trees(arr, i - 2) + arr[i], trees(arr, i - 1))


