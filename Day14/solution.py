import numpy as np


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data.copy()))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return np.rot90(np.array([list(line.strip()) for line in f.readlines()]))


def tilting(data):
  for line in data:
    floor_idx = 0
    for idx,ch in enumerate(line):
      match ch:
        case '#':
          floor_idx = idx+1
        case 'O':
          line[idx] = '.'
          line[floor_idx] = 'O'
          floor_idx += 1
  return data

def north_load(data):
  return sum(sum(idx+1 for idx, ch in enumerate(reversed(line)) if ch == 'O') for line in data)

def part1(data):
  return north_load(tilting(data))

def hashing(data):
  return hash(tuple(tuple(line) for line in data))

def part2(data):
  spins = {}
  while True:
    for _ in range(4):
      data = np.rot90(tilting(data),-1)
    current = hashing(data)
    if current in spins:
      start = list(spins).index(current)
      break
    spins[current]=north_load(data)
  return list(spins.values())[(1000000000-start)%(len(spins)-start)-1+ start]
