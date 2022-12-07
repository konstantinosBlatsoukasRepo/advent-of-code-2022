test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def is_cd_and_ls_cmd(cmds, curr_cmd):
    cmd = cmds[curr_cmd].split(' ')
    if cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] != '..':
        return [True, cmd[2]]

    return [False, -1]


def is_cd_and_dots(cmds, curr_cmd):
    cmd = cmds[curr_cmd].split(' ')
    if cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] == '..':
        return True
    return False


def parse_contents(curr_cmd, current_folder, cmds, folder_id):
    while True:
        if curr_cmd == len(cmds):
            return curr_cmd

        cmd = cmds[curr_cmd].split(' ')
        if cmd[0] == 'dir':
            current_folder['childs'].append(folder_id + '/' + cmd[1])
            curr_cmd += 1
        elif cmd[0] != 'dir' and cmd[0] != '$':
            current_folder['contents'].append((int(cmd[0]), cmd[1]))
            curr_cmd += 1
        else:
            return curr_cmd


def calculate_folder_size(dir_tree, folder_id):
    sum_dir = 0
    sum_dir = sum([file_size for file_size,
                  _ in dir_tree[folder_id]['contents']])
    for child_id in dir_tree[folder_id]['childs']:
        sum_dir += calculate_folder_size(dir_tree, child_id)

    return sum_dir


def parse_sys_dir_tree(input):
    dir_tree = {}
    cmds = input.splitlines()
    curr_cmd = 0
    path = []
    while curr_cmd < len(cmds):
        is_cd_and_ls, folder_name = is_cd_and_ls_cmd(cmds, curr_cmd)

        if is_cd_and_ls:
            path.append(folder_name)
            folder_id = '/'.join(path)
            dir_tree[folder_id] = {'childs': [], 'contents': []}
            curr_cmd += 2
            curr_cmd = parse_contents(
                curr_cmd, dir_tree[folder_id], cmds, folder_id)
        elif is_cd_and_dots(cmds, curr_cmd):
            path.pop()
            curr_cmd += 1

    for folder_id in dir_tree.keys():
        dir_tree[folder_id]['total_folder_size'] = calculate_folder_size(
            dir_tree, folder_id)
    return dir_tree


def part_one(input):
    dir_tree = parse_sys_dir_tree(input)

    size_less = 0
    for folder_id in dir_tree.keys():
        if dir_tree[folder_id]['total_folder_size'] <= 100000:
            size_less += dir_tree[folder_id]['total_folder_size']

    return size_less


def part_two(input):
    dir_tree = parse_sys_dir_tree(input)
    current_free_space = 70000000 - dir_tree['/']['total_folder_size']

    sorted_sizes = [vals['total_folder_size'] for k, vals in dir_tree.items()]
    sorted_sizes.sort()

    for sorted_size in sorted_sizes:
        if current_free_space + sorted_size >= 30000000:
            return sorted_size


puzzle_input = open("input.txt", "r").read()

assert part_one(test_input) == 95437
print(part_one(puzzle_input))

assert part_two(test_input) == 24933642
print(part_two(puzzle_input))
