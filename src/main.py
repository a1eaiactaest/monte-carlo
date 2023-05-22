#!/usr/bin/env python3

import os
import sys
import numpy as np


def estimate(n: int, seed:int = None) -> float:
  np.random.seed(seed if seed else 1337)
  x = np.random.random(n)
  y = np.random.random(n)
  s = np.sqrt(x**2 + y**2)
  included = s[s <= 1] # points inside circle
  return 4 * len(included) / n

def main():
  print(estimate(100000000))

if __name__ == "__main__":
  main()