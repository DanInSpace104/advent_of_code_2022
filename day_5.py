from copy import deepcopy
from typing import List, Tuple

Vec3 = Tuple[int, int, int]


def part_one(stacks: List[List[str]], actions: List[Vec3]) -> str:
    def move(f, t):
        stacks[t].append(stacks[f].pop())

    for act in actions:
        for _ in range(act[0]):
            move(act[1] - 1, act[2] - 1)

    return ''.join([s[-1] for s in stacks])


def part_two(stacks: List[List[str]], actions: List[Vec3]) -> str:
    for act in actions:
        div = []
        for _ in range(act[0]):
            div.append(stacks[act[1] - 1].pop())
        stacks[act[2] - 1].extend(reversed(div))

    return ''.join([s[-1] for s in stacks])


def prepare_data(s: str) -> Tuple[List, List]:
    cargo, actions = s.split('\n\n')
    actions = [tuple(map(int, l.split()[1::2])) for l in actions.splitlines()]

    stacks = []
    cargo = cargo.splitlines()[:-1]
    stack_number = (len(cargo[-1]) + 1) // 4
    for n in range(stack_number):
        stack = []
        for i in range(len(cargo) - 1, -1, -1):
            char = cargo[i][n * 4 + 1]
            if char != ' ':
                stack.append(char)
        stacks.append(stack)
    return stacks, actions


test_input = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
stacks, actions = prepare_data(test_input[1:])

assert part_one(deepcopy(stacks), actions) == 'CMZ'
assert part_two(deepcopy(stacks), actions) == 'MCD'

with open('inputs/day_5.input') as fl:
    stacks, actions = prepare_data(fl.read())
    print(part_one(deepcopy(stacks), actions))
    print(part_two(deepcopy(stacks), actions))
