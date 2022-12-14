
test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def parse_rocks(input):
    lines = input.splitlines()
    rocks = set()
    for line in lines:
        x_ys = [x.strip() for x in line.split("->")]

        for i in range(0, len(x_ys) - 1):
            from_x, from_y = x_ys[i].split(",")
            to_x, to_y = x_ys[i + 1].split(",")

            if from_x == to_x and int(from_y) > int(to_y):
                for i in range(int(to_y), int(from_y) + 1):
                    rocks.add((int(from_x), i))

            if from_x == to_x and int(from_y) < int(to_y):
                for i in range(int(from_y),  int(to_y) + 1):
                    rocks.add((int(from_x), i))

            if from_y == to_y and int(from_x) > int(to_x):
                for i in range(int(to_x), int(from_x) + 1):
                    rocks.add((i, int(from_y)))

            if from_y == to_y and int(from_x) < int(to_x):
                for i in range(int(from_x),  int(to_x) + 1):
                    rocks.add((i, int(from_y)))
    return rocks


def simulate(sand, rocks, rested_sands, constraints):
    sand_x, sand_y = sand
    max_y, max_x, min_x = constraints

    for dx, dy in (0, 1), (-1, 1), (1, 1):
        new_sand_y = sand_y + dy
        new_sand_x = sand_x + dx

        not_in_abyss = new_sand_y <= max_y and new_sand_x >= min_x and new_sand_x <= max_x
        new_sand = (new_sand_x, new_sand_y)
        if new_sand not in rocks and new_sand not in rested_sands and not_in_abyss:
            return [(sand_x + dx, sand_y + dy), False]

    return [(sand_x, sand_y), True]


def simulate_p2(sand, rocks, rested_sands, constraints):
    sand_x, sand_y = sand
    max_y, _, _ = constraints

    for dx, dy in (0, 1), (-1, 1), (1, 1):
        new_sand_y = sand_y + dy
        new_sand_x = sand_x + dx

        not_in_abyss = new_sand_y < max_y + 2
        new_sand = (new_sand_x, new_sand_y)
        if new_sand not in rocks and new_sand not in rested_sands and not_in_abyss:
            return [(sand_x + dx, sand_y + dy), False]

    return [(sand_x, sand_y), True]
    


def is_not_in_abyss(current_sand, constraints):
    sand_x, sand_y = current_sand
    max_y, max_x, min_x = constraints
    return sand_y < max_y and sand_x > min_x and sand_x < max_x


def is_not_in_abyss_p2(current_sand, constraints):
    _, sand_y = current_sand
    max_y, _, _ = constraints
    return sand_y < max_y + 2

def part_one(input):
    rocks = parse_rocks(input)
    rested_sands = set()

    max_y = max([y for _, y in rocks])
    max_x = max([x for x, _ in rocks])
    min_x = min([x for x, _ in rocks])

    constraints = (max_y, max_x, min_x)

    pouring_sand_x = 500
    pouring_sand_y = 0
    pouring_sand = (pouring_sand_x, pouring_sand_y)
    current_sand = pouring_sand

    while is_not_in_abyss(current_sand, constraints):
        [(new_sand_x, new_sand_y), is_rested] = simulate(
            current_sand, rocks, rested_sands, constraints)

        if is_rested and is_not_in_abyss((new_sand_x, new_sand_y), constraints):
            rested_sands.add((new_sand_x, new_sand_y))
            current_sand = pouring_sand
        elif not is_rested and is_not_in_abyss((new_sand_x, new_sand_y), constraints):
            current_sand = (new_sand_x, new_sand_y)
        elif not is_rested and not is_not_in_abyss((new_sand_x, new_sand_y), constraints):
            break

    return len(rested_sands)

def print_grid(max_y, max_x, min_x, rocks, rested_sands):
    for y in range(max_y + 1):
        row = []
        for x in range(min_x - 30, max_x + 30):
            if (x, y) in rocks:
                row.append("#")
            elif (x, y) in rested_sands:
                row.append("o")
            else:
                row.append(".")
        print(''.join(row))
    print('-----------------------------------------------')
    print('-----------------------------------------------')

def part_two(input):
    rocks = parse_rocks(input)
    rested_sands = set()

    max_y = max([y for _, y in rocks])
    max_x = max([x for x, _ in rocks])
    min_x = min([x for x, _ in rocks])

    constraints = (max_y, max_x, min_x)

    pouring_sand_x = 500
    pouring_sand_y = 0
    pouring_sand = (pouring_sand_x, pouring_sand_y)
    current_sand = pouring_sand

    while is_not_in_abyss_p2(current_sand, constraints):
        [(new_sand_x, new_sand_y), is_rested] = simulate_p2(
            current_sand, rocks, rested_sands, constraints)

        if is_rested and is_not_in_abyss_p2((new_sand_x, new_sand_y), constraints):
            rested_sands.add((new_sand_x, new_sand_y))
            current_sand = pouring_sand
            if new_sand_x == 500 and  new_sand_y == 0:
                return len(rested_sands)
        elif not is_rested and is_not_in_abyss_p2((new_sand_x, new_sand_y), constraints):
            current_sand = (new_sand_x, new_sand_y)
        elif not is_rested and not is_not_in_abyss_p2((new_sand_x, new_sand_y), constraints):
            break

    return len(rested_sands)



assert part_one(test_input) == 24
assert part_two(test_input) == 93

input = open("input.txt").read()

print(part_one(input))
print(part_two(input))

