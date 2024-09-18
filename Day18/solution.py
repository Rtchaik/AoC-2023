def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return tuple(line.split() for line in f.readlines())


def part1(data):
  dirs = {'R':(0,1), 'D':(1,0), 'L':(0,-1), 'U':(-1,0)}
  current = (0,0)
  digs = {current}
  for direct, steps, _ in data:
    for __ in range(int(steps)):
      current = (current[0] + dirs[direct][0], current[1] + dirs[direct][1])
      digs.add(current)
  return len(digs)
    
  return data


def part2(data):
  return 0
