from typing import List, Tuple

Pair = Tuple[int, int]


def get_pairs(line: str) -> Tuple[Pair, Pair]:
    p1, p2 = line.strip().split(',')
    p1 = tuple(map(int, p1.split('-')))
    p2 = tuple(map(int, p2.split('-')))
    return p1, p2


def part_one(pairs: List[str]) -> int:
    def check(c1: Pair, c2: Pair) -> bool:
        return c1[0] <= c2[0] and c1[1] >= c2[1]

    res = 0
    for line in pairs:
        p1, p2 = get_pairs(line)
        if check(p1, p2) or check(p2, p1):
            res += 1
    return res


def part_two(pairs: list[str]) -> int:
    def check(c1: Pair, c2: Pair) -> bool:
        return c1[1] >= c2[0] and c2[1] >= c1[0]

    res = 0
    for line in pairs:
        p1, p2 = get_pairs(line)
        if check(p1, p2) or check(p2, p1):
            res += 1
    return res


test_input = '''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''.strip().splitlines()


assert part_one(test_input) == 2
assert part_two(test_input) == 4

with open('inputs/day_4.input') as fl:
    lines = fl.readlines()
    print(part_one(lines))
    print(part_two(lines))
