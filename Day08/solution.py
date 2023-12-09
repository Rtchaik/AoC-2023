import re
from itertools import cycle
from math import lcm


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    instr = [int('LR'.index(num)) for num in f.readline().strip()]
    next(f)
    nodes = [re.findall(r'\w+', node) for node in f.readlines()]
  nodes = {nod: values for nod, *values in nodes}
  return instr, nodes


def find_path(data, current):
  instr, nodes = data
  for total, idx in enumerate(cycle(instr), 1):
    current = nodes[current][idx]
    if current.endswith('Z'):
      return total


def part1(data):
  return find_path(data, 'AAA')


def part2(data):
  return lcm(
      *[find_path(data, item) for item in data[1] if item.endswith('A')])
