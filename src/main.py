#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt
import tqdm

SEED = 1337

def estimate(n: int, seed:int = None) -> float:
  np.random.seed(seed if seed else SEED)
  x = np.random.random(n)
  y = np.random.random(n)
  s = np.sqrt(x**2 + y**2)
  included = s[s <= 1] # points inside circle
  return 4 * len(included) / n

def plot_estimates(n: int) -> None:
  x = list(range(1, n))
  y = [estimate(iterations) for iterations in tqdm.tqdm(x)]
  print(f"Last π estimate {y[-1]}")
  plt.plot(x,y)
  plt.xlabel('iterations')
  plt.ylabel('estimate')
  plt.axhline(y=y[-1], color='r', label='last π estimate')
  plt.axhline(y=np.pi, color='r', linestyle='--', label='π')
  plt.legend(loc='best')
  plt.show()

def main():
  param_N = os.environ.get('ITER')
  N = int(param_N) if param_N else 1000000
  plot_estimates(N)

if __name__ == "__main__":
  main()