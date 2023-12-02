import Day02.solution as current

test1 = [[{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}], [{'blue': 1, 'green': 2}, {'green': 3, 'blue': 4, 'red': 1}, {'green': 1, 'blue': 1}], [{'green': 8, 'blue': 6, 'red': 20}, {'blue': 5, 'red': 4, 'green': 13}, {'green': 5, 'red': 1}], [{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}], [{'red': 6, 'blue': 1, 'green': 3}, {'blue': 2, 'red': 1, 'green': 2}]]

assert current.part1(test1) == 8
assert current.part2(test1) == 2286
