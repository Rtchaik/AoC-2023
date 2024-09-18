import re
from contextlib import suppress
from functools import reduce


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return tuple(f.read().split(','))


def holiday_hash(word):
  return reduce(lambda x, y: (x + ord(y)) * 17 % 256, word, 0)


def part1(data):
  return sum(holiday_hash(word) for word in data)


def part2(data):
  boxes = [{} for _ in range(256)]
  for seq in data:
    label, op, num = re.fullmatch(r'(\w+)([-=])(\d)?', seq).groups()
    if op == '=':
      boxes[holiday_hash(label)][label] = num
    else:
      with suppress(KeyError):
        del boxes[holiday_hash(label)][label]
  return sum(
      sum(idx1 * idx2 * int(lens[1])
          for idx2, lens in enumerate(box.items(), 1))
      for idx1, box in enumerate(boxes, 1))
