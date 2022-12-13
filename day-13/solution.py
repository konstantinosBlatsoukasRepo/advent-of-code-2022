import functools
test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parse(input):
    pairs = []
    unparsed_pairs = input.split("\n\n")
    for unparsed_pair in unparsed_pairs:
        left_part, right_part = unparsed_pair.split("\n")
        pairs.append([eval(left_part), eval(right_part)])
    return pairs


def is_right_order(left_part_ele, right_part_ele):
    if type(left_part_ele) is int and type(right_part_ele) is int and left_part_ele < right_part_ele:
        return 1
    elif type(left_part_ele) is int and type(right_part_ele) is int and left_part_ele > right_part_ele:
        return -1
    elif type(left_part_ele) is int and type(right_part_ele) is int:
        return 0
    elif type(left_part_ele) is list and type(right_part_ele) is int:
        return is_right_order(left_part_ele, [right_part_ele])
    elif type(left_part_ele) is int and type(right_part_ele) is list:
        return is_right_order([left_part_ele], right_part_ele)
    elif type(left_part_ele) is list and type(right_part_ele) is list:
        reps = len(left_part_ele) if len(left_part_ele) > len(
            right_part_ele) else len(right_part_ele)
        for i in range(reps):
            if i > len(left_part_ele) - 1:
                return 1
            if i > len(right_part_ele) - 1:
                return -1

            if type(left_part_ele[i]) is int and type(right_part_ele[i]) is int and left_part_ele[i] < right_part_ele[i]:
                return 1

            if type(left_part_ele[i]) is int and type(right_part_ele[i]) is int and left_part_ele[i] > right_part_ele[i]:
                return -1

            res = is_right_order(left_part_ele[i], right_part_ele[i])
            if res == 0:
                continue

            if res == 1 or res == -1:
                return res


def part_one(input):
    orders = []

    pairs = parse(input)
    for left_part, right_part in pairs:
        orders.append(is_right_order(left_part, right_part))

    return sum([i + 1 for i in range(len(orders)) if orders[i] == 1])


def part_two(input):
    all_inputs = [[[2]], [[6]]]
    pairs = parse(input)
    for left_part, right_part in pairs:
        all_inputs.append(left_part)
        all_inputs.append(right_part)

    all_inputs = sorted(all_inputs, key=functools.cmp_to_key(is_right_order))[::-1]
    indices = []
    for i, val in enumerate(all_inputs):
        if val == [[2]] or val == [[6]]:
            indices.append(i + 1)
            
    
    return indices[0] * indices[1]


assert part_one(test_input) == 13
assert part_two(test_input) == 140

input = open("input.txt").read()

print(part_one(input))
print(part_two(input))
