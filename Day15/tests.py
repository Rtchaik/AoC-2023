import Day15.solution as current

test1 = ('rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7')
assert current.part1(test1) == 1320
assert current.part2(test1) == 145
