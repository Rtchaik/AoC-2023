import re


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return f.readlines()


def part1(data):
  result = 0
  for line in data:
    nums = re.findall(r'\d', line)
    result += int(nums[0] + nums[-1])
  return result


def part2(data):
  nums = {
      'one': 'o1e',
      'two': 't2o',
      'three': 't3e',
      'four': 'f4r',
      'five': 'f5e',
      'six': 's6x',
      'seven': 's7n',
      'eight': 'e8t',
      'nine': 'n9e'
  }
  result = []
  for line in data:
    for num in nums:
      line = re.sub(num, nums[num], line)
    result.append(line)
  return part1(result)
