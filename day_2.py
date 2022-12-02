with open('inputs/day_2.input') as fl:
    lines = fl.readlines()


def part_one():
    '''
    A - Rock - X
    B - Paper - Y
    C - Scissors - Z
    '''
    values = {
        'X': {'C': 6, 'A': 3, 'B': 0, 'val': 1},
        'Y': {'C': 0, 'A': 6, 'B': 3, 'val': 2},
        'Z': {'C': 3, 'A': 0, 'B': 6, 'val': 3},
    }
    res = 0
    for line in lines:
        op, me = line.split()
        res += values[me][op] + values[me]['val']
    print(res)


def part_two():
    '''
    X - Must Loose
    Y - Must Draw
    Z - Must Win
    '''
    points = {'X': 0, 'Y': 3, 'Z': 6}
    vals = {
        'A': {'X': 'C', 'Y': 'A', 'Z': 'B', 'val': 1},
        'B': {'X': 'A', 'Y': 'B', 'Z': 'C', 'val': 2},
        'C': {'X': 'B', 'Y': 'C', 'Z': 'A', 'val': 3},
    }
    res = 0
    for line in lines:
        op, end = line.split()
        my = vals[op][end]
        res += vals[my]['val'] + points[end]
    print(res)
