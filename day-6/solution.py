

def start_of_distinct_chars(input, n):
    for i in range(0, len(input)):
        if len(set(list(input[i:i+n]))) == n:
            return i + n


def part_one(input):
    return start_of_distinct_chars(input, 4)


def part_two(input):
    return start_of_distinct_chars(input, 14)


assert part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert part_one("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert part_one("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert part_one("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert part_one("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

assert part_two("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
assert part_two("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
assert part_two("nppdvjthqldpwncqszvftbrmjlhg") == 23
assert part_two("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
assert part_two("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26

puzzle_input = open("input.txt", "r").read()

print(part_one(puzzle_input))
print(part_two(puzzle_input))
