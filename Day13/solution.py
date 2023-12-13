import numpy as np


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return [
        np.array([['.#'.index(ch) for ch in line]
                  for line in pat.splitlines()])
        for pat in f.read().split('\n\n')
    ]


def find_mirrors(pattern, mode):
  for axis in (100, 1):
    for row in range(1, len(pattern)):
      if sum((pattern[row + idx] != pattern[row - idx - 1]).sum()
             for idx in range(min(row,
                                  len(pattern) - row))) == mode:
        return row * axis
    pattern = np.rot90(pattern, -1)


def part1(data, mode=0):
  return sum(find_mirrors(pat, mode) for pat in data)


def part2(data):
  return part1(data, 1)
