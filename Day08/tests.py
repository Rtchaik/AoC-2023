import Day08.solution as current

test1 = ([0, 0, 1], {'AAA': ['BBB', 'BBB'], 'BBB': ['AAA', 'ZZZ'], 'ZZZ': ['ZZZ', 'ZZZ']})
assert current.part1(test1) == 6

test2 = ([0, 1], {'11A': ['11B', 'XXX'], '11B': ['XXX', '11Z'], '11Z': ['11B', 'XXX'], '22A': ['22B', 'XXX'], '22B': ['22C', '22C'], '22C': ['22Z', '22Z'], '22Z': ['22B', '22B'], 'XXX': ['XXX', 'XXX']})
assert current.part2(test2) == 6
