# part 1

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def sum_cals_per_elf(input):
    sum_cals_per_elf = []
    for group_cals in input.split('\n\n'):
        totalElfCals = sum([int(strCal) for strCal in group_cals.splitlines()])
        sum_cals_per_elf.append(totalElfCals)

    return sum_cals_per_elf

def part_one(input):
    return max(sum_cals_per_elf(input))

assert part_one(test_input) == 24000

def part_two(input):
    sums = sum_cals_per_elf(input)
    sums.sort(reverse=True)
    return sum(sums[:3])

assert part_two(test_input) == 45000


puzzle_input = open("input.txt", "r").read()

# part one solution
print(part_one(puzzle_input))

# part two solution
print(part_two(puzzle_input))