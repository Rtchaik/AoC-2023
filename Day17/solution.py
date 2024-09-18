import heapq
from dataclasses import dataclass


@dataclass
class Point:
  direct: int = 0
  steps: int = 0
  total: float = float('infinity')


def solve_day(my_file):
  data = parse_data(my_file)
  print('Part 1: ', part1(data))
  print('Part 2: ', part2(data))


def parse_data(my_file):
  with open(my_file) as f:
    return tuple(tuple(int(num) for num in list(line.strip())) for line in f.readlines())


def dijkstra(graph, start):
    dirs = ((0,1), (1,0), (0,-1), (-1,0))
    heats = {(y,x): Point() for y in range(len(graph)) for x in range(len(graph[0]))}
    heats[start].total = 0
    pq = [(0, start)]
    
    while pq:
        current_heat, current_point = heapq.heappop(pq)
        current_point_data = heats[current_point]

        if current_heat > current_point_data.total:
            continue

        for idx in (-1,0,1):
            direction = (current_point_data.direct + idx)%4
            new_point = tuple(sum(pair) for pair in zip(current_point, dirs[direction]))
            if new_point in heats and (idx!=0 or (idx==0 and current_point_data.steps<3)):
              new_heat = current_heat + graph[new_point[0]][new_point[1]]
              if new_heat < heats[new_point].total:
                  heats[new_point].total = new_heat
                  heats[new_point].direct = direction
                  if idx == 0:
                    heats[new_point].steps = 1+current_point_data.steps
                  else:
                    heats[new_point].steps = 1
                  heapq.heappush(pq, (new_heat, new_point))
    return heats


def part1(data):
  result = dijkstra(data, (0,0))
  for item in result:
    print(item, result[item])
  return 0#result[len(data)-1][len(data(0))-1]


def part2(data):
  return 0
