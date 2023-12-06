from functools import reduce
from operator import mul


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return [line.split(':')[1].split() for line in f.readlines()]


def binomial_search(n, x):
  low = 0
  high = n // 2
  while low < high:
    mid = (low + high) // 2
    if mid * (n - mid) <= x:
      low = mid + 1
    else:
      high = mid
  ways = (n // 2 - high + 1) * 2
  return ways if n % 2 else ways - 1


def part1(data):
  data = zip(*[[int(race) for race in line] for line in data])
  return reduce(mul, (binomial_search(t, win) for t, win in data))


def part2(data):
  return binomial_search(*[int(''.join(line)) for line in data])
