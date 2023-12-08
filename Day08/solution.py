import re
from math import lcm


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    instr, nodes = f.read().split('\n\n')
  table = str.maketrans('LR', '01')
  instr = [int(num) for num in instr.translate(table)]
  nodes = [re.findall(r'\w+', node) for node in nodes.split('\n')]
  nodes = {nod[0]: [nod[1], nod[2]] for nod in nodes}
  return instr, nodes


def find_path(data, current):
  instr, nodes = data
  pos = 0
  total = len(instr)
  while not current.endswith('Z'):
    current = nodes[current][instr[pos % total]]
    pos += 1
  return pos


def part1(data):
  return find_path(data, 'AAA')


def part2(data):
  return lcm(
      *[find_path(data, item) for item in data[1] if item.endswith('A')])
