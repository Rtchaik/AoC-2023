from itertools import combinations

import numpy as np


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return np.array([['.#'.index(ch) for ch in line.strip()]
                     for line in f.readlines()])


def expand_universe(data, rate):
  row = [0]
  step = 1
  for idx in range(len(data) - 1):
    if np.all(data[idx] == 0):
      step += rate
    row.append(step + idx)
  return row


def distances(data, rate):
  cols = expand_universe(data, rate)
  rows = expand_universe(np.rot90(data, -1), rate)
  ones = np.where(data == 1)
  galaxies = list(zip([cols[c] for c in ones[0]], [rows[r] for r in ones[1]]))
  dist = 0
  for gal_1, gal_2 in combinations(galaxies, 2):
    dist += sum(abs(x1 - x2) for x1, x2 in zip(gal_1, gal_2))
  return dist


def part1(data):
  return distances(data, 2 - 1)


def part2(data):
  return distances(data, 1000000 - 1)
