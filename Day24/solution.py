def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return tuple(int(line) for line in f.readlines())


def part1(data):
  return data


def part2(data):
  return 0
