test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def parse_rucksacks(input):
    rucksacks = []
    for ruck in input.splitlines():
        mid_ruck = int(len(ruck)/2)
        first_compartment = ruck[0:mid_ruck]
        second_compartment = ruck[mid_ruck:]
        rucksack = [first_compartment, second_compartment]
        rucksacks.append(rucksack)
    return rucksacks

def parse_rucksacks_groups(input):
    rucksacks_groups = []
    raw = input.splitlines()
    start = 0
    while start != len(raw):
        rucksacks_groups.append([raw[start], raw[start + 1], raw[start + 2]])
        start += 3
    return rucksacks_groups

def get_common_compartments_items(rucksacks):
    common_items = []
    for first_compartment, second_compartment in rucksacks:
        cur_common_items = {item for item in first_compartment} & {
            item for item in second_compartment}
        common_items.extend(cur_common_items)
    return common_items

def get_budge_from(rucksacks_groups):
    budges = []
    for group_one, group_two, group_three in rucksacks_groups:
        budge = {item for item in group_one} & {item for item in group_two} & {item for item in group_three}
        budges.extend(budge)
    return budges

def part_one(input):
    rucksacks = parse_rucksacks(input)
    common_compartments_items = get_common_compartments_items(rucksacks)
    sum = 0
    for item in common_compartments_items:
        cur_priority = ord(item) - 38 if item.isupper() else ord(item) - 96
        sum += cur_priority

    return sum

def part_two(input):
    rucksacks_groups = parse_rucksacks_groups(input)
    budges = get_budge_from(rucksacks_groups)

    sum = 0
    for item in budges:
        cur_priority = ord(item) - 38 if item.isupper() else ord(item) - 96
        sum += cur_priority

    return sum
    
puzzle_input = open("input.txt", "r").read()

assert part_one(test_input) == 157
print(part_one(puzzle_input))

assert part_two(test_input) == 70
print(part_two(puzzle_input))