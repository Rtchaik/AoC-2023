def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    res = [[{int(x)
             for x in side.split()} for side in line.split(': ')[1].split('|')]
           for line in f.readlines()]
    return [len(x & y) for x, y in res]


def part1(data):
  return sum(2**(num - 1) for num in data if num > 0)


def part2(data):
  cards = [1] * len(data)
  for idx, card in enumerate(cards):
    for x in range(1, data[idx] + 1):
      cards[idx + x] += card
  return sum(cards)
