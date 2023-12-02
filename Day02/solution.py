from functools import reduce
from operator import mul


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    games = []
    for line in f.readlines():
      _, final = line.split(': ')
      final = [{(vals := pair.split())[1]: int(vals[0])
                for pair in x.split(', ')} for x in final.split('; ')]
      games.append(final)
    return games


def part1(data):
  maxims = {'red': 12, 'green': 13, 'blue': 14}
  result = 0
  for idx, game in enumerate(data):
    valid = True
    for round in game:
      if any(v > maxims[k] for k, v in round.items()):
        valid = False
        break
    if valid:
      result += idx + 1
  return result


def part2(data):
  result = 0
  for game in data:
    minims = dict.fromkeys(('red', 'green', 'blue'), 0)
    for round in game:
      for col, val in round.items():
        minims[col] = max(minims[col], val)
    result += reduce(mul, minims.values())
  return result
