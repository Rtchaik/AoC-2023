def solve_day(my_file):
  data = parse_data(my_file)
  result = [sum(items) for items in zip(*[find_next(line) for line in data])]
  print('Part 1: ', result[0])
  print('Part 2: ', result[1])


def parse_data(my_file):
  with open(my_file) as f:
    return tuple([int(num) for num in line.split()] for line in f.readlines())


def find_next(line):
  history = [line]
  while len(set(last := history[-1])) > 1:
    history.append([a - b for a, b in zip(last[1:], last)])
  history.reverse()
  first = history[0][0]
  last = history[0][-1]
  for item in history[1:]:
    first = item[0] - first
    last += item[-1]
  return first, last
