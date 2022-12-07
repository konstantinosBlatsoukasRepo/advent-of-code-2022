import re


test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def parse_crates_line(line):
    end = len(line)
    start = end - 3
    line_crates = []
    while start >= 0:

        curr_crate = line[start:end].strip()
        if curr_crate == '':
            line_crates.append(curr_crate)
        else:
            line_crates.append(curr_crate[1:2])

        end -= 4
        start = end - 3
    return line_crates


def parse_crates(crates_input):
    crates_input = crates_input.splitlines()
    stacks = []

    for curr_crate_line in range(0, len(crates_input) - 1):
        parsed_line = parse_crates_line(crates_input[curr_crate_line])

        if len(stacks) == 0:
            total_stacks = len(parsed_line)
            stacks = [[] for i in range(0, total_stacks)]

        for stack_index in range(0, len(stacks)):
            stacks[stack_index].append(parsed_line[stack_index])

    for stack_index in range(0, len(stacks)):
        stacks[stack_index] = stacks[stack_index][::-1]
        stacks[stack_index] = [
            crate for crate in stacks[stack_index] if crate != '']

    return stacks[::-1]


def parse_moves(moves_input):
    moves_input = moves_input.splitlines()
    moves = []
    for moves_input in moves_input:
        total_moves, from_crate_id, to_crate_id = re.findall(
            '\d+', moves_input)
        moves.append((int(total_moves), int(from_crate_id), int(to_crate_id)))

    return moves


def parse(input):
    crates_input, moves_input = input.split('\n\n')
    return parse_crates(crates_input), parse_moves(moves_input)


def part_one(input):
    stacks, moves = parse(input)
    for total_moves, from_crate_id, to_crate_id in moves:
        for _ in range(0, total_moves):
            poped_crate = stacks[from_crate_id - 1].pop()
            stacks[to_crate_id - 1].append(poped_crate)

    res = []
    for stack in stacks:
        res.append(stack[-1])

    return "".join(res)


def part_two(input):
    stacks, moves = parse(input)
    for total_moves, from_crate_id, to_crate_id in moves:

        crates_to_move = []
        for _ in range(0, total_moves):
            crates_to_move.append(stacks[from_crate_id - 1].pop())

        stacks[to_crate_id - 1].extend(crates_to_move[::-1])

    res = []
    for stack in stacks:
        res.append(stack[-1])

    return "".join(res)


puzzle_input = open("input.txt", "r").read()

assert part_one(test_input) == "CMZ"
print(part_one(puzzle_input))

assert part_two(test_input) == "MCD"
print(part_two(puzzle_input))
