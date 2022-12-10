test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def part_one(input):
    instructions = input.splitlines()
    instruction_id = 0
    cycle = 1
    x_value = 1
    signal_strengh = {}
    while True:
        if cycle == 221:
            break

        curr_instruction__id = instruction_id % len(instructions)
        instruction = instructions[curr_instruction__id].split(' ')
        if instruction[0] == 'noop':
            cycle += 1
            signal_strengh[cycle] = x_value * cycle

        elif instruction[0] == 'addx':
            cycle += 1
            signal_strengh[cycle] = x_value * cycle

            cycle += 1
            x_value += int(instruction[1])
            signal_strengh[cycle] = x_value * cycle

        instruction_id = instruction_id + 1

    res = []
    for k in [20, 60, 100, 140, 180, 220]:
        res.append(signal_strengh[k])

    return sum(res)


def draw_pixel(position, sprite_position, pixels):
    if position in [sprite_position, sprite_position + 1, sprite_position + 2]:
        pixels.append('#')
    else:
        pixels.append('.')


def print_crt_row_if_complete(pixels, position):
    if position % 40 == 0:
        print("".join(pixels[position - 40:]))


def reset_position_if_row_complete(position):
    return position if position != 40 else 0


def update_cycle_and_position(cycle, position):
    cycle += 1
    position += 1
    position = reset_position_if_row_complete(position)
    return cycle, position


def part_two(input):
    instructions = input.splitlines()
    instruction_id = 0

    cycle, position, sprite_position = 1, 0, 0

    pixels = []
    while True:
        if cycle == 241:
            break

        curr_instruction__id = instruction_id % len(instructions)
        instruction = instructions[curr_instruction__id].split(' ')
        if instruction[0] == 'noop':
            draw_pixel(position, sprite_position, pixels)
            cycle, position = update_cycle_and_position(cycle, position)
            print_crt_row_if_complete(pixels, position)

        elif instruction[0] == 'addx':
            draw_pixel(position, sprite_position, pixels)
            cycle, position = update_cycle_and_position(cycle, position)
            print_crt_row_if_complete(pixels, position)

            draw_pixel(position, sprite_position, pixels)
            cycle, position = update_cycle_and_position(cycle, position)
            print_crt_row_if_complete(pixels, position)

            sprite_position = (sprite_position + int(instruction[1])) % 40

        instruction_id += 1


assert part_one(test_input) == 13140

input = open("input.txt").read().strip()

print(part_one(test_input))

print(part_one(input))
print(part_two(input))
