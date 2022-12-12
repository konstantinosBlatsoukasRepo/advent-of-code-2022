

from collections import deque
test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def parse(input):
    grid = [x for x in input.split('\n')]
    return len(grid), len(grid[0]), grid


def calculate_elevations(grid):
    elevations = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 'S':
                elevations[row][column] = 1
            elif grid[row][column] == 'E':
                elevations[row][column] = 26
            else:
                elevations[row][column] = ord(
                    grid[row][column]) - ord('a') + 1
    return elevations


def bfs(input, part):
    total_rows, total_columns, grid = parse(input)
    elevations = calculate_elevations(grid)

    print(grid)
    queue = deque()
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if (grid[row][column] == 'S' and part == 1) or (elevations[row][column] == 1 and part == 2):
                queue.append(((row, column), 0))

    seen = set()
    while queue:
        (row, column), dist = queue.popleft()

        if (row, column) in seen:
            continue

        if grid[row][column] == 'E':
            return dist

        seen.add((row, column))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr = row + dr
            cc = column + dc
            if 0 <= rr < total_rows and 0 <= cc < total_columns and elevations[rr][cc] <= 1 + elevations[row][column]:
                queue.append(((rr, cc), dist + 1))



input = open("input.txt").read()

print(bfs(input, 1))
print(bfs(input, 2))
