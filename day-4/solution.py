# Every section has a unique ID number, and
# each Elf is assigned a range of section IDs
# many of the assignments overlap


test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def parse_section_assignment_pairs(input):
    section_assignment_pairs = []
    for line in input.splitlines():
        first_p, second_p = line.split(',')

        first_from, first_to = first_p.split('-')
        second_from, second_to = second_p.split('-')

        first_assignment = [i for i in range(
            int(first_from), int(first_to) + 1)]
        second_assignment = [i for i in range(
            int(second_from), int(second_to) + 1)]
        section_assignment_pairs.append(
            [set(first_assignment), set(second_assignment)])

    return section_assignment_pairs


def are_fully_contained(assignment_pair):
    first_assignment, second_assignment = assignment_pair
    union = first_assignment.union(second_assignment)
    return union == first_assignment or union == second_assignment


def part_one(input):
    count = 0
    assignment_pairs = parse_section_assignment_pairs(input)
    for assignment_pair in assignment_pairs:
        if are_fully_contained(assignment_pair):
            count += 1
    return count


def are_assignments_intersect(assignment_pair):
    first_assignment, second_assignment = assignment_pair
    intersection = first_assignment.intersection(second_assignment)
    return len(intersection) != 0


def part_two(input):
    count = 0
    assignment_pairs = parse_section_assignment_pairs(input)
    for assignment_pair in assignment_pairs:
        if are_assignments_intersect(assignment_pair):
            count += 1
    return count


puzzle_input = open("input.txt", "r").read()


assert part_one(test_input) == 2
print(part_one(puzzle_input))

assert part_two(test_input) == 4
print(part_two(puzzle_input))
