#!/usr/bin/env python3

def steal(towers, height):
  towers = [sorted(t, reverse=True) for t in towers]
  S = [sum(t) for t in towers]

  max_tower = max(S)
  my_tower = height

  

