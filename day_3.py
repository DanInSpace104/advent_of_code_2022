import itertools
import string
from typing import List


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def part_one(rucksacks: List[str]):
    sum = 0
    for sack in rucksacks:
        mid = len(sack) // 2
        for char in sack[:mid]:
            if char in sack[mid:]:
                sum += string.ascii_letters.index(char) + 1
                break
    return sum


def part_two(rucksacks: List[str]):
    sum = 0
    for group in grouper(3, rucksacks, ''):
        sacks = list(map(tuple, group))
        for char in sacks[0]:
            if char in sacks[1] and char in sacks[2]:
                sum += string.ascii_letters.index(char) + 1
                break
    return sum


test_input = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''.strip().splitlines()

assert part_one(test_input) == 157
assert part_two(test_input) == 70

with open('inputs/day_3.input') as fl:
    rucksacks = fl.readlines()

print(part_one(rucksacks), part_two(rucksacks))
