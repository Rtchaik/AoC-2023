import Day03.solution as current

test1 = [
    '467..114..', '...*......', '..35..633.', '......#...', '617*......',
    '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..'
]
total, gears = current.part1(test1)
assert total == 4361
assert current.part2(gears) == 467835
