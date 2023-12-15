from functools import cache


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    result = []
    for line in f.readlines():
      row, nums = line.split()
      nums = tuple(int(num) for num in nums.split(','))
      result.append((row, nums))
    return result


@cache
def springs_finder(row, nums):
  next_part = nums[1:]
  springs = (f"{spr*'.'}{'#'*nums[0]}."
             for spr in range(len(row) - sum(nums) - len(next_part)))
  valid = (len(spr) for spr in springs
           if all(r in (c, '?') for r, c in zip(row, spr)))
  return sum(springs_finder(row[v:], next_part)
             for v in valid) if next_part else sum('#' not in row[v:]
                                                   for v in valid)


def part1(data):
  return sum(springs_finder(r + '.', n) for r, n in data)


def part2(data):
  return part1((('?'.join([r] * 5), n * 5) for r, n in data))
