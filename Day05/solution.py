from operator import itemgetter


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    result = tuple(
        sorted(([int(num) for num in lines.split()]
                for lines in part.split(':')[1].strip().split('\n')),
               key=itemgetter(1)) for part in f.read().split('\n\n'))
    for trans in result[1:]:
      for item in trans:
        dest, source, step = item
        item[0] = source
        item[1] = source + step
        item[2] = dest - source
    return result


def find_location(seeds, data):
  for trans in data:
    new_seeds = []
    for seed in seeds:
      for start, finish, move in trans:
        if seed[0] < start:
          if seed[1] <= start:
            new_seeds.append(seed)
            seed = 0
            break
          else:
            new_seeds.append([seed[0], start])
            seed[0] = start
        if start <= seed[0] < finish:
          new_seeds.append([seed[0] + move, min(seed[1], finish) + move])
          if seed[1] <= finish:
            seed = 0
            break
          else:
            seed[0] = finish
      if seed:
        new_seeds.append(seed)
    seeds = new_seeds
  return min(seeds)[0]


def part1(data):
  seeds = [[num, num + 1] for num in data[0][0]]
  return find_location(seeds, data[1:])


def part2(data):
  seeds = data[0][0]
  seeds = [[seeds[num], seeds[num] + seeds[num + 1]]
           for num in range(0,
                            len(seeds) - 1, 2)]
  return find_location(seeds, data[1:])
