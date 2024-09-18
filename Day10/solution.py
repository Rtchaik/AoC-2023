def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data)[0])
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return tuple(line.strip() for line in f.readlines())


def valid_neighbour(data, y, x):
  offset = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  moves = {
      '|': (0, 1),
      '-': (2, 3),
      'L': (0, 3),
      'J': (0, 2),
      '7': (1, 2),
      'F': (1, 3),
      'S': (0, 1, 2, 3),
      '.': tuple(),
      '^': tuple()
  }
  offsets = [offset[move] for move in moves[data[y][x]]]
  nods = [
      (ny, nx) for dy, dx in offsets
      if 0 <= (ny := y + dy) < len(data) and 0 <= (nx := x + dx) < len(data[0])
  ]
  for idx, node in enumerate(nods):
    if data[node[0]][node[1]] == '^':
      data[node[0]][node[1]] = '|' if offsets[idx][0] else '-'
  return nods


def find__start(data):
  for y, row in enumerate(data):
    for x, c in enumerate(row):
      if c == 'S':
        return (y, x)


def part1(data):
  start = find__start(data)
  visited = {start}
  new_neighbs = {
      node
      for node in valid_neighbour(data, *start)
      if start in valid_neighbour(data, *node)
  }
  while new_neighbs:
    visited.update(new_neighbs)
    new_neighbs = set().union(
        *[valid_neighbour(data, *node) for node in new_neighbs]) - visited
  return len(visited) // 2, visited


def part2(data):
  new_data = []
  for line in data:
    new_data.append(['^'] * (len(line) * 2 + 1))
    new_data.append(list('^' + '^'.join(line) + '^'))
  new_data.append(new_data[0].copy())
  _, loop = part1(new_data)
  tiles = set()
  for y, row in enumerate(new_data):
    for x, _ in enumerate(row):
      tiles.add((y, x))
  tiles -= loop
  nest = set()
  offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  while tiles:
    new = {tiles.pop()}
    visited = new.copy()
    is_nest = True
    while new:
      next_new = set()
      for y, x in new:
        current = {(ny, nx)
                   for dy, dx in offsets if 0 <= (ny := y + dy) < len(new_data)
                   and 0 <= (nx := x + dx) < len(new_data[0])}
        if len(current) < 4:
          is_nest = False
        current -= loop
        current -= visited
        next_new.update(current)
      visited.update(next_new)
      new = next_new
    if is_nest:
      nest.update(visited)
    tiles -= visited
  return sum(new_data[y][x] != '^' for y, x in nest)
