def load_input() -> str:
    with open('inputs/day_6.input') as fl:
        return fl.read()


def detect_marker(datastream: str, num: int):
    for i in range(num, len(datastream)):
        if len(set(datastream[i - num : i])) == num:
            return i


def part_one(datastream: str) -> int:
    return detect_marker(datastream, 4)


def part_two(datastream: str) -> int:
    return detect_marker(datastream, 14)


tests = (
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26),
)

for test in tests:
    assert part_one(test[0]) == test[1]
    assert part_two(test[0]) == test[2]

print(part_one(load_input()))
print(part_two(load_input()))
