from collections import Counter


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    table = str.maketrans('AKQJT', 'EDCBA')
    return tuple([(pair := line.split())[0].translate(table),
                  int(pair[1])] for line in f.readlines())


def part1(data):
  types = {key: [] for key in ['11111', '2111', '221', '311', '32', '41', '5']}
  for hand in data:
    wild = 0
    counts = Counter(hand[0])
    if '1' in counts and len(counts) > 1:
      wild = counts.pop('1')
    counts = sorted(counts.values(), reverse=True)
    counts[0] += wild
    current_type = ''.join(str(ch) for ch in counts)
    types[current_type].append(hand)
  for key in types:
    types[key].sort()
  winners = sum(types.values(), [])
  return sum(hand[1] * (idx + 1) for idx, hand in enumerate(winners))


def part2(data):
  for hand in data:
    if 'B' in hand[0]:
      hand[0] = hand[0].replace('B', '1')
  return part1(data)
