import Day01.solution as current

test1 = ['1abc2\n', 'pqr3stu8vwx\n', 'a1b2c3d4e5f\n', 'treb7uchet']
assert current.part1(test1) == 142

test2 = [
    'two1nine\n', 'eightwothree\n', 'abcone2threexyz\n', 'xtwone3four\n',
    '4nineeightseven2\n', 'zoneight234\n', '7pqrstsixteen'
]
assert current.part2(test2) == 281
