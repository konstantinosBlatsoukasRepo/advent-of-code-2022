import re
from collections import deque
test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


# print(re.split('Monkey \d:\n', test_input))
# print(re.split('\n\n', test_input))

monkeys = []
inspected_items = []


class Monkey:
    def __init__(self, items, operation, is_divisible_by, true_false_mokeys_id):
        self.items = deque(items)
        self.operation = operation
        self.is_divisible_by = is_divisible_by
        self.true_monkey_id, self.false_monkey_id = true_false_mokeys_id

    def inspect_items(self):
        while self.items:
            item = self.items.popleft()
            new_worry_level = self.operation(item) // 3
            throw_monkey_id = self.true_monkey_id if new_worry_level % self.is_divisible_by == 0 else self.false_monkey_id
            monkeys[throw_monkey_id].items.append(new_worry_level)

    def inspect_items_no_div(self):
        while self.items:
            item = self.items.popleft()
            new_worry_level = self.operation(item)

            new_worry_level %= 19 * 3 * 13 * 7 * 5 * 11 * 17 * 2

            throw_monkey_id = self.true_monkey_id if new_worry_level % self.is_divisible_by == 0 else self.false_monkey_id
            monkeys[throw_monkey_id].items.append(new_worry_level)

    def __repr__(self):
        return repr(self.items)


def parse_operation(operation):
    if "*" in operation and bool(re.search('\d+', operation)):
        return lambda old: old * int(re.findall('\d+', operation)[0])
    elif "*" in operation:
        return lambda old: old * old
    elif "+" in operation and bool(re.search('\d+', operation)):
        return lambda old: old + int(re.findall('\d+', operation)[0])
    elif "+" in operation:
        return lambda old: old + old


def parse_input(input):
    monkeys_raw = input.split('\n\n')
    parsed_monkeys = []
    for monkey_raw in monkeys_raw:
        monkey_data = monkey_raw.splitlines()
        items = [int(item) for item in re.findall('\d+', monkey_data[1])]
        operation = parse_operation(monkey_data[2])

        is_divisible_by = int(re.findall('\d+', monkey_data[3])[0])

        true_monkey_id = int(re.findall('\d+', monkey_data[4])[0])
        false_monkey_id = int(re.findall('\d+', monkey_data[5])[0])

        parsed_monkeys.append(
            Monkey(items, operation, is_divisible_by, (true_monkey_id, false_monkey_id)))

    return parsed_monkeys


def perform_round():
    for monkey_id in range(len(monkeys)):
        inspected_items[monkey_id] += len(monkeys[monkey_id].items)
        monkeys[monkey_id].inspect_items()


def perform_round_no_div():
    for monkey_id in range(len(monkeys)):
        inspected_items[monkey_id] += len(monkeys[monkey_id].items)
        monkeys[monkey_id].inspect_items_no_div()


def part_one(input):
    monkeys.extend(parse_input(input))
    inspected_items.extend([0 for _ in range(len(monkeys))])

    for _ in range(20):
        perform_round()

    sorted_inspected_items = sorted(inspected_items)

    return sorted_inspected_items[-1] * sorted_inspected_items[-2]


def part_two(input):
    monkeys.extend(parse_input(input))
    inspected_items.extend([0 for _ in range(len(monkeys))])

    for i in range(10000):
        perform_round_no_div()

    sorted_inspected_items = sorted(inspected_items)
    return sorted_inspected_items[-1] * sorted_inspected_items[-2]


# print(part_one(test_input))
input = open("input.txt").read()
print(part_two(input))
