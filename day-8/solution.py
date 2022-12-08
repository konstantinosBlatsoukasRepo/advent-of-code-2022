test_input = """30373
25512
65332
33549
35390"""


def is_visible_and_calc_score(row, column, tree__map, is_part_one=True):
    # up
    up_row = row - 1
    is_visible_from_up = True
    up_score = 0
    while up_row >= 0:
        up_score += 1
        if tree__map[up_row][column] >= tree__map[row][column]:
            is_visible_from_up = False
            break
        up_row -= 1

    if is_part_one and is_visible_from_up:
        return True

    # bottom
    bottom_row = row + 1
    is_visible_from_bottom = True
    bottom_score = 0
    while bottom_row < len(tree__map):
        bottom_score += 1
        if tree__map[bottom_row][column] >= tree__map[row][column]:
            is_visible_from_bottom = False
            break
        bottom_row += 1

    if is_part_one and is_visible_from_bottom:
        return True

    # right
    right_column = column + 1
    is_visible_from_right = True
    right_score = 0
    while right_column < len(tree__map[0]):
        right_score += 1
        if tree__map[row][right_column] >= tree__map[row][column]:
            is_visible_from_right = False
            break

        right_column += 1

    if is_part_one and is_visible_from_right:
        return True

    # left
    left_column = column - 1
    is_visible_from_left = True
    left_score = 0
    while left_column >= 0:
        left_score += 1
        if tree__map[row][left_column] >= tree__map[row][column]:
            is_visible_from_left = False
            break
        left_column -= 1

    if is_part_one and is_visible_from_left:
        return True

    if is_part_one:
        return False

    return left_score * right_score * bottom_score * up_score


def part_one(input):
    tree__map = input.splitlines()
    count = 0
    for row in range(1, len(tree__map) - 1):
        for column in range(1, len(tree__map[0]) - 1):
            if is_visible_and_calc_score(row, column, tree__map):
                count += 1

    visible_perimeter_trees = (2 * len(tree__map) + 2 * len(tree__map[0])) - 4

    return visible_perimeter_trees + count


def part_two(input):
    tree__map = input.splitlines()
    scores = []
    for row in range(1, len(tree__map) - 1):
        for column in range(1, len(tree__map[0]) - 1):
            score = is_visible_and_calc_score(row, column, tree__map, False)
            scores.append(score)

    return max(scores)


puzzle_input = open("input.txt", "r").read()

assert part_one(test_input) == 21
print(part_one(puzzle_input))

assert part_two(test_input) == 8
print(part_two(puzzle_input))
