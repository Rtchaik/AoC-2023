from collections import defaultdict
from operator import mul


def solve_day(my_file):
  data = parse_data(my_file)
  total, gears = part1(data)
  print('Part 1: ', total)
  print('Part 2: ', part2(gears))


def parse_data(my_file):
  with open(my_file) as f:
    return [line.strip() for line in f.readlines()]


def find_neighbours(x, y, grid):
  neighbours = set()
  gear = set()
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if dx == 0 and dy == 0:
        continue
      nx = x + dx
      ny = y + dy
      if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
        symbol = grid[nx][ny]
        neighbours.add(symbol)
        if symbol == '*':
          gear.add((nx, ny))
  return neighbours, gear


def part1(data):
  total = 0
  current = ''
  neighbours = set()
  cur_gear = set()
  gears = defaultdict(set)
  for y in range(len(data)):
    for x in range(len(data[0])):
      if data[y][x].isdigit():
        current += data[y][x]
        new_neighbours, new_gears = find_neighbours(y, x, data)
        neighbours |= new_neighbours
        cur_gear |= new_gears
      else:
        if current:
          if len(neighbours - set(current)) > 1:
            current_int = int(current)
            total += current_int
            for g in cur_gear:
              gears[g].add(current_int)
            cur_gear = set()
          current = ''
          neighbours = set()
  return total, gears


def part2(data):
  return sum(mul(*v) for v in data.values() if len(v) > 1)
