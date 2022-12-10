test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def update_tail_to_be_adj(head_pos, tail_pos, direction):
    if head_pos == tail_pos:
        return tail_pos

    head_row, head_col = head_pos
    tail_row, tail_col = tail_pos

    if direction == 'U':
        if head_col == tail_col:
            return (tail_row + (-1), tail_col)
        if tail_row != head_row and head_col > tail_col:
            return (tail_row + (-1), tail_col + 1)
        return (tail_row + (-1), tail_col - 1)

    elif direction == 'D':
        if head_col == tail_col:
            return (tail_row + 1, tail_col)
        if tail_row != head_row and head_col > tail_col:
            return (tail_row + 1, tail_col + 1)
        return (tail_row + 1, tail_col - 1)
    elif direction == 'R':
        if tail_row == head_row:
            return (tail_row, tail_col + 1)

        if tail_row != head_row and head_row > tail_row:
            return (tail_row + 1, tail_col + 1)
        return (tail_row - 1, tail_col + 1)
    elif direction == 'L':
        if tail_row == head_row:
            return (tail_row, tail_col - 1)

        if tail_row != head_row and head_row > tail_row:
            return (tail_row + 1, tail_col - 1)
        return (tail_row - 1, tail_col - 1)


def is_tail_adj_to_head(head_pos, tail_pos):
    head_row, head_col = head_pos
    adj_pos = [(head_row, head_col + 1), (head_row + 1, head_col + 1), (head_row + 1, head_col), (head_row - 1, head_col + 1),
               (head_row + 1, head_col - 1), (head_row, head_col - 1), (head_row - 1, head_col - 1), (head_row - 1, head_col)]

    return tail_pos in adj_pos


def update_head_and_tail(head_pos, tail_pos, direction):
    head_row, head_col = head_pos
    if direction == 'U':
        head_pos = (head_row - 1, head_col)
    elif direction == 'D':
        head_pos = (head_row + 1, head_col)
    elif direction == 'R':
        head_pos = (head_row, head_col + 1)
    elif direction == 'L':
        head_pos = (head_row, head_col - 1)

    if not is_tail_adj_to_head(head_pos, tail_pos):
        tail_pos = update_tail_to_be_adj(head_pos, tail_pos, direction)

    return head_pos, tail_pos


def part_one(input):
    head_moves = input.splitlines()
    head_pos = (0, 0)
    tail_pos = (0, 0)
    seen_tail_pos = set()
    for head_move in head_moves:
        direction, reps = head_move.split(' ')

        for _ in range(0, int(reps)):
            head_pos, tail_pos = update_head_and_tail(
                head_pos, tail_pos, direction)
            seen_tail_pos.add(tail_pos)

    return len(seen_tail_pos)

def part_two(input):
    knots_pos = [(0, 0) for _ in range(0, 9)]

    head_moves = input.splitlines()
    head_pos = (0, 0)
    tail_pos = (0, 0)
    seen_tail_pos = set()
    for head_move in head_moves:
        direction, reps = head_move.split(' ')

        for _ in range(0, int(reps)):
            head_pos, tail_pos = update_head_and_tail(
                head_pos, tail_pos, direction)
            
            knots_pos[0] = tail_pos
            for i in range(1, 9):
                head_pos, tail_pos = update_head_and_tail(
                knots_pos[i-1], knots_pos[i], direction)
                knots_pos[i] = tail_pos

            seen_tail_pos.add(knots_pos[8])


    return len(seen_tail_pos)


data = open("input.txt").read().strip()

print(part_two(data))