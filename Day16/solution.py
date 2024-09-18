def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return tuple(line.strip() for line in f.readlines())


def part1(data, start=((0,0),'E')):
  dirs= {'E': (0,1), 'S': (1,0), 'W': (0,-1), 'N': (-1,0)}
  maxims = (len(data), len(data[0]))
  beams={start}
  visited = beams
  while beams:
    new_beams = set()
    for coord,dir in beams:
      new_dirs = []
      match data[coord[0]][coord[1]]:
        case '/': new_dirs.append('NESW'['ENWS'.index(dir)])
        case '\\': new_dirs.append('NESW'['WSEN'.index(dir)])
        case '|' if dir in 'WE':
            new_dirs.extend(['N','S'])
        case '-' if dir in 'NS':
            new_dirs.extend(['W','E'])
        case _: new_dirs.append(dir)
      new_beams |= {tuple((tuple(c1+c2 for c1,c2 in zip(coord,dirs[new])),new)) for new in new_dirs}
    new_beams = {beam for beam in new_beams if beam[0][0] in range(maxims[0]) and beam[0][1] in range(maxims[1])} - visited
    visited |= new_beams
    beams = new_beams
  return len({coord for coord, _ in visited})


def part2(data):
  starts = set([((0,x),'S') for x in range(len(data[0]))]+[((len(data)-1,x),'N') for x in range(len(data[0]))]+[((y,0),'E') for y in range(len(data))]+[((y,len(data[0])-1),'W') for y in range(len(data))])
  return max(part1(data,start) for start in starts)
