with open('inputs/day_1.input') as fl:
    input = fl.read()

elfs = [sum(map(int, elf.split())) for elf in input.split('\n\n')]


def part_one():
    print('The Elf with the most callories carrying', max(elfs), 'callories.')


def part_two():
    print(
        'Three Elves with the most callories carrying',
        sum(sorted(elfs)[-3:]),
        'in total.',
    )
